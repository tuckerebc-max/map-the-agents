---
access: public
aliases: []
claim_ids:
- clm_376099eb2fa171100dac3317388f18fab5152e87e26810640d556d1922020fd6
- clm_57b809944a359776734d03d2bbbb759fc21d290e7a2e7b28ba5bbd6c329c68e4
- clm_6b33ceec78816b1cfa5d71d9c8ce81748b124806bb367d73cd2cfb76e85e1021
- clm_7ba89c6aa92eb70aae21bb18e99cff662b735a79e569a55605d289b638b9dfae
- clm_d1a68de2df1a07a21139e916e87ef6ebf5ff8c4101bddf20cd02a5e7cf8461a8
- clm_d88f3a9f14892bc2275e3735c81cd9a84822a72a430a22d173b36d7402513227
- clm_df7a80fa8f76bee3f90dde48a76a7570bf3ca2b7e8736c617b2851f454236131
- clm_e600e51cf5eff6e022fe34badd64dbec88875b281c301479f40b88920882e042
- clm_fa0114844b315731b5b1bd9e994af92220b4e63e7a89de114c4f74af8bdd97b9
maturity: draft
page_id: pg_e72e0566e2ac53f6a67b6f3ba182f78d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b4107762eeff58f7816e174fdf76b855
title: kristoferlund/duet-gpt/README.md @ 6e28904075b5
updated_at: '2026-09-14T02:09:41Z'
---

# kristoferlund/duet-gpt/README.md @ 6e28904075b5

<!-- rcw:begin owner=source:src_b4107762eeff58f7816e174fdf76b855 block=evidence -->
- DuetGPT is an experimental AI-powered CLI tool and semi-autonomous agent that helps developers with coding and file system tasks. [@claim:clm_376099eb2fa171100dac3317388f18fab5152e87e26810640d556d1922020fd6]
- A changelog entry indicates AI assistant responses are added to memory, and the sample interaction shows 'LLM and memory started' at launch. [@claim:clm_57b809944a359776734d03d2bbbb759fc21d290e7a2e7b28ba5bbd6c329c68e4]
- Example tasks include refactoring code, writing bash scripts, searching files for text, and drafting PR descriptions from commit messages; it is also described as a general bash helper. [@claim:clm_6b33ceec78816b1cfa5d71d9c8ce81748b124806bb367d73cd2cfb76e85e1021]
- The approval step before command execution appears to be the product's core safety mechanism, since the README describes automatic execution only after developer approval. [@claim:clm_7ba89c6aa92eb70aae21bb18e99cff662b735a79e569a55605d289b638b9dfae]
- Installed globally via npm as duet-gpt and started with the duet-gpt command; on first run it prompts for an OpenAI API key. [@claim:clm_d1a68de2df1a07a21139e916e87ef6ebf5ff8c4101bddf20cd02a5e7cf8461a8]
- The project no longer uses langchain, relying instead on OpenAI function calling, which the author says improved reliability and performance. [@claim:clm_d88f3a9f14892bc2275e3735c81cd9a84822a72a430a22d173b36d7402513227]
- Works with OpenAI models gpt-3.5-turbo-0613 (noted as not producing great code) and gpt-4-0613. [@claim:clm_df7a80fa8f76bee3f90dde48a76a7570bf3ca2b7e8736c617b2851f454236131]
- The developer describes a task; the AI issues commands or follow-up questions, and after developer approval DuetGPT automatically executes the commands. [@claim:clm_e600e51cf5eff6e022fe34badd64dbec88875b281c301479f40b88920882e042]
- Known issue: when proposing changes to large files the AI may return incomplete results due to the limited gpt-4 context window; it works best with small files. [@claim:clm_fa0114844b315731b5b1bd9e994af92220b4e63e7a89de114c4f74af8bdd97b9]
<!-- rcw:end owner=source:src_b4107762eeff58f7816e174fdf76b855 block=evidence -->

## Researcher notes

