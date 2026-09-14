---
access: public
aliases: []
claim_ids:
- clm_442dced50544ec622ef145569cd890b475db488f5e73e638f0da868f00303bfd
- clm_565971245ff9a52f6c3edf00baa303577f04f73907e3bcb6b6b51354d0d65c05
- clm_853994d3d623d71cfcd6c590acc385a91da44914187cfbe43bafd3eb277775d0
- clm_a692fdea4dd38903f37de5e42ef443834dcde85f71b13e14394778f048ecfa44
- clm_b03e2bd78b1b3c951fd25ea9ad0de90a81729db11484c8dcd0992a1da8d95b01
maturity: draft
page_id: pg_2ac8d82cc73a514fb3f8b4d80fe4323e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_16f684c1c31258ac9dd4e99f8556f1bf
title: agentlas-ai/Agentlas-OS/agent.md @ dcd9dd800f65
updated_at: '2026-09-14T03:30:46Z'
---

# agentlas-ai/Agentlas-OS/agent.md @ dcd9dd800f65

<!-- rcw:begin owner=source:src_16f684c1c31258ac9dd4e99f8556f1bf block=evidence -->
- Inputs include a user goal plus optional target project path, repository, ZIP, prompt, existing agent, runtime requirements, and a public/private boundary. [@claim:clm_442dced50544ec622ef145569cd890b475db488f5e73e638f0da868f00303bfd]
- Outputs include a selected mode, a canonical AGENTS.md, .agentlas contract files, thin runtime adapters for Codex, Claude Code, Gemini CLI, and Cursor, a global command registry, and interview/research/eval artifacts. [@claim:clm_565971245ff9a52f6c3edf00baa303577f04f73907e3bcb6b6b51354d0d65c05]
- Four core builders are defined: single-agent-builder, multi-agent-team-builder, agentlas-packager, and session-agent-builder, each with a distinct role such as converting exported sessions into reviewed reusable candidates. [@claim:clm_853994d3d623d71cfcd6c590acc385a91da44914187cfbe43bafd3eb277775d0]
- The agent's mission is to route rough agent, team, or package requests to the right core builder and produce a portable Agentlas-compatible package. [@claim:clm_a692fdea4dd38903f37de5e42ef443834dcde85f71b13e14394778f048ecfa44]
- Durable memory writes go through Memory Events and Memory Tickets, and generated packages may include memory-map, memory-tickets, and vault-reference files; recall counters and semantic index state serialize read-modify-writes. [@claim:clm_b03e2bd78b1b3c951fd25ea9ad0de90a81729db11484c8dcd0992a1da8d95b01]
<!-- rcw:end owner=source:src_16f684c1c31258ac9dd4e99f8556f1bf block=evidence -->

## Researcher notes

