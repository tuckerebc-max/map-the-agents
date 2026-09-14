# langchain-ai/open-swe

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1aa5d3b068c0 @ 96ddadd1932f01c2

## Summary (orientation draft, not independently verified)

Open SWE is an open-source (MIT) software-engineering agent built on Deep Agents and LangGraph, with cloud sandboxes, PR review, CI monitoring, and integrations (GitHub, Slack, Linear, dashboard). Evidence is mostly README and customization documentation describing runtime behavior and configuration. Evidence coverage: 130 of 362 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Open SWE is described as an open-source software factory built on Deep Agents by LangChain, licensed under the MIT License. -- evidence: [README.md#L11-L13](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L11-L13), [README.md#L167-L167](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L167-L167)
- components (2 claim(s)):
  - [observation/documented] The system ships five LangGraph graph entrypoints: Agent (implement/validate/deliver changes), Reviewer (read-only PR reviews), Analyzer (learns review style), Chat (PR Q&A), and Scheduler (recurring tasks and CI monitoring). -- evidence: [README.md#L93-L93](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L93-L93), [README.md#L95-L101](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L95-L101)
  - [observation/documented] Deep Agents supplies planning, file operations, shell access, skills, state, and subagent primitives; Open SWE adds software-engineering tools, prompts, middleware, integrations, authorization, and product surfaces on top. -- evidence: [README.md#L87-L87](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L87-L87)
- design-choices (2 claim(s)):
  - [observation/documented] The core agent is assembled in a single function, get_agent() in agent/server.py, where the sandbox, model, tools, and triggers can be swapped; custom sandbox providers implement SandboxBackendProtocol from deepagents. -- evidence: [docs/CUSTOMIZATION.md#L3-L3](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L3-L3), [docs/CUSTOMIZATION.md#L103-L103](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L103-L103)
  - [observation/documented] Model defaults are configurable via LLM_MODEL_ID and LLM_REASONING_EFFORT; an Anthropic-only deployment defaults to anthropic:claude-opus-5, other deployments to openai:gpt-5.6-sol, with default reasoning effort medium. -- evidence: [docs/CUSTOMIZATION.md#L139-L139](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L139-L139), [docs/CUSTOMIZATION.md#L146-L146](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/docs/CUSTOMIZATION.md#L146-L146)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local development uses uv venv/uv sync, make build-dashboard, and make dev serving API and dashboard at localhost:2024, with make dev-ui for hot-reloading UI work and an ngrok tunnel exposing only /webhooks/* for webhooks. -- evidence: [README.md#L157-L157](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L157-L157), [README.md#L147-L155](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L147-L155)
  - [observation/documented] Repository development practice: regenerate swagger.json with make swagger after changing backend routes or models, per the customization documentation. -- evidence: [README.md#L81-L81](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L81-L81)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The custom FastAPI backend (agent.webapp:app) has a generated OpenAPI 3.1 contract in swagger.json, served live at /openapi.json and browsable at /docs; LangGraph runtime endpoints like /runs and /threads are not included in it. -- evidence: [README.md#L79-L79](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L79-L79), [README.md#L81-L81](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L81-L81)
  - [observation/documented] Tasks can be started from a web dashboard, GitHub, Slack, or Linear (or on a schedule), and an experimental desktop client runs the agent against local projects, with packaged releases currently targeting macOS. -- evidence: [README.md#L115-L119](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L115-L119), [README.md#L65-L68](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L65-L68), [README.md#L25-L25](https://github.com/langchain-ai/open-swe/blob/1aa5d3b068c06f83229adf500f56600519cf10a7/README.md#L25-L25)
- memory-state (1 claim(s)):
More evidence: [full detail](open-swe.detail.md)

Metadata and full claim list: [full detail](open-swe.detail.md)
Human notes ([notes](open-swe.notes.md), never overwritten by build)

[Back to map index](../../index.md)
