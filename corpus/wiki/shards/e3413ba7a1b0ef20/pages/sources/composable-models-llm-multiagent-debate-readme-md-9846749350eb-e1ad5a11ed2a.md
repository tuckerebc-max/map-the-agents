---
access: public
aliases: []
claim_ids:
- clm_11baeaae672ee54036db2c0b8542e601a36de7c3074b13584bab5fe738415b03
- clm_22444835d11faf8ffb8f19dda5ba5f8748177023a40395279ec1b3be33c0236a
- clm_4b475c9de024e71a72e9284553605942b02d56047a32dd7025651b8a4cd1b41b
- clm_89f602a850c2b4130f53212036cad093da57506ce8adee6811212e4b4824f014
- clm_a4e6c19ef2d944ad051d237165fc9443e7f4ebb8e6e326fefc1ca43546b84790
- clm_cdde99fe7d15a7a5e7ffe04ab793464378d2c2ea3e02af6a0ca1b2028d8d525f
- clm_fcedf510b3af498c2e246b727cb4e41951891943445becf8c4966f75e32948f6
maturity: draft
page_id: pg_5b88f526275052219115e1ad5a11ed2a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1b656fe7150d57019aeecb69e8810145
title: composable-models/llm_multiagent_debate/README.md @ 9846749350eb
updated_at: '2026-09-14T03:41:49Z'
---

# composable-models/llm_multiagent_debate/README.md @ 9846749350eb

<!-- rcw:begin owner=source:src_1b656fe7150d57019aeecb69e8810145 block=evidence -->
- The README notes this is a preliminary implementation and that additional debate logs are hosted externally on Dropbox. [@claim:clm_11baeaae672ee54036db2c0b8542e601a36de7c3074b13584bab5fe738415b03]
- Each task is run via a generation script (e.g. gen_math.py, gen_gsm.py, gen_conversation.py, gen_mmlu.py) executed from its task directory. [@claim:clm_22444835d11faf8ffb8f19dda5ba5f8748177023a40395279ec1b3be33c0236a]
- The GSM and MMLU datasets are external, with links to the openai/grade-school-math and hendrycks/test repositories for download. [@claim:clm_4b475c9de024e71a72e9284553605942b02d56047a32dd7025651b8a4cd1b41b]
- The repo contains four task subfolders: ./math, ./gsm, ./biography, and ./mmlu, each holding code for running its respective task. [@claim:clm_89f602a850c2b4130f53212036cad093da57506ce8adee6811212e4b4824f014]
- The repository is described as a preliminary implementation of the paper 'Improving Factuality and Reasoning in Language Models through Multiagent Debate', with more tasks and settings to be released. [@claim:clm_a4e6c19ef2d944ad051d237165fc9443e7f4ebb8e6e326fefc1ca43546b84790]
- Separate evaluation scripts exist per task: eval_gsm.py, eval_conversation.py, and eval_mmlu.py evaluate the generated results of GSM, biography, and MMLU problems respectively. [@claim:clm_cdde99fe7d15a7a5e7ffe04ab793464378d2c2ea3e02af6a0ca1b2028d8d525f]
- The work is associated with authors Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch, with a project page and arXiv paper (2305.14325). [@claim:clm_fcedf510b3af498c2e246b727cb4e41951891943445becf8c4966f75e32948f6]
<!-- rcw:end owner=source:src_1b656fe7150d57019aeecb69e8810145 block=evidence -->

## Researcher notes

