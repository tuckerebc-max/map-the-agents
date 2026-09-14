---
access: public
aliases: []
claim_ids:
- clm_05c7220d696492261aabbc848875da9f160633de7f67e8e88bd6844d2857e757
- clm_0a459826bd51137c6203a8929641ebb3fd3262bfadd38512c897a16a36458eba
- clm_9e908bb8989964a439f8341c3f587d050c804d465c68b6da9f49dfa1a2e610cf
maturity: draft
page_id: pg_99fda1fa64345f2ea89cbc2601ad4d1e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8b43e12dd1f95bac9d91e3d59667a199
title: ochyai/vibe-local/RELEASE_NOTES.md @ 5ea328e201c1
updated_at: '2026-09-14T03:10:50Z'
---

# ochyai/vibe-local/RELEASE_NOTES.md @ 5ea328e201c1

<!-- rcw:begin owner=source:src_8b43e12dd1f95bac9d91e3d59667a199 block=evidence -->
- Repository development practice: release notes report 780 unit tests plus 7 PTY integration tests (787 total) for vibe-coder.py, stated to pass on macOS, Linux, and Windows WSL. [@claim:clm_05c7220d696492261aabbc848875da9f160633de7f67e8e88bd6844d2857e757]
- The TUI uses a VT100 DECSTBM scroll region so AI output scrolls above a fixed three-row footer, with a store-only update pattern, non-blocking resize locking, and single-syscall atomic writes. [@claim:clm_0a459826bd51137c6203a8929641ebb3fd3262bfadd38512c897a16a36458eba]
- An optional built-in Python engine, vibe-coder.py, is dependency-free (stdlib only), talks directly to Ollama's /api/chat with a tool-execution loop, and can run standalone via python3. [@claim:clm_9e908bb8989964a439f8341c3f587d050c804d465c68b6da9f49dfa1a2e610cf]
<!-- rcw:end owner=source:src_8b43e12dd1f95bac9d91e3d59667a199 block=evidence -->

## Researcher notes

