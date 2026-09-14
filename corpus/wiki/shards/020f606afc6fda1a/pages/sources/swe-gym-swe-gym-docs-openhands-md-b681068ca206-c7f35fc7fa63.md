---
access: public
aliases: []
claim_ids:
- clm_2df5ec0eb257056d2be96fe20f7b7af7e8ce60c9b14a9e298549815c21932d1b
- clm_51627c3842e0f5085b67cb3544890a512f5b6647bbed0d0a9464f35578d78892
- clm_80b7aceaab9a85ebb3edd412c47fb671d00b8263dddd4333bd0834014c7f3ce5
- clm_b8b1da1205fd8b208b17ca531dcbd7b45a3b579db25207dd2ef005d7a834ef61
- clm_eac755af09aba079cce4cc1278b64a97d4c27437b1d578f89da5dca9481498f7
- clm_f70a496e3e20a647be21fc83852c83871350c649f335982e105355665afb041f
maturity: draft
page_id: pg_8771b4543ca853ca8f94c7f35fc7fa63
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4c0833f76ad95207a63ed25b67b89576
title: SWE-Gym/SWE-Gym/docs/OpenHands.md @ b681068ca206
updated_at: '2026-09-14T04:24:26Z'
---

# SWE-Gym/SWE-Gym/docs/OpenHands.md @ b681068ca206

<!-- rcw:begin owner=source:src_4c0833f76ad95207a63ed25b67b89576 block=evidence -->
- Repository development practice: the verifier is trained with unsloth on one GPU via a Modal script, with torchtune verifier configs also provided. [@claim:clm_2df5ec0eb257056d2be96fe20f7b7af7e8ce60c9b14a9e298549815c21932d1b]
- Environment constants are maintained in a separate SWE-Bench-Fork repository, and reproduction relies on forks of OpenHands and Moatless-Agent. [@claim:clm_51627c3842e0f5085b67cb3544890a512f5b6647bbed0d0a9464f35578d78892]
- The docs note results were obtained with a specific OpenHands fork and that notable performance differences are expected with the latest OpenHands version. [@claim:clm_80b7aceaab9a85ebb3edd412c47fb671d00b8263dddd4333bd0834014c7f3ce5]
- Repository development practice: policy training uses Modal with torchtune full-parameter fine-tuning (N_GPUS=8) on a Qwen2.5-Coder-32B config, with SFT trajectories downloaded from Hugging Face. [@claim:clm_b8b1da1205fd8b208b17ca531dcbd7b45a3b579db25207dd2ef005d7a834ef61]
- Repository development practice: model serving uses SGLang via a Modal script that starts an OpenAI-compatible server on 4 GPUs for up to 4 hours. [@claim:clm_eac755af09aba079cce4cc1278b64a97d4c27437b1d578f89da5dca9481498f7]
- Repository development practice: docs instruct cloning the SWE-Gym OpenHands fork, configuring models via config.toml, exporting ALLHANDS_API_KEY for RemoteRuntime, and running rollout and eval scripts. [@claim:clm_f70a496e3e20a647be21fc83852c83871350c649f335982e105355665afb041f]
<!-- rcw:end owner=source:src_4c0833f76ad95207a63ed25b67b89576 block=evidence -->

## Researcher notes

