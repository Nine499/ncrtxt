"""
命令行接口模块

该模块提供 ncrtxt49 工具的命令行接口，用于将 HTML 数字字符引用转换为 Unicode 字符。
"""

import argparse
import sys
from pathlib import Path
from .converter import convert_file


def main() -> None:
    """
    主函数：处理命令行参数并执行转换操作。

    命令行格式：
        ncrtxt49 <输入文件路径> <输出文件路径>

    参数说明：
        输入文件路径：已存在的原始文件
        输出文件路径：目标文件（如果已存在将被覆盖，如果不存在将被创建）
    """
    # 创建参数解析器
    parser = argparse.ArgumentParser(
        description='将 HTML 数字字符引用转换为对应的 Unicode 字符',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  ncrtxt49 input.txt output.txt
  ncrtxt49 /path/to/input.html /path/to/output.txt

支持的格式:
  十进制格式: &#65; → A
  十六进制格式: &#x41; → A
  命名实体: &amp; → &
        '''
    )

    # 添加位置参数
    parser.add_argument(
        'input_file',
        help='输入文件路径（包含 HTML 数字字符引用的文件）'
    )
    parser.add_argument(
        'output_file',
        help='输出文件路径（转换后的文件）'
    )

    # 解析参数
    args = parser.parse_args()

    # 验证输入文件是否存在
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f'错误: 输入文件 "{args.input_file}" 不存在', file=sys.stderr)
        sys.exit(1)

    if not input_path.is_file():
        print(f'错误: "{args.input_file}" 不是文件', file=sys.stderr)
        sys.exit(1)

    # 执行转换
    try:
        convert_file(str(input_path), args.output_file)
        print(f'转换成功！结果已保存到 "{args.output_file}"')
    except Exception as e:
        print(f'错误: 转换失败 - {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()