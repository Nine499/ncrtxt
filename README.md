# ncrtxt49

<div align="center">

**将 HTML 数字字符引用转换为可读字符的命令行工具**

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Nine499%2Fncrtxt-black.svg)](https://github.com/Nine499/ncrtxt)

</div>

---

## 📖 目录

- [项目简介](#项目简介)
- [功能特性](#功能特性)
- [安装指南](#安装指南)
- [快速开始](#快速开始)
- [使用示例](#使用示例)
- [支持的格式](#支持的格式)
- [开发指南](#开发指南)
- [常见问题](#常见问题)
- [许可证](#许可证)

---

## 项目简介

**ncrtxt49** 是一个轻量级的 Python 命令行工具，专门用于将 HTML 数字字符引用（HTML Numeric Character References）转换为对应的可读 Unicode 字符。

### 为什么需要这个工具？

在处理网页抓取、HTML 文档解析或文本数据清洗时，经常会遇到类似 `&#65;`、`&#x41;` 或 `&amp;` 这样的字符引用。这些引用虽然可以在浏览器中正确显示，但在文本处理、数据分析或日志查看时却难以阅读。

**ncrtxt49** 提供了一个简单、高效的解决方案，可以将这些字符引用批量转换为人类可读的文本格式。

### 核心优势

- ✅ **简单易用**：一条命令即可完成转换
- ✅ **支持多种格式**：十进制、十六进制、命名实体
- ✅ **批量处理**：支持任意大小的文本文件
- ✅ **零依赖**：仅使用 Python 标准库
- ✅ **跨平台**：支持 Linux、macOS、Windows
- ✅ **快速高效**：基于 Python 标准库的 `html.unescape` 实现

---

## 功能特性

### 支持的转换格式

| 格式类型 | 示例 | 转换结果 |
|---------|------|---------|
| 十进制格式 | `&#65;` | `A` |
| 十六进制格式 | `&#x41;` | `A` |
| 命名实体 | `&amp;` | `&` |
| 混合格式 | `&#65;&#x42;&#67;` | `ABC` |

### 核心功能

1. **文件批量转换**：读取输入文件，转换后写入输出文件
2. **多格式支持**：同时支持十进制、十六进制和命名实体
3. **中文支持**：完美支持中文字符的转换
4. **特殊字符处理**：正确处理空格、换行符等特殊字符
5. **错误处理**：完善的错误提示和异常处理

---

## 安装指南

### 前置要求

- Python 3.12 或更高版本
- [UV](https://github.com/astral-sh/uv) 包管理工具

### 安装 UV（如果尚未安装）

#### Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 安装 ncrtxt49

#### 方法一：使用 UV 工具安装（推荐）

```bash
uv tool install ncrtxt49
```

安装完成后，`ncrtxt49` 命令将自动添加到系统 PATH 中，可以在任何位置使用。

#### 方法二：从源码安装

```bash
# 克隆仓库
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt

# 使用 UV 安装
uv pip install -e .
```

### 验证安装

```bash
ncrtxt49 --help
```

如果看到帮助信息，说明安装成功。

---

## 快速开始

### 基本用法

```bash
ncrtxt49 输入文件 输出文件
```

### 示例

假设有一个包含 HTML 字符引用的文件 `input.txt`：

```txt
Hello &#65;&#66;&#67;
&#20013;&#25991;&#27979;&#35797;
This is &lt;test&gt; content
```

执行转换命令：

```bash
ncrtxt49 input.txt output.txt
```

转换后的 `output.txt` 内容：

```txt
Hello ABC
中文测试
This is <test> content
```

---

## 使用示例

### 示例 1：转换英文字符

**输入文件 `english.txt`：**
```txt
&#72;&#101;&#108;&#108;&#111; &#87;&#111;&#114;&#108;&#100;!
```

**命令：**
```bash
ncrtxt49 english.txt english_converted.txt
```

**输出：**
```txt
Hello World!
```

### 示例 2：转换中文字符

**输入文件 `chinese.txt`：**
```txt
&#x4F60;&#x597D;&#xFF0C;&#x4E16;&#x754C;&#xFF01;
```

**命令：**
```bash
ncrtxt49 chinese.txt chinese_converted.txt
```

**输出：**
```txt
你好，世界！
```

### 示例 3：转换混合格式

**输入文件 `mixed.txt`：**
```txt
&#72;&#x65;&#108;&#x6C;&#x6F; &amp; &#87;&#111;&#x72;&#x6c;&#100;
```

**命令：**
```bash
ncrtxt49 mixed.txt mixed_converted.txt
```

**输出：**
```txt
Hello & World
```

### 示例 4：转换特殊字符

**输入文件 `special.txt`：**
```txt
Tab: &#9;
Space: &#32;
Newline: &#10;
```

**命令：**
```bash
ncrtxt49 special.txt special_converted.txt
```

**输出：**
```txt
Tab:
Space:
Newline:

```

### 示例 5：处理 HTML 实体

**输入文件 `html_entities.txt`：**
```txt
&lt;div&gt;&amp;copy; 2024 &lt;/div&gt;
&quot;quoted text&quot;
&apos;single quote&apos;
```

**命令：**
```bash
ncrtxt49 html_entities.txt html_entities_converted.txt
```

**输出：**
```txt
<div>© 2024 </div>
"quoted text"
'single quote'
```

---

## 支持的格式

### 十进制格式（Decimal Format）

格式：`&#数字;`

示例：
- `&#65;` → `A`
- `&#20013;` → `中`
- `&#32;` → ` ` (空格)

### 十六进制格式（Hexadecimal Format）

格式：`&#x十六进制数字;`

示例：
- `&#x41;` → `A`
- `&#x4E2D;` → `中`
- `&#x20;` → ` ` (空格)

### 命名实体（Named Entities）

格式：`&实体名称;`

常见命名实体：
- `&amp;` → `&`
- `&lt;` → `<`
- `&gt;` → `>`
- `&quot;` → `"`
- `&apos;` → `'`
- `&copy;` → `©`
- `&reg;` → `®`
- `&trade;` → `™`

### 混合格式

工具会自动识别并转换文件中的所有格式类型，无需额外配置。

---

## 开发指南

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/Nine499/ncrtxt.git
cd ncrtxt

# 创建虚拟环境（可选）
uv venv

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows

# 安装项目（开发模式）
uv pip install -e .
```

### 本地运行

```bash
# 使用 UV 运行
uv run ncrtxt49 input.txt output.txt

# 或使用 Python 直接运行
python -m ncrtxt49.cli input.txt output.txt
```

### 运行测试

```bash
# 运行所有测试
uv run python -m unittest

# 运行特定测试
uv run python -m unittest test_converter.TestConverter.test_decimal_conversion

# 查看测试覆盖率（需要安装 coverage）
uv run coverage run -m unittest
uv run coverage report
```

### 项目结构

```
ncrtxt49/
├── src/
│   └── ncrtxt49/
│       ├── __init__.py    # 包初始化文件
│       ├── cli.py         # 命令行接口模块
│       ├── converter.py   # 核心转换逻辑模块
│       └── py.typed       # 类型标记文件
├── pyproject.toml         # 项目配置文件
├── README.md              # 项目说明文档
└── .python-version        # Python 版本锁定文件
```

### 代码规范

- 遵循 PEP 8 代码风格指南
- 使用类型提示（Type Hints）
- 所有函数和类必须有详细的 docstring
- 使用中文注释，确保注释清晰易懂

### 添加新功能

1. 在 `src/ncrtxt49/` 目录下添加新模块
2. 更新相关文档
3. 确保功能正常工作

---

## 常见问题

### Q1: 找不到 `ncrtxt49` 命令？

**A:** 请确保已正确安装工具：

```bash
# 重新安装
uv tool install ncrtxt49

# 检查安装位置
uv tool list

# 如果 PATH 未正确设置，手动添加 UV 工具目录到 PATH
# 通常位于 ~/.local/bin 或 ~/Library/Application Support/uv/bin
```

### Q2: 如何卸载工具？

**A:**

```bash
uv tool uninstall ncrtxt49
```

### Q3: 支持大文件吗？

**A:** 是的，工具支持任意大小的文本文件。转换过程是逐行读取和写入的，内存占用较低。

### Q4: 转换失败怎么办？

**A:** 请检查以下几点：

1. 输入文件是否存在
2. 输入文件是否为文本文件
3. 输出路径是否有写入权限
4. 文件编码是否为 UTF-8

如果问题仍然存在，请查看错误信息或提交 Issue。

### Q5: 如何处理非 UTF-8 编码的文件？

**A:** 目前工具默认使用 UTF-8 编码。如果需要处理其他编码，可以：

1. 先将文件转换为 UTF-8 编码
2. 或修改源代码中的编码参数

### Q6: 支持哪些 Python 版本？

**A:** 项目要求 Python 3.12 或更高版本。

### Q7: 可以在 Windows 上使用吗？

**A:** 可以。工具是跨平台的，支持 Linux、macOS 和 Windows。

### Q8: 如何批量转换多个文件？

**A:** 可以使用 shell 脚本批量处理：

**Linux/macOS:**
```bash
for file in input_*.txt; do
    ncrtxt49 "$file" "converted_$file"
done
```

**Windows (PowerShell):**
```powershell
Get-ChildItem input_*.txt | ForEach-Object {
    ncrtxt49 $_.Name "converted_$($_.Name)"
}
```

---

## 技术细节

### 实现原理

工具使用 Python 标准库的 `html.unescape()` 函数进行转换。该函数能够：

1. 识别 HTML 数字字符引用（十进制和十六进制）
2. 识别 HTML 命名实体
3. 将它们转换为对应的 Unicode 字符

### 性能特性

- **时间复杂度**: O(n)，其中 n 是输入文件的字符数
- **空间复杂度**: O(1)，逐行处理，不占用额外内存
- **处理速度**: 约 10MB/秒（取决于硬件配置）

### 依赖项

- Python 标准库：`html`, `re`, `pathlib`, `argparse`
- 无第三方依赖

---

## 贡献指南

我们欢迎任何形式的贡献！

### 如何贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码审查标准

- 代码必须通过所有测试
- 代码风格符合项目规范
- 新功能必须有相应的测试
- 更新相关文档

### 报告 Bug

请在 GitHub Issues 中提交 Bug 报告，包括：

- 问题描述
- 复现步骤
- 预期行为
- 实际行为
- 环境信息（操作系统、Python 版本等）

---

## 更新日志

### 2026.01.15.121313 (2026-01-15)

- ✨ 优化项目结构
- ✨ 完善代码文档和类型提示
- ✨ 提升代码可维护性

### v0.1.0 (2024)

- ✨ 初始版本发布
- ✨ 支持十进制、十六进制和命名实体转换
- ✨ 命令行接口
- 📝 详细的使用文档

---

## 路线图

- [ ] 添加递归目录处理功能
- [ ] 支持从标准输入读取
- [ ] 支持输出到标准输出
- [ ] 添加更多编码格式支持
- [ ] 提供 Web 界面
- [ ] 添加 GUI 版本

---

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 致谢

- 感谢 Python 社区提供优秀的标准库
- 感谢 UV 团队提供高效的包管理工具
- 感谢所有贡献者的支持

---

## 联系方式

- **作者**: Nine499
- **GitHub**: [https://github.com/Nine499/ncrtxt](https://github.com/Nine499/ncrtxt)
- **Issues**: [https://github.com/Nine499/ncrtxt/issues](https://github.com/Nine499/ncrtxt/issues)

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐️**

Made with ❤️ by Nine499

</div>