---
access: public
aliases: []
claim_ids:
- clm_1cc5dc55902f1f28c0346ae05858dad6d4e21663ed4e47e2a72e20a47b38df1b
- clm_35d7c29340e9b13035ec3e61307c80be70cf44cab79619229b08e571cd3ccafe
- clm_5610ba2c29b2cf8fecd5ca977b8420b90a94d0370c1614b1ac5d85a0da92fac0
- clm_c1fd597dd809c3e5e2e51e5993826bfbf52ad2c82951888c1442286f9e1efc90
- clm_d785052957aaa61010b4e5deccb7f1ddfc93327cdb01e806ab44c95f5dcfa164
maturity: draft
page_id: pg_b32de48f11b0584ca851a492ecbdd7ef
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_824cbb48444450aba5185fbcd9b90a6a
title: winfunc/opcode/README.md @ 70c16d8a4910
updated_at: '2026-09-14T03:24:03Z'
---

# winfunc/opcode/README.md @ 70c16d8a4910

<!-- rcw:begin owner=source:src_824cbb48444450aba5185fbcd9b90a6a block=evidence -->
- The stack comprises a React 18 + TypeScript + Vite 6 frontend, a Rust backend using Tauri 2, Tailwind CSS v4 with shadcn/ui, and SQLite via rusqlite, with Bun as package manager. [@claim:clm_1cc5dc55902f1f28c0346ae05858dad6d4e21663ed4e47e2a72e20a47b38df1b]
- Building from source requires Rust 1.70.0+, Bun, Git, and the Claude Code CLI available on PATH, plus platform-specific system libraries such as webkit2gtk on Linux. [@claim:clm_35d7c29340e9b13035ec3e61307c80be70cf44cab79619229b08e571cd3ccafe]
- opcode is a desktop GUI application and toolkit for Claude Code, supporting custom agent creation, interactive session management, and background agent execution. [@claim:clm_5610ba2c29b2cf8fecd5ca977b8420b90a94d0370c1614b1ac5d85a0da92fac0]
- When creating a custom agent, users can configure permissions for file read/write and network access per agent, and agents run in separate processes. [@claim:clm_c1fd597dd809c3e5e2e51e5993826bfbf52ad2c82951888c1442286f9e1efc90]
- The Rust backend is organized into Tauri command handlers, a checkpoint module for timeline management, and a process module for process management, with a Rust test suite under src-tauri/tests. [@claim:clm_d785052957aaa61010b4e5deccb7f1ddfc93327cdb01e806ab44c95f5dcfa164]
<!-- rcw:end owner=source:src_824cbb48444450aba5185fbcd9b90a6a block=evidence -->

## Researcher notes

