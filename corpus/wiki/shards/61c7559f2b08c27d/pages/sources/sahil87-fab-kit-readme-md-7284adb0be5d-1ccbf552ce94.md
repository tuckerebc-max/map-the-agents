---
access: public
aliases: []
claim_ids:
- clm_0852a708a82e799d75b8b53357e3e9244057a3aeddb502cc1767c6c0e5d9db26
- clm_13d27fff53dadd589d4f5f4b8f4c86253ba2bdbd1eadde69e844e5477ea02bf7
- clm_1418936003b7402fbaea4fad7dc2ca76f7f9b53bc31b6be9293333782b6dddf4
- clm_15a6ef3e94dce14f16c0524da32c09e1efb37d09c9f528d283ad64371e1815cf
- clm_1ad29eb2ba8434bb3b7728baef654fc2167c3519cfdd74145eddf19c6d85673e
- clm_65e4713477d443c6eda2aca577c9c893cee97f7c266e8b4518a6562e64323f18
- clm_78fda2114021aed6726dbbba196c7d2bcf602c814db2b44a1a29b54444c01bc2
- clm_7ad5a63812c3c12754b006072eea62801b84b33b303d80a2ef13d994990f42d8
- clm_80e5973d6b733cb47f7412fa13e7dfc7a10405c73bb893f3f9ef226847c1065c
- clm_b73a8aefd5af57902af462ea84f8dec69c6cbc41d3db0cb129a664148c824656
- clm_c7177dac9c6b1022068cdd189f2dacd30ed120c96ac5b637d48463618506bb11
- clm_d8fe5c5d69d80af81c5d5b8b400e80ec12a62ace0a99e2a33112194ed53f5ee6
- clm_ed93e5eaa55d0cd8b4a97a78c1ac155cd7c5247dcc9d9ebdb6bf22ffe91f2bd3
- clm_f2b384b9e7dc8f1cdbb92b094e188b92fcfd5c4b302c0b91778e298fb8c6b7fd
maturity: draft
page_id: pg_f965c038dd105c72ab6a1ccbf552ce94
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6a7d8df1744a5715b664c5f8faf23e0e
title: sahil87/fab-kit/README.md @ 7284adb0be5d
updated_at: '2026-09-14T04:19:51Z'
---

# sahil87/fab-kit/README.md @ 7284adb0be5d

<!-- rcw:begin owner=source:src_6a7d8df1744a5715b664c5f8faf23e0e block=evidence -->
- Changes move through six stages — intake, apply, review, hydrate, ship, review-PR — each producing a persistent artifact such as intake.md, plan.md, or a PR. [@claim:clm_0852a708a82e799d75b8b53357e3e9244057a3aeddb502cc1767c6c0e5d9db26]
- A project constitution (fab/project/constitution.md) with MUST/SHOULD/MUST NOT rules is checked by every plan and review; it and config.yaml are the only required of five config files. [@claim:clm_13d27fff53dadd589d4f5f4b8f4c86253ba2bdbd1eadde69e844e5477ea02bf7]
- Each change is a self-contained folder under fab/changes/ holding intake.md, plan.md, and a .status.yaml state file symlinked at the repo root while active. [@claim:clm_1418936003b7402fbaea4fad7dc2ca76f7f9b53bc31b6be9293333782b6dddf4]
- Parallelism relies on git worktree isolation: wt create makes an isolated worktree, fab sync runs automatically in each new worktree, and self-contained change folders avoid shared state. [@claim:clm_15a6ef3e94dce14f16c0524da32c09e1efb37d09c9f528d283ad64371e1815cf]
- Repository development practice: building Fab Kit from source requires Go for the binaries under src/go/ and the just task runner for build, test, and release recipes. [@claim:clm_1ad29eb2ba8434bb3b7728baef654fc2167c3519cfdd74145eddf19c6d85673e]
- Review runs in a separate sub-agent context; /fab-ff and /fab-fff auto-loop between apply and review up to 3 cycles, fixing issues before escalating to the user. [@claim:clm_65e4713477d443c6eda2aca577c9c893cee97f7c266e8b4518a6562e64323f18]
- The fab CLI exposes subcommands including sync, config show/explain/set, doctor, operator, and batch new/switch/archive for worktree tab management. [@claim:clm_78fda2114021aed6726dbbba196c7d2bcf602c814db2b44a1a29b54444c01bc2]
- Learnings from each change are saved into docs/memory/, a domain-organized knowledge base committed to git and shared across the team; /docs-hydrate-memory can bootstrap it from Notion, Linear, or local files. [@claim:clm_7ad5a63812c3c12754b006072eea62801b84b33b303d80a2ef13d994990f42d8]
- Skills are slash commands typed into an AI agent's chat (/fab-* in Claude Code, $fab-* in Codex), not terminal commands; each command runs one pipeline stage. [@claim:clm_80e5973d6b733cb47f7412fa13e7dfc7a10405c73bb893f3f9ef226847c1065c]
- The kit includes the fab CLI router (init/upgrade-repo/sync), companion tools wt for worktrees and idea for backlogs, and batch orchestration for parallel AI agents. [@claim:clm_b73a8aefd5af57902af462ea84f8dec69c6cbc41d3db0cb129a664148c824656]
- The optional /fab-operator skill is a long-running coordination layer in its own tmux pane that monitors and directs agents across panes, with auto-answering and dependency-aware spawning. [@claim:clm_c7177dac9c6b1022068cdd189f2dacd30ed120c96ac5b637d48463618506bb11]
- Prompts are plain markdown with no SDK and no vendor lock-in, and the kit works with Claude Code, Codex, Cursor, and Windsurf. [@claim:clm_d8fe5c5d69d80af81c5d5b8b400e80ec12a62ace0a99e2a33112194ed53f5ee6]
- SRAD is a four-dimension framework (signal strength, reversibility, agent competence, disambiguation type) whose grades aggregate into a confidence score gating /fab-ff and blocking when ambiguity is too high. [@claim:clm_ed93e5eaa55d0cd8b4a97a78c1ac155cd7c5247dcc9d9ebdb6bf22ffe91f2bd3]
- Runtime dependencies include yq (YAML for status files), jq (JSON for settings merge during sync), gh (releases and PR workflows), and direnv (workspace env vars), installable via brew. [@claim:clm_f2b384b9e7dc8f1cdbb92b094e188b92fcfd5c4b302c0b91778e298fb8c6b7fd]
<!-- rcw:end owner=source:src_6a7d8df1744a5715b664c5f8faf23e0e block=evidence -->

## Researcher notes

