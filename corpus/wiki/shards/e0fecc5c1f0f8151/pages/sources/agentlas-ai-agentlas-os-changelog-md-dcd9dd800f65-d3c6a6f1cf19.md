---
access: public
aliases: []
claim_ids:
- clm_12f6fa3da4ddb59b4552dbced47346bb0cc58a6450921cb613cde70d2875ea69
- clm_1f10b98de5155d11144b69ac91238c3ae78e5cd5c5a0858464387a43671ac817
- clm_4ef40794cd24585f5e7f8e15fce73a70bfba12458ba45877e6deb70dc3b270c8
- clm_b03e2bd78b1b3c951fd25ea9ad0de90a81729db11484c8dcd0992a1da8d95b01
- clm_cfc3a26b6f9e516661ba43fdb0e17ce767c366278c0f59e27815ba03f0a57497
- clm_de5741d5d37e64d5d547a81429f17b6f978f3a84e9c508e4aac1b4112ac7aeb5
- clm_e83f3e96d8a6e8e8464dac596c2780de6f70e737c3ebd47d09f878e0ca7c454d
maturity: draft
page_id: pg_50aaa4696b0a5069a94cd3c6a6f1cf19
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_326298e3d3715df38d924efcac583742
title: agentlas-ai/Agentlas-OS/CHANGELOG.md @ dcd9dd800f65
updated_at: '2026-09-14T03:30:46Z'
---

# agentlas-ai/Agentlas-OS/CHANGELOG.md @ dcd9dd800f65

<!-- rcw:begin owner=source:src_326298e3d3715df38d924efcac583742 block=evidence -->
- The runtime vendors pure-Python jsonschema 4.17.3 (with attrs and pyrsistent) behind a loader that prefers a healthy installed copy, so schema validation works on Python 3.9 without the native rpds module. [@claim:clm_12f6fa3da4ddb59b4552dbced47346bb0cc58a6450921cb613cde70d2875ea69]
- The per-agent package ceiling is 10 MB transport and 2 MB per file (40 MB as authored), constrained by a 16 MiB MongoDB manifest record with base64 content. [@claim:clm_1f10b98de5155d11144b69ac91238c3ae78e5cd5c5a0858464387a43671ac817]
- The permissionPolicy schema accepts a host mode for network, shell, fileRead.mode, and mcp.mode, where the package declares no tool ceiling and the host runtime decides at execution time, emitting enforcement receipts. [@claim:clm_4ef40794cd24585f5e7f8e15fce73a70bfba12458ba45877e6deb70dc3b270c8]
- Durable memory writes go through Memory Events and Memory Tickets, and generated packages may include memory-map, memory-tickets, and vault-reference files; recall counters and semantic index state serialize read-modify-writes. [@claim:clm_b03e2bd78b1b3c951fd25ea9ad0de90a81729db11484c8dcd0992a1da8d95b01]
- Repository development practice: the packaging flow runs a Hephaestus security scan, adds .agentlas contracts, removes private or unsafe material, and verifies the package via scripts/verify-package.sh; CI contract gates such as scripts/verify-host-authority-contract.sh run in the cross-platform-wiring workflow. [@claim:clm_cfc3a26b6f9e516661ba43fdb0e17ce767c366278c0f59e27815ba03f0a57497]
- The product exposes an MCP tool agentlas_resolve_plugins and a plugins tool-search command; tool search ranks servers before tools and loads input schemas only for the chosen tool. [@claim:clm_de5741d5d37e64d5d547a81429f17b6f978f3a84e9c508e4aac1b4112ac7aeb5]
- Changelog entries report measured task performance: tool search placed the expected server in a four-candidate shortlist 5/5 times at ~209 tokens and ~3ms, and candidate menus put the right agent in the top four 97.4% of the time over 116 profiles and 389 queries. [@claim:clm_e83f3e96d8a6e8e8464dac596c2780de6f70e737c3ebd47d09f878e0ca7c454d]
<!-- rcw:end owner=source:src_326298e3d3715df38d924efcac583742 block=evidence -->

## Researcher notes

