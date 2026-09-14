# AgentNotch - Claude Code Project Memory

## Project Overview
AgentNotch is a macOS menu bar app that displays real-time AI coding assistant telemetry in the Mac's notch area. It monitors Claude Code and OpenAI Codex sessions via JSONL file parsing and displays tool usage, token counts, and session status.

## Key Directories
```
AgentNotch/
├── Core/
│   ├── ClaudeCode/
│   │   └── ClaudeCodeManager.swift    # Claude Code JSONL parsing, session watching
│   ├── Codex/
│   │   └── CodexManager.swift         # OpenAI Codex JSONL parsing, session watching
│   ├── Settings/
│   │   └── AppSettings.swift          # @AppStorage settings
│   ├── Telemetry/
│   │   ├── TelemetryCoordinator.swift # OTLP telemetry handling
│   │   └── OTLPHTTPServer.swift       # HTTP server for telemetry
│   └── Process/
│       └── MCPProcessManager.swift    # MCP process management
├── Models/
│   ├── ClaudeCodeModels.swift         # ClaudeSession, ClaudeToolExecution, etc.
│   └── CodexModels.swift              # CodexSession, CodexToolExecution, etc.
├── Views/
│   ├── Notch/
│   │   └── AgentNotchContentView.swift # Main notch UI
│   ├── ClaudeCode/
│   │   └── ClaudeToolListView.swift   # Claude tool list UI
│   ├── Codex/
│   │   └── CodexToolListView.swift    # Codex tool list UI
│   └── Settings/
│       └── AgentSettingsView.swift    # Settings UI
└── homebrew/                          # Homebrew cask distribution
    ├── agentnotch.rb                  # Cask formula
    └── AgentNotch.zip                 # Release artifact
```

## Claude Code JSONL Integration

### File Locations
- Claude directory: `~/.claude/`
- IDE sessions: `~/.claude/ide/*.lock`
- Project JSONL: `~/.claude/projects/{project-key}/{uuid}.jsonl`
- Stats cache: `~/.claude/stats-cache.json`

### Project Key Format
Path `/Users/foo/project` becomes `-Users-foo-project` (replace `/` with `-`)

### JSONL Message Types
- `tool_use` - Tool execution started (has id, name, input)
- `tool_result` - Tool completed (has tool_use_id)
- `thinking` - Model thinking block
- `text` - Text output (check for `[Request interrupted by user`)
- `toolUseResult` - Top-level field for tool results

### Key State Detection
- **Thinking**: `content[].type == "thinking"` or `role == "assistant"`
- **Tool running**: Active tools in `state.activeTools`
- **Session done**: `stop_reason == "end_turn"` or interrupted text
- **Permission needed**: Tool running > 2.5s without result
- **Idle timeout**: No new tool for 10 seconds

## OpenAI Codex JSONL Integration

### File Locations
- Codex directory: `~/.codex/`
- Sessions: `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`
- History: `~/.codex/history.jsonl`
- Config: `~/.codex/config.toml`

### JSONL Event Types
- `session_meta` - Session start (id, cwd, cli_version, model_provider, git info)
- `turn_context` - Turn metadata (model, cwd, approval_policy)
- `event_msg` with `payload.type`:
  - `token_count` - Token usage with `info.total_token_usage`
  - `agent_reasoning` - Model thinking/reasoning text
- `response_item` with `payload.type`:
  - `function_call` - Tool call started (name, arguments, call_id)
  - `function_call_output` - Tool completed (call_id, output)
  - `message` - User/assistant messages

### Token Usage Structure
```swift
struct CodexTokenUsage {
    var inputTokens: Int
    var outputTokens: Int
    var cachedInputTokens: Int        // Prompt cache hits
    var reasoningOutputTokens: Int    // o1/o3 reasoning tokens
    var totalTokens: Int
    var modelContextWindow: Int
}
```

### Key State Detection
- **Thinking**: `agent_reasoning` event or no active tools with activity
- **Tool running**: Active tools in `state.activeTools`
- **Idle timeout**: 3 seconds of no new events

## Debug Logging
All print statements wrapped in `debugLog()` - only active in DEBUG builds:
```swift
@inline(__always)
func debugLog(_ message: @autoclosure () -> String) {
    #if DEBUG
    print(message())
    #endif
}
```

## Settings (AppSettings.swift)
```swift
// Claude Code
enableClaudeCodeJSONL: Bool = true
showSessionDots: Bool = true
showPermissionIndicator: Bool = true
showTodoList: Bool = true
showThinkingState: Bool = true

// Codex
enableCodexJSONL: Bool = true

// Context & Display
contextTokenLimit: Int = 200_000  // 50k-1M range
showContextProgress: Bool = true
toolDisplayMode: String = "list"  // "list" or "singular"
```

## Token Usage Structure
```swift
struct ClaudeTokenUsage {
    var inputTokens: Int
    var outputTokens: Int
    var cacheReadInputTokens: Int      // Green in UI - savings
    var cacheCreationInputTokens: Int  // Yellow in UI - creation
}
```

## UI Components

### Notch States
- `closed` - Minimal view with wings showing tool/thinking status
- `peeking` - Dropdown notification (permission, completion)
- `open` - Full expanded view with tools list, todos, footer

### Source Colors
- **Claude Code**: Orange glow (`rgb(0.9, 0.4, 0.1)`)
- **Codex**: Blue glow (`rgb(0.1, 0.3, 0.7)`)

### Footer Display
- Session duration
- Git branch badge (purple)
- Token total (sparkles icon)
- Cache read tokens (green arrow down)
- Cache write tokens (yellow arrow up)

### Context Progress Bar
- Shows token usage vs configurable limit
- Colors: green (<50%), yellow (50-70%), orange (70-90%), red (>90%)

## Homebrew Distribution

### Tap Repository
`appgram/homebrew-tap`

### Release Process
1. Build app in Xcode (Release)
2. Copy .app to `homebrew/AgentNotch.app`
3. Create zip: `zip -r AgentNotch.zip AgentNotch.app`
4. Calculate SHA256: `shasum -a 256 AgentNotch.zip`
5. Update `agentnotch.rb` with new version and sha256
6. Create GitHub release: `gh release create vX.X.X AgentNotch.zip --repo AppGram/agentnotch`
7. Push formula to tap: copy to homebrew-tap/Casks/, commit, push

### Install Commands
```bash
brew tap appgram/homebrew-tap
brew install --cask agentnotch
brew upgrade --cask agentnotch
```

## Important Patterns

### Session Watching
- Uses `DispatchSource.makeFileSystemObjectSource` with `O_EVTONLY`
- Watches for `.write, .extend` events
- Fallback scan if direct projectKey match fails

### State Synchronization
- Per-session state in `sessionStates[sessionId]`
- Main state synced when `selectedSession?.id == sessionId`
- Always call `objectWillChange.send()` for UI updates

### Interruption Detection
Check multiple locations:
1. `toolUseResult` field containing "interrupted"
2. `text` content containing `[Request interrupted by user`
3. `tool_result` with "rejected" content

### Timers
- `idleCheckTimer` - 3s, marks thinking as false
- `toolIdleTimer` - 10s, marks session as done if no new tools
- `permissionCheckTimer` - 2.5s, marks tool as needing permission
