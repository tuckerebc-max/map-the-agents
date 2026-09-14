---
access: public
aliases: []
claim_ids:
- clm_1095e22f83e87c0d0f81c23bf4e10d345063d96fe349612433e0e4f76718e337
- clm_12bee3f31ba7f3645c11e95b418d3277c0bc343f628d4eec5b3fa7c3dafaa5df
- clm_30b1f905f2be6cc5abed2485ea79c148d95f7819d875987aba4b183aba9220a2
- clm_868ee557da0d841fffc1396f92bf9e82a2ba390c4f6be68ccc8178e68ca5ef87
- clm_92fe4edd0a45f7317da5dc4a2ce3931b523532d9d8e0b9347091c5cf86364b7b
- clm_958f015877fb238170c14298d3db9399182748c226eee2396bef9e8e7bd4b9a9
- clm_9bb0d76b026b7fc704616006669df783a83e00341ed41ca20669caa3aaddefe9
- clm_b97e74373cbfdc3da9b3d16a391d98a22805b5e97cb4bd09555f8a1007d26067
maturity: draft
page_id: pg_7a3d0ed22dbf5ed0aa395943b70e735c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ac97650c472f5ec5aeb69d3fcb0b1a29
title: agentscope-ai/agentscope/README.md @ b82253ba1b68
updated_at: '2026-09-14T03:32:05Z'
---

# agentscope-ai/agentscope/README.md @ b82253ba1b68

<!-- rcw:begin owner=source:src_ac97650c472f5ec5aeb69d3fcb0b1a29 block=evidence -->
- The agent service offers leader-worker orchestration with built-in team tools and task planning, where a leader agent spawns and coordinates workers. [@claim:clm_1095e22f83e87c0d0f81c23bf4e10d345063d96fe349612433e0e4f76718e337]
- The agent service is a FastAPI backend with a pre-built Web UI offering multi-tenancy, multi-session isolation, channels (Feishu, Discord, DingTalk), RAG service, persistence, and scheduling. [@claim:clm_12bee3f31ba7f3645c11e95b418d3277c0bc343f628d4eec5b3fa7c3dafaa5df]
- AgentScope requires Python 3.11 or higher and can be installed from PyPI via 'uv pip install agentscope'. [@claim:clm_30b1f905f2be6cc5abed2485ea79c148d95f7819d875987aba4b183aba9220a2]
- Recent releases add A2A protocol support via an A2AAgent for chatting with remote A2A agents, and RealtimeAgent supporting DashScope, OpenAI, Gemini, and xAI realtime APIs. [@claim:clm_868ee557da0d841fffc1396f92bf9e82a2ba390c4f6be68ccc8178e68ca5ef87]
- The Toolkit manages Python tools, MCP servers, and skills, and ships built-in coding tools (shell, file edit, search) plus task/plan tools. [@claim:clm_92fe4edd0a45f7317da5dc4a2ce3931b523532d9d8e0b9347091c5cf86364b7b]
- The SDK exposes building blocks including a ReAct reasoning-acting loop, Toolkit, Model, Context, Event System, Permission & HITL, Middleware, Memory, and Workspace/Sandbox. [@claim:clm_958f015877fb238170c14298d3db9399182748c226eee2396bef9e8e7bd4b9a9]
- The design philosophy is to leverage models' reasoning and tool-use abilities rather than constrain them with strict prompts and opinionated orchestrations. [@claim:clm_9bb0d76b026b7fc704616006669df783a83e00341ed41ca20669caa3aaddefe9]
- The product includes a permission system with fine-grained control over tools and resources, confirmation flows, and a bypass mode where the agent runs without pausing for tool-call confirmations. [@claim:clm_b97e74373cbfdc3da9b3d16a391d98a22805b5e97cb4bd09555f8a1007d26067]
<!-- rcw:end owner=source:src_ac97650c472f5ec5aeb69d3fcb0b1a29 block=evidence -->

## Researcher notes

