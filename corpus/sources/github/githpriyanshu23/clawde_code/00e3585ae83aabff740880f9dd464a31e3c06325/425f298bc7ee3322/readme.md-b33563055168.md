> Note: The original unmodified leaked source is preserved in the backup branch.

# Claude Code - Leaked Source (2026-03-31)

On March 31, 2026, the full source code of Anthropic's Claude Code CLI was leaked via a `.map` file exposed in their npm registry.

## How It Leaked

Chaofan Shou (@Fried_rice) discovered the leak and posted it publicly:

"Claude code source code has been leaked via a map file in their npm registry!"

- @Fried_rice, March 31, 2026

The source map file in the published npm package contained a reference to the full, unobfuscated TypeScript source, which was downloadable as a zip archive from Anthropic's R2 storage bucket.

## Overview

Claude Code is Anthropic's official CLI tool that lets you interact with Claude directly from the terminal to perform software engineering tasks - editing files, running commands, searching codebases, managing git workflows, and more.

This repository contains the leaked `src/` directory.

- Leaked on: 2026-03-31
- Language: TypeScript
- Runtime: Bun
- Terminal UI: React + Ink (React for CLI)
- Scale: ~1,900 files, 512,000+ lines of code

## Directory Structure

```text
src/
|- main.tsx                 # Entrypoint (Commander.js-based CLI parser)
|- commands.ts              # Command registry
|- tools.ts                 # Tool registry
|- Tool.ts                  # Tool type definitions
|- QueryEngine.ts           # LLM query engine (core Anthropic API caller)
|- context.ts               # System/user context collection
|- cost-tracker.ts          # Token cost tracking
|
|- commands/                # Slash command implementations (~50)
|- tools/                   # Agent tool implementations (~40)
|- components/              # Ink UI components (~140)
|- hooks/                   # React hooks
|- services/                # External service integrations
|- screens/                 # Full-screen UIs (Doctor, REPL, Resume)
|- types/                   # TypeScript type definitions
|- utils/                   # Utility functions
|
|- bridge/                  # IDE integration bridge (VS Code, JetBrains)
|- coordinator/             # Multi-agent coordinator
|- plugins/                 # Plugin system
|- skills/                  # Skill system
|- keybindings/             # Keybinding configuration
|- vim/                     # Vim mode
|- voice/                   # Voice input
|- remote/                  # Remote sessions
|- server/                  # Server mode
|- memdir/                  # Memory directory (persistent memory)
|- tasks/                   # Task management
|- state/                   # State management
|- migrations/              # Config migrations
|- schemas/                 # Config schemas (Zod)
|- entrypoints/             # Initialization logic
|- ink/                     # Ink renderer wrapper
|- buddy/                   # Companion sprite (Easter egg)
|- native-ts/               # Native TypeScript utils
|- outputStyles/            # Output styling
|- query/                   # Query pipeline
+- upstreamproxy/           # Proxy configuration
```

## Core Architecture

### 1. Tool System (src/tools/)

Every tool Claude Code can invoke is implemented as a self-contained module. Each tool defines its input schema, permission model, and execution logic.

| Tool | Description |
|---|---|
| BashTool | Shell command execution |
| FileReadTool | File reading (images, PDFs, notebooks) |
| FileWriteTool | File creation / overwrite |
| FileEditTool | Partial file modification (string replacement) |
| GlobTool | File pattern matching search |
| GrepTool | ripgrep-based content search |
| WebFetchTool | Fetch URL content |
| WebSearchTool | Web search |
| AgentTool | Sub-agent spawning |
| SkillTool | Skill execution |
| MCPTool | MCP server tool invocation |
| LSPTool | Language Server Protocol integration |
| NotebookEditTool | Jupyter notebook editing |
| TaskCreateTool / TaskUpdateTool | Task creation and management |
| SendMessageTool | Inter-agent messaging |
| TeamCreateTool / TeamDeleteTool | Team agent management |
| EnterPlanModeTool / ExitPlanModeTool | Plan mode toggle |
| EnterWorktreeTool / ExitWorktreeTool | Git worktree isolation |
| ToolSearchTool | Deferred tool discovery |
| CronCreateTool | Scheduled trigger creation |
| RemoteTriggerTool | Remote trigger |
| SleepTool | Proactive mode wait |
| SyntheticOutputTool | Structured output generation |

### 2. Command System (src/commands/)

User-facing slash commands invoked with / prefix.

| Command | Description |
|---|---|
| /commit | Create a git commit |
| /review | Code review |
| /compact | Context compression |
| /mcp | MCP server management |
| /config | Settings management |
| /doctor | Environment diagnostics |
| /login / /logout | Authentication |
| /memory | Persistent memory management |
| /skills | Skill management |
| /tasks | Task management |
| /vim | Vim mode toggle |
| /diff | View changes |
| /cost | Check usage cost |
| /theme | Change theme |
| /context | Context visualization |
| /pr_comments | View PR comments |
| /resume | Restore previous session |
| /share | Share session |
| /desktop | Desktop app handoff |
| /mobile | Mobile app handoff |

### 3. Service Layer (src/services/)

| Service | Description |
|---|---|
| api/ | Anthropic API client, file API, bootstrap |
| mcp/ | Model Context Protocol server connection and management |
| oauth/ | OAuth 2.0 authentication flow |
| lsp/ | Language Server Protocol manager |
| analytics/ | GrowthBook-based feature flags and analytics |
| plugins/ | Plugin loader |
| compact/ | Conversation context compression |
| policyLimits/ | Organization policy limits |
| remoteManagedSettings/ | Remote managed settings |
| extractMemories/ | Automatic memory extraction |
| tokenEstimation.ts | Token count estimation |
| teamMemorySync/ | Team memory synchronization |

### 4. Bridge System (src/bridge/)

A bidirectional communication layer connecting IDE extensions (VS Code, JetBrains) with the Claude Code CLI.

- bridgeMain.ts - Bridge main loop
- bridgeMessaging.ts - Message protocol
- bridgePermissionCallbacks.ts - Permission callbacks
- replBridge.ts - REPL session bridge
- jwtUtils.ts - JWT-based authentication
- sessionRunner.ts - Session execution management

### 5. Permission System (src/hooks/toolPermission/)

Checks permissions on every tool invocation. Either prompts the user for approval/denial or automatically resolves based on the configured permission mode (default, plan, bypassPermissions, auto, etc.).

### 6. Feature Flags

Dead code elimination via Bun's `bun:bundle` feature flags:

```typescript
import { feature } from 'bun:bundle'

// Inactive code is completely stripped at build time
const voiceCommand = feature('VOICE_MODE')
  ? require('./commands/voice/index.js').default
  : null
```

Notable flags: PROACTIVE, KAIROS, BRIDGE_MODE, DAEMON, VOICE_MODE, AGENT_TRIGGERS, MONITOR_TOOL

## Key Files in Detail

### QueryEngine.ts (~46K lines)

The core engine for LLM API calls. Handles streaming responses, tool-call loops, thinking mode, retry logic, and token counting.

### Tool.ts (~29K lines)

Defines base types and interfaces for all tools - input schemas, permission models, and progress state types.

### commands.ts (~25K lines)

Manages registration and execution of all slash commands. Uses conditional imports to load different command sets per environment.

### main.tsx

Commander.js-based CLI parser + React/Ink renderer initialization. At startup, parallelizes MDM settings, keychain prefetch, and GrowthBook initialization for faster boot.

## Tech Stack

| Category | Technology |
|---|---|
| Runtime | Bun |
| Language | TypeScript (strict) |
| Terminal UI | React + Ink |
| CLI Parsing | Commander.js (extra-typings) |
| Schema Validation | Zod v4 |
| Code Search | ripgrep (via GrepTool) |
| Protocols | MCP SDK, LSP |
| API | Anthropic SDK |
| Telemetry | OpenTelemetry + gRPC |
| Feature Flags | GrowthBook |
| Auth | OAuth 2.0, JWT, macOS Keychain |

## Notable Design Patterns

### Parallel Prefetch

Startup time is optimized by prefetching MDM settings, keychain reads, and API preconnect in parallel - before heavy module evaluation begins.

```typescript
// main.tsx - fired as side-effects before other imports
startMdmRawRead()
startKeychainPrefetch()
```

### Lazy Loading

Heavy modules (OpenTelemetry ~400KB, gRPC ~700KB) are deferred via dynamic `import()` until actually needed.

### Agent Swarms

Sub-agents are spawned via AgentTool, with coordinator/ handling multi-agent orchestration. TeamCreateTool enables team-level parallel work.

### Skill System

Reusable workflows defined in skills/ and executed through SkillTool. Users can add custom skills.

### Plugin Architecture

Built-in and third-party plugins are loaded through the plugins/ subsystem.

## GitPretty Setup (Per-File Pretty Commits)

If you want GitHub's file UI to show visually distinct commit messages per file, use the helper script in this repo:

```bash
bash ./gitpretty-apply.sh .
```

This will:

1. Clone gitpretty into ~/.gitpretty (first run only)
2. Make scripts executable
3. Run emoji-file-commits.sh against this repo

Optional: install auto-emoji hooks for future commits:

```bash
bash ./gitpretty-apply.sh . --hooks
```

After running, push as usual:

```bash
git push origin main
```

## Use It in Claude Code (MCP Server)

This repo includes an MCP server that lets you explore the Claude Code source directly from any Claude session. One command to set it up:

### Quick Start

```bash
# Clone the repo (if you haven't already)
git clone https://github.com/Atharvsinh-codez/claude-code.git
cd claude-code/mcp-server

# Install dependencies and build
npm install && npm run build

# Add to Claude Code (run from the repo root)
claude mcp add claude-code-explorer -- node /absolute/path/to/claude-code/mcp-server/dist/index.js
```

Replace /absolute/path/to/claude-code with the actual path where you cloned the repo.

Or as a single copy-paste block (clones, builds, and registers in one go):

```bash
git clone https://github.com/Atharvsinh-codez/claude-code.git ~/claude-code \
  && cd ~/claude-code/mcp-server \
  && npm install && npm run build \
  && claude mcp add claude-code-explorer -- node ~/claude-code/mcp-server/dist/index.js
```

### What You Get

Once added, Claude has access to these tools for exploring the codebase:

| Tool | Description |
|---|---|
| list_tools | List all ~40 agent tools with source files |
| list_commands | List all ~50 slash commands with source files |
| get_tool_source | Read full source of any tool (e.g. BashTool, FileEditTool) |
| get_command_source | Read source of any slash command (e.g. review, mcp) |
| read_source_file | Read any file from src/ by path |
| search_source | Grep across the entire source tree |
| list_directory | Browse src/ directories |
| get_architecture | High-level architecture overview |

Plus prompts for guided exploration:

- explain_tool - Deep-dive into how a specific tool works
- explain_command - Understand a slash command's implementation
- architecture_overview - Guided tour of the full architecture
- how_does_it_work - Explain any subsystem (permissions, MCP, bridge, etc.)
- compare_tools - Side-by-side comparison of two tools

### Example Usage

After adding the MCP server, just ask Claude naturally:

"How does the BashTool work?"
"Search for where permissions are checked"
"Show me the /review command source"
"Explain the MCP client integration"

### Custom Source Path

If your src/ directory is in a non-standard location, set the environment variable:

```bash
claude mcp add claude-code-explorer -e CLAUDE_CODE_SRC_ROOT=/path/to/src -- node /path/to/mcp-server/dist/index.js
```

### Remove It

```bash
claude mcp remove claude-code-explorer
```

## Disclaimer

This repository archives source code that was leaked from Anthropic's npm registry on 2026-03-31. All original source code is the property of Anthropic.
