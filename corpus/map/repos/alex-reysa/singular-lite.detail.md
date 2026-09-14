# alex-reysa/singular-lite -- full detail

[Back to orientation](singular-lite.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/alex-reysa/singular-lite/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/812d525520c3a671.json](../../../wiki/dossiers/alex-reysa/singular-lite/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/812d525520c3a671.json)

## specifications (1 claim(s))

- [observation/documented] The README describes singular as a bash and Python orchestration engine that runs autonomous AI coding agents in parallel across a repository, using a three-tier scheduling model of an origin loop, area planners, and worker agents with git-worktree isolation. -- evidence: [README.md#L7-L12](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L7-L12) (`clm_a58e8eaee8334719b99217a3f63915e68acb3b095d8746994191b068438f4ff4`)

## components (1 claim(s))

- [observation/documented] An agent-tiers table documents three roles: an L0 origin scheduler that runs the reconcile cycle, L1 area planners that stage batches of tasks per DAG node, and L2 workers that execute one task per isolated git worktree and produce a state packet for review. -- evidence: [README.md#L18-L22](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L18-L22) (`clm_4eeed67f2b747bac91d8ab0a57bb28e67e2edfd15908980909e8616f9f87b322`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are asked to run the test script before opening a PR, keep the generic engine free of project-specific rules, and avoid committing state, worktree, or evidence directories. -- evidence: [CONTRIBUTING.md#L7-L15](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/CONTRIBUTING.md#L7-L15) (`clm_7fcd57f05cd9cd2874b44dcf4b3bd1cabcc389aa190f52d0c7eb875293528279`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Each reconcile cycle is documented as five ordered steps: importing staged task proposals, recovering stale leases, integrating completed worker branches, dispatching new tasks, and writing a state snapshot. -- evidence: [README.md#L28-L32](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L28-L32) (`clm_b4a00f426526a8ad4e7518f64e7bcd209f3c74ae5849c63fb03653c32557253d`)
- [observation/documented] With detached dispatch on by default, reconcile pre-leases frontier tasks and spawns each worker in its own session, returning quickly; a separate reaper process later attributes completions, failures, and crashes from dispatch records and worker exit files. -- evidence: [README.md#L83-L89](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L83-L89) (`clm_e346a1d4a0395511577bc30bac2c041e19115129e06445354f0e46abfd4b2992`)

## tools-permissions (2 claim(s))

- [observation/documented] After each worker run, a configured gate command's result feeds an auditor model, and a decider maps the failure class and remaining retries to a recovery action - retry, amend-scope, escalate, or park - via a deterministic table before any model round-trip. -- evidence: [README.md#L43-L47](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L43-L47) (`clm_63470019199fb459e94688778d2d5cf473a165a29b46244bd1c6483577bf18ab`)
- [observation/documented] The docs state an independence pin that always runs final-audit, paired-audit, re-critique, and critic-recheck fresh, regardless of session-routing settings, so no configuration lets an auditor grade work from a session that already formed an opinion on it. -- evidence: [README.md#L380-L386](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L380-L386) (`clm_978e141d0d07d924837d6d0a5c2b86cf3fa1ab82d255df2f1798a70065814dd7`)

## evaluation (1 claim(s))

- [observation/documented] Documentation states that gates and audit checks stay identical across every session-routing strategy, and that any outcome improvement from session continuity is measured rather than assumed, via per-strategy results recorded in an attempts index and a metrics command. -- evidence: [README.md#L464-L469](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L464-L469) (`clm_80ba83c198dd12aa94258ead07f7ab11e1776146ccdf5106a1007bd3327c6a49`)

## dependencies (1 claim(s))

- [observation/documented] Documented install prerequisites are Bash 4+, Python 3, Git, and one supported runner CLI on PATH; the shipped runner adapters listed are for codex, claude, gemini, opencode, cursor, openrouter, and grok. -- evidence: [README.md#L101-L119](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/README.md#L101-L119) (`clm_e46f7d6556cc28f2fb3c5fb8ffa73055e5e8b853e388f56dd02376d78ba6fdbf`)

## limitations (1 claim(s))

- [observation/documented] The security policy states the engine runs repo-configured shell commands and launches local coding agents inside git worktrees, and asks users to treat a repo's config files, task files, and opt-in modules as executable trust boundaries. -- evidence: [SECURITY.md#L3-L5](https://github.com/alex-reysa/singular-lite/blob/0f92cba1fb1f2b51d6762b493b0ac7aaded8fdd9/SECURITY.md#L3-L5) (`clm_72a5c1f6161a02fb914114032d783e87ddf185a20f86df2b680f80bfe2296d68`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

