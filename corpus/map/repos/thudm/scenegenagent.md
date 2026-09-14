# thudm/scenegenagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cbaeeb96860f @ 8327735a5b52c650

## Summary (orientation draft, not independently verified)

README documents SceneGenAgent, an LLM-based agent generating industrial scenes via C# code with layout verification and iterative refinement, deployed as a Gradio app, with a SceneInstruct fine-tuning dataset and a curated benchmark reporting up to 81.0% success rate.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] SceneGenAgent is an LLM-based agent that generates industrial scenes through C# code, targeting precise measurements and positioning in industrial scene generation. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] SceneInstruct is a dataset built for fine-tuning open-source LLMs to integrate into SceneGenAgent; fine-tuned Llama3.1-70B reportedly approaches GPT-4o capability. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7)
- design-choices (1 claim(s)):
  - [observation/documented] Precise layout planning is reportedly ensured through a structured, calculable format, layout verification, and iterative refinement to meet quantitative industrial requirements. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7)
- workflows (2 claim(s)):
  - [observation/documented] Installation is via git clone of the THUDM/SceneGenAgent repository followed by pip install -r requirements.txt. -- evidence: [README.md#L29-L33](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L29-L33)
  - [observation/documented] Separate linked docs cover running the Gradio demo with API-based or offline models, training with SceneInstruct, building the SceneInstruct dataset, and running benchmark generation. -- evidence: [README.md#L55-L55](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L55-L55), [README.md#L41-L41](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L41-L41), [README.md#L45-L45](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L45-L45), [README.md#L37-L37](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L37-L37)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The repository provides code for deploying SceneGenAgent as a Gradio application. -- evidence: [README.md#L9-L9](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L9-L9)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] The README reports that LLMs powered by SceneGenAgent reach up to an 81.0% success rate on real-world industrial scene generation tasks. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7)
  - [observation/documented] Evaluation uses a curated benchmark of engineer-written scene descriptions, with manual checking of each generation's correctness. -- evidence: [README.md#L49-L49](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L49-L49)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt pins gradio==5.3.0, transformers==4.43.4, llama-recipes==0.0.3, and vllm==0.6.1; torch and openai are minimum-bounded (>=2.0, >=1.0), and datasets, fire, peft, accelerate, and wandb are unpinned. -- evidence: [requirements.txt#L1-L11](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/requirements.txt#L1-L11)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The work is documented in an arXiv paper (2410.21909, 2024) with a linked Hugging Face collection. -- evidence: [README.md#L3-L5](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L3-L5), [README.md#L59-L69](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L59-L69)

Every claim for this repository is shown above and in [full detail](scenegenagent.detail.md).

Metadata and full claim list: [full detail](scenegenagent.detail.md)
Human notes ([notes](scenegenagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
