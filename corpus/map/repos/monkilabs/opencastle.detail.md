# monkilabs/opencastle -- full detail

[Back to orientation](opencastle.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/monkilabs/opencastle/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/cc0f087fa67f4abd.json](../../../wiki/dossiers/monkilabs/opencastle/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/cc0f087fa67f4abd.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] OpenCastle compiles to native formats for seven assistants including Claude Code (CLAUDE.md + .claude/), Cursor, Windsurf, Copilot, OpenCode, Codex CLI, and Antigravity. -- evidence: [README.md#L123-L131](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L123-L131) (`clm_1b6c4432a08887fe775af4e489abe7784f67862803984f8619bb03f3cbb1d6a1`)
- [observation/documented] Compiled content includes 13 role agent definitions, 31 domain skills plus 31 tool integrations loaded on demand, and 9 workflow templates. -- evidence: [README.md#L141-L142](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L141-L142), [README.md#L148-L149](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L148-L149), [README.md#L144-L146](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L144-L146) (`clm_dead6bf90aa07ecb23999bdcb3c7b6c3b293328c0ebd95424b1caad7bcd87a55`)

## design-choices (1 claim(s))

- [observation/documented] Agents declare capability tiers (premium, standard, economy) instead of pinned model names, letting the user's assistant choose the concrete model. -- evidence: [README.md#L154-L156](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L154-L156) (`clm_584ee797f3939285b5986aae939f25e1f2fdb047238c147329618fee438e7c7c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork, branch as feat/ or fix/, ensure npm test and npx tsc --noEmit pass, then open a PR. -- evidence: [README.md#L189-L192](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L189-L192) (`clm_b8a7094ff45ebec4632a0dd0a5df899f48cb6f39f7255566681555aa18fd81fd`)
- [observation/documented] Repository development practice: a CI workflow runs 'npx opencastle sync --check' on Node 22, and generated config is committed like a lockfile so the check has something to compare. -- evidence: [README.md#L105-L108](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L105-L108), [README.md#L110-L112](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L110-L112) (`clm_e13e8a900c50387938ff469bd2ae46ea7162b5227c5fef98936fdda51e8a31b0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands including bare status, sync (with --check for CI drift detection), add, and doctor, per the README's everyday-use examples. -- evidence: [README.md#L72-L78](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L72-L78) (`clm_5d839887db4c8d4b2bb40284b08faddf7c32e5658f394de783d53eac5733efde`)
- [observation/documented] Running opencastle with no arguments reports installed targets, sync/drift state per assistant, and suggests the next command such as running sync. -- evidence: [README.md#L91-L93](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L91-L93), [README.md#L86-L89](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L86-L89), [README.md#L80-L81](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L80-L81) (`clm_18aedf9b60a07a8dfecd3d4bb8198ed4979070f0f82189706ba445cbe11518e0`)
- [observation/documented] The init command scans the repository for existing assistant config, framework, database, and test runner, then shows findings and asks a single confirmation. -- evidence: [README.md#L60-L61](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L60-L61), [README.md#L40-L42](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L40-L42), [README.md#L44-L46](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L44-L46) (`clm_d4cfc6dea62942ca25475b8609e3485a6fb97daef9e1379fa1dc2d6d6118399a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The experimental convoy engine runs long tasks in dependency order across isolated git worktrees with SQLite persistence so crashes resume rather than restart. -- evidence: [README.md#L162-L164](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L162-L164), [README.md#L175-L176](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L175-L176) (`clm_10aa696aa08f7227c6c28225dced3c7ed40b84bcfbfbc7f935cdf032f2c008b0`)
- [observation/documented] Convoy is invoked via 'opencastle convoy "<task>"', with bare convoy showing run state and 'convoy resume' continuing after interruption. -- evidence: [README.md#L166-L170](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L166-L170) (`clm_151850951726e5b919a3bba97b8d0bbcc2ee7e654e666a2c109694cb2a52f81a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] A proposed split plan indicates the post-split OpenCastle product would have zero runtime dependencies, while Convoy would depend on the Copilot SDK, valibot, yaml, and node:sqlite. -- evidence: [docs/plans/2026-07-27-convoy-split-plan.md#L12-L17](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/docs/plans/2026-07-27-convoy-split-plan.md#L12-L17) (`clm_b6bebd0c4ddf4db21dd2dc5aae8b6717cebdf33196940f6d26ed14187e119e37`)

## limitations (1 claim(s))

- [observation/documented] The convoy engine is explicitly labeled experimental and may change; the compiler does not depend on it. -- evidence: [README.md#L175-L176](https://github.com/monkilabs/opencastle/blob/f297837635b1a108c6f732bbc0cb1e5d5cbd30f7/README.md#L175-L176) (`clm_54f42e89394cfa61fd2e6f98dc5deffb1a467d9edd73c0a0124e57e391d39333`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

