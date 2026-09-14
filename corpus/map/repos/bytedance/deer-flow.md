# bytedance/deer-flow

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d5ae3882b670 @ f0af2b8a99cbd610

## Summary (orientation draft, not independently verified)

DeerFlow 2.0 is a ground-up rewrite of the v1 Deep Research framework: a LangGraph-based super-agent harness with a four-service topology (nginx, FastAPI Gateway, Next.js frontend, optional provisioner), a harness/app backend split, middleware-wrapped agent runtime, per-thread isolation, and a documented database-recovery path. Evidence is documentation-heavy; no benchmark/eval harness is described. Evidence coverage: 126 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 60 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super-agent harness built on LangGraph, where a lead agent orchestrates sub-agents, persistent memory, sandboxed code execution, and extensible skills/tools, isolated per conversation thread. -- evidence: [docs/ARCHITECTURE.md#L17-L22](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L17-L22)
  - [observation/documented] DeerFlow 2.0 is a ground-up rewrite sharing no code with the original v1 Deep Research framework, which per the French README is maintained on a separate 1.x branch. -- evidence: [README_fr.md#L16-L17](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L16-L17), [docs/ARCHITECTURE.md#L10-L11](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L10-L11)
- components (1 claim(s)):
  - [observation/documented] A single make dev or Docker stack runs four services: Nginx on port 2026 as the only public entry point, a FastAPI Gateway on 8001 with an embedded LangGraph-compatible agent runtime, a Next.js frontend on 3000, and an optional provisioner on 8002 for provisioner/K8s sandbox mode. -- evidence: [docs/ARCHITECTURE.md#L31-L36](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L31-L36), [docs/ARCHITECTURE.md#L28-L29](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L28-L29)
- design-choices (2 claim(s)):
  - [observation/documented] The backend splits into a publishable harness package (deerflow.*: orchestration, tools, sandbox, models, MCP, skills, memory, config) and an unpublished app layer (FastAPI Gateway, IM integrations), with a one-way rule that app imports deerflow but never the reverse, enforced by a CI test. -- evidence: [docs/ARCHITECTURE.md#L55-L59](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L55-L59), [docs/ARCHITECTURE.md#L61-L64](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L61-L64)
  - [observation/documented] The security model gates client-writable body.context and body.config: keys like non_interactive, disable_clarification and github_token are honored only for internally-authenticated callers, identity/sandbox fields are cleared and restamped from auth state, and nginx is the only published, loopback-by-default surface. -- evidence: [docs/ARCHITECTURE.md#L169-L184](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/docs/ARCHITECTURE.md#L169-L184)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: Install.md is written for coding agents and prescribes an idempotent bootstrap that prefers Docker when available, avoids sudo and secret-file inspection, runs make config/docker-init or make check/install, and stops with a status report plus the exact next launch command. -- evidence: [Install.md#L79-L83](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L79-L83), [Install.md#L18-L23](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L18-L23), [Install.md#L3-L3](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L3-L3), [Install.md#L29-L34](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L29-L34), [Install.md#L38-L56](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/Install.md#L38-L56)
  - [observation/documented] Repository development practice: the documented setup flow recommends make setup, an interactive wizard generating a minimal config.yaml and writing keys to .env, with make doctor for configuration checks and make support-bundle producing sanitized diagnostics (no .env, raw conversations, or user file contents) for GitHub issues. -- evidence: [README_fr.md#L113-L115](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L113-L115), [README_fr.md#L117-L117](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L117-L117), [README_fr.md#L119-L129](https://github.com/bytedance/deer-flow/blob/d5ae3882b6708fa9af7289a0c3c0be3eee157203/README_fr.md#L119-L129)
More evidence: [full detail](deer-flow.detail.md)

Metadata and full claim list: [full detail](deer-flow.detail.md)
Human notes ([notes](deer-flow.notes.md), never overwritten by build)

[Back to map index](../../index.md)
