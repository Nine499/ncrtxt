"""数字字符引用转换核心功能"""

import re
from pathlib import Path
from typing import Union

# 预编译正则表达式，避免每次调用时重复编译
_DECIMAL_PATTERN = re.compile(r"&#(\d+);")
_HEX_PATTERN = re.compile(r"&#[xX]([0-9a-fA-F]+);")


def convert_html_entities(text: str) -> str:
    """转换HTML数字字符引用为对应字符

    支持十进制（&#1234;）和十六进制（&#x1F600; 或 &#X1F600;）格式的数字字符引用

    Args:
        text: 包含数字字符引用的文本

    Returns:
        转换后的文本

    Examples:
        >>> convert_html_entities('&#18487;')
        '䠷'
        >>> convert_html_entities('&#x4E2D;')
        '中'
    """

    def replace_decimal(match):
        code_point = int(match.group(1))
        try:
            return chr(code_point)
        except (ValueError, OverflowError):
            return match.group(0)

    def replace_hex(match):
        code_point = int(match.group(1), 16)
        try:
            return chr(code_point)
        except (ValueError, OverflowError):
            return match.group(0)

    # 先处理十六进制引用
    text = _HEX_PATTERN.sub(replace_hex, text)
    # 再处理十进制引用
    text = _DECIMAL_PATTERN.sub(replace_decimal, text)

    return text


def convert_file(input_file: Union[str, Path], output_file: Union[str, Path]) -> None:
    """转换文件中的数字字符引用

    读取输入文件，转换其中的数字字符引用，并写入输出文件

    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径

    Raises:
        FileNotFoundError: 输入文件不存在
        UnicodeDecodeError: 文件编码问题
        OSError: 文件读写权限问题

    Examples:
        >>> convert_file('input.txt', 'output.txt')
    """
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    try:
        # 读取输入文件
        content = input_path.read_text(encoding="utf-8")

        # 转换内容
        converted_content = convert_html_entities(content)

        # 写入输出文件
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(converted_content, encoding="utf-8")

    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(
            e.encoding,
            e.object,
            e.start,
            e.end,
            f"无法解码文件 {input_path}，请确保文件使用UTF-8编码",
        ) from e
    except OSError as e:
        raise OSError(f"文件操作错误: {e}") from e
