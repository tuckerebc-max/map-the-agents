---
access: public
aliases: []
claim_ids:
- clm_2420627bb93950f04f5d3f5322240c6668e9f8e9161a3878bf1174ea2b7f3980
- clm_5ce3ba16420e452bfac529a0b48e2c457fb4456e8dc54dc5f18261b01cc6f089
- clm_6e3691dc845547df4ee44d44d8c693cfe19c971fba524d5ccfb51c0dcff9dd02
- clm_713b9b4d15ca07423e17080b8b519178076b68a0b51a8b102d9a9ae0e54788d0
- clm_78f91e40e3c96fbcfc2341b19b081ff62f10f3bc7d04624cfc94427933bc26c9
- clm_7f36ca9e1482194b24fab4dd1b4df7bdbfbec5c6bb1ec26c275dc822d3448fa5
- clm_8c5ba1c4989f77d3eba76de6aaab63d517befb0f652840d261b5860ade31f325
- clm_9813df8558bf24e68b0de0f6b144bbb9331843a1a96edbacfc6717fbf29cb0d1
- clm_a8d80e58f3d4e58974041b790c6aee231b14469fbbbb5da1381f5241022cbce1
- clm_d83de37e3b95aae5307efb7bbb4317a9edbe3cc93dd49933f3e5a6dcb941a73f
- clm_e34a039faaf2387b92efb6c3a62dc9cf703c6ddbeb39e20639e4499339dd5c59
- clm_e7538650d16c48edc5c4685df2d79ba79a61ffce8b354085c66ce511c13a2a81
- clm_f8b477392ef4571c46d66b44366e6ed00a3029cd4ec158051d04db5cba76f9c6
- clm_fd3ed60846126e05a825e0061cf8a6a37a7bfdb462ec1bcae1b3befaedba8acb
maturity: draft
page_id: pg_65f67f1ede3852b8bd4a927bc9ccbe2c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bfa788ad2b71566eb32db98556df84b5
title: Arch1eSUN/Arcgentic/README.md @ 645c345077d7
updated_at: '2026-09-14T03:34:59Z'
---

# Arch1eSUN/Arcgentic/README.md @ 645c345077d7

<!-- rcw:begin owner=source:src_bfa788ad2b71566eb32db98556df84b5 block=evidence -->
- Role/state routing is implemented as a Topology module (toolkit/src/arcgentic/topology.py) that projects can override via project.arcgentic_v2.topology in state.yaml; custom topologies are validated at parse time and zero-config projects keep the default 5-role sequence. [@claim:clm_2420627bb93950f04f5d3f5322240c6668e9f8e9161a3878bf1174ea2b7f3980]
- Arcgentic is described as a harness engineering layer for AI coding agents, turning ad-hoc prompting into a gated engineering workflow for Codex and Claude Code. [@claim:clm_5ce3ba16420e452bfac529a0b48e2c457fb4456e8dc54dc5f18261b01cc6f089]
- The V2 workflow sequence is: idea, brainstorm/planning, round handoff, development, developer self-audit, optional user-test, external audit, pass-or-fix, then next round, next phase, or closeout. [@claim:clm_6e3691dc845547df4ee44d44d8c693cfe19c971fba524d5ccfb51c0dcff9dd02]
- Five fixed roles are defined: Orchestrator (routing/dispatch), Planner (planning and closeout decisions), Developer (building, fixes, self-audit), Test (realistic user testing when needed), and Auditor (independent PASS/NEEDS_FIX/AUDIT_INCOMPLETE review). [@claim:clm_713b9b4d15ca07423e17080b8b519178076b68a0b51a8b102d9a9ae0e54788d0]
- In multi-thread mode the Orchestrator should sleep after dispatching a role and wake only on the role's return, to avoid guessing completion or dispatching duplicate auditors. [@claim:clm_78f91e40e3c96fbcfc2341b19b081ff62f10f3bc7d04624cfc94427933bc26c9]
- For Claude Code, only single-session-subagent mode via a foreground Agent tier-0 broker dispatch has dogfood evidence; multi-session-subthread mode, the SendMessage-based retry path, ListAgents, and the hook-backed fallback path are documented as unverified. [@claim:clm_7f36ca9e1482194b24fab4dd1b4df7bdbfbec5c6bb1ec26c275dc822d3448fa5]
- An optional MCP server exposes a round_status_panel tool rendering round id, per-role dispatch progress, and latest audit verdict; the panel has no write path and falls back to a plain text summary on hosts without MCP Apps support. [@claim:clm_8c5ba1c4989f77d3eba76de6aaab63d517befb0f652840d261b5860ade31f325]
- The npm package arcgentic@2.2.0 is described as a zero-dependency plugin bundle containing skills, agents, scripts, schemas, templates, and platform manifests, while the Python CLI is published separately on PyPI. [@claim:clm_9813df8558bf24e68b0de0f6b144bbb9331843a1a96edbacfc6717fbf29cb0d1]
- Two project-level modes are offered: single-session with named role agents inside the Orchestrator session (faster, weaker audit isolation) and multi-session with fixed project threads (slower, stronger audit discipline); the choice is made once per project. [@claim:clm_a8d80e58f3d4e58974041b790c6aee231b14469fbbbb5da1381f5241022cbce1]
- In the verified Codex path, the current conversation becomes Orchestrator, which creates or reuses fixed role threads, sends role prompts, waits for return signals, and dispatches the next role without manual thread switching. [@claim:clm_d83de37e3b95aae5307efb7bbb4317a9edbe3cc93dd49933f3e5a6dcb941a73f]
- The MCP status panel is optional and installed via pip install 'arcgentic[mcp]', and it depends on host support for the MCP Apps extension. [@claim:clm_e34a039faaf2387b92efb6c3a62dc9cf703c6ddbeb39e20639e4499339dd5c59]
- Arcgentic targets frequent Codex/Claude Code users, agent builders, small AI-native teams, and complex multi-round work where AI-written code must be shown to have passed planning, testing, and audit. [@claim:clm_e7538650d16c48edc5c4685df2d79ba79a61ffce8b354085c66ce511c13a2a81]
- The README states Arcgentic is intentionally heavier than normal prompting and is not suited to one-line commands, tiny edits, quick experiments, or work where auditability does not matter. [@claim:clm_f8b477392ef4571c46d66b44366e6ed00a3029cd4ec158051d04db5cba76f9c6]
- The Auditor role returns one of three verdicts — PASS, NEEDS_FIX, or AUDIT_INCOMPLETE — and the Orchestrator routes the next step based on that outcome. [@claim:clm_fd3ed60846126e05a825e0061cf8a6a37a7bfdb462ec1bcae1b3befaedba8acb]
<!-- rcw:end owner=source:src_bfa788ad2b71566eb32db98556df84b5 block=evidence -->

## Researcher notes

