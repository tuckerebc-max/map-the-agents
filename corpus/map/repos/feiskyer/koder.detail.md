# feiskyer/koder -- full detail

[Back to orientation](koder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/feiskyer/koder/55f553326039a07a811b5a68c3d78ecd3113f0fc/46fb8c41ea09079f.json](../../../wiki/dossiers/feiskyer/koder/55f553326039a07a811b5a68c3d78ecd3113f0fc/46fb8c41ea09079f.json)

## specifications (1 claim(s))

- [observation/documented] Koder is an experimental, open-source terminal AI coding assistant in Python (3.10+), MIT-licensed, in alpha status, combining a streaming TUI, persistent sessions, goals, scheduled loops, skills, MCP, sandbox-aware permissions, and multi-agent workflows. -- evidence: [README.md#L86-L86](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L86-L86), [README.md#L11-L11](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L11-L11), [README.md#L411-L411](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L411-L411), [README.md#L9-L9](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L9-L9) (`clm_56ad9bfb2a1dcc719d9de3d5a1d8c981547f4671413a0115e068193860cd0db2`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork, create a feature branch, make focused changes with tests, and open PRs; the repo uses uv for setup, black/ruff for formatting and linting, and pytest for tests (uv run pytest). -- evidence: [README.md#L348-L351](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L348-L351), [README.md#L401-L405](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L401-L405), [README.md#L341-L344](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L341-L344) (`clm_7f720e9d62c2316f1468d04f2b8b01ae522168dba020dcfbc93e44038b09d912`)
- [observation/documented] Repository development practice: the generated command reference is regenerated and verified by maintainers via scripts/tmux_feature_scenarios.py --check, optionally with --strict-acceptance; this is doc-verification tooling, not a scored agent benchmark. -- evidence: [docs/commands.md#L131-L134](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/commands.md#L131-L134), [docs/commands.md#L129-L129](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/commands.md#L129-L129) (`clm_754f80e4ec207d0d08592b539a3bbf32f4c8dd0b973f521d37500b769909f038`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are local instruction bundles loaded on demand from .koder/skills/ or ~/.koder/skills/ as SKILL.md files with frontmatter including name, description, and allowed_tools; plugins can contribute skills, commands, MCP servers, channels, and dependencies. -- evidence: [README.md#L300-L300](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L300-L300), [README.md#L269-L272](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L269-L272), [README.md#L267-L267](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L267-L267), [README.md#L274-L281](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L274-L281) (`clm_882cd4d50867a2d64e0bcd1ae50a6765a1db83508846c15337bfea581ac7da53`)

## interfaces (2 claim(s))

- [observation/documented] The CLI supports interactive TUI mode, one-shot prompts (koder "..."), script-friendly --print output, named sessions via -s, and --resume/--continue for resuming prior work. -- evidence: [README.md#L106-L110](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L106-L110), [README.md#L133-L147](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L133-L147), [README.md#L100-L102](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L100-L102) (`clm_7a82cba2f97ded2812781d3f25c70c0cea832429ec658504a877456530160630`)
- [observation/documented] The TUI exposes a slash-command registry (79 runtime commands per the generated reference) including /status, /model, /permissions, /diff, /review, /goal, /loop, /agents, /fork, /peers, /skills, /mcp, and /sandbox. -- evidence: [README.md#L133-L147](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L133-L147), [README.md#L114-L121](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L114-L121), [docs/commands.md#L9-L11](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/commands.md#L9-L11) (`clm_7d26ccba856793d4d1f0e75f5dee36f70760ccd5fcc514be5072965339712970`)

## memory-state (1 claim(s))

- [observation/documented] Runtime state is stored locally: SQLite sessions and transcripts in ~/.koder/koder.db, goals, memories, settings, OAuth tokens under ~/.koder/tokens/, and team state under ~/.koder/ and project .koder/ paths; sessions are not uploaded to a Koder-hosted service. -- evidence: [README.md#L330-L335](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L330-L335), [README.md#L362-L366](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L362-L366), [README.md#L155-L160](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L155-L160) (`clm_d010d5caed9876e94fa8ebafbe7a96df4c2c6c188c37f76c536eb4268dd038a4`)

## orchestration (2 claim(s))

- [observation/documented] Koder supports background subagents via /fork and task_delegate with isolated default context, plus local teams via /peers with mailbox routing, task records, and team memory; teammates run in-process (default) or in tmux panes. -- evidence: [docs/agents-and-teams.md#L36-L36](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/agents-and-teams.md#L36-L36), [docs/agents-and-teams.md#L60-L67](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/agents-and-teams.md#L60-L67), [docs/agents-and-teams.md#L69-L69](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/agents-and-teams.md#L69-L69), [docs/agents-and-teams.md#L75-L78](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/agents-and-teams.md#L75-L78), [docs/agents-and-teams.md#L44-L44](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/agents-and-teams.md#L44-L44) (`clm_2387c9da7ef7a5914910e8d0c01e00943c2cbc4a3aa2ae4493cf9949d38d593a`)
- [observation/documented] Agents with isolation: worktree frontmatter run in their own git worktree under .koder/worktrees/; empty worktrees are auto-removed and ones with uncommitted work are kept, with SubagentStart/Stop and WorktreeCreate/Remove hook events. -- evidence: [docs/agents-and-teams.md#L40-L40](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/agents-and-teams.md#L40-L40) (`clm_d2ca4f0502aeaff82bcc5cbed1c85b86a3ce0b5b710717b7df24e017e49142c7`)

## tools-permissions (2 claim(s))

- [observation/documented] Permission rules live in settings files under permissions.allow/deny as tool_name(content) strings with deny winning over allow; KODER_ENFORCE_TOOL_APPROVAL controls approval-required tool calls, failing closed when non-interactive by default. -- evidence: [README.md#L183-L193](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/README.md#L183-L193), [docs/configuration.md#L128-L128](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/configuration.md#L128-L128) (`clm_4d8bc7825855389170daecb49ea3b693b282ab114288602de290d30e2eb73f6e`)
- [observation/documented] An optional local managed policy file ~/.koder/managed-settings.json can define high-priority hook settings and sandbox policy keys (enabled, mode, backend, autoAllowBashIfSandboxed); no hosted managed-settings service is fetched. -- evidence: [docs/configuration.md#L152-L152](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/configuration.md#L152-L152), [docs/configuration.md#L145-L145](https://github.com/feiskyer/koder/blob/55f553326039a07a811b5a68c3d78ecd3113f0fc/docs/configuration.md#L145-L145) (`clm_9b91732c095465e78c07c8bfc395c9576fccb738fddb1e5a0f64e9f67db71edd`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

