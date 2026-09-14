---
access: public
aliases: []
claim_ids:
- clm_343e4a063e6081fd5573b2f5f1c60e6573398ec21db5860274d87aef4aecbac7
- clm_357c787f72ec9f8643146ba754680d5fe9c262c996f95ce0ed67be5910ace9a8
- clm_83bbf83f043afe56f460a5fbfff429d2431be07c2e2b9543f12d89ff5366201a
- clm_8dc8aecfab573f92199621de441a22961d79b3f5f571affc8c2de10711d98420
- clm_8dd84f5bd01fbe557570566361b745db9fa9c30cc8470f57990825892fd4fc86
- clm_9247e38aeafdcac56ad862f87a6b2a007648cff57e911193c9abe00e4aba06a3
- clm_a1a9b07908cbf11b42acb8181063dab2f31c39add148e38b04094ce7464f918d
- clm_a835415e02ad16f0407f9e24caddc775f9b1eec121875e7db2508c41299ad028
- clm_b4ece05db271e7b785e8b76c07d13d0091a61cd39da34f92b9e556f52a692644
- clm_c12ac87655548397741ee5fc5c9baac9ba426fe75d7a8e39cb34b900f06fa78b
- clm_da8a421c9a09af8d21dbd6faaccee8c984b7ecd6ca1ce6e462151baabec59d33
- clm_dd5445f844f24db32a3917fbdf18a87fd44c5a61d21b0c02d09f8bc5132a30c4
- clm_f521cd83e367f14d3a34e0ebeb3692f4484f505c6e32694f982fbbaf2f9d03e6
- clm_f8ac1291ee794115efac84357687950f4dd3dde948b22397438743a5f574f24e
maturity: draft
page_id: pg_12a50712245e554a9b3330f78b4fc49c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1a415f8d2a32571a93cdadc5310d1391
title: avelikiy/great_cto/README.md @ 5ca5a322ac7a
updated_at: '2026-09-14T01:36:37Z'
---

# avelikiy/great_cto/README.md @ 5ca5a322ac7a

<!-- rcw:begin owner=source:src_1a415f8d2a32571a93cdadc5310d1391 block=evidence -->
- The tool is positioned for a solo builder, is not a CI/CD system (gates run locally, merging still goes through GitHub Actions), and is not certification-audited despite PCI/HIPAA/SOC2 scaffolds. [@claim:clm_343e4a063e6081fd5573b2f5f1c60e6573398ec21db5860274d87aef4aecbac7]
- The product follows a rule that a thing which did not happen must never look like one that did: missing harnesses show 'unavailable', undecidable checks show 'unverifiable', unmeasured costs show 'unmeasured', and unassessed stages show 'null'. [@claim:clm_357c787f72ec9f8643146ba754680d5fe9c262c996f95ce0ed67be5910ace9a8]
- An open benchmark built seven products with a median token cost of $171 and a median quality score of 70/100 (range 58-86), measured 2026-07-10, with a reproduction doc cited. [@claim:clm_83bbf83f043afe56f460a5fbfff429d2431be07c2e2b9543f12d89ff5366201a]
- An 'approval-level' setting in .great_cto/PROJECT.md controls where the pipeline stops, from 'auto' (0 stops) through the default 'gates-only' (3 stops) to 'ship-only' (1 stop at deploy). [@claim:clm_8dc8aecfab573f92199621de441a22961d79b3f5f571affc8c2de10711d98420]
- The system uses about 70 specialized agents with their own review gates, plus critics for architecture, spec, and schema that run before planning. [@claim:clm_8dd84f5bd01fbe557570566361b745db9fa9c30cc8470f57990825892fd4fc86]
- Per-agent budgets in PROJECT.md ('agent-budgets:') make the pipeline decline to dispatch past a stage's spending cap and name the number; unmeasured runs hold nothing rather than firing a budget. [@claim:clm_9247e38aeafdcac56ad862f87a6b2a007648cff57e911193c9abe00e4aba06a3]
- The tool installs via 'npx great-cto init', with an '--host codex' variant that installs skills and an MCP server instead of the Claude Code pipeline. [@claim:clm_a1a9b07908cbf11b42acb8181063dab2f31c39add148e38b04094ce7464f918d]
- Requires Node >= 18.17; companion plugins Superpowers and Beads install automatically, and users are told to verify the plugin loaded via 'claude plugin list --json'. [@claim:clm_a835415e02ad16f0407f9e24caddc775f9b1eec121875e7db2508c41299ad028]
- Agents are scope-restricted at write time: an agent is described as physically unable to touch files outside its brief, refused at write rather than flagged at review. [@claim:clm_b4ece05db271e7b785e8b76c07d13d0091a61cd39da34f92b9e556f52a692644]
- Per-agent cost attribution is unreliable: cost is read from the host's session transcript, which covers the session rather than one subagent, so per-agent figures can be inflated and should be treated as a ceiling. [@claim:clm_c12ac87655548397741ee5fc5c9baac9ba426fe75d7a8e39cb34b900f06fa78b]
- Users interact via slash commands: /start to describe a product or feature and run the pipeline, /inbox for pending gates and blocked tasks, and /digest for weekly DORA metrics and cost roll-ups. [@claim:clm_da8a421c9a09af8d21dbd6faaccee8c984b7ecd6ca1ce6e462151baabec59d33]
- On Codex the pipeline does not run: hooks, slash commands, the gate chain and secret-scan are unavailable there because the host lacks a plugin surface for them; only skills and the MCP server work. [@claim:clm_dd5445f844f24db32a3917fbdf18a87fd44c5a61d21b0c02d09f8bc5132a30c4]
- Decisions, lessons, and promoted patterns persist per project and globally across sessions, and an interrupted run resumes knowing which stages already ran. [@claim:clm_f521cd83e367f14d3a34e0ebeb3692f4484f505c6e32694f982fbbaf2f9d03e6]
- A web board at localhost:3141 shows Decisions, Ledger (costs), Fleet, and Harness screens, and renders never-run scans as 'n/a' rather than a green zero. [@claim:clm_f8ac1291ee794115efac84357687950f4dd3dde948b22397438743a5f574f24e]
<!-- rcw:end owner=source:src_1a415f8d2a32571a93cdadc5310d1391 block=evidence -->

## Researcher notes

