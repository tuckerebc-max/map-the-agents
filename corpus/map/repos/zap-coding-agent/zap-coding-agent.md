# zap-coding-agent/zap-coding-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6ab48b82c15e @ e16dd8e1241033bc

## Summary (orientation draft, not independently verified)

ZAP is a terminal-first, local AI coding agent written in Rust and shipped as a single statically-linked binary, featuring keyword-triggered skill injection, a tree-sitter/SQLite AST code index, lazy-loaded MCP servers, three permission modes, secret scanning with audit logging, and four on-demand project context files. Evidence coverage: 147 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 33 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] A documented domain map lists modules including agent_core, llm_client, tools with permission_manager and shell_runner, context_manager, code_index, mcp, persistence, skill_manager, and remote session sharing. -- evidence: [README.md#L115-L125](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L115-L125)
  - [observation/documented] The AST code index is built at startup with tree-sitter and SQLite, stored at .zap/code.db, supports Rust, Python, TypeScript, JavaScript, Go, and Java, and reindexes edited files before the next LLM turn. -- evidence: [README.md#L365-L365](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L365-L365), [README.md#L267-L267](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L267-L267), [README.md#L279-L279](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L279-L279), [README.md#L233-L233](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L233-L233)
- design-choices (1 claim(s)):
  - [observation/documented] ZAP is a terminal-first, local AI coding agent written in Rust, distributed as a single statically-linked binary with no runtime dependency on Python, Node.js, or Docker. -- evidence: [README.md#L9-L9](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L9-L9), [README.md#L430-L434](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L430-L434), [README.md#L428-L428](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L428-L428)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (3 claim(s)):
  - [observation/documented] ZAP uses a skill system of markdown files injected only when triggered: always-on skills (e.g. karpathy-guidelines) fire every turn, while triggered skills like rust, git, or security fire on keyword matches in the user's message. -- evidence: [README.md#L150-L150](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L150-L150), [README.md#L161-L172](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L161-L172), [README.md#L154-L157](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L154-L157)
  - [observation/documented] Skills resolve by priority: project-level .zap/skills/ overrides personal ~/.zap/skills/, which overrides built-in defaults compiled into the binary; same-name custom skills override built-ins. -- evidence: [README.md#L187-L187](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L187-L187), [README.md#L218-L218](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L218-L218), [README.md#L212-L216](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L212-L216)
- interfaces (1 claim(s)):
  - [observation/documented] Index-backed tools include code_map, find_definition, find_references, who_calls, file_imports, where_imported, find_subtypes/supertypes, pack_context, ripple_analysis, get_diagnostics, lsp_definition, and lsp_type_at. -- evidence: [README.md#L283-L296](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L283-L296)
- memory-state (1 claim(s)):
  - [observation/documented] ZAP maintains four context files (ZAP.md, .zap/understanding.md, .zap/context.md, .zap/session_log.md) updated at defined times and loaded on demand via read_file rather than pre-loaded into context. -- evidence: [README.md#L81-L86](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L81-L86), [README.md#L88-L88](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L88-L88)
- orchestration (1 claim(s)):
  - [observation/documented] MCP servers stay pending at startup with only a lightweight mcp_connect stub in context; the server process is spawned and its real tool schemas fetched only when the model calls mcp_connect. -- evidence: [README.md#L470-L475](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L470-L475), [README.md#L468-L468](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L468-L468), [README.md#L459-L459](https://github.com/zap-coding-agent/zap-coding-agent/blob/6ab48b82c15ea52b82ed8fa3598e4118cd4b2914/README.md#L459-L459)
- tools-permissions (2 claim(s)):
More evidence: [full detail](zap-coding-agent.detail.md)

Metadata and full claim list: [full detail](zap-coding-agent.detail.md)
Human notes ([notes](zap-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
