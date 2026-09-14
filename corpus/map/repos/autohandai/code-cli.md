# autohandai/code-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f4775fdebd93 @ 39ddcfcd21c53f63

## Summary (orientation draft, not independently verified)

Evidence covers Autohand Code CLI, a terminal-native AI coding agent with an Ink-based REPL, a modular skills system with multi-source discovery, multi-provider LLM support, browser automation, and memory tools. Most claims are documentation-based; no evaluation or contributor-workflow evidence is present. Evidence coverage: 157 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 88 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Browser automation is built in via /browser or --browser flags, with tools for tabs, tab groups, network and console inspection, extension bridge calls, and JavaScript execution. -- evidence: [docs/announcing-0.9.md#L53-L53](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/announcing-0.9.md#L53-L53)
- design-choices (1 claim(s)):
  - [observation/documented] Every installer scans writable PATH directories and silently replaces any existing `agent` command so `agent` resolves to Autohand, which can break other tools' `agent` commands. -- evidence: [README.md#L52-L60](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L52-L60)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (3 claim(s)):
  - [observation/documented] Skills are SKILL.md packages with YAML frontmatter (name, description, optional allowed-tools, license, compatibility, metadata) plus markdown instructions injected into agent context when activated. -- evidence: [docs/agent-skills.md#L28-L28](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L28-L28), [docs/agent-skills.md#L21-L21](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L21-L21), [docs/agent-skills.md#L149-L149](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L149-L149), [docs/agent-skills.md#L170-L177](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L170-L177), [docs/agent-skills.md#L151-L161](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L151-L161)
  - [observation/documented] Skills are discovered from many locations with later sources taking precedence, including built-in dist skills, Codex, Claude, shared agent directories, Autohand user/project dirs, and extension contributions. -- evidence: [docs/agent-skills.md#L107-L107](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L107-L107), [docs/agent-skills.md#L109-L123](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L109-L123)
- interfaces (4 claim(s)):
  - [observation/documented] The product runs as a terminal REPL with file mentions, slash commands, keyboard shortcuts, provider switching, and session history available from one prompt. -- evidence: [README.md#L14-L14](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L14-L14), [README.md#L22-L28](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/README.md#L22-L28)
  - [observation/documented] Slash commands include /skills (list, use, deactivate, info, new) and /deep-research with a /deep-search alias for research runs. -- evidence: [docs/agent-skills.md#L693-L699](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L693-L699), [docs/agent-skills.md#L78-L78](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L78-L78), [docs/agent-skills.md#L38-L39](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L38-L39), [docs/agent-skills.md#L74-L76](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L74-L76)
- memory-state (2 claim(s)):
  - [observation/documented] Memory tools include save_memory, recall_memory (ranked by content, tags, recency), inspect_memory, and delete_memory which retains a canonical deletion event. -- evidence: [docs/agent-skills.md#L288-L293](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L288-L293)
  - [observation/documented] Delegated workers read up to five recent project lessons (each truncated to 1,000 chars) from the workspace's .autohand/memory; bare mode disables this, and agent.autoMemory:false disables automatic lesson saving. -- evidence: [docs/agent-skills.md#L300-L305](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L300-L305), [docs/agent-skills.md#L295-L298](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L295-L298)
- orchestration (1 claim(s)):
  - [observation/documented] The bundled deep-research skill runs multi-task research with persisted status (task progress, tool, evidence/failure counts, tokens), and a run is marked complete only after tasks finish, the report passes a source audit, and project checks pass. -- evidence: [docs/agent-skills.md#L78-L78](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L78-L78), [docs/agent-skills.md#L80-L80](https://github.com/autohandai/code-cli/blob/f4775fdebd930b7e1a624aebab7dc98fed04ca50/docs/agent-skills.md#L80-L80)
- tools-permissions (1 claim(s)):
More evidence: [full detail](code-cli.detail.md)

Metadata and full claim list: [full detail](code-cli.detail.md)
Human notes ([notes](code-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
