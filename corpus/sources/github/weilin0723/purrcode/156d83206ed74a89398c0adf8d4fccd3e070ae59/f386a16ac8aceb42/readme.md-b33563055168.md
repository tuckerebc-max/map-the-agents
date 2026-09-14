<p align="center">
  <img src="brand/purrcode-logo-horizontal-light.png" alt="PurrCode" width="320" />
</p>

<p align="center">
  <b>A local-first coding agent with an independent, auditable judgment runtime.</b>
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="https://weilin0723.github.io/PurrCode/">Documentation</a> ·
  <a href="https://github.com/Weilin0723/PurrCode/wiki">Wiki</a> ·
  <a href="https://github.com/Weilin0723/PurrCode/releases/latest">Latest release</a>
</p>

<p align="center">
  <a href="https://github.com/Weilin0723/PurrCode/actions/workflows/ci.yml"><img src="https://github.com/Weilin0723/PurrCode/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://github.com/Weilin0723/PurrCode/releases/latest"><img src="https://img.shields.io/github/v/release/Weilin0723/PurrCode" alt="Release" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Weilin0723/PurrCode" alt="License" /></a>
</p>

> Models propose. PawGate authorizes. Claw executes. Evidence decides.

PurrCode is a terminal coding agent that works in isolated Git worktrees. It is built around a simple idea: model output is a *proposal*, never authority. Every native action is bound to a durable authorization, checked again immediately before execution, and followed by recorded validation. Repository content, model output, and downloaded skills remain untrusted.

PurrCode v1.0 adds its own **native desktop IDE** — a pure-Rust desktop application, not a browser portal and not an extension inside somebody else's editor. `purrcode ide` opens a real window on the same session the terminal TUI is running, so you can move between them without losing anything.

## Screens

- **Terminal Workbench** — the default interface. `purrcode` opens it on every platform and never an unexpected browser.
- **Native desktop IDE** — `purrcode ide` (or `purrcode gui`, the same command). A pure-Rust desktop window with a conversation Workbench, a syntax-highlighted editor, and a docked Diff/Tests/Terminal/Problems/Output panel.
- **Studio** — `purrcode studio`. A secure browser-based maintenance client for daemon health, sessions, and environment inspection. It is not the v1.0 release IDE and nothing routes to it automatically.

## Install

### macOS — drag-and-drop app

The easiest way to try the native desktop IDE: download **PurrCode.app**, drag it into **/Applications**, and double-click — no terminal required.

1. Download `PurrCode.app.zip` from the [latest release](https://github.com/Weilin0723/PurrCode/releases/latest).
2. Unzip it and drag **PurrCode.app** into **Applications**.
3. Double-click PurrCode to open the native desktop IDE. The first launch creates your config and starts the loopback daemon automatically; subsequent launches reuse it.

> Gatekeeper note: the app is not notarized, so macOS may show "PurrCode.app cannot be opened". Right-click the app and choose **Open**, then **Open** again to run it. We plan to notarize future releases.

### macOS and Linux (terminal)

```bash
curl -fsSL https://raw.githubusercontent.com/Weilin0723/PurrCode/v1.0.0/scripts/install.sh | sh
```

The installer detects the host platform, downloads the release archive, verifies it against the release `SHA256SUMS`, and installs into `~/.local/bin`. Set `PURRCODE_INSTALL_DIR` to choose another destination.

### npm

```bash
npm install --global @minaovo/purrcode
```

Node.js 18 or newer. The package selects the correct macOS, Linux, or Windows binary, verifies its pinned SHA-256 digest, and exposes both `purrcode` and `purrcoded`. You can also install the signed-release launcher directly from GitHub:

```bash
npm install --global https://github.com/Weilin0723/PurrCode/releases/latest/download/purrcode-1.0.0.tgz
```

### Windows

Download and extract `purrcode-x86_64-pc-windows-msvc.zip` from the [latest release](https://github.com/Weilin0723/PurrCode/releases/latest).

### Build from source

Rust 1.88 or newer, Git, and your platform build tools:

```bash
# Clone and build everything (CLI, daemon, and native IDE)
git clone https://github.com/Weilin0723/PurrCode.git
cd PurrCode
cargo build --release

# The binaries are in target/release/:
#   purrcode        — CLI + terminal Workbench + IDE launcher
#   purrcoded       — background daemon
```

For development, `cargo build` produces debug binaries. `cargo build --release` is recommended for actual use — the debug IDE starts noticeably slower because egui rendering is not optimized in debug mode.

## Quick start

```bash
# 1. Discover local providers, write secure defaults, and start the daemon
purrcode init

# 2. Open a repository
cd your-project

# 3. Start the terminal Workbench — or open the native desktop IDE
purrcode                  # terminal Workbench
purrcode ide              # native desktop IDE (current directory)
purrcode ide --repository /path/to/project   # IDE for a specific repo
```

### Opening the IDE

```bash
# From the command line
purrcode ide                          # open IDE for the current directory
purrcode ide --repository "$PWD"      # explicit repository path
purrcode ide --session <UUID> --repository "$PWD"  # resume a specific session

# From inside the terminal Workbench
/ide                                  # opens the IDE attached to the same session
```

The IDE and terminal Workbench share one daemon session. You can move between them freely — `/ide` in the TUI opens the desktop window, and `purrcode resume --tui` reopens the terminal view. Nothing is lost in either direction.

The IDE is a pure-Rust native desktop application (`eframe`/`egui`). It does not open a browser, does not depend on VS Code / Electron / Tauri, and runs as its own process (macOS and Windows require the desktop event loop to own the main thread).

Inside the TUI, `/connect` discovers Ollama or LM Studio and configures remote providers — no manual TOML editing. Credentials are stored in the operating-system credential store and never enter the model context or tool processes.

```text
/connect          discover and configure a model provider
/connect import   paste a Python, JavaScript, cURL, JSON, YAML, TOML, or dotenv example
/mode             switch task mode: Ask, Plan, Build, Review
/permission       switch permission mode: Ask, Auto, Full Access
/ide              open the native desktop IDE attached to this session
```

## Usage

```bash
# One-shot commands
purrcode plan "Add pagination to the orders API"   # plan first, write nothing
purrcode run "Implement pagination and update tests"

# Session management
purrcode sessions                                  # review active sessions
purrcode resume                                    # resume a paused session (terminal)
purrcode ide --session <UUID> --repository "$PWD"  # resume a paused session (IDE)
purrcode rollback                                  # roll back isolated work

# Review and control
purrcode review                                    # review the current diff
purrcode approve                                   # approve a proposed action
purrcode doctor                                    # environment diagnostics

# IDE
purrcode ide                          # open the native desktop IDE
purrcode gui                          # same as `purrcode ide`
```

Plan mode pauses on its plan and stays open to a reply — say what to change and the plan is rewritten as a numbered revision and paused again, for as many rounds as you need. Nothing is written to disk in any of them. `Build this plan` (or `/resume`) turns the plan you settled on into the work, in the same session.

## v1.0 highlights

- **Native desktop IDE**: conversation Workbench, artifact cards, semantic activity, composer controls, syntax-highlighted editor, and a docked Diff/Tests/Terminal/Problems/Output panel — all drawn by PurrCode itself.
- **Unified session state**: TUI, IDE, and CLI share one authoritative daemon-owned session model.
- **Selectable modes**: `Ctrl+K` / `/mode` switches Ask, Plan, Build, Review; `/permission` switches Ask, Auto, Full Access. A read-only mode is a constraint the daemon enforces, not a hint.
- **A real terminal in both clients**: the IDE reuses the daemon's cross-platform PTY with incremental output, input, stop, and ownership generations.
- **Adaptive workflow orchestration**: Direct/Standard/Ultra workflow selection based on task evidence.
- **Multiple secure credentials**: provider/model/key routing with budget enforcement and usage accounting.
- **GitHub-native completion**: branch, commit, push, pull request, and checks.
- **NVIDIA NIM as a first-class provider**: `NVIDIA_API_KEY` is detected during onboarding.
- **Evidence-based model selection**: names parsed as tokens, size judged against host memory, proven tool-calling prioritized.
- **One presentation vocabulary**: typed activity/validation/summary endpoints, so clients no longer each invent a reading of the durable event log.

## Security and verification

PurrCode uses `sandbox-exec` on macOS and Bubblewrap on supported Linux hosts. Weaker host isolation is reported accurately and never presented as a full sandbox. Agent work runs in detached Git worktrees under PurrCode-managed storage; your existing uncommitted work is never silently stashed, overwritten, or discarded. Read the [security model](docs/security.md), [architecture](docs/architecture.md), and [production acceptance audit](docs/production-acceptance.md) before using PurrCode for sensitive repositories.

Repository checks:

```bash
cargo fmt --all --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
npm test --prefix packages/purrcode
npm test --prefix sdk/typescript
PYTHONPATH=sdk/python/src python3 -m unittest discover -s sdk/python/tests -v
```

## Documentation

The [PurrCode documentation site](https://weilin0723.github.io/PurrCode/) has the full guides: Installation, Quick Start, Modes, Providers and Models, the v1.0 IDE, CLI Reference, Architecture, Security, Recovery, and Troubleshooting. The [wiki](https://github.com/Weilin0723/PurrCode/wiki) mirrors it.

In-repo references:

- [Installation](docs/installation.md)
- [Provider setup](docs/providers.md)
- [Architecture](docs/architecture.md)
- [Security](docs/security.md)
- [Recovery](docs/recovery.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Implementation status](docs/implementation-status.md)
- [Wiki](https://github.com/Weilin0723/PurrCode/wiki) — guides, modes, the v1.0 IDE, and release notes
- [PurrCode v1.0 Master PRD](docs/prd/PurrCode_v1.0_Codex_Master_PRD.md)

PurrCode is under active development. Consult the implementation status and release notes for verified capabilities and remaining platform-specific gates.

## License

Apache-2.0. See [LICENSE](LICENSE).
