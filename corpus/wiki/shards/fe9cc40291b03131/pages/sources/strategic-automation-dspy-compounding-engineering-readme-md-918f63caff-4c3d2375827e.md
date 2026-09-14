---
access: public
aliases: []
claim_ids:
- clm_0c8b310c35c06e63bd9bf6b68601577f9b48d0c1eb1d6254282a1e323f5cdf14
- clm_140ba188d741e515c5fe9659795b85555510f54b6f081df3d1b07095da9f815e
- clm_2282cc45b7b763672a60bffcde8e090ecb761c78a0c2ab299357fea5fffa4fcf
- clm_519257e91ad178073e35be7c1f61147855fd64c14a0807f1df44f1037a86e518
- clm_52a42e925f6d311e8f109073c74063fe67b141093ec1162576ee220543af3485
- clm_579119dc01569c49d291fd01c2e675d95c545e0b2f991307cfbad0a2d6d457cc
- clm_8395cb28fc32919358425a6857a0e1a67d6b9631a8ac6d4ccce4557f5ce9ccf1
- clm_99fffbc13297e97fe4adb725d74312a2ec89cb7a81525bd790a082beabb62262
- clm_9b5a268f1b5137b90e378a75e14166d12d3a5879c1be6f60b8a9042f03054a22
- clm_a1fd99747b9dc8f7c8c2a6bef42a8fcab4b9077de626776b492f6d8b9fb6b9de
- clm_a4de5b450f2907fd55cee35dea117bd8351a943693a1b6ed772b3b22c912fbd3
- clm_b3589ade229303d9d7034ba686bdb8cfa53d3dd97fd8a2eca8de042357c89a46
- clm_bd7a9278969d1cc51945dd59810d9610efe684f428320877088deafd35e6d2cd
- clm_d8f3fe892b2a15961648c6a102734991a85ea0dc06ae0dadef85a09bcba711f4
- clm_f286d75ec5e663819d15c0c6b19c35a71ad7ec3a4902f32a305dc039d06e8b42
maturity: draft
page_id: pg_2e89e4999bde5c0fa9b74c3d2375827e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f0a7a9d0806c54ac814fe8ec356e813e
title: Strategic-Automation/dspy-compounding-engineering/README.md @ 918f63caff79
updated_at: '2026-09-14T03:15:54Z'
---

# Strategic-Automation/dspy-compounding-engineering/README.md @ 918f63caff79

<!-- rcw:begin owner=source:src_f0a7a9d0806c54ac814fe8ec356e813e block=evidence -->
- Installation is uv-based: a recommended installer script locks Python 3.12 in an isolated environment, a pip wrapper (dspyce-install) bootstraps uv, and a repo-root ./uvx wrapper runs the CLI without global install. [@claim:clm_0c8b310c35c06e63bd9bf6b68601577f9b48d0c1eb1d6254282a1e323f5cdf14]
- Configuration is loaded in priority order: --env-file flag, COMPOUNDING_ENV variable, CWD .env, ~/.config/compounding/.env, then ~/.env, with a warning on conflicting files. [@claim:clm_140ba188d741e515c5fe9659795b85555510f54b6f081df3d1b07095da9f815e]
- The CLI also includes a generate-agent command that creates new review agents from a natural language description, with a --dry-run option. [@claim:clm_2282cc45b7b763672a60bffcde8e090ecb761c78a0c2ab299357fea5fffa4fcf]
- Work execution can run in isolated git worktrees for safe parallel execution, with automatic worktree cleanup after completion. [@claim:clm_519257e91ad178073e35be7c1f61147855fd64c14a0807f1df44f1037a86e518]
- The project depends on the DSPy framework, supports LLM providers OpenAI, Anthropic, Ollama, and OpenRouter via env config, and uses Playwright (Chromium) for documentation fetching. [@claim:clm_52a42e925f6d311e8f109073c74063fe67b141093ec1162576ee220543af3485]
- Global options include -e/--env-file and -h/--help; the work command supports --dry-run, --worktree, --sequential, and --workers flags. [@claim:clm_579119dc01569c49d291fd01c2e675d95c545e0b2f991307cfbad0a2d6d457cc]
- The tool is designed as a local-first CLI running on the user's machine, in contrast to the original Claude Code plugin it reimplements. [@claim:clm_8395cb28fc32919358425a6857a0e1a67d6b9631a8ac6d4ccce4557f5ce9ccf1]
- Repository development practice: contributors are directed to CONTRIBUTING.md for guidelines, and source setup involves cloning, copying .env.example to .env, and running 'uv sync'. [@claim:clm_99fffbc13297e97fe4adb725d74312a2ec89cb7a81525bd790a082beabb62262]
- The tool can run as an MCP server (compounding-mcp, described as a FastMCP server) exposing compounding_review, compounding_plan, compounding_work, compounding_triage, and compounding_sync tools to clients like Claude Desktop. [@claim:clm_9b5a268f1b5137b90e378a75e14166d12d3a5879c1be6f60b8a9042f03054a22]
- The system is layered: a CLI layer (cli.py), orchestration layer (workflows/), DSPy agents layer (agents/), knowledge layer, and infrastructure/utils layer. [@claim:clm_a1fd99747b9dc8f7c8c2a6bef42a8fcab4b9077de626776b492f6d8b9fb6b9de]
- The product exposes a Typer-based CLI ('compounding') with commands including review, triage, work, plan, and codify, mapping user intents to workflows. [@claim:clm_a4de5b450f2907fd55cee35dea117bd8351a943693a1b6ed772b3b22c912fbd3]
- Learnings are persisted as structured JSON in a .knowledge/ directory, with keyword/tag-based retrieval and automatic injection of relevant past learnings into agent calls via a KBPredict wrapper. [@claim:clm_b3589ade229303d9d7034ba686bdb8cfa53d3dd97fd8a2eca8de042357c89a46]
- Qdrant is used for semantic search (startable via Docker Compose on localhost:6333); if Qdrant is not running, the system falls back to keyword-based search over local JSON files. [@claim:clm_bd7a9278969d1cc51945dd59810d9610efe684f428320877088deafd35e6d2cd]
- Parallelism uses ThreadPoolExecutor for multi-agent and multi-todo execution, with --workers to set worker count and --sequential for serial mode. [@claim:clm_d8f3fe892b2a15961648c6a102734991a85ea0dc06ae0dadef85a09bcba711f4]
- Review agents include specialized roles such as Security Sentinel (vulnerabilities), Performance Oracle (bottlenecks), Architecture Strategist, and Data Integrity Guardian, with 10+ agents run in parallel. [@claim:clm_f286d75ec5e663819d15c0c6b19c35a71ad7ec3a4902f32a305dc039d06e8b42]
<!-- rcw:end owner=source:src_f0a7a9d0806c54ac814fe8ec356e813e block=evidence -->

## Researcher notes

