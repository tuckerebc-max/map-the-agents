# sahil87/fab-kit -- full detail

[Back to orientation](fab-kit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sahil87/fab-kit/7284adb0be5d6af553d44e708c82568465263a18/f72bfce7b5fd26a6.json](../../../wiki/dossiers/sahil87/fab-kit/7284adb0be5d6af553d44e708c82568465263a18/f72bfce7b5fd26a6.json)

## specifications (2 claim(s))

- [observation/documented] Changes move through six stages — intake, apply, review, hydrate, ship, review-PR — each producing a persistent artifact such as intake.md, plan.md, or a PR. -- evidence: [README.md#L7-L7](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L7-L7), [README.md#L61-L68](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L61-L68) (`clm_0852a708a82e799d75b8b53357e3e9244057a3aeddb502cc1767c6c0e5d9db26`)
- [observation/documented] Each change is a self-contained folder under fab/changes/ holding intake.md, plan.md, and a .status.yaml state file symlinked at the repo root while active. -- evidence: [README.md#L76-L81](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L76-L81) (`clm_1418936003b7402fbaea4fad7dc2ca76f7f9b53bc31b6be9293333782b6dddf4`)

## components (1 claim(s))

- [observation/documented] The kit includes the fab CLI router (init/upgrade-repo/sync), companion tools wt for worktrees and idea for backlogs, and batch orchestration for parallel AI agents. -- evidence: [README.md#L7-L7](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L7-L7), [README.md#L105-L112](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L105-L112) (`clm_b73a8aefd5af57902af462ea84f8dec69c6cbc41d3db0cb129a664148c824656`)

## design-choices (3 claim(s))

- [observation/documented] Prompts are plain markdown with no SDK and no vendor lock-in, and the kit works with Claude Code, Codex, Cursor, and Windsurf. -- evidence: [README.md#L7-L7](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L7-L7) (`clm_d8fe5c5d69d80af81c5d5b8b400e80ec12a62ace0a99e2a33112194ed53f5ee6`)
- [observation/documented] A project constitution (fab/project/constitution.md) with MUST/SHOULD/MUST NOT rules is checked by every plan and review; it and config.yaml are the only required of five config files. -- evidence: [README.md#L397-L397](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L397-L397), [README.md#L369-L371](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L369-L371) (`clm_13d27fff53dadd589d4f5f4b8f4c86253ba2bdbd1eadde69e844e5477ea02bf7`)
- [observation/documented] SRAD is a four-dimension framework (signal strength, reversibility, agent competence, disambiguation type) whose grades aggregate into a confidence score gating /fab-ff and blocking when ambiguity is too high. -- evidence: [README.md#L414-L414](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L414-L414), [README.md#L407-L412](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L407-L412), [README.md#L403-L403](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L403-L403), [README.md#L401-L401](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L401-L401) (`clm_ed93e5eaa55d0cd8b4a97a78c1ac155cd7c5247dcc9d9ebdb6bf22ffe91f2bd3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building Fab Kit from source requires Go for the binaries under src/go/ and the just task runner for build, test, and release recipes. -- evidence: [README.md#L122-L125](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L122-L125) (`clm_1ad29eb2ba8434bb3b7728baef654fc2167c3519cfdd74145eddf19c6d85673e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Skills are slash commands typed into an AI agent's chat (/fab-* in Claude Code, $fab-* in Codex), not terminal commands; each command runs one pipeline stage. -- evidence: [README.md#L418-L418](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L418-L418), [README.md#L229-L229](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L229-L229), [README.md#L235-L235](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L235-L235) (`clm_80e5973d6b733cb47f7412fa13e7dfc7a10405c73bb893f3f9ef226847c1065c`)
- [observation/documented] The fab CLI exposes subcommands including sync, config show/explain/set, doctor, operator, and batch new/switch/archive for worktree tab management. -- evidence: [README.md#L478-L489](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L478-L489) (`clm_78fda2114021aed6726dbbba196c7d2bcf602c814db2b44a1a29b54444c01bc2`)

## memory-state (1 claim(s))

- [observation/documented] Learnings from each change are saved into docs/memory/, a domain-organized knowledge base committed to git and shared across the team; /docs-hydrate-memory can bootstrap it from Notion, Linear, or local files. -- evidence: [README.md#L333-L333](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L333-L333), [README.md#L346-L349](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L346-L349) (`clm_7ad5a63812c3c12754b006072eea62801b84b33b303d80a2ef13d994990f42d8`)

## orchestration (3 claim(s))

- [observation/documented] Parallelism relies on git worktree isolation: wt create makes an isolated worktree, fab sync runs automatically in each new worktree, and self-contained change folders avoid shared state. -- evidence: [README.md#L265-L265](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L265-L265), [README.md#L223-L223](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L223-L223), [README.md#L327-L329](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L327-L329) (`clm_15a6ef3e94dce14f16c0524da32c09e1efb37d09c9f528d283ad64371e1815cf`)
- [observation/documented] The optional /fab-operator skill is a long-running coordination layer in its own tmux pane that monitors and directs agents across panes, with auto-answering and dependency-aware spawning. -- evidence: [README.md#L470-L472](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L470-L472), [README.md#L468-L468](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L468-L468) (`clm_c7177dac9c6b1022068cdd189f2dacd30ed120c96ac5b637d48463618506bb11`)
- [observation/documented] Review runs in a separate sub-agent context; /fab-ff and /fab-fff auto-loop between apply and review up to 3 cycles, fixing issues before escalating to the user. -- evidence: [README.md#L72-L72](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L72-L72), [README.md#L381-L381](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L381-L381) (`clm_65e4713477d443c6eda2aca577c9c893cee97f7c266e8b4518a6562e64323f18`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies include yq (YAML for status files), jq (JSON for settings merge during sync), gh (releases and PR workflows), and direnv (workspace env vars), installable via brew. -- evidence: [README.md#L91-L93](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L91-L93), [README.md#L105-L112](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L105-L112) (`clm_f2b384b9e7dc8f1cdbb92b094e188b92fcfd5c4b302c0b91778e298fb8c6b7fd`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

