# bytedance/deer-flow -- full detail

[Back to orientation](deer-flow.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bytedance/deer-flow/d5ae3882b6708fa9af7289a0c3c0be3eee157203/f0af2b8a99cbd610.json](../../../wiki/dossiers/bytedance/deer-flow/d5ae3882b6708fa9af7289a0c3c0be3eee157203/f0af2b8a99cbd610.json)

## specifications (2 claim(s))

- [observation/documented] DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super-agent harness built on LangGraph, where a lead agent orchestrates sub-agents, persistent memory, sandboxed code execution, and extensible skills/tools, isolated per conversation thread. -- evidence: [docs/ARCHITECTURE.md#L17-L22](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L17-L22) (`clm_225af7dde29dfafcf43671f46ead14926f6d211f5c2486ff6418b71835e51270`)
- [observation/documented] DeerFlow 2.0 is a ground-up rewrite sharing no code with the original v1 Deep Research framework, which per the French README is maintained on a separate 1.x branch. -- evidence: [README_fr.md#L16-L17](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L16-L17), [docs/ARCHITECTURE.md#L10-L11](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L10-L11) (`clm_15f65575ecc3b5d8090e4243a00316e6d21d32b7db1a350225f91af8884c3e75`)

## components (1 claim(s))

- [observation/documented] A single make dev or Docker stack runs four services: Nginx on port 2026 as the only public entry point, a FastAPI Gateway on 8001 with an embedded LangGraph-compatible agent runtime, a Next.js frontend on 3000, and an optional provisioner on 8002 for provisioner/K8s sandbox mode. -- evidence: [docs/ARCHITECTURE.md#L31-L36](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L31-L36), [docs/ARCHITECTURE.md#L28-L29](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L28-L29) (`clm_1fde4adef3a342da1eb21e71717381f270b5654775103cfaf7b4c0be6cc7392a`)

## design-choices (2 claim(s))

- [observation/documented] The backend splits into a publishable harness package (deerflow.*: orchestration, tools, sandbox, models, MCP, skills, memory, config) and an unpublished app layer (FastAPI Gateway, IM integrations), with a one-way rule that app imports deerflow but never the reverse, enforced by a CI test. -- evidence: [docs/ARCHITECTURE.md#L55-L59](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L55-L59), [docs/ARCHITECTURE.md#L61-L64](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L61-L64) (`clm_a74cd3372d89d3041ddb3ee085837c91bfae71bdab1b8c82f84a2942725e651d`)
- [observation/documented] The security model gates client-writable body.context and body.config: keys like non_interactive, disable_clarification and github_token are honored only for internally-authenticated callers, identity/sandbox fields are cleared and restamped from auth state, and nginx is the only published, loopback-by-default surface. -- evidence: [docs/ARCHITECTURE.md#L169-L184](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L169-L184) (`clm_890d7ab8da77cdf148b6f41fcd213b8ecb2798ee8ace0464a3b86bd6209ab9e8`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: Install.md is written for coding agents and prescribes an idempotent bootstrap that prefers Docker when available, avoids sudo and secret-file inspection, runs make config/docker-init or make check/install, and stops with a status report plus the exact next launch command. -- evidence: [Install.md#L79-L83](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L79-L83), [Install.md#L18-L23](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L18-L23), [Install.md#L3-L3](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L3-L3), [Install.md#L29-L34](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L29-L34), [Install.md#L38-L56](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L38-L56) (`clm_205af757a08de45635376754ed619ef14f30910535c2493db1ffba9ea2f06781`)
- [observation/documented] Repository development practice: the documented setup flow recommends make setup, an interactive wizard generating a minimal config.yaml and writing keys to .env, with make doctor for configuration checks and make support-bundle producing sanitized diagnostics (no .env, raw conversations, or user file contents) for GitHub issues. -- evidence: [README_fr.md#L113-L115](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L113-L115), [README_fr.md#L117-L117](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L117-L117), [README_fr.md#L119-L129](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L119-L129) (`clm_1803af411e1dce5ee868bc04a7f004a57255fa94c223b891e8abfeecca8bf82e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Nginx routes /api/langgraph/* to the Gateway's LangGraph-compatible runtime (rewritten to native /api/*), other /api/* paths to Gateway REST routers, and non-API paths to the frontend, so standard LangGraph SDK clients can talk to DeerFlow without a separate LangGraph server. -- evidence: [docs/ARCHITECTURE.md#L43-L47](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L43-L47), [docs/ARCHITECTURE.md#L38-L41](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L38-L41) (`clm_f91e4a78e4d0705f41b18e58de2a874c5fa0cb18629194b6b9c471c53a98648e`)

## memory-state (2 claim(s))

- [observation/documented] ThreadState extends LangGraph's AgentState with sandbox, artifacts, thread_data, title, todos and viewed_images, and each thread gets isolated data directories under backend/.deer-flow/threads/{thread_id}/. -- evidence: [docs/ARCHITECTURE.md#L92-L101](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L92-L101) (`clm_68e1f616c226e3b335ccba954f7e4cfc83c79fd8e45942c345afad9f00ae3494`)
- [observation/documented] An experiment prompt template defines a Context Extraction Assistant that summarizes conversation history into checklist sections (session intent, summary, artifacts, next steps) so the extracted context can replace the history and free conversation space. -- evidence: [docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L1-L3](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L1-L3), [docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L18-L18](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L18-L18), [docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L40-L41](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L40-L41), [docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L34-L34](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L34-L34), [docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L30-L30](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L30-L30), [docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L22-L22](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L22-L22), [docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L26-L26](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/experiments/task-continuity-20260912/prompts/deerflow-default-summary.txt#L26-L26) (`clm_9fbde2b32e3faf41042fb46305c99648d9a6b13606404badcbd696d6c9caff45`)

## orchestration (1 claim(s))

- [observation/documented] All run modes execute the agent through the Gateway via RunManager, run_agent() and StreamBridge; the lead agent is assembled by make_lead_agent() and wrapped in a middleware chain (thread data, uploads, sandbox, summarization, title, todo list, view image, clarification) that runs before the model call. -- evidence: [docs/ARCHITECTURE.md#L71-L74](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L71-L74), [docs/ARCHITECTURE.md#L76-L83](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L76-L83) (`clm_3996320ef5eac73d43c8e8b306a1840fbaba629593f4d3bb8f015ca1ceba28b5`)

## tools-permissions (1 claim(s))

- [observation/documented] Tools come from three merged sources via get_available_tools(): built-ins (present_files, ask_clarification, view_image, review_skill_package), configured tools (bash, file operations, web search/fetch), and MCP tools; the sandbox is an abstract SandboxProvider with a dev-only LocalSandboxProvider and a Docker-based AioSandboxProvider using virtual path mapping. -- evidence: [docs/ARCHITECTURE.md#L92-L101](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L92-L101) (`clm_c076ce65c493b76e61e7bc0154547a5dd98b5cea7c6dd5e4fbde21c070a2ea2a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The frontend uses Next.js 16, React 19, TypeScript and Tailwind v4, with the LangGraph SDK for orchestration/streaming and TanStack Query for server state, requiring Node 22+ and pnpm 10.26.2+; a README badge indicates Python 3.12+ for the backend. -- evidence: [README_fr.md#L5-L7](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L5-L7), [docs/ARCHITECTURE.md#L107-L109](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L107-L109) (`clm_3d57d70b7cbe0a2375d3e65fe93901931f1253958cda949ea3eee9e7c93ccb6b`)

## limitations (1 claim(s))

- [observation/documented] A database recovery doc states that an older deployment stamped with revision 0019_thread_incarnations but lacking the projects table and threads_meta.project_id cannot serve the current build; startup rejects that schema without changing it and reports the missing tables/columns. -- evidence: [docs/database-forward-revision-recovery.md#L3-L8](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/database-forward-revision-recovery.md#L3-L8) (`clm_6a04b155903f19f5b046e4ae4f7776ab66023f67f7c4f29fbf6b9da5a599080a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

