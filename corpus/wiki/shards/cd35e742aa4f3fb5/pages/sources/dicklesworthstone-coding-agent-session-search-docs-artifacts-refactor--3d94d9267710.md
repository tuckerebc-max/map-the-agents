---
access: public
aliases: []
claim_ids:
- clm_109a5e847d816ce1754fcfc79c183c2be56f93f187917029de41383be3dc63c8
- clm_31043c1a5824fd53811fcc3fe206217ebee6d7bfde3ee343cfc4b9f4509e6cbf
- clm_3facd194f76ab95f5f0e27cbca895b78fe47b2eed0b2d94f9785dffd80d7b803
- clm_6b1904770a1c00dab97d68a30f68cede318cb5635112c72df6da8017d6b046a6
- clm_8fa0eab95bdd69795ce40223e6b1ed98adb29171bef9dd0c99e68945c0db22ea
- clm_bead293f6fc9391d43054144e36b96740b23bac43deb581f0af24319ca03b877
- clm_cb25b36eb2fd33a049bc4e96f740b6c7f9e258ab12b6c2124c224a2cc04dce85
maturity: draft
page_id: pg_5219f5d200005d42a4623d94d9267710
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dc1ff6b128335c42bd685531b22ad977
title: Dicklesworthstone/coding_agent_session_search/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md
  @ 6d445f64db1a
updated_at: '2026-09-14T03:46:27Z'
---

# Dicklesworthstone/coding_agent_session_search/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md @ 6d445f64db1a

<!-- rcw:begin owner=source:src_dc1ff6b128335c42bd685531b22ad977 block=evidence -->
- Hybrid search is designed to fail open to lexical results with truthful metadata, and lexical publish uses atomic swap/retention semantics that must not be bypassed. [@claim:clm_109a5e847d816ce1754fcfc79c183c2be56f93f187917029de41383be3dc63c8]
- frankensqlite-backed SQLite storage is the durable source of truth, while lexical and semantic search assets are treated as derived state rebuilt from it. [@claim:clm_31043c1a5824fd53811fcc3fe206217ebee6d7bfde3ee343cfc4b9f4509e6cbf]
- Repository development practice: AGENTS.md is authoritative for repo-local safety rules including no file deletion, no destructive git/filesystem commands, no new rusqlite, and no script-based code rewrites. [@claim:clm_3facd194f76ab95f5f0e27cbca895b78fe47b2eed0b2d94f9785dffd80d7b803]
- Repository development practice: refactor passes follow one lever per pass with one commit each, a proof card, and a fresh-eyes review prompt before closeout, while avoiding peer-dirty high-blast-radius files like indexer and storage. [@claim:clm_6b1904770a1c00dab97d68a30f68cede318cb5635112c72df6da8017d6b046a6]
- cass exposes a human/TUI surface plus a robot-mode JSON API, with stable robot JSON schemas, error kind values, and exit codes treated as user contracts. [@claim:clm_8fa0eab95bdd69795ce40223e6b1ed98adb29171bef9dd0c99e68945c0db22ea]
- New SQLite code must use frankensqlite rather than adding new rusqlite, which is described as legacy debt in the storage layer. [@claim:clm_bead293f6fc9391d43054144e36b96740b23bac43deb581f0af24319ca03b877]
- Connector modules are compatibility re-export stubs over franken_agent_detection, normalizing provider sessions into internal Conversation, Message, and Snippet types. [@claim:clm_cb25b36eb2fd33a049bc4e96f740b6c7f9e258ab12b6c2124c224a2cc04dce85]
<!-- rcw:end owner=source:src_dc1ff6b128335c42bd685531b22ad977 block=evidence -->

## Researcher notes

