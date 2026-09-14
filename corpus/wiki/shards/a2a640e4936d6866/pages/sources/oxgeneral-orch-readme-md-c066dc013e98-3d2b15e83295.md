---
access: public
aliases: []
claim_ids:
- clm_08569e44fc8bd43487689889348c5d96d9dced2ae1a09a227644c62f95570c32
- clm_0bd0f5f22d71c11d5ef518b271eb0f8eae03cad958f334c27546cd479d10c770
- clm_13bd75b62e6872704931e609b0d874af568111c79315a5b02ed41b89bb2279eb
- clm_4fca750d1579bb89b05b5efa0f3a5c80935ae5805b75527c1a6f1887e4112fe6
- clm_5ecd8e0f55cf6451263727dcc2012865189445fd8a7bf5ac96586463c8cca31b
- clm_639e84802208e1b57113845f1f3b831ab7353ba48554e3009d850bdad05f0bdc
- clm_73a2fa9a38b90e6f54419894110e30021ecd96cfae5bac23943d763303bf82e5
- clm_7516dc2b3db2d8609a70e6c20dd1259b622fd18cf9f5c898f37ea6740ce0c709
- clm_81fca59ea3a29c8b3a5ac861dcd6d032cd4d76749a8650f0174e25496be49562
- clm_95b34a8fc44b365c6a4f30f774c90e4a0920f1eecc82f8a9fdfb9f711799b51e
- clm_9949c9c5f9fd94f16d5909b6e4d3269c1086caa0d7b11e2925b0499568a82229
- clm_9956bb50131e6ed127f2eda66b23e5f9e86f16ab9649e0740bff89cada5036aa
- clm_ca1122903fb4773dd73c69ec81c2d3eb6077f29fdb48bc2758aeda3ab49a3f82
- clm_cab5a1fa178971ea023cffef36eb30af85c3a1faef14849d68af9daecd41baf5
- clm_d13e86e7b71a2d235b00d69607af451e7d611baabc9cec2863984070fc823c5a
- clm_f5f29fbd0b7ae4437ede475e49b58c6a2e0a9b84600b96aa8dcda5093ca48e8c
maturity: draft
page_id: pg_b4a83545f7145fa187253d2b15e83295
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1a8c9323c4b859c1958c10eabc7950f2
title: oxgeneral/ORCH/readme.md @ c066dc013e98
updated_at: '2026-09-14T02:29:04Z'
---

# oxgeneral/ORCH/readme.md @ c066dc013e98

<!-- rcw:begin owner=source:src_1a8c9323c4b859c1958c10eabc7950f2 block=evidence -->
- `orch serve` runs a headless daemon with a tick loop that picks up newly added tasks; a `--once` mode processes todo tasks and exits, with exit 0 meaning all done and exit 1 indicating failures. [@claim:clm_08569e44fc8bd43487689889348c5d96d9dced2ae1a09a227644c62f95570c32]
- The package can be imported as a library; the core reportedly has no dependency on the CLI/TUI layers, letting users build their own interface on top. [@claim:clm_0bd0f5f22d71c11d5ef518b271eb0f8eae03cad958f334c27546cd479d10c770]
- A CTO-style agent decomposes a high-level goal into tasks and delegates them; failed tasks auto-retry with exponential backoff and stalled agents are killed and re-queued by zombie detection. [@claim:clm_13bd75b62e6872704931e609b0d874af568111c79315a5b02ed41b89bb2279eb]
- Storage is file-based using YAML/JSON/JSONL, and agents communicate through direct messages, team broadcasts, and a shared context store. [@claim:clm_4fca750d1579bb89b05b5efa0f3a5c80935ae5805b75527c1a6f1887e4112fe6]
- The CLI is published as the npm package @oxgeneral/orch, installed globally, and launching `orch` in a project opens a TUI dashboard after auto-initialization. [@claim:clm_5ecd8e0f55cf6451263727dcc2012865189445fd8a7bf5ac96586463c8cca31b]
- ORCH targets solo founders and small teams running multiple AI coding/CLI agents on one project, positioning itself as open-source (MIT) orchestration where users pay only for their own AI API usage. [@claim:clm_639e84802208e1b57113845f1f3b831ab7353ba48554e3009d850bdad05f0bdc]
- Eight adapters are documented: Claude Code, OpenCode, Codex, Pi, Cursor, Grok, Antigravity, and Shell, where the shell adapter wraps any terminal CLI tool as an agent. [@claim:clm_73a2fa9a38b90e6f54419894110e30021ecd96cfae5bac23943d763303bf82e5]
- The daemon enforces single-orchestrator-per-project via a lock file (.orchestry/orchestry.lock), shuts down gracefully on SIGINT/SIGTERM, logs heap usage each tick, and throttles idle-tick logging. [@claim:clm_7516dc2b3db2d8609a70e6c20dd1259b622fd18cf9f5c898f37ea6740ce0c709]
- Pre-built organization templates are provided (e.g. startup-mvp, pr-review-corp, migration-squad, security-dept, content-agency, data-lab, sales-machine, docs-team) deployable via `orch org deploy`, with export of custom setups. [@claim:clm_81fca59ea3a29c8b3a5ac861dcd6d032cd4d76749a8650f0174e25496be49562]
- The runtime requires Node.js >= 20 on macOS, Linux, or WSL2, and needs no database, cloud service, Docker, or GPU since LLMs are accessed via API. [@claim:clm_95b34a8fc44b365c6a4f30f774c90e4a0920f1eecc82f8a9fdfb9f711799b51e]
- After installation, an `/orch` skill is reportedly available in Claude Code, translating natural-language requests into orch commands for agents, tasks, goals, and runs. [@claim:clm_9949c9c5f9fd94f16d5909b6e4d3269c1086caa0d7b11e2925b0499568a82229]
- Each agent works in an isolated git worktree on its own branch, and code reaches main only after explicit user approval through a mandatory review step in the task state machine. [@claim:clm_9956bb50131e6ed127f2eda66b23e5f9e86f16ab9649e0740bff89cada5036aa]
- Serve mode emits one JSON line per event (e.g. agent:started, task:status_changed, orchestrator:tick) with configurable json/text format, optional log file, and a default 10000 ms tick interval. [@claim:clm_ca1122903fb4773dd73c69ec81c2d3eb6077f29fdb48bc2758aeda3ab49a3f82]
- Tasks flow through a state machine (todo → in_progress → review → done) with validated transitions, and no code merges without approval. [@claim:clm_cab5a1fa178971ea023cffef36eb30af85c3a1faef14849d68af9daecd41baf5]
- The documented source layout includes domain (models, state machine), application (orchestrator engine, services, event bus), infrastructure (adapters, file storage, process management, LiquidJS templates, git worktree workspace), cli (Commander.js), and tui (Ink + React). [@claim:clm_d13e86e7b71a2d235b00d69607af451e7d611baabc9cec2863984070fc823c5a]
- ORCH exposes a CLI including commands such as orch init, doctor, agent add/list, org deploy/export, task add/assign/cancel, team create, goal add, msg send/broadcast, run, serve, status, logs, and tui. [@claim:clm_f5f29fbd0b7ae4437ede475e49b58c6a2e0a9b84600b96aa8dcda5093ca48e8c]
<!-- rcw:end owner=source:src_1a8c9323c4b859c1958c10eabc7950f2 block=evidence -->

## Researcher notes

