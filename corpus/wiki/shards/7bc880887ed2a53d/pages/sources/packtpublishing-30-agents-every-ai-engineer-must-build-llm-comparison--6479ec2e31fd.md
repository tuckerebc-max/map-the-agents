---
access: public
aliases: []
claim_ids:
- clm_5aae5dbfae7e8a4b86700d84d8d4ad7234f1c196fb26a8c1127643784d251657
- clm_9c200ff1d124a1fbb2cc9780e8a34fc34505fb26b8a215ca1955d968066ddc1e
- clm_b28146f8d94733d0b082dba93642eedef168f04fd46152f622bf74709cd60486
- clm_b9dce0875e4c48132add211b4b48f2df1a66780671df0c199513aea3ce910484
maturity: draft
page_id: pg_aa090e4f33135eb381536479ec2e31fd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_15258b7c59b555fd84de6364a8a6cbe7
title: PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/LLM_COMPARISON_SUMMARY.md
  @ bb19628dd41f
updated_at: '2026-09-14T04:15:30Z'
---

# PacktPublishing/30-Agents-Every-AI-Engineer-Must-Build/LLM_COMPARISON_SUMMARY.md @ bb19628dd41f

<!-- rcw:begin owner=source:src_15258b7c59b555fd84de6364a8a6cbe7 block=evidence -->
- The comparison's honesty notes state that 11 of 17 chapters produce identical outputs regardless of provider due to deterministic pipelines or shared mock frameworks, and some providers fell back to MockLLM because of API format bugs in shared llm_call() functions rather than model limitations. [@claim:clm_5aae5dbfae7e8a4b86700d84d8d4ad7234f1c196fb26a8c1127643784d251657]
- The comparison concludes no single provider wins overall: GPT-4o and local DeepSeek each won 3 chapters, Claude Sonnet 4 and Gemini Flash 2.5 one each, with 8 chapters tied as deterministic and 1 with no winner. [@claim:clm_9c200ff1d124a1fbb2cc9780e8a34fc34505fb26b8a215ca1955d968066ddc1e]
- Claude Sonnet 4 has no outputs for chapters 9, 10, 14, and 15, which the document says limits head-to-head comparison. [@claim:clm_b28146f8d94733d0b082dba93642eedef168f04fd46152f622bf74709cd60486]
- A book-wide comparison scored four providers 0-10 per chapter across eight dimensions (including factual accuracy, source grounding, and Bloom's level), based on 68 notebook executions with live API keys in April 2026. [@claim:clm_b9dce0875e4c48132add211b4b48f2df1a66780671df0c199513aea3ce910484]
<!-- rcw:end owner=source:src_15258b7c59b555fd84de6364a8a6cbe7 block=evidence -->

## Researcher notes

