---
access: public
aliases: []
claim_ids:
- clm_1f279a9815daec4bf8db82b54d2bb55e59f642c523b71cbb89f13c1e680e98d2
- clm_1f6db99ab0c539bd9c610a285ff0ffb8e33c2d6afab573fc26fbcfc78ebeefc7
- clm_254a4ec615c5ccbfe8623974811120f33db685fdad36f97628467a52a32d3b75
- clm_4c52c6a4997e97a6951af68698879785680eb833d78a081e1d997ea4273bcd57
- clm_525b64bb7f8f6b109fb5cdc115487b7c5199583462720c20e8b6de0fb2e20527
- clm_80742661beddb1a77a576c05f7d3386ba8469136d39c519535cd1ebd5ddd749c
- clm_948d0361ca80b1dbd1a45b782799f68b948900c469871185afec537c35bb0a6d
- clm_aa509a4cfca10b1f3fcf95ce6848ed728adb6f423f5253e44c47138a4d1e04d0
- clm_b006ee4fbdf795a91b4f35fdf2e14c9e6649eb2bf47253d7e90712fcdb2fd680
- clm_d5708579cd114a667b9a9a2fd8897a1fc69c319fd263337c0af87d497fa3e89e
- clm_e2f0f67a0911193cdc777d97548a1bcadf45988fc2c5a5641e399ead6b246c0d
maturity: draft
page_id: pg_07dda5063b0654e0b292f93177e72b33
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_53d996e04de15ae9930eafe0ccada087
title: vibheksoni/VerbalCodeAi/README.md @ b65654df0be4
updated_at: '2026-09-14T03:22:07Z'
---

# vibheksoni/VerbalCodeAi/README.md @ b65654df0be4

<!-- rcw:begin owner=source:src_53d996e04de15ae9930eafe0ccada087 block=evidence -->
- Repository development practice: setup is via platform scripts (setup_windows.bat, setup_linux.sh) or manual venv creation plus pip install -r requirements.txt and a .env file. [@claim:clm_1f279a9815daec4bf8db82b54d2bb55e59f642c523b71cbb89f13c1e680e98d2]
- Performance can be tuned via PERFORMANCE_MODE (LOW/MEDIUM/MAX), MAX_THREADS, embedding cache size, similarity threshold, and per-provider API delay settings. [@claim:clm_1f6db99ab0c539bd9c610a285ff0ffb8e33c2d6afab573fc26fbcfc78ebeefc7]
- The app runs via `python app.py` with a main menu offering Chat with AI, Agent Mode, Reindex Project, Project Info, Settings, and Exit. [@claim:clm_254a4ec615c5ccbfe8623974811120f33db685fdad36f97628467a52a32d3b75]
- Anthropic and Groq do not provide embedding capabilities, so a different provider must be used for embeddings when those providers are selected. [@claim:clm_4c52c6a4997e97a6951af68698879785680eb833d78a081e1d997ea4273bcd57]
- Repository development practice: contributions follow a fork, feature-branch, commit, push, and pull-request workflow, and PRs are welcomed. [@claim:clm_525b64bb7f8f6b109fb5cdc115487b7c5199583462720c20e8b6de0fb2e20527]
- Supported LLM providers are Ollama (default, local), Google AI, OpenAI, Anthropic, Groq, and OpenRouter, each configured via .env provider and API-key variables. [@claim:clm_80742661beddb1a77a576c05f7d3386ba8469136d39c519535cd1ebd5ddd749c]
- The AI has a memory system for project information, controlled by MEMORY_ENABLED with a configurable MAX_MEMORY_ITEMS cap (default 10). [@claim:clm_948d0361ca80b1dbd1a45b782799f68b948900c469871185afec537c35bb0a6d]
- VerbalCodeAI is a terminal-based AI code companion offering code analysis, natural-language code search, chat, and agent mode, using embeddings and LLM integration. [@claim:clm_aa509a4cfca10b1f3fcf95ce6848ed728adb6f423f5253e44c47138a4d1e04d0]
- Agent Mode provides search, file, code-analysis, git, memory, system-command, and web tools, including embed_search, run_command, git_history, and google_search. [@claim:clm_b006ee4fbdf795a91b4f35fdf2e14c9e6649eb2bf47253d7e90712fcdb2fd680]
- The HTTP server accepts only localhost connections by default; setting HTTP_ALLOW_ALL_ORIGINS=TRUE in .env allows connections from any IP address. [@claim:clm_d5708579cd114a667b9a9a2fd8897a1fc69c319fd263337c0af87d497fa3e89e]
- A built-in HTTP API server is started with `python app.py --serve [PORT]` (default 8000) and exposes health, initialize, ask, index/start, and index/status endpoints. [@claim:clm_e2f0f67a0911193cdc777d97548a1bcadf45988fc2c5a5641e399ead6b246c0d]
<!-- rcw:end owner=source:src_53d996e04de15ae9930eafe0ccada087 block=evidence -->

## Researcher notes

