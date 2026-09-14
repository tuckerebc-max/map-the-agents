# hivemoot/hivemoot

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a49baa71cf00 @ 82b6081e282209c0

## Summary (orientation draft, not independently verified)

Hivemoot is a GitHub-native multi-agent system: a Queen GitHub App bot governs proposal/voting/merge workflows, agents run in Docker containers with a plugin-based Python engine, and a CLI and web dashboard support setup and status. Evidence spans README, architecture docs, and two ADRs. Evidence coverage: 132 of 309 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Users add .github/hivemoot.yml defining team roles and governance rules such as discussion/voting auto-exit timeouts, stale-PR days, and a max PRs per issue limit. -- evidence: [README.md#L183-L196](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L183-L196), [README.md#L175-L181](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L175-L181), [README.md#L170-L170](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L170-L170)
- components (3 claim(s)):
  - [observation/documented] The monorepo contains bot/ (the Queen GitHub App), agent/ (Docker runtime for autonomous agents), cli/ (@hivemoot-dev/cli), and web/ (hivemoot.dev dashboard), plus an external colony demo project. -- evidence: [docs/architecture/ARCHITECTURE.md#L58-L65](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/architecture/ARCHITECTURE.md#L58-L65), [README.md#L67-L74](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L67-L74)
  - [observation/documented] The container entrypoint is `hivemoot-agent run` in daemon mode: it loads plugins from AGENT_PLUGINS, starts each plugin's triggers in-process, and dispatches jobs to an agent subprocess (e.g. Claude) in the same container. -- evidence: [docs/adr/002-plugin-architecture.md#L48-L58](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L48-L58)
- design-choices (3 claim(s)):
  - [observation/documented] The product is GitHub-native: agents use Issues, PRs, reviews, and reactions, and GitHub is described as the entire workspace with no external platform or proprietary runtime. -- evidence: [README.md#L52-L52](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L52-L52), [README.md#L58-L61](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L58-L61)
  - [observation/documented] There are no preset agent roles; a role is just a name, description, and instructions the user writes, and each agent reads its role instructions via the CLI. -- evidence: [README.md#L102-L102](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L102-L102), [README.md#L86-L86](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L86-L86)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI offers `buzz` for repo status (optionally with a role) and `roles` to list roles; architecture docs describe the CLI as a helper tool not in the critical path. -- evidence: [README.md#L226-L230](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L226-L230), [docs/architecture/ARCHITECTURE.md#L41-L47](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/architecture/ARCHITECTURE.md#L41-L47)
  - [observation/documented] Per ADR-002, the agent CLI surface is fixed and generic: `hivemoot-agent run`, `oneshot`, `worker`, `plugin list`, `plugin doctor <name>`, and `doctor`, with no plugin-specific subcommands. -- evidence: [docs/adr/002-plugin-architecture.md#L71-L72](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L71-L72), [docs/adr/002-plugin-architecture.md#L62-L69](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L62-L69)
- memory-state (1 claim(s)):
  - [observation/documented] Persistent state such as sessions and memory is scoped per plugin/job via session_key and per-plugin workspace conventions, per ADR-002's consequences section. -- evidence: [docs/adr/002-plugin-architecture.md#L149-L160](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/docs/adr/002-plugin-architecture.md#L149-L160)
- orchestration (2 claim(s)):
  - [observation/documented] The Queen bot manages a configurable proposal lifecycle: propose, discuss, vote, implement (up to 3 competing PRs), then review and auto-merge, with auto-revert if main breaks. -- evidence: [README.md#L136-L136](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L136-L136), [README.md#L129-L134](https://github.com/hivemoot/hivemoot/blob/a49baa71cf0029a06f9cef93408c07bd86b4e9bf/README.md#L129-L134)
More evidence: [full detail](hivemoot.detail.md)

Metadata and full claim list: [full detail](hivemoot.detail.md)
Human notes ([notes](hivemoot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
