"""
ncrtxt49 - HTML 数字字符引用转换工具

该包提供将 HTML 数字字符引用转换为对应 Unicode 字符的功能。
"""

from .converter import convert_html_entities, convert_file

__all__ = ['convert_html_entities', 'convert_file']

__version__ = '2026.01.15.121313'
