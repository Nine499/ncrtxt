# ncrtxt 项目上下文

## 项目概述

ncrtxt 是一个 Python 命令行工具，用于将 HTML 数字字符引用转换为对应的 Unicode 字符。该工具支持十进制（&#1234;）和十六进制（&#x1F600;）格式的数字字符引用。项目已完全适配 **UV** 包管理器。

**主要技术栈：**

- Python 3.12
- 标准库：argparse, re, pathlib
- 构建工具：hatchling
- 包管理：UV（主要）、pip（兼容）
- 项目配置：pyproject.toml

**项目架构：**

```text
ncrtxt/
├── ncrtxt/           # 主包目录
│   ├── __init__.py   # 包初始化，包含版本信息
│   ├── cli.py        # 命令行接口和参数解析（UV 优化）
│   └── converter.py  # 核心转换功能
├── pyproject.toml    # 项目配置和依赖管理（UV 专用）
├── README.md         # 项目说明文档（UV 相关）
└── IFLOW.md          # 项目上下文文档
```

## 构建和运行

### 安装和开发设置（UV 方式）

```bash
# 同步依赖（UV 会自动创建虚拟环境）
uv sync

# 激活虚拟环境（可选）
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows

# 安装项目（开发模式）
uv pip install -e .

# 或者使用 UV 工具安装
uv tool install -e .
```

### 安装和开发设置（传统方式）

```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows

# 安装项目（开发模式）
pip install -e .
```

### 运行命令

```bash
# 基本用法
ncrtxt 输入文件.txt 输出文件.txt

# 使用 UV 运行
uv run ncrtxt 输入文件.txt 输出文件.txt

# 查看帮助
ncrtxt --help
uv run ncrtxt --help

# 查看版本
ncrtxt --version
uv run ncrtxt --version
```

### 开发命令（UV）

```bash
# 运行测试
uv run test

# 代码检查
uv run lint

# 代码格式化
uv run format

# 类型检查
uv run type-check

# 构建包
uv build

# 发布到 PyPI
uv publish
```

### 构建和发布

```bash
# UV 构建包
uv build

# 传统构建包
python -m build

# 本地安装
uv pip install dist/ncrtxt-*.whl
# 或
pip install dist/ncrtxt-*.whl
```

## 开发约定

### 代码风格

- 使用 Python 3.12+ 特性
- 遵循 PEP 8 代码规范
- 使用类型注解（typing 模块）
- 函数和类包含详细的 docstring
- UV 兼容的依赖管理

### 错误处理

- 使用 try-except 块处理常见错误
- 提供清晰的错误消息
- 支持键盘中断（Ctrl+C）
- 文件编码强制使用 UTF-8
- UV 环境下的路径处理优化

### 测试和验证

- 核心功能包含 doctest 示例
- 命令行接口包含完整的错误处理
- 支持文件路径验证和权限检查
- UV 脚本集成测试

### 功能特性

- **十进制转换**：&#18487; → 䠷
- **十六进制转换**：&#x4E2D; → 中
- **混合使用**：&#65;&#66;&#67; → ABC
- **批处理**：支持整个文件的转换
- **安全处理**：无效字符引用保持原样
- **UV 优化**：快速依赖解析和虚拟环境管理

## 项目配置

### pyproject.toml 关键配置

- 项目名称：ncrtxt
- 入口点：ncrtxt.cli:main
- Python 版本要求：>=3.8
- 构建后端：hatchling
- UV 开发依赖组：pytest, ruff, mypy 等
- UV 脚本：test, lint, format, type-check

### UV 专用配置

- 开发依赖通过 [tool.uv.dev-dependencies] 管理
- 预定义脚本通过 [tool.uv.scripts] 配置
- 支持快速测试、检查和格式化

### 开发环境

- Python 版本：3.12（见 .python-version）
- 虚拟环境：.venv（被 git 忽略）
- 包构建：使用 hatchling
- 主要包管理器：UV
- 备用包管理器：pip（兼容性）

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
