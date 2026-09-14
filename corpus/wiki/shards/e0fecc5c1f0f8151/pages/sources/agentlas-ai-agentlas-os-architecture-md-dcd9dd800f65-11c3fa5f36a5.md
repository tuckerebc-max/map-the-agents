---
access: public
aliases: []
claim_ids:
- clm_853994d3d623d71cfcd6c590acc385a91da44914187cfbe43bafd3eb277775d0
- clm_8ba789e4b0a265eff1258280f6a1a982b75ce1600c398ea38b9c7503fe567b2d
- clm_aeff2315f8bf0a924fca0e1220adbbc736bd641789ba8815dec3caa00c7f961f
- clm_b03e2bd78b1b3c951fd25ea9ad0de90a81729db11484c8dcd0992a1da8d95b01
- clm_cfc3a26b6f9e516661ba43fdb0e17ce767c366278c0f59e27815ba03f0a57497
maturity: draft
page_id: pg_266822f49bc9558bb57411c3fa5f36a5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2ca20015af8a527db871f54fd644d739
title: agentlas-ai/Agentlas-OS/ARCHITECTURE.md @ dcd9dd800f65
updated_at: '2026-09-14T03:30:46Z'
---

# agentlas-ai/Agentlas-OS/ARCHITECTURE.md @ dcd9dd800f65

<!-- rcw:begin owner=source:src_2ca20015af8a527db871f54fd644d739 block=evidence -->
- Four core builders are defined: single-agent-builder, multi-agent-team-builder, agentlas-packager, and session-agent-builder, each with a distinct role such as converting exported sessions into reviewed reusable candidates. [@claim:clm_853994d3d623d71cfcd6c590acc385a91da44914187cfbe43bafd3eb277775d0]
- The canonical core is runtime-neutral, with adapters translating the same core into each runtime and adapters instructed not to contain private logic missing from the canonical core. [@claim:clm_8ba789e4b0a265eff1258280f6a1a982b75ce1600c398ea38b9c7503fe567b2d]
- Runtime adapter surfaces include codex/marketplace.json, .claude/commands, GEMINI.md files, a root AGENTS.md for generic tools, and a bin/ontology CLI for local-first storage/search/graph/memory. [@claim:clm_aeff2315f8bf0a924fca0e1220adbbc736bd641789ba8815dec3caa00c7f961f]
- Durable memory writes go through Memory Events and Memory Tickets, and generated packages may include memory-map, memory-tickets, and vault-reference files; recall counters and semantic index state serialize read-modify-writes. [@claim:clm_b03e2bd78b1b3c951fd25ea9ad0de90a81729db11484c8dcd0992a1da8d95b01]
- Repository development practice: the packaging flow runs a Hephaestus security scan, adds .agentlas contracts, removes private or unsafe material, and verifies the package via scripts/verify-package.sh; CI contract gates such as scripts/verify-host-authority-contract.sh run in the cross-platform-wiring workflow. [@claim:clm_cfc3a26b6f9e516661ba43fdb0e17ce767c366278c0f59e27815ba03f0a57497]
<!-- rcw:end owner=source:src_2ca20015af8a527db871f54fd644d739 block=evidence -->

## Researcher notes

