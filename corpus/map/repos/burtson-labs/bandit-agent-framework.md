# burtson-labs/bandit-agent-framework

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e926d20a48e6 @ d3f4e5b0d79a465f

## Summary (orientation draft, not independently verified)

The README documents a local-first AI coding agent with two hosts (VS Code extension and CLI) over one stealth-core-runtime, Ollama-based models, skills, memory files, hooks, MCP client/server, and a scoped approval-gate permission model; BANDIT.md and the contributing section describe development practice. Evidence coverage: 134 of 225 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 32 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Stated design rules include local models as first-class citizens, one host-agnostic runtime, language adapters validating before write so invalid content never reaches disk, and intent-based skill activation. -- evidence: [README.md#L535-L538](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L535-L538)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run pnpm test (what CI runs on PRs), add contract tests for new behaviors, and add real-trace replay fixtures for recurring failure modes per the agent-core test docs. -- evidence: [README.md#L568-L568](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L568-L568), [README.md#L570-L572](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L570-L572)
  - [observation/documented] Repository development practice: the repo's own BANDIT.md instructs agents to read files before editing, prefer replace_range for large changes, run typecheck/smoke/vitest before claiming done, and bump versions without amending tagged releases. -- evidence: [BANDIT.md#L6-L8](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/BANDIT.md#L6-L8), [BANDIT.md#L17-L20](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/BANDIT.md#L17-L20)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are markdown files with YAML frontmatter in .bandit/skills/ that load on the next turn; triggers are regex matches on the user prompt, activation:always skills run every turn, and legacy JSON skills still load. -- evidence: [README.md#L76-L80](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L76-L80)
  - [observation/documented] The default skill set includes always-on filesystem and git skills plus context-triggered code review, testing, planning, semantic search, and Gmail-dependent mail search skills. -- evidence: [README.md#L84-L90](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L84-L90)
- interfaces (4 claim(s)):
  - [observation/documented] The product ships two hosts — a VS Code/Cursor extension (Bandit Stealth) and a terminal CLI — both backed by the same stealth-core-runtime package, with skills, memory files, and hooks working identically across them. -- evidence: [README.md#L34-L34](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L34-L34), [README.md#L29-L32](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L29-L32)
  - [observation/documented] The CLI offers slash commands including /help, /doctor, /model, /skills, /session, /memory, /remember, /trace, /insights, and /exit. -- evidence: [README.md#L200-L212](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L200-L212)
- memory-state (3 claim(s)):
  - [observation/documented] The agent auto-loads BANDIT.md, CLAUDE.md, or AGENTS.md from the workspace root into the system prompt; /remember appends facts and /init scaffolds a new BANDIT.md. -- evidence: [README.md#L131-L133](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L131-L133), [README.md#L98-L101](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L98-L101)
  - [observation/documented] A MEMORY.md topic index (capped at 4 KB) loads every turn while linked memory/ files (32 KB cap) are lazily fetched via read_memory when the task matches. -- evidence: [README.md#L149-L152](https://github.com/Burtson-Labs/bandit-agent-framework/blob/e926d20a48e61918946439a5e99c1d259dca45b3/README.md#L149-L152)
- orchestration (2 claim(s)):
More evidence: [full detail](bandit-agent-framework.detail.md)

Metadata and full claim list: [full detail](bandit-agent-framework.detail.md)
Human notes ([notes](bandit-agent-framework.notes.md), never overwritten by build)

[Back to map index](../../index.md)
