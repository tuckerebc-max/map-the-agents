---
access: public
aliases: []
claim_ids:
- clm_05a07e1178e8c5e7d9ded916316bfc503229a19baf78017ffda9dd363ecdfea1
- clm_3c30ecddfee0b9a69b8e49f97128fd9594ff50b02f46c6d6d1942bdcc9975751
- clm_53e4b08c3ca90b122284cbbf1ff159126de02cb17b279e4880d5a17d22b48c19
- clm_699d4bde830e954b2e3c8af759257034d25781422d9e591e222b18c6a0dc934f
- clm_808c47044ffa994cf6887b5978fb0bc576968d4b56b9190a6fd00e1889727a7a
- clm_8b08a05cf45d14ccc99b06a37c22da5d09aa63970b0f2b0f29c7c5440b2ef0af
maturity: draft
page_id: pg_2a139bb2a01157e5a9596b9eeda2d665
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_32790870da7a505c80a1053a62d8cf2f
title: agent-of-empires/agent-of-empires/README.md @ bdf21c256673
updated_at: '2026-09-14T03:30:42Z'
---

# agent-of-empires/agent-of-empires/README.md @ bdf21c256673

<!-- rcw:begin owner=source:src_32790870da7a505c80a1053a62d8cf2f block=evidence -->
- Repository development practice: the README's Development section lists cargo build, cargo test, cargo fmt, cargo clippy, and cargo build --features web, with docs/development.md as the full reference. [@claim:clm_05a07e1178e8c5e7d9ded916316bfc503229a19baf78017ffda9dd363ecdfea1]
- The product exposes TUI, web, CLI, and HTTP API surfaces, with status detection, notifications, persistent tmux sessions, git worktrees, multi-repo workspaces, and Docker/Podman/Apple Containers sandboxing. [@claim:clm_3c30ecddfee0b9a69b8e49f97128fd9594ff50b02f46c6d6d1942bdcc9975751]
- AoE is described as a session manager for AI coding agents on Linux and macOS, running agents in parallel across branches with persistent sessions and optional worktree or container isolation. [@claim:clm_53e4b08c3ca90b122284cbbf1ff159126de02cb17b279e4880d5a17d22b48c19]
- tmux is a required prerequisite and Docker is optional for sandboxing; the project is built with cargo, and native Windows is unsupported because AoE depends on tmux and POSIX process handling (WSL2 only). [@claim:clm_699d4bde830e954b2e3c8af759257034d25781422d9e591e222b18c6a0dc934f]
- Each agent runs in its own tmux session, so sessions persist when the TUI closes, SSH disconnects, or the terminal crashes; sessions are only removed when explicitly deleted. [@claim:clm_808c47044ffa994cf6887b5978fb0bc576968d4b56b9190a6fd00e1889727a7a]
- The project is MIT licensed, with one file (src/tui/hyperlink.rs) containing code derived from the herdr project under Apache License 2.0. [@claim:clm_8b08a05cf45d14ccc99b06a37c22da5d09aa63970b0f2b0f29c7c5440b2ef0af]
<!-- rcw:end owner=source:src_32790870da7a505c80a1053a62d8cf2f block=evidence -->

## Researcher notes

