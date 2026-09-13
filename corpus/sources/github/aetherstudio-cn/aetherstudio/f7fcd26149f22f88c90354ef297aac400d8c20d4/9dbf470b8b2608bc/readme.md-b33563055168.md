# Aether Studio（牧羊人编辑器）

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.txt)
[![Rust](https://img.shields.io/badge/built%20with-Rust-orange.svg)](https://www.rust-lang.org)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)]()

---

## 目录 / Table of Contents

- [English](#english)
  - [The Repository](#the-repository)
  - [Product Introduction](#product-introduction)
  - [Features](#features)
  - [Contributing](#contributing)
  - [Building from Source](#building-from-source)
  - [Testing](#testing)
  - [Project Architecture](#project-architecture)
  - [Documentation](#documentation)
  - [Feedback](#feedback)
  - [License](#license)
- [中文](#中文)
  - [仓库说明](#仓库说明)
  - [产品简介](#产品简介)
  - [功能特性](#功能特性)
  - [参与贡献](#参与贡献)
  - [从源码构建](#从源码构建)
  - [测试](#测试)
  - [项目架构](#项目架构)
  - [文档](#文档)
  - [反馈](#反馈)
  - [许可证](#许可证)

---

## English

### The Repository

This repository is where we develop the **Aether Studio** product. Aether Studio is a modern code editor built with Rust and Win32 API, designed for native Windows experience with high performance and low latency. The source code is available to everyone under the standard [MIT license](LICENSE.txt).

### Product Introduction

Aether Studio combines the simplicity of a lightweight editor with what developers need for their core edit-build-debug cycle. It provides comprehensive code editing, navigation, and syntax highlighting support along with AI-assisted coding, a modular extensibility model, and native Windows integration.

Aether Studio is actively developed with new features and bug fixes. It is currently available for **Windows 10 1809+** and **Windows 11**.

### Features

- **Native Windows Experience**: Win32 window with DWM immersive dark mode, high DPI support, DPI scaling, and system high contrast mode.
- **Self-Rendered UI Engine**: Direct2D / DirectWrite 2D rendering pipeline with themes, translucent backgrounds, shadows, animations, and dirty rectangle optimization.
- **High-Performance Text Editing**: Piece Table text buffer, multi-cursor support, selection, undo/redo history stack, syntax highlighting, find/replace, and auto-indentation.
- **Markdown Preview**: Built-in Markdown reader with edit/preview mode switching, live rendering, and synchronized scrolling.
- **Image Preview**: Image preview with zoom, pan, and middle-button drag support.
- **Multi-Language Lexer**: Built-in tokenization for C, Rust, JavaScript, Python, JSON, TOML, HTML, Markdown, and more.
- **File Tree & Workspace**: Asynchronous file scanning, Git status markers, recent projects, and drag-and-drop support.
- **AI Integration**: HTTP-based LLM interaction with DeepSeek and Kimi presets, code explanation, rewrite, inline suggestions, Agent tool result feedback, and API configuration panel.
- **LSP Support**: Language Server Protocol client framework (document sync, semantic tokens, incremental sync).
- **DAP Support**: Debug Adapter Protocol client foundation (types, transport, session, client).
- **Tree-sitter Integration**: Syntax parsing, language detection, TextMate theme mapping, highlight rendering, and file-switch highlight caching.
- **Remote Development**: SSH connection, remote file system, Git clone, and remote directory browsing.
- **Terminal Panel**: Built-in terminal panel with PowerShell / CMD subprocess support via ConPTY.
- **Plugin System**: Plugin registration, permission control, and runtime foundation.
- **International Input Method**: CJK IME candidate window positioning and composition events.
- **Command Line Tool**: `aether` CLI to launch GUI, open paths, navigate to line/column, and support `--wait` / `--new-window`.

### Contributing

There are many ways in which you can participate in this project:

* [Submit bugs and feature requests](https://github.com/songdiyang/AetherStudio/issues)
* [Review source code changes](https://github.com/songdiyang/AetherStudio/pulls)
* [Review the documentation](.qoder/repowiki) and make pull requests for anything from typos to new content.

If you are interested in fixing issues and contributing directly to the code base, please see the document [CONTRIBUTING.md](CONTRIBUTING.md), which covers the following:

* [Fork workflow for external contributors](CONTRIBUTING.md#1-外部贡献者-fork-流程)
* [Branch conventions for repository members](CONTRIBUTING.md#2-仓库成员分支规范)
* [Pre-commit checklist](CONTRIBUTING.md#3-提交前检查清单)
* [Commit message conventions](CONTRIBUTING.md#3-提交信息规范)
* [PR creation process](CONTRIBUTING.md#4-pr-创建流程)
* [CI failure handling](CONTRIBUTING.md#6-ci-失败处理)
* [Merge conflict resolution](CONTRIBUTING.md#6-合并冲突处理)

### Building from Source

#### Requirements

- Windows 10 1809 or higher (Windows 11 recommended)
- Rust stable toolchain (see `rust-toolchain.toml`)
- Visual Studio 2022 (or Windows SDK build tools)
- Target: `x86_64-pc-windows-msvc`

#### Build

```powershell
# Debug build
cargo build -p aether-win32 --bin aether-app

# Release build (fat LTO, single codegen unit, strip)
cargo build -p aether-win32 --bin aether-app --release

# CLI tool
cargo build -p aether-cli --bin aether
```

#### Run

```powershell
# Launch GUI directly
cargo run -p aether-win32 --bin aether-app

# Open file via CLI
cargo run -p aether-cli --bin aether -- path/to/file.rs

# Navigate to line:column
cargo run -p aether-cli --bin aether -- file.txt:10:5
```

Build artifacts are located at:

```
target\x86_64-pc-windows-msvc\debug\aether-app.exe
target\x86_64-pc-windows-msvc\release\aether-app.exe
```

### Testing

```powershell
# Full workspace unit tests (disable incremental compilation to avoid ICE)
$env:CARGO_INCREMENTAL = '0'
cargo test --workspace --no-fail-fast

# Static analysis
cargo clippy --workspace --all-targets -- -D warnings

# Format check
cargo fmt --all -- --check

# GUI smoke test (requires release build)
cargo build --release -p aether-win32
python tests/gui_smoke.py

# Coverage collection (requires llvm-tools-preview)
powershell -File tests/tools/coverage.ps1
```

Latest test snapshot (2026-07-06):

| Metric | Result |
|---|---|
| Unit tests | **793 tests passing** |
| Code coverage | Regions 47.82% / Lines 43.70% / Functions 61.66% |
| Clippy | Passing with `-D warnings` |
| Release build | Successful |
| GUI smoke test | Successful startup, click, screenshot, close |
| Memory | ~67MB |
| Lexer benchmark | ~500–650 MiB/s |

> Coverage is affected by Win32 / Direct2D GUI rendering code, window procedures, real subprocesses, and network interactions. Business logic modules that can be unit-tested generally reach **80–100%** coverage.

### Project Architecture

The repository is organized as a Cargo Workspace with multiple crates:

| Crate | Responsibility |
|---|---|
| `aether-core` | Text buffer, history stack, lexer, workspace data structures, search |
| `aether-render` | Direct2D / DirectWrite rendering abstraction, theme system, brush cache |
| `aether-win32` | Windows native UI layer: window, message loop, menus, layout, events, app entry |
| `aether-shared` | Shared configuration and persistence (UI, AI, recent projects, window state) |
| `aether-lsp` | Language Server Protocol client (sync, incremental sync, semantic tokens) |
| `aether-dap` | Debug Adapter Protocol client foundation |
| `aether-remote` | SSH / Git / container remote operation abstraction |
| `aether-ai` | AI service interface and request handling |
| `aether-tree-sitter` | Tree-sitter syntax parsing, language detection, theme mapping |
| `aether-plugin` | Plugin registration, permissions, and runtime |
| `aether-cli` | Command-line launcher, parsing arguments and launching the GUI |

### Documentation

The project includes a comprehensive internal documentation system under `.qoder/repowiki/zh/content/` covering:

- **Project Overview**: Architecture, core components, dependencies, performance considerations
- **Quick Start**: Getting started guide for new developers
- **Development Guide**: Development workflow, testing strategy, coding standards
- **API Reference**: Public interfaces, CLI, plugin development interfaces, configuration
- **UI System**: Theme system, rendering pipeline, window management, input events
- **Architecture Design**: Overall architecture, text buffer system, lexer framework, rendering engine, UI event system, language service integration
- **Core Components**: Workspace management, search system, text buffer, rendering engine, lexer framework
- **Performance Optimization**: SIMD algorithms, memory management, async I/O, rendering optimization
- **Extension System**: AI assistant integration, plugin architecture, remote development
- **Language Support**: LSP client, DAP debugging, Tree-sitter integration, language configuration

### Feedback

* [Request a new feature](https://github.com/songdiyang/AetherStudio/issues)
* [File an issue](https://github.com/songdiyang/AetherStudio/issues)
* Follow the project and let us know what you think!

### License

Copyright (c) 2024 - present 宋狄阳 (Song Diyang).

Licensed under the [MIT](LICENSE.txt) license.

---

## 中文

### 仓库说明

本仓库是 **Aether Studio（牧羊人编辑器）** 的开发仓库。Aether Studio 是一款基于 Rust + Win32 API 构建的现代化代码编辑器，面向 Windows 平台原生体验设计，追求高性能与低延迟。源代码在标准 [MIT 许可证](LICENSE.txt) 下向所有人开放。

### 产品简介

Aether Studio 将轻量级编辑器的简洁性与开发者核心编辑-构建-调试周期所需的功能相结合。提供全面的代码编辑、导航、语法高亮支持，以及 AI 辅助编程、模块化可扩展模型和原生 Windows 集成。

Aether Studio 正在积极开发中，持续推出新功能和错误修复。目前支持 **Windows 10 1809+** 和 **Windows 11**。

### 功能特性

- **原生 Windows 体验**: 基于 Win32 窗口 + DWM 沉浸式深色模式，支持高 DPI、DPI 缩放与系统高对比度模式。
- **自绘渲染引擎**: 基于 Direct2D / DirectWrite 的 2D 渲染管线，支持主题、半透明背景、阴影、动画与脏矩形优化。
- **高性能文本编辑**: Piece Table 文本缓冲、多光标、选择区、撤销/重做历史栈、语法高亮、查找替换、自动缩进。
- **Markdown 预览**: 内置 Markdown 阅读器，支持编辑/预览模式切换、实时渲染与同步滚动。
- **图片预览**: 图片预览支持缩放、平移与中键拖拽。
- **多语言词法分析器**: 内置 C、Rust、JavaScript、Python、JSON、TOML、HTML、Markdown 等语言的分词支持。
- **文件树与工作区**: 异步文件扫描、Git 状态标记、最近项目、拖拽支持。
- **AI 集成**: 基于 HTTP 的大模型交互，支持 DeepSeek / Kimi 预设配置、代码解释、改写、内联建议、Agent 工具结果回喂与 API 配置面板。
- **LSP 支持**: 语言服务器协议客户端框架（文档同步、语义 token、增量同步）。
- **DAP 支持**: 调试适配器协议客户端基础实现。
- **Tree-sitter 集成**: 语法解析、语言检测、TextMate 主题映射、高亮渲染与文件切换高亮缓存。
- **远程开发**: SSH 连接、远程文件系统、Git 克隆与远程目录浏览。
- **终端面板**: 内置终端面板，通过 ConPTY 支持 PowerShell / CMD 子进程。
- **插件系统**: 插件注册、权限控制与运行时基础。
- **国际化输入法**: CJK 输入法候选窗口定位与合成事件。
- **命令行工具**: `aether` CLI 可启动 GUI、打开路径、定位行列并支持 `--wait` / `--new-window`。

### 参与贡献

您可以通过多种方式参与本项目：

* [提交错误和功能请求](https://github.com/songdiyang/AetherStudio/issues)
* [审查源代码变更](https://github.com/songdiyang/AetherStudio/pulls)
* [审查文档](.qoder/repowiki) 并针对从拼写错误到新内容的任何内容提交 PR。

如果您有兴趣修复问题并直接贡献代码，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)，其中涵盖以下内容：

* [外部贡献者 Fork 流程](CONTRIBUTING.md#1-外部贡献者-fork-流程)
* [仓库成员分支规范](CONTRIBUTING.md#2-仓库成员分支规范)
* [提交前检查清单](CONTRIBUTING.md#3-提交前检查清单)
* [提交信息规范](CONTRIBUTING.md#3-提交信息规范)
* [PR 创建流程](CONTRIBUTING.md#4-pr-创建流程)
* [CI 失败处理](CONTRIBUTING.md#6-ci-失败处理)
* [合并冲突处理](CONTRIBUTING.md#6-合并冲突处理)

### 从源码构建

#### 环境要求

- Windows 10 1809 或更高版本（推荐 Windows 11）
- Rust stable 工具链（见 `rust-toolchain.toml`）
- Visual Studio 2022（或 Windows SDK 构建工具）
- 目标平台：`x86_64-pc-windows-msvc`

#### 构建

```powershell
# 调试构建
cargo build -p aether-win32 --bin aether-app

# 发布构建（fat LTO、单代码生成单元、strip）
cargo build -p aether-win32 --bin aether-app --release

# 命令行工具
cargo build -p aether-cli --bin aether
```

#### 运行

```powershell
# 直接启动 GUI
cargo run -p aether-win32 --bin aether-app

# 通过 CLI 打开文件
cargo run -p aether-cli --bin aether -- path/to/file.rs

# 定位到指定行列
cargo run -p aether-cli --bin aether -- file.txt:10:5
```

编译产物位于：

```
target\x86_64-pc-windows-msvc\debug\aether-app.exe
target\x86_64-pc-windows-msvc\release\aether-app.exe
```

### 测试

```powershell
# 全 Workspace 单元测试（禁用增量编译以避免 ICE）
$env:CARGO_INCREMENTAL = '0'
cargo test --workspace --no-fail-fast

# 静态分析
cargo clippy --workspace --all-targets -- -D warnings

# 格式化检查
cargo fmt --all -- --check

# GUI 冒烟测试（需 release 构建产物）
cargo build --release -p aether-win32
python tests/gui_smoke.py

# 覆盖率收集（需 llvm-tools-preview）
powershell -File tests/tools/coverage.ps1
```

最新测试快照（2026-07-06）：

| 指标 | 结果 |
|---|---|
| 单元测试 | **793 个测试全部通过** |
| 代码覆盖率 | Regions 47.82% / Lines 43.70% / Functions 61.66% |
| Clippy | 通过（`-D warnings`） |
| 发布构建 | 成功 |
| GUI 冒烟测试 | 成功启动、点击、截图、关闭 |
| 内存 | ~67MB |
| 词法分析器基准 | ~500–650 MiB/s |

> 覆盖率受大量 Win32 / Direct2D GUI 渲染代码、窗口过程、真实子进程与网络交互代码拖累。可单元测试的业务逻辑模块覆盖率普遍达到 **80–100%**。

### 项目架构

仓库采用 Cargo Workspace 组织，按职责拆分为多个 Crate：

| Crate | 职责 |
|---|---|
| `aether-core` | 编辑器核心：文本缓冲、历史栈、词法分析器、工作区数据结构、搜索 |
| `aether-render` | 渲染抽象、主题系统、画笔缓存 |
| `aether-win32` | Windows 原生 UI 层：窗口、消息循环、菜单、布局、事件处理、应用入口 |
| `aether-shared` | 共享配置与持久化设置 |
| `aether-lsp` | LSP 客户端实现 |
| `aether-dap` | DAP 客户端基础实现 |
| `aether-remote` | 远程操作抽象 |
| `aether-ai` | AI 服务接口与请求处理 |
| `aether-tree-sitter` | 语法解析、语言检测、主题映射 |
| `aether-plugin` | 插件注册、权限与运行时 |
| `aether-cli` | 命令行启动器 |

### 文档

项目内置详细的内部文档系统（位于 `.qoder/repowiki/zh/content/`），涵盖：

- **项目概述**: 架构总览、核心组件、依赖关系、性能考量
- **快速开始**: 新开发者入门指南
- **开发指南**: 开发工作流、测试策略、编码规范
- **API 参考**: 公共接口、命令行接口、插件开发接口、配置接口
- **UI 系统**: 主题系统、渲染管线、窗口管理、输入事件处理
- **架构设计**: 整体架构、文本缓冲区系统、词法分析器框架、渲染引擎、UI 事件系统、语言服务集成
- **核心组件**: 工作区管理、搜索系统、文本缓冲区、渲染引擎、词法分析器框架
- **性能优化**: SIMD 算法、内存管理、异步 IO、渲染优化
- **扩展系统**: AI 助手集成、插件架构、远程开发
- **语言支持**: LSP 客户端、DAP 调试、Tree-sitter 集成、语言配置管理

### 反馈

* [请求新功能](https://github.com/songdiyang/AetherStudio/issues)
* [提交问题](https://github.com/songdiyang/AetherStudio/issues)
* 关注项目并告诉我们您的想法！

### 许可证

Copyright (c) 2024 - present 宋狄阳 (Song Diyang).

本项目采用 [MIT 许可证](LICENSE.txt)。详见 LICENSE.txt 文件。

---

## Repository / 仓库

- GitHub: [https://github.com/songdiyang/AetherStudio](https://github.com/songdiyang/AetherStudio)
