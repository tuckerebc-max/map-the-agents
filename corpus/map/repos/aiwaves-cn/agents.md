# aiwaves-cn/agents

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e8c4e3c2d197 @ e1eef48ba43f73dd

## Summary (orientation draft, not independently verified)

The README describes Agents 2.0, a framework for training language agents via symbolic learning (language-based loss, gradients, and weight updates), with pinned Python dependencies and Apache-2.0 licensing. Evidence is limited to README and requirements.txt.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The project is Agents 2.0, a major update adding support for agent learning and evaluation, released 2024-06-25. -- evidence: [README.md#L26-L27](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L26-L27), [README.md#L6-L13](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L6-L13)
  - [observation/documented] The repository is versioned v2.0.0 and licensed under Apache 2.0, with project page, arXiv paper, and docs links provided. -- evidence: [README.md#L15-L18](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L15-L18), [README.md#L6-L13](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L6-L13)
- components (2 claim(s)):
  - [observation/documented] Training implements a forward pass (agent execution) recording inputs, outputs, prompts, and tool usage per node in a trajectory, then a prompt-based loss producing a language loss. -- evidence: [README.md#L35-L35](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L35-L35)
  - [observation/documented] The framework back-propagates language loss along the trajectory to produce textual 'language gradients', then updates symbolic components and the node graph via prompts. -- evidence: [README.md#L35-L35](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L35-L35)
- design-choices (1 claim(s)):
  - [observation/documented] Agent symbolic learning analogizes an agent pipeline to a neural net's computational graph, with prompts and tools playing the role of layer weights. -- evidence: [README.md#L31-L31](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L31-L31)
- workflows (1 claim(s)):
  - [observation/documented] Installation is documented via pip from the GitHub master branch or an editable local clone with 'pip install -e .'. -- evidence: [README.md#L51-L56](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L51-L56), [README.md#L46-L49](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L46-L49)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The approach supports optimizing multi-agent systems by treating nodes as distinct agents or allowing multiple agents to act within one node. -- evidence: [README.md#L35-L35](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L35-L35)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt pins exact versions of torch, openai, litellm, langchain-core/community, gradio, wandb, pymilvus, qdrant-client, selenium, and other libraries. -- evidence: [requirements.txt#L1-L30](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/requirements.txt#L1-L30)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The work is associated with the 2024 arXiv paper 'Symbolic Learning Enables Self-Evolving Agents' and a 2023 companion framework paper, both cited in the README. -- evidence: [README.md#L67-L77](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L67-L77), [README.md#L79-L88](https://github.com/aiwaves-cn/agents/blob/e8c4e3c2d19739d3dff59e577d1c97090cc15f59/README.md#L79-L88)

Every claim for this repository is shown above and in [full detail](agents.detail.md).

Metadata and full claim list: [full detail](agents.detail.md)
Human notes ([notes](agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
