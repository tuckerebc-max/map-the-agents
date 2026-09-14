# zykjshadow/async

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2c18a43c0711 @ b8601518a228cb3a

## Summary (orientation draft, not independently verified)

Evidence describes Async IDE, an open-source Electron+React+Monaco agent-first desktop workspace, plus a curated LLM wiki documentation layer and a macOS auto-update test guide documenting unsigned-build behavior. Evidence coverage: 170 of 206 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 43 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Async IDE is an open-source, agent-first desktop workspace combining Agent, editor, Git, and terminal, licensed Apache 2.0, local-first with BYOK model access. -- evidence: [README.md#L290-L290](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L290-L290), [README.md#L33-L33](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L33-L33), [README.md#L7-L10](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L7-L10)
- components (1 claim(s)):
  - [observation/documented] The main process contains agentLoop.ts (multi-round tool calls, partial JSON streaming, tool repair, aborts), toolExecutor, LLM adapters, gitService, threadStore, settingsStore, LSP session, and PTY terminal. -- evidence: [README.md#L142-L155](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L142-L155), [README.md#L182-L224](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L182-L224), [README.md#L173-L178](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L173-L178)
- design-choices (1 claim(s)):
  - [observation/documented] The app is built from scratch on Electron + React + Monaco and is explicitly not a VS Code fork, with a deliberately lean two-process architecture and clear IPC boundaries. -- evidence: [README.md#L29-L29](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L29-L29), [README.md#L173-L178](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L173-L178)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: docs/llm-wiki is a structured knowledge layer for humans and agents, with maintenance conventions like link-first navigation, code-over-docs conflict resolution, and recording contradictions in a dedicated page. -- evidence: [docs/llm-wiki/README.md#L3-L5](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/README.md#L3-L5), [docs/README.md#L5-L6](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/README.md#L5-L6), [docs/llm-wiki/README.md#L9-L13](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/README.md#L9-L13), [docs/llm-wiki/README.md#L103-L105](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/README.md#L103-L105)
  - [observation/documented] Repository development practice: the repo can be run with npm install then npm run desktop, with dev, dev:debug, and icons scripts; the macOS test guide documents building unsigned packages via npm run release:mac:unsigned. -- evidence: [README.md#L248-L253](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L248-L253), [docs/mac-mini-auto-update-test.md#L99-L102](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/mac-mini-auto-update-test.md#L99-L102), [README.md#L266-L270](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L266-L270)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The Composer offers four modes: Agent (full auto), Plan (review before run), Ask (read-only Q&A), and Debug (systematic troubleshooting). -- evidence: [README.md#L39-L46](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L39-L46), [docs/llm-wiki/project-overview.md#L22-L25](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/project-overview.md#L22-L25)
  - [observation/documented] The app bridges to Telegram, Slack, Discord, and Feishu bots; inbound messages run through botRuntime, reusing the same agentLoop and teamOrchestrator paths as the desktop Composer, with per-integration model, workspace, and allowlist config. -- evidence: [README.md#L129-L134](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L129-L134)
- memory-state (1 claim(s)):
  - [observation/documented] Threads, settings, and plans persist locally as JSON/Markdown under Electron userData (threads.json, settings.json, .async/plans/); threads.json is the authoritative conversation source. -- evidence: [README.md#L230-L232](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L230-L232), [README.md#L234-L234](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L234-L234), [README.md#L228-L228](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L228-L228), [README.md#L173-L178](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L173-L178)
- orchestration (1 claim(s)):
  - [observation/documented] Team mode provides multi-agent collaboration with a Lead planning, specialist execution, reviewer verification, and plan-approval workflows; nested and background sub-agents are supported. -- evidence: [README.md#L39-L46](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L39-L46), [docs/llm-wiki/project-overview.md#L22-L25](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/docs/llm-wiki/project-overview.md#L22-L25), [README.md#L105-L109](https://github.com/ZYKJShadow/Async/blob/2c18a43c0711d1f991a6eabd913831f9c82794b0/README.md#L105-L109)
- tools-permissions (1 claim(s)):
More evidence: [full detail](async.detail.md)

Metadata and full claim list: [full detail](async.detail.md)
Human notes ([notes](async.notes.md), never overwritten by build)

[Back to map index](../../index.md)
