# ncrtxt 项目上下文

## 项目概述

ncrtxt 是一个 Python 命令行工具，用于将 HTML 数字字符引用转换为对应的 Unicode 字符。该工具支持十进制（&#1234;）和十六进制（&#x1F600;）格式的数字字符引用。

**主要技术栈：**

- Python 3.12
- 标准库：argparse, re, pathlib
- 构建工具：hatchling
- 包管理：pyproject.toml

**项目架构：**

```text
ncrtxt/
├── ncrtxt/           # 主包目录
│   ├── __init__.py   # 包初始化，包含版本信息
│   ├── cli.py        # 命令行接口和参数解析
│   └── converter.py  # 核心转换功能
├── pyproject.toml    # 项目配置和依赖管理
└── README.md         # 项目说明文档
```

## 构建和运行

### 安装和开发设置

```bash
# 创建虚拟环境（推荐）
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows

# 安装项目（开发模式）
pip install -e .

# 或者使用 uv（如果可用）
uv sync
```

### 运行命令

```bash
# 基本用法
ncrtxt 输入文件.txt 输出文件.txt

# 查看帮助
ncrtxt --help

# 查看版本
ncrtxt --version
```

### 构建和发布

```bash
# 构建包
python -m build

# 本地安装
pip install dist/ncrtxt-*.whl
```

## 开发约定

### 代码风格

- 使用 Python 3.12+ 特性
- 遵循 PEP 8 代码规范
- 使用类型注解（typing 模块）
- 函数和类包含详细的 docstring

### 错误处理

- 使用 try-except 块处理常见错误
- 提供清晰的错误消息
- 支持键盘中断（Ctrl+C）
- 文件编码强制使用 UTF-8

### 测试和验证

- 核心功能包含 doctest 示例
- 命令行接口包含完整的错误处理
- 支持文件路径验证和权限检查

### 功能特性

- **十进制转换**：&#18487; → 䠷
- **十六进制转换**：&#x4E2D; → 中
- **混合使用**：&#65;&#66;&#67; → ABC
- **批处理**：支持整个文件的转换
- **安全处理**：无效字符引用保持原样

## 项目配置

### pyproject.toml 关键配置

- 项目名称：ncrtxt
- 入口点：ncrtxt.cli:main
- Python 版本要求：>=3.8
- 构建后端：hatchling

### 开发环境

- Python 版本：3.12（见 .python-version）
- 虚拟环境：.venv（被 git 忽略）
- 包构建：使用 hatchling

## 常见用例

1. **HTML 文档处理**：转换包含数字字符引用的 HTML 文件
2. **文本数据清理**：处理从网页抓取的文本数据
3. **国际化文本**：处理包含 Unicode 字符的文档
4. **编码转换**：将数字引用转换为可读字符

## 注意事项

- 输入文件必须是 UTF-8 编码
- 输出文件会自动创建父目录
- 无效的数字字符引用会保持原样
- 支持大文件处理（逐行读取）
