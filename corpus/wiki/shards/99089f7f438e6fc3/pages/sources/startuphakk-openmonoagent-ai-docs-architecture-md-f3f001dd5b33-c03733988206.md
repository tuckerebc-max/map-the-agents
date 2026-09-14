---
access: public
aliases: []
claim_ids:
- clm_0641fe9b019de1a567b881f65e66b01d468320fa0ca6994975e16440f63d19de
- clm_420740377277fcfd902da187e2b896d3017d2f97b1c5aa4c3896e6a86890e142
- clm_5d6b7f2fbc595d4a3d5260fc241bc5236a6ad105e115dc98b06deb64dba57551
- clm_65a58eb902cf36160e7f11c5f13f02ba063b96d5c28d01e314c257eb55702126
- clm_938f517c21119d7d155b05ff723df8702b6db1b85aefc3d59e837e44d05b8c14
- clm_ac1f29675af26284103b979753bafc0c9300278dea75d3e2dda2aef9cb6b2143
- clm_b59c11f6e8329cdfd91d8a2cbdf570822d56f42f5e5a7ddbceb2f017ab823969
- clm_bd1f76a5e424e225aeb6281413f4302e4609191b2b4469fdb688e1acfec55465
- clm_c7a625b02570aa55c43c9fab0a3f618bf92abde3de835a94c6a28ead5d73e3de
- clm_ca66c7cac0c064bd0110c4bf071f24bc7f75c3b685c69cab52e7a9d5eaafd1a1
- clm_ce440f9177eeff87dbaa5d83320db4d29bcdce56b314bdf711fc8df3160559da
- clm_f6e27268dee23c4d465b7cb710fe710338cdcd030baf73f05c1ffcd21ce6cf07
- clm_ffbe4ca569205d7d9363b00f7fea62b96266c27d72fe2611eabbae0c14e4837c
maturity: draft
page_id: pg_6a26848395fb5779a5e4c03733988206
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3cc2d25e0d7652dca1217ef1200717f5
title: StartupHakk/OpenMonoAgent.ai/docs/ARCHITECTURE.md @ f3f001dd5b33
updated_at: '2026-09-14T02:43:21Z'
---

# StartupHakk/OpenMonoAgent.ai/docs/ARCHITECTURE.md @ f3f001dd5b33

<!-- rcw:begin owner=source:src_3cc2d25e0d7652dca1217ef1200717f5 block=evidence -->
- OpenMono is described as a .NET 10 CLI coding agent that runs entirely on local hardware, pairing with its own llama.cpp inference server and Docker sandboxing. [@claim:clm_0641fe9b019de1a567b881f65e66b01d468320fa0ca6994975e16440f63d19de]
- Sessions persist as JSONL under `~/.openmono/sessions/` with a header record plus messages, and checkpoints are stored in a sibling `.checkpoints.json` file. [@claim:clm_420740377277fcfd902da187e2b896d3017d2f97b1c5aa4c3896e6a86890e142]
- The agentic loop runs up to 25 iterations per turn, aborts on three identical repeated tool sequences (doom-loop detection), and ends when the LLM emits text with no tool calls. [@claim:clm_5d6b7f2fbc595d4a3d5260fc241bc5236a6ad105e115dc98b06deb64dba57551]
- Context management checkpoints at 65% context fill with an LLM summary and compacts at 80% as a fallback; thresholds track the real window read from llama.cpp `/props`. [@claim:clm_65a58eb902cf36160e7f11c5f13f02ba063b96d5c28d01e314c257eb55702126]
- LSP servers for C#, TypeScript, Python, Go, and Rust start lazily on first use, and MCP servers are spawned as subprocesses with a JSON-RPC 2.0 handshake over stdin/stdout. [@claim:clm_938f517c21119d7d155b05ff723df8702b6db1b85aefc3d59e837e44d05b8c14]
- A VS Code/Cursor extension connects to the agent over ACP on port 7475, started with `--acp-only --acp-port 7475`, sharing the same agent core as the CLI. [@claim:clm_ac1f29675af26284103b979753bafc0c9300278dea75d3e2dda2aef9cb6b2143]
- Five specialist sub-agents (Explore, Plan, Coder, Verify, general-purpose) run in isolated sessions with restricted tool allow-lists and per-agent turn budgets from 10 to 30. [@claim:clm_b59c11f6e8329cdfd91d8a2cbdf570822d56f42f5e5a7ddbceb2f017ab823969]
- Every tool call passes a 12-step pipeline including schema validation, plan-mode guard, capability check, caching, pre/post hooks, and artifact storage for results over 10 KB. [@claim:clm_bd1f76a5e424e225aeb6281413f4302e4609191b2b4469fdb688e1acfec55465]
- A PermissionEngine uses a capability system (file read/write, process exec, network egress, VCS mutation, agent spawn) with decision order: deny-all, deny patterns, allow-all, allow patterns, then interactive prompt. [@claim:clm_c7a625b02570aa55c43c9fab0a3f618bf92abde3de835a94c6a28ead5d73e3de]
- Web search and scraping rely on self-hosted SearXNG and Scrapling+Camoufox behind a Caddy gateway, with automatic fallback to DuckDuckGo or direct HTTP fetch when services are absent. [@claim:clm_ca66c7cac0c064bd0110c4bf071f24bc7f75c3b685c69cab52e7a9d5eaafd1a1]
- A Roslyn tool loads .cs files into an in-memory AdhocWorkspace with a 5-minute compilation cache, exposing actions like find-references, callers, diagnostics, type-hierarchy, and blast-radius. [@claim:clm_ce440f9177eeff87dbaa5d83320db4d29bcdce56b314bdf711fc8df3160559da]
- The Docker sandbox mounts the project as /workspace, and the documentation states nothing outside that mount is visible or reachable from the agent. [@claim:clm_f6e27268dee23c4d465b7cb710fe710338cdcd030baf73f05c1ffcd21ce6cf07]
- The CLI offers TUI mode by default and a classic scrolling terminal via `openmono agent --classic`; renderer selection falls back to classic when I/O is redirected. [@claim:clm_ffbe4ca569205d7d9363b00f7fea62b96266c27d72fe2611eabbae0c14e4837c]
<!-- rcw:end owner=source:src_3cc2d25e0d7652dca1217ef1200717f5 block=evidence -->

## Researcher notes

