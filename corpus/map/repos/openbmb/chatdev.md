# openbmb/chatdev

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4fb2db0ea903 @ 73ccffc33d7b49cd

## Summary (orientation draft, not independently verified)

ChatDev 2.0 (DevAll) is a zero-code multi-agent orchestration platform with a FastAPI backend, Vue 3 web console, YAML-defined workflows, a Python SDK, REST/WebSocket attachment APIs, and a pluggable memory system; legacy ChatDev 1.0 lives on a separate branch. Evidence coverage: 119 of 205 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 47 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] ChatDev 2.0 (DevAll) is described as a zero-code multi-agent platform where users define agents, workflows, and tasks via configuration for scenarios such as data visualization, 3D generation, and deep research. -- evidence: [README.md#L22-L23](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L22-L23), [README.md#L8-L10](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L8-L10)
  - [observation/documented] ChatDev 1.0, the legacy 'Virtual Software Company' with CEO/CTO/Programmer-style agents automating the software lifecycle, has been moved to the chatdev1.0 branch for maintenance. -- evidence: [README.md#L22-L23](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L22-L23), [README.md#L26-L26](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L26-L26)
- components (1 claim(s)):
  - [observation/documented] The project is modular: server/ hosts the FastAPI backend, runtime/ handles agent abstraction and tool execution, workflow/ contains multi-agent logic driven by entity/ configs, frontend/ is a Vue 3 web console, and functions/ holds custom Python tools. -- evidence: [README.md#L271-L276](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L271-L276)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] The application can be started with make dev, or manually via uv run python server_main.py --port 6400 for the backend and a frontend dev server on port 5173 with VITE_API_BASE_URL pointing at the backend. -- evidence: [README.md#L152-L157](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L152-L157), [README.md#L136-L139](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L136-L139), [README.md#L145-L150](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L145-L150)
  - [observation/documented] Alternatively the whole application runs via Docker Compose (docker compose up --build) with backend on port 6400 and frontend on 5173; services auto-restart on crash and local file changes are reflected in containers. -- evidence: [README.md#L209-L209](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L209-L209), [README.md#L215-L219](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L215-L219), [README.md#L221-L223](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L221-L223), [README.md#L225-L225](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L225-L225)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] A Python SDK exposes run_workflow (from runtime.sdk) taking a YAML file, task prompt, attachments, and variable overrides, returning a result with a final message; it is also published on PyPI as chatdev 0.1.0. -- evidence: [README.md#L247-L248](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L247-L248), [README.md#L262-L262](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L262-L262), [README.md#L251-L256](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L251-L256), [README.md#L258-L260](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L258-L260)
  - [observation/documented] The backend exposes REST endpoints for uploading and listing session attachments (POST/GET /api/uploads/{session_id}), artifact-event polling, per-artifact download with meta/stream modes, and a whole-session zip download, with WebSocket mirrors emitting artifact_created events. -- evidence: [docs/user_guide/en/attachments.md#L24-L25](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L24-L25), [docs/user_guide/en/attachments.md#L32-L48](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L32-L48), [docs/user_guide/en/attachments.md#L57-L58](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L57-L58), [docs/user_guide/en/attachments.md#L51-L54](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L51-L54), [docs/user_guide/en/attachments.md#L9-L21](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L9-L21)
- memory-state (2 claim(s)):
  - [observation/documented] The memory system offers four built-in store types: simple (FAISS plus semantic rerank, read/write), file (read-only vector index over documents), blackboard (append-only recency log), and mem0 (cloud-managed, requires the mem0ai package). -- evidence: [docs/user_guide/en/modules/memory.md#L46-L51](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/modules/memory.md#L46-L51)
More evidence: [full detail](chatdev.detail.md)

Metadata and full claim list: [full detail](chatdev.detail.md)
Human notes ([notes](chatdev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
