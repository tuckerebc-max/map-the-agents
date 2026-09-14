---
access: public
aliases: []
claim_ids:
- clm_51627c3842e0f5085b67cb3544890a512f5b6647bbed0d0a9464f35578d78892
- clm_c32d0058f9dd8d04cf91a0a334736c001b0d481f229140d11bb104e1bedb613c
- clm_eac755af09aba079cce4cc1278b64a97d4c27437b1d578f89da5dca9481498f7
maturity: draft
page_id: pg_8a781a6e673050ab86babbbc5203d65e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e88529c1359657a8a8f3533f4de38498
title: SWE-Gym/SWE-Gym/docs/MoatlessTools.md @ b681068ca206
updated_at: '2026-09-14T04:24:26Z'
---

# SWE-Gym/SWE-Gym/docs/MoatlessTools.md @ b681068ca206

<!-- rcw:begin owner=source:src_e88529c1359657a8a8f3533f4de38498 block=evidence -->
- Environment constants are maintained in a separate SWE-Bench-Fork repository, and reproduction relies on forks of OpenHands and Moatless-Agent. [@claim:clm_51627c3842e0f5085b67cb3544890a512f5b6647bbed0d0a9464f35578d78892]
- Verifiers trained on agent trajectories perform best-of-N selection to enable inference-time scaling alongside the learned agents. [@claim:clm_c32d0058f9dd8d04cf91a0a334736c001b0d481f229140d11bb104e1bedb613c]
- Repository development practice: model serving uses SGLang via a Modal script that starts an OpenAI-compatible server on 4 GPUs for up to 4 hours. [@claim:clm_eac755af09aba079cce4cc1278b64a97d4c27437b1d578f89da5dca9481498f7]
<!-- rcw:end owner=source:src_e88529c1359657a8a8f3533f4de38498 block=evidence -->

## Researcher notes

