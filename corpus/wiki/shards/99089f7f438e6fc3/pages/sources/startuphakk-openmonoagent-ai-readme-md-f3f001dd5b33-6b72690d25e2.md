---
access: public
aliases: []
claim_ids:
- clm_0641fe9b019de1a567b881f65e66b01d468320fa0ca6994975e16440f63d19de
- clm_138fbf0c21b79c0f1041154cdba3d948fef9a5d54d90d113577c3c8f43c6dbad
- clm_5d6b7f2fbc595d4a3d5260fc241bc5236a6ad105e115dc98b06deb64dba57551
- clm_ac1f29675af26284103b979753bafc0c9300278dea75d3e2dda2aef9cb6b2143
- clm_b59c11f6e8329cdfd91d8a2cbdf570822d56f42f5e5a7ddbceb2f017ab823969
- clm_bd1f76a5e424e225aeb6281413f4302e4609191b2b4469fdb688e1acfec55465
- clm_ca66c7cac0c064bd0110c4bf071f24bc7f75c3b685c69cab52e7a9d5eaafd1a1
- clm_f6e27268dee23c4d465b7cb710fe710338cdcd030baf73f05c1ffcd21ce6cf07
- clm_fd6c150a9cb6312fde2ad8251bcfad84b788b37823367c30cdf71f9575b43f27
- clm_ffbe4ca569205d7d9363b00f7fea62b96266c27d72fe2611eabbae0c14e4837c
maturity: draft
page_id: pg_d196452660ed50d5bfec6b72690d25e2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c881fdfb315658d688a9b132e3d16a6b
title: StartupHakk/OpenMonoAgent.ai/README.md @ f3f001dd5b33
updated_at: '2026-09-14T02:43:21Z'
---

# StartupHakk/OpenMonoAgent.ai/README.md @ f3f001dd5b33

<!-- rcw:begin owner=source:src_c881fdfb315658d688a9b132e3d16a6b block=evidence -->
- OpenMono is described as a .NET 10 CLI coding agent that runs entirely on local hardware, pairing with its own llama.cpp inference server and Docker sandboxing. [@claim:clm_0641fe9b019de1a567b881f65e66b01d468320fa0ca6994975e16440f63d19de]
- Repository development practice: the README directs contributors to read CONTRIBUTING.md before opening a PR and welcomes contributions of tools, providers, LSP servers, playbooks, bug fixes, and docs. [@claim:clm_138fbf0c21b79c0f1041154cdba3d948fef9a5d54d90d113577c3c8f43c6dbad]
- The agentic loop runs up to 25 iterations per turn, aborts on three identical repeated tool sequences (doom-loop detection), and ends when the LLM emits text with no tool calls. [@claim:clm_5d6b7f2fbc595d4a3d5260fc241bc5236a6ad105e115dc98b06deb64dba57551]
- A VS Code/Cursor extension connects to the agent over ACP on port 7475, started with `--acp-only --acp-port 7475`, sharing the same agent core as the CLI. [@claim:clm_ac1f29675af26284103b979753bafc0c9300278dea75d3e2dda2aef9cb6b2143]
- Five specialist sub-agents (Explore, Plan, Coder, Verify, general-purpose) run in isolated sessions with restricted tool allow-lists and per-agent turn budgets from 10 to 30. [@claim:clm_b59c11f6e8329cdfd91d8a2cbdf570822d56f42f5e5a7ddbceb2f017ab823969]
- Every tool call passes a 12-step pipeline including schema validation, plan-mode guard, capability check, caching, pre/post hooks, and artifact storage for results over 10 KB. [@claim:clm_bd1f76a5e424e225aeb6281413f4302e4609191b2b4469fdb688e1acfec55465]
- Web search and scraping rely on self-hosted SearXNG and Scrapling+Camoufox behind a Caddy gateway, with automatic fallback to DuckDuckGo or direct HTTP fetch when services are absent. [@claim:clm_ca66c7cac0c064bd0110c4bf071f24bc7f75c3b685c69cab52e7a9d5eaafd1a1]
- The Docker sandbox mounts the project as /workspace, and the documentation states nothing outside that mount is visible or reachable from the agent. [@claim:clm_f6e27268dee23c4d465b7cb710fe710338cdcd030baf73f05c1ffcd21ce6cf07]
- Local llama.cpp is the default and fully supported provider; OpenAI, Anthropic, and Ollama providers are documented as available but work-in-progress. [@claim:clm_fd6c150a9cb6312fde2ad8251bcfad84b788b37823367c30cdf71f9575b43f27]
- The CLI offers TUI mode by default and a classic scrolling terminal via `openmono agent --classic`; renderer selection falls back to classic when I/O is redirected. [@claim:clm_ffbe4ca569205d7d9363b00f7fea62b96266c27d72fe2611eabbae0c14e4837c]
<!-- rcw:end owner=source:src_c881fdfb315658d688a9b132e3d16a6b block=evidence -->

## Researcher notes

