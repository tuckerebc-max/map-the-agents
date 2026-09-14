---
access: public
aliases: []
claim_ids:
- clm_05e5caed0636562102fb164961c9d12697681a7d9cfb974ff3f4f9e9a7bf8d48
- clm_1249423a4b3c6a3aff241e09241e3ab21a6ee5aecb1d244c7bc4e1e1153181ac
- clm_284ee53b233a5bd7c32a72700fcc6a4d9e4965a94b412fb5beefda8e0a3637ef
- clm_28df0c67b0b8449675e230afee62f7d2a96ad031d0fa61fab0eaa418df445c98
- clm_43c26cca1e3c4426e52dcaec0d27b6133dceac93bdef69fd2c0fa57c0e3713a2
- clm_83351cb1f7e6ebd6b9f398b4f165d5ed26c95cda1002d5da80d809a817591f92
- clm_adad25f7d3f8016dce392f75c19c42a563af7837d5c8b8b226f52c9f905275ea
- clm_eedc583ae6b2c59659f750aeb4a97ea03aa145a3f39ab6f7aaee20908af2dbfe
maturity: draft
page_id: pg_cebb873dab0858b082c6c5d29ab815a4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5ce8a7e4abf05d4bb586c0b15e41621e
title: dazuiba/handoff/README.md @ 717ac79e1885
updated_at: '2026-09-14T03:06:31Z'
---

# dazuiba/handoff/README.md @ 717ac79e1885

<!-- rcw:begin owner=source:src_5ce8a7e4abf05d4bb586c0b15e41621e block=evidence -->
- The tool is distributed as handoff-cli, installable via uv tool install, pipx, or pip, and requires Claude Code or Codex to be installed and logged in. [@claim:clm_05e5caed0636562102fb164961c9d12697681a7d9cfb974ff3f4f9e9a7bf8d48]
- In Claude Code the tool is invoked via slash skills like /handoff-ds and /handoff-codex; Codex has no slash commands, so users mention custom agents such as handoff-ds by name. [@claim:clm_1249423a4b3c6a3aff241e09241e3ab21a6ee5aecb1d244c7bc4e1e1153181ac]
- The CLI exposes run, resume, list/ls, tail, env, init, and new commands; list and tail provide interactive TUI views of task history and live output streams. [@claim:clm_284ee53b233a5bd7c32a72700fcc6a4d9e4965a94b412fb5beefda8e0a3637ef]
- State persists under ~/.handoff, including config.yaml, a SQLite runs database (handoff.db), and tui_state.json storing the user's TUI theme choice. [@claim:clm_28df0c67b0b8449675e230afee62f7d2a96ad031d0fa61fab0eaa418df445c98]
- Backends are configured in ~/.handoff/config.yaml; any Anthropic-compatible endpoint can be added, env keys are exported before the CLI launches, {model} substitutes the resolved model, and ${ENV_VAR} expands from the shell. [@claim:clm_43c26cca1e3c4426e52dcaec0d27b6133dceac93bdef69fd2c0fa57c0e3713a2]
- Dispatched tasks return exactly one line, RESULT=<path-to-result-file>, to the calling session; that path serves as a stable handle so every follow-up resumes the same session. [@claim:clm_83351cb1f7e6ebd6b9f398b4f165d5ed26c95cda1002d5da80d809a817591f92]
- The opus and codex backends reuse existing Claude Code / Codex logins with zero configuration; only DeepSeek requires a token. [@claim:clm_adad25f7d3f8016dce392f75c19c42a563af7837d5c8b8b226f52c9f905275ea]
- Tasks run in the background so the main session never blocks; handoff launches the backend CLI (claude -p or codex exec) in an isolated context and streams output to disk, and several tasks can be dispatched in one message. [@claim:clm_eedc583ae6b2c59659f750aeb4a97ea03aa145a3f39ab6f7aaee20908af2dbfe]
<!-- rcw:end owner=source:src_5ce8a7e4abf05d4bb586c0b15e41621e block=evidence -->

## Researcher notes

