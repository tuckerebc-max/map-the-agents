# kingbootoshi/rgr -- full detail

[Back to orientation](rgr.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kingbootoshi/rgr/45ffc907a54b0e4d69424c7caa5f88ddff558f37/608a715aaa98a9c8.json](../../../wiki/dossiers/kingbootoshi/rgr/45ffc907a54b0e4d69424c7caa5f88ddff558f37/608a715aaa98a9c8.json)

## specifications (1 claim(s))

- [observation/documented] rgr is described as a no-dependency Red-Green-Refactor gate for coding agents that records the failing test first, freezes it with hashes and snapshots, and refuses Green or Refactor if the Red test was edited. -- evidence: [README.md#L5-L5](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L5-L5) (`clm_97b577b99e2bb8835a5a8995c6b359c688078e46abc77cc1812284ddc3da761e`)

## components (2 claim(s))

- [observation/documented] The intent-lock feature adds core files intent.ts, scope-audit.ts, glob.ts, and stable-json.ts, with the scope audit composed inside verifyCommand rather than as a standalone authoritative command. -- evidence: [docs/prds/intent-lock-scope-audit.intent-boundary.md#L117-L117](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L117-L117), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L34-L42](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L34-L42), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L24-L31](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L24-L31) (`clm_5eb3e72825e6d10306645adce4fe2a85f1652ff8629bac52644c047ab29854c1`)
- [observation/documented] RGR ships two skills as Claude Code and Codex plugins: the rgr skill and intent-contract, which compiles a signed Locked Intent Boundary into an IntentLock that `rgr verify --intent-lock` enforces. -- evidence: [README.md#L40-L40](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L40-L40), [README.md#L42-L43](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L42-L43) (`clm_9ef1c58777b257877c2dc78e4c15b46fdc9430f6dfe0373fd4e4456f4fdc7cd5`)

## design-choices (1 claim(s))

- [observation/documented] Enforcement rules include: Red must fail, Red defaults to test-surface changes only, protected Red files are hashed with SHA-256 and snapshotted, Green runs the exact Red command, and strict Red protects imported helpers, fixtures, snapshots, test config, and lockfiles. -- evidence: [README.md#L116-L131](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L116-L131) (`clm_41f7efe1058853cd503512261dc36bb04e738500a18948ce51c8de77d7bd92c7`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to write the failing test first, capture Red via `bun run rgr -- red --strict`, change production code only after Red, then run green, refactor, and `verify --ci --replay` before handoff, and to use `rgr revise-test` rather than editing protected Red tests. -- evidence: [AGENTS.md#L3-L3](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L3-L3), [AGENTS.md#L14-L14](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L14-L14), [AGENTS.md#L5-L5](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L5-L5), [AGENTS.md#L7-L12](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L7-L12) (`clm_4702a081ce6d335ccf9e4fd376328f52de026ad8c3153c8871fb4bcd6abdecd1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes subcommands including init, red, green, refactor, verify, revise-test, status, doctor, inspect-test, prompt, and lock-intent, invoked via Bun with flags like --goal-id, --test, --protect, --ci, --replay. -- evidence: [docs/TEST-DISCIPLINE.md#L28-L31](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/TEST-DISCIPLINE.md#L28-L31), [README.md#L96-L96](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L96-L96), [README.md#L147-L149](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L147-L149), [README.md#L93-L93](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L93-L93), [README.md#L99-L100](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L99-L100), [README.md#L87-L87](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L87-L87), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L45-L51](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L45-L51), [README.md#L84-L84](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L84-L84) (`clm_a3013de4a7d0fb3024bd1409eaf0ad792e71886313a4c78780bbaceb97627f58`)
- [observation/documented] Every command proof uses the argv after the -- separator, and per the enforcement list this is currently direct `bun test` only. -- evidence: [README.md#L116-L131](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L116-L131) (`clm_4812ceee52e841b721437d7eca50668dc25ec8882b0fff47abc972b1dced1ede`)

## memory-state (1 claim(s))

- [observation/documented] Every rgr run writes .rgr/manifest.json, .rgr/events.jsonl, snapshots, diffs, and command output logs as an audit trail. -- evidence: [README.md#L102-L102](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L102-L102) (`clm_725688658c0766c43e2e7d9aa797385dcd83c7b2c82a014ca5966ae1277699a5`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] docs/EVALS.md describes deterministic Tier 1 harness checks (no model judge) that verify the production RGR proof layers reject known bad agent behaviors such as helper tampering, changed Green commands, non-bun-test proofs, and Red self-mutation. -- evidence: [docs/EVALS.md#L17-L29](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/EVALS.md#L17-L29), [docs/EVALS.md#L33-L43](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/EVALS.md#L33-L43), [docs/EVALS.md#L7-L7](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/EVALS.md#L7-L7), [docs/EVALS.md#L3-L3](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/EVALS.md#L3-L3) (`clm_7a7e15276d199b5f1029eb452432b92426960ecfc851a2600e50e27f774e2451`)

## dependencies (1 claim(s))

- [observation/documented] The project is intended to stay zero-dependency, using only Bun and node: builtins; the boundary forbids adding npm packages for glob matching, signature verification, or JSON canonicalization. -- evidence: [docs/prds/intent-lock-scope-audit.intent-boundary.md#L34-L42](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L34-L42), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L45-L51](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L45-L51), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L21-L21](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L21-L21) (`clm_9fe03ac6c24a79c2eb41f18ca165e2426c5558925e9a4b520f1ded755b3eb655`)

## limitations (1 claim(s))

- [observation/documented] The threat model states that an agent with unrestricted write access to the same repo can still delete .rgr or bypass the CLI, so local use is a discipline gate and authoritative results require running verify inside CI, sandboxes, or agent harnesses. -- evidence: [README.md#L135-L135](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L135-L135) (`clm_83cc8a355c6e7f664c9654fb2eefe1423a1bb18b787130102f44b202daf01e85`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

