---
access: public
aliases: []
claim_ids:
- clm_0baa37ce201822a478a776f7daba1b74abc4ce0f2026dee83d0a4685038640fb
- clm_1d310568b677a06c7fe23d8cfd7116f1c0b0b4e07758110f19a7993dc80db8f7
- clm_2e847a2d1ace253497f63d58e46dbadc556e402b8ea7e09041811b43c9d26f35
- clm_2fc2b97348c1555c5ba81b888cf8c5e7b45f4e70bf58fb5075e95baa03253843
- clm_3c14424bc4334b88070601ba6dc1305cdcf6292afc9d07318511261da4d86950
- clm_4dfe9c7a7357fadb0e55e2af544c1074fcb80ba3fdf4394ec3865a5d4e56f005
- clm_51026b6e21cca3154de9adb1ae9ccc6e5c97616437ba0732128e603166460e40
- clm_69a04ac3a23bf342b9db88c4a08b8fde46a182bea213842d8223a7979d8d1f1b
- clm_79d0bb44e32584ddb4b06b655ce953583e9282baee7342d263a455a6000b56da
- clm_8f43a2c17da823b86637cfe0997ec782476659fdd467e501576b100917d2c3dc
- clm_96c4ae598502f6bb42b0056b703d31bc5c276cbf27c518d42cd3a3b7c097e8a4
- clm_be95bf4204416c7310220ba674091f41d401029d0aa7d121f6550e2c70bf5d6c
maturity: draft
page_id: pg_a0a13f19dede51e59537b7c6e55749a5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d4adc3b2a4365db8a923c7a2f89c0ffa
title: ramarlina/agx/README.md @ e674cec11088
updated_at: '2026-09-14T02:34:58Z'
---

# ramarlina/agx/README.md @ e674cec11088

<!-- rcw:begin owner=source:src_d4adc3b2a4365db8a923c7a2f89c0ffa block=evidence -->
- CLI commands include `agx init` for first-time setup, `agx board start` to open the ticket-agent-PR board, plus project, repo, workspace, and vars subcommands. [@claim:clm_0baa37ce201822a478a776f7daba1b74abc4ce0f2026dee83d0a4685038640fb]
- Repository development practice: contributions are welcomed via GitHub Discussions and Issues, with PRs made by forking main, adding tests, and submitting. [@claim:clm_1d310568b677a06c7fe23d8cfd7116f1c0b0b4e07758110f19a7993dc80db8f7]
- The CLI exposes provider chat commands such as `agx claude -p`, `agx codex -p`, `agx gemini -p`, and `agx ollama -p`, with single-letter aliases c, x, g, o. [@claim:clm_2e847a2d1ace253497f63d58e46dbadc556e402b8ea7e09041811b43c9d26f35]
- Repository development practice: the repo is an npm workspace with apps/local (Next.js dashboard), apps/desktop (Electron), lib, commands, and cloud-runtime; dev commands include `npm run local:dev`, `local:build`, `board:bundle`, and Electron `build:mac`. [@claim:clm_2fc2b97348c1555c5ba81b888cf8c5e7b45f4e70bf58fb5075e95baa03253843]
- The telemetry documentation states prompts, code, API keys, file paths, and PII are not collected. [@claim:clm_3c14424bc4334b88070601ba6dc1305cdcf6292afc9d07318511261da4d86950]
- Agents pause for explicit human approve/reject before anything irreversible, and PR review begins with a first pass from a reviewer agent. [@claim:clm_4dfe9c7a7357fadb0e55e2af544c1074fcb80ba3fdf4394ec3865a5d4e56f005]
- Requires Node.js >= 22.16.0 for CLI install and at least one provider CLI (Claude Code, Codex CLI, Gemini CLI, or Ollama); no external database is needed since SQLite is used locally. [@claim:clm_51026b6e21cca3154de9adb1ae9ccc6e5c97616437ba0732128e603166460e40]
- Telemetry is enabled by default, collecting anonymous usage data such as OS, Node and AGX versions, commands run, provider used, task outcomes, and timing; it can be disabled via `agx telemetry off` or config. [@claim:clm_69a04ac3a23bf342b9db88c4a08b8fde46a182bea213842d8223a7979d8d1f1b]
- AGX ships as a CLI, a local web dashboard, and a macOS desktop app from one repository. [@claim:clm_79d0bb44e32584ddb4b06b655ce953583e9282baee7342d263a455a6000b56da]
- Work is checkpointed at every step so restarts resume where the user left off, and resuming is described as constant-cost regardless of thread age. [@claim:clm_8f43a2c17da823b86637cfe0997ec782476659fdd467e501576b100917d2c3dc]
- The product claims fully local operation with an activity log, signed actions, and destructive-command safeguards. [@claim:clm_96c4ae598502f6bb42b0056b703d31bc5c276cbf27c518d42cd3a3b7c097e8a4]
- The architecture comprises a SQLite (WAL mode) state layer with durable checkpoints, a CLI plus daemon handling provider tool calls, filesystem edits, and worktree isolation, and a decision layer for human gate transitions and review flow. [@claim:clm_be95bf4204416c7310220ba674091f41d401029d0aa7d121f6550e2c70bf5d6c]
<!-- rcw:end owner=source:src_d4adc3b2a4365db8a923c7a2f89c0ffa block=evidence -->

## Researcher notes

