# Formax CODEMAP

This file is a “where to change what” index for quickly navigating the codebase.

## Entry Points
- CLI entrypoint (main): `packages/core/src/entrypoints/cli.tsx`
- CLI arg parsing + dispatch: `packages/core/src/runtime/cli/args.ts`, `packages/core/src/runtime/cli/main.ts`
- Legacy REPL bootstrap orchestration: `packages/core/src/runtime/bootstrap/runLegacyCli.tsx`
  - Runtime assembly slices: `packages/core/src/runtime/bootstrap/*`
- App-server entrypoint (JSON-RPC over stdio): `packages/core/src/app-server/index.ts`
- In-process SDK unified API entry (`query()` + `unstable_v2_*`): `packages/core/src/sdk/api.ts` (public re-export: `packages/core/src/sdk/index.ts`)
- SDK query facade (`query()`): `packages/core/src/sdk/query.ts` (runtime implementation: `packages/core/src/sdk/query/runner.ts`)
- SDK session-query facade (`listSessions()` + `getSessionMessages()`): `packages/core/src/sdk/sessions.ts` (backed by `packages/core/src/features/repl/sessionSave/reader.ts`)
- SDK v2 session facade (`unstable_v2_*`): `packages/core/src/sdk/v2.ts` (runtime implementation: `packages/core/src/sdk/session/core.ts`)
- SDK local usage guide: `packages/core/src/sdk/README.md`
- Serve runtime launcher (`formax serve`, WebSocket bridge): `packages/core/src/runtime/serve/localServer.ts`
- Web UI runtime launcher (`formax web`, bridge + static host): `packages/core/src/runtime/web/localUi.ts`
- App-server dev bridge entrypoint (WebSocket -> stdio loop): `packages/core/src/entrypoints/app-server-bridge.ts`
- Git-backed Review source command planning (unstaged/staged/commit source keys and git diff args): `packages/core/src/app-server/gitReviewOperations.ts`
- App-server web reference entrypoint (bridge + React UI dev server): `packages/core/src/entrypoints/app-server-web-reference.ts`
- Desktop Electron shell (orchestrator + main/preload): `packages/desktop-electron/scripts/run.mjs`, `packages/desktop-electron/src/main.ts`, `packages/desktop-electron/src/preload.ts`
- Transcript perf playground: `packages/core/src/entrypoints/perf-transcript.tsx`

## App Server (GUI Bridge)
- JSON-RPC server/router: `packages/core/src/app-server/server.ts`
- Protocol parsing + param validation: `packages/core/src/app-server/protocol.ts`, `packages/core/src/app-server/protocol/input.ts`
- JSON-RPC message classification/encoding: `packages/core/src/app-server/jsonrpc.ts`
- Thread/session mapping (sessionSave-backed): `packages/core/src/app-server/threadStore.ts`
- Turn execution + streaming forwarding: `packages/core/src/app-server/turnRunner.ts`
- Input lifecycle helpers: `packages/core/src/app-server/turn/inputId.ts`, `packages/core/src/app-server/turn/inputStore.ts`
- Stdio JSONL transport: `packages/core/src/app-server/transport/stdio.ts`
- Dev bridge (WebSocket fan-in/fan-out to app-server loop): `packages/core/src/app-server/devBridge.ts`
- Dev bridge Git Review operations (source-aware diff summary/file patch/image preview/full-file content planning): `packages/core/src/app-server/gitReviewOperations.ts`, `packages/core/src/app-server/devBridge.ts`
- Serve command parsing/help text: `packages/core/src/runtime/cli/serveCommand.ts`
- Web command parsing/help text: `packages/core/src/runtime/cli/webCommand.ts`
- Shared web/bridge network + security helpers (host/port/url/origin/token): `packages/core/src/runtime/network/runtime.ts`
- Web reference React client (isolated app): `packages/web-reference-react/*` (see "Web Reference React Client")
- Session event recovery for stale inputs: `packages/core/src/app-server/store/sessionEventReader.ts`
- Shared persisted tool-event reconstruction (used by app-server + REPL resume): `packages/core/src/features/repl/sessionSave/persistedToolEvents.ts`
- Session persistence DTO/event readers (Repo-owned): `packages/core/src/features/repl/sessionSave/{contextCollapseStoreEvents,durableSnipStoreEvents,durableToolResultContentReplacementEvents,reactiveCompactEvents,sessionMemorySidecar}.ts`
- Session restore semantic rebuilders (Service-owned): `packages/core/src/features/repl/sessionRestore/{contextCollapseStore,durableSnipStore,durableToolResultContentReplacement,sessionMemory}.ts`
- Durable compression success-boundary writers:
  - REPL: `packages/core/src/features/repl/controller/session/sessionEvents.ts`, `packages/core/src/features/repl/controller/send/sendMainTurn.ts`
  - App-server: `packages/core/src/app-server/turnRunner.ts`
  - SDK: `packages/core/src/sdk/query/runner.ts`
- Primary tests: `packages/core/src/app-server/*.test.ts`, `packages/core/src/app-server/store/*.test.ts`, `packages/core/src/app-server/turn/*.test.ts`

## REPL UI (Ink)
- Main screen: `packages/core/src/screens/REPL.tsx`
- Controller/state (send/streaming/overlays): `packages/core/src/features/repl/useReplController.ts`, `packages/core/src/features/repl/controller/{send,streaming,canonical,session,ui,shared}/*`
- Canonical event projection helper (hook-level orchestration): `packages/core/src/features/repl/controller/canonical/canonicalEventOrchestration.ts`
- Session transition helpers (abort/new session): `packages/core/src/features/repl/controller/session/sessionTransitions.ts`
- Session save/replay core (writer/reader + app tool-event payload mapping + durable transcript turn snapshots): `packages/core/src/features/repl/sessionSave/{writer,reader,appToolEventPayload,transcriptTurnSnapshots}.ts`
- REPL hotkeys / input routing (Ctrl+O Expanded Transcript, Ctrl+E fold history, etc.): `packages/core/src/screens/repl/hotkeys.ts`
- Prompt mode gating (overlays/prompt blocks disable hotkeys): `packages/core/src/screens/repl/promptMode.ts`
- Transcript renderers (Primary vs Expanded): `packages/core/src/screens/repl/transcript.tsx`
- Active interactive bottom prompt slot (approval / ask-user controls after transcript): `packages/core/src/screens/repl/ActivePromptSlot.tsx`
- Expanded Transcript tests: `packages/core/src/screens/repl/expandedTranscript.test.tsx`
- Input UI: `packages/core/src/components/chat/InputBar.tsx`
- Header: `packages/core/src/components/chat/HeaderBanner.tsx`
- Mode indicator: `packages/core/src/components/chat/ModeIndicator.tsx`
- Pulsing dot: `packages/core/src/components/ui/PulsingDot.tsx`

## Setup / Dialogs (Overlays)
- First-run setup wizard (UI): `packages/core/src/tui/SetupWizard.tsx`
- Setup session + state machine: `packages/core/src/core/setup/session.ts`
- Setup/model pure helpers (context-window extraction/inference, runtime model profile metadata): `packages/core/src/config/modelContextWindow.ts`, `packages/core/src/config/modelCapability.ts`
- Web/Electron Setup Wizard contract: `docs/contracts/setup-wizard-contract.md`
- Shared setup configured-status gate: `packages/core/src/core/setup/configuredStatus.ts`
- Web setup bridge service (status/session/action/commit): `packages/core/src/core/setup/bridgeService.ts`
- Setup persistence + connection checks: `packages/core/src/adapters/setup/writeSetupFiles.ts`, `packages/core/src/adapters/setup/connectionTest.ts`
- Web setup side-channel wiring: `packages/core/src/app-server/devBridge.ts`, `packages/core/src/runtime/web/localUi.ts`
- Web setup route/UI: `packages/web-reference-react/src/App.tsx`
- Electron setup/main route gate + IPC handoff: `packages/desktop-electron/src/main.ts`, `packages/desktop-electron/src/preload.ts`
- Overlay manager (open/close dialogs): `packages/core/src/features/repl/overlays/OverlayManager.ts`
- Agents dialog (overlay UI): `packages/core/src/tui/agents/AgentsDialog.tsx`
- Permissions dialog (overlay UI): `packages/core/src/tui/permissions/PermissionsDialog.tsx`
- Config dialog (overlay UI, WIP): `packages/core/src/tui/config/ConfigDialog.tsx`

## Chat Loop / Streaming
- Chat loop + tool loop: `packages/core/src/chat/engine.ts`
  - TodoWrite reminders (prompt injection): `packages/core/src/prompts/reminders/todos.ts` + wiring in `packages/core/src/chat/engine.ts`
  - Runtime flags used by loop debug/limits: `packages/core/src/config/runtimeFlags.ts`
- Streaming provider factory (provider -> client): `packages/core/src/streaming/index.ts`
- Anthropic streaming client: `packages/core/src/streaming/anthropic/StreamClient.ts`
- OpenAI-compatible streaming client: `packages/core/src/streaming/openai/StreamClient.ts`
- SSE parser: `packages/core/src/streaming/anthropic/sseParser.ts`
- Stream events/types: `packages/core/src/streaming/types.ts`

## Context Management (UI transcript vs prompt history)
- Prompt-history owner (historyRef), pre/post pruning, `/compact`, auto-compact:
  - Pre-main routing coordinator (clear/compact/slash): `packages/core/src/features/repl/controller/send/sendPreMainRouting.ts`
  - Pre-main command handlers (`/compact`, consumed slash, local async): `packages/core/src/features/repl/controller/send/send.ts`
  - Main turn execution + prompt/history pipeline: `packages/core/src/features/repl/controller/send/sendMainTurn.ts`
  - Main turn deps/refs context builder: `packages/core/src/features/repl/controller/send/sendMainTurnContext.ts`
  - Context compression coordination service (manual compact + auto-compact preflight + pre/post prune/context): `packages/core/src/features/repl/controller/send/contextCompressionService.ts`
  - Shared send context types/builders: `packages/core/src/features/repl/controller/send/sendTypes.ts`
  - Wiring entry: `packages/core/src/features/repl/useReplController.ts`
- Budget + stats: `packages/core/src/chat/context/budget.ts`
- Token estimate fallback: `packages/core/src/chat/context/estimate.ts`
- Context diagnostics snapshot/report builder (`/context`): `packages/core/src/chat/context/contextDiagnostics.ts`
- Anthropic cache editing capability gate: `packages/core/src/chat/context/cacheEditing.ts`
- Durable context-collapse committed entry/snapshot schema and commit-candidate gate: `packages/core/src/chat/context/contextCollapseStore.ts`
- Shared query-time middle-layer strategy stack (`microcompact` / `prune` / `collapse` execution + facts): `packages/core/src/chat/context/middleLayerStrategyStack.ts`
- Shared runtime request projection adapter (persisted history vs request history/user for app-server + SDK): `packages/core/src/chat/context/turnRequestProjection.ts`
- Durable request projection owner (`raw history -> model-facing baseline -> durable snip -> durable collapse -> durable tool-result replacement`), durable snapshot merge/scoping, and projection facts: `packages/core/src/chat/context/contextProjection.ts`
- Message identity / fingerprint helpers for compression projection diagnostics, compact preserved segments, and preserved-tail relink: `packages/core/src/chat/context/compact.ts`
- Independent request-time tool-result budget replacement strategy: `packages/core/src/chat/context/toolResultBudget.ts`
- Independent request-time snip reducer for older assistant text messages + durable identity/fingerprint removal metadata: `packages/core/src/chat/context/snip.ts`
- Lightweight old-tool-result compaction (microcompact): `packages/core/src/chat/context/microCompact.ts`
- Model context window helpers (Config-owned; chat path is a compatibility shim): `packages/core/src/config/modelContextWindow.ts`, `packages/core/src/chat/context/modelWindow.ts`
- Hard pruning rules (tool pair invariants + truncation): `packages/core/src/chat/context/prune.ts`
- Tool-use/tool-result orphan-block normalization shared by durable projection and prune: `packages/core/src/chat/context/toolPairProjection.ts`
- Compaction tail selection (keep last N turns): `packages/core/src/chat/context/compact.ts`
- Tool-loop pruning (pre-`streamOnce`): `packages/core/src/chat/engine.ts` (`promptBudget`)
- Config knobs (defaults + env): `packages/core/src/config/settings/schema.ts`, `packages/core/src/config/settings/resolve.ts`, `packages/core/src/config/config.ts`
- Shared runtime preference literals used across config, semantics, persistence, app-server, and Web-facing adapters: `packages/core/src/shared/runtimePreferences.ts`

## Semantics Parity (TUI + App-Server + Web)
- Semantics governance contract (SoT): `docs/contracts/semantics-contract.md`
- Shared semantics source of truth:
  - Canonical event envelope/types: `packages/core/src/features/semantics/core/canonicalEvents.ts`
  - Transcript projection reducer (segment model): `packages/core/src/features/semantics/projection/transcriptProjection.ts`
  - Mode semantics: `packages/core/src/features/semantics/core/modeSemantics.ts`
  - Mode transition semantics (normalize/transition helpers): `packages/core/src/features/semantics/core/replModeTransition.ts`
  - Slash semantics: `packages/core/src/features/semantics/core/slashSemantics.ts`
  - Turn input builder: `packages/core/src/features/semantics/adapters/turnInputBuilder.ts`
  - Input state machine: `packages/core/src/features/semantics/runtime/inputStateMachine.ts`
  - Thread runtime state reducer (shared by app-server/web): `packages/core/src/features/semantics/runtime/threadRuntimeState.ts`
- Contract tests:
  - `packages/core/src/features/semantics/__tests__/*`
  - `packages/core/src/features/semantics/*.test.ts`
- Web-side parity adapters:
  - Tool event normalizer: `packages/web-reference-react/src/toolEventNormalizer.ts`
  - Event cursor (eventId dedupe + replaySeq-first ordering): `packages/web-reference-react/src/turnEventCursor.ts`
  - Reducer integration points: `packages/web-reference-react/src/store.ts`, `packages/web-reference-react/src/App.tsx`
  - Browser-safe tool parity adapters: `packages/web-reference-react/src/parity/tools/*`

## Web Reference React Client
- App package root (isolated deps/scripts): `packages/web-reference-react/package.json`
- Vite entry + mount: `packages/web-reference-react/src/main.tsx`
- App composition root: `packages/web-reference-react/src/App.tsx`
- RPC client transport: `packages/web-reference-react/src/rpcClient.ts`
- Runtime orchestration (initialize/notifications/replay/thread actions): `packages/web-reference-react/src/app/runtime/*`
- Core state machines/contracts/selectors: `packages/web-reference-react/src/app/core/*`
- App runtime hook boundary: `packages/web-reference-react/src/app/useAppRuntime.ts`
- UI shell/layout: `packages/web-reference-react/src/app/ui/AppShell.tsx`
- Transcript + tool rendering: `packages/web-reference-react/src/components/TranscriptPane.tsx`, `packages/web-reference-react/src/components/tool/*`
- Pending-input/approval UI: `packages/web-reference-react/src/components/InputApprovalDock.tsx`, `packages/web-reference-react/src/components/approval/*`
- Web parity adapters + reducers: `packages/web-reference-react/src/toolEventNormalizer.ts`, `packages/web-reference-react/src/turnEventCursor.ts`, `packages/web-reference-react/src/store.ts`, `packages/web-reference-react/src/parity/*`
- E2E protocol/UI specs + rpc mock: `packages/web-reference-react/e2e/*.spec.js`, `packages/web-reference-react/e2e/helpers/mockRpc.js`

## Desktop Electron Shell
- Package root (isolated desktop-shell deps/scripts): `packages/desktop-electron/package.json`
- Runtime orchestrator (dev/debug/preview process lifecycle): `packages/desktop-electron/scripts/run.mjs`
- Runtime bundle builder (copies root CLI/web artifacts into embedded runtime): `packages/desktop-electron/scripts/build-runtime.mjs`
- Embedded packaged runtime artifacts (generated): `packages/desktop-electron/runtime/{cli.mjs,web/*}`
- Main process window/security lifecycle: `packages/desktop-electron/src/main.ts`
- Preload bridge (minimal read-only runtime metadata): `packages/desktop-electron/src/preload.ts`
- Local usage guide: `packages/desktop-electron/README.md`

## Permissions / Approvals (Claude Code-style)
- Permissions store (read/merge/write settings): `packages/core/src/adapters/permissions/permissionsStore.ts`
- Rule matcher (deny/ask/allow priority + ToolName(spec) matching): `packages/core/src/adapters/permissions/matcher.ts`
- Permission key helpers: `packages/core/src/adapters/permissions/permissionKeys.ts`
- Skill allowlist (legacy, being migrated): `packages/core/src/adapters/permissions/skillAllowList.ts`
- Policy rules store + schema: `packages/core/src/core/policy/store.ts`, `packages/core/src/core/policy/schema.ts`
- Policy evaluation + explain output: `packages/core/src/core/policy/engine.ts`
- Tool preflight hook (central enforcement before tool execution): `packages/core/src/tools/executor/policyPreflight.ts`
- ToolCall → PolicyAction mapping: `packages/core/src/tools/executor/policyAction.ts`
- Policy explain formatter (CLI/debug): `packages/core/src/tools/executor/policyExplain.ts`
- Approval service (user prompts, remember, auditable decision): `packages/core/src/tools/executor/approvalService.ts`
- Shared approval-like prompt transaction helper (approval + skill preflight): `packages/core/src/tools/executor/approvalLikePrompt.ts`
- Bash policy engine (risk classification, confirmation triggers): `packages/core/src/tools/modules/bash/policy.ts`
- `/permissions` wiring (slash command → open overlay): `packages/core/src/features/commands/registry.ts`, `packages/core/src/features/commands/adapter.ts`, `packages/core/src/features/repl/useReplController.ts`, `packages/core/src/screens/REPL.tsx`
- `/permissions` UI: `packages/core/src/tui/permissions/PermissionsDialog.tsx`

## Hooks (Phase 1: PreToolUse / PermissionRequest / PostToolUse)
- Hook config (repo-level): `.formax/settings.local.json` (see `hooks` field)
- Hook scripts (repo-level): `.formax/hooks/*`
- Store (load/parse + list active hooks): `packages/core/src/hooks/store.ts`
- Matcher (which hooks apply to which event/tool/action): `packages/core/src/hooks/matcher.ts`
- Runner (spawn scripts, timeout, stdout/stderr, exit code semantics): `packages/core/src/hooks/runner.ts`
- Runtime (event payload builder + per-event orchestration): `packages/core/src/hooks/runtime.ts`
- Wiring points (where hooks are called):
  - PreToolUse: `packages/core/src/tools/executor/index.ts`
  - PermissionRequest: `packages/core/src/tools/executor/policyPreflight.ts`
  - PostToolUse (+ `additionalContext` injection before next LLM turn): `packages/core/src/chat/engine.ts`
- Audit/debug (observability, not UI):
  - Centralized `hook.run` audit fields: `packages/core/src/hooks/audit.ts`
  - `hook.run` schema: `packages/core/src/core/audit/schema.ts`
  - Debug previews (stdout tail, etc): `FORMAX_HOOKS_DEBUG=1`
- Tests:
  - Audit fields: `packages/core/src/hooks/audit.test.ts`
  - Runner/runtime: `packages/core/src/hooks/runner.test.ts`, `packages/core/src/hooks/runtime.test.ts`
  - PermissionRequest wiring: `packages/core/src/tools/executor/policyPreflight.test.ts`
  - PostToolUse wiring: `packages/core/src/chat/engine.test.ts`

## Prompts
- System prompt builder (profiles, env snapshot, constraints): `packages/core/src/prompts/system.ts`
- Prompt composition helpers: `packages/core/src/prompts/index.ts`, `packages/core/src/prompts/user.ts`, `packages/core/src/prompts/types.ts`
- Prompt authoring primitives (sections, reminder wrappers, text rendering): `packages/core/src/prompts/authoring.ts`
- TodoWrite reminder text + formatting helpers: `packages/core/src/prompts/reminders/todos.ts`
- Prompt porting status/TODOs: `packages/core/src/prompts/STATUS.md`, `system-prompts/PORTING-STATUS.md`

## Tools (Registry → Execution → Presentation)

### Tool registry + loader
- Tool definitions (ToolDefinition): `packages/core/src/tools/types.ts`
- Tool module registry: `packages/core/src/tools/registry.ts`
- Built-in tool modules registration: `packages/core/src/tools/modules/index.ts`
- Runtime tool module wiring (including manager-bound MCP module): `packages/core/src/runtime/bootstrap/tooling.ts`
- MCP tool-name/config/catalog/result pure helpers: `packages/core/src/mcp/*`
- MCP generic tool module (dynamic catalog patch, handler, REPL/TUI presenter): `packages/core/src/tools/modules/mcp/*`

### Tool execution pipeline
- Executor entry (enforces allow/deny lists, routes to handlers): `packages/core/src/tools/executor/index.ts`
- Executor handlers (e.g. Task): `packages/core/src/tools/executor/handlers/*`
- Runtime task manager (background tasks, cancel): `packages/core/src/tools/runtime/taskManager.ts`
- Runtime user input manager (approval prompts / AskUserQuestion answers): `packages/core/src/tools/runtime/userInputManager.ts`
- Runtime active interactive prompt descriptor surface: `packages/core/src/tools/runtime/interactivePromptDescriptor.ts`, `packages/core/src/tools/runtime/userInputContext.tsx`
- Runtime ask-user-question transaction helper: `packages/core/src/tools/runtime/askUserQuestionPrompt.ts`
- Runtime interactive prompt descriptor builders (approval / ask payload wiring): `packages/core/src/tools/runtime/interactivePromptDescriptor.ts`
- Runtime unified interactive prompt transaction core: `packages/core/src/tools/runtime/interactivePromptTransaction.ts`
- Deferred tool exposure store + ToolSearch session state: `packages/core/src/tools/runtime/deferredToolExposure.ts`
- Cross-entry deferred exposure resolver (REPL/app-server/SDK shared wiring): `packages/core/src/tools/runtime/deferredToolExposureResolver.ts`
- ToolSearch engine core (mode parsing + regex/BM25/hybrid ranking): `packages/core/src/tools/runtime/toolSearchEngine.ts`

### Tool UI / presenters
- Default tool renderer: `packages/core/src/components/tool/ToolMessage.tsx`
- Tool UI Blocks renderer (C-lite): `packages/core/src/components/tool/ToolUiBlocks.tsx`
- Presenter interface: `packages/core/src/shared/toolPresenterContracts.ts`
- Blocks presenter helper: `createToolBlocksPresenter` in `packages/core/src/shared/toolPresenterContracts.ts`
- Web generic tool block registry, including `mcp__*` renderer: `packages/web-reference-react/src/components/tool/toolBlocksRegistry.ts`
- FS read approval bridge (blocks presenter → runtime user input): `packages/core/src/components/tool/FsReadApprovalToolBlock.tsx`
- Inline interactive prompt surface guard: `packages/core/src/components/tool/InteractivePromptSurfaceContext.tsx`
- Shared approval prompt (Edit/Write/NotebookEdit): `packages/core/src/components/tool/editApprovalPrompt.tsx`
- Fallback presenter: `packages/core/src/components/tool/FallbackToolPresenter.tsx`

### Tool specs (“model-facing contract”)
- Each tool module owns its spec under `packages/core/src/tools/modules/<tool>/spec.ts`.
- Reference snapshot for parity checks: `packages/core/src/tools/specs/reference/tools-copy.json`
- Spec/handler drift tracking: `packages/core/src/tools/SPEC_HANDLER_MISMATCHES.md`

## Key Tool Modules (where to implement behavior)
- Read: `packages/core/src/tools/modules/read/*`
- Write (approval + preview UI): `packages/core/src/tools/modules/write/*`
- Edit (diff UI + approval): `packages/core/src/tools/modules/edit/*`
- Glob: `packages/core/src/tools/modules/glob/*`
- Grep: `packages/core/src/tools/modules/grep/*`
- Bash (policy, filepath extraction, approval workflow): `packages/core/src/tools/modules/bash/*`
- AskUserQuestion (interactive prompts): `packages/core/src/tools/modules/askUserQuestion/*`
- KillShell (terminate running shell): `packages/core/src/tools/modules/killShell/*`
- NotebookEdit: `packages/core/src/tools/modules/notebookEdit/*`
- TodoWrite: `packages/core/src/tools/modules/todoWrite/*`
- WebFetch: `packages/core/src/tools/modules/webFetch/*`
- WebSearch: `packages/core/src/tools/modules/webSearch/*`
- Skill: `packages/core/src/tools/modules/skill/*`
- SlashCommand: `packages/core/src/tools/modules/slashCommand/*`
- Task (sub-agents + nested prompts UI): `packages/core/src/tools/modules/task/*`
- TaskOutput (background task UI): `packages/core/src/tools/modules/taskOutput/*`
- Search (high-level search): `packages/core/src/tools/modules/search/*`
- MCP generic dynamic tools: `packages/core/src/tools/modules/mcp/*`

## Plan Mode
- REPL mode type: `packages/core/src/features/repl/mode.ts`
- REPL mode transition application: `packages/core/src/features/repl/useReplController.ts`
- Plan session manager (plan file path, lifecycle): `packages/core/src/features/repl/planSession.ts`
- Plan path helpers: `packages/core/src/shared/utils/planMode.ts`
- Plan mode injected blocks: `packages/core/src/features/repl/controller/send/sendMainTurn.ts` (wired by `packages/core/src/features/repl/useReplController.ts`)
- App-server runtime mode change notifications: `packages/core/src/app-server/turnRunner.ts` (`turn/modeChanged`)
- Plan tools:
  - EnterPlanMode: `packages/core/src/tools/modules/enterPlanMode/*`
  - ExitPlanMode: `packages/core/src/tools/modules/exitPlanMode/*`

## Sub-agents (Task tool)
- Built-in subagents registry (names, prompts, tool allowlist): `packages/core/src/features/subagents/builtins.ts`
- Subagent registry: `packages/core/src/features/subagents/registry.ts`
- Runner (spawning + tool allowlist enforcement): `packages/core/src/features/subagents/runner.ts`
- Agents creation wizard (generate with model / manual): `packages/core/src/features/subagents/agentsWizard.ts`
- Sub-agent approval / non-interactive policy contract: `docs/contracts/permissions-policy-contract.md`

## Slash Commands
- Slash command registry + suggest + dispatch: `packages/core/src/features/commands/registry.ts`
- Built-in command effects → command contract adapter: `packages/core/src/features/commands/adapter.ts`, `packages/core/src/features/commands/contracts.ts`
- Custom commands store (scan `.formax/commands/**` and global overrides): `packages/core/src/features/commands/CommandStore.ts`
- Custom command rendering (markdown → injected prompt blocks): `packages/core/src/features/commands/render.ts`
- CLI wires suggestions/registry into REPL: `packages/core/src/features/repl/useReplController.ts`, `packages/core/src/screens/REPL.tsx`

## Config / Auth / Paths
- Runtime config loader: `packages/core/src/config/config.ts`
- Runtime env flag parser (single entry for `FORMAX_*` runtime toggles): `packages/core/src/config/runtimeFlags.ts`
- Runtime model profile and model capability helpers: `packages/core/src/config/runtimeModelProfile.ts`, `packages/core/src/config/modelCapability.ts`, `packages/core/src/config/modelContextWindow.ts`
- Config paths + migration/legacy behavior: `packages/core/src/adapters/fs/configPaths.ts`
- Reading config files (auth.json, etc): `packages/core/src/adapters/fs/configFiles.ts`

## Subsystem READMEs (Deep Dives)
- Core (config/auth/setup/policy): `packages/core/src/core/README.md`
- Tools (registry/executor/presenters/runtime): `packages/core/src/tools/README.md`
- Streaming (SSE parsing + tool execution): `packages/core/src/streaming/README.md`
- Sub-agents (registry/runner/allowlist): `packages/core/src/features/subagents/README.md`

## Docs Governance (Quick Links)
- Docs source-of-truth map: `docs/index.md`
- Core contracts:
  - Semantics: `docs/contracts/semantics-contract.md`
  - Interactive input: `docs/contracts/interactive-input-contract.md`
  - Permissions/policy: `docs/contracts/permissions-policy-contract.md`
  - Transcript surface: `docs/contracts/transcript-surface-contract.md`
  - Prompt/tool exposure: `docs/contracts/prompt-tool-exposure-contract.md`
  - Tool runtime: `docs/contracts/tool-runtime-contract.md`
- Runtime config / env:
  - `docs/contracts/config-settings-contract.md`
  - `docs/environment-variables.md`
- App-server + Web summaries:
  - `docs/contracts/app-server-interaction-contract.md`
  - `docs/references/app-server-api-reference.md`
  - `docs/frontend/app-server-ui-spec.md`
  - `docs/contracts/web-parity-adapter-contract.md`
- Verification / troubleshooting:
  - `docs/runbooks/runbook.md`
  - `docs/audits/repl-single-writer-audit.md`
  - `docs/pitfalls/index.md`

## If You're Adding a Feature, Start Here
- UI / REPL behavior: `packages/core/src/screens/REPL.tsx` + `packages/core/src/features/repl/useReplController.ts`
- New tool: `packages/core/src/tools/modules/<name>/{spec.ts,handler.ts,presenter.tsx,index.ts}` + register in `packages/core/src/tools/registry.ts`
- New slash command: `packages/core/src/features/commands/registry.ts` + `packages/core/src/features/commands/adapter.ts`
- Cross-surface semantic change: `packages/core/src/features/semantics/*` first, then app-server / TUI / Web adapters
- Sub-agent capability / prompt: `packages/core/src/features/subagents/builtins.ts` + `packages/core/src/features/subagents/prompts/*`
