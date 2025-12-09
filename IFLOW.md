# ncrtxt 项目上下文

## 项目概述

ncrtxt 是一个高性能 Python 命令行工具，专门用于将 HTML 数字字符引用转换为对应的 Unicode 字符。该工具采用流式处理架构，支持十进制（&#1234;）和十六进制（&#x1F600;）格式的数字字符引用，能够处理任意大小的文件而内存占用保持恒定。

本项目以 **PythonUV** 为核心包管理器和开发工具链，提供现代化的 Python 开发体验。UV 的极速依赖解析、统一配置管理和跨平台兼容性让项目开发变得更加高效和可靠。

**主要技术栈：**

- **Python**：3.12+（支持 >=3.8）
- **包管理器**：PythonUV（核心）、pip（兼容）
- **构建系统**：hatchling
- **项目配置**：pyproject.toml（统一配置）
- **代码质量**：ruff（格式化和检查）、mypy（类型检查）、pytest（测试）
- **开发工具**：UV 脚本系统、预编译正则表达式
- **处理架构**：流式处理，内存优化

**UV 核心特性：**

- 闪电般的依赖解析（比 pip 快 10-100 倍）
- 自动锁定文件管理（uv.lock）
- 跨平台统一体验
- 零配置开发环境
- 并行安装和缓存优化

**项目架构：**

```text
ncrtxt/
├── ncrtxt/              # 主包目录
│   ├── __init__.py      # 包初始化和版本信息
│   ├── cli.py           # 命令行接口（UV 优化）
│   └── converter.py     # 核心转换功能
├── dev/                 # 开发工具目录
│   └── up-version.py    # 版本更新脚本
├── pyproject.toml       # UV 项目配置中心
│   ├── [project]        # 项目元数据
│   ├── [dependency-groups] # UV 依赖组
│   ├── [tool.uv.scripts]   # UV 脚本系统
│   └── [tool.*]         # 工具链配置（ruff, mypy, pytest）
├── uv.lock              # UV 锁定文件（自动生成）
├── README.md            # 项目文档
├── IFLOW.md             # 项目上下文文档
├── .python-version      # Python 版本指定
└── .gitignore           # Git 忽略文件
```

## UV 驱动的开发环境

### 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt

# UV 自动设置开发环境
uv sync

# 运行项目
uv run ncrtxt input.txt output.txt
```

### 📋 UV 脚本系统

项目通过 `pyproject.toml` 预配置了完整的开发脚本：

```bash
# 测试相关
uv run test          # 快速测试
uv run test-cov      # 测试并生成覆盖率报告

# 代码质量
uv run lint          # 代码检查
uv run format        # 代码格式化
uv run type-check    # 类型检查

# 构建和发布
uv run build         # 构建包
uv run clean         # 清理构建产物
uv publish           # 发布到 PyPI

# 一键检查
uv run all-checks    # 运行所有检查
```

### 🔧 UV 核心命令

```bash
# 环境管理
uv sync              # 同步依赖
uv add package       # 添加依赖
uv remove package    # 移除依赖

# 运行命令
uv run command       # 在虚拟环境中运行命令
uv run python script.py

# 工具管理
uv tool install tool # 安装全局工具
uv tool run tool     # 运行全局工具
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

# 使用版本更新脚本（自动更新版本并构建）
python3 dev/up-version.py
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

- **多格式支持**：十进制（&#18487; → 䠷）、十六进制（&#x4E2D; → 中）
- **混合处理**：支持同一文本中的多种格式（&#65;&#66;&#67; → ABC）
- **流式批处理**：支持任意大小文件的转换
- **安全处理**：无效字符引用保持原样，不破坏原始内容
- **内存优化**：流式架构，内存占用恒定（< 10MB）
- **性能优化**：预编译正则表达式，高效处理
- **UV 驱动**：闪电般的依赖解析和虚拟环境管理
- **零配置开发**：开箱即用的 UV 脚本系统
- **统一工具链**：集成 ruff、mypy、pytest 等现代化工具
- **错误处理**：完善的异常处理和错误提示

## 项目配置

### 📄 pyproject.toml 配置详解

#### 项目元数据

- **项目名称**：ncrtxt
- **入口点**：ncrtxt.cli:main
- **Python 版本要求**：>=3.8（推荐 3.12+）
- **构建后端**：hatchling

#### UV 依赖组配置

```toml
[dependency-groups]
dev = [
    "hatchling>=1.27.0",
    "pytest>=8.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0"
]
```

#### UV 脚本系统

```toml
[tool.uv.scripts]
test = "pytest -q"
test-cov = "pytest --cov=ncrtxt --cov-report=term-missing"
lint = "ruff check ."
format = "ruff format ."
type-check = "mypy ncrtxt/"
build = "python -m build"
clean = "rm -rf dist/ build/ *.egg-info/"
all-checks = "ruff check . && ruff format . --check && mypy ncrtxt/ && pytest -q"
```

#### 工具配置

- **Ruff**：代码格式化和检查
- **MyPy**：静态类型检查
- **Pytest**：测试框架和覆盖率

### 🌍 UV 生态系统

- **锁定文件**：`uv.lock` 确保可重现构建
- **缓存系统**：全局缓存加速重复安装
- **并行处理**：充分利用多核性能
- **跨平台**：Windows、macOS、Linux 统一体验
- **解析器**：Rust 编写的极速依赖解析器

## 常见用例

1. **HTML 文档处理**：转换包含数字字符引用的 HTML 文件
2. **文本数据清理**：处理从网页抓取的文本数据
3. **国际化文本**：处理包含 Unicode 字符的文档
4. **编码转换**：将数字引用转换为可读字符
5. **大数据处理**：流式处理 GB 级别的日志文件
6. **批量文档转换**：自动化处理大量文档
7. **内容管理系统**：集成到 CMS 中处理用户内容
8. **数据迁移**：转换遗留系统中的数字字符引用

## 性能特征

- **处理速度**：约 50MB/s（依赖存储性能）
- **内存占用**：恒定 < 10MB（无论文件大小）
- **支持文件大小**：无限制（受文件系统限制）
- **并发处理**：可多进程并行处理不同文件
- **错误恢复**：部分错误不影响整体处理

## 🏗️ UV 驱动的项目架构

### 核心组件

1. **converter.py**：核心转换引擎

   - 预编译正则表达式（性能优化）
   - 流式文件处理（内存优化）
   - 智能实体边界处理

2. **cli.py**：命令行接口

   - 参数解析和验证
   - 错误处理和用户提示
   - UV 兼容性优化

3. \***\*init**.py\*\*：包初始化

   - 版本信息管理
   - 公共 API 导出

4. **pyproject.toml**：UV 项目配置中心
   - 统一依赖管理
   - 脚本系统配置
   - 工具链集成

### 🎯 UV 设计原则

- **性能优先**：预编译正则表达式，流式处理
- **内存安全**：恒定内存占用，支持大文件
- **错误容错**：无效引用保持原样，部分错误不影响整体
- **用户体验**：清晰的错误提示和进度反馈
- **可扩展性**：模块化设计，易于扩展新功能
- **现代化**：基于 UV 的现代 Python 开发最佳实践

### 🔄 UV 工作流程

1. **项目初始化**：`uv sync` 自动创建和配置环境
2. **开发迭代**：使用 UV 脚本进行测试、检查、格式化
3. **依赖管理**：`uv add/remove` 管理项目依赖
4. **构建发布**：`uv build` 和 `uv publish` 完成发布流程
5. **质量保证**：`uv run all-checks` 确保代码质量

## 🚀 UV 最佳实践

### 开发工作流程

1. **项目初始化**

   ```bash
   git clone https://github.com/Nine499/ncrtxt.git
   cd ncrtxt
   uv sync  # 一次性设置完整开发环境
   ```

2. **日常开发**

   ```bash
   # 添加新依赖
   uv add requests

   # 运行测试
   uv run test

   # 代码检查和格式化
   uv run lint && uv run format

   # 运行所有检查
   uv run all-checks
   ```

3. **发布流程**

   ```bash
   # 更新版本
   python3 dev/up-version.py

   # 构建包
   uv build

   # 发布到 PyPI
   uv publish
   ```

### UV 优势

- **⚡ 极速安装**：比 pip 快 10-100 倍
- **🔒 可重现构建**：`uv.lock` 确保环境一致性
- **📦 统一管理**：依赖、脚本、工具链一站式配置
- **🌍 跨平台**：Windows、macOS、Linux 统一体验
- **🚀 现代化**：Rust 编写的高性能工具

## ⚠️ 注意事项

- **编码要求**：输入文件必须是 UTF-8 编码
- **目录创建**：输出文件会自动创建父目录
- **容错处理**：无效的数字字符引用会保持原样
- **大文件支持**：支持任意大小文件（逐块读取）
- **性能考虑**：处理速度主要受存储 I/O 性能影响
- **并发安全**：多个进程可同时处理不同文件
- **UV 环境**：推荐使用 UV 进行开发和部署
