# ncrtxt

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/ncrtxt.svg)](https://pypi.org/project/ncrtxt/)

**ncrtxt** 是一个强大的 Python 命令行工具，专门用于将 HTML 数字字符引用转换为对应的 Unicode 字符。它支持十进制和十六进制格式的数字字符引用，是处理网页内容、文本数据清理和国际化的理想工具。

## ✨ 特性

- 🔢 **多格式支持**：同时支持十进制（&#1234;）和十六进制（&#x1F600;）格式
- 🚀 **高性能处理**：使用正则表达式优化，快速处理大文件
- 🛡️ **安全可靠**：无效字符引用保持原样，不会破坏原始内容
- 📁 **批量转换**：支持整个文件的批量处理
- 🌍 **Unicode 完整支持**：支持所有 Unicode 字符范围
- 📖 **详细错误提示**：提供清晰的错误信息和解决建议
- 🔧 **零依赖**：仅使用 Python 标准库，无需额外安装依赖

## 🚀 快速开始

### 安装

#### 使用 pip 安装（推荐）

```bash
pip install ncrtxt
```

#### 从源码安装

```bash
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt
pip install -e .
```

### 基本使用

```bash
# 转换文件
ncrtxt input.txt output.txt

# 查看帮助
ncrtxt --help

# 查看版本
ncrtxt --version
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
<p>&#20851;&#20110;&#25105;&#20204;: &#x6211;&#x4eec;&#x662f;&#x4e00;&#x4e2a;&#x6d4b;&#x8bd5;&#x9875;&#x9762;</p>
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

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt

# 创建虚拟环境
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
├── tests/               # 测试文件（如果存在）
├── docs/                # 文档（如果存在）
├── pyproject.toml       # 项目配置
├── README.md           # 项目说明
├── LICENSE             # 许可证
└── .gitignore          # Git 忽略文件
```

### 运行测试

```bash
# 运行所有测试
python -m pytest

# 运行特定测试
python -m pytest tests/test_converter.py

# 生成覆盖率报告
python -m pytest --cov=ncrtxt
```

### 构建和发布

```bash
# 构建包
python -m build

# 检查包
twine check dist/*

# 上传到 PyPI（需要配置认证）
twine upload dist/*
```

## 📝 API 参考

### `convert_html_entities(text: str) -> str`

转换 HTML 数字字符引用为对应字符。

**参数：**

- `text` (str): 包含数字字符引用的文本

**返回：**

- `str`: 转换后的文本

**示例：**

```python
>>> convert_html_entities('&#18487;')
'䠷'
>>> convert_html_entities('&#x4E2D;')
'中'
```

### `convert_file(input_file: Union[str, Path], output_file: Union[str, Path]) -> None`

转换文件中的数字字符引用。

**参数：**

- `input_file` (Union[str, Path]): 输入文件路径
- `output_file` (Union[str, Path]): 输出文件路径

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

- 使用 SSD 存储可以提高大文件处理速度
- 对于批量处理，考虑使用并行处理
- 内存充足时，可以处理更大的文件

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
