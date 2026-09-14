---
access: public
aliases: []
claim_ids:
- clm_1da20a10437cc0a60885a64ee2488c4af45a021c523de6751280360a6d540ca0
- clm_52655e66584a87e1bb3ff6752f0d992b2dc84a1c3c2e38ac6d07175215fce278
- clm_577b614381fab4418b75ea648d9438ea1082f80f4351c694c135902468d1e5d2
- clm_57ae1673933e78fc68cc5af1bc9edbb301a4cd3f050663dc4a67bc7346272d02
- clm_7a7096f91a2eb545640a7b611de43e8f07921697dbbd5829272b7e4e5bfd6c94
- clm_8709082d819b7fca2d3a86159e6e92c996cfaae5d7142acf31a44a9b5a345815
- clm_9ba0395e23c00fa7a63ba7d2bf9acc190414b8ddeb54af265c21612edb07e4f5
- clm_aea4b775dd5aeb3ee6a208331d9419381c0290443220776fa6f1a20f1deb481a
- clm_d9fe1c643132a386b8e356e05b3d4fb227d30657f84769ceefdaae34fb26822e
- clm_dc22235b02dde51c1de34e7f47ce0c208d31078f8388be408f38db87866d5823
- clm_dca51135bd999b3d67cc382e6545de869ef2db8571144e680b7fe7e3f2c2efa9
- clm_e4a9dc1309f1e3977c989582be20d3107b77829e8af3f0b121ae62b1d9790866
- clm_feecdf62a6a0e6a2eca193e583e655be12eed01fd19d531b35ddff32ec96bb41
maturity: draft
page_id: pg_e06b99a5d1885942bc2ce4c8fe65b2c2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8130f6f96f285e65a37437545da05e83
title: langchain-ai/open-swe/README.md @ 1aa5d3b068c0
updated_at: '2026-09-14T02:10:57Z'
---

# langchain-ai/open-swe/README.md @ 1aa5d3b068c0

<!-- rcw:begin owner=source:src_8130f6f96f285e65a37437545da05e83 block=evidence -->
- Each coding thread is bound to its own persistent sandbox; a thread is a durable conversation containing multiple invocations, independent threads run in parallel, and read-only PR chat needs no sandbox. [@claim:clm_1da20a10437cc0a60885a64ee2488c4af45a021c523de6751280360a6d540ca0]
- Repository development practice: regenerate swagger.json with make swagger after changing backend routes or models, per the customization documentation. [@claim:clm_52655e66584a87e1bb3ff6752f0d992b2dc84a1c3c2e38ac6d07175215fce278]
- LangSmith is the default sandbox and tracing provider; Modal, Daytona, Runloop, E2B, and local execution are also supported via a pluggable provider interface selected by the SANDBOX_TYPE environment variable. [@claim:clm_577b614381fab4418b75ea648d9438ea1082f80f4351c694c135902468d1e5d2]
- The system ships five LangGraph graph entrypoints: Agent (implement/validate/deliver changes), Reviewer (read-only PR reviews), Analyzer (learns review style), Chat (PR Q&A), and Scheduler (recurring tasks and CI monitoring). [@claim:clm_57ae1673933e78fc68cc5af1bc9edbb301a4cd3f050663dc4a67bc7346272d02]
- Safety controls include per-thread sandbox isolation, GitHub App installation boundaries with optional per-user OAuth, org/repo allowlists with actor authorization checks, human approval before pushing workflow-file changes, and read-only reviewer/chat agents. [@claim:clm_7a7096f91a2eb545640a7b611de43e8f07921697dbbd5829272b7e4e5bfd6c94]
- Open SWE is described as an open-source software factory built on Deep Agents by LangChain, licensed under the MIT License. [@claim:clm_8709082d819b7fca2d3a86159e6e92c996cfaae5d7142acf31a44a9b5a345815]
- Repository development practice: local development uses uv venv/uv sync, make build-dashboard, and make dev serving API and dashboard at localhost:2024, with make dev-ui for hot-reloading UI work and an ngrok tunnel exposing only /webhooks/* for webhooks. [@claim:clm_9ba0395e23c00fa7a63ba7d2bf9acc190414b8ddeb54af265c21612edb07e4f5]
- The custom FastAPI backend (agent.webapp:app) has a generated OpenAPI 3.1 contract in swagger.json, served live at /openapi.json and browsable at /docs; LangGraph runtime endpoints like /runs and /threads are not included in it. [@claim:clm_aea4b775dd5aeb3ee6a208331d9419381c0290443220776fa6f1a20f1deb481a]
- The project is under active development and its APIs, setup, and product surfaces may continue to evolve; the local sandbox provider runs commands directly on the host with no isolation and is intended only for development. [@claim:clm_d9fe1c643132a386b8e356e05b3d4fb227d30657f84769ceefdaae34fb26822e]
- Cloud work runs in isolated Linux sandboxes that persist with their thread; an unreachable coding sandbox is not silently replaced—the system fails safely rather than risk discarding uncommitted work. [@claim:clm_dc22235b02dde51c1de34e7f47ce0c208d31078f8388be408f38db87866d5823]
- Deep Agents supplies planning, file operations, shell access, skills, state, and subagent primitives; Open SWE adds software-engineering tools, prompts, middleware, integrations, authorization, and product surfaces on top. [@claim:clm_dca51135bd999b3d67cc382e6545de869ef2db8571144e680b7fe7e3f2c2efa9]
- LangGraph provides durable execution and thread state, with each Open SWE invocation executing as a LangGraph run within a thread. [@claim:clm_e4a9dc1309f1e3977c989582be20d3107b77829e8af3f0b121ae62b1d9790866]
- Tasks can be started from a web dashboard, GitHub, Slack, or Linear (or on a schedule), and an experimental desktop client runs the agent against local projects, with packaged releases currently targeting macOS. [@claim:clm_feecdf62a6a0e6a2eca193e583e655be12eed01fd19d531b35ddff32ec96bb41]
<!-- rcw:end owner=source:src_8130f6f96f285e65a37437545da05e83 block=evidence -->

## Researcher notes

