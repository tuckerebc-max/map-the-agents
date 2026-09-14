# swe-gym/swe-gym -- full detail

[Back to orientation](swe-gym.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/swe-gym/swe-gym/b681068ca20628c6987b7416cc4cf03f06b77ba5/be525b8e3fa4d1c5.json](../../../wiki/dossiers/swe-gym/swe-gym/b681068ca20628c6987b7416cc4cf03f06b77ba5/be525b8e3fa4d1c5.json)

## specifications (1 claim(s))

- [observation/documented] SWE-Gym provides 2.4K real tasks from 11 Python repositories plus a Lite split of 234 instances, combining repository context, executable environments, and test verification. -- evidence: [README.md#L44-L44](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L44-L44) (`clm_df5800ce8a3c67cee68026e89930bad62271c6801d37e34e003d96c398619e1b`)

## components (1 claim(s))

- [observation/documented] Verifiers trained on agent trajectories perform best-of-N selection to enable inference-time scaling alongside the learned agents. -- evidence: [docs/MoatlessTools.md#L21-L21](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/MoatlessTools.md#L21-L21), [README.md#L68-L69](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L68-L69) (`clm_c32d0058f9dd8d04cf91a0a334736c001b0d481f229140d11bb104e1bedb613c`)

## design-choices (1 claim(s))

- [inference/documented] The project appears to emphasize scaling trends, stating results are bottlenecked by training and inference compute rather than environment size. -- evidence: [README.md#L39-L40](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L39-L40), [README.md#L81-L81](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L81-L81) (`clm_01077bd95f6dff2feec3a2396d8944da590737a5312aff62ec5f50785e691eed`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: docs instruct cloning the SWE-Gym OpenHands fork, configuring models via config.toml, exporting ALLHANDS_API_KEY for RemoteRuntime, and running rollout and eval scripts. -- evidence: [docs/OpenHands.md#L72-L74](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L72-L74), [docs/OpenHands.md#L8-L11](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L8-L11), [docs/OpenHands.md#L47-L47](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L47-L47), [docs/OpenHands.md#L55-L55](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L55-L55), [docs/OpenHands.md#L20-L20](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L20-L20), [docs/OpenHands.md#L60-L60](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L60-L60) (`clm_f70a496e3e20a647be21fc83852c83871350c649f335982e105355665afb041f`)
- [observation/documented] Repository development practice: policy training uses Modal with torchtune full-parameter fine-tuning (N_GPUS=8) on a Qwen2.5-Coder-32B config, with SFT trajectories downloaded from Hugging Face. -- evidence: [docs/OpenHands.md#L90-L90](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L90-L90), [docs/OpenHands.md#L96-L96](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L96-L96), [docs/OpenHands.md#L92-L92](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L92-L92), [docs/OpenHands.md#L94-L94](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L94-L94) (`clm_b8b1da1205fd8b208b17ca531dcbd7b45a3b579db25207dd2ef005d7a834ef61`)
- [observation/documented] Repository development practice: the verifier is trained with unsloth on one GPU via a Modal script, with torchtune verifier configs also provided. -- evidence: [docs/OpenHands.md#L104-L104](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L104-L104) (`clm_2df5ec0eb257056d2be96fe20f7b7af7e8ce60c9b14a9e298549815c21932d1b`)
- [observation/documented] Repository development practice: model serving uses SGLang via a Modal script that starts an OpenAI-compatible server on 4 GPUs for up to 4 hours. -- evidence: [docs/OpenHands.md#L111-L113](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L111-L113), [docs/MoatlessTools.md#L16-L17](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/MoatlessTools.md#L16-L17), [docs/OpenHands.md#L108-L109](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L108-L109) (`clm_eac755af09aba079cce4cc1278b64a97d4c27437b1d578f89da5dca9481498f7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (3 claim(s))

- [observation/documented] The project reports baselines achieving 32%/26% on SWE-Bench Verified/Lite, described as a new open state of the art. -- evidence: [README.md#L68-L69](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L68-L69), [README.md#L36-L37](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L36-L37) (`clm_72acbffd1a6d32410dc288805c8e4ede8bab7646222e0dc41a2ef2efba246899`)
- [observation/documented] Fine-tuning a 32B OpenHands agent on under 500 trajectories from GPT-4o and Claude 3.5 Sonnet reportedly yields +14% absolute gains on SWE-Bench Verified. -- evidence: [README.md#L51-L51](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L51-L51) (`clm_ab9c113c5954bb03e2290a2ce7ec20c64461245d9c2e3df2ecaa9fd154e0dd74`)
- [observation/documented] With rejection sampling fine-tuning and the MoatlessTools scaffold, 32B and 7B models reportedly reach 20% and 10% on SWE-Bench Lite via self-improvement. -- evidence: [README.md#L58-L58](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L58-L58) (`clm_f952c047c5e2b4a6fb59ea6560fa4877a03975e716353a6c81f3e2522a65ab84`)

## dependencies (2 claim(s))

- [observation/documented] The dataset is hosted on Hugging Face under the SWE-Gym organization, and pre-built Docker images exist under the xingyaoww/sweb.eval.x86_64 prefix on Docker Hub. -- evidence: [README.md#L88-L88](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L88-L88), [README.md#L92-L92](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L92-L92) (`clm_cc4d92948fdf4398a4d656feb1a8270439f8ba3084c03b5fc569194bb511dee4`)
- [observation/documented] Environment constants are maintained in a separate SWE-Bench-Fork repository, and reproduction relies on forks of OpenHands and Moatless-Agent. -- evidence: [README.md#L90-L90](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L90-L90), [docs/OpenHands.md#L8-L11](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L8-L11), [docs/MoatlessTools.md#L8-L10](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/MoatlessTools.md#L8-L10) (`clm_51627c3842e0f5085b67cb3544890a512f5b6647bbed0d0a9464f35578d78892`)

## limitations (1 claim(s))

- [observation/documented] The docs note results were obtained with a specific OpenHands fork and that notable performance differences are expected with the latest OpenHands version. -- evidence: [docs/OpenHands.md#L8-L11](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L8-L11) (`clm_80b7aceaab9a85ebb3edd412c47fb671d00b8263dddd4333bd0834014c7f3ce5`)

## relevance (1 claim(s))

- [observation/documented] Downstream works listed include Sky-RL (online RL improving OpenHands-7B-Agent from 11% to 14.6% SR) and OpenHands LM 32B trained with SWE-Gym reaching 37% on SWE-Bench Verified. -- evidence: [README.md#L101-L103](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L101-L103) (`clm_ae595c464dd51f5fe0ce0b2b231cd35b4324ee5ce71a751493f5d40f563d6dc0`)

