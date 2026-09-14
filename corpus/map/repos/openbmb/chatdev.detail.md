# openbmb/chatdev -- full detail

[Back to orientation](chatdev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openbmb/chatdev/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/73ccffc33d7b49cd.json](../../../wiki/dossiers/openbmb/chatdev/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/73ccffc33d7b49cd.json)

## specifications (2 claim(s))

- [observation/documented] ChatDev 2.0 (DevAll) is described as a zero-code multi-agent platform where users define agents, workflows, and tasks via configuration for scenarios such as data visualization, 3D generation, and deep research. -- evidence: [README.md#L22-L23](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L22-L23), [README.md#L8-L10](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L8-L10) (`clm_d4261314489e9628f0af62079f341f006bc760f9e1c3aad9245c98fb517d401c`)
- [observation/documented] ChatDev 1.0, the legacy 'Virtual Software Company' with CEO/CTO/Programmer-style agents automating the software lifecycle, has been moved to the chatdev1.0 branch for maintenance. -- evidence: [README.md#L22-L23](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L22-L23), [README.md#L26-L26](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L26-L26) (`clm_b436a660288c396288fbd47e94f772cdd08e2eb1d3104f4684ac14685c15d8f7`)

## components (1 claim(s))

- [observation/documented] The project is modular: server/ hosts the FastAPI backend, runtime/ handles agent abstraction and tool execution, workflow/ contains multi-agent logic driven by entity/ configs, frontend/ is a Vue 3 web console, and functions/ holds custom Python tools. -- evidence: [README.md#L271-L276](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L271-L276) (`clm_2ffa16cbf093b932782b37191564262314acb9ccd74b5c51171327494dd7d1ba`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] The application can be started with make dev, or manually via uv run python server_main.py --port 6400 for the backend and a frontend dev server on port 5173 with VITE_API_BASE_URL pointing at the backend. -- evidence: [README.md#L152-L157](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L152-L157), [README.md#L136-L139](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L136-L139), [README.md#L145-L150](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L145-L150) (`clm_7743aebec48fc5047881a063b8487fe6e227b507c1366ec778bfa6e9c13272a2`)
- [observation/documented] Alternatively the whole application runs via Docker Compose (docker compose up --build) with backend on port 6400 and frontend on 5173; services auto-restart on crash and local file changes are reflected in containers. -- evidence: [README.md#L209-L209](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L209-L209), [README.md#L215-L219](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L215-L219), [README.md#L221-L223](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L221-L223), [README.md#L225-L225](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L225-L225) (`clm_f1d65bd27a4a9c5932319a3e835f4db76905fef863fc658bb5f45857d7295953`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] A Python SDK exposes run_workflow (from runtime.sdk) taking a YAML file, task prompt, attachments, and variable overrides, returning a result with a final message; it is also published on PyPI as chatdev 0.1.0. -- evidence: [README.md#L247-L248](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L247-L248), [README.md#L262-L262](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L262-L262), [README.md#L251-L256](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L251-L256), [README.md#L258-L260](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L258-L260) (`clm_267909084b2727ecf4b3a5f6b655ea8f8055cb5846f1bbd5803217272c34fbf3`)
- [observation/documented] The backend exposes REST endpoints for uploading and listing session attachments (POST/GET /api/uploads/{session_id}), artifact-event polling, per-artifact download with meta/stream modes, and a whole-session zip download, with WebSocket mirrors emitting artifact_created events. -- evidence: [docs/user_guide/en/attachments.md#L24-L25](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L24-L25), [docs/user_guide/en/attachments.md#L32-L48](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L32-L48), [docs/user_guide/en/attachments.md#L57-L58](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L57-L58), [docs/user_guide/en/attachments.md#L51-L54](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L51-L54), [docs/user_guide/en/attachments.md#L9-L21](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/attachments.md#L9-L21) (`clm_22bd14b15df8dbd9ebc8176eeff6373582dca5b86d068bd7e400e26849491547`)
- [observation/documented] The web console includes a visual drag-and-drop workflow canvas for configuring node parameters and context flows, plus a Launch tab to run workflows, watch real-time logs, inspect artifacts, and give human-in-the-loop feedback. -- evidence: [README.md#L241-L242](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L241-L242), [README.md#L238-L239](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L238-L239) (`clm_a699ba226554947ccf84644cbaf2b34b2b7d08329a9439ff670f6cd86989670f`)

## memory-state (2 claim(s))

- [observation/documented] The memory system offers four built-in store types: simple (FAISS plus semantic rerank, read/write), file (read-only vector index over documents), blackboard (append-only recency log), and mem0 (cloud-managed, requires the mem0ai package). -- evidence: [docs/user_guide/en/modules/memory.md#L46-L51](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/modules/memory.md#L46-L51) (`clm_d7537b2c88ec5bfdb16c8b73c39c243c7eb6238b84151fa60e4b0e0b31c1a060`)
- [observation/documented] Agent nodes attach memories via MemoryAttachmentConfig with fields for store name, retrieve_stage, top_k (default 3), similarity_threshold, and read/write flags; retrieved items are injected into the agent context and writes occur after node completion. -- evidence: [docs/user_guide/en/modules/memory.md#L6-L9](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/modules/memory.md#L6-L9), [docs/user_guide/en/modules/memory.md#L64-L87](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/modules/memory.md#L64-L87), [docs/user_guide/en/modules/memory.md#L56-L62](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/docs/user_guide/en/modules/memory.md#L56-L62) (`clm_4b0c04c68b0b3663363980086499526722e0b608797c34729b7dcd0b62314c27`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are macOS/Linux/WSL/Windows, Python 3.12+, Node.js 18+, and the uv package manager; Python dependencies are synced with uv sync and frontend dependencies with npm install. -- evidence: [README.md#L106-L109](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L106-L109), [README.md#L118-L121](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L118-L121), [README.md#L113-L116](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L113-L116) (`clm_563418ec0285f29a25a49e207e04deb499f4416b56c9d1a38e968891fe508b39`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Out-of-the-box YAML workflow templates ship in yaml_instance/, covering data visualization, Blender-based 3D generation, game development, deep research, and teaching-video scenarios. -- evidence: [README.md#L285-L287](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L285-L287), [README.md#L291-L297](https://github.com/OpenBMB/ChatDev/blob/4fb2db0ea90375ce1059f44fe03ffbd191a7a169/README.md#L291-L297) (`clm_65d83930604d5d2125e877ac5333874b17ed6a6c1171b977ac64ac067dae2941`)

