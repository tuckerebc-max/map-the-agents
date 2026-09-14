---
access: public
aliases: []
claim_ids:
- clm_5f7fac188bddb460e8cd013022694227ad9392a0f98060760b8f592a20add196
- clm_781fd6831d01c65f30ad76385d3b29c7708a4efe7a3b27de5858738fd09bab78
- clm_943d1be51bd95cddac51df9c188b9134130b7248d01d611aa153e77ee694e8b6
- clm_b8b4c53727a9f762c4ccf95425b9f3f8b21b992437e6b7060701e8fde78cd664
- clm_c5cd795d3b75d336ea38e0eefa16b3996ccd4a1376f8231a2cb9d1941ff8ee33
- clm_cc036dae03cd4053d27b9efa3a2e74a39893e1a7195ee999c66bba73d130b2f4
- clm_dbd78977816da1d4ae475df719fdf71e423ae378a227922589d0622f8bcbb795
- clm_f5a7455bafb4e5a1251f0cd39d472372e1557414f0cd16ac33d0a45a65772cd3
maturity: draft
page_id: pg_1c92f76f0af55c76bfbce67558ae8713
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3259ced3441c504db8ff928f39d56c55
title: disler/agentic-coding-tool-eval/README.md @ 9580b9ccaf0f
updated_at: '2026-09-14T03:47:47Z'
---

# disler/agentic-coding-tool-eval/README.md @ 9580b9ccaf0f

<!-- rcw:begin owner=source:src_3259ced3441c504db8ff928f39d56c55 block=evidence -->
- The evaluated tools are run in permissionless mode; the README warns about this explicitly. [@claim:clm_5f7fac188bddb460e8cd013022694227ad9392a0f98060760b8f592a20add196]
- The README links to the evaluated tools' documentation: Claude Code docs, the gemini-cli GitHub repo, and the OpenAI codex repo. [@claim:clm_781fd6831d01c65f30ad76385d3b29c7708a4efe7a3b27de5858738fd09bab78]
- The repository provides micro apps intended to compare and evaluate agentic coding tools in a hands-on way. [@claim:clm_943d1be51bd95cddac51df9c188b9134130b7248d01d611aa153e77ee694e8b6]
- Documented invocations include claude --dangerously-skip-permissions, gemini --yolo, and codex --dangerously-auto-approve-everything. [@claim:clm_b8b4c53727a9f762c4ccf95425b9f3f8b21b992437e6b7060701e8fde78cd664]
- The repo is aimed at developers wanting to benchmark AI coding assistants side by side, and links to related AI-coding educational resources. [@claim:clm_c5cd795d3b75d336ea38e0eefa16b3996ccd4a1376f8231a2cb9d1941ff8ee33]
- One evaluation app, apps/ui_component_eval, tests which agentic coding tool can follow its prompts and build the best UI component. [@claim:clm_cc036dae03cd4053d27b9efa3a2e74a39893e1a7195ee999c66bba73d130b2f4]
- Stated requirements are Claude Code (or manual git worktree setup), Git, a bun/npm/yarn/pnpm package manager, and a .env copied from .env.sample. [@claim:clm_dbd78977816da1d4ae475df719fdf71e423ae378a227922589d0622f8bcbb795]
- Setup uses Claude Code to run a custom slash command /trees with tool names like claude_code,gemini_cli to create git worktrees. [@claim:clm_f5a7455bafb4e5a1251f0cd39d472372e1557414f0cd16ac33d0a45a65772cd3]
<!-- rcw:end owner=source:src_3259ced3441c504db8ff928f39d56c55 block=evidence -->

## Researcher notes

