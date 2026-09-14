---
access: public
aliases: []
claim_ids:
- clm_4241fbeac06d3e97c164183b8465546028cd82147fed26bbac5c926376569049
- clm_5c6b83246d050c5a920f328a5e560024391d0bf578276efe022c78151e4d191e
- clm_bcaa4dd7944a227363f2f5b75e98e84d92c9f50f8b84ff41ee7bdb5f209112e4
- clm_cc6f81e534358cc1add6c2cfaba0c304997b1d8654e23a187fac6f7e41eb3612
- clm_dbf5003be61d4eb18234969493881dc5e366c687a57e421a870f21f14719789a
maturity: draft
page_id: pg_07dfcd4b262550ae8df3412369f19ae0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_458988914bc75d8787fca99800aeaaa1
title: editor-code-assistant/eca/README.md @ e30026331ad6
updated_at: '2026-09-14T01:47:30Z'
---

# editor-code-assistant/eca/README.md @ e30026331ad6

<!-- rcw:begin owner=source:src_458988914bc75d8787fca99800aeaaa1 block=evidence -->
- Repository development practice: contributions are welcomed via issue discussion or pull request with developer details in the development docs, and new-editor integrations follow a UX-consistency checklist. [@claim:clm_4241fbeac06d3e97c164183b8465546028cd82147fed26bbac5c926376569049]
- ECA supports configuring multiple agents/subagents, each with different models, tools, and behaviors. [@claim:clm_5c6b83246d050c5a920f328a5e560024391d0bf578276efe022c78151e4d191e]
- Editors spawn the server via `eca server` and communicate over stdin/stdout using a JSON-RPC protocol inspired by LSP, so any editor can integrate. [@claim:clm_bcaa4dd7944a227363f2f5b75e98e84d92c9f50f8b84ff41ee7bdb5f209112e4]
- The server is written in Clojure with a layered layout: handlers.clj receives all JSON-RPC requests, db.clj holds in-memory state, llm_api.clj is the LLM facade, and llm_providers/ holds vendor adapters. [@claim:clm_cc6f81e534358cc1add6c2cfaba0c304997b1d8654e23a187fac6f7e41eb3612]
- ECA places a server between editors and LLMs to centralize tool-call management, multi-LLM interaction, telemetry, and a single configuration shared across editors. [@claim:clm_dbf5003be61d4eb18234969493881dc5e366c687a57e421a870f21f14719789a]
<!-- rcw:end owner=source:src_458988914bc75d8787fca99800aeaaa1 block=evidence -->

## Researcher notes

