# pawanosman/opencursor

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e94886325f76 @ 4d702a4dae4114d6

## Summary (orientation draft, not independently verified)

OpenCursor is an open-source VS Code AI coding agent with local (llama.cpp/Ollama) and cloud providers, a 25-tool suite, semantic codebase search, approval policies, and subagents. The evidence is README marketing/feature text plus a detailed changelog; no source code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The agent ships a suite of 25 tools including read/write/edit, shell, grep/glob, semantic search, web search/fetch, notebooks, todos, subagents, and MCP. -- evidence: [README.md#L45-L54](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L45-L54)
  - [observation/documented] Local AI support includes built-in llama.cpp management (spawning llama-server with control over context size, GPU layers, flash attention, etc.) and zero-config Ollama integration. -- evidence: [README.md#L23-L26](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L23-L26)
- design-choices (2 claim(s)):
  - [observation/documented] Edits get per-hunk Keep/Undo CodeLenses for inline review, and the README states this works without requiring git. -- evidence: [README.md#L45-L54](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L45-L54)
  - [observation/documented] Shell commands run in their own child shell and kill child processes on termination, and denied commands are checked per sub-command to prevent chaining-based bypasses. -- evidence: [CHANGELOG.md#L111-L119](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L111-L119)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: build from source with pnpm install and pnpm run compile (or watch), press F5 for the Extension Development Host, and package with pnpm run vsix; issues and PRs are welcome. -- evidence: [README.md#L80-L80](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L80-L80), [README.md#L76-L76](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L76-L76), [README.md#L69-L74](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L69-L74)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] OpenCursor is a VS Code extension installable from the Marketplace or as a .vsix, providing a multi-tab sidebar chat with @-mentions of files, folders, docs, commits, diffs, terminals, and rules. -- evidence: [README.md#L45-L54](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L45-L54), [README.md#L58-L63](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L58-L63)
  - [observation/documented] Providers include OAuth sign-in for Claude Code, OpenAI Codex, and Google Antigravity accounts, API-key presets (OpenAI, Anthropic, Gemini, OpenRouter), and custom OpenAI-compatible or Anthropic-style endpoints usable simultaneously. -- evidence: [README.md#L38-L41](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/README.md#L38-L41)
- memory-state (2 claim(s)):
  - [observation/documented] The semantic index persists across VS Code restarts, re-indexes incrementally on changed files, and auto-indexes new/modified files via a workspace file watcher; indexing can be fully disabled in settings. -- evidence: [CHANGELOG.md#L257-L262](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L257-L262)
  - [observation/documented] Context management includes auto-compaction with a verbatim tail, lossless persisted chat history for export, and latest-wins deduplication of older tool results for the same target. -- evidence: [CHANGELOG.md#L164-L170](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L164-L170)
- orchestration (2 claim(s)):
  - [observation/documented] Project mode lets the agent act as a project lead delegating to a team of subagents (TeamDef presets), with subagents running on isolated history so the parent only receives the final Task result. -- evidence: [CHANGELOG.md#L266-L269](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L266-L269), [CHANGELOG.md#L81-L86](https://github.com/PawanOsman/OpenCursor/blob/e94886325f765dc4f98f49b20e3b44af05a2f3d1/CHANGELOG.md#L81-L86)
More evidence: [full detail](opencursor.detail.md)

Metadata and full claim list: [full detail](opencursor.detail.md)
Human notes ([notes](opencursor.notes.md), never overwritten by build)

[Back to map index](../../index.md)
