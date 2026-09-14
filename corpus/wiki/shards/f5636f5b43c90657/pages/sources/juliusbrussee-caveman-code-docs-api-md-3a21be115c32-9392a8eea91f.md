---
access: public
aliases: []
claim_ids:
- clm_1ca907050d7156c082f0afd4f0d0b74a0b274726d6c62bca45b06ced0ed1d9a5
- clm_5c9804309248beec18da355f2a2201c50fc7c4e4c83d6b7643298be9c5aceb2e
- clm_b1005c391272f4010296e5c50b86dab123f6880cc8507a2a3974c831c0503e3a
- clm_d515a55f72ca4a610429a15ccf0dd27c1e7ba05a5d252eabe08962516671b5a4
maturity: draft
page_id: pg_beafa5cef9f45fc4af109392a8eea91f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_591d832f4fd05fcaa988d71a13635a94
title: JuliusBrussee/caveman-code/docs/api.md @ 3a21be115c32
updated_at: '2026-09-14T02:08:09Z'
---

# JuliusBrussee/caveman-code/docs/api.md @ 3a21be115c32

<!-- rcw:begin owner=source:src_591d832f4fd05fcaa988d71a13635a94 block=evidence -->
- An in-process extension API lets TypeScript modules in .cave/extensions register tools and commands and subscribe to events, with 40+ event types documented. [@claim:clm_1ca907050d7156c082f0afd4f0d0b74a0b274726d6c62bca45b06ced0ed1d9a5]
- Four programmatic surfaces are documented: a Node SDK (createAgentSession), a daemon SDK (@juliusbrussee/caveman-sdk over HTTP/WS), JSON-RPC over stdin/stdout via --mode rpc, and print/JSON output modes including --output-schema validation for CI. [@claim:clm_5c9804309248beec18da355f2a2201c50fc7c4e4c83d6b7643298be9c5aceb2e]
- The repository is described as a TypeScript monorepo of 9 packages, with the coding-agent package exporting full TypeScript types and hosting the daemon's OpenAPI 3.1 spec. [@claim:clm_b1005c391272f4010296e5c50b86dab123f6880cc8507a2a3974c831c0503e3a]
- The JSON-RPC mode accepts JSONL requests with methods such as session.create, session.prompt, session.events, session.tool.allow, session.compact, session.fork, and session.close. [@claim:clm_d515a55f72ca4a610429a15ccf0dd27c1e7ba05a5d252eabe08962516671b5a4]
<!-- rcw:end owner=source:src_591d832f4fd05fcaa988d71a13635a94 block=evidence -->

## Researcher notes

