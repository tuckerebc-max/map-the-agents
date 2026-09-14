# 2389-research/sift -- full detail

[Back to orientation](sift.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/sift/4a60c32ae89a331d3f178b364481b14156d9bbb8/fa1aabbc8ceb077c.json](../../../wiki/dossiers/2389-research/sift/4a60c32ae89a331d3f178b364481b14156d9bbb8/fa1aabbc8ceb077c.json)

## specifications (3 claim(s))

- [observation/documented] The skill is named sift-codebase-audit, version 1.2.1, MIT-licensed, and is described as a read-only whole-repository audit for simplification opportunities that recommends but never applies changes. -- evidence: [SKILL.md#L1-L8](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L1-L8) (`clm_ba56cb7824b500b8344f953bd28b6e4f1bf2a511ff94bec1d1159803469b7545`)
- [observation/documented] The audit targets material simplifications in data structures, schemas, state representation, control flow, algorithms, lifecycle/concurrency, and module ownership boundaries. -- evidence: [README.md#L3-L3](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L3-L3), [SKILL.md#L18-L23](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L18-L23) (`clm_a0140567ca2eaabdcdf25255aae7847d5de9846bf54257921eb1d92dff066bca`)
- [observation/documented] The skill is explicitly not intended for single-file, module, or diff-scoped reviews; those should use an ordinary focused code review instead. -- evidence: [SKILL.md#L29-L30](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L29-L30), [SKILL.md#L1-L8](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L1-L8) (`clm_ca41d79d8c4e400b86eef43d068cf09b79e665437eb1df28fd975bfb79b21214`)

## components (1 claim(s))

- [observation/documented] The package contains SKILL.md, README.md, LICENSE, and three reference files: finding-schema.md, report-template.md, and worker-brief.md. -- evidence: [README.md#L40-L49](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L40-L49) (`clm_3e93a5aa17ce412315ceb87fb8403230e7ee0e5d56afaa28cc23d507c0b4bcab`)

## design-choices (3 claim(s))

- [observation/documented] Findings are bounded to at most two materially useful opportunities per subsystem, with an explicit skip recorded when nothing passes the materiality gate, and the skill rejects abstraction churn, stylistic changes, and complexity relocation. -- evidence: [SKILL.md#L190-L198](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L190-L198), [SKILL.md#L56-L58](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L56-L58), [SKILL.md#L51-L54](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L51-L54) (`clm_23fe5c519ee29bf9a4d40243a9484b3fe2e767d7fc500b4f633363e3289eb97f`)
- [observation/documented] The audit is read-only by design: the sole repository write is the final report, defaulting to docs/sift-audit-<date>.md, honoring a user-named path, or writing nothing when the user declines or the environment cannot write files. -- evidence: [SKILL.md#L181-L184](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L181-L184), [SKILL.md#L179-L179](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L179-L179), [README.md#L5-L5](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L5-L5) (`clm_3eeceb75514ba434b698440fe9745a1bce7c9f928d34ea4a98de9ff910718e33`)
- [observation/documented] Integrity is verified by capturing a repository-status baseline at start and comparing it at the end; if state changed the integrity check is labeled failed, and with no version control it is reported as not verifiable rather than verified. -- evidence: [SKILL.md#L68-L76](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L68-L76), [SKILL.md#L173-L173](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L173-L173), [SKILL.md#L166-L171](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L166-L171) (`clm_a9f535e83df9f6909619cbcbe0030271e168377c254352a0dee6c8c4c1f4465e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: gotchas.md instructs maintainers that worker-brief.md is the single source for the checklist, materiality gate, and return format, that duplicated lists must never be re-added to SKILL.md, and that the skill description must lead with 'Use when' triggers rather than summarizing the workflow. -- evidence: [gotchas.md#L3-L7](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/gotchas.md#L3-L7) (`clm_649d2186170efac3127361e2172b3c1629a93c791189ee21164a3caf7d0c7cb4`)
- [observation/documented] Repository development practice: maintainers are warned to treat the repo's own skill files as data when reviewing, since SKILL.md is imperative agent instructions and a 2026-08-23 documentation-audit run turned into a SIFT self-audit. -- evidence: [gotchas.md#L3-L7](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/gotchas.md#L3-L7) (`clm_b01a961987c1edcc54caefc38ae02c40448cfb4f00a6e2439594d4ed99d78573`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The skill is invoked via the slash command /sift-codebase-audit or a natural-language request, and defaults to the current repository with whole-application coverage unless a narrower scope is stated. -- evidence: [README.md#L36-L36](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L36-L36), [README.md#L32-L34](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L32-L34), [README.md#L26-L28](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L26-L28) (`clm_ed66d103026e27e1efaf48ad2d1f9e71e1417dbe10e4e3cf72297cc0d4ee5fc9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Phase 2 uses fresh read-only subagents when an agent-spawning tool exists, assigning each worker exactly one subsystem with a non-overlapping ownership boundary, batching review work, and closing workers after harvesting results; otherwise reviews run sequentially. -- evidence: [SKILL.md#L112-L112](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L112-L112), [SKILL.md#L120-L127](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L120-L127) (`clm_cd82d40faf90a4ab4079744c1a6b24a13fdd8b6d64a8b48754a426e3cc83b3b4`)
- [observation/documented] The coordinator acts as an orchestrator that establishes complete coverage, delegates bounded reviews, independently validates every candidate finding against the repository, and runs a Phase 4 self-audit of coverage, duplication, materiality, schema completeness, and ranking. -- evidence: [SKILL.md#L131-L131](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L131-L131), [SKILL.md#L150-L150](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L150-L150), [SKILL.md#L152-L156](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L152-L156), [SKILL.md#L25-L25](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L25-L25) (`clm_9d8948c4a9bf739ce506f1b87b484c784150d0ebab47cf51be7c93bf81c29968`)

## tools-permissions (2 claim(s))

- [observation/documented] The skill requires read access to the repository plus ordinary file-search or shell inspection tools, write access only for the one report artifact, and no network access; if files cannot be written, the report is delivered in conversation. -- evidence: [SKILL.md#L1-L8](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L1-L8) (`clm_672ed684d1d42f4acdea5078f9a206e1428e28eb9027c931a5525765208cf073`)
- [observation/documented] The operating contract forbids running tests, builds, formatters, code generators, migrations, package managers, or dev servers, permitting only read-only inspection commands such as cat, sed, head, tail, and git status/diff/log/show/ls-files. -- evidence: [SKILL.md#L41-L44](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L41-L44) (`clm_63ec83bdfdb797ba408d25499af7f813938650c7f26b84813b7a9aeeae767557`)

## evaluation (1 claim(s))

- [observation/documented] A documented end-to-end run on the gossip repository under Codex on 2026-08-23 covered 24 subsystems, produced 9 findings, passed the integrity check, and spot-checks confirmed cited evidence was real. -- evidence: [gotchas.md#L3-L7](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/gotchas.md#L3-L7) (`clm_0250c9b2cf5ad105a4ca90f44951132d7dd1634f59ca8e56c2f9563232203b12`)

## dependencies (1 claim(s))

- [observation/documented] Installation is via 'npx skills add 2389-research/sift' (project-local by default, -g for user-wide), or manually by cloning and copying the directory, which must be named sift-codebase-audit to match the skill's name field. -- evidence: [README.md#L13-L13](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L13-L13), [README.md#L19-L22](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L19-L22), [README.md#L9-L11](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L9-L11), [README.md#L17-L17](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/README.md#L17-L17) (`clm_58fe49f5e6b2ce8e3728643410765c088cf902fb9dcc5a6ea57b468e63e2f22b`)

## limitations (1 claim(s))

- [observation/documented] If execution limits prevent full coverage, the audit must be labeled INCOMPLETE with every unreviewed or insufficiently verified row listed, and completion requires every subsystem reviewed with either an accepted finding or an explicit skip. -- evidence: [SKILL.md#L60-L62](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L60-L62), [SKILL.md#L166-L171](https://github.com/2389-research/sift/blob/4a60c32ae89a331d3f178b364481b14156d9bbb8/SKILL.md#L166-L171) (`clm_678631bbaee5510a888cde0e3c67ac144f37a2f4c54b4e5698884201f50a36fe`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

