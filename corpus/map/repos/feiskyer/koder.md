# feiskyer/koder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 55f553326039 @ 46fb8c41ea09079f

## Summary (orientation draft, not independently verified)

Selected evidence records: Koder is an experimental, open-source terminal AI coding assistant in Python (3.10+), MIT-licensed, in alpha status, combining a streaming TUI, persistent sessions, goals, scheduled loops, skills, MCP, sandbox-aware permissions, and multi-agent workflows. The CLI supports interactive TUI mode, one-shot prompts (koder "..."), script-friendly --print output, named sessions via -s, and --resume/--continue for resuming prior work.

## Source coverage

Source coverage (partial): 6 of 16 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Koder is an experimental, open-source terminal AI coding assistant in Python (3.10+), MIT-licensed, in alpha status, combining a streaming TUI, persistent sessions, goals, scheduled loops, skills, MCP, sandbox-aware permissions, and multi-agent workflows. -- evidence: [README.md#L86-L86](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L86-L86), [README.md#L11-L11](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L11-L11), [README.md#L411-L411](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L411-L411), [README.md#L9-L9](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L9-L9)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, create a feature branch, make focused changes with tests, and open PRs; the repo uses uv for setup, black/ruff for formatting and linting, and pytest for tests (uv run pytest). -- evidence: [README.md#L348-L351](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L348-L351), [README.md#L401-L405](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L401-L405), [README.md#L341-L344](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L341-L344)
  - [observation/documented] Repository development practice: the generated command reference is regenerated and verified by maintainers via scripts/tmux_feature_scenarios.py --check, optionally with --strict-acceptance; this is doc-verification tooling, not a scored agent benchmark. -- evidence: [docs/commands.md#L131-L134](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/commands.md#L131-L134), [docs/commands.md#L129-L129](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/commands.md#L129-L129)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are local instruction bundles loaded on demand from .koder/skills/ or ~/.koder/skills/ as SKILL.md files with frontmatter including name, description, and allowed_tools; plugins can contribute skills, commands, MCP servers, channels, and dependencies. -- evidence: [README.md#L300-L300](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L300-L300), [README.md#L269-L272](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L269-L272), [README.md#L267-L267](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L267-L267), [README.md#L274-L281](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L274-L281)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI supports interactive TUI mode, one-shot prompts (koder "..."), script-friendly --print output, named sessions via -s, and --resume/--continue for resuming prior work. -- evidence: [README.md#L106-L110](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L106-L110), [README.md#L133-L147](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L133-L147), [README.md#L100-L102](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L100-L102)
  - [observation/documented] The TUI exposes a slash-command registry (79 runtime commands per the generated reference) including /status, /model, /permissions, /diff, /review, /goal, /loop, /agents, /fork, /peers, /skills, /mcp, and /sandbox. -- evidence: [README.md#L133-L147](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L133-L147), [README.md#L114-L121](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L114-L121), [docs/commands.md#L9-L11](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/commands.md#L9-L11)
- memory-state (1 claim(s)):
  - [observation/documented] Runtime state is stored locally: SQLite sessions and transcripts in ~/.koder/koder.db, goals, memories, settings, OAuth tokens under ~/.koder/tokens/, and team state under ~/.koder/ and project .koder/ paths; sessions are not uploaded to a Koder-hosted service. -- evidence: [README.md#L330-L335](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L330-L335), [README.md#L362-L366](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L362-L366), [README.md#L155-L160](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L155-L160)
- orchestration (2 claim(s)):
More evidence: [full detail](koder.detail.md)

Metadata and full claim list: [full detail](koder.detail.md)
Human notes ([notes](koder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
