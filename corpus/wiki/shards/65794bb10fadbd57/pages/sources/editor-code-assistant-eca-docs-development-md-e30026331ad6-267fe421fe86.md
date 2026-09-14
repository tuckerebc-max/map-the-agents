---
access: public
aliases: []
claim_ids:
- clm_4241fbeac06d3e97c164183b8465546028cd82147fed26bbac5c926376569049
- clm_58069c3585076b2b2d16173260158378e67d1a445e64939f04dac93538e92d0d
- clm_8f7c14c99f4f427934720a2d66c6a69b3d3b1dc9f6878121068a9ad5b7f3b6d0
- clm_9bba2c9d7fbacad909f4c7adea10fc9cb6e0c9dc690ad9484c53a06d4ab0b505
- clm_c1250660aa7f98281ad294ecb84885b03eece47645ec19e5fdff809bb4499d82
- clm_cc6f81e534358cc1add6c2cfaba0c304997b1d8654e23a187fac6f7e41eb3612
- clm_dc297a72bf081d7431be1cf606dbf20e3aa81f9aca554cea28643cd311290f09
- clm_dd26149171401eb9d477820d0a500ae91440461cb0627f210095ffea76fef8f2
- clm_df94f3c9cc1b97bc1ae558e66262dfab16bb3bf7cb5251c037875bdd52f5f621
- clm_fe481f51f9018c41875141329e76601e840885d80e441d8f5022c3529712ce9c
maturity: draft
page_id: pg_810d9b7ea65f5ce9a01e267fe421fe86
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e7a8321878f35a30854832ccae1a5175
title: editor-code-assistant/eca/docs/development.md @ e30026331ad6
updated_at: '2026-09-14T01:47:30Z'
---

# editor-code-assistant/eca/docs/development.md @ e30026331ad6

<!-- rcw:begin owner=source:src_e7a8321878f35a30854832ccae1a5175 block=evidence -->
- Repository development practice: contributions are welcomed via issue discussion or pull request with developer details in the development docs, and new-editor integrations follow a UX-consistency checklist. [@claim:clm_4241fbeac06d3e97c164183b8465546028cd82147fed26bbac5c926376569049]
- The documented request flow is: client/editor → stdin JSON-RPC → handlers → features → llm_api → llm_provider, with results streamed back via messenger. [@claim:clm_58069c3585076b2b2d16173260158378e67d1a445e64939f04dac93538e92d0d]
- No evidence in this snapshot describes benchmarks or success-rate evaluation of the agent; the only test-related material is the repository's own unit and integration test suites. [@claim:clm_8f7c14c99f4f427934720a2d66c6a69b3d3b1dc9f6878121068a9ad5b7f3b6d0]
- Repository development practice: a local debug binary is built with `bb debug-cli` (requires babashka), and contributors can attach to the nREPL port printed on stderr to modify the running ECA process. [@claim:clm_9bba2c9d7fbacad909f4c7adea10fc9cb6e0c9dc690ad9484c53a06d4ab0b505]
- The project builds with Babashka tasks (bb.edn) and Clojure deps.edn including a native GraalVM image target; the server wires together via jsonrpc4clj. [@claim:clm_c1250660aa7f98281ad294ecb84885b03eece47645ec19e5fdff809bb4499d82]
- The server is written in Clojure with a layered layout: handlers.clj receives all JSON-RPC requests, db.clj holds in-memory state, llm_api.clj is the LLM facade, and llm_providers/ holds vendor adapters. [@claim:clm_cc6f81e534358cc1add6c2cfaba0c304997b1d8654e23a187fac6f7e41eb3612]
- Configuration is centralized and resolved from multiple sources: global config, local config, environment variables, and initializationOptions. [@claim:clm_dc297a72bf081d7431be1cf606dbf20e3aa81f9aca554cea28643cd311290f09]
- The new-editor checklist documents protocol methods including initialize/initialized, exit/shutdown, chat/prompt, chat/contentReceived, chat/queryContext, chat/toolCallApprove/Reject, and chat/queryCommands. [@claim:clm_dd26149171401eb9d477820d0a500ae91440461cb0627f210095ffea76fef8f2]
- All runtime state — sessions, chats, and tool servers — lives in an in-memory atom (`db*`) in db.clj. [@claim:clm_df94f3c9cc1b97bc1ae558e66262dfab16bb3bf7cb5251c037875bdd52f5f621]
- Repository development practice: contributors run unit tests with `bb test` (CI runs the same task), single namespaces via kaocha focus, and integration tests with `bb integration-test`, which spawns the server over JSON-RPC with mocked LLM and MCP servers. [@claim:clm_fe481f51f9018c41875141329e76601e840885d80e441d8f5022c3529712ce9c]
<!-- rcw:end owner=source:src_e7a8321878f35a30854832ccae1a5175 block=evidence -->

## Researcher notes

