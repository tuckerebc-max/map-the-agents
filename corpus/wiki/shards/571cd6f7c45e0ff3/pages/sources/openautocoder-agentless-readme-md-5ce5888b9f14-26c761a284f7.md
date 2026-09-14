---
access: public
aliases: []
claim_ids:
- clm_26431d3167774d453f21f3f0d6cc485651a9a38155f63fccc0c05e54fae50996
- clm_499cdd9aa559cbe400f9166db0da9acd32e9a0fe92b031516658c3e5fd974644
- clm_a72d597e3d509cc7383c4a2406b18d4b5f4257f3833cd6a77c180f0d22c11895
- clm_be892d20062dc631b9474dbf2160838bd9bf9391131841f9eb34e9bdfa48f3b1
- clm_d51faede34c1415543919d2a51badad21019a37c116123e50ef0634ff8f1dfec
- clm_ea4f1685fabc66a7ba2c25042f1702330a91fd6683a34494797a0b3eab05595b
- clm_f0e5e51d052be817ae8712f42304656f921c343d5e04e1a47b9ff2117769ec16
maturity: draft
page_id: pg_6d30c7902287568794b626c761a284f7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_87037666b2445846be7bb1862de8dfb9
title: OpenAutoCoder/Agentless/README.md @ 5ce5888b9f14
updated_at: '2026-09-14T04:13:59Z'
---

# OpenAutoCoder/Agentless/README.md @ 5ce5888b9f14

<!-- rcw:begin owner=source:src_87037666b2445846be7bb1862de8dfb9 block=evidence -->
- Repair samples multiple candidate patches per bug in a simple diff format, with context windows around each edit location. [@claim:clm_26431d3167774d453f21f3f0d6cc485651a9a38155f63fccc0c05e54fae50996]
- Reported results: with Claude 3.5 Sonnet, 40.7% and 50.8% solve rates on SWE-bench Lite and Verified; v1.0 achieved 27.3% (82 fixes) on SWE-bench Lite at ~$0.34 per issue. [@claim:clm_499cdd9aa559cbe400f9166db0da9acd32e9a0fe92b031516658c3e5fd974644]
- Localization is hierarchical: faults are first localized to files, then to classes/functions, then to fine-grained edit locations. [@claim:clm_a72d597e3d509cc7383c4a2406b18d4b5f4257f3833cd6a77c180f0d22c11895]
- The tool requires an OpenAI API key exported as OPENAI_API_KEY, and requirements include openai, anthropic, tiktoken, libcst, llama-index, and the SWE-bench package. [@claim:clm_be892d20062dc631b9474dbf2160838bd9bf9391131841f9eb34e9bdfa48f3b1]
- Repository development practice: contributors are asked to install a pre-commit hook for standardized code style. [@claim:clm_d51faede34c1415543919d2a51badad21019a37c116123e50ef0634ff8f1dfec]
- Agentless solves software development issues without an agent loop, using a three-phase process: localization, repair, and patch validation. [@claim:clm_ea4f1685fabc66a7ba2c25042f1702330a91fd6683a34494797a0b3eab05595b]
- Patch validation runs selected regression tests plus generated reproduction tests, and results are used to re-rank and select the final patch. [@claim:clm_f0e5e51d052be817ae8712f42304656f921c343d5e04e1a47b9ff2117769ec16]
<!-- rcw:end owner=source:src_87037666b2445846be7bb1862de8dfb9 block=evidence -->

## Researcher notes

