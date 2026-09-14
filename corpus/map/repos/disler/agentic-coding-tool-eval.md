# disler/agentic-coding-tool-eval

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9580b9ccaf0f @ 3b49b69f2d8e9a42

## Summary (orientation draft, not independently verified)

A small repository of micro apps for hands-on comparison of agentic coding tools (Claude Code, Gemini CLI, Codex CLI), with setup instructions and a UI-component evaluation app.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Setup uses Claude Code to run a custom slash command /trees with tool names like claude_code,gemini_cli to create git worktrees. -- evidence: [README.md#L10-L10](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L10-L10)
  - [observation/documented] Stated requirements are Claude Code (or manual git worktree setup), Git, a bun/npm/yarn/pnpm package manager, and a .env copied from .env.sample. -- evidence: [README.md#L14-L17](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L14-L17)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The evaluated tools are run in permissionless mode; the README warns about this explicitly. -- evidence: [README.md#L22-L24](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L22-L24)
  - [observation/documented] Documented invocations include claude --dangerously-skip-permissions, gemini --yolo, and codex --dangerously-auto-approve-everything. -- evidence: [README.md#L26-L26](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L26-L26), [README.md#L30-L30](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L30-L30), [README.md#L28-L28](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L28-L28)
- evaluation (2 claim(s)):
  - [observation/documented] The repository provides micro apps intended to compare and evaluate agentic coding tools in a hands-on way. -- evidence: [README.md#L2-L2](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L2-L2)
  - [observation/documented] One evaluation app, apps/ui_component_eval, tests which agentic coding tool can follow its prompts and build the best UI component. -- evidence: [README.md#L6-L6](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L6-L6)
- dependencies (1 claim(s)):
  - [observation/documented] The README links to the evaluated tools' documentation: Claude Code docs, the gemini-cli GitHub repo, and the OpenAI codex repo. -- evidence: [README.md#L26-L26](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L26-L26), [README.md#L30-L30](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L30-L30), [README.md#L28-L28](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L28-L28)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The repo is aimed at developers wanting to benchmark AI coding assistants side by side, and links to related AI-coding educational resources. -- evidence: [README.md#L35-L35](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L35-L35), [README.md#L33-L33](https://github.com/disler/agentic-coding-tool-eval/blob/9580b9ccaf0ffcea780d55d9d5823397b3e94a27/README.md#L33-L33)

Every claim for this repository is shown above and in [full detail](agentic-coding-tool-eval.detail.md).

Metadata and full claim list: [full detail](agentic-coding-tool-eval.detail.md)
Human notes ([notes](agentic-coding-tool-eval.notes.md), never overwritten by build)

[Back to map index](../../index.md)
