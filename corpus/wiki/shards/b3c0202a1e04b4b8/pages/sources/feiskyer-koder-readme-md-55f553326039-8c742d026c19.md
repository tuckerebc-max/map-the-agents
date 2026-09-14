---
access: public
aliases: []
claim_ids:
- clm_4d8bc7825855389170daecb49ea3b693b282ab114288602de290d30e2eb73f6e
- clm_56ad9bfb2a1dcc719d9de3d5a1d8c981547f4671413a0115e068193860cd0db2
- clm_7a82cba2f97ded2812781d3f25c70c0cea832429ec658504a877456530160630
- clm_7d26ccba856793d4d1f0e75f5dee36f70760ccd5fcc514be5072965339712970
- clm_7f720e9d62c2316f1468d04f2b8b01ae522168dba020dcfbc93e44038b09d912
- clm_882cd4d50867a2d64e0bcd1ae50a6765a1db83508846c15337bfea581ac7da53
- clm_d010d5caed9876e94fa8ebafbe7a96df4c2c6c188c37f76c536eb4268dd038a4
maturity: draft
page_id: pg_f2f50cededa85d408b418c742d026c19
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_644c2f113f7c534da6521882167388c1
title: feiskyer/koder/README.md @ 55f553326039
updated_at: '2026-09-14T02:01:03Z'
---

# feiskyer/koder/README.md @ 55f553326039

<!-- rcw:begin owner=source:src_644c2f113f7c534da6521882167388c1 block=evidence -->
- Permission rules live in settings files under permissions.allow/deny as tool_name(content) strings with deny winning over allow; KODER_ENFORCE_TOOL_APPROVAL controls approval-required tool calls, failing closed when non-interactive by default. [@claim:clm_4d8bc7825855389170daecb49ea3b693b282ab114288602de290d30e2eb73f6e]
- Koder is an experimental, open-source terminal AI coding assistant in Python (3.10+), MIT-licensed, in alpha status, combining a streaming TUI, persistent sessions, goals, scheduled loops, skills, MCP, sandbox-aware permissions, and multi-agent workflows. [@claim:clm_56ad9bfb2a1dcc719d9de3d5a1d8c981547f4671413a0115e068193860cd0db2]
- The CLI supports interactive TUI mode, one-shot prompts (koder "..."), script-friendly --print output, named sessions via -s, and --resume/--continue for resuming prior work. [@claim:clm_7a82cba2f97ded2812781d3f25c70c0cea832429ec658504a877456530160630]
- The TUI exposes a slash-command registry (79 runtime commands per the generated reference) including /status, /model, /permissions, /diff, /review, /goal, /loop, /agents, /fork, /peers, /skills, /mcp, and /sandbox. [@claim:clm_7d26ccba856793d4d1f0e75f5dee36f70760ccd5fcc514be5072965339712970]
- Repository development practice: contributors fork, create a feature branch, make focused changes with tests, and open PRs; the repo uses uv for setup, black/ruff for formatting and linting, and pytest for tests (uv run pytest). [@claim:clm_7f720e9d62c2316f1468d04f2b8b01ae522168dba020dcfbc93e44038b09d912]
- Skills are local instruction bundles loaded on demand from .koder/skills/ or ~/.koder/skills/ as SKILL.md files with frontmatter including name, description, and allowed_tools; plugins can contribute skills, commands, MCP servers, channels, and dependencies. [@claim:clm_882cd4d50867a2d64e0bcd1ae50a6765a1db83508846c15337bfea581ac7da53]
- Runtime state is stored locally: SQLite sessions and transcripts in ~/.koder/koder.db, goals, memories, settings, OAuth tokens under ~/.koder/tokens/, and team state under ~/.koder/ and project .koder/ paths; sessions are not uploaded to a Koder-hosted service. [@claim:clm_d010d5caed9876e94fa8ebafbe7a96df4c2c6c188c37f76c536eb4268dd038a4]
<!-- rcw:end owner=source:src_644c2f113f7c534da6521882167388c1 block=evidence -->

## Researcher notes

