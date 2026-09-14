---
access: public
aliases: []
claim_ids:
- clm_0cbadcc8047e32e3963c954f3489b3da7a3337759c1bc723495f9c02f6481fc3
- clm_1498106074384681347da2843fe5328e05416eb8f52482ec873661a6ae3a16a3
- clm_2d46bb3a2ee2ab34a435799916aacc0d0fa234728a33e36364e961b58b1ac404
- clm_31ca53605b9ffa5e977bdd5f2fa1b0d79a8db1e1fa219394e3bc8c90ff791fca
- clm_402d827ddfa00ffec9ef659ce16cfce5f421717d11e0af792f5e9ba0ef730ab2
- clm_437bc316111fa639905d9ef1f01b02ba11e20b0d58eca3a8f0700980d973dd07
- clm_631282014c8209c51c393c78a6d12ab03ff84cbfb48f1af94e14e7f18fae2e74
- clm_8271009ffd6728d4cec7df24567777d0afd05ba58c2218f451f4bab9b8712a4c
- clm_90214120fc7c6c43456a3c439bbafaa64df0858f5b31ea0370771579741c66a8
- clm_b47aa5719529611de33ff28e629038b70b6ef95b0d773e78ac8e61d6727c0978
- clm_d79d9ee3e5e097013e2922a6f27049a5b22d0170005b88d0d25946628c4af597
- clm_db5e90f1f143c0e21a75cfdd920a931e1fc29f0de292f09282d0346c854690d8
maturity: draft
page_id: pg_14f8b1c0a2d95a81b751d90a8447516c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_566f9cc73b1a506ba0c6356333b29a40
title: zap-coding-agent/zap-coding-agent/README.md @ 6ab48b82c15e
updated_at: '2026-09-14T03:27:14Z'
---

# zap-coding-agent/zap-coding-agent/README.md @ 6ab48b82c15e

<!-- rcw:begin owner=source:src_566f9cc73b1a506ba0c6356333b29a40 block=evidence -->
- MCP servers stay pending at startup with only a lightweight mcp_connect stub in context; the server process is spawned and its real tool schemas fetched only when the model calls mcp_connect. [@claim:clm_0cbadcc8047e32e3963c954f3489b3da7a3337759c1bc723495f9c02f6481fc3]
- ZAP uses a skill system of markdown files injected only when triggered: always-on skills (e.g. karpathy-guidelines) fire every turn, while triggered skills like rust, git, or security fire on keyword matches in the user's message. [@claim:clm_1498106074384681347da2843fe5328e05416eb8f52482ec873661a6ae3a16a3]
- Before content is sent to a cloud LLM, a secret scanner checks patterns including API keys, VCS tokens, AWS/GCP credentials, PEM blocks, and JWTs, blocking matches with a redacted warning; every tool call is appended to ~/.zap/audit.jsonl. [@claim:clm_2d46bb3a2ee2ab34a435799916aacc0d0fa234728a33e36364e961b58b1ac404]
- The AST code index is built at startup with tree-sitter and SQLite, stored at .zap/code.db, supports Rust, Python, TypeScript, JavaScript, Go, and Java, and reindexes edited files before the next LLM turn. [@claim:clm_31ca53605b9ffa5e977bdd5f2fa1b0d79a8db1e1fa219394e3bc8c90ff791fca]
- The README reports a token-efficiency comparison claiming ZAP sends task-specific prompts (1,889 vs 1,661 tokens for Spring Boot vs React) versus identical static prompts from Gemini CLI and OpenCode, with methodology in a linked evidence file. [@claim:clm_402d827ddfa00ffec9ef659ce16cfce5f421717d11e0af792f5e9ba0ef730ab2]
- Skills resolve by priority: project-level .zap/skills/ overrides personal ~/.zap/skills/, which overrides built-in defaults compiled into the binary; same-name custom skills override built-ins. [@claim:clm_437bc316111fa639905d9ef1f01b02ba11e20b0d58eca3a8f0700980d973dd07]
- Slash commands manage skills, including /skill list, show, export, create, and capture, the last of which extracts instructions from the current session into a reusable skill. [@claim:clm_631282014c8209c51c393c78a6d12ab03ff84cbfb48f1af94e14e7f18fae2e74]
- ZAP has three permission modes — ask (default, prompts before writes and shell), auto, and deny (read-only) — switchable via /permissions, plus a shell sandbox with workdir and container (Docker/Podman, network disabled) modes. [@claim:clm_8271009ffd6728d4cec7df24567777d0afd05ba58c2218f451f4bab9b8712a4c]
- ZAP is a terminal-first, local AI coding agent written in Rust, distributed as a single statically-linked binary with no runtime dependency on Python, Node.js, or Docker. [@claim:clm_90214120fc7c6c43456a3c439bbafaa64df0858f5b31ea0370771579741c66a8]
- Index-backed tools include code_map, find_definition, find_references, who_calls, file_imports, where_imported, find_subtypes/supertypes, pack_context, ripple_analysis, get_diagnostics, lsp_definition, and lsp_type_at. [@claim:clm_b47aa5719529611de33ff28e629038b70b6ef95b0d773e78ac8e61d6727c0978]
- ZAP maintains four context files (ZAP.md, .zap/understanding.md, .zap/context.md, .zap/session_log.md) updated at defined times and loaded on demand via read_file rather than pre-loaded into context. [@claim:clm_d79d9ee3e5e097013e2922a6f27049a5b22d0170005b88d0d25946628c4af597]
- A documented domain map lists modules including agent_core, llm_client, tools with permission_manager and shell_runner, context_manager, code_index, mcp, persistence, skill_manager, and remote session sharing. [@claim:clm_db5e90f1f143c0e21a75cfdd920a931e1fc29f0de292f09282d0346c854690d8]
<!-- rcw:end owner=source:src_566f9cc73b1a506ba0c6356333b29a40 block=evidence -->

## Researcher notes

