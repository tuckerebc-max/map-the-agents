# OpenHarness Architecture

A contributor-oriented walkthrough of how OpenHarness is built. Complements the conceptual overview in [`docs/architecture.md`](docs/architecture.md) — that doc is for users curious about the system; this one is for developers planning to change it.

> Last updated: 2026-05-02 (v2.29.0). For the latest user-facing feature list, see [README](README.md). For the engineering history of recent changes, see [CHANGELOG](CHANGELOG.md) and [`docs/superpowers/specs/`](docs/superpowers/specs/).

## At a glance

```
┌──────────────────────────────────────────────────────────────────────┐
│                              REPL (src/repl.ts)                      │
│   keyboard input → renderer state → CellGrid frame → ANSI to stdout  │
└────────┬─────────────────────────────────────────────────────────────┘
         │ user prompt
         ▼
┌──────────────────────────────────────────────────────────────────────┐
│                       Query loop (src/query/)                        │
│   message history → provider stream → tool call dispatch → repeat    │
└────┬─────────────────────────┬─────────────────────────┬─────────────┘
     │                         │                         │
     ▼                         ▼                         ▼
┌─────────┐           ┌─────────────┐           ┌─────────────┐
│Provider │           │Tools (44)   │           │Hooks (27)   │
│adapters │           │             │           │             │
│ollama   │           │Read/Write/  │           │preTool /    │
│openai   │           │Edit/Bash/   │           │postTool /   │
│anthrop. │           │Agent/MCP/   │           │subagentStart│
│openrouter│          │PowerShell/  │           │turnStart/.. │
│llama.cpp│           │ParallelAg.. │           │             │
│bedrock  │           │             │           │             │
│vertex   │           │             │           │             │
└─────────┘           └──────┬──────┘           └─────────────┘
                             │
                             ▼
                     ┌─────────────────┐
                     │   MCP servers   │
                     │  (stdio/http/   │
                     │     sse)        │
                     └─────────────────┘
```

The whole thing is one Node.js process. State lives in the renderer's `LayoutState` (in-memory) and on disk in `.oh/` (config) + `~/.oh/sessions/` (transcripts) + `.oh/checkpoints/` (file snapshots).

## Lifecycle of one user message

Tracing what happens when you type `"explain the build system"` and press Enter:

1. **Keyboard input → REPL state** (`src/repl.ts`)  
   Raw stdin bytes go through `readline` + custom keybinding dispatch. Pressing Enter assembles the buffered input into a `string`, clears the buffer, pushes a user `Message` into `state.messages`, and triggers the query loop.

2. **REPL spawns the query loop** (`src/query/index.ts:query`)  
   `query()` is an async generator. It takes the prompt + config and yields `StreamEvent`s. The REPL consumes events in a `for await` loop and dispatches each to a renderer-state mutation (text deltas → streaming buffer; tool starts → `LayoutState.toolCalls.set(callId, {...})`; etc.).

3. **Query loop calls the provider** (`src/providers/<name>.ts`)  
   The provider adapts the model's wire protocol (Anthropic Messages, OpenAI Chat Completions, Ollama's native API, etc.) to OH's internal `Message[]` shape. It returns an async generator yielding text chunks + tool call descriptors. Each provider also reports `ModelInfo` (context window, supports tools, etc.) used for compaction decisions.

4. **Model emits a tool call → query loop dispatches** (`src/query/tools.ts:executeToolCalls`)  
   Tool calls are partitioned into batches by concurrency safety. Concurrent-safe tools (Read, Glob, Grep — all read-only) run via `Promise.all`. Non-concurrent tools (Bash, Edit, Write — mutators) run sequentially. Each tool invocation is wrapped in a permission check (`src/types/permissions.ts:checkPermission`), which may consult hooks, the user (via dialog), or a managed-settings rule.

5. **Tool runs → output streams back** (`src/tools/<Name>/index.ts`)  
   Tool's `call(input, ctx)` returns `Promise<ToolResult>`. While running, it can stream chunks via `ctx.onOutputChunk(chunkText)` (which appears under the tool's row in the REPL) or — for sub-agent tools — forward inner events via `ctx.emitChildEvent({...})` for nested tool-call rendering.

6. **Tool result feeds back into query loop**  
   `executeToolCalls` collects all results, pushes them as tool-result messages into the message history, then yields `tool_call_end` events. Hooks fire (`postToolUse`, `postToolBatch`). Loop repeats from step 3 with the augmented history. Loop exits when the model responds with text only (no tool calls) or when `maxTurns` is hit.

7. **REPL renders each event into LayoutState**  
   Event handlers in `src/repl.ts` mutate `LayoutState` immutably-ish (Map updates, string concatenation for streaming text). After every batch of mutations, the renderer recomputes a `CellGrid` from the state.

8. **Renderer rasterizes LayoutState → CellGrid → ANSI** (`src/renderer/`)  
   The renderer is sequential, not React/Ink: it computes the full grid every frame and diffs against the prior grid to emit minimal ANSI. Frame rate is gated by terminal capability (~60fps target on modern terminals; falls back to lower rates on laggy ones). Completed messages flush into native scrollback; the live area (streaming text + spinner + input) rewrites in-place via relative cursor movement.

## Key abstractions

### `Tool` (`src/Tool.ts`)

Every built-in capability — Read, Write, Bash, Agent, MCP-bridge, etc. — is a `Tool<Input>`:

```ts
type Tool<Input> = {
  name: string;
  description: string;
  inputSchema: z.ZodType<Input>;        // runtime validation + JSON schema export
  riskLevel: "low" | "medium" | "high"; // affects permission prompt
  isReadOnly(input): boolean;           // hint for parallel batching
  isConcurrencySafe(input): boolean;    // strict gate for parallel batching
  call(input, context): Promise<ToolResult>;
  prompt(): string;                     // LLM-visible description
};
```

`ToolContext` carries the cwd, abort signal, callId, the current `provider` (for sub-agent tools), `tools` list, hooks, and optional callbacks (`onOutputChunk` for live streaming, `emitChildEvent` for nested-tool-call event forwarding).

### `Provider` (`src/providers/base.ts`)

Adapts an LLM API to OH's internal `Message[]` shape:

```ts
interface Provider {
  name: string;
  stream(messages, system, tools?, model?): AsyncIterator<StreamEvent>;
  complete(messages, system, tools?, model?): Promise<Message>;
  listModels(): ModelInfo[];
  healthCheck(): Promise<boolean>;
}
```

Each provider lives in `src/providers/<name>.ts`. To add one: implement the interface, register in `src/providers/index.ts`'s `createProviderInstance()` switch, mirror an existing provider as a template (Ollama is the simplest reference).

### `StreamEvent` (`src/types/events.ts`)

The event protocol that flows from `query()` through to the REPL:

```ts
type StreamEvent =
  | TextDelta                  // streaming text
  | ThinkingDelta              // streaming "thinking" content (for reasoning models)
  | ToolCallStart              // a tool is about to execute
  | ToolCallComplete           // tool call args fully assembled
  | ToolCallEnd                // tool execution finished (success or error)
  | ToolOutputDelta            // streaming chunk from a tool's stdout
  | PermissionRequest          // model wants to run a tool that needs approval
  | AskUserRequest             // tool asked user a question
  | CostUpdate                 // cumulative tokens + USD
  | TurnComplete               // loop iteration done
  | ErrorEvent                 // unrecoverable error
  | RateLimited;               // provider rate-limited; retry pending
```

`ToolCall*` events optionally carry `parentCallId` for nested-tool-call rendering (added in v2.27.0). `ToolCallEnd` optionally carries `outputType` (`"json"` / `"markdown"` / `"image"` / `"plain"`) for typed-dispatch rendering (added in v2.26.0). Both fields are optional everywhere — non-breaking.

### `LayoutState` (`src/renderer/layout.ts`)

The single source of truth for what the renderer draws each frame:

```ts
type LayoutState = {
  messages: Message[];              // completed conversation
  streamingText: string;            // in-flight assistant text
  thinkingText: string;             // in-flight thinking (collapsed by default)
  toolCalls: Map<string, ToolCallInfo>;  // running + completed tool calls
  inputText: string;                // user's current input
  inputCursor: number;
  permissionBox: PermissionBox | null;
  questionPrompt: AskUserState | null;
  // ...spinner state, theme, scrolling, autocomplete, etc.
};
```

Anything visible on screen is derivable from `LayoutState`. The renderer is purely functional in the state → grid transformation; mutations happen only via REPL event handlers.

### Hook (`src/harness/hooks.ts`)

Pluggable extension points fired at lifecycle moments. 27 events as of v2.27.0 (matches CC stable):

- **Tool lifecycle**: `preToolUse`, `postToolUse`, `preToolBatch`, `postToolBatch`
- **Sub-agent lifecycle**: `subagentStart`, `subagentStop`
- **Turn lifecycle**: `turnStart`, `turnComplete`
- **Session lifecycle**: `sessionStart`, `sessionEnd`
- **Message events**: `userPromptSubmit`, `assistantMessage`
- ...and more

Hooks are configured via `.oh/config.yaml`'s `hooks:` block. Each hook can be a shell command (synchronous gate) or a script that returns a `HookDecision` (continue / block / replace input). See [`docs/hooks.md`](docs/hooks.md).

### MCP integration (`src/mcp/`)

Model Context Protocol servers expose tools to OH the same way built-in tools do. Three transports:

- **stdio** (default) — server runs as subprocess; OH speaks JSON-RPC over its stdio
- **http** — Streamable HTTP for remote MCP servers
- **sse** — legacy Server-Sent Events

Configured via `.oh/config.yaml`'s `mcpServers:` block. See [`examples/mcp-config-sample.yaml`](examples/mcp-config-sample.yaml) for an annotated config.

## Major design decisions

### Sequential renderer instead of Ink/React

Most CLI agents (CC, aider, Codex CLI) use Ink (React-for-CLI). OH uses a sequential renderer in `src/renderer/` built on a `CellGrid` primitive (a 2D array of styled cells with diff-and-emit-ANSI semantics).

**Why:** Ink rebuilds the entire UI tree on every render; for our use case (high-frequency token streaming + 44 mutating tools) that produces unacceptable flicker on slower terminals. The CellGrid model lets us compute the full frame, diff against the prior frame, and emit only the cells that changed — typically <100 ANSI sequences per frame even during heavy streaming.

**Tradeoff:** more code (we maintain a renderer instead of leaning on React). The renderer is currently ~3000 LOC across `src/renderer/`. CC's renderer is comparable.

### `parentCallId` for nested tool-call rendering (v2.27.0)

When `Agent` or `ParallelAgents` spawns inner tool calls, those children render indented under their spawning parent. Implemented via an optional `parentCallId?: string` field on the four tool-call events + a `ToolContext.emitChildEvent` callback that forwards inner events to the outer stream stamped with the parent's callId.

**Why this shape:** symmetric with existing `tool_output_delta` plumbing, avoids new event types, optional everywhere = non-breaking. Aligns with `traces.ts`'s OTel-style `parentSpanId` (durable observability layer); StreamEvent's `parentCallId` is the live UI feed equivalent.

**Alternative considered:** synthetic `agent_summary` event emitted at the end of a sub-agent's run. Rejected because it loses live streaming visibility — children only appear after the parent's `tool_call_end`, making the Agent row look frozen until completion.

### Typed tool-output dispatch (v2.26.0)

Tools optionally stamp `outputType?: "json" | "markdown" | "image" | "plain"` on their `ToolResult`. The renderer dispatches via this hint — `"json"` → JSON tree renderer, `"markdown"` → markdown renderer, `"image"` → inline image protocol (Kitty/iTerm2), `"plain"` → flat lines. Tools that don't stamp fall through a heuristic (parse-as-JSON, structural-markdown markers, plain).

**Why:** Modern tool-call protocols (MCP, Anthropic Messages API, OpenAI tool-use schema) all type their content. Typed dispatch is the modern standard. Heuristic-only would have worked but fights the ecosystem.

### Per-task synthetic parents under `ParallelAgents` (v2.28.0)

When `ParallelAgents` runs multiple tasks, the `AgentDispatcher` synthesizes a per-task wrapper event (`toolName: "Task"`) so children of each task render under their own `Task` row, not flat under the bundled `ParallelAgents` parent.

**Why:** flat children render makes it impossible to tell which task spawned which tool. Synthesizing wrappers gives 3-level structure (`ParallelAgents → Task → child tool`) without needing new event types — reuses the v2.27.0 `parentCallId` plumbing.

### Progressive tool loading

44 tools is a lot of system-prompt overhead. OH loads ~17 core tools with full schemas on session start; the remaining ~27 deferred tools show a one-line description in the system prompt and resolve full schema on first use via the `ToolSearch` tool. Saves ~46% of tool-prompt tokens.

**Tradeoff:** slight latency on first deferred-tool use (typically <100ms — the schema is already in memory, just not in the system prompt). Net win on context budget.

### Worktree isolation for sub-agents

By default, when `Agent` or `ParallelAgents` spawns a sub-agent, the sub-agent runs in an isolated git worktree (`src/git/`). Changes in the worktree merge back to the main checkout via a follow-up commit, or stay in the worktree if the user wants to review.

**Why:** parallel sub-agents editing the same files in the same checkout race each other and clobber changes. Worktrees give each sub-agent its own filesystem scratchpad without cloning or copying.

**Tradeoff:** adds disk I/O at sub-agent spawn time (~50-200ms per worktree create). Skipped automatically when not in a git repo.

## Engineering practice

### Spec → plan → execute workflow

Non-trivial features go through `docs/superpowers/specs/<date>-<topic>-design.md` (design doc) and `docs/superpowers/plans/<date>-<topic>-plan.md` (TDD task breakdown) before any code. Recent examples: PRs #93, #94, #95, #96. Spec/plan PRs land first; implementation lands as a follow-up PR. See [CONTRIBUTING.md](CONTRIBUTING.md#spec--plan-workflow).

### Tests

1502 tests as of v2.29.0. Live next to the code (`src/foo.ts` → `src/foo.test.ts`). Use `node:test` + `node:assert/strict`. Integration / e2e tests live in `src/renderer/e2e.test.ts`, `src/query.test.ts`. Run via `npm run test:cli` (~60s on a modern machine).

### CI

GitHub Actions runs `typecheck`, `lint`, `test:cli`, and `test:sdk` on Ubuntu and Windows for every PR. Publish workflow (`.github/workflows/publish.yml`) builds and publishes to npm on tag push (`v*`).

### Memory / observability

Engineering memory lives in `.claude/projects/<project>/memory/` (per-developer). Agent telemetry routes through `src/harness/traces.ts` with OpenTelemetry-style spans (`spanId` / `parentSpanId`).

## Where to start reading

If you want to understand the system in depth, read in this order:

1. `src/main.tsx` — entry point and bootstrap (~200 lines)
2. `src/repl.ts` — the REPL loop and event handlers (~1200 lines, but skim — most of it is per-event handlers)
3. `src/query/index.ts` — the agent loop (~390 lines)
4. `src/query/tools.ts` — tool dispatch + permission gating (~430 lines)
5. `src/Tool.ts` — the Tool interface (~125 lines)
6. `src/types/events.ts` — the event protocol (~95 lines)
7. `src/renderer/layout.ts` — LayoutState and the rasterize entry point (~440 lines)
8. `src/renderer/layout-sections.ts` — per-section renderers (this is where the visible UI lives)
9. One representative tool: `src/tools/AgentTool/index.ts` (the Agent tool) or `src/tools/FileEditTool/index.ts` (a file mutator)

After that, browse `docs/superpowers/specs/` for the engineering history of recent decisions.
