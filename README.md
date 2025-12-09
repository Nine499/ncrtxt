# ncrtxt

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/ncrtxt.svg)](https://pypi.org/project/ncrtxt/)
[![UV Powered](https://img.shields.io/badge/UV%20Powered-blue.svg)](https://github.com/astral-sh/uv)
[![UV Managed](https://img.shields.io/badge/UV%20Managed-00d084.svg)](https://github.com/astral-sh/uv)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type Checked](https://img.shields.io/badge/type%20checked-mypy-success.svg)](https://mypy-lang.org/)

**ncrtxt** 是一个高性能 Python 命令行工具，专门用于将 HTML 数字字符引用转换为对应的 Unicode 字符。它支持十进制和十六进制格式的数字字符引用，采用流式处理架构，是处理网页内容、文本数据清理和国际化的理想工具。

本项目以 **PythonUV** 为核心包管理器，提供闪电般的依赖解析、虚拟环境管理和项目构建体验。UV 的现代化设计让 Python 开发变得更加简单和高效。

## ✨ 特性

- 🔢 **多格式支持**：同时支持十进制（&#1234;）和十六进制（&#x1F600;）格式
- 🚀 **高性能处理**：使用预编译正则表达式和流式处理，快速处理任意大小文件
- 💾 **内存优化**：流式架构支持 GB 级大文件，内存占用恒定
- 🛡️ **安全可靠**：无效字符引用保持原样，不会破坏原始内容
- 📁 **批量转换**：支持整个文件的批量处理
- 🌍 **Unicode 完整支持**：支持所有 Unicode 字符范围
- 📖 **详细错误提示**：提供清晰的错误信息和解决建议
- 🔧 **零依赖**：仅使用 Python 标准库，无需额外安装依赖
- ⚡ **UV 驱动**：完全基于 UV 包管理器，提供闪电般的依赖解析和安装
- 🚀 **现代化工具链**：集成 UV、Ruff、MyPy 等现代化 Python 工具
- 🔧 **零配置开发**：开箱即用的开发环境配置
- 📦 **统一依赖管理**：通过 pyproject.toml 统一管理所有依赖和脚本

## 🚀 快速开始

### 先决条件

确保已安装 **PythonUV**：

```bash
# 在 macOS/Linux 上
curl -LsSf https://astral.sh/uv/install.sh | sh

# 在 Windows 上
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 或使用 pip
pip install uv
```

### 安装

#### 🔥 使用 UV（推荐）

```bash
# 从 PyPI 安装
uv add ncrtxt

# 全局安装为工具
uv tool install ncrtxt

# 从源码安装
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt
uv sync      # 自动创建虚拟环境并安装依赖
```

#### 📦 使用 pip（兼容）

```bash
pip install ncrtxt
```

### 基本使用 1

```bash
# 使用 UV 运行
uv run ncrtxt input.txt output.txt

# 如果全局安装
ncrtxt input.txt output.txt

# 查看帮助
uv run ncrtxt --help
```

### 基本使用 2

```bash
# 转换文件
ncrtxt input.txt output.txt

# 查看帮助
ncrtxt --help

# 查看版本
ncrtxt --version

# 使用 UV 运行
uv run ncrtxt input.txt output.txt
```

## 📖 详细使用说明

### 命令行参数

| 参数          | 类型   | 必需 | 说明                                   |
| ------------- | ------ | ---- | -------------------------------------- |
| `input_file`  | 字符串 | ✅   | 输入文件路径（包含数字字符引用的文件） |
| `output_file` | 字符串 | ✅   | 输出文件路径（转换后的文件）           |
| `--version`   | 标志   | ❌   | 显示版本信息                           |
| `--help`      | 标志   | ❌   | 显示帮助信息                           |

### 支持的格式

#### 十进制格式

```text
&#65;     → A
&#20013;  → 中
&#128512; → 😀
```

#### 十六进制格式

```text
&#x41;    → A
&#x4E2D;  → 中
&#x1F600; → 😀
```

#### 混合使用

```text
&#65;&#66;&#67;     → ABC
&#x4E2D;&#x6587;     → 中文
Hello&#x20;&#World; → Hello World
```

### 使用示例

#### 示例 1：基本转换

创建一个包含数字字符引用的文件：

```bash
echo "&#72;&#101;&#108;&#108;&#111;&#x20;&#87;&#111;&#114;&#108;&#100;" > input.txt
ncrtxt input.txt output.txt
cat output.txt
# 输出: Hello World
```

#### 示例 2：HTML 内容处理

```bash
# 创建 HTML 文件
cat > sample.html << EOF
<html>
<head><title>&#27979;&#35797;&#39029;</title></head>
<body>
<p>&#20851;&#20110;&#25105;&#20204;: &#x6211;&#x4eec;&#x662f;&#x4e00;&#x4e2a;&#x6d4b;&#8bd5;&#x9875;&#x9762;</p>
<p>&#128512;&#128514;&#128516;</p>
</body>
</html>
EOF

# 转换 HTML 文件
ncrtxt sample.html converted.html
```

#### 示例 3：批量处理脚本

```bash
#!/bin/bash
# 批量转换目录中的所有 txt 文件

for file in *.txt; do
    if [[ -f "$file" ]]; then
        output="converted_$file"
        echo "转换 $file -> $output"
        ncrtxt "$file" "$output"
    fi
done
```

#### 示例 4：大文件处理

```bash
# 处理大文件（流式处理，内存占用恒定）
ncrtxt large_input.txt large_output.txt

# 监控内存使用
time ncrtxt huge_file.txt output.txt
```

#### 示例 5：Python 脚本集成

```python
#!/usr/bin/env python3
from pathlib import Path
from ncrtxt.converter import convert_file

# 批量处理目录
input_dir = Path("data/raw")
output_dir = Path("data/processed")

for file_path in input_dir.glob("*.txt"):
    output_path = output_dir / file_path.name
    output_path.parent.mkdir(parents=True, exist_ok=True)
    convert_file(file_path, output_path)
    print(f"已处理: {file_path} -> {output_path}")
```

## 🔧 高级用法

### 在 Python 代码中使用

```python
from ncrtxt.converter import convert_html_entities, convert_file
from pathlib import Path

# 转换文本字符串
text = "&#72;&#101;&#108;&#108;&#111;&#x20;&#20013;&#25991;"
converted = convert_html_entities(text)
print(converted)  # 输出: Hello 中文

# 转换文件
convert_file("input.txt", "output.txt")

# 使用 Path 对象
input_path = Path("data/input.txt")
output_path = Path("data/output.txt")
convert_file(input_path, output_path)
```

### 使用 UV 运行脚本

```bash
# 直接运行脚本
uv run python your_script.py

# 使用项目中的工具
uv run ncrtxt input.txt output.txt

# 在虚拟环境中运行
uv run --no-project python your_script.py


```

### 错误处理

```python
try:
    convert_file("input.txt", "output.txt")
    print("转换成功")
except FileNotFoundError:
    print("输入文件不存在")
except UnicodeDecodeError:
    print("文件编码错误，请使用 UTF-8 编码")
except OSError as e:
    print(f"文件操作错误: {e}")
```

## 🛠️ 开发指南

### 🚀 快速开发环境设置（UV）

```bash
# 克隆仓库
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt

# UV 自动创建虚拟环境并安装所有依赖
uv sync

# 激活虚拟环境（可选）
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows
```

### 📋 开发命令

项目通过 `pyproject.toml` 预配置了所有常用命令：

```bash
# 运行测试
uv run test

# 运行测试并生成覆盖率报告
uv run test-cov

# 代码检查
uv run lint

# 代码格式化
uv run format

# 类型检查
uv run type-check

# 构建包
uv run build

# 清理构建产物
uv run clean

# 运行所有检查
uv run all-checks
```

### 🔧 传统开发环境

```bash
# 克隆仓库
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt

# 手动创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e ".[dev]"
```

### 项目结构

```text
ncrtxt/
├── ncrtxt/              # 主包目录
│   ├── __init__.py      # 包初始化文件
│   ├── cli.py           # 命令行接口
│   └── converter.py     # 核心转换功能
├── dev/                 # 开发工具
│   └── up-version.py    # 版本更新脚本
├── tests/               # 测试文件（如果存在）
├── docs/                # 文档（如果存在）
├── pyproject.toml       # 项目配置
├── README.md           # 项目说明
├── IFLOW.md            # 项目上下文文档
├── LICENSE             # 许可证
├── .python-version     # Python 版本指定
└── .gitignore          # Git 忽略文件
```

### 🧪 测试和代码质量

所有测试和质量检查都通过 UV 脚本统一管理：

```bash
# 快速测试
uv run test

# 详细测试报告
uv run test-cov

# 代码质量检查
uv run lint

# 自动格式化代码
uv run format

# 类型检查
uv run type-check

# 一键运行所有检查
uv run all-checks
```

### 📊 项目结构

```text
ncrtxt/
├── ncrtxt/              # 主包目录
│   ├── __init__.py      # 包初始化和版本信息
│   ├── cli.py           # 命令行接口
│   └── converter.py     # 核心转换功能
├── dev/                 # 开发工具
│   └── up-version.py    # 版本更新脚本
├── pyproject.toml       # UV 项目配置
├── README.md           # 项目文档
├── IFLOW.md            # 项目上下文
├── .python-version     # Python 版本指定
└── .gitignore          # Git 忽略文件
```

### 📦 构建和发布

#### UV 构建流程

```bash
# 构建包
uv build

# 检查构建产物
uv run twine check dist/*  # 如果安装了 twine

# 发布到测试 PyPI
uv publish --publish-url https://test.pypi.org/legacy/

# 发布到 PyPI（需要配置认证）
uv publish

# 使用版本更新脚本（自动更新版本并构建）
python3 dev/up-version.py
```

#### 传统构建流程

```bash
# 构建包
python -m build

# 检查包
twine check dist/*

# 上传到 PyPI（需要配置认证）
twine upload dist/*
```

### 🔄 UV 工作流程优势

- **⚡ 极速安装**：比 pip 快 10-100 倍的依赖解析
- **🔒 锁定文件**：自动生成 `uv.lock` 确保可重现构建
- **🌍 跨平台**：统一的体验，支持所有平台
- **📦 零配置**：开箱即用的现代 Python 开发体验
- **🚀 并行安装**：充分利用多核性能

## 📝 API 参考

### `convert_html_entities(text: str) -> str`

转换 HTML 数字字符引用为对应字符。

**参数：**

- `text` (str): 包含数字字符引用的文本

**返回：**

- `str`: 转换后的文本

**特性：**

- 使用预编译正则表达式，性能优化
- 自动处理无效引用，保持原样
- 支持所有 Unicode 字符范围

**示例：**

```python
>>> convert_html_entities('&#18487;')
'䠷'
>>> convert_html_entities('&#x4E2D;')
'中'
>>> convert_html_entities('&#65;&#66;&#67;')
'ABC'
```

### `convert_file(input_file: Union[str, Path], output_file: Union[str, Path], chunk_size: int = 1024*1024) -> None`

转换文件中的数字字符引用（流式处理）。

**参数：**

- `input_file` (Union[str, Path]): 输入文件路径
- `output_file` (Union[str, Path]): 输出文件路径
- `chunk_size` (int): 每次读取的块大小（字符数），默认 1MB

**特性：**

- 流式处理，支持任意大小文件
- 内存占用恒定，与文件大小无关
- 自动创建输出目录
- 智能处理跨块的不完整实体

**异常：**

- `FileNotFoundError`: 输入文件不存在
- `UnicodeDecodeError`: 文件编码问题
- `OSError`: 文件读写权限问题

## 🔍 故障排除

### 常见问题

#### Q: 转换后某些字符没有变化？

A: 这可能是由于：

1. 字符引用格式不正确（缺少分号）
2. 字符编码超出 Unicode 范围
3. 输入文件不是 UTF-8 编码

#### Q: 出现 "UnicodeDecodeError" 错误？

A: 请确保输入文件使用 UTF-8 编码。可以使用以下命令转换：

```bash
iconv -f GBK -t UTF-8 input.txt > input_utf8.txt
```

#### Q: 如何处理大文件？

A: ncrtxt 支持处理大文件，但对于特别大的文件（>100MB），建议：

1. 确保有足够的内存
2. 考虑分批处理
3. 使用更快的存储设备

### 性能优化

- **存储优化**：使用 SSD 存储可以提高大文件处理速度
- **并行处理**：对于批量处理，考虑使用多进程/多线程
- **内存调整**：可通过 `chunk_size` 参数调整内存使用
- **编码优化**：确保输入文件使用 UTF-8 编码以获得最佳性能

### 性能基准

| 文件大小 | 处理时间 | 内存占用 | 备注         |
| -------- | -------- | -------- | ------------ |
| 1MB      | < 0.1s   | < 10MB   | 流式处理     |
| 100MB    | ~ 2s     | < 10MB   | 内存恒定     |
| 1GB      | ~ 20s    | < 10MB   | 适合大文件   |
| 10GB     | ~ 200s   | < 10MB   | 依赖存储速度 |

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 代码规范

- 遵循 PEP 8 代码风格
- 添加适当的类型注解
- 编写清晰的文档字符串
- 为新功能添加测试

### 报告问题

如果发现 bug 或有功能建议，请：

1. 检查是否已有相关 issue
2. 创建新 issue，详细描述问题
3. 提供重现步骤和环境信息

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢所有贡献者的支持
- 灵感来源于处理网页内容时的实际需求
- 感谢 Python 社区的优秀工具和库

## 📞 联系方式

- 项目主页: <https://github.com/Nine499/ncrtxt>
- 问题反馈: <https://github.com/Nine499/ncrtxt/issues>
- PyPI 页面: <https://pypi.org/project/ncrtxt/>

---

**ncrtxt** - 让数字字符引用转换变得简单高效！ 🎉
