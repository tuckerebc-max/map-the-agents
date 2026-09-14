# fivetaku/kkirikkiri -- full detail

[Back to orientation](kkirikkiri.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fivetaku/kkirikkiri/99df0f40feb6011b62094677b86260acc9fbb575/93071784013c9844.json](../../../wiki/dossiers/fivetaku/kkirikkiri/99df0f40feb6011b62094677b86260acc9fbb575/93071784013c9844.json)

## specifications (1 claim(s))

- [observation/documented] kkirikkiri is a Claude Code plugin that takes a plain-language goal, asks only for missing decisions, scans the environment, and runs an approved agent team or Workflow. -- evidence: [README.md#L9-L9](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L9-L9), [README.md#L11-L11](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L11-L11) (`clm_95a653ba569c170b4303dfea9742f8f672457d1cd8fe96567894ebf7a9ad2632`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The validation loop runs at most two rounds by default: round 1 is the original team, round 2 an auto-judge choosing keep, full replacement, or partial swap; further rounds need explicit approval. -- evidence: [README.md#L130-L134](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L130-L134) (`clm_44b3ffddb82b45d500b26d1a11689fd4d67a34338ed0d2089e69bdfea443be95`)
- [observation/documented] Five built-in presets (Research, Development, Analysis, Content, Product/PM) are matched by natural-language trigger words and serve only as starting points for the final team. -- evidence: [README.md#L105-L111](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L105-L111), [README.md#L113-L113](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L113-L113), [README.md#L103-L103](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L103-L103) (`clm_ed8461dbe64fcabfaa6586e88ce08e6a69d0f87226846da8050a5f0d430ad37e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The product is invoked via a /kkirikkiri slash command (e.g. '/kkirikkiri build me a research team') after installing from a plugin marketplace. -- evidence: [README.md#L29-L31](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L29-L31), [README.md#L46-L48](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L46-L48), [README.md#L23-L25](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L23-L25) (`clm_5eda18cb33add8db489a45a606ee3f61c21e647f33145cfd45b4449e0678fe65`)

## memory-state (1 claim(s))

- [observation/documented] Teams write session-scoped files under .kkirikkiri/teams/{team_name}/ (TEAM_PLAN.md, TEAM_PROGRESS.md, TEAM_FINDINGS.md, report.md), while saved teams persist cross-session under .kkirikkiri/shared/saved-teams/. -- evidence: [README.md#L119-L124](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L119-L124), [README.md#L117-L117](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L117-L117), [README.md#L126-L126](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L126-L126) (`clm_3f4af1bb55fb0e07df543d85bc12db5227e537ef3aa6ec865720210834dcb08d`)

## orchestration (2 claim(s))

- [observation/documented] Execution follows an eight-step pipeline: intent/preset matching, parallel environment scan, interview, team composition, user confirmation, shared-memory init, quality validation, and report collection. -- evidence: [README.md#L69-L79](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L69-L79) (`clm_8584bbe79eddc0ddec2ae35ed860cfa49f3d136d8cd9e6bedbd54cb2d0bed7bd`)
- [observation/documented] Two execution substrates are offered: a live collaborating Agent Teams mode or a deterministic Workflow pipeline for high-volume fan-out work; the user picks between them. -- evidence: [CHANGELOG.md#L205-L208](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L205-L208), [README.md#L54-L61](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L54-L61) (`clm_9a6af3e7ea044000ddd3793fdb33078ae900a109006e3725494cf3f174b4383b`)

## tools-permissions (1 claim(s))

- [observation/documented] Hook-based gates enforce write boundaries at runtime: gate-spawn blocks spawning a member whose write_scope overlaps another member's declared scope, and blocks spawns lacking tool/read-only/write_scope/stop declarations. -- evidence: [CHANGELOG.md#L33-L36](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L33-L36), [CHANGELOG.md#L57-L60](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L57-L60) (`clm_e058d91f5fab7be25fda81680cd62504d2b0ecfd1865625e730bb3c471daf567`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requires Claude Code with the CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 env flag and Node.js; tmux is optional, and external CLIs (Codex, Antigravity agy, Grok) are optional since Claude alone can run the full team. -- evidence: [README.md#L172-L183](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L172-L183), [README.md#L187-L191](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L187-L191), [README.md#L193-L193](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L193-L193) (`clm_a5186fdfe2d8d001b2c69f34b2d7fa52e1100420ca65e28d92d5c9fcc0bcf6be`)
- [inference/documented] Multi-model support appears to work by shelling out to installed external CLIs (Codex, agy, grok, gjc) with per-provider flags and model-override env vars like KKIRIKKIRI_GROK_MODEL. -- evidence: [CHANGELOG.md#L169-L174](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L169-L174), [README.md#L138-L138](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L138-L138), [CHANGELOG.md#L128-L143](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L128-L143), [README.md#L187-L191](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L187-L191) (`clm_4eb4f4f0e76508af22b9aaa7e34e3254c8c9eb3aae69a2f908f27aa336195e19`)

## limitations (2 claim(s))

- [observation/documented] The changelog explicitly notes a known limit: gates verify that write_scope declarations exist but cannot judge actual compliance without per-member output isolation, deferred to a v0.25 backlog. -- evidence: [CHANGELOG.md#L48-L50](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L48-L50) (`clm_de65a34c4bf86ee8b14d771c02e1eccc7f541c8e99f9fe10cdb225c6eaf9cbc4`)
- [observation/documented] The opt-in preparation pilot generates cards and Agent requests from one approved plan but is explicitly not a runtime permission sandbox, and no OS sandbox or write serialization for concurrent sessions is newly guaranteed. -- evidence: [CHANGELOG.md#L14-L21](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L14-L21), [README.md#L13-L13](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L13-L13) (`clm_69210465d4e48c55c184d3b0ee9154dca80b249543ef129e81d26fe77bdbce7e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

