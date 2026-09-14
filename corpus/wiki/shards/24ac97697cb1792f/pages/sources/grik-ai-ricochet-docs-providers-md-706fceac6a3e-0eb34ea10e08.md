---
access: public
aliases: []
claim_ids:
- clm_ae259f0f6629bb262002a103b911fce02ebdd158956a6207286d5e8d18681726
- clm_ead285506ba680e3171df101134a24d06cb3c80fcf8a9a477ef343ae7682f146
maturity: draft
page_id: pg_333fb06676bb57e1a95a0eb34ea10e08
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e50a76b4e34a58bb958088e4d52d7b3e
title: Grik-ai/ricochet/docs/providers.md @ 706fceac6a3e
updated_at: '2026-09-14T01:52:28Z'
---

# Grik-ai/ricochet/docs/providers.md @ 706fceac6a3e

<!-- rcw:begin owner=source:src_e50a76b4e34a58bb958088e4d52d7b3e block=evidence -->
- BYOK provider keys are stored locally (user settings, OS secret store, or environment variables), and the Go core resolves catalog placeholders from the user's environment or local configuration at runtime. [@claim:clm_ae259f0f6629bb262002a103b911fce02ebdd158956a6207286d5e8d18681726]
- The public provider catalog lives at core/config/providers.yaml and contains model metadata and environment-variable placeholders such as key: "${OPENROUTER_API_KEY}". [@claim:clm_ead285506ba680e3171df101134a24d06cb3c80fcf8a9a477ef343ae7682f146]
<!-- rcw:end owner=source:src_e50a76b4e34a58bb958088e4d52d7b3e block=evidence -->

## Researcher notes

