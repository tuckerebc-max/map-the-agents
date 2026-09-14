---
access: public
aliases: []
claim_ids:
- clm_1d420df65fb5faf82007fa72f2259b0162051296301856c51f473b188d73b4ee
- clm_270696d65805383ec97ef3c7814e31ec64b6b883df3b13e64def131e237f870e
- clm_348d2201733e5695078f30a40b91ddafa25cf0cd2b2e0e7d87ac019012ff9b96
- clm_527cef466feb87996281312d8fba7dd5282bf122bbcd45f59b202a367e63e0c3
- clm_5ed679f2e3751906f4447a3da39fcd759fca00470c005f58ce48157e09f8fb21
- clm_6dc5efe24d6c7f87c67060a7435ab98d951335969ae7f7e09b193b4d8c77b5ee
- clm_d8073d6887fd543270ac5fc17e391f6154679e4a3bb9390a7be34bc512635444
- clm_df2769309b4444b276236564b419700a85cde2a56aa5b21b4954b96582998b69
- clm_f170c7f8620d525fa3b69b90323ac4653aa4e10ee719e0d73995ee1b1e7814fe
maturity: draft
page_id: pg_5ab77cba061655a4ac8310e1007c93e9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b88739974450536385313501a8bc2262
title: cactus-compute/needle/README.md @ 956840ff176b
updated_at: '2026-09-14T03:40:37Z'
---

# cactus-compute/needle/README.md @ 956840ff176b

<!-- rcw:begin owner=source:src_b88739974450536385313501a8bc2262 block=evidence -->
- The repository is the Python package cactus-needle covering inference, LoRA fine-tuning, and export; the inference engine is fetched once from Hugging Face and cached. [@claim:clm_1d420df65fb5faf82007fa72f2259b0162051296301856c51f473b188d73b4ee]
- Every response carries a calibrated confidence score from a learned head, defined as the minimum of a post-hoc head score and the decoding probability of the call tokens; users set a threshold and escalate below it. [@claim:clm_270696d65805383ec97ef3c7814e31ec64b6b883df3b13e64def131e237f870e]
- The documented fine-tuning workflow is: optionally synthesize data via needle generate-data (needs OPENROUTER_API_KEY), LoRA fine-tune with needle finetune (defaults epochs 3, lora-rank 16, lr 1e-4), then merge and quantize with needle build into a .cact archive. [@claim:clm_348d2201733e5695078f30a40b91ddafa25cf0cd2b2e0e7d87ac019012ff9b96]
- The model is said to be compressed to CQ2-bit via Cactus Quants and built on the Simple Attention Network findings, baked into its own engine. [@claim:clm_527cef466feb87996281312d8fba7dd5282bf122bbcd45f59b202a367e63e0c3]
- Needle 2 is described as an open 45M-parameter model for tool calling, device use and structured extraction, shipped as a single 14MB binary that runs a session in about 28MB of RAM. [@claim:clm_5ed679f2e3751906f4447a3da39fcd759fca00470c005f58ce48157e09f8fb21]
- The runtime install excludes training; fine-tuning and export need the [train] extra (JAX, imported lazily), with [train,gpu] for CUDA and [train,metal] for Apple Silicon; Pydantic is used for typed extraction. [@claim:clm_6dc5efe24d6c7f87c67060a7435ab98d951335969ae7f7e09b193b4d8c77b5ee]
- Tool calls are constrained by a byte-level grammar compiled from the declared schemas, so output is structured JSON and cannot be malformed; the reasoning field is generated unconstrained. [@claim:clm_d8073d6887fd543270ac5fc17e391f6154679e4a3bb9390a7be34bc512635444]
- The runtime uses a 256-token sliding window with tools pinned as KV sinks, which the README says keeps total memory near 28MB regardless of conversation length. [@claim:clm_df2769309b4444b276236564b419700a85cde2a56aa5b21b4954b96582998b69]
- For catalogues above five tools, a built-in contrastive retrieval head embeds schemas at init and renders only the top five tools per turn, rebuilding the grammar over that subset. [@claim:clm_f170c7f8620d525fa3b69b90323ac4653aa4e10ee719e0d73995ee1b1e7814fe]
<!-- rcw:end owner=source:src_b88739974450536385313501a8bc2262 block=evidence -->

## Researcher notes

