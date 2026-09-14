---
access: public
aliases: []
claim_ids:
- clm_07ff707ed03df83946f99d560215fe47adb4cf06e3983f32651a26dc0e4b3429
- clm_0d36ab97baa7d137fc6cf2dd0f41cf1aef121c5cd38d17470636a0088f42aff5
- clm_10d38630123cb9ea5b3e2677a0704e49280dd570e1b9cf9ce24b1c567486d1f7
- clm_1e93f72e5985659eb5b60a52e8530afd39ef8abe3eceaf450ffba34688715c14
- clm_39f17a94648d3760f736674f93015db6b513f53bb61c484ae47ce9d94f1b0a18
- clm_c44d51af70841ce17e3f3da7f5eb7520e82d478069967b2b6cd986a71b593cf2
- clm_e5e2f2a95e099f6a7e9ba6d256b0e6b0578a8638de3ed05fc6bb01ca3d60a58c
- clm_e6479d35af452fc8df7321677e3bb8f1e00b7ff1322b263041099bd780b9e78e
maturity: draft
page_id: pg_0b856e9ee4da55ffb2436229b18a75f7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4c717d08875e5bc78046f74c980636be
title: aiwaves-cn/agents/README.md @ e8c4e3c2d197
updated_at: '2026-09-14T01:30:54Z'
---

# aiwaves-cn/agents/README.md @ e8c4e3c2d197

<!-- rcw:begin owner=source:src_4c717d08875e5bc78046f74c980636be block=evidence -->
- The project is Agents 2.0, a major update adding support for agent learning and evaluation, released 2024-06-25. [@claim:clm_07ff707ed03df83946f99d560215fe47adb4cf06e3983f32651a26dc0e4b3429]
- Agent symbolic learning analogizes an agent pipeline to a neural net's computational graph, with prompts and tools playing the role of layer weights. [@claim:clm_0d36ab97baa7d137fc6cf2dd0f41cf1aef121c5cd38d17470636a0088f42aff5]
- Training implements a forward pass (agent execution) recording inputs, outputs, prompts, and tool usage per node in a trajectory, then a prompt-based loss producing a language loss. [@claim:clm_10d38630123cb9ea5b3e2677a0704e49280dd570e1b9cf9ce24b1c567486d1f7]
- Installation is documented via pip from the GitHub master branch or an editable local clone with 'pip install -e .'. [@claim:clm_1e93f72e5985659eb5b60a52e8530afd39ef8abe3eceaf450ffba34688715c14]
- The framework back-propagates language loss along the trajectory to produce textual 'language gradients', then updates symbolic components and the node graph via prompts. [@claim:clm_39f17a94648d3760f736674f93015db6b513f53bb61c484ae47ce9d94f1b0a18]
- The repository is versioned v2.0.0 and licensed under Apache 2.0, with project page, arXiv paper, and docs links provided. [@claim:clm_c44d51af70841ce17e3f3da7f5eb7520e82d478069967b2b6cd986a71b593cf2]
- The approach supports optimizing multi-agent systems by treating nodes as distinct agents or allowing multiple agents to act within one node. [@claim:clm_e5e2f2a95e099f6a7e9ba6d256b0e6b0578a8638de3ed05fc6bb01ca3d60a58c]
- The work is associated with the 2024 arXiv paper 'Symbolic Learning Enables Self-Evolving Agents' and a 2023 companion framework paper, both cited in the README. [@claim:clm_e6479d35af452fc8df7321677e3bb8f1e00b7ff1322b263041099bd780b9e78e]
<!-- rcw:end owner=source:src_4c717d08875e5bc78046f74c980636be block=evidence -->

## Researcher notes

