---
access: public
aliases: []
claim_ids:
- clm_0e00e645b8daf3e7c0235365253d43f81c750ac183df914a5e2d45b127b5df88
- clm_627d829ba3f32cd5f2fb1ee8f98f3a4b50beeca60147ae46eb910dba740e38dc
- clm_65f10b9848277131091a6d0d75cd9fbe28c47d48626832cfab51791beb87651f
- clm_7b60b6b7cdda99d008059e9a9f24816afc8d1666b19fa3be8340a70024a4f61c
- clm_82ca6c942a0816f17fd9de53073b1412977e5a4a343dc7888014d785c6db15fc
- clm_9a8f9904663487a5be3c373f07749e1507fc0fae6d7139369f45947f0a87980f
- clm_b8d8bdea9e2e7023abc49bdc9d9af76e740d6d08a8d8cca6d72fededf2a7dcb4
- clm_d2535d283b54d38cbf9fe5aec52a1bdc128aeafca0a14b5e6e31ebec046e729d
- clm_e3e02f21aa765804791976a0bc11fa9767c2548d851540defd5921545cc77c9e
- clm_fbce3145a3f79cf234902a7c2cb97925325c1fa916babc919920994f3e4fb541
maturity: draft
page_id: pg_d99799b0c22b5bee8953481165ac37e8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_158e6e62fd735b4584df266d0701fe0b
title: codeaholicguy/ai-devkit/README.md @ 1a3a0024eb3b
updated_at: '2026-09-14T01:42:05Z'
---

# codeaholicguy/ai-devkit/README.md @ 1a3a0024eb3b

<!-- rcw:begin owner=source:src_158e6e62fd735b4584df266d0701fe0b block=evidence -->
- agent send supports --stdin for piped input, --wait to block until a response, --timeout in milliseconds, --json structured output, and --group for sending to saved agent groups. [@claim:clm_0e00e645b8daf3e7c0235365253d43f81c750ac183df914a5e2d45b127b5df88]
- A single .ai-devkit.json config reconciles setup across supported agents, and init writes per-agent directories, skills, MCP settings, and docs/ai phase folders. [@claim:clm_627d829ba3f32cd5f2fb1ee8f98f3a4b50beeca60147ae46eb910dba740e38dc]
- A channel command bridges running agent sessions to external channels such as Telegram and Slack, with named configs, daemon mode, stop/status commands, and authorization state reporting. [@claim:clm_65f10b9848277131091a6d0d75cd9fbe28c47d48626832cfab51791beb87651f]
- Nine built-in skills are documented, anchored by dev-lifecycle, plus verify, tdd, structured-debug, memory, dev-commit, document-code, simplify-implementation, and technical-writer. [@claim:clm_7b60b6b7cdda99d008059e9a9f24816afc8d1666b19fa3be8340a70024a4f61c]
- Repository development practice: contributors clone the repo, run npm install and npm run build, and contributing guidance lives in CONTRIBUTING.md. [@claim:clm_82ca6c942a0816f17fd9de53073b1412977e5a4a343dc7888014d785c6db15fc]
- Memory stores project decisions, conventions, and fixes in a local SQLite file, exposed through MCP and CLI, with store and search commands and opt-in hybrid semantic search. [@claim:clm_9a8f9904663487a5be3c373f07749e1507fc0fae6d7139369f45947f0a87980f]
- The CLI exposes agent subcommands including agent list, agent detail, agent console, agent send, agent start, and agent rename; agent kill is documented as a console command with confirmation and tmux cleanup. [@claim:clm_b8d8bdea9e2e7023abc49bdc9d9af76e740d6d08a8d8cca6d72fededf2a7dcb4]
- The verify skill blocks completion claims without fresh test or build evidence, and dev-commit checks diffs, stages explicit paths, validates, and reports the SHA/status. [@claim:clm_d2535d283b54d38cbf9fe5aec52a1bdc128aeafca0a14b5e6e31ebec046e729d]
- The tool targets developers running multiple AI coding agents who lack a shared control surface, maintain separate per-tool config files, and have no easy way to message running sessions. [@claim:clm_e3e02f21aa765804791976a0bc11fa9767c2548d851540defd5921545cc77c9e]
- The README states the tool is not a smarter LLM, not a replacement for the coding agents it coordinates, and not a hosted service; it runs locally with no telemetry. [@claim:clm_fbce3145a3f79cf234902a7c2cb97925325c1fa916babc919920994f3e4fb541]
<!-- rcw:end owner=source:src_158e6e62fd735b4584df266d0701fe0b block=evidence -->

## Researcher notes

