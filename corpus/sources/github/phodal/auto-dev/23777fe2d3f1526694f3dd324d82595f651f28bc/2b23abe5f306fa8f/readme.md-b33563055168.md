# AutoDev 3.0 Xiuper (Alpha)

> **One Platform. All Phases. Every Device.**  
> 统一平台 · 全开发阶段 · 跨全设备

**AutoDev Xiuper** is an AI-native, multi-agent development platform built on Kotlin Multiplatform. Based on the current codebase,
it focuses on document research, coding, code review, data query, artifact generation, and web interaction workflows, and targets
IntelliJ IDEA, VS Code, CLI, Desktop JVM, Android, iOS, JS/WASM Web, and Server runtimes.

![ScreenShot](https://xiuper.com/screenshot.png)

## One Platform Architecture

![AutoDev Xiuper One Platform Architecture](https://xiuper.com/xiuper-arch.svg)

## Get Started

### Download AutoDev Xiuper

- **IntelliJ IDEA Plugin**: [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/29223-autodev-experiment)
- **VSCode Extension**: [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Phodal.autodev)
- **CLI Tool**: `npm install -g @xiuper/cli`
- **Web App**: [web.xiuper.com](https://web.xiuper.com/)
- **Desktop & Android**: [GitHub Releases](https://github.com/phodal/auto-dev/releases)
- **iOS**: Build from source.

### Previous Versions

- **AutoDev 2.0** (Stable): [Branch](https://github.com/phodal/auto-dev/tree/autodev2) | [Plugin](https://plugins.jetbrains.com/plugin/26988)

### Modules

| Module | Platform | Current Status | Description |
|--------|----------|----------------|-------------|
| **mpp-core** | Shared KMP runtime | ✅ In default build | Shared agent engine, tools, MCP integration, AGENTS.md loading |
| **mpp-ui** | Desktop / Android / iOS / JS / WASM | ✅ In default build | Main multiplatform UI surface and app entrypoints |
| **mpp-server** | JVM server | ✅ In default build | Ktor-based remote coding agent server |
| **mpp-idea** | IntelliJ IDEA | ✅ Composite build | IDEA plugin with dedicated renderers and toolwindow integration |
| **mpp-vscode** | VS Code | ✅ Standalone package in repo | VS Code extension backed by `mpp-core` JS bindings |
| **mpp-viewer / mpp-viewer-web** | Shared viewer stack | ✅ In default build | Diagram/viewer support used by UI surfaces |
| **xiuper-ui / xiuper-fs / xiuper-e2e** | Shared support modules | ✅ In default build | UI foundation, cross-platform file system, and E2E support |
| **mpp-ios** | iOS app shell | 🔄 Present in repo | Native iOS wrapper and build scripts, not included in current root Gradle graph |
| **mpp-web** | Landing / demo web | 🔄 Present in repo | Vite-based landing page and demo web entry, not included in current root Gradle graph |

### Current Status Snapshot

- The default root Gradle build currently includes `mpp-core`, `mpp-ui`, `mpp-codegraph`, `mpp-server`, `mpp-viewer`, `mpp-viewer-web`, `xiuper-ui`, `xiuper-fs`, and `xiuper-e2e`, with `mpp-idea` as a composite build.
- `mpp-ui` is the main cross-platform application module and already declares JVM, Android, iOS, JS, and WASM targets.
- `mpp-vscode`, `mpp-ios`, and `mpp-web` are maintained in the repository, but they are not part of the current root `settings.gradle.kts` default build graph.

### Key Features

**Xiuper Edition** currently exposes these code-backed capabilities:

- **Unified KMP Runtime**: Shared agent/runtime code across JVM, Android, iOS, JS, and WASM targets
- **Core Agents in Code**: `DocumentAgent`, `CodingAgent`, `CodeReviewAgent`, `ChatDBAgent`, and `ArtifactAgent`
- **Tool-Driven Coding Agent**: Built-in file system, grep/glob, shell, web fetch, MCP tools, and renderer integration
- **Project Rule Awareness**: Automatic `AGENTS.md` discovery and prompt injection from project hierarchy
- **SubAgent Architecture**: Analysis, error recovery, NanoDSL, chart/plot, codebase investigation, domain dictionary, SQL revision, and web agent flows
- **IDE Workflow Features**: PR review, pre-push review, diagram-related review flows, chat history, token usage, and model/tool configuration UIs
- **Agent Ecosystem Support**: MCP, A2A agent commands, Claude Skill loading, and SpecKit command integration
- **Multi-LLM Support**: OpenAI, Anthropic, Google, DeepSeek, Ollama, and more
- **Code Intelligence**: Tree-sitter based parsing for Java, Kotlin, Python, JavaScript/TypeScript, Go, Rust, C#
- **Global Ready**: Full internationalization (Chinese/English)

## Built-in Agents

AutoDev Xiuper currently has the following code-backed top-level agents and adjacent agent capabilities:

| Agent | Area | Description | Capabilities | Status |
|-------|------|-------------|--------------|--------|
| **Document / Knowledge** | Requirements / Research | `DocumentAgent` for document querying and feature tree generation | DocQL / analysis sub-agent / feature tree | ✅ Code-backed |
| **Coding** | Development | `CodingAgent` with workspace tools and orchestration | File system / shell / MCP / sub-agents / AGENTS.md | ✅ Code-backed |
| **Review** | Code Review | `CodeReviewAgent` for review, lint summary, and fix generation | Linter / diff review / PR review services | ✅ Code-backed |
| **ChatDB** | Data | `ChatDBAgent` for natural-language database interaction | Schema linking / SQL generation / SQL revision | ✅ Code-backed |
| **Artifact** | Rapid Prototyping | `ArtifactAgent` for self-contained runnable outputs | HTML / React / Node.js / Python / SVG / Mermaid | ✅ Code-backed |
| **Web Agent / WebEdit** | Web Interaction | Web interaction capability exists as web-agent and WebEdit UI flows | Page inspection / DOM context / chat-assisted actions | 🔄 Experimental |

Testing-related capability currently exists mainly through `xiuper-e2e` and E2E-oriented agent/tooling work, but it is not yet represented as a clearly separated top-level agent in the current code layout.

### SubAgents

SubAgents are specialized micro-agents invoked by the main Coding Agent for focused tasks. They follow the "agent as tool" architecture pattern:

| SubAgent                  | Purpose                                                                                  | Key Features                                                                          | Platform Support      |
|---------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------|
| **NanoDSL Agent**         | Generate AI-native UI code from natural language descriptions                            | Token-efficient DSL / Component generation / State management / HTTP requests         | All platforms         |
| **PlotDSL Agent**         | Generate statistical charts and data visualizations from natural language                | ggplot2-inspired syntax / Multiple chart types / Themes / Lets-Plot rendering         | JVM Desktop & Android |
| **Chart Agent**           | Generate chart configurations for ComposeCharts library                                  | Pie/Line/Column/Row charts / Data analysis / Cross-platform rendering                 | All platforms         |
| **Analysis Agent**        | Intelligently analyze and summarize any type of content (logs, errors, JSON, code, etc.) | Content type detection / Smart summarization / Metadata extraction                    | All platforms         |
| **Codebase Investigator** | Investigate codebase structure, patterns, dependencies, and architectural issues         | Architecture analysis / Pattern detection / Dependency mapping / Issue identification | All platforms         |
| **Domain Dict Agent**     | Generate domain dictionaries from codebase analysis for better context understanding     | Hot file detection / Class/method extraction / Domain term identification             | All platforms         |
| **Error Recovery Agent**  | Analyze errors and suggest fixes with self-healing capabilities                          | Error pattern recognition / Fix suggestion / Auto-retry logic                         | All platforms         |
| **SQL Revise Agent**      | Revise and optimize SQL queries based on schema and execution feedback                   | Schema-aware correction / Query optimization / Syntax validation                      | All platforms         |
| **E2E Testing Agent**     | Perform end-to-end testing with visual understanding and self-healing locators           | Natural language test scenario generation / Multi-modal perception / Self-healing     | All platforms         |

SubAgents enable modular, composable workflows: complex work is decomposed into focused sub-tasks, each handled by a specialized agent.

## License

This code is distributed under the MPL 2.0 license. See `LICENSE` in this directory.
