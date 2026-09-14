# clawplays/ospec -- full detail

[Back to orientation](ospec.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/clawplays/ospec/be449f2ce6986c62410a34b3bd4521d2f952a19c/01de477712b27c38.json](../../../wiki/dossiers/clawplays/ospec/be449f2ce6986c62410a34b3bd4521d2f952a19c/01de477712b27c38.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] New projects initialized by `ospec init` default to a nested layout: root .skillrc and README.md with OSpec-managed files under .ospec/, while CLI shorthand like changes/active/<name> still resolves to .ospec/ paths. -- evidence: [README.md#L88-L99](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L88-L99) (`clm_352968681cfa2367e1ff24d59f076e7548c600326245c2f2d57ba4a8573ecbe6`)
- [observation/documented] A user-selected Change stays a Change regardless of complexity or risk; the full goal workflow is entered via `ospec goal` or explicit opt-in, and the classic change flow has no controller layer or subagents. -- evidence: [README.md#L194-L194](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L194-L194), [README.md#L133-L133](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L133-L133) (`clm_f9c3ec2ef15297ea60f536a96ccbcaa0923de8508eaabfd7453d8a58cb313cc2`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The official npm package is @clawplays/ospec-cli and the command is `ospec`; documented subcommands include init, change, goal, verify, finalize, session, execute, loop, docs, update, and layout migrate. -- evidence: [SKILL.md#L74-L81](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/SKILL.md#L74-L81), [README.md#L200-L202](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L200-L202), [README.md#L244-L249](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L244-L249), [README.md#L240-L242](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L240-L242), [README.md#L218-L218](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L218-L218), [README.md#L24-L24](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L24-L24), [README.md#L170-L173](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L170-L173) (`clm_d48f189365599463aed619dfbad38049d7431897bc643ff0d2a2b073cbdfa4c3`)
- [observation/documented] `ospec init` accepts flags such as --summary, --tech-stack, --architecture, and --document-language (en-US, zh-CN, ja-JP, or ar) to shape generated project docs. -- evidence: [README.md#L88-L99](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L88-L99), [README.md#L79-L84](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L79-L84) (`clm_7eb22274a8eba5983d1a7aaeba23bb697b6e7b22659e0f1f69afc962f7283da8`)

## memory-state (3 claim(s))

- [observation/documented] Workflow state lives in repository artifacts: active changes hold proposal.md, tasks.md, state.json, verification.md, and review.md; goals add design.md, implementation-plan.md, task-graph.json, worker/reviewer/evidence artifacts, so later sessions can resume without replaying chat. -- evidence: [README.md#L39-L42](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L39-L42), [README.md#L309-L314](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L309-L314), [README.md#L214-L214](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L214-L214) (`clm_faf06daf426b8ad16b358bb8f5f4c1a9a59324e34f8ccb9a977d40bb97a83865`)
- [observation/documented] The chosen document language is persisted in .skillrc and reused for for-ai guidance, `ospec change`, and `ospec update`; CLI language resolution falls back through explicit flag, persisted settings, existing docs, then en-US. -- evidence: [README.md#L88-L99](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L88-L99) (`clm_b52fcbb7b99b1bc58515ceead6317cd0a3060f04f6e44ed9472e6648124d892b`)
- [observation/documented] Archiving writes an SKILL.index.json.archived_changes entry, refreshes docs/project/feature-catalog.md rows, and idempotently replaces ospec:last-change traceability comments — described as the engine's only write into human-owned documents, with comment failures warning rather than blocking. -- evidence: [SKILL.md#L56-L56](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/SKILL.md#L56-L56), [README.md#L318-L336](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L318-L336) (`clm_690d78b56edd195ea23e6842d51eb6a79d71ee900b654e926d7d9ef97ec8efca`)

## orchestration (3 claim(s))

- [observation/documented] The goal controller dispatches native subagents per harness (Codex spawn_agent with bounded waits, Claude Code background Task polling, Gemini @generalist, OpenCode @mention), with 60-second poll boundaries, heartbeats, and immediate persistence of completed children. -- evidence: [README.md#L147-L147](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L147-L147) (`clm_818b2e2423704a6aa8bc647b2f92a136fed3b61fec1f2ded9796a5e8a5d51545`)
- [observation/documented] OSpec never launches agent CLIs as a fallback; if the harness lacks native subagents, executable dispatch blocks until a supported harness reports capability, and IDE controller dispatch fails clearly. -- evidence: [README.md#L147-L147](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L147-L147), [README.md#L216-L216](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L216-L216) (`clm_421f937769a97c599bc85b33a51831b0c120f1843776a7faa2669d71c13edd98`)
- [observation/documented] Loop commands manage concurrency and recovery: `ospec loop tick` issues task/final reviews bound to the real reviewer executor, `loop configure` sets concurrency/budgets/limits, and `loop recover --force` expires only unfinished items after confirmed session or child loss. -- evidence: [README.md#L149-L149](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L149-L149), [README.md#L218-L218](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L218-L218) (`clm_a796981ee60e84ca41e06fe59ad0621945c0365da6c8af536304782ca498ffc2`)

## tools-permissions (1 claim(s))

- [observation/documented] For Claude Code, `ospec session hook --target claude --apply` installs a hook bundle under .ospec/hooks/claude merged into .claude/settings.json that announces dispatches, hard-blocks subagent dispatch while a required decision is pending, and is Claude-only and opt-in. -- evidence: [README.md#L230-L232](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L230-L232), [README.md#L224-L226](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L224-L226), [SKILL.md#L44-L44](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/SKILL.md#L44-L44), [README.md#L228-L228](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L228-L228) (`clm_187a580e443fed83d8ec8d04543aa3c66af299e604742089d6cab1ecbfe60924`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation docs require Node.js >= 18 and npm >= 8, installed globally via npm install -g @clawplays/ospec-cli, verified with ospec --version / --help. -- evidence: [docs/installation.md#L14-L16](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/docs/installation.md#L14-L16), [docs/installation.ar.md#L9-L10](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/docs/installation.ar.md#L9-L10), [docs/installation.md#L20-L23](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/docs/installation.md#L20-L23), [README.md#L46-L48](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L46-L48), [docs/installation.md#L9-L10](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/docs/installation.md#L9-L10) (`clm_535d81ac10dd42283939d67bbe8a3802c52f58a5ffef8942983908e0594184b4`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

