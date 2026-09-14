# atomgit-atomcode/atomcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 287bff70f940 @ 21b0b17abcf968f4

## Summary (orientation draft, not independently verified)

Selected evidence records: AtomCode is described as an open-source terminal AI coding agent written in Rust, positioned as an alternative to Claude Code / Cursor Agent that connects to any OpenAI-compatible API. The project is a layered Rust workspace with crates for kernel (agent loop), capabilities (providers/tools/MCP/skills/sessions/memory), coding, review, TUI, CLI, and daemon (HTTP/SSE/WebSocket transport).

## Source coverage

Source coverage (partial): 6 of 146 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AtomCode is described as an open-source terminal AI coding agent written in Rust, positioned as an alternative to Claude Code / Cursor Agent that connects to any OpenAI-compatible API. -- evidence: [README.md#L47-L47](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L47-L47), [README.md#L11-L13](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L11-L13)
- components (1 claim(s)):
  - [observation/documented] The project is a layered Rust workspace with crates for kernel (agent loop), capabilities (providers/tools/MCP/skills/sessions/memory), coding, review, TUI, CLI, and daemon (HTTP/SSE/WebSocket transport). -- evidence: [README.md#L629-L639](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L629-L639)
- design-choices (1 claim(s)):
  - [observation/documented] Stated design principles include tech-stack agnosticism via descriptor-file detection (package.json, Cargo.toml, etc.), a single CodingRuntime owner, tool safety, token-budget-aware context windowing, and directed dependencies keeping the kernel neutral. -- evidence: [README.md#L650-L650](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L650-L650), [README.md#L652-L652](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L652-L652), [README.md#L648-L648](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L648-L648), [README.md#L654-L654](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L654-L654), [README.md#L646-L646](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L646-L646)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building from source requires Rust 1.88+ and Git; the webui frontend must be built with npm before the Rust build (webui/dist is gitignored and embedded), and cargo clean -p atomcode-daemon is needed after frontend rebuilds. -- evidence: [README.md#L187-L191](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L187-L191), [README.md#L678-L680](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L678-L680), [README.md#L203-L207](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L203-L207)
- skills-patterns (1 claim(s)):
  - [observation/documented] Users can define custom slash commands as Markdown template files with frontmatter (name, description, args) in global, project-level, or plugin directories; project-level overrides global, but custom commands cannot shadow built-ins. -- evidence: [README.md#L564-L564](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L564-L564), [README.md#L568-L572](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L568-L572), [README.md#L623-L623](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L623-L623), [README.md#L590-L592](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L590-L592)
- interfaces (4 claim(s)):
  - [observation/documented] Built-in tools include file/shell operations (read_file, edit_file, bash, grep, glob), web search/fetch, code-graph tools (list_symbols, trace_callers, blast_radius), auto_fix, and use_skill. -- evidence: [README.md#L77-L79](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L77-L79), [README.md#L83-L84](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L83-L84), [README.md#L71-L73](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L71-L73)
  - [observation/documented] The CLI offers persistent sessions (--continue, /resume), AtomGit OAuth login, SSO login, headless single-prompt mode, and a daemon exposing an HTTP API with SSE streaming chat. -- evidence: [README.md#L103-L107](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L103-L107)
- memory-state (2 claim(s)):
  - [observation/documented] Memory commands let users save facts (/remember, with --global scope), remove them (/forget), and list them (/memory); sessions are persisted and resumable. -- evidence: [README.md#L520-L524](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L520-L524), [README.md#L103-L107](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L103-L107)
  - [observation/documented] A .atomcode.md file in the project root provides persistent context included in the system prompt; AGENTS.md is supported as an alternative, with .atomcode.md taking priority if both exist. -- evidence: [README.md#L670-L670](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L670-L670), [README.md#L658-L658](https://github.com/atomgit-atomcode/atomcode/blob/287bff70f9400c24f4afd8fcf4762fbab63d8efa/README.md#L658-L658)
- orchestration (1 claim(s)):
More evidence: [full detail](atomcode.detail.md)

Metadata and full claim list: [full detail](atomcode.detail.md)
Human notes ([notes](atomcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
