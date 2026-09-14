---
access: public
aliases: []
claim_ids:
- clm_09b5fddd434153c0becee974b4945ee1ea9e124eb6fb9f96e71f05f38c1efbb5
- clm_afe52be53242a691c9958a7c95729c1cc094e4ea2ff2b8a45e2b42147c40f3e8
- clm_b4cca94010c68f4a00f99b87b5a5728f695746469b1192ce87afe3d94729b8f9
maturity: draft
page_id: pg_a73ad972f0215db0827367fa09b48649
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_140adfe1143e551ab910113e52e41a7e
title: alibaba/open-code-review/CONTRIBUTING.ja-JP.md @ 494bf1c8d7a1
updated_at: '2026-09-14T01:59:22Z'
---

# alibaba/open-code-review/CONTRIBUTING.ja-JP.md @ 494bf1c8d7a1

<!-- rcw:begin owner=source:src_140adfe1143e551ab910113e52e41a7e block=evidence -->
- Repository development practice: PRs must be focused on one logical change, include tests for behavior changes, update docs when user-facing behavior changes, pass all CI checks, and every contributor must sign the Alibaba CLA before merge. [@claim:clm_09b5fddd434153c0becee974b4945ee1ea9e124eb6fb9f96e71f05f38c1efbb5]
- Repository development practice: AI-assisted contributions must be disclosed early, contributors must understand and be able to explain all AI-generated code, AI/LLM may only be used for translation or prose polishing of replies, and 'Assisted-by'/'Co-developed-by' trailers are prohibited. [@claim:clm_afe52be53242a691c9958a7c95729c1cc094e4ea2ff2b8a45e2b42147c40f3e8]
- The repository layout includes cmd/opencodereview (CLI entry), internal packages for agent, config, diff parsing, LLM clients (Anthropic & OpenAI), session, tool, telemetry (OpenTelemetry), and viewer, plus a pages/ WebUI frontend. [@claim:clm_b4cca94010c68f4a00f99b87b5a5728f695746469b1192ce87afe3d94729b8f9]
<!-- rcw:end owner=source:src_140adfe1143e551ab910113e52e41a7e block=evidence -->

## Researcher notes

