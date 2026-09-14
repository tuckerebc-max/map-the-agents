---
access: public
aliases: []
claim_ids:
- clm_76fa19e420250ca5f943589b6273de2b3d3684a1b472083a6f3b004453f33ef5
- clm_cff985d61b758b2344aa0323b0cb397543f9d8073f2d81a081e6098355905b0f
- clm_ea9c87f62f69143d57dcc344525ea199b1ccebc69180d9a16862e411c4a17fbf
- clm_ef0faa80a8e793e4a990e7f2c0b49b8d50b6bcaebb6586f9942ad35cc03f4318
maturity: draft
page_id: pg_b9a495d18ad55318baa4eca659cf7d8c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_25f9af1c0dcd587f85e08e09bdf8f74d
title: XMUDeepLIT/LegalGraphRAG/docs/TABLE2_REPRODUCTION.md @ a3c9c3070cad
updated_at: '2026-09-14T04:33:00Z'
---

# XMUDeepLIT/LegalGraphRAG/docs/TABLE2_REPRODUCTION.md @ a3c9c3070cad

<!-- rcw:begin owner=source:src_25f9af1c0dcd587f85e08e09bdf8f74d block=evidence -->
- Baseline systems such as HippoRAG2, RAPTOR, LightRAG, LegalDelta, and ADAPT are not included in the repository; their outputs can be compared externally if converted to the same result schema. [@claim:clm_76fa19e420250ca5f943589b6273de2b3d3684a1b472083a6f3b004453f33ef5]
- As a regression check, evaluating the archived Table 2 Qwen3 CMDL output yields Accuracy 0.5756914119359534 and Micro-F1 0.617426820966644. [@claim:clm_cff985d61b758b2344aa0323b0cb397543f9d8073f2d81a081e6098355905b0f]
- The evaluator accepts current judge_result.charge_name predictions and the legacy Table 2 judge_res[].crime format; each CMDL defendant row is scored once, giving judgment_count 1,374. [@claim:clm_ea9c87f62f69143d57dcc344525ea199b1ccebc69180d9a16862e411c4a17fbf]
- The main retrieval corpus combines 3,512 CAIL test, 5,752 JuDGE, and 4,785 CMDL cases with sequential IDs, and a small amount of LeCaRDv2 data was incorporated as untagged supplementary material. [@claim:clm_ef0faa80a8e793e4a990e7f2c0b49b8d50b6bcaebb6586f9942ad35cc03f4318]
<!-- rcw:end owner=source:src_25f9af1c0dcd587f85e08e09bdf8f74d block=evidence -->

## Researcher notes

