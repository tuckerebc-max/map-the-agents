# agent-test-tui Design

Simple REPL for testing mux-rs with Claude, tools, and MCP servers.

## Overview

Binary crate in the mux-rs workspace. Readline-based interface that:
- Chats with Claude via AnthropicClient
- Loads MCP servers from `.mcp.json`, proxies their tools
- Prompts for approval on each tool call
- Runs the full agentic loop until Claude stops calling tools

## Architecture

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────┐
│   User Input    │────▶│  Agent Loop  │────▶│   Claude    │
│   (rustyline)   │◀────│              │◀────│ (Anthropic) │
└─────────────────┘     └──────────────┘     └─────────────┘
                              │
                              ▼
                        ┌──────────┐
                        │ Registry │
                        │  Tools   │
                        └──────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │ MCP Srv1 │   │ MCP Srv2 │   │BuiltIns  │
        └──────────┘   └──────────┘   └──────────┘
```

## Core Loop

```
1. Load .mcp.json from cwd (or ~/.mcp.json fallback)
2. Connect to each MCP server, merge tools into registry
3. Print welcome message with tool count
4. Loop:
   a. Print "> " prompt
   b. Read user input (rustyline with history)
   c. If empty or "quit"/"exit", break
   d. Add user message to conversation history
   e. Call Claude with history + tools
   f. While response has tool_use:
      - Print tool name + params
      - Prompt "Allow [tool]? [y/n]: "
      - If yes: execute, add result to history
      - If no: add "Tool call denied" result
      - Call Claude again with updated history
   g. Print assistant text response
   h. Add assistant message to history
5. Cleanup: shutdown MCP servers
```

## File Structure

```
mux-rs/
├── Cargo.toml              # workspace members += ["agent-test-tui"]
├── src/                    # library
└── agent-test-tui/
    ├── Cargo.toml
    └── src/
        └── main.rs         # ~250 lines
```

## Dependencies

```toml
[dependencies]
mux = { path = ".." }
tokio = { version = "1", features = ["full"] }
rustyline = "14"
serde_json = "1"
anyhow = "1"
```

## .mcp.json Format

Standard MCP configuration (same as Claude Desktop):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxx"
      }
    }
  }
}
```

## Tool Approval Flow

When Claude returns a tool_use block:

```
Claude wants to call: read_file
Parameters: {"path": "/etc/passwd"}

Allow? [y/n]: n

[Tool denied, informing Claude...]
```

If approved, execute and show result:

```
Claude wants to call: read_file
Parameters: {"path": "/tmp/test.txt"}

Allow? [y/n]: y

[Executing read_file...]
Result: "Hello, world!"
```

## Error Handling

- Missing `.mcp.json`: Continue without MCP tools, print warning
- MCP server fails to start: Print error, continue with other servers
- API key missing: Exit with clear error message
- Tool execution fails: Return error to Claude as tool_result with is_error=true
- Network errors: Print error, let user retry

## Future Enhancements (Not in v1)

- Streaming responses (option 3 from brainstorm)
- Ratatui panels (option 2 from brainstorm)
- Built-in tools (read_file, write_file, bash)
- Policy-based approval
- Session save/restore
