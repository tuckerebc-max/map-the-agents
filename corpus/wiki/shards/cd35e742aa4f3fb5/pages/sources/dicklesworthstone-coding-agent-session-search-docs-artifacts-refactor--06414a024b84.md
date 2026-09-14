---
access: public
aliases: []
claim_ids:
- clm_31043c1a5824fd53811fcc3fe206217ebee6d7bfde3ee343cfc4b9f4509e6cbf
- clm_47d2840c083ab9007273e9a8ac1363246b97a7a7f6a3ee83c6622b7e968d66d5
- clm_8fa0eab95bdd69795ce40223e6b1ed98adb29171bef9dd0c99e68945c0db22ea
- clm_9f5b8d354985e383a29a2f959a0a64561bd323450e0fd6de1fb3cdd01a47273b
- clm_bead293f6fc9391d43054144e36b96740b23bac43deb581f0af24319ca03b877
- clm_cb25b36eb2fd33a049bc4e96f740b6c7f9e258ab12b6c2124c224a2cc04dce85
maturity: draft
page_id: pg_e4e9da081e1d566fac6b06414a024b84
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ca676734f2d35fd2a0d470ce3f5d1812
title: Dicklesworthstone/coding_agent_session_search/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md
  @ 6d445f64db1a
updated_at: '2026-09-14T03:46:27Z'
---

# Dicklesworthstone/coding_agent_session_search/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md @ 6d445f64db1a

<!-- rcw:begin owner=source:src_ca676734f2d35fd2a0d470ce3f5d1812 block=evidence -->
- frankensqlite-backed SQLite storage is the durable source of truth, while lexical and semantic search assets are treated as derived state rebuilt from it. [@claim:clm_31043c1a5824fd53811fcc3fe206217ebee6d7bfde3ee343cfc4b9f4509e6cbf]
- cass indexes local and remote coding-agent conversation histories into a unified archive and provides search across providers, with optional Tailscale-based fleet discovery wired through discovery and setup. [@claim:clm_47d2840c083ab9007273e9a8ac1363246b97a7a7f6a3ee83c6622b7e968d66d5]
- cass exposes a human/TUI surface plus a robot-mode JSON API, with stable robot JSON schemas, error kind values, and exit codes treated as user contracts. [@claim:clm_8fa0eab95bdd69795ce40223e6b1ed98adb29171bef9dd0c99e68945c0db22ea]
- The crate is organized into main.rs (entrypoint with dotenv, robot-mode detection, CLI parsing), lib.rs (Clap command surface and dispatch), connectors, indexer, storage, search, pages/html_export, analytics, and sources modules. [@claim:clm_9f5b8d354985e383a29a2f959a0a64561bd323450e0fd6de1fb3cdd01a47273b]
- New SQLite code must use frankensqlite rather than adding new rusqlite, which is described as legacy debt in the storage layer. [@claim:clm_bead293f6fc9391d43054144e36b96740b23bac43deb581f0af24319ca03b877]
- Connector modules are compatibility re-export stubs over franken_agent_detection, normalizing provider sessions into internal Conversation, Message, and Snippet types. [@claim:clm_cb25b36eb2fd33a049bc4e96f740b6c7f9e258ab12b6c2124c224a2cc04dce85]
<!-- rcw:end owner=source:src_ca676734f2d35fd2a0d470ce3f5d1812 block=evidence -->

## Researcher notes

