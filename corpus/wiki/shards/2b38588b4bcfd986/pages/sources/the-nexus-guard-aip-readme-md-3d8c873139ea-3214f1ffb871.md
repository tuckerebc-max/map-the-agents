---
access: public
aliases: []
claim_ids:
- clm_3715f251fceb5812b75246e44ef07b0f02bfd974d74f356d5ccfb1d01d6fbb00
- clm_612a45aec8782e67978dbf64daa8d4cb5e87536f369ad477b92e75110922e0ef
- clm_65b86f13998ec396cca9bb073d7e369a1f2960beddc417ed6699eaca8820a199
- clm_69941c125971d2e5c56fd8abb934dd0c71702f1049b279f9d40d4f9878707724
- clm_ba7db7ae40652595d077e6138ae6ac1a97d039c1984ae8a81d7d2ea32bb8af37
- clm_c7792ef0f183a74aa8ce2b5b8d55e63032db8e712c5919c3d0b2576a4cff8e02
- clm_c8161a12388fd119441499c2afc79faee98109dfed98008c618fd30f334addbe
- clm_d0a97f31febeb14bd0df7911e4774f70f7c7b41fe550626bd9992f08889f46d2
- clm_f8d132b6b3202243fe667dc83b212702ae75f1ac3c533ef13766dde48ff432aa
- clm_f99fa7e0d037e1fad8f722297072e61ca507bcc86627f8b0c7b9f99720b34b4a
maturity: draft
page_id: pg_ad1973a4aa0a535892463214f1ffb871
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_383914975aaf5cbbbb09ab19317e0008
title: The-Nexus-Guard/aip/README.md @ 3d8c873139ea
updated_at: '2026-09-14T05:10:26Z'
---

# The-Nexus-Guard/aip/README.md @ 3d8c873139ea

<!-- rcw:begin owner=source:src_383914975aaf5cbbbb09ab19317e0008 block=evidence -->
- AIP targets agent-to-agent security gaps: verifying who an agent is, deciding trustworthiness via vouch chains, signing skills for code provenance, and private messaging, including MCP and A2A protocol integrations. [@claim:clm_3715f251fceb5812b75246e44ef07b0f02bfd974d74f356d5ccfb1d01d6fbb00]
- A CLI named 'aip' exposes commands including init, register, verify, vouch, revoke, sign, message, messages, reply, rotate-key, trust-score, trust-graph, doctor, export, import, search, and cache. [@claim:clm_612a45aec8782e67978dbf64daa8d4cb5e87536f369ad477b92e75110922e0ef]
- A pure-Python implementation exists with zero dependencies; optional performance dependencies include cryptography or pynacl, and langchain-core is an optional dependency for framework tools. [@claim:clm_65b86f13998ec396cca9bb073d7e369a1f2960beddc417ed6699eaca8820a199]
- The protocol is designed to be decentralized with no central registry, local-first so each agent keeps its own trust view, and auditable via signed 'isnad' trust chains. [@claim:clm_69941c125971d2e5c56fd8abb934dd0c71702f1049b279f9d40d4f9878707724]
- Message signing uses the payload format sender_did|recipient_did|timestamp|encrypted_content; the older format without encrypted_content still works but is deprecated and slated for removal. [@claim:clm_ba7db7ae40652595d077e6138ae6ac1a97d039c1984ae8a81d7d2ea32bb8af37]
- Trust paths use decay scoring across hops (e.g., a documented example of 0.64 for two hops at 0.8 decay), and badges turn green 'Verified' at 3+ CODE_SIGNING vouches. [@claim:clm_c7792ef0f183a74aa8ce2b5b8d55e63032db8e712c5919c3d0b2576a4cff8e02]
- An identity middleware (AIPMiddleware) signs outgoing HTTP requests and verifies incoming ones, exposing trust-score-gated processing and peer discovery by minimum trust. [@claim:clm_c8161a12388fd119441499c2afc79faee98109dfed98008c618fd30f334addbe]
- The status checklist marks trust gossip protocol and reputation scoring as unchecked, indicating these are not yet implemented in v0.5.46. [@claim:clm_d0a97f31febeb14bd0df7911e4774f70f7c7b41fe550626bd9992f08889f46d2]
- AIP is organized into three layers: an identity layer (Ed25519 keypairs, DIDs, challenge-response), a trust layer (vouches, scopes, paths, revocation), and a communication layer (E2E encrypted messaging). [@claim:clm_f8d132b6b3202243fe667dc83b212702ae75f1ac3c533ef13766dde48ff432aa]
- Repository development practice: the README points contributors to a Contributing Guide and GitHub Discussions for questions and ideas. [@claim:clm_f99fa7e0d037e1fad8f722297072e61ca507bcc86627f8b0c7b9f99720b34b4a]
<!-- rcw:end owner=source:src_383914975aaf5cbbbb09ab19317e0008 block=evidence -->

## Researcher notes

