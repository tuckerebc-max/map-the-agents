# gastownhall/gastown

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: steveyegge/gastown (github id 1117184424).
Latest snapshot: commit 649b832b7672 @ 46e632c92880ab13

## Summary (orientation draft, not independently verified)

Gas Town is a multi-agent workspace manager that orchestrates AI coding agents (Claude Code, Copilot, Codex, Gemini, etc.) via tmux, with git-backed persistent work state (Hooks, Beads), a Mayor coordinator, per-rig watchdogs, a Bors-style merge queue, and a federated Wasteland network through DoltHub. Evidence coverage: 171 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 75 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The architecture includes a Mayor AI coordinator, a Town workspace directory (e.g. ~/gt/), per-project Rigs wrapping git repositories, and Polecats (worker agents with persistent identity but ephemeral sessions). -- evidence: [README.md#L58-L58](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L58-L58), [README.md#L66-L66](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L66-L66), [README.md#L54-L54](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L54-L54), [README.md#L50-L50](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L50-L50)
- design-choices (2 claim(s)):
  - [observation/documented] A stated key design principle is loose coupling: Gas Town orchestrates agents through tmux and environment variables, without importing or linking agent libraries — integration is configuration, not compilation. -- evidence: [docs/agent-provider-integration.md#L23-L26](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L23-L26)
  - [observation/documented] Agent provider integration is tiered: Tier 0 is zero-change tmux orchestration via send-keys and capture-pane, Tier 1 is a JSON preset in agents.json, Tier 2 adds hooks, and Tier 3 is deep native API integration. -- evidence: [docs/agent-provider-integration.md#L49-L52](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L49-L52), [docs/agent-provider-integration.md#L30-L35](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L30-L35), [docs/agent-provider-integration.md#L46-L47](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/agent-provider-integration.md#L46-L47)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Bead/issue IDs use a prefix plus 5-character alphanumeric format (e.g. gt-abc12), where the prefix indicates the item's origin or rig; commands like gt sling and gt convoy accept these IDs. -- evidence: [README.md#L80-L80](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L80-L80)
  - [observation/documented] Runtime configuration is per-rig via settings/config.json with provider, command, args, and prompt_mode fields; built-in agent presets include claude, gemini, codex, kiro, cursor, auggie, amp, opencode, copilot, pi, and omp. -- evidence: [README.md#L507-L507](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L507-L507), [README.md#L458-L467](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L458-L467), [README.md#L456-L456](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L456-L456)
- memory-state (1 claim(s)):
  - [observation/documented] Agent work state persists in git worktree-based 'Hooks' storage that survives crashes and restarts, and work items are stored in the Beads ledger, a git-backed issue tracking system. -- evidence: [README.md#L7-L7](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L7-L7), [README.md#L70-L70](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L70-L70), [README.md#L78-L78](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L78-L78)
- orchestration (2 claim(s)):
  - [observation/documented] A three-tier watchdog system keeps agents healthy: per-rig Witnesses monitor polecats and trigger recovery, the Deacon runs continuous patrol cycles across rigs, and Dogs are dispatched for maintenance tasks like triage. -- evidence: [README.md#L88-L88](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L88-L88), [README.md#L633-L633](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L633-L633), [README.md#L90-L92](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L90-L92), [README.md#L637-L637](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md#L637-L637)
More evidence: [full detail](gastown.detail.md)

Metadata and full claim list: [full detail](gastown.detail.md)
Human notes ([notes](gastown.notes.md), never overwritten by build)

[Back to map index](../../index.md)
