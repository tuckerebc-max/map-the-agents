---
access: public
aliases: []
claim_ids:
- clm_0f1e88d9415ec6b2d0616a43280d7272405aa1f7576f16e94b28cb3d9693e390
- clm_e3c8564315e97072da76ec1060ae5787e419f95951e990ee9227b682c88cf140
maturity: draft
page_id: pg_0a3eb4b7cc8c5b32b71580cb3831d907
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4217d20861fd5d6f9d601c3900f19bde
title: xingyaoww/code-act/docs/MODEL_TRAINING.md @ d607f56c9cfe
updated_at: '2026-09-14T04:59:21Z'
---

# xingyaoww/code-act/docs/MODEL_TRAINING.md @ d607f56c9cfe

<!-- rcw:begin owner=source:src_4217d20861fd5d6f9d601c3900f19bde block=evidence -->
- Repository development practice: training data is converted to Megatron format with ChatML chat templating and sequence packing (e.g., 78k instances packed into 19k sequences), and checkpoints can be converted back to HuggingFace format with a ChatML chat_template added. [@claim:clm_0f1e88d9415ec6b2d0616a43280d7272405aa1f7576f16e94b28cb3d9693e390]
- Repository development practice: reproducing the released models involves cloning submodules, optionally generating CodeActInstruct trajectories via the MINT framework in Docker, and training with a forked Megatron-LLM using provided 4xA100 scripts or SLURM job files. [@claim:clm_e3c8564315e97072da76ec1060ae5787e419f95951e990ee9227b682c88cf140]
<!-- rcw:end owner=source:src_4217d20861fd5d6f9d601c3900f19bde block=evidence -->

## Researcher notes

