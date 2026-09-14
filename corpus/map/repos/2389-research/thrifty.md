# 2389-research/thrifty

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit f7d6c4463c6d @ e5c1fe9c72e06cb4

## Summary (orientation draft, not independently verified)

thrifty is a Claude Code plugin (formerly 'atelier') implementing tiered delegation: a Sonnet planner writes a contract and sprints, a Haiku executor builds and self-verifies against an independently re-run gate, with a lean dispatch flow benchmarked ~64% cheaper than Opus at equal gate quality across 7 tasks.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The planner (Sonnet) writes a contract plus sprints.jsonl with one self-contained unit of work per sprint, pinning cross-sprint and genuinely ambiguous decisions so the executor never invents system-level choices. -- evidence: [README.md#L22-L32](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L22-L32), [README.md#L34-L41](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L34-L41)
- components (2 claim(s)):
  - [observation/documented] The plugin bundles six skills: thrifty and thrifty-dispatch (orchestrators), thrifty-plan (Sonnet), thrifty-brief (Sonnet, split tier), thrifty-execute (Haiku), and thrifty-check (Sonnet), with orchestrators running in-session. -- evidence: [README.md#L45-L45](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L45-L45), [README.md#L86-L93](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L86-L93)
  - [observation/documented] The lean dispatch flow uses dispatch.py to run bare claude -p calls that hard-pin every codegen sprint to Haiku regardless of the plan's tier, writing outputs to disk while the orchestrator reads only a tiny manifest. -- evidence: [README.md#L186-L193](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L186-L193)
- design-choices (1 claim(s)):
  - [observation/documented] Core philosophy: concentrate planning in a strong model and push execution to a cheap one, with a gate (tests/checklist) re-run independently rather than self-reported as the trust contract. -- evidence: [README.md#L11-L14](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L11-L14)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the project follows SemVer with the version in .claude-plugin/plugin.json as source of truth, and every release bumps it so /plugin installs pick up changes cleanly. -- evidence: [CHANGELOG.md#L3-L5](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/CHANGELOG.md#L3-L5)
  - [observation/documented] Repository development practice: contributors can hack locally by symlinking the skills directories into ~/.claude/skills/ instead of installing the plugin. -- evidence: [README.md#L59-L59](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L59-L59), [README.md#L61-L63](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L61-L63)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] thrifty installs as a Claude Code plugin via /plugin marketplace add 2389-research/thrifty and /plugin install thrifty@thrifty, triggered by phrases like 'thrifty', 'delegate this', or 'tiered build'. -- evidence: [README.md#L52-L52](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L52-L52), [README.md#L47-L50](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L47-L50)
- memory-state (1 claim(s)):
  - [observation/documented] Run artifacts (CONTRACT.md, briefs/, LEDGER.md) are written under docs/thrifty/<task-slug>/ so a run is auditable and resumable. -- evidence: [README.md#L143-L144](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L143-L144)
- orchestration (3 claim(s)):
  - [observation/documented] Verification is adaptive: runnable criteria are checked by re-running the gate at no model cost; Sonnet checkers are spent only on gate failures or assertional criteria such as prose and design quality. -- evidence: [README.md#L140-L141](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L140-L141), [README.md#L133-L138](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L133-L138)
More evidence: [full detail](thrifty.detail.md)

Metadata and full claim list: [full detail](thrifty.detail.md)
Human notes ([notes](thrifty.notes.md), never overwritten by build)

[Back to map index](../../index.md)
