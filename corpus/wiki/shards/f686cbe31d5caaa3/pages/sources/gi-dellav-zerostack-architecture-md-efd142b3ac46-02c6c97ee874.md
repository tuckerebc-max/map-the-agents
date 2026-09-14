---
access: public
aliases: []
claim_ids:
- clm_086f898a17059924faa1d4771f665f96c4e2a3db45584d5cd2c852d64355e6bb
- clm_554651672dc1cb2fea8824f44ec80296b586c644f10a545663483beb814a18fd
- clm_99ae4ebf9a0c929a178f2b2f2ec7bc5c3d90e96c7c94d0b7aedbee71df455c15
- clm_a87e4289fb44c49fd9feb8892a2c8f7a5123517cecd82802b2d23e074e6dfee9
- clm_f5b1127ab69be0b28108aab81240fb1b93d4b9994be2eab2961f9e7d421f4238
maturity: draft
page_id: pg_f165efd6f6b552a4876c02c6c97ee874
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4686454d9b635fd19cf9705fc971d56a
title: gi-dellav/zerostack/ARCHITECTURE.md @ efd142b3ac46
updated_at: '2026-09-14T01:51:09Z'
---

# gi-dellav/zerostack/ARCHITECTURE.md @ efd142b3ac46

<!-- rcw:begin owner=source:src_4686454d9b635fd19cf9705fc971d56a block=evidence -->
- The project is a single Rust crate with source under src/, including agent, session, permission, ui, context, and config modules; the TUI is custom on crossterm without ratatui. [@claim:clm_086f898a17059924faa1d4771f665f96c4e2a3db45584d5cd2c852d64355e6bb]
- Core dependencies include rig 0.39, clap 4, crossterm 0.29, tokio, serde, pulldown-cmark, regex, reqwest, and mimalloc; optional features add rmcp (MCP) and agent-client-protocol (ACP). [@claim:clm_554651672dc1cb2fea8824f44ec80296b586c644f10a545663483beb814a18fd]
- Sessions are saved as JSON under $XDG_DATA_HOME/zerostack/sessions/ and can be resumed with -c, -r, or --session <id>; auto-compaction summarizes old messages near the context-window limit. [@claim:clm_99ae4ebf9a0c929a178f2b2f2ec7bc5c3d90e96c7c94d0b7aedbee71df455c15]
- Provider abstraction uses type-erased enums (AnyClient/AnyModel/AnyAgent) instead of trait objects, and tokio runs single-threaded by default unless the multithread feature is enabled. [@claim:clm_a87e4289fb44c49fd9feb8892a2c8f7a5123517cecd82802b2d23e074e6dfee9]
- Repository development practice: unit tests live in src/tests/ and headless TUI-loop integration tests drive the real loop with a FakeBackend and mock agent models, without a terminal or network. [@claim:clm_f5b1127ab69be0b28108aab81240fb1b93d4b9994be2eab2961f9e7d421f4238]
<!-- rcw:end owner=source:src_4686454d9b635fd19cf9705fc971d56a block=evidence -->

## Researcher notes

