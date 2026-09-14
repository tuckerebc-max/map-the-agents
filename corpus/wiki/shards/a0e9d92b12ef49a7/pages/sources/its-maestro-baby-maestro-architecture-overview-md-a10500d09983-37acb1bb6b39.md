---
access: public
aliases: []
claim_ids:
- clm_039bd1db609224cd2a16193080f49bd8d77b87d9aa9efb44dbbfd4d55a1fc7d8
- clm_26603713113acd85c431057d86988577713fe8d6e8ebfcff966d31b8076ffadf
- clm_f3e7c9bb07fec59fcbe24ebca9d4300675180b39d3ad6b9b222c822cef23db56
maturity: draft
page_id: pg_7352b09220545efca75937acb1bb6b39
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3e46076c523e52e5a1f9eb050b13b3dc
title: its-maestro-baby/maestro/ARCHITECTURE-OVERVIEW.md @ a10500d09983
updated_at: '2026-09-14T02:06:00Z'
---

# its-maestro-baby/maestro/ARCHITECTURE-OVERVIEW.md @ a10500d09983

<!-- rcw:begin owner=source:src_3e46076c523e52e5a1f9eb050b13b3dc block=evidence -->
- Key frontend dependencies include @tauri-apps/api ^2.10.1, @xterm/xterm ^5.5.0, react ^18.3.0, zustand ^5.0.10, and tailwindcss ^3.4.0; the backend uses Tauri 2.0, tokio, serde, and DashMap. [@claim:clm_039bd1db609224cd2a16193080f49bd8d77b87d9aa9efb44dbbfd4d55a1fc7d8]
- Frontend state is organized into Zustand stores including useGitHubStore, useGitStore, useWorkspaceStore, useSessionStore, useMarketplaceStore, and useMcpStore. [@claim:clm_26603713113acd85c431057d86988577713fe8d6e8ebfcff966d31b8076ffadf]
- The Rust backend has command handlers for git, worktrees, GitHub, marketplace, MCP, sessions, terminals, updates, and usage, plus core modules for process, plugin, worktree, and session management. [@claim:clm_f3e7c9bb07fec59fcbe24ebca9d4300675180b39d3ad6b9b222c822cef23db56]
<!-- rcw:end owner=source:src_3e46076c523e52e5a1f9eb050b13b3dc block=evidence -->

## Researcher notes

