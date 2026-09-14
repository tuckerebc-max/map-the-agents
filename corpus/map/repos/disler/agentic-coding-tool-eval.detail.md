# disler/agentic-coding-tool-eval -- full detail

[Back to orientation](agentic-coding-tool-eval.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/disler/agentic-coding-tool-eval/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/3b49b69f2d8e9a42.json](../../../wiki/dossiers/disler/agentic-coding-tool-eval/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/3b49b69f2d8e9a42.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Setup uses Claude Code to run a custom slash command /trees with tool names like claude_code,gemini_cli to create git worktrees. -- evidence: [README.md#L10-L10](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L10-L10) (`clm_f5a7455bafb4e5a1251f0cd39d472372e1557414f0cd16ac33d0a45a65772cd3`)
- [observation/documented] Stated requirements are Claude Code (or manual git worktree setup), Git, a bun/npm/yarn/pnpm package manager, and a .env copied from .env.sample. -- evidence: [README.md#L14-L17](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L14-L17) (`clm_dbd78977816da1d4ae475df719fdf71e423ae378a227922589d0622f8bcbb795`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The evaluated tools are run in permissionless mode; the README warns about this explicitly. -- evidence: [README.md#L22-L24](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L22-L24) (`clm_5f7fac188bddb460e8cd013022694227ad9392a0f98060760b8f592a20add196`)
- [observation/documented] Documented invocations include claude --dangerously-skip-permissions, gemini --yolo, and codex --dangerously-auto-approve-everything. -- evidence: [README.md#L26-L26](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L26-L26), [README.md#L30-L30](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L30-L30), [README.md#L28-L28](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L28-L28) (`clm_b8b4c53727a9f762c4ccf95425b9f3f8b21b992437e6b7060701e8fde78cd664`)

## evaluation (2 claim(s))

- [observation/documented] The repository provides micro apps intended to compare and evaluate agentic coding tools in a hands-on way. -- evidence: [README.md#L2-L2](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L2-L2) (`clm_943d1be51bd95cddac51df9c188b9134130b7248d01d611aa153e77ee694e8b6`)
- [observation/documented] One evaluation app, apps/ui_component_eval, tests which agentic coding tool can follow its prompts and build the best UI component. -- evidence: [README.md#L6-L6](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L6-L6) (`clm_cc036dae03cd4053d27b9efa3a2e74a39893e1a7195ee999c66bba73d130b2f4`)

## dependencies (1 claim(s))

- [observation/documented] The README links to the evaluated tools' documentation: Claude Code docs, the gemini-cli GitHub repo, and the OpenAI codex repo. -- evidence: [README.md#L26-L26](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L26-L26), [README.md#L30-L30](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L30-L30), [README.md#L28-L28](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L28-L28) (`clm_781fd6831d01c65f30ad76385d3b29c7708a4efe7a3b27de5858738fd09bab78`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The repo is aimed at developers wanting to benchmark AI coding assistants side by side, and links to related AI-coding educational resources. -- evidence: [README.md#L35-L35](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L35-L35), [README.md#L33-L33](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L33-L33) (`clm_c5cd795d3b75d336ea38e0eefa16b3996ccd4a1376f8231a2cb9d1941ff8ee33`)

