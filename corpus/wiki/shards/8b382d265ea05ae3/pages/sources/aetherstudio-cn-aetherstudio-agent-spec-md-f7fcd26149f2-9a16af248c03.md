---
access: public
aliases: []
claim_ids:
- clm_41018fc6304a989dcee919a9cb64b0045cfb80858b43d3f097c3a7dd71f52338
- clm_43366760b3184d893c2923802d1e949bb19867412af520144e55020e081102fc
- clm_e566c9e832b219f65dc74af7cf2cd5281569e30f38e2a488a3b9d42023ad8bd7
- clm_f6f3af944d23d376866c241ba1daf64e9b58315403c9d90eabd1f47c3c05de1b
maturity: draft
page_id: pg_99e03084d133578680ee9a16af248c03
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d1676137d63651adb39a2a6da77daa21
title: aetherstudio-cn/AetherStudio/AGENT_SPEC.md @ f7fcd26149f2
updated_at: '2026-09-14T01:29:58Z'
---

# aetherstudio-cn/AetherStudio/AGENT_SPEC.md @ f7fcd26149f2

<!-- rcw:begin owner=source:src_d1676137d63651adb39a2a6da77daa21 block=evidence -->
- AGENT_SPEC.md records that aether-ai, aether-shared, and aether-terminal crates were missing (directories present but empty) at spec time, and plans an AiClient with a complete(prompt) async method plus an AppSettings struct covering AI, UI, and remote settings. [@claim:clm_41018fc6304a989dcee919a9cb64b0045cfb80858b43d3f097c3a7dd71f52338]
- AGENT_SPEC.md lists non-goals: no new LSP/DAP features, no new plugin-system features, no additional localization, and no cloud sync or collaborative editing. [@claim:clm_43366760b3184d893c2923802d1e949bb19867412af520144e55020e081102fc]
- The product currently targets only Windows 10 1809+ and Windows 11; AGENT_SPEC.md also notes the build environment lacked a Rust toolchain, so code correctness had to be ensured without compile verification. [@claim:clm_e566c9e832b219f65dc74af7cf2cd5281569e30f38e2a488a3b9d42023ad8bd7]
- AGENT_SPEC.md sets goals of production-grade Git support, SSH remote connections, Acrylic/glass UI, 60fps rendering with sub-16ms input latency, and configurable LLM API keys (OpenAI, Claude, Kimi). [@claim:clm_f6f3af944d23d376866c241ba1daf64e9b58315403c9d90eabd1f47c3c05de1b]
<!-- rcw:end owner=source:src_d1676137d63651adb39a2a6da77daa21 block=evidence -->

## Researcher notes

