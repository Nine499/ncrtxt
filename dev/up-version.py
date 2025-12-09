"""版本更新脚本 - 自动更新版本号并构建项目"""

import datetime
import re
import subprocess
import sys
from pathlib import Path


def generate_version():
    """生成基于当前时间的版本号"""
    now = datetime.datetime.now()
    return now.strftime("%Y.%m.%d.%H%M%S")


def update_pyproject_toml(version):
    """更新 pyproject.toml 中的版本号"""
    pyproject_path = Path("pyproject.toml")

    if not pyproject_path.exists():
        print("错误: 找不到 pyproject.toml 文件")
        return False

    content = pyproject_path.read_text(encoding="utf-8")

    # 使用正则表达式替换版本号
    new_content = re.sub(r'version = ".*?"', f'version = "{version}"', content)

    pyproject_path.write_text(new_content, encoding="utf-8")
    print(f"✓ 已更新 pyproject.toml 版本为: {version}")
    return True


def update_init_version(version):
    """更新 ncrtxt/__init__.py 中的版本号"""
    init_path = Path("ncrtxt/__init__.py")

    if not init_path.exists():
        print("错误: 找不到 ncrtxt/__init__.py 文件")
        return False

    content = init_path.read_text(encoding="utf-8")

    # 使用正则表达式替换版本号
    new_content = re.sub(r'__version__ = ".*?"', f'__version__ = "{version}"', content)

    init_path.write_text(new_content, encoding="utf-8")
    print(f"✓ 已更新 ncrtxt/__init__.py 版本为: {version}")
    return True


def run_build():
    """执行 uv build"""
    try:
        print("正在执行 uv build...")
        result = subprocess.run(
            ["uv", "build"], check=True, capture_output=True, text=True
        )
        print("✓ 构建成功!")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 构建失败: {e}")
        print(f"错误输出: {e.stderr}")
        return False
    except FileNotFoundError:
        print("✗ 未找到 uv 命令，请确保已安装 uv")
        return False


def main():
    """主函数"""
    print("=== 版本更新脚本 ===")

    # 生成新版本号
    new_version = generate_version()
    print(f"生成的新版本号: {new_version}")

    # 检查是否在项目根目录
    if not Path("pyproject.toml").exists():
        print("错误: 请在项目根目录运行此脚本")
        sys.exit(1)

    # 更新版本号
    success = True
    success &= update_pyproject_toml(new_version)
    success &= update_init_version(new_version)

    if not success:
        print("✗ 版本更新失败")
        sys.exit(1)

    # 执行构建
    if not run_build():
        print("✗ 构建失败")
        sys.exit(1)

    print(f"\n🎉 版本更新完成! 新版本: {new_version}")


if __name__ == "__main__":
    main()
