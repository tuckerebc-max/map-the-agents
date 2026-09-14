---
access: public
aliases: []
claim_ids:
- clm_0e00e645b8daf3e7c0235365253d43f81c750ac183df914a5e2d45b127b5df88
- clm_115898b4e63993fc6ce3a3702d67de57cae817c78a20fbea32869a9468aab9c7
- clm_2772c2c58d9336d95b5303a312b1fea886f9babe1f6c93158b661ad5cb0f5e08
- clm_5f3b05a24633a7f9491b659c0f6302dba0c461ee673989fbe075bee9c559005a
- clm_65f10b9848277131091a6d0d75cd9fbe28c47d48626832cfab51791beb87651f
- clm_9a8f9904663487a5be3c373f07749e1507fc0fae6d7139369f45947f0a87980f
- clm_b8d8bdea9e2e7023abc49bdc9d9af76e740d6d08a8d8cca6d72fededf2a7dcb4
- clm_c6471923b7153cc2abd6cbba3d0f8ae7c683d2d7cc2304bdcc2b81ae841daf51
maturity: draft
page_id: pg_d09fe51e2ba654fe816d08c503aeb37c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4f948b178ae6567fa14b1799c11403a8
title: codeaholicguy/ai-devkit/CHANGELOG.md @ 1a3a0024eb3b
updated_at: '2026-09-14T01:42:05Z'
---

# codeaholicguy/ai-devkit/CHANGELOG.md @ 1a3a0024eb3b

<!-- rcw:begin owner=source:src_4f948b178ae6567fa14b1799c11403a8 block=evidence -->
- agent send supports --stdin for piped input, --wait to block until a response, --timeout in milliseconds, --json structured output, and --group for sending to saved agent groups. [@claim:clm_0e00e645b8daf3e7c0235365253d43f81c750ac183df914a5e2d45b127b5df88]
- The changelog records a broken release: 0.62.0 pinned @ai-devkit/agent-manager 0.32.0 while importing 0.33.0 exports, was removed from npm, and 0.62.1 repinned to 0.33.0. [@claim:clm_115898b4e63993fc6ce3a3702d67de57cae817c78a20fbea32869a9468aab9c7]
- The changelog notes better-sqlite3 was updated to 12.11.1 and @ai-devkit/memory was pinned to 0.17.0 to include a database WAL concurrency fix. [@claim:clm_2772c2c58d9336d95b5303a312b1fea886f9babe1f6c93158b661ad5cb0f5e08]
- A changelog entry reports retrieval-quality metrics for hybrid semantic memory search tuning: judged irrelevant top-3 results fell from 4.7% to 2.5% while hit@3 stayed at 97%. [@claim:clm_5f3b05a24633a7f9491b659c0f6302dba0c461ee673989fbe075bee9c559005a]
- A channel command bridges running agent sessions to external channels such as Telegram and Slack, with named configs, daemon mode, stop/status commands, and authorization state reporting. [@claim:clm_65f10b9848277131091a6d0d75cd9fbe28c47d48626832cfab51791beb87651f]
- Memory stores project decisions, conventions, and fixes in a local SQLite file, exposed through MCP and CLI, with store and search commands and opt-in hybrid semantic search. [@claim:clm_9a8f9904663487a5be3c373f07749e1507fc0fae6d7139369f45947f0a87980f]
- The CLI exposes agent subcommands including agent list, agent detail, agent console, agent send, agent start, and agent rename; agent kill is documented as a console command with confirmation and tmux cleanup. [@claim:clm_b8d8bdea9e2e7023abc49bdc9d9af76e740d6d08a8d8cca6d72fededf2a7dcb4]
- The project comprises packages including cli, agent-manager, channel-connector, and memory, which were migrated from CommonJS to ES Modules with Vitest replacing Jest. [@claim:clm_c6471923b7153cc2abd6cbba3d0f8ae7c683d2d7cc2304bdcc2b81ae841daf51]
<!-- rcw:end owner=source:src_4f948b178ae6567fa14b1799c11403a8 block=evidence -->

## Researcher notes

