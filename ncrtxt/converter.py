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


def _find_incomplete_entity(text: str, max_len: int = 12) -> int:
    """查找文本末尾可能不完整的数字字符引用

    Args:
        text: 要检查的文本
        max_len: 实体最大长度（&#1114111; 或 &#x10FFFF; 约10字符）

    Returns:
        不完整实体的起始位置，未找到返回 -1
    """
    # 只检查末尾 max_len 个字符
    search_start = max(0, len(text) - max_len)
    pos = text.rfind("&#", search_start)
    if pos == -1:
        return -1
    # 如果后面有分号，说明实体是完整的
    if ";" in text[pos:]:
        return -1
    return pos


def convert_file(
    input_file: Union[str, Path],
    output_file: Union[str, Path],
    chunk_size: int = 1024 * 1024,
) -> None:
    """转换文件中的数字字符引用（流式处理，支持大文件）

    读取输入文件，转换其中的数字字符引用，并写入输出文件。
    使用流式处理，内存占用与文件大小无关。

    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径
        chunk_size: 每次读取的块大小（字符数），默认 1MB

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
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with (
            open(input_path, "r", encoding="utf-8") as infile,
            open(output_path, "w", encoding="utf-8") as outfile,
        ):
            buffer = ""

            while True:
                chunk = infile.read(chunk_size)
                if not chunk:
                    # 处理剩余缓冲区
                    if buffer:
                        outfile.write(convert_html_entities(buffer))
                    break

                # 合并缓冲区和新块
                data = buffer + chunk
                buffer = ""

                # 检查末尾是否有不完整的实体
                incomplete_pos = _find_incomplete_entity(data)
                if incomplete_pos != -1:
                    buffer = data[incomplete_pos:]
                    data = data[:incomplete_pos]

                # 处理并写入完整部分
                if data:
                    outfile.write(convert_html_entities(data))

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
