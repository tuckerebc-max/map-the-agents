---
access: public
aliases: []
claim_ids:
- clm_218e15edcc6f415087bcabd838011b9a0955da30cd668baed3cf0d9a3d2c1314
- clm_3c84438fa8653291dd4085852d5af5781d91abd671ab05ea36bf1d7d75e9fd45
- clm_68b0c3e344fb183685739c8b58069a1b5973ce0fa73c6093178fe77ab591ccad
- clm_706ef55e52cf12d2ef5cd096912a5e44098a56dc70a633f84ca5b821ec6acb6d
- clm_79be6ddfaadeee675fdc7effff93b4c9724d3f6ff99ae5110747602707c579b6
- clm_7be3102974ebd2a6598b9688012b82c1920d734b3286e4faa6b6716455833b9c
- clm_a8151abc510ddd17b79baa7ea2860d8d31873c749d4b43250849136ef534d861
- clm_b15ac39f424c74f9b3055310193167d06eca8b31ec65ff4491727c394c505e3f
- clm_cacefcb6fb54ab215d891f43c7fe0c78c075932c9f93bde9483b81405aa9feab
- clm_dcc2a07f58084c5a5c433d81272c1e7f82aeb1eb378c76093cf4fcad683a8d10
- clm_e3c30333f6ca868772cfa0db363aaac78e0d381ec03ab945876b97ff9e878de2
maturity: draft
page_id: pg_d31d9b0fc348533baf7e03bc7c407c0e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c248bbe947875788b7c371ab20358dfa
title: VasiHemanth/tokentelemetry/README.md @ 0d691ae343ed
updated_at: '2026-09-14T04:30:01Z'
---

# VasiHemanth/tokentelemetry/README.md @ 0d691ae343ed

<!-- rcw:begin owner=source:src_c248bbe947875788b7c371ab20358dfa block=evidence -->
- State lives in ~/.tokentelemetry/ as hand-editable JSON files (aliases, hidden projects, preferences, billing, power, VERSION), with no database; a data directory can be relocated via --data-dir or TOKENTELEMETRY_DATA_DIR. [@claim:clm_218e15edcc6f415087bcabd838011b9a0955da30cd668baed3cf0d9a3d2c1314]
- Requirements are Node.js 20.9+, Python 3.9+, git, and at least one supported AI coding agent already installed; a badge also mentions Node 18+. [@claim:clm_3c84438fa8653291dd4085852d5af5781d91abd671ab05ea36bf1d7d75e9fd45]
- TokenTelemetry is a free, open-source, 100% local observability dashboard tracking token usage, LLM costs, tool calls, session traces, and reasoning steps across AI coding agents, with no signup or cloud. [@claim:clm_68b0c3e344fb183685739c8b58069a1b5973ce0fa73c6093178fe77ab591ccad]
- Remote access is opt-in: --host 0.0.0.0 exposes the backend, a random auth token is auto-generated and printed once unless --auth-token or --insecure-no-auth is passed, and loopback clients never need the token. [@claim:clm_706ef55e52cf12d2ef5cd096912a5e44098a56dc70a633f84ca5b821ec6acb6d]
- Repository development practice: contributions follow a branch-and-PR flow (feat/ branches, conventional commit messages), and ADR-0001 requires an architecture decision record in docs/adr/ committed in the same PR as the code it describes. [@claim:clm_79be6ddfaadeee675fdc7effff93b4c9724d3f6ff99ae5110747602707c579b6]
- The Hermes dashboard plugin embeds TokenTelemetry as a tab inside Hermes's own web dashboard (port 9119 to 3000), is pure-frontend with no extra backend, and deep-links to Analytics, Projects, and All Agents pages. [@claim:clm_7be3102974ebd2a6598b9688012b82c1920d734b3286e4faa6b6716455833b9c]
- Budgets are observational by design: TokenTelemetry tracks spend against user-set limits and alerts at 80% and 100% thresholds but never blocks an agent. [@claim:clm_a8151abc510ddd17b79baa7ea2860d8d31873c749d4b43250849136ef534d861]
- Plan-limit readings come from the provider's own login data on the machine rather than being estimated from history, and the UI distinguishes provider plan ceilings from user-defined project budgets. [@claim:clm_b15ac39f424c74f9b3055310193167d06eca8b31ec65ff4491727c394c505e3f]
- Hermes support reads $HERMES_HOME (or ~/.hermes/) locally on the same host, with no remote-DB mode yet; Qoder support tracks credits rather than tokens because Qoder records none. [@claim:clm_cacefcb6fb54ab215d891f43c7fe0c78c075932c9f93bde9483b81405aa9feab]
- The project structure includes a Python FastAPI backend that reads agent logs and serves a REST API, a Next.js 16 React frontend dashboard, a cross-platform bin/cli.js launcher, and install.sh/install.ps1 installers. [@claim:clm_dcc2a07f58084c5a5c433d81272c1e7f82aeb1eb378c76093cf4fcad683a8d10]
- Unlike Langfuse, LangSmith, or Helicone, TokenTelemetry requires no code instrumentation, account, SDK, or API key — it works by reading the log files agents already write, fully locally. [@claim:clm_e3c30333f6ca868772cfa0db363aaac78e0d381ec03ab945876b97ff9e878de2]
<!-- rcw:end owner=source:src_c248bbe947875788b7c371ab20358dfa block=evidence -->

## Researcher notes

