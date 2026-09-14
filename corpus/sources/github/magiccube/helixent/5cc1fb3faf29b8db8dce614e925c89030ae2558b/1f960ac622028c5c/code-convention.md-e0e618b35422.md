# Code Convention

## Stack
- TS strict, ESM (`"type": "module"`), Bun runtime + test (`bun:test`)
- Zod for schemas; OpenAI SDK; Ink + React 19 for TUI; Commander for CLI; `gray-matter` + `yaml` for skills
- Path alias: `@/*` → `src/*`. Use it for cross-layer imports; relative only within the same folder.
- Gate: `tsc --noEmit && eslint . --ext .ts && bun test`

## Layers (strict dependency direction)
`foundation` → (nothing) • `agent` → `foundation` • `coding` → `foundation` • `community/*` → `foundation` (adapters) • `cli` → everything
- `agent` must stay generic (not coding-specific). Provider adapters live in `community/`, never `foundation/`.

## File & folder naming
- Folders: kebab-case. Plural for collections (`tools/`, `messages/`, `hooks/`, `components/`, `commands/`), singular for layers/concepts (`foundation`, `agent`, `coding`, `cli`, `community`).
- Files: always kebab-case (`read-file.ts`, `model-provider.ts`, `message-history.tsx`). No PascalCase files even for class/component modules.
- Tests: co-located `__tests__/<name>.test.ts` beside the source. Imports from `bun:test`.
- Every directory has an `index.ts` barrel that re-exports.
- No default exports anywhere — only named exports.

## Type system
- `interface` for object shapes; `type` for unions, aliases, and generics (`type Message = System | User | ...`, `type ToolResult<T> = ...`).
- No `I`-prefix on interfaces. No `T`-prefix on types.
- Suffix vocabulary (use these, don't invent new ones):
  - `*Params` — function/method input bag (`ModelProviderInvokeParams`)
  - `*Options` — optional config bag (`AgentOptions`)
  - `*Context` — threaded state passed through a run (`AgentContext`, `ModelContext`)
  - `*Provider` — adapter implementing a foundation interface
  - `*Middleware` — lifecycle hook object
  - `*Message` / `*Content` — discriminated-union variants
- Discriminated unions via string-literal field: `role` for messages, `type` for content segments, `ok: boolean` for results.
- JSDoc on public types/interfaces and public methods; private methods uncommented. Keep comments minimal, intent-only.

## Wire vs internal casing (load-bearing split)
- **camelCase everywhere internal** (fields, params, locals): `promptTokens`, `startLine`, `maxSteps`.
- **snake_case only on OpenAI-wire content types** inside message content: `tool_use`, `tool_result`, `tool_use_id`. Preserve these exactly — they bridge to provider wire format.
- Error codes: `SCREAMING_SNAKE` strings (`INVALID_PATH`, `FILE_NOT_FOUND`, `START_LINE_OUT_OF_RANGE`).
- Module constants: `SCREAMING_SNAKE` (`DEFAULT_MAX_CHARS`).

## Functions, classes, members
- Functions: camelCase, verb-first. Prefer `defineX` / `okX` / `errorX` factories over `createX`/`makeX`.
- Classes: constructor takes a **single options object** (destructured), never positional args.
- Public fields set at construction are `readonly`.
- **Private members use `_` prefix, not `#`**: `_context`, `_streaming`, `_abortController`, `_client`, `_baseChatCompletionParams()`. Applies to both fields and methods.
- Getters expose the underscored backing field without the prefix (`get streaming()` → `_streaming`).

## Lifecycle hook naming (pervasive pattern)
- Paired `_beforeX` / `_afterX` methods on hosts; middlewares mirror with `beforeX` / `afterX` (no underscore).
- Canonical set: `beforeAgentRun`/`afterAgentRun`, `beforeAgentStep`/`afterAgentStep`, `beforeModel`/`afterModel`, `beforeToolUse`/`afterToolUse`.
- Middleware hook contract: return `undefined` for no-op, or a partial object that is `Object.assign`-merged into the relevant context. Skip signal: return `{ __skip: true, result }` from `beforeToolUse`.

## Tool authoring (coding/tools/)
- Export shape: `export const xxxTool = defineTool({ name, description, parameters, invoke })`. Variable name = `<snake_name>Tool` in camelCase (e.g. `readFileTool`).
- `name` is `snake_case` (the wire name the model sees). File is kebab-case.
- **Zod params object — first field is always `description: z.string()`** with describe text `"Explain why you want to <action>. Always place \`description\` as the first parameter."`. This is the agent's rationale, not the tool's own description. Remaining params are camelCase.
- Path inputs: validate with `ensureAbsolutePath()` from `./tool-utils`; return `INVALID_PATH` on failure.
- Return `ToolResult<T>`:
  - success → `okToolResult(summary, data)` where `data` includes echoed inputs + outputs
  - failure → `errorToolResult(message, CODE, details)` — `code` is SCREAMING_SNAKE, `details` echoes inputs
- File I/O: use `Bun.file(path)` (not `node:fs` unless you need `mkdtemp`/`rm` in tests).
- Every tool gets a co-located `__tests__/<name>.test.ts` covering: happy path, structured error cases (by `code`), and boundary/range validation. Use `mkdtemp` + `afterEach` cleanup for filesystem tests.

## Async & streaming idioms
- Streaming = `async *stream(): AsyncGenerator<...>` yielding **cumulative snapshots** (each yield is a complete progressively-filled `AssistantMessage`; final yield equals `invoke()`'s return).
- Aborts: hold `AbortController` as an instance field (`_abortController`), thread `signal` through `ModelContext`, tool `invoke`, and fetch calls. Null it in a `finally`.
- Parallel tool dispatch uses a `Promise.race` loop over a pending set (not `Promise.all`), so each `tool_result` message emits as soon as its tool resolves. Preserve this ordering when editing `agent.ts`.
- Tool errors are caught per-tool and surfaced as `"Error: <msg>"` tool_result content — never thrown out of `_act`.

## Provider defaults
- `OpenAIModelProvider` merges `options` last, but defaults `temperature: 0, top_p: 0`. Keep these defaults; provider-specific flags pass through `options` untyped (`Record<string, unknown>`).
- Conversion helpers live in `community/openai/utils.ts` (`convertToOpenAIMessages`, `convertToOpenAITools`, `parseAssistantMessage`). Streaming uses `StreamAccumulator`.

## React / Ink (cli/tui/)
- All components: `export const X = memo(function X({ ... }: { ... }) { ... })`. Named inner function (shows in devtools), always `memo`-wrapped, props typed inline in the destructure — no separate `XProps` interface for single-use props.
- Colors come from `currentTheme.colors.*` — do not hardcode color strings.
- Hooks live in `cli/tui/hooks/use-*.ts`.
- Message rendering has two parallel renderers (ANSI in `message-text.ts`, Ink in `message-history.tsx`) — intentionally not shared. If extending, extend both; don't unify without extracting a structured-summary helper first.

## Imports (import-x enforced)
Three groups separated by a blank line, in this order:
1. `node:*`, `bun:*`, third-party (`openai`, `zod`, `ink`, `react`, `commander`)
2. `@/*` aliases
3. Relative (`./`, `../`)

Use `import type { ... }` for type-only imports. No default imports from internal modules.

## Adding things (recipes)
- **New tool**: create `src/coding/tools/<name>.ts` exporting `<name>Tool` via `defineTool`; add co-located test; export from `src/coding/tools/index.ts`; register in the lead agent's tool list.
- **New provider**: create `src/community/<vendor>/model-provider.ts` implementing `ModelProvider` (both `invoke` and `stream`); put conversion helpers in `./utils.ts`; accept `{ baseURL, apiKey }` in constructor.
- **New middleware**: object literal with any subset of `beforeX`/`afterX` hooks; pass via `Agent` constructor's `middlewares` array. Return partial context to merge, or nothing.
- **New message content variant**: add the interface in `foundation/messages/types/content.ts` with a `type` discriminator, add to the relevant `*MessageContent` union, then update `community/openai/utils.ts` converters.

## Anti-patterns (evidence-backed)
- Positional constructor args — always destructure from an options object.
- `#private` fields — use `_prefix` instead (codebase is uniform on this).
- `create*` / `make*` factory names — prefer `define*` or domain verbs.
- Default exports.
- Raw string `content` on messages — content is always a typed segment array.
- Hardcoded colors in Ink components.
- `fs.readFile` in tool impls when `Bun.file` works.
- Throwing out of tool `invoke` — return `errorToolResult` instead; the agent loop only catches as a last resort.
- Mutating `ModelContext` outside of a middleware hook's return value.
