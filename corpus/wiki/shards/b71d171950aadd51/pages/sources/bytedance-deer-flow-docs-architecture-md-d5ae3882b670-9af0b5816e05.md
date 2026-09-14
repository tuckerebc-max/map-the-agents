---
access: public
aliases: []
claim_ids:
- clm_15f65575ecc3b5d8090e4243a00316e6d21d32b7db1a350225f91af8884c3e75
- clm_1fde4adef3a342da1eb21e71717381f270b5654775103cfaf7b4c0be6cc7392a
- clm_225af7dde29dfafcf43671f46ead14926f6d211f5c2486ff6418b71835e51270
- clm_3996320ef5eac73d43c8e8b306a1840fbaba629593f4d3bb8f015ca1ceba28b5
- clm_3d57d70b7cbe0a2375d3e65fe93901931f1253958cda949ea3eee9e7c93ccb6b
- clm_68e1f616c226e3b335ccba954f7e4cfc83c79fd8e45942c345afad9f00ae3494
- clm_890d7ab8da77cdf148b6f41fcd213b8ecb2798ee8ace0464a3b86bd6209ab9e8
- clm_a74cd3372d89d3041ddb3ee085837c91bfae71bdab1b8c82f84a2942725e651d
- clm_c076ce65c493b76e61e7bc0154547a5dd98b5cea7c6dd5e4fbde21c070a2ea2a
- clm_f91e4a78e4d0705f41b18e58de2a874c5fa0cb18629194b6b9c471c53a98648e
maturity: draft
page_id: pg_fa05c2f4135b558895719af0b5816e05
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b8d8f964e1e959869ce91d82ef10b5e9
title: bytedance/deer-flow/docs/ARCHITECTURE.md @ d5ae3882b670
updated_at: '2026-09-14T01:38:55Z'
---

# bytedance/deer-flow/docs/ARCHITECTURE.md @ d5ae3882b670

<!-- rcw:begin owner=source:src_b8d8f964e1e959869ce91d82ef10b5e9 block=evidence -->
- DeerFlow 2.0 is a ground-up rewrite sharing no code with the original v1 Deep Research framework, which per the French README is maintained on a separate 1.x branch. [@claim:clm_15f65575ecc3b5d8090e4243a00316e6d21d32b7db1a350225f91af8884c3e75]
- A single make dev or Docker stack runs four services: Nginx on port 2026 as the only public entry point, a FastAPI Gateway on 8001 with an embedded LangGraph-compatible agent runtime, a Next.js frontend on 3000, and an optional provisioner on 8002 for provisioner/K8s sandbox mode. [@claim:clm_1fde4adef3a342da1eb21e71717381f270b5654775103cfaf7b4c0be6cc7392a]
- DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super-agent harness built on LangGraph, where a lead agent orchestrates sub-agents, persistent memory, sandboxed code execution, and extensible skills/tools, isolated per conversation thread. [@claim:clm_225af7dde29dfafcf43671f46ead14926f6d211f5c2486ff6418b71835e51270]
- All run modes execute the agent through the Gateway via RunManager, run_agent() and StreamBridge; the lead agent is assembled by make_lead_agent() and wrapped in a middleware chain (thread data, uploads, sandbox, summarization, title, todo list, view image, clarification) that runs before the model call. [@claim:clm_3996320ef5eac73d43c8e8b306a1840fbaba629593f4d3bb8f015ca1ceba28b5]
- The frontend uses Next.js 16, React 19, TypeScript and Tailwind v4, with the LangGraph SDK for orchestration/streaming and TanStack Query for server state, requiring Node 22+ and pnpm 10.26.2+; a README badge indicates Python 3.12+ for the backend. [@claim:clm_3d57d70b7cbe0a2375d3e65fe93901931f1253958cda949ea3eee9e7c93ccb6b]
- ThreadState extends LangGraph's AgentState with sandbox, artifacts, thread_data, title, todos and viewed_images, and each thread gets isolated data directories under backend/.deer-flow/threads/{thread_id}/. [@claim:clm_68e1f616c226e3b335ccba954f7e4cfc83c79fd8e45942c345afad9f00ae3494]
- The security model gates client-writable body.context and body.config: keys like non_interactive, disable_clarification and github_token are honored only for internally-authenticated callers, identity/sandbox fields are cleared and restamped from auth state, and nginx is the only published, loopback-by-default surface. [@claim:clm_890d7ab8da77cdf148b6f41fcd213b8ecb2798ee8ace0464a3b86bd6209ab9e8]
- The backend splits into a publishable harness package (deerflow.*: orchestration, tools, sandbox, models, MCP, skills, memory, config) and an unpublished app layer (FastAPI Gateway, IM integrations), with a one-way rule that app imports deerflow but never the reverse, enforced by a CI test. [@claim:clm_a74cd3372d89d3041ddb3ee085837c91bfae71bdab1b8c82f84a2942725e651d]
- Tools come from three merged sources via get_available_tools(): built-ins (present_files, ask_clarification, view_image, review_skill_package), configured tools (bash, file operations, web search/fetch), and MCP tools; the sandbox is an abstract SandboxProvider with a dev-only LocalSandboxProvider and a Docker-based AioSandboxProvider using virtual path mapping. [@claim:clm_c076ce65c493b76e61e7bc0154547a5dd98b5cea7c6dd5e4fbde21c070a2ea2a]
- Nginx routes /api/langgraph/* to the Gateway's LangGraph-compatible runtime (rewritten to native /api/*), other /api/* paths to Gateway REST routers, and non-API paths to the frontend, so standard LangGraph SDK clients can talk to DeerFlow without a separate LangGraph server. [@claim:clm_f91e4a78e4d0705f41b18e58de2a874c5fa0cb18629194b6b9c471c53a98648e]
<!-- rcw:end owner=source:src_b8d8f964e1e959869ce91d82ef10b5e9 block=evidence -->

## Researcher notes

