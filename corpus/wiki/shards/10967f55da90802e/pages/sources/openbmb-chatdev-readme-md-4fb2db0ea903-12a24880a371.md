---
access: public
aliases: []
claim_ids:
- clm_267909084b2727ecf4b3a5f6b655ea8f8055cb5846f1bbd5803217272c34fbf3
- clm_2ffa16cbf093b932782b37191564262314acb9ccd74b5c51171327494dd7d1ba
- clm_563418ec0285f29a25a49e207e04deb499f4416b56c9d1a38e968891fe508b39
- clm_65d83930604d5d2125e877ac5333874b17ed6a6c1171b977ac64ac067dae2941
- clm_7743aebec48fc5047881a063b8487fe6e227b507c1366ec778bfa6e9c13272a2
- clm_a699ba226554947ccf84644cbaf2b34b2b7d08329a9439ff670f6cd86989670f
- clm_b436a660288c396288fbd47e94f772cdd08e2eb1d3104f4684ac14685c15d8f7
- clm_d4261314489e9628f0af62079f341f006bc760f9e1c3aad9245c98fb517d401c
- clm_f1d65bd27a4a9c5932319a3e835f4db76905fef863fc658bb5f45857d7295953
maturity: draft
page_id: pg_4f4a92409eec5ae1860312a24880a371
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0656200055b95265931bfe038a70db9b
title: OpenBMB/ChatDev/README.md @ 4fb2db0ea903
updated_at: '2026-09-14T02:26:10Z'
---

# OpenBMB/ChatDev/README.md @ 4fb2db0ea903

<!-- rcw:begin owner=source:src_0656200055b95265931bfe038a70db9b block=evidence -->
- A Python SDK exposes run_workflow (from runtime.sdk) taking a YAML file, task prompt, attachments, and variable overrides, returning a result with a final message; it is also published on PyPI as chatdev 0.1.0. [@claim:clm_267909084b2727ecf4b3a5f6b655ea8f8055cb5846f1bbd5803217272c34fbf3]
- The project is modular: server/ hosts the FastAPI backend, runtime/ handles agent abstraction and tool execution, workflow/ contains multi-agent logic driven by entity/ configs, frontend/ is a Vue 3 web console, and functions/ holds custom Python tools. [@claim:clm_2ffa16cbf093b932782b37191564262314acb9ccd74b5c51171327494dd7d1ba]
- Prerequisites are macOS/Linux/WSL/Windows, Python 3.12+, Node.js 18+, and the uv package manager; Python dependencies are synced with uv sync and frontend dependencies with npm install. [@claim:clm_563418ec0285f29a25a49e207e04deb499f4416b56c9d1a38e968891fe508b39]
- Out-of-the-box YAML workflow templates ship in yaml_instance/, covering data visualization, Blender-based 3D generation, game development, deep research, and teaching-video scenarios. [@claim:clm_65d83930604d5d2125e877ac5333874b17ed6a6c1171b977ac64ac067dae2941]
- The application can be started with make dev, or manually via uv run python server_main.py --port 6400 for the backend and a frontend dev server on port 5173 with VITE_API_BASE_URL pointing at the backend. [@claim:clm_7743aebec48fc5047881a063b8487fe6e227b507c1366ec778bfa6e9c13272a2]
- The web console includes a visual drag-and-drop workflow canvas for configuring node parameters and context flows, plus a Launch tab to run workflows, watch real-time logs, inspect artifacts, and give human-in-the-loop feedback. [@claim:clm_a699ba226554947ccf84644cbaf2b34b2b7d08329a9439ff670f6cd86989670f]
- ChatDev 1.0, the legacy 'Virtual Software Company' with CEO/CTO/Programmer-style agents automating the software lifecycle, has been moved to the chatdev1.0 branch for maintenance. [@claim:clm_b436a660288c396288fbd47e94f772cdd08e2eb1d3104f4684ac14685c15d8f7]
- ChatDev 2.0 (DevAll) is described as a zero-code multi-agent platform where users define agents, workflows, and tasks via configuration for scenarios such as data visualization, 3D generation, and deep research. [@claim:clm_d4261314489e9628f0af62079f341f006bc760f9e1c3aad9245c98fb517d401c]
- Alternatively the whole application runs via Docker Compose (docker compose up --build) with backend on port 6400 and frontend on 5173; services auto-restart on crash and local file changes are reflected in containers. [@claim:clm_f1d65bd27a4a9c5932319a3e835f4db76905fef863fc658bb5f45857d7295953]
<!-- rcw:end owner=source:src_0656200055b95265931bfe038a70db9b block=evidence -->

## Researcher notes

