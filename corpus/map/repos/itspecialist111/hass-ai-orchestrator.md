# itspecialist111/hass-ai-orchestrator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cebfdff5d5a9 @ 9cd40944db7532c2

## Summary (orientation draft, not independently verified)

README evidence describes HASS-AI-Orchestrator v0.13.6, a Home Assistant add-on pairing a local/cloud LLM reasoning agent with a deterministic kernel that validates tools, intercepts mutations into reviewable plans, and replays them with checkpoints. It also documents an eval scenario suite, safety policy, memory/RAG, and developer test instructions. Evidence coverage: 145 of 329 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is versioned v0.13.6 and is distributed as a Home Assistant add-on, with a badge claiming 286 backend tests passing. -- evidence: [README.md#L3-L6](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L3-L6)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The design principle is that the model proposes while application code validates: the runtime, not the model, decides which tools exist, which domains/services are allowed, what needs approval, and what is audited. -- evidence: [README.md#L28-L28](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L28-L28), [README.md#L12-L12](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L12-L12), [README.md#L14-L14](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L14-L14), [README.md#L16-L24](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L16-L24)
  - [observation/documented] The product ships dry-run by default with direct execution disabled; first-run config sets dry_run_mode true, reasoning_allow_direct_execute false, and legacy autonomous loops disabled. -- evidence: [README.md#L471-L474](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L471-L474), [README.md#L456-L460](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L456-L460), [README.md#L32-L35](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L32-L35)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run backend tests via pytest in a Python 3.11/3.12 venv, build the dashboard with npm ci/audit/build on Node 22, and can use a Dockerfile.test image for a lockfile-only reproducible test run. -- evidence: [README.md#L615-L615](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L615-L615), [README.md#L641-L644](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L641-L644), [README.md#L629-L635](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L629-L635), [README.md#L639-L639](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L639-L639), [README.md#L627-L627](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L627-L627), [README.md#L617-L623](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L617-L623)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A React dashboard provides Home, Ask & Run, Action center, Automation, Advanced insights, Dashboard Studio, and Quick Ask surfaces; generated dashboard HTML runs in an opaque sandbox under a restrictive CSP with no same-origin API access. -- evidence: [README.md#L187-L195](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L187-L195), [README.md#L197-L197](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L197-L197)
  - [observation/documented] Three reasoning profiles (Rapid, Balanced, Deep) vary thinking, iteration, tool-call, and time ceilings while keeping identical schema validation, allowlists, approval requirements, and checkpointed replay. -- evidence: [README.md#L418-L418](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L418-L418), [README.md#L410-L414](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L410-L414)
- memory-state (1 claim(s)):
  - [observation/documented] Optional RAG and episodic memory use ChromaDB with local Ollama embeddings to store entity capabilities, manuals, past goals and outcomes, and user feedback; recalled episodes are reweighted by feedback without changing execution policy. -- evidence: [README.md#L181-L181](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L181-L181), [README.md#L173-L173](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L173-L173), [README.md#L175-L179](https://github.com/ITSpecialist111/HASS-AI-Orchestrator/blob/cebfdff5d5a950ea9ad2cd166f7768af997e4d3b/README.md#L175-L179)
- orchestration (3 claim(s)):
More evidence: [full detail](hass-ai-orchestrator.detail.md)

Metadata and full claim list: [full detail](hass-ai-orchestrator.detail.md)
Human notes ([notes](hass-ai-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
