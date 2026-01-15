"""
HTML 数字字符引用转换器

该模块提供将 HTML 数字字符引用转换为对应 Unicode 字符的功能。
支持十进制格式（如 &#65;）和十六进制格式（如 &#x41;）。
"""

import re
import html


def convert_html_entities(text: str) -> str:
    """
    将文本中的 HTML 数字字符引用转换为对应的 Unicode 字符。

    该函数使用 Python 标准库的 html.unescape 方法，它可以正确处理：
    - 十进制格式：&#65; → A
    - 十六进制格式：&#x41; → A
    - 命名实体：&amp; → &

    Args:
        text (str): 包含 HTML 数字字符引用的原始文本

    Returns:
        str: 转换后的文本，其中所有 HTML 实体都已转换为对应的字符

    Example:
        >>> convert_html_entities("Hello &#65; &#x42;")
        'Hello A B'
        >>> convert_html_entities("&#65;&#66;&#67;")
        'ABC'
    """
    # 使用 Python 标准库的 html.unescape 进行转换
    # 该方法可以正确处理十进制、十六进制和命名实体
    return html.unescape(text)


def convert_file(input_path: str, output_path: str) -> None:
    """
    读取输入文件，转换其中的 HTML 数字字符引用，并将结果写入输出文件。

    Args:
        input_path (str): 输入文件的路径
        output_path (str): 输出文件的路径（如果文件已存在将被覆盖）

    Raises:
        FileNotFoundError: 当输入文件不存在时
        IOError: 当文件读取或写入失败时
    """
    # 读取输入文件
    with open(input_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    # 转换内容
    converted_content = convert_html_entities(content)

    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(converted_content)