# CyCode

CyCode is a lightweight AI coding agent that runs in your terminal. It uses an OpenAI-compatible Chat Completions API and provides built-in tools for reading files, applying precise edits, searching code, running shell commands, and delegating work to sub-agents.

It is designed for local software engineering workflows: understanding codebases, fixing bugs, refactoring code, generating focused changes, and automating repository-level tasks.

## Features

- **OpenAI-compatible API**: Works with OpenAI, DeepSeek, DashScope/Qwen, and other providers that support compatible Chat Completions APIs.
- **Terminal-first UX**: Starts an Ink-based TUI by default, with an automatic text REPL fallback when TTY rendering is unavailable.
- **One-shot mode**: Run a single prompt with `--message` or `--prompt` for scripts, automation, and CI-style usage.
- **Local coding tools**: Read files, apply exact text replacements, write files, run regex search, run glob search, and execute shell commands.
- **Session management**: Save, list, and resume conversations.
- **Context compression**: Compress long conversations to reduce the risk of exceeding the model context window.
- **Token and cost tracking**: Tracks prompt and completion tokens, with estimated cost for known models.

## Requirements

- Node.js 18 or later
- npm
- An OpenAI-compatible API key

## Quick Start

```bash
npm install
cp .env.example .env
npm run build
npm start
```

Edit `.env` and configure at least one API key:

```bash
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL=gpt-5-mini
```

For other compatible providers, you can also use `CYCODE_API_KEY`, `DEEPSEEK_API_KEY`, or `DASHSCOPE_API_KEY`.

## Usage

### Interactive Mode

```bash
npm start
```

After building, you can run the compiled CLI directly:

```bash
node dist/cli.js
```

If the package has been linked with `npm link`, run:

```bash
cycode
```

### One-Shot Tasks

```bash
node dist/cli.js -p "Read src/agent.ts and summarize the Agent execution flow"
node dist/cli.js -m "Add a focused README for this project"
```

### Use a Different Working Directory

```bash
node dist/cli.js --dir /path/to/project -p "Inspect the test structure in this repository"
```

### Override Model or API Settings

```bash
node dist/cli.js --model gpt-5-mini --base-url https://api.openai.com/v1 --api-key "$OPENAI_API_KEY"
```

## CLI Options

| Option | Description |
| --- | --- |
| `-m, --message <text>` | Run a one-shot message and skip interactive mode |
| `-p, --prompt <text>` | Alias for `--message` |
| `-r, --resume <id>` | Resume a saved session |
| `-d, --dir <path>` | Set the working directory, defaults to the current directory |
| `--model <name>` | Set the model name |
| `--base-url <url>` | Set the API base URL |
| `--api-key <key>` | Set the API key |
| `-V, --version` | Print the version |
| `-h, --help` | Show help |

## Interactive Commands

| Command | Description |
| --- | --- |
| `/help` | Show available commands |
| `/reset` | Clear the current conversation history |
| `/model` | Show the active model |
| `/model <name>` | Switch models during the current session |
| `/tokens` | Show token usage and estimated cost when available |
| `/compact` | Compress the current conversation context |
| `/diff` | Show files modified during the current session |
| `/save` | Save the current session |
| `/sessions` | List recently saved sessions |
| `quit` / `exit` | Exit CyCode |

## Configuration

CyCode loads `.env` from the current directory or a parent directory. Common configuration variables:

| Environment Variable | Description | Default |
| --- | --- | --- |
| `CYCODE_API_KEY` | CyCode-specific API key, highest priority | None |
| `OPENAI_API_KEY` | OpenAI API key | None |
| `DEEPSEEK_API_KEY` | DeepSeek API key | None |
| `DASHSCOPE_API_KEY` | DashScope API key | None |
| `CYCODE_MODEL` | CyCode-specific model name | `qwen3.6-plus` |
| `MODEL` | Generic model name | `qwen3.6-plus` |
| `OPENAI_BASE_URL` | OpenAI-compatible base URL | None |
| `CYCODE_BASE_URL` | CyCode-specific base URL | None |
| `DASHSCOPE_BASE_URL` | DashScope base URL | None |
| `MAX_TURNS` | Maximum tool-use turns for a single task | `50` |
| `CYCODE_MAX_TOKENS` | Maximum model output tokens per call | `4096` |
| `CYCODE_TEMPERATURE` | Model sampling temperature | `0` |
| `CYCODE_MAX_CONTEXT` | Context compression threshold | `128000` |
| `CYCODE_HOME` | Root directory for saved sessions | `~/.cycode` |

API key priority is: `CYCODE_API_KEY`, `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`, `DASHSCOPE_API_KEY`.

## Built-In Tools

CyCode exposes the following tools to the model:

| Tool | Description |
| --- | --- |
| `read_file` | Read file contents with optional line ranges |
| `edit_file` | Replace a unique text fragment and return a unified diff |
| `write_file` | Create a new file or fully rewrite a file |
| `bash` | Run a shell command in the working directory and return stdout/stderr |
| `grep` | Search file contents with a regular expression |
| `glob` | Find files with a glob pattern |
| `agent` | Spawn a sub-agent for complex subtasks |

The `bash` tool blocks several high-risk command patterns, such as forced recursive deletion, filesystem formatting, and piping downloaded scripts into a shell. This is not a complete sandbox. Run CyCode only in repositories and environments you trust.

## Project Structure

```text
.
├── src/
│   ├── agent.ts              # Agent loop, tool execution, and lifecycle events
│   ├── cli.ts                # CLI entry point and option parsing
│   ├── config.ts             # Environment and runtime configuration
│   ├── context.ts            # Context estimation and compression
│   ├── llm.ts                # OpenAI-compatible streaming client wrapper
│   ├── repl.ts               # Interactive entry point and text REPL fallback
│   ├── session.ts            # Session save, load, and list operations
│   ├── tool-registry.ts      # Tool registration and execution
│   ├── tools/                # Built-in tool implementations
│   └── tui/                  # Ink TUI UI and components
├── tests/                    # Node.js test runner tests
├── docs/                     # Design documentation
├── package.json
└── tsconfig.json
```

## Development

```bash
npm run build
npm test
npm run dev
```

Scripts:

| Script | Description |
| --- | --- |
| `npm run build` | Compile TypeScript into `dist/` |
| `npm start` | Run `dist/cli.js` |
| `npm run dev` | Build, then run the CLI |
| `npm test` | Build, then run `tests/*.test.mjs` |

## Programmatic API

After building, the core modules can be reused from the package entry point:

```ts
import { Agent, loadConfig, createToolRegistry } from "cycode";

const config = loadConfig({ workingDir: process.cwd() });
const registry = createToolRegistry(config);
const agent = new Agent(config, registry);

const result = await agent.run("Summarize the current project structure");
console.log(result);
```

## Sessions

Use `/save` in interactive mode to save the current session. Sessions are stored by default in:

```text
~/.cycode/sessions
```

Resume a session:

```bash
node dist/cli.js --resume session_20260627_abcdef12
```

To change the session storage root:

```bash
CYCODE_HOME=/path/to/cycode-home node dist/cli.js
```

## Notes

- CyCode can read and modify files in the working directory and execute shell commands. Use it in trusted workspaces.
- `edit_file` depends on exact text matching. If the target fragment is not unique, the edit is rejected and more context is required.
- One-shot mode preserves plain stdout behavior for scripting. Interactive mode prefers the TUI.
- Different compatible providers may vary in streaming, tool calling, and `stream_options` support. CyCode retries with a downgraded streaming request when needed.

## License

This repository does not currently declare a license. Add an explicit license before publishing or distributing the project.
