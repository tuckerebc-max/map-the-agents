# aiwaves-cn/agents -- full detail

[Back to orientation](agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aiwaves-cn/agents/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/e1eef48ba43f73dd.json](../../../wiki/dossiers/aiwaves-cn/agents/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/e1eef48ba43f73dd.json)

## specifications (2 claim(s))

- [observation/documented] The project is Agents 2.0, a major update adding support for agent learning and evaluation, released 2024-06-25. -- evidence: [README.md#L26-L27](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L26-L27), [README.md#L6-L13](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L6-L13) (`clm_07ff707ed03df83946f99d560215fe47adb4cf06e3983f32651a26dc0e4b3429`)
- [observation/documented] The repository is versioned v2.0.0 and licensed under Apache 2.0, with project page, arXiv paper, and docs links provided. -- evidence: [README.md#L15-L18](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L15-L18), [README.md#L6-L13](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L6-L13) (`clm_c44d51af70841ce17e3f3da7f5eb7520e82d478069967b2b6cd986a71b593cf2`)

## components (2 claim(s))

- [observation/documented] Training implements a forward pass (agent execution) recording inputs, outputs, prompts, and tool usage per node in a trajectory, then a prompt-based loss producing a language loss. -- evidence: [README.md#L35-L35](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L35-L35) (`clm_10d38630123cb9ea5b3e2677a0704e49280dd570e1b9cf9ce24b1c567486d1f7`)
- [observation/documented] The framework back-propagates language loss along the trajectory to produce textual 'language gradients', then updates symbolic components and the node graph via prompts. -- evidence: [README.md#L35-L35](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L35-L35) (`clm_39f17a94648d3760f736674f93015db6b513f53bb61c484ae47ce9d94f1b0a18`)

## design-choices (1 claim(s))

- [observation/documented] Agent symbolic learning analogizes an agent pipeline to a neural net's computational graph, with prompts and tools playing the role of layer weights. -- evidence: [README.md#L31-L31](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L31-L31) (`clm_0d36ab97baa7d137fc6cf2dd0f41cf1aef121c5cd38d17470636a0088f42aff5`)

## workflows (1 claim(s))

- [observation/documented] Installation is documented via pip from the GitHub master branch or an editable local clone with 'pip install -e .'. -- evidence: [README.md#L51-L56](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L51-L56), [README.md#L46-L49](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L46-L49) (`clm_1e93f72e5985659eb5b60a52e8530afd39ef8abe3eceaf450ffba34688715c14`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The approach supports optimizing multi-agent systems by treating nodes as distinct agents or allowing multiple agents to act within one node. -- evidence: [README.md#L35-L35](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L35-L35) (`clm_e5e2f2a95e099f6a7e9ba6d256b0e6b0578a8638de3ed05fc6bb01ca3d60a58c`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt pins exact versions of torch, openai, litellm, langchain-core/community, gradio, wandb, pymilvus, qdrant-client, selenium, and other libraries. -- evidence: [requirements.txt#L1-L30](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/requirements.txt#L1-L30) (`clm_718764ac1ead91a7ff67d51473f4eb81bcb3fc3c3de5e223f52fefb1deb7f4ab`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The work is associated with the 2024 arXiv paper 'Symbolic Learning Enables Self-Evolving Agents' and a 2023 companion framework paper, both cited in the README. -- evidence: [README.md#L67-L77](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L67-L77), [README.md#L79-L88](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L79-L88) (`clm_e6479d35af452fc8df7321677e3bb8f1e00b7ff1322b263041099bd780b9e78e`)

