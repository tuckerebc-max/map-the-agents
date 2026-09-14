---
access: public
aliases: []
claim_ids:
- clm_0439fe278b5f000b295c49b89f010875e5d73395fb216a5a60d5ecc760885200
- clm_47af5f31c1074fb53e676ab9da528757714a9f6a157f96390752708f51867b2f
- clm_4eb31c13b6105610e0931d75aee87361fa5b49b4650e417becc8e6fe72b56117
- clm_766686a1a7b330f1e8f970ec65f01190238bddb6f95fb6ee4a849f0269abb820
- clm_8471d28b3fc8babfa88846d5467c8eb94d234ff4466defc381217d5f026619a3
- clm_b50087df7adedc04d45031a8a88eba5e3c09c6827ac7be3b1c0d2704bbb1a532
- clm_c5639129a9e23d32896f707cc01f258322d3f8d36af5094e9587a83ae588dd84
- clm_f1fed25b9a55101fb5d39eefb74c7715133c9ba39dcea1e1b6e52d4d9569ebb6
maturity: draft
page_id: pg_e4526635cff6536ea93b52dc94dda66e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_153217620dfd5e5490a9968c1aaa3b86
title: runvendo/vendo/README.md @ 4d149938d7d3
updated_at: '2026-09-14T02:37:55Z'
---

# runvendo/vendo/README.md @ 4d149938d7d3

<!-- rcw:begin owner=source:src_153217620dfd5e5490a9968c1aaa3b86 block=evidence -->
- Vendo is an embedded agent for B2B SaaS that acts through the host product's own API as the signed-in user and renders generated UI in a sandboxed, brand-native surface without touching host source code. [@claim:clm_0439fe278b5f000b295c49b89f010875e5d73395fb216a5a60d5ecc760885200]
- Cloud-gated features (sharing, publishing, org overlays, pinning) activate with VENDO_API_KEY while the open-source blocks remain self-hosted. [@claim:clm_47af5f31c1074fb53e676ab9da528757714a9f6a157f96390752708f51867b2f]
- The npm package @vendoai/vendo is the default composition (vendoai is a thin alias), with subpath exports /core and /ui providing shared types/schemas and headless React hooks plus an in-jail component kit. [@claim:clm_4eb31c13b6105610e0931d75aee87361fa5b49b4650e417becc8e6fe72b56117]
- Policy, approvals, grants, breakers, and audit sit at one execution choke point; app machines reach host tools only through a guarded tool proxy. [@claim:clm_766686a1a7b330f1e8f970ec65f01190238bddb6f95fb6ee4a849f0269abb820]
- Generated components run in an iframe jail with connect-src 'none', escalating to a sandboxed server only when needed. [@claim:clm_8471d28b3fc8babfa88846d5467c8eb94d234ff4466defc381217d5f026619a3]
- PGlite at .vendo/data serves as the zero-config store, and production runs the same schema on Postgres. [@claim:clm_b50087df7adedc04d45031a8a88eba5e3c09c6827ac7be3b1c0d2704bbb1a532]
- Vendo runs a streaming agent that works with any AI SDK LanguageModel, and extracts the host API into tools the agent executes as the signed-in user. [@claim:clm_c5639129a9e23d32896f707cc01f258322d3f8d36af5094e9587a83ae588dd84]
- The CLI offers `vendo init` for setup and an optional `vendo doctor` checkup whose printed codes link to exact fixes; a backend package exposes `agent()` and `chat()` without mounting Vendo's CLI or UI. [@claim:clm_f1fed25b9a55101fb5d39eefb74c7715133c9ba39dcea1e1b6e52d4d9569ebb6]
<!-- rcw:end owner=source:src_153217620dfd5e5490a9968c1aaa3b86 block=evidence -->

## Researcher notes

