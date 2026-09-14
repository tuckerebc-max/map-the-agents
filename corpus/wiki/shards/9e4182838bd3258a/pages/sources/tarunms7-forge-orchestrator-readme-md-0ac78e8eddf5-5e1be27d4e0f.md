---
access: public
aliases: []
claim_ids:
- clm_0bcf280e948c1f20c08f7ace889c794519d1f7f0ff3d3805d81f69f5309bffbd
- clm_33f32e56edc697a59e9af78ddd8093c84d189188eab0bb424117818a9cd271c4
- clm_39cb5a8c1ce0d3afe40ff97ba09a46aecfde5eac5131ab4b5fce348945947fc4
- clm_7411f0e60d0310a10281c7c9accd8bc28e294697e7e1ba2e54d304b3e8405b6c
- clm_7b24c603b726ce130335b2c3ee33d7dcb555c211c381afce0f104f58663589e6
- clm_7d67f40c3bad1e1cf7e7e9bfdf7f43acae1b30c91bf4f80f549a0af9835e84a0
- clm_8a6ddf7536a6b29973804692e572d8e9f533e8e6906933d52864c0e3a08738d3
- clm_97ae59c960fad73e8553fd6ad5da1ca2ad33a268e79fcf8bc48228859f2ccae2
- clm_b62033299eb5122380245f1aef5f1906cee40c31b5a3d59e5a4aac80bed9a7d7
- clm_b6f2650fe72face375d81b566897f355f626f64e6f113cf89fff7ff2cc5a63a2
- clm_f0b547aba31bdf94027edff00a7c3a70ac5f40424bea70f22c149dcbba9854ef
maturity: draft
page_id: pg_a563fddfc8dc5c77bdfa5e1be27d4e0f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_24eada21bb3455a8825e324665831420
title: tarunms7/forge-orchestrator/README.md @ 0ac78e8eddf5
updated_at: '2026-09-14T03:18:05Z'
---

# tarunms7/forge-orchestrator/README.md @ 0ac78e8eddf5

<!-- rcw:begin owner=source:src_24eada21bb3455a8825e324665831420 block=evidence -->
- Claude is the default provider; OpenAI routing is opt-in via FORGE_OPENAI_ENABLED, with Codex-backed models using codex login or CODEX_API_KEY and openai:o3 requiring OPENAI_API_KEY. [@claim:clm_0bcf280e948c1f20c08f7ace889c794519d1f7f0ff3d3805d81f69f5309bffbd]
- Codex-backed agent executions run in full-access sandbox mode with automatic execution, no per-command approval prompts, live network access and native web search, while a Forge-level safety policy still blocks explicitly denied operations. [@claim:clm_33f32e56edc697a59e9af78ddd8093c84d189188eab0bb424117818a9cd271c4]
- Forge stores lessons learned from failed-then-retried tasks, filters transient errors like 503s, persists lessons across projects, and adapts timeouts after slow failures; lessons are viewable and addable via forge lessons. [@claim:clm_39cb5a8c1ce0d3afe40ff97ba09a46aecfde5eac5131ab4b5fce348945947fc4]
- A terminal UI (forge tui) and a web dashboard (forge serve, backend on port 8000 and frontend on 3000) provide live pipeline progress, plan editing, contract viewing, and cost tracking. [@claim:clm_7411f0e60d0310a10281c7c9accd8bc28e294697e7e1ba2e54d304b3e8405b6c]
- Pipelines run six stages: pre-flight validation, planning into a task DAG, contract generation, parallel execution in isolated git worktrees, a five-gate review (build, lint, test, LLM review, contracts), then format, rebase, merge, and gh pr create. [@claim:clm_7b24c603b726ce130335b2c3ee33d7dcb555c211c381afce0f104f58663589e6]
- A background health monitor detects tasks in progress over 15 minutes without activity, reviews running over 10 minutes, deadlocks, and dependency cascades, surfacing problems during execution. [@claim:clm_7d67f40c3bad1e1cf7e7e9bfdf7f43acae1b30c91bf4f80f549a0af9835e84a0]
- The product exposes a Click-based CLI with 14 commands including forge tui, run, fix, status, stats, logs, lessons, doctor, clean, init, serve, upgrade, and ping. [@claim:clm_8a6ddf7536a6b29973804692e572d8e9f533e8e6906933d52864c0e3a08738d3]
- Before coding, a Contract Builder generates binding API and type specs naming producer and consumer tasks, so parallel agents agree on interfaces; the reviewer checks compliance. [@claim:clm_97ae59c960fad73e8553fd6ad5da1ca2ad33a268e79fcf8bc48228859f2ccae2]
- Prerequisites are Git 2.20+ and the Claude Code CLI (claude login); the gh CLI is optional for automatic PR creation, and the installer handles Python 3.12 and uv. [@claim:clm_b62033299eb5122380245f1aef5f1906cee40c31b5a3d59e5a4aac80bed9a7d7]
- The resolved provider configuration is persisted in pipelines.provider_config at pipeline creation, and restarts, retries, and webhook resumptions reuse that snapshot rather than current settings. [@claim:clm_b6f2650fe72face375d81b566897f355f626f64e6f113cf89fff7ff2cc5a63a2]
- Repository development practice: contributors set up a venv, pip install -e '.[dev,web]', and run python -m pytest forge/ -q; CI runs ruff lint and format plus 2200+ tests on every PR. [@claim:clm_f0b547aba31bdf94027edff00a7c3a70ac5f40424bea70f22c149dcbba9854ef]
<!-- rcw:end owner=source:src_24eada21bb3455a8825e324665831420 block=evidence -->

## Researcher notes

