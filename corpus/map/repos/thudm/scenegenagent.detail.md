# thudm/scenegenagent -- full detail

[Back to orientation](scenegenagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/thudm/scenegenagent/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/8327735a5b52c650.json](../../../wiki/dossiers/thudm/scenegenagent/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/8327735a5b52c650.json)

## specifications (1 claim(s))

- [observation/documented] SceneGenAgent is an LLM-based agent that generates industrial scenes through C# code, targeting precise measurements and positioning in industrial scene generation. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7) (`clm_5ba315d076d971c4378a0200c54b921bc1ca8f1071b8a769c9cad3a5b0609ded`)

## components (1 claim(s))

- [observation/documented] SceneInstruct is a dataset built for fine-tuning open-source LLMs to integrate into SceneGenAgent; fine-tuned Llama3.1-70B reportedly approaches GPT-4o capability. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7) (`clm_9f77c4ee5da92ae207f527d497e5ae5d693d367e8d915597074bc7de0c5b644d`)

## design-choices (1 claim(s))

- [observation/documented] Precise layout planning is reportedly ensured through a structured, calculable format, layout verification, and iterative refinement to meet quantitative industrial requirements. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7) (`clm_3c2aea56abc6126810a2d8bbc073b1a7db69c03eeedf08eeb5602a9303744a66`)

## workflows (2 claim(s))

- [observation/documented] Installation is via git clone of the THUDM/SceneGenAgent repository followed by pip install -r requirements.txt. -- evidence: [README.md#L29-L33](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L29-L33) (`clm_4d44144348fd136992a4185c7ee0cca4d172fdf1542b9a90ffbaa738a3ce9708`)
- [observation/documented] Separate linked docs cover running the Gradio demo with API-based or offline models, training with SceneInstruct, building the SceneInstruct dataset, and running benchmark generation. -- evidence: [README.md#L55-L55](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L55-L55), [README.md#L41-L41](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L41-L41), [README.md#L45-L45](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L45-L45), [README.md#L37-L37](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L37-L37) (`clm_37008e7e1337d799ae90204017f2f4bf26bd87850403608c49f892b1ee06cb73`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The repository provides code for deploying SceneGenAgent as a Gradio application. -- evidence: [README.md#L9-L9](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L9-L9) (`clm_98b0719b3de55437a5703137485a8a3c6c9d248895b8f9a2f23703b0f614bd80`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The README reports that LLMs powered by SceneGenAgent reach up to an 81.0% success rate on real-world industrial scene generation tasks. -- evidence: [README.md#L7-L7](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L7-L7) (`clm_cb0e2b6fba1174e40230f3b2e3fe57346b40eca18fa5f89e3bf5ce52877c6bc4`)
- [observation/documented] Evaluation uses a curated benchmark of engineer-written scene descriptions, with manual checking of each generation's correctness. -- evidence: [README.md#L49-L49](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L49-L49) (`clm_d732bf585fea1b8fbc9295f5177f114b160f7e72f6e99fde1a42b2367861d222`)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt pins gradio==5.3.0, transformers==4.43.4, llama-recipes==0.0.3, and vllm==0.6.1; torch and openai are minimum-bounded (>=2.0, >=1.0), and datasets, fire, peft, accelerate, and wandb are unpinned. -- evidence: [requirements.txt#L1-L11](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/requirements.txt#L1-L11) (`clm_8412cde7c165d5c716fad9a9a6ebe7c54d601865e5e8cf9a8b00454e039246ab`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The work is documented in an arXiv paper (2410.21909, 2024) with a linked Hugging Face collection. -- evidence: [README.md#L3-L5](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L3-L5), [README.md#L59-L69](https://github.com/THUDM/SceneGenAgent/blob/cbaeeb96860fceaa64f2f50a8e6fff48895be9f4/README.md#L59-L69) (`clm_caaab00ba6d5cd7c0affae318ea4b114dda6decae5df62c33c9b88b00ef261dc`)

