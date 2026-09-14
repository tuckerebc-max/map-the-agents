# vishal2612200/agentpack

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 42291598e793 @ fa61ecf8e3ff9329

## Summary (orientation draft, not independently verified)

AgentPack is a local, agent-neutral context-preparation and workflow-state layer for AI coding agents, distributed as agentpack-cli (PyPI) and an npm wrapper, with a CLI, MCP server, adapters/installers, thread-scoped local state under .agentpack/, and a published file-selection benchmark. The prior summary's mention of a dashboard distribution component is unsupported by the cited slices and has been removed. Evidence coverage: 118 of 183 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 48 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is at alpha version 0.4.4, licensed AGPL v3, with APIs that may change before 1.0 and platform targets of macOS, Linux, and Windows PowerShell with Git for Windows. -- evidence: [README.md#L422-L422](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L422-L422), [README.md#L398-L398](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L398-L398), [README.md#L400-L402](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L400-L402)
- components (2 claim(s)):
  - [observation/documented] The architecture is a local pipeline: scan with .agentignore, build offline summaries and a Tree-sitter semantic graph, score files for the task, select by value per token, redact secrets at materialization, and cache a pack registry with block IDs. -- evidence: [docs/architecture.md#L3-L3](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L3-L3), [docs/architecture.md#L66-L86](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L66-L86)
  - [observation/documented] Adapters render agent-specific context files (Claude, Cursor, Windsurf, Codex, Antigravity, generic), while separate installers configure each tool's repo files such as CLAUDE.md, .cursorrules, and AGENTS.md. -- evidence: [docs/architecture.md#L269-L277](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L269-L277), [docs/architecture.md#L279-L284](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L279-L284)
- design-choices (1 claim(s)):
  - [observation/documented] Core scan, route, pack, stats, explain, and benchmark operations run without hosted indexing, embeddings, or model API calls; network use is limited to explicit GitHub operations, optional enrichment, and external-agent workflows. -- evidence: [README.md#L264-L267](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L264-L267), [README.md#L276-L280](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L276-L280)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a CLI four-command loop: agentpack work, learn --json, finish, and doctor, where work prepares task context, finish records validation and task memory, and doctor checks installation and integration. -- evidence: [README.md#L88-L93](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L88-L93), [README.md#L362-L366](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L362-L366)
  - [observation/documented] The MCP server exposes tools including start_task, pack_context, get_context, explain, related, stats, and delta, per the package layout documentation. -- evidence: [docs/architecture.md#L304-L304](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L304-L304)
- memory-state (2 claim(s)):
  - [observation/documented] Generated context, receipts, task state, snapshots, and memory are stored locally under .agentpack/, and summary caches are keyed by file hash so only changed files are re-summarized. -- evidence: [README.md#L264-L267](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/README.md#L264-L267), [docs/architecture.md#L386-L386](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L386-L386)
  - [observation/documented] Sessions are thread-scoped by default: when host session/thread environment variables are present, commands and MCP tools use isolated state under .agentpack/threads/<id>/, with --thread global as a legacy opt-out. -- evidence: [docs/architecture.md#L343-L368](https://github.com/vishal2612200/agentpack/blob/42291598e79344feae3a9dfdfd0778df9e7dd578/docs/architecture.md#L343-L368)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agentpack.detail.md)

Metadata and full claim list: [full detail](agentpack.detail.md)
Human notes ([notes](agentpack.notes.md), never overwritten by build)

[Back to map index](../../index.md)
