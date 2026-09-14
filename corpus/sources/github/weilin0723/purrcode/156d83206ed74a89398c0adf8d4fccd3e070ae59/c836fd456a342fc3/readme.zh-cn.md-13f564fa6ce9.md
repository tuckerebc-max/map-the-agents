<p align="center">
  <img src="brand/purrcode-logo-horizontal-light.png" alt="PurrCode" width="320" />
</p>

<p align="center">
  <b>一个本地优先、拥有独立且可审计判断运行时的编程智能体。</b>
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://weilin0723.github.io/PurrCode/">文档</a> ·
  <a href="https://github.com/Weilin0723/PurrCode/wiki">Wiki</a> ·
  <a href="https://github.com/Weilin0723/PurrCode/releases/latest">最新版本</a>
</p>

<p align="center">
  <a href="https://github.com/Weilin0723/PurrCode/actions/workflows/ci.yml"><img src="https://github.com/Weilin0723/PurrCode/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://github.com/Weilin0723/PurrCode/releases/latest"><img src="https://img.shields.io/github/v/release/Weilin0723/PurrCode" alt="Release" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Weilin0723/PurrCode" alt="License" /></a>
</p>

> 模型负责提议，PawGate 负责授权，Claw 负责执行，证据决定结果。

PurrCode 是一个在隔离 Git worktree 中工作的终端编程智能体。它的核心理念很简单：模型输出只是
**提议**，而不是权威。每个原生操作都必须绑定到持久化授权，并在执行前再次校验，随后记录真实
验证结果。仓库内容、模型输出和下载的技能始终被视为不可信数据。

PurrCode v1.0 让纯 Rust native IDE 成为图形产品本身：直接运行 `purrcode ide` 打开 PurrCode
自己的桌面窗口，和终端 Workbench 共用 daemon 的同一会话。浏览器 portal 只通过
`purrcode experimental portal` 用于开发和维护，不会被 native IDE 自动打开，也不依赖
VS Code/Electron/Tauri。

## 界面

- **终端 Workbench** — 默认界面。直接运行 `purrcode` 在所有平台上都会打开它，绝不会意外弹出
  浏览器。
- **原生桌面 IDE** — `purrcode ide`（或 `purrcode gui`，两者是同一命令）。纯 Rust 桌面窗口，
  包含对话 Workbench、语法高亮编辑器，以及停靠的 Diff/Tests/Terminal/Problems/Output 面板。
- **Studio** — `purrcode studio`。用于 daemon 健康检查、会话和环境检查的安全浏览器维护客户端。
  它不是 v1.0 的正式 IDE，也不会有任何路径自动打开它。

## 安装

### macOS — 拖拽安装 App

体验原生桌面 IDE 最简单的方式：下载 **PurrCode.app**，拖入 **应用程序**，双击即可——无需终端。

1. 从 [最新版本](https://github.com/Weilin0723/PurrCode/releases/latest) 下载 `PurrCode.app.zip`。
2. 解压后把 **PurrCode.app** 拖进「应用程序」。
3. 双击 PurrCode 打开原生桌面 IDE。首次启动会自动创建配置并启动本机 daemon，之后启动会复用。

> 关于 Gatekeeper：应用暂未公证，macOS 可能提示「无法打开 PurrCode.app」。
> 右键应用选择「打开」，再点一次「打开」即可运行。我们计划在后续版本中做公证。

### macOS 和 Linux（终端）

```bash
curl -fsSL https://raw.githubusercontent.com/Weilin0723/PurrCode/v1.0.0/scripts/install.sh | sh
```

脚本会检测主机平台、下载发布归档，使用 `SHA256SUMS` 校验归档，并默认安装到 `~/.local/bin`。
可通过 `PURRCODE_INSTALL_DIR` 指定其他目录。

### npm

```bash
npm install --global @minaovo/purrcode
```

需要 Node.js 18 或更高版本。安装包会选择正确的 macOS、Linux 或 Windows 二进制文件，校验固定的
SHA-256 摘要，并提供 `purrcode` 和 `purrcoded` 两个命令。也可以直接从 GitHub 安装已签名 launcher：

```bash
npm install --global https://github.com/Weilin0723/PurrCode/releases/latest/download/purrcode-1.0.0.tgz
```

### Windows

从[最新发布](https://github.com/Weilin0723/PurrCode/releases/latest)下载并解压
`purrcode-x86_64-pc-windows-msvc.zip`。

### 从源码构建

需要 Rust 1.88 或更高版本、Git 以及对应平台的构建工具：

```bash
# 克隆并构建全部（CLI、daemon 和原生 IDE）
git clone https://github.com/Weilin0723/PurrCode.git
cd PurrCode
cargo build --release

# 二进制文件位于 target/release/：
#   purrcode        — CLI + 终端 Workbench + IDE 启动器
#   purrcoded       — 后台 daemon
```

开发时使用 `cargo build` 生成调试二进制文件。建议实际使用时执行 `cargo build --release`——调试模式下 IDE 启动明显更慢，因为 egui 渲染未优化。

## 三步开始使用

```bash
# 1. 发现本地模型供应商、创建安全默认配置并启动 daemon
purrcode init

# 2. 进入项目仓库
cd your-project

# 3. 打开终端 Workbench —— 或打开原生桌面 IDE
purrcode                  # 终端 Workbench
purrcode ide              # 原生桌面 IDE（当前目录）
purrcode ide --repository /path/to/project   # 指定仓库路径打开 IDE
```

### 打开 IDE

```bash
# 命令行
purrcode ide                          # 在当前目录打开 IDE
purrcode ide --repository "$PWD"      # 显式指定仓库路径
purrcode ide --session <UUID> --repository "$PWD"  # 恢复指定会话

# 在终端 Workbench 中
/ide                                  # 打开 IDE 并附加到当前会话
```

IDE 和终端 Workbench 共享同一个 daemon 会话，可以随时切换——TUI 中输入 `/ide` 打开桌面窗口，`purrcode resume --tui` 重新打开终端视图，任何方向都不会丢失数据。

IDE 是纯 Rust 原生桌面应用（`eframe`/`egui`）。它不会打开浏览器，不依赖 VS Code / Electron / Tauri，并作为独立进程运行（macOS 和 Windows 要求桌面事件循环拥有主线程）。

在 TUI 内使用 `/connect` 即可发现 Ollama 或 LM Studio，也可以配置远程供应商，无需手动编辑
TOML。凭据存储在操作系统密钥库中，不会进入模型上下文或工具进程。

```text
/connect          发现并配置模型供应商
/connect import   粘贴 Python、JavaScript、cURL、JSON、YAML、TOML 或 dotenv 示例
/mode             切换任务模式：Ask、Plan、Build、Review
/permission       切换权限模式：Ask、Auto、Full Access
/ide              打开原生桌面 IDE 并附加到当前会话
```

## 常用命令

```bash
# 单次命令
purrcode plan "为订单 API 添加分页"          # 先规划，不写任何内容
purrcode run "实现分页并更新测试"

# 会话管理
purrcode sessions                           # 查看活动会话
purrcode resume                             # 恢复已暂停的会话（终端）
purrcode ide --session <UUID> --repository "$PWD"  # 恢复已暂停的会话（IDE）
purrcode rollback                           # 回滚隔离工作

# 审查与控制
purrcode review                             # 查看当前 diff
purrcode approve                            # 批准提议的操作
purrcode doctor                             # 环境诊断

# IDE
purrcode ide                          # 打开原生桌面 IDE
purrcode gui                          # 同 purrcode ide
```

Plan 模式在计划处暂停并继续接受回复——说明要改什么，计划会被改写为带编号的新修订版并再次暂停，
可以往复任意多轮，任何一轮都不会写入磁盘。确定之后用 `Build this plan`（或 `/resume`）在同一
会话内开始执行。

## v1.0 亮点

- **原生桌面 IDE**：对话 Workbench、artifact 卡片、语义活动、composer 控件、语法高亮编辑器，
  以及停靠的 Diff/Tests/Terminal/Problems/Output 面板——全部由 PurrCode 自己绘制。
- **统一的会话状态**：TUI、IDE、CLI 共享同一个由 daemon 持有的权威会话模型。
- **可真正选择的模式**：`Ctrl+K` / `/mode` 切换 Ask、Plan、Build、Review；`/permission` 切换
  Ask、Auto、Full Access。只读模式是 daemon 强制执行的约束而非提示。
- **两个客户端中的真正终端**：IDE 复用 daemon 的跨平台 PTY，支持增量输出、输入、停止和
  ownership generation。
- **自适应工作流编排**：基于任务证据选择 Direct/Standard/Ultra 工作流。
- **多种安全凭据**：Provider/模型/密钥路由，带预算强制与用量核算。
- **GitHub 原生交付**：branch、commit、push、pull request 和 checks。
- **NVIDIA NIM 一等支持**：初始化时自动检测 `NVIDIA_API_KEY`。
- **基于证据的模型选择**：名称按词元解析、体积按主机内存判断、已验证的工具调用能力优先。
- **统一的呈现契约**：类型化的 activity/validation/summary 端点，客户端不再各自解读持久化
  事件日志。

## 安全与验证

PurrCode 在 macOS 上使用 `sandbox-exec`，在受支持的 Linux 主机上使用 Bubblewrap。较弱的主机
隔离能力会被如实标记，绝不会伪装成完整沙箱。智能体的修改在 PurrCode 托管的独立 Git worktree
中进行；你已有的未提交内容绝不会被静默 stash、覆盖或丢弃。在敏感仓库中使用前，请阅读
[安全模型](docs/security.md)、[架构说明](docs/architecture.md)和
[生产验收审计](docs/production-acceptance.md)。

仓库验证命令：

```bash
cargo fmt --all --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
npm test --prefix packages/purrcode
npm test --prefix sdk/typescript
PYTHONPATH=sdk/python/src python3 -m unittest discover -s sdk/python/tests -v
```

## 文档

- [安装](docs/installation.md)
- [供应商配置](docs/providers.md)
- [架构](docs/architecture.md)
- [安全](docs/security.md)
- [恢复](docs/recovery.md)
- [故障排查](docs/troubleshooting.md)
- [实现状态](docs/implementation-status.md)
- [Wiki](https://github.com/Weilin0723/PurrCode/wiki) —— 指南、模式、v1.0 IDE 与发布说明
- [PurrCode v1.0 Master PRD](docs/prd/PurrCode_v1.0_Codex_Master_PRD.md)

PurrCode 仍在积极开发中。请查看实现状态和发布说明，确认已经验证的能力以及仍待完成的平台专项
验收。

## 许可证

Apache-2.0，详见 [LICENSE](LICENSE)。
