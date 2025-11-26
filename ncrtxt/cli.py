"""命令行接口"""

import argparse
import sys
from pathlib import Path

from . import __version__
from .converter import convert_file


def main():
    """主命令行入口"""
    parser = argparse.ArgumentParser(
        prog="ncrtxt",
        description="转换数字字符引用文件 - 将HTML数字字符引用转换为对应的Unicode字符",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  ncrtxt 原始文件.txt 转换后文件.txt
  ncrtxt input.txt output.txt
  ncrtxt document.html converted.txt

支持的格式:
  - 十进制: &#18487; → 䠷
  - 十六进制: &#x4E2D; → 中
  - 混合使用: &#65;&#66;&#67; → ABC
        """,
    )

    parser.add_argument(
        "input_file", type=str, help="输入文件路径（包含数字字符引用的文件）"
    )

    parser.add_argument("output_file", type=str, help="输出文件路径（转换后的文件）")

    parser.add_argument("--version", action="version", version=f"ncrtxt {__version__}")

    args = parser.parse_args()

    try:
        # 验证输入文件
        input_path = Path(args.input_file)
        if not input_path.exists():
            print(f"错误: 输入文件不存在: {args.input_file}", file=sys.stderr)
            sys.exit(1)

        if not input_path.is_file():
            print(f"错误: 输入路径不是文件: {args.input_file}", file=sys.stderr)
            sys.exit(1)

        # 执行转换
        convert_file(args.input_file, args.output_file)
        print(f"✓ 转换完成: {args.input_file} -> {args.output_file}")

    except KeyboardInterrupt:
        print("\n操作被用户中断", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"编码错误: {e}", file=sys.stderr)
        print("提示: 请确保输入文件使用UTF-8编码", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"文件操作错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"未知错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
