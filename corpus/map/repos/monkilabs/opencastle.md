# monkilabs/opencastle

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f297837635b1 @ cc0f087fa67f4abd

## Summary (orientation draft, not independently verified)

OpenCastle is a CLI that compiles one AI-assistant configuration source into native formats for seven assistants, detects drift in CI, and includes an experimental convoy engine; internal plan documents describe a major refactor and a proposed split into two projects. Evidence coverage: 125 of 271 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] OpenCastle compiles to native formats for seven assistants including Claude Code (CLAUDE.md + .claude/), Cursor, Windsurf, Copilot, OpenCode, Codex CLI, and Antigravity. -- evidence: [README.md#L123-L131](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L123-L131)
  - [observation/documented] Compiled content includes 13 role agent definitions, 31 domain skills plus 31 tool integrations loaded on demand, and 9 workflow templates. -- evidence: [README.md#L141-L142](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L141-L142), [README.md#L148-L149](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L148-L149), [README.md#L144-L146](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L144-L146)
- design-choices (1 claim(s)):
  - [observation/documented] Agents declare capability tiers (premium, standard, economy) instead of pinned model names, letting the user's assistant choose the concrete model. -- evidence: [README.md#L154-L156](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L154-L156)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, branch as feat/ or fix/, ensure npm test and npx tsc --noEmit pass, then open a PR. -- evidence: [README.md#L189-L192](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L189-L192)
  - [observation/documented] Repository development practice: a CI workflow runs 'npx opencastle sync --check' on Node 22, and generated config is committed like a lockfile so the check has something to compare. -- evidence: [README.md#L105-L108](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L105-L108), [README.md#L110-L112](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L110-L112)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands including bare status, sync (with --check for CI drift detection), add, and doctor, per the README's everyday-use examples. -- evidence: [README.md#L72-L78](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L72-L78)
  - [observation/documented] Running opencastle with no arguments reports installed targets, sync/drift state per assistant, and suggests the next command such as running sync. -- evidence: [README.md#L91-L93](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L91-L93), [README.md#L86-L89](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L86-L89), [README.md#L80-L81](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L80-L81)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] The experimental convoy engine runs long tasks in dependency order across isolated git worktrees with SQLite persistence so crashes resume rather than restart. -- evidence: [README.md#L162-L164](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L162-L164), [README.md#L175-L176](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L175-L176)
  - [observation/documented] Convoy is invoked via 'opencastle convoy "<task>"', with bare convoy showing run state and 'convoy resume' continuing after interruption. -- evidence: [README.md#L166-L170](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L166-L170)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](opencastle.detail.md)

Metadata and full claim list: [full detail](opencastle.detail.md)
Human notes ([notes](opencastle.notes.md), never overwritten by build)

[Back to map index](../../index.md)
