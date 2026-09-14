<p align="center">
  <img src="./apps/desktop/src-tauri/icons/128x128.png" alt="Ore Code icon" width="104" height="104">
</p>

<h1 align="center">Ore Code</h1>

<p align="center">
  <strong>A DeepSeek-first desktop coding agent workbench for real projects.</strong>
</p>

<p align="center">
  Long-context coding, structured tool execution, local project context, DeepSeek / Mimo / Ark Coding providers, MCP integrations, skills, automation, and a native desktop shell for macOS and Windows.
</p>

<p align="center">
  <a href="https://github.com/233i/ore-code/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/233i/ore-code?style=flat-square"></a>
  <a href="./LICENSE"><img alt="License" src="https://img.shields.io/github/license/233i/ore-code?style=flat-square"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-macOS%20Apple%20Silicon-24292f?style=flat-square">
  <img alt="Built with Tauri" src="https://img.shields.io/badge/Tauri-2.x-24c8db?style=flat-square">
</p>

<p align="center">
  <a href="https://github.com/233i/ore-code/releases/download/v0.1.1/Ore.Code_0.1.1_aarch64.dmg"><strong>Download for macOS</strong></a>
  ·
  <a href="https://github.com/233i/ore-code/releases/latest"><strong>Windows build pending</strong></a>
  ·
  <a href="./docs/README.md">Docs</a>
  ·
  <a href="./README.zh-CN.md">简体中文</a>
</p>

![Ore Code home screen](./docs/assets/ore-code-home.png)

## What It Is

Ore Code is a desktop coding agent built around real workspace context. It combines a TypeScript agent runtime, a React/Tauri desktop app, and a Rust OS boundary for local file, shell, process, Git, keychain, artifact, and MCP operations.

It is designed for coding sessions where the agent needs to inspect the project, run commands, keep track of long conversations, and show exactly what changed.

## Highlights

| Coding workflow | Local execution | Context control |
| --- | --- | --- |
| Chat with a project-aware agent, review diffs, restore task changes, and keep task status visible. | Run file, shell, process, Git, test, web fetch, artifact, and MCP tools through a native desktop boundary. | Use history compression, context briefing, checkpoint summaries, usage visibility, and provider-aware request shaping. |

| Configuration | Skills and MCP | Release targets |
| --- | --- | --- |
| Configure DeepSeek, Mimo, Ark Coding, or custom endpoints in `~/.ore-code/config.toml`; keep API keys in the OS keychain. | Add reusable skills and connect user-level MCP servers. | Current release ships a macOS Apple Silicon installer; Windows x64 packaging is built separately. |

## Download

Latest release: [Ore Code v0.1.1](https://github.com/233i/ore-code/releases/tag/v0.1.1)

| Platform | Installer | SHA-256 |
| --- | --- | --- |
| macOS Apple Silicon | [`Ore.Code_0.1.1_aarch64.dmg`](https://github.com/233i/ore-code/releases/download/v0.1.1/Ore.Code_0.1.1_aarch64.dmg) | `988e5ff9c021f6d8cd2632686791d62e730170338803805b11399b273c627d61` |
| Windows x64 | Pending Windows build | - |

Only install builds downloaded from this repository's GitHub Releases.

### macOS Install Note

The macOS build is ad-hoc signed and not notarized because the project is not using an Apple Developer ID certificate yet. If macOS blocks the app:

1. Control-click or right-click `Ore Code.app`.
2. Choose **Open**.
3. Confirm **Open** again.
4. If needed, use **System Settings > Privacy & Security > Open Anyway**.

### Windows Install Note

Windows may show a SmartScreen warning for early builds. If you downloaded the installer from the official release page, choose **More info** and then **Run anyway**.

## Repository Layout

```text
apps/desktop/          Tauri desktop application
packages/protocol/     Runtime event schemas and shared protocol types
packages/tools/        Tool specifications, approval policy, and tool helpers
packages/agent-core/   Agent engine, prompts, runtime context, and model adapters
packages/state/        Session/event/artifact storage helpers
packages/harness/      Scenario replay and harness tests
docs/                  Product, architecture, workflow, and project planning docs
scripts/               Local helper scripts
```

## Development

Prerequisites:

- Node.js 20+; Node 22 is the pinned development and CI version in `.node-version`.
- pnpm 11.x. This repo declares `pnpm@11.0.8` in `packageManager`.
- Rust stable with Cargo.
- Tauri 2 system prerequisites for your OS.
- Git.

Start the desktop app:

```bash
pnpm install
pnpm dev
```

Run local checks:

```bash
pnpm ci:local
pnpm --filter @ore-code/desktop smoke
```

Build installers:

```bash
pnpm --filter @ore-code/desktop tauri:build
pnpm build:desktop:windows
```

## Configuration and Local Data

Ore Code keeps user-level runtime data outside the repository:

- `~/.ore-code/config.toml` for provider/model/base URL/thinking configuration
- `~/.ore-code/mcp.json` for user-level MCP servers
- `~/.ore-code/skills` for user-level skills

Project-level `.ore-code/config.toml` files are not read by the current release.

## Documentation

- [Architecture overview](./docs/ARCHITECTURE_OVERVIEW.md)
- [Development guide](./docs/DEVELOPMENT.md)
- [Troubleshooting](./docs/TROUBLESHOOTING.md)
- [FAQ](./docs/FAQ.md)
- [Local data and configuration](./docs/LOCAL_DATA_AND_CONFIG.md)
- [Package boundaries and compatibility](./docs/API_AND_COMPATIBILITY.md)
- [Roadmap](./docs/ROADMAP.md)
- [Skill system](./docs/06-skill-system.md)
- [DeepSeek V4 context strategy](./docs/DEEPSEEK_V4_CONTEXT.md)
- [Known limitations](./docs/KNOWN_LIMITATIONS.md)

## Project

- [Contributing](./CONTRIBUTING.md)
- [Support](./SUPPORT.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Privacy](./PRIVACY.md)
- [Security](./SECURITY.md)
- [Changelog](./CHANGELOG.md)

## Star History

<a href="https://www.star-history.com/#233i/ore-code&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=233i/ore-code&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=233i/ore-code&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=233i/ore-code&type=Date" />
 </picture>
</a>

## License

Ore Code is released under the [MIT License](./LICENSE).
