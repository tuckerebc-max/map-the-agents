---
access: public
aliases: []
claim_ids:
- clm_01077bd95f6dff2feec3a2396d8944da590737a5312aff62ec5f50785e691eed
- clm_51627c3842e0f5085b67cb3544890a512f5b6647bbed0d0a9464f35578d78892
- clm_72acbffd1a6d32410dc288805c8e4ede8bab7646222e0dc41a2ef2efba246899
- clm_ab9c113c5954bb03e2290a2ce7ec20c64461245d9c2e3df2ecaa9fd154e0dd74
- clm_ae595c464dd51f5fe0ce0b2b231cd35b4324ee5ce71a751493f5d40f563d6dc0
- clm_c32d0058f9dd8d04cf91a0a334736c001b0d481f229140d11bb104e1bedb613c
- clm_cc4d92948fdf4398a4d656feb1a8270439f8ba3084c03b5fc569194bb511dee4
- clm_df5800ce8a3c67cee68026e89930bad62271c6801d37e34e003d96c398619e1b
- clm_f952c047c5e2b4a6fb59ea6560fa4877a03975e716353a6c81f3e2522a65ab84
maturity: draft
page_id: pg_445f5aec206d54ea80831ad52e42dde2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_500b51a72a6a58f19cde62da27865fe1
title: SWE-Gym/SWE-Gym/README.md @ b681068ca206
updated_at: '2026-09-14T04:24:26Z'
---

# SWE-Gym/SWE-Gym/README.md @ b681068ca206

<!-- rcw:begin owner=source:src_500b51a72a6a58f19cde62da27865fe1 block=evidence -->
- The project appears to emphasize scaling trends, stating results are bottlenecked by training and inference compute rather than environment size. [@claim:clm_01077bd95f6dff2feec3a2396d8944da590737a5312aff62ec5f50785e691eed]
- Environment constants are maintained in a separate SWE-Bench-Fork repository, and reproduction relies on forks of OpenHands and Moatless-Agent. [@claim:clm_51627c3842e0f5085b67cb3544890a512f5b6647bbed0d0a9464f35578d78892]
- The project reports baselines achieving 32%/26% on SWE-Bench Verified/Lite, described as a new open state of the art. [@claim:clm_72acbffd1a6d32410dc288805c8e4ede8bab7646222e0dc41a2ef2efba246899]
- Fine-tuning a 32B OpenHands agent on under 500 trajectories from GPT-4o and Claude 3.5 Sonnet reportedly yields +14% absolute gains on SWE-Bench Verified. [@claim:clm_ab9c113c5954bb03e2290a2ce7ec20c64461245d9c2e3df2ecaa9fd154e0dd74]
- Downstream works listed include Sky-RL (online RL improving OpenHands-7B-Agent from 11% to 14.6% SR) and OpenHands LM 32B trained with SWE-Gym reaching 37% on SWE-Bench Verified. [@claim:clm_ae595c464dd51f5fe0ce0b2b231cd35b4324ee5ce71a751493f5d40f563d6dc0]
- Verifiers trained on agent trajectories perform best-of-N selection to enable inference-time scaling alongside the learned agents. [@claim:clm_c32d0058f9dd8d04cf91a0a334736c001b0d481f229140d11bb104e1bedb613c]
- The dataset is hosted on Hugging Face under the SWE-Gym organization, and pre-built Docker images exist under the xingyaoww/sweb.eval.x86_64 prefix on Docker Hub. [@claim:clm_cc4d92948fdf4398a4d656feb1a8270439f8ba3084c03b5fc569194bb511dee4]
- SWE-Gym provides 2.4K real tasks from 11 Python repositories plus a Lite split of 234 instances, combining repository context, executable environments, and test verification. [@claim:clm_df5800ce8a3c67cee68026e89930bad62271c6801d37e34e003d96c398619e1b]
- With rejection sampling fine-tuning and the MoatlessTools scaffold, 32B and 7B models reportedly reach 20% and 10% on SWE-Bench Lite via self-improvement. [@claim:clm_f952c047c5e2b4a6fb59ea6560fa4877a03975e716353a6c81f3e2522a65ab84]
<!-- rcw:end owner=source:src_500b51a72a6a58f19cde62da27865fe1 block=evidence -->

## Researcher notes

