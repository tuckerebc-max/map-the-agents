# dicklesworthstone/coding_agent_session_search -- full detail

[Back to orientation](coding_agent_session_search.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cd35e742/aa4f3fb5/6d445f64db1a61c302afdc7d0e38137d1f192c2e/ec453b73017ae594.json](../../../wiki/dossiers/cd35e742/aa4f3fb5/6d445f64db1a61c302afdc7d0e38137d1f192c2e/ec453b73017ae594.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The crate is organized into main.rs (entrypoint with dotenv, robot-mode detection, CLI parsing), lib.rs (Clap command surface and dispatch), connectors, indexer, storage, search, pages/html_export, analytics, and sources modules. -- evidence: [docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L11-L30](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L11-L30), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L12-L21](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L12-L21) (`clm_9f5b8d354985e383a29a2f959a0a64561bd323450e0fd6de1fb3cdd01a47273b`)

## design-choices (2 claim(s))

- [observation/documented] frankensqlite-backed SQLite storage is the durable source of truth, while lexical and semantic search assets are treated as derived state rebuilt from it. -- evidence: [docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L12-L19](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L12-L19), [docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L34-L42](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L34-L42), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8) (`clm_31043c1a5824fd53811fcc3fe206217ebee6d7bfde3ee343cfc4b9f4509e6cbf`)
- [observation/documented] Hybrid search is designed to fail open to lexical results with truthful metadata, and lexical publish uses atomic swap/retention semantics that must not be bypassed. -- evidence: [docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L12-L19](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L12-L19) (`clm_109a5e847d816ce1754fcfc79c183c2be56f93f187917029de41383be3dc63c8`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md is authoritative for repo-local safety rules including no file deletion, no destructive git/filesystem commands, no new rusqlite, and no script-based code rewrites. -- evidence: [docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8) (`clm_3facd194f76ab95f5f0e27cbca895b78fe47b2eed0b2d94f9785dffd80d7b803`)
- [observation/documented] Repository development practice: refactor passes follow one lever per pass with one commit each, a proof card, and a fresh-eyes review prompt before closeout, while avoiding peer-dirty high-blast-radius files like indexer and storage. -- evidence: [docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L32-L34](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L32-L34), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L25-L28](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L25-L28), [docs/artifacts/refactor-runs/20260425T180745Z-fourth-simplify/architecture.md#L3-L7](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T180745Z-fourth-simplify/architecture.md#L3-L7) (`clm_6b1904770a1c00dab97d68a30f68cede318cb5635112c72df6da8017d6b046a6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] cass exposes a human/TUI surface plus a robot-mode JSON API, with stable robot JSON schemas, error kind values, and exit codes treated as user contracts. -- evidence: [docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26), [docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L46-L55](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L46-L55), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8) (`clm_8fa0eab95bdd69795ce40223e6b1ed98adb29171bef9dd0c99e68945c0db22ea`)
- [observation/documented] Connector modules are compatibility re-export stubs over franken_agent_detection, normalizing provider sessions into internal Conversation, Message, and Snippet types. -- evidence: [docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L12-L19](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L12-L19), [docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L11-L30](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L11-L30) (`clm_cb25b36eb2fd33a049bc4e96f740b6c7f9e258ab12b6c2124c224a2cc04dce85`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] New SQLite code must use frankensqlite rather than adding new rusqlite, which is described as legacy debt in the storage layer. -- evidence: [docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L11-L30](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L11-L30), [docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T024205Z-second-simplify/architecture.md#L22-L26), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8) (`clm_bead293f6fc9391d43054144e36b96740b23bac43deb581f0af24319ca03b877`)
- [observation/documented] The changelog research records published FAD dependency 0.2.4, crossbeam-channel 0.5.17, asupersync 0.4.11 as a pending candidate, and final engine/search versions 0.3.18 and 0.4.3. -- evidence: [CHANGELOG_RESEARCH.md#L3-L16](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L3-L16), [CHANGELOG_RESEARCH.md#L561-L566](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L561-L566) (`clm_a3d99482ea732b2f6038dd8b9f46604b671ea0af4db8c8c5392cc23f06dee88b`)

## limitations (2 claim(s))

- [observation/documented] The strict UBS scanner gate repeatedly remained red, with Rust module timeouts at 300 seconds and various critical/warning findings left unresolved and unsuppressed. -- evidence: [CHANGELOG_RESEARCH.md#L280-L289](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L280-L289), [CHANGELOG_RESEARCH.md#L35-L44](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L35-L44), [CHANGELOG_RESEARCH.md#L224-L239](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L224-L239), [CHANGELOG_RESEARCH.md#L410-L430](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L410-L430) (`clm_e7fb4b4f974ffe82f73bba6f06b353327d19e17f0a8747fd3b619408a2cdc2cb`)
- [observation/documented] Default hybrid search matched lexical results without a model download, so neural semantic retrieval and archive-scale performance were not validated by the live SSH harness. -- evidence: [CHANGELOG_RESEARCH.md#L306-L313](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L306-L313) (`clm_978bca506c757231bcf6baf148816908a69e9524dff3d276c14adfdfff789d80`)

## relevance (1 claim(s))

- [observation/documented] cass indexes local and remote coding-agent conversation histories into a unified archive and provides search across providers, with optional Tailscale-based fleet discovery wired through discovery and setup. -- evidence: [CHANGELOG_RESEARCH.md#L261-L268](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/CHANGELOG_RESEARCH.md#L261-L268), [docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L5-L7](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T184600Z-fifth-simplify/architecture.md#L5-L7), [docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8](https://github.com/Dicklesworthstone/coding_agent_session_search/blob/6d445f64db1a61c302afdc7d0e38137d1f192c2e/docs/artifacts/refactor-runs/20260425T154730Z-third-simplify/architecture.md#L7-L8) (`clm_47d2840c083ab9007273e9a8ac1363246b97a7a7f6a3ee83c6622b7e968d66d5`)

