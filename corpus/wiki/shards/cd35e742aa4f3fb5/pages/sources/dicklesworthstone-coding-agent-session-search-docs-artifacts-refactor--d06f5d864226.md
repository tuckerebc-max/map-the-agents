---
access: public
aliases: []
claim_ids:
- clm_31043c1a5824fd53811fcc3fe206217ebee6d7bfde3ee343cfc4b9f4509e6cbf
- clm_3facd194f76ab95f5f0e27cbca895b78fe47b2eed0b2d94f9785dffd80d7b803
- clm_47d2840c083ab9007273e9a8ac1363246b97a7a7f6a3ee83c6622b7e968d66d5
- clm_6b1904770a1c00dab97d68a30f68cede318cb5635112c72df6da8017d6b046a6
- clm_8fa0eab95bdd69795ce40223e6b1ed98adb29171bef9dd0c99e68945c0db22ea
- clm_9f5b8d354985e383a29a2f959a0a64561bd323450e0fd6de1fb3cdd01a47273b
- clm_bead293f6fc9391d43054144e36b96740b23bac43deb581f0af24319ca03b877
maturity: draft
page_id: pg_fb56470732445f60b5a9d06f5d864226
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_acb276c9802f50e8b4be84a7b6dcfb6b
title: Dicklesworthstone/coding_agent_session_search/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md
  @ 6d445f64db1a
updated_at: '2026-09-14T03:46:27Z'
---

# Dicklesworthstone/coding_agent_session_search/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md @ 6d445f64db1a

<!-- rcw:begin owner=source:src_acb276c9802f50e8b4be84a7b6dcfb6b block=evidence -->
- frankensqlite-backed SQLite storage is the durable source of truth, while lexical and semantic search assets are treated as derived state rebuilt from it. [@claim:clm_31043c1a5824fd53811fcc3fe206217ebee6d7bfde3ee343cfc4b9f4509e6cbf]
- Repository development practice: AGENTS.md is authoritative for repo-local safety rules including no file deletion, no destructive git/filesystem commands, no new rusqlite, and no script-based code rewrites. [@claim:clm_3facd194f76ab95f5f0e27cbca895b78fe47b2eed0b2d94f9785dffd80d7b803]
- cass indexes local and remote coding-agent conversation histories into a unified archive and provides search across providers, with optional Tailscale-based fleet discovery wired through discovery and setup. [@claim:clm_47d2840c083ab9007273e9a8ac1363246b97a7a7f6a3ee83c6622b7e968d66d5]
- Repository development practice: refactor passes follow one lever per pass with one commit each, a proof card, and a fresh-eyes review prompt before closeout, while avoiding peer-dirty high-blast-radius files like indexer and storage. [@claim:clm_6b1904770a1c00dab97d68a30f68cede318cb5635112c72df6da8017d6b046a6]
- cass exposes a human/TUI surface plus a robot-mode JSON API, with stable robot JSON schemas, error kind values, and exit codes treated as user contracts. [@claim:clm_8fa0eab95bdd69795ce40223e6b1ed98adb29171bef9dd0c99e68945c0db22ea]
- The crate is organized into main.rs (entrypoint with dotenv, robot-mode detection, CLI parsing), lib.rs (Clap command surface and dispatch), connectors, indexer, storage, search, pages/html_export, analytics, and sources modules. [@claim:clm_9f5b8d354985e383a29a2f959a0a64561bd323450e0fd6de1fb3cdd01a47273b]
- New SQLite code must use frankensqlite rather than adding new rusqlite, which is described as legacy debt in the storage layer. [@claim:clm_bead293f6fc9391d43054144e36b96740b23bac43deb581f0af24319ca03b877]
<!-- rcw:end owner=source:src_acb276c9802f50e8b4be84a7b6dcfb6b block=evidence -->

## Researcher notes

