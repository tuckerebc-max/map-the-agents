# swe-gym/swe-gym

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b681068ca206 @ be525b8e3fa4d1c5

## Summary (orientation draft, not independently verified)

SWE-Gym is a training environment for software engineering agents and verifiers, with 2.4K real Python tasks from 11 repos, documented reproduction workflows for OpenHands and MoatlessTools agents, and reported SOTA results on SWE-Bench Verified/Lite.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] SWE-Gym provides 2.4K real tasks from 11 Python repositories plus a Lite split of 234 instances, combining repository context, executable environments, and test verification. -- evidence: [README.md#L44-L44](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L44-L44)
- components (1 claim(s)):
  - [observation/documented] Verifiers trained on agent trajectories perform best-of-N selection to enable inference-time scaling alongside the learned agents. -- evidence: [docs/MoatlessTools.md#L21-L21](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/MoatlessTools.md#L21-L21), [README.md#L68-L69](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L68-L69)
- design-choices (1 claim(s)):
  - [inference/documented] The project appears to emphasize scaling trends, stating results are bottlenecked by training and inference compute rather than environment size. -- evidence: [README.md#L39-L40](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L39-L40), [README.md#L81-L81](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L81-L81)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: docs instruct cloning the SWE-Gym OpenHands fork, configuring models via config.toml, exporting ALLHANDS_API_KEY for RemoteRuntime, and running rollout and eval scripts. -- evidence: [docs/OpenHands.md#L72-L74](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L72-L74), [docs/OpenHands.md#L8-L11](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L8-L11), [docs/OpenHands.md#L47-L47](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L47-L47), [docs/OpenHands.md#L55-L55](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L55-L55), [docs/OpenHands.md#L20-L20](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L20-L20), [docs/OpenHands.md#L60-L60](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L60-L60)
  - [observation/documented] Repository development practice: policy training uses Modal with torchtune full-parameter fine-tuning (N_GPUS=8) on a Qwen2.5-Coder-32B config, with SFT trajectories downloaded from Hugging Face. -- evidence: [docs/OpenHands.md#L90-L90](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L90-L90), [docs/OpenHands.md#L96-L96](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L96-L96), [docs/OpenHands.md#L92-L92](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L92-L92), [docs/OpenHands.md#L94-L94](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L94-L94)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (3 claim(s)):
  - [observation/documented] The project reports baselines achieving 32%/26% on SWE-Bench Verified/Lite, described as a new open state of the art. -- evidence: [README.md#L68-L69](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L68-L69), [README.md#L36-L37](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L36-L37)
  - [observation/documented] Fine-tuning a 32B OpenHands agent on under 500 trajectories from GPT-4o and Claude 3.5 Sonnet reportedly yields +14% absolute gains on SWE-Bench Verified. -- evidence: [README.md#L51-L51](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L51-L51)
- dependencies (2 claim(s)):
  - [observation/documented] The dataset is hosted on Hugging Face under the SWE-Gym organization, and pre-built Docker images exist under the xingyaoww/sweb.eval.x86_64 prefix on Docker Hub. -- evidence: [README.md#L88-L88](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L88-L88), [README.md#L92-L92](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L92-L92)
  - [observation/documented] Environment constants are maintained in a separate SWE-Bench-Fork repository, and reproduction relies on forks of OpenHands and Moatless-Agent. -- evidence: [README.md#L90-L90](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/README.md#L90-L90), [docs/OpenHands.md#L8-L11](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L8-L11), [docs/MoatlessTools.md#L8-L10](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/MoatlessTools.md#L8-L10)
- limitations (1 claim(s)):
  - [observation/documented] The docs note results were obtained with a specific OpenHands fork and that notable performance differences are expected with the latest OpenHands version. -- evidence: [docs/OpenHands.md#L8-L11](https://github.com/SWE-Gym/SWE-Gym/blob/b681068ca20628c6987b7416cc4cf03f06b77ba5/docs/OpenHands.md#L8-L11)
- relevance (1 claim(s)):
More evidence: [full detail](swe-gym.detail.md)

Metadata and full claim list: [full detail](swe-gym.detail.md)
Human notes ([notes](swe-gym.notes.md), never overwritten by build)

[Back to map index](../../index.md)
