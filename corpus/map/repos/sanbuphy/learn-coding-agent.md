# sanbuphy/learn-coding-agent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ce8ca4a8e722 @ e96abc602fa9c456

## Summary (orientation draft, not independently verified)

This repository is a quadrilingual educational study of the Claude Code CLI agent (v2.1.88), compiled from public references, containing architecture documentation, telemetry/privacy analysis, and harness-mechanism breakdowns. Claims below describe what the documentation reports about Claude Code, not independently verified runtime behavior. Evidence coverage: 122 of 248 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The analyzed target is Claude Code v2.1.88; reports cover telemetry, codenames, undercover mode, remote control, and a future roadmap. -- evidence: [README.md#L59-L65](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L59-L65), [README.md#L24-L24](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L24-L24)
  - [observation/documented] Documentation reports roughly 1,884 TS/TSX files, ~512,664 lines, ~40+ built-in tools, ~80+ slash commands, and a Bun runtime compiled to a Node.js >= 18 bundle. -- evidence: [README.md#L83-L91](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L83-L91)
- components (1 claim(s)):
  - [observation/documented] The documented source layout includes main.tsx (REPL bootstrap), QueryEngine.ts (headless/SDK lifecycle), query.ts (main agent loop, largest file), Tool.ts, tools.ts, commands.ts, and a bridge/ directory for Claude Desktop/remote sessions. -- evidence: [README.md#L121-L248](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L121-L248)
- design-choices (2 claim(s)):
  - [observation/documented] Documented design patterns include AsyncGenerator streaming through the query chain, a buildTool factory with safe defaults, compile-time feature-flag dead-code elimination via Bun, and AsyncLocalStorage for per-agent context isolation. -- evidence: [README.md#L779-L791](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L779-L791)
  - [observation/documented] The documentation frames Claude Code as a minimal agent loop (call API, check stop_reason for tool_use, execute tools, append results) wrapped by a production harness adding permissions, streaming, concurrency, compaction, sub-agents, persistence, and MCP. -- evidence: [README.md#L112-L115](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L112-L115), [README.md#L101-L109](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L101-L109)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The entry layer routes interactive use through a REPL and headless/SDK use through QueryEngine, whose submitMessage returns an AsyncGenerator of SDKMessages streamed to the consumer. -- evidence: [README.md#L254-L314](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L254-L314)
  - [observation/documented] Each tool implements a documented lifecycle (validateInput, checkPermissions, call) plus capability predicates like isConcurrencySafe, isReadOnly, and isDestructive, and React/Ink renderers for tool use and results. -- evidence: [README.md#L375-L375](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L375-L375), [README.md#L377-L402](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L377-L402)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions persist as append-only JSONL under ~/.claude/projects/<hash>/sessions/, with resume options --continue, --resume <id>, and --fork-session; user messages are written blocking for crash recovery while assistant messages use a fire-and-forget queue. -- evidence: [README.md#L640-L645](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L640-L645), [README.md#L626-L631](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L626-L631), [README.md#L633-L638](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L633-L638)
  - [observation/documented] Context management uses three compression strategies: autoCompact (summarize old messages via an API call when tokens exceed a threshold), snipCompact, and contextCollapse, the latter two behind feature flags. -- evidence: [README.md#L542-L548](https://github.com/sanbuphy/learn-coding-agent/blob/ce8ca4a8e7224817f46e5db08973b4022bd1eb0a/README.md#L542-L548)
- orchestration (1 claim(s)):
More evidence: [full detail](learn-coding-agent.detail.md)

Metadata and full claim list: [full detail](learn-coding-agent.detail.md)
Human notes ([notes](learn-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
