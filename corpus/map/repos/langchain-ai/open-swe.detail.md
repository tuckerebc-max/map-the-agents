# langchain-ai/open-swe -- full detail

[Back to orientation](open-swe.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/langchain-ai/open-swe/1aa5d3b068c06f83229adf500f56600519cf10a7/96ddadd1932f01c2.json](../../../wiki/dossiers/langchain-ai/open-swe/1aa5d3b068c06f83229adf500f56600519cf10a7/96ddadd1932f01c2.json)

## specifications (1 claim(s))

- [observation/documented] Open SWE is described as an open-source software factory built on Deep Agents by LangChain, licensed under the MIT License. -- evidence: [README.md#L11-L13](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L11-L13), [README.md#L167-L167](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L167-L167) (`clm_8709082d819b7fca2d3a86159e6e92c996cfaae5d7142acf31a44a9b5a345815`)

## components (2 claim(s))

- [observation/documented] The system ships five LangGraph graph entrypoints: Agent (implement/validate/deliver changes), Reviewer (read-only PR reviews), Analyzer (learns review style), Chat (PR Q&A), and Scheduler (recurring tasks and CI monitoring). -- evidence: [README.md#L93-L93](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L93-L93), [README.md#L95-L101](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L95-L101) (`clm_57ae1673933e78fc68cc5af1bc9edbb301a4cd3f050663dc4a67bc7346272d02`)
- [observation/documented] Deep Agents supplies planning, file operations, shell access, skills, state, and subagent primitives; Open SWE adds software-engineering tools, prompts, middleware, integrations, authorization, and product surfaces on top. -- evidence: [README.md#L87-L87](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L87-L87) (`clm_dca51135bd999b3d67cc382e6545de869ef2db8571144e680b7fe7e3f2c2efa9`)

## design-choices (2 claim(s))

- [observation/documented] The core agent is assembled in a single function, get_agent() in agent/server.py, where the sandbox, model, tools, and triggers can be swapped; custom sandbox providers implement SandboxBackendProtocol from deepagents. -- evidence: [docs/CUSTOMIZATION.md#L3-L3](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L3-L3), [docs/CUSTOMIZATION.md#L103-L103](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L103-L103) (`clm_48a50b6f1cca70c7d6b6878699a9ad939c23417a1d9d36cd4415866b6e9e2d67`)
- [observation/documented] Model defaults are configurable via LLM_MODEL_ID and LLM_REASONING_EFFORT; an Anthropic-only deployment defaults to anthropic:claude-opus-5, other deployments to openai:gpt-5.6-sol, with default reasoning effort medium. -- evidence: [docs/CUSTOMIZATION.md#L139-L139](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L139-L139), [docs/CUSTOMIZATION.md#L146-L146](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L146-L146) (`clm_676c40853ff37e9148beb3dd2417582aaf7277322c59750fe31050ca74c2b4ca`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local development uses uv venv/uv sync, make build-dashboard, and make dev serving API and dashboard at localhost:2024, with make dev-ui for hot-reloading UI work and an ngrok tunnel exposing only /webhooks/* for webhooks. -- evidence: [README.md#L157-L157](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L157-L157), [README.md#L147-L155](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L147-L155) (`clm_9ba0395e23c00fa7a63ba7d2bf9acc190414b8ddeb54af265c21612edb07e4f5`)
- [observation/documented] Repository development practice: regenerate swagger.json with make swagger after changing backend routes or models, per the customization documentation. -- evidence: [README.md#L81-L81](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L81-L81) (`clm_52655e66584a87e1bb3ff6752f0d992b2dc84a1c3c2e38ac6d07175215fce278`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The custom FastAPI backend (agent.webapp:app) has a generated OpenAPI 3.1 contract in swagger.json, served live at /openapi.json and browsable at /docs; LangGraph runtime endpoints like /runs and /threads are not included in it. -- evidence: [README.md#L79-L79](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L79-L79), [README.md#L81-L81](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L81-L81) (`clm_aea4b775dd5aeb3ee6a208331d9419381c0290443220776fa6f1a20f1deb481a`)
- [observation/documented] Tasks can be started from a web dashboard, GitHub, Slack, or Linear (or on a schedule), and an experimental desktop client runs the agent against local projects, with packaged releases currently targeting macOS. -- evidence: [README.md#L115-L119](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L115-L119), [README.md#L65-L68](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L65-L68), [README.md#L25-L25](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L25-L25) (`clm_feecdf62a6a0e6a2eca193e583e655be12eed01fd19d531b35ddff32ec96bb41`)

## memory-state (1 claim(s))

- [observation/documented] Cloud work runs in isolated Linux sandboxes that persist with their thread; an unreachable coding sandbox is not silently replaced—the system fails safely rather than risk discarding uncommitted work. -- evidence: [README.md#L105-L105](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L105-L105) (`clm_dc22235b02dde51c1de34e7f47ce0c208d31078f8388be408f38db87866d5823`)

## orchestration (2 claim(s))

- [observation/documented] Each coding thread is bound to its own persistent sandbox; a thread is a durable conversation containing multiple invocations, independent threads run in parallel, and read-only PR chat needs no sandbox. -- evidence: [README.md#L45-L45](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L45-L45) (`clm_1da20a10437cc0a60885a64ee2488c4af45a021c523de6751280360a6d540ca0`)
- [observation/documented] LangGraph provides durable execution and thread state, with each Open SWE invocation executing as a LangGraph run within a thread. -- evidence: [README.md#L93-L93](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L93-L93) (`clm_e4a9dc1309f1e3977c989582be20d3107b77829e8af3f0b121ae62b1d9790866`)

## tools-permissions (3 claim(s))

- [observation/documented] Safety controls include per-thread sandbox isolation, GitHub App installation boundaries with optional per-user OAuth, org/repo allowlists with actor authorization checks, human approval before pushing workflow-file changes, and read-only reviewer/chat agents. -- evidence: [README.md#L125-L132](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L125-L132) (`clm_7a7096f91a2eb545640a7b611de43e8f07921697dbbd5829272b7e4e5bfd6c94`)
- [observation/documented] For LangSmith sandboxes, GitHub proxy rules give github.com Basic auth for git-over-HTTPS and api.github.com Bearer auth for gh/REST; the proxy token is minted at runtime from GitHub App installation credentials rather than stored as env vars. -- evidence: [docs/CUSTOMIZATION.md#L50-L51](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L50-L51), [docs/CUSTOMIZATION.md#L53-L53](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L53-L53), [docs/CUSTOMIZATION.md#L48-L48](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L48-L48) (`clm_f26c6b8dede45e8fd1dbd978bc158faf62561c576a36b146af11efd8467db946`)
- [observation/documented] Admins can connect remote MCP servers whose enabled tools become available to all coding-agent users; personal MCP connections load only in private threads owned by the triggering user, and plan mode blocks workspace MCP tools. -- evidence: [docs/CUSTOMIZATION.md#L407-L416](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L407-L416), [docs/CUSTOMIZATION.md#L234-L239](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L234-L239) (`clm_8de56af2cfa5a93a1bf4cb0e3cbfcc3c1da84b2dcf97ace0bd6bcd0b2722226d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] LangSmith is the default sandbox and tracing provider; Modal, Daytona, Runloop, E2B, and local execution are also supported via a pluggable provider interface selected by the SANDBOX_TYPE environment variable. -- evidence: [README.md#L107-L107](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L107-L107), [docs/CUSTOMIZATION.md#L59-L66](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L59-L66), [docs/CUSTOMIZATION.md#L57-L57](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L57-L57) (`clm_577b614381fab4418b75ea648d9438ea1082f80f4351c694c135902468d1e5d2`)

## limitations (1 claim(s))

- [observation/documented] The project is under active development and its APIs, setup, and product surfaces may continue to evolve; the local sandbox provider runs commands directly on the host with no isolation and is intended only for development. -- evidence: [docs/CUSTOMIZATION.md#L68-L68](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L68-L68), [README.md#L29-L30](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L29-L30) (`clm_d9fe1c643132a386b8e356e05b3d4fb227d30657f84769ceefdaae34fb26822e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

