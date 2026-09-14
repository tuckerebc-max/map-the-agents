# Hex Architecture Documentation

Technical overview of Hex's design, architecture, and implementation.

## Table of Contents

- [System Overview](#system-overview)
- [Project Structure](#project-structure)
- [Core Components](#core-components)
- [Data Flow](#data-flow)
- [Storage Architecture](#storage-architecture)
- [Tool System](#tool-system)
- [UI Architecture](#ui-architecture)
- [API Client](#api-client)
- [Design Decisions](#design-decisions)

## System Overview

Hex is a Go-based CLI for Claude with three main operational modes:

1. **Print Mode**: Single request-response (non-interactive)
2. **Interactive Mode**: Full TUI with streaming and tools
3. **Resume Mode**: Continue previous conversations

### High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│                     CLI Layer                        │
│                   (cmd/hex)                         │
│                                                      │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐   │
│  │   Print    │  │ Interactive│  │   Resume   │   │
│  │    Mode    │  │    Mode    │  │    Mode    │   │
│  └─────┬──────┘  └──────┬─────┘  └──────┬─────┘   │
└────────┼─────────────────┼────────────────┼─────────┘
         │                 │                │
         ▼                 ▼                ▼
┌─────────────────────────────────────────────────────┐
│                 Internal Components                  │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │   Core   │  │    UI    │  │ Storage  │         │
│  │ (client, │  │(Bubbletea│  │ (SQLite) │         │
│  │  types)  │  │   TUI)   │  │          │         │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘         │
│       │             │              │                │
│  ┌────┴─────────────┴──────────────┴─────┐         │
│  │          Tool System                   │         │
│  │  (Registry, Executor, Tools)           │         │
│  └────┬─────────┬──────────┬──────────────┘         │
│       │         │          │                         │
│  ┌────▼────┐ ┌─▼──────┐ ┌─▼──────┐ ┌──────────┐  │
│  │  Read   │ │ Write  │ │  Bash  │ │ Edit,    │  │
│  │  Tool   │ │  Tool  │ │  Tool  │ │ Grep ... │  │
│  └─────────┘ └────────┘ └────────┘ └──────────┘  │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
         ┌─────────────────────┐
         │  Anthropic API      │
         │  (Messages API)     │
         │  - Streaming        │
         │  - Tool Use         │
         └─────────────────────┘
```

## Project Structure

```
hex/
├── cmd/hex/              # CLI entry point and commands
│   ├── main.go           # Application entry
│   ├── root.go           # Root command + interactive mode
│   ├── print.go          # Print mode implementation
│   ├── setup.go          # Configuration setup
│   ├── doctor.go         # Health check command
│   └── storage.go        # Database helpers
│
├── internal/             # Private implementation
│   ├── core/            # Core types and API client
│   │   ├── client.go    # HTTP client for Anthropic API
│   │   ├── stream.go    # SSE streaming support
│   │   ├── types.go     # API request/response types
│   │   └── config.go    # Configuration management
│   │
│   ├── ui/              # Terminal UI (Bubbletea)
│   │   ├── model.go     # UI state and data
│   │   ├── update.go    # Event handling logic
│   │   ├── view.go      # Rendering logic
│   │   └── (styling distributed across component files)
│   │
│   ├── storage/         # SQLite persistence
│   │   ├── schema.go    # Database initialization
│   │   ├── conversations.go  # Conversation CRUD
│   │   ├── messages.go       # Message CRUD
│   │   └── migrations/       # Embedded SQL migrations
│   │       └── 001_initial.sql
│   │
│   └── tools/           # Tool execution system
│       ├── tool.go      # Tool interface
│       ├── registry.go  # Tool registry
│       ├── executor.go  # Execution + approval
│       ├── types.go     # Common types
│       ├── result.go    # Result types
│       ├── read_tool.go # Read file tool
│       ├── write_tool.go # Write file tool
│       └── bash_tool.go  # Bash command tool
│
│
├── test/integration/    # Integration test suites
│   ├── api_test.go
│   ├── storage_test.go
│   ├── tools_test.go
│   └── ui_test.go
│
├── docs/                # Documentation
│   ├── USER_GUIDE.md
│   ├── ARCHITECTURE.md (this file)
│   ├── TOOLS.md
│   └── plans/
│
├── go.mod               # Go module definition
├── Makefile             # Build automation
├── README.md            # Project overview
└── CHANGELOG.md         # Version history
```

## Core Components

### 1. CLI Layer (cmd/hex)

**Purpose**: Command-line interface and mode orchestration

**Components**:
- `main.go`: Entry point, Cobra setup
- `root.go`: Root command, interactive mode launcher
- `print.go`: Non-interactive print mode
- `setup.go`: API key configuration
- `doctor.go`: Health checks

**Responsibilities**:
- Parse command-line flags
- Load configuration
- Route to appropriate mode (print/interactive/resume)
- Initialize subsystems (DB, API client, UI)

### 2. Core Package (internal/core)

**Purpose**: API client, types, and configuration

**Components**:

**client.go** - Anthropic API HTTP client
- Request/response handling
- Authentication headers
- Error handling
- Both streaming and non-streaming modes

**stream.go** - SSE streaming support
- Parse Server-Sent Events (SSE)
- Delta accumulation
- Channel-based streaming
- Context cancellation

**types.go** - API data structures
- MessageRequest/Response
- ContentBlock types
- ToolUse/ToolResult
- Usage tracking

**config.go** - Configuration management
- Multi-source loading (file, env, flags)
- Viper integration
- Default values
- Validation

### 3. Storage Package (internal/storage)

**Purpose**: SQLite persistence layer

**Design**: Hybrid schema (normalized tables + JSON)

**Components**:

**schema.go** - Database initialization
- Embedded migrations
- Schema versioning
- Pragma configuration (foreign keys, WAL mode)

**conversations.go** - Conversation operations
- Create, Get, List
- Timestamp updates
- Title management

**messages.go** - Message operations
- Create, Get, List by conversation
- JSON serialization for tool_calls
- Foreign key relationships

### 4. Tools Package (internal/tools)

**Purpose**: Tool execution framework

**Architecture**: Registry + Executor pattern

**Components**:

**Tool Interface**:
```go
type Tool interface {
    Name() string
    Description() string
    Execute(ctx context.Context, params map[string]interface{}) (*Result, error)
    RequiresApproval(params map[string]interface{}) bool
}
```

**Registry**: Tool discovery and management
- Register tools by name
- List available tools
- Get tool by name

**Executor**: Permission-based execution
- Approval callback system
- Parameter validation
- Execution lifecycle
- Error handling

**Tools** (14+ implementations):
- Core: ReadTool, WriteTool, BashTool, EditTool, GrepTool, GlobTool
- Advanced: AskUserQuestion, TodoWrite, WebFetch, WebSearch, Task
- Process Management: BashOutput, KillShell

### 5. UI Package (internal/ui)

**Purpose**: Interactive terminal interface

**Framework**: Bubbletea (Elm Architecture)

**Components**:

**Model** - UI state
- Conversation data
- Input textarea
- Viewport for messages
- Status (idle/streaming/error)
- Token counters

**Update** - Event handling
- Keyboard input
- Window resize
- Streaming chunks
- Tool execution events

**View** - Rendering
- Markdown formatting (Glamour)
- Syntax highlighting
- Status bar
- Input area
- Help text

**Styles** - Lipgloss styling
- Color schemes
- Borders and padding
- Responsive layouts

## Data Flow

### Print Mode Flow

```
User Input
    │
    ▼
CLI Parser
    │
    ▼
Config Loader ──> API Client ──> Anthropic API
                       │              │
                       ▼              │
                  [Wait for          │
                   response]         │
                       │              │
                       ◀──────────────┘
                       │
                       ▼
                  Format & Print
                       │
                       ▼
                     Exit
```

### Interactive Mode Flow

```
User starts Hex
    │
    ▼
Initialize DB ──> Load last conversation (if --continue)
    │                      │
    ▼                      │
Launch UI ◀───────────────┘
    │
    │  ┌─────────────────────────────────┐
    │  │   Event Loop (Bubbletea)        │
    │  │                                  │
    ▼  ▼                                  │
User types message                        │
    │                                     │
    ▼                                     │
Add to messages array                    │
    │                                     │
    ▼                                     │
Save to DB ──> Send to API (streaming)  │
    │                 │                   │
    │                 ▼                   │
    │          Parse SSE chunks          │
    │                 │                   │
    │                 ▼                   │
    │          Update UI (delta)         │
    │                 │                   │
    │                 ▼                   │
    │          Tool use detected?        │
    │            ┌────┴────┐              │
    │           No        Yes             │
    │            │          │              │
    │            │          ▼              │
    │            │    Show approval       │
    │            │    prompt              │
    │            │          │              │
    │            │      ┌───┴───┐          │
    │            │    Deny    Approve     │
    │            │      │       │          │
    │            │      │       ▼          │
    │            │      │  Execute tool   │
    │            │      │       │          │
    │            │      │       ▼          │
    │            │      │  Return result  │
    │            │      │       │          │
    │            ◀──────┴───────┘          │
    │                 │                   │
    ▼                 ▼                   │
Complete ──> Display in UI ─────────────┘
    │
    ▼
Save to DB
```

### Streaming Flow Detail

```
API Client                   UI Model
    │                           │
    │ CreateMessageStream()     │
    │───────────────────────────>│
    │                           │
    │ <-chan *StreamChunk       │
    │<──────────────────────────│
    │                           │
┌───┴────────────────┐          │
│ SSE Parser         │          │
│ (goroutine)        │          │
│                    │          │
│ Read SSE line ────>│ chunk 1  │
│                    │────────────────────>│
│                    │          │ Update() │
│ Read SSE line ────>│ chunk 2  │          │
│                    │────────────────────>│
│                    │          │ View()   │
│ Read SSE line ────>│ chunk 3  │          │
│                    │────────────────────>│
│                    │          │          │
│ [DONE] ───────────>│ stop     │          │
│                    │────────────────────>│
└────────────────────┘          │          │
                               │          │
                          Close chan    Complete
```

## Storage Architecture

### Database Schema

**Hybrid Design**: Normalized core + JSON for flexibility

```sql
-- Conversations table (normalized)
CREATE TABLE conversations (
    id TEXT PRIMARY KEY,              -- conv-{timestamp}
    title TEXT NOT NULL,              -- Auto-generated from first message
    model TEXT NOT NULL,              -- claude-sonnet-4-5-20250929
    system_prompt TEXT,               -- Optional system prompt
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- Messages table (hybrid: normalized + JSON)
CREATE TABLE messages (
    id TEXT PRIMARY KEY,              -- msg-{uuid}
    conversation_id TEXT NOT NULL,    -- Foreign key
    role TEXT NOT NULL,               -- user|assistant|system
    content TEXT NOT NULL,            -- Text content
    tool_calls JSON,                  -- Array of ToolUse (flexible)
    metadata JSON,                    -- Extension point
    created_at TIMESTAMP NOT NULL,

    FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
);

-- Indexes for performance
CREATE INDEX idx_messages_conversation ON messages(conversation_id);
CREATE INDEX idx_conversations_updated ON conversations(updated_at DESC);
```

### Design Rationale

**Why hybrid schema?**

1. **Normalized tables**: Fast queries, referential integrity
2. **JSON columns**: Flexibility for complex/evolving data
3. **Tool calls as JSON**: Structure varies by tool type
4. **Metadata as JSON**: Extension point for future features

**Why SQLite?**

1. **Zero configuration**: Single file database
2. **Embedded**: No separate process
3. **ACID transactions**: Data safety
4. **WAL mode**: Better concurrency
5. **Cross-platform**: Pure Go driver (modernc.org/sqlite)

**Trade-offs**:
- JSON columns: Less queryable (but rarely needed)
- Single file: Not suitable for multi-user (but that's ok for CLI)
- Pure Go driver: Slower than cgo (but good enough)

### Migration Strategy

**Current**: Embedded SQL files with version tracking

```go
//go:embed migrations/*.sql
var migrations embed.FS

func InitializeSchema(db *sql.DB) error {
    // Read and execute migrations
    // Future: version tracking table
}
```

**Future** (v0.3.0+):
- Migration version table
- Up/down migrations
- Rollback support

## Tool System

### Architecture

**Pattern**: Registry + Executor with approval callbacks

```
┌─────────────────────────────────────────┐
│           Tool Registry                  │
│  map[string]Tool                         │
│  - "read_file" -> ReadTool              │
│  - "write_file" -> WriteTool            │
│  - "bash" -> BashTool                   │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│         Tool Executor                    │
│  - Approval callback                     │
│  - Parameter validation                  │
│  - Execution lifecycle                   │
└────────────┬────────────────────────────┘
             │
             ▼
        Execute Tool
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
ReadTool WriteTool BashTool
```

### Tool Interface

```go
type Tool interface {
    // Metadata
    Name() string
    Description() string

    // Execution
    Execute(ctx context.Context, params map[string]interface{}) (*Result, error)

    // Permission
    RequiresApproval(params map[string]interface{}) bool
}
```

### Approval Flow

```
Claude requests tool
    │
    ▼
Executor.Execute(toolName, params)
    │
    ▼
Get tool from registry
    │
    ▼
RequiresApproval(params)?
    ├─ No ──> Execute directly
    │
    └─ Yes ──> Call approvalFunc(toolName, params)
               │
               ├─ Denied ──> Return error result
               │
               └─ Approved ──> Execute tool
                               │
                               ▼
                         Return result
```

### Tool Result Format

```go
type Result struct {
    ToolName   string                 // Which tool
    Success    bool                   // Did it work?
    Output     string                 // Main output
    Error      string                 // Error message (if failed)
    Metadata   map[string]interface{} // Extra data
}
```

## UI Architecture

### Bubbletea Pattern (Elm Architecture)

```
┌──────────────────────────────────────────┐
│              Model                        │
│  - State (messages, input, status)       │
│  - Components (textarea, viewport)       │
│  - Data (conversation ID, tokens)        │
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│             Update                        │
│  - Handle events (keyboard, resize)      │
│  - Update state                           │
│  - Return new model + commands           │
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│              View                         │
│  - Render model to string                │
│  - Apply styles (Lipgloss)               │
│  - Format markdown (Glamour)             │
└──────────────────────────────────────────┘
```

### Event Flow

```
User input (keyboard)
    │
    ▼
tea.KeyMsg ───> Update()
                  │
                  ├─ Enter key?
                  │   └─> Send message
                  │       └─> Return tea.Cmd (async API call)
                  │
                  ├─ Resize?
                  │   └─> Update dimensions
                  │
                  └─> Update input component
                      │
                      ▼
                Return (new model, cmds)
                      │
                      ▼
                View() renders new state
```

### Component Hierarchy

```
Model
  ├─ Input (bubbles/textarea)
  │    ├─ Cursor
  │    ├─ Line wrapping
  │    └─ Character limit
  │
  ├─ Viewport (bubbles/viewport)
  │    ├─ Scrollable content
  │    ├─ Vi-style navigation
  │    └─ Content buffer
  │
  └─ Messages []Message
       ├─ Role (user/assistant)
       ├─ Content (markdown)
       └─ Timestamp
```

## API Client

### Architecture

```
Client
  ├─ HTTP Client (net/http)
  ├─ Base URL (api.anthropic.com)
  ├─ API Key (from config)
  └─ Methods
       ├─ CreateMessage() - Non-streaming
       └─ CreateMessageStream() - SSE streaming
```

### Streaming Implementation

**SSE Format**:
```
data: {"type":"message_start",...}

data: {"type":"content_block_delta","delta":{"type":"text_delta","text":"Hello"}}

data: {"type":"content_block_delta","delta":{"type":"text_delta","text":" world"}}

data: [DONE]
```

**Parser**:
```go
func ParseSSEChunk(line string) (*StreamChunk, error) {
    // Strip "data: " prefix
    // Parse JSON
    // Return chunk
}
```

**Accumulator**:
```go
type StreamAccumulator struct {
    text string
}

func (a *StreamAccumulator) Add(chunk *StreamChunk) {
    if chunk.Delta != nil {
        a.text += chunk.Delta.Text
    }
}
```

## Design Decisions

### 1. Why Go?

**Pros**:
- Single binary distribution (no runtime)
- Fast compilation and execution
- Excellent concurrency (goroutines for streaming)
- Strong standard library (net/http, database/sql)
- Cross-platform (macOS, Linux, Windows)

**Cons**:
- More verbose than Python/JS
- Smaller ecosystem for AI tools

**Decision**: Go's deployment simplicity and performance outweigh verbosity.

### 2. Why Bubbletea for UI?

**Alternatives considered**:
- tcell: Too low-level
- tview: Less idiomatic, heavier
- Raw terminal control: Too much work

**Choice**: Bubbletea
- Elm Architecture (testable, predictable)
- Charm ecosystem (Lipgloss, Glamour, Bubbles)
- Active development
- Great documentation

### 3. Why SQLite?

**Alternatives considered**:
- JSON files: No querying, race conditions
- Bolt/BadgerDB: Overkill for this use case
- Postgres: Requires server process

**Choice**: SQLite
- Self-contained
- ACID transactions
- SQL querying
- WAL mode for concurrency
- Pure Go driver available

### 4. Why Hybrid Schema?

**Alternatives**:
- Fully normalized: Rigid, requires migrations for schema changes
- Fully JSON: Poor performance, no referential integrity

**Choice**: Hybrid
- Normalized core: conversations, messages (rigid structure)
- JSON columns: tool_calls, metadata (flexible structure)
- Best of both worlds

### 5. Why Registry Pattern for Tools?

**Alternatives**:
- Hard-coded if/else: Not extensible
- Plugin system: Too complex for v0.2.0

**Choice**: Registry + Interface
- Extensible (add tools easily)
- Testable (mock tools)
- Type-safe (interface contract)
- Future: plugins can register tools

### 6. Streaming vs Polling

**Decision**: Streaming (SSE)

**Rationale**:
- Real-time feedback (better UX)
- Lower latency (no polling delay)
- Efficient (server pushes, no repeated requests)
- Standard (SSE is well-supported)

**Trade-off**: More complex client implementation (goroutines, channels)

### 7. Approval Callback Pattern

**Decision**: Callback function for tool approval

**Rationale**:
- Decouples tools from UI
- Testable (inject mock approval)
- Flexible (different approval logic per mode)

**Alternative**: Could use channels, but callbacks are simpler.

---

## Completed Phases

### Phase 3: Extended Tools (Complete)

- Edit tool (exact string replacement)
- Grep tool (ripgrep-based code search)
- Glob tool (file pattern matching)

### Phase 4: MCP Integration (Complete)

- MCP server support via mux library
- External tool discovery and registration
- Sub-agent system via Task tool

### Future

- Plugin system (public plugin API)
- HTTP/SSE MCP transport
- Advanced resource and prompt support

---

**Next Reading**:
- [TOOLS.md](TOOLS.md) - Tool system details
- [USER_GUIDE.md](USER_GUIDE.md) - Usage examples
- [CHANGELOG.md](../CHANGELOG.md) - Version history
