---
access: public
aliases: []
claim_ids:
- clm_08c1442c8ba39b44ad195fc4f799f82db630b67adde1d4462d9faa7388cc4a99
- clm_117813620b870bc6441ccc1278877749b78300ab93e19feb74cb46c736d9a13f
- clm_3eb5905676aaa9b01f870acc7cba1c41ecaa6ebe95979991b3cdde6d7184b29b
- clm_49c25e9e4c714aa8c5ff0386c2b77d3f42de2833fc38028ce18331f7420d7917
- clm_ab89b3e6f087705482b6c66f6b7487d2acc55f07efc9bd120e7e31a254b1fd25
- clm_b102b6fbf0dd73b87495b80b328e6fd09ac258d037bc803aa0c14527fd5e220d
- clm_b5778ec096c8aedf70bda1d8e9768c89805135737f4f2341627da89487741738
- clm_c4e24fcc04fef0d130e6b37aaa2389bbdbb1304395e66cd59b6820e67fe33d80
- clm_f1c91aec83a0e9718c944ae4ea5faa2012761c4654b0ee3e5d2bc82d01b4a720
- clm_fc6129a93846711e98cfe1c967e72301cac361acb4a3e2253bf8319653df7d71
maturity: draft
page_id: pg_6957b22d860c5de19fa94cf1a3c3bfac
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1a51db768e475ba89850aa4383e53641
title: OpenHands/OpenHands/README.md @ 28464621d879
updated_at: '2026-09-14T02:27:26Z'
---

# OpenHands/OpenHands/README.md @ 28464621d879

<!-- rcw:begin owner=source:src_1a51db768e475ba89850aa4383e53641 block=evidence -->
- Running without a sandbox executes the agent-server directly on the host, where the agent has full filesystem access; the Docker option restricts agent access to projects under PROJECTS_PATH. [@claim:clm_08c1442c8ba39b44ad195fc4f799f82db630b67adde1d4462d9faa7388cc4a99]
- Non-sandboxed installs require Node.js 22.12.x or later and uv; the Docker option requires Docker Desktop or Engine and a PROJECTS_PATH host directory. [@claim:clm_117813620b870bc6441ccc1278877749b78300ab93e19feb74cb46c736d9a13f]
- Agent Canvas is described as a self-hosted developer control center for coding agents and automations, currently in beta status. [@claim:clm_3eb5905676aaa9b01f870acc7cba1c41ecaa6ebe95979991b3cdde6d7184b29b]
- The UI is served at localhost:8000 for npm/source launches and at /canvas for the Docker image, with backends addable from the UI. [@claim:clm_49c25e9e4c714aa8c5ff0386c2b77d3f42de2833fc38028ce18331f7420d7917]
- Agent Canvas is powered by the OpenHands Agent Server, a REST API for running multiple agents on one machine; the frontend can connect to and switch between multiple Agent Servers. [@claim:clm_ab89b3e6f087705482b6c66f6b7487d2acc55f07efc9bd120e7e31a254b1fd25]
- The project is split across repositories: this repo owns the frontend, backend selection, and local-stack orchestration, while the SDK owns the Agent Server API and the automation repo owns scheduling and dispatching. [@claim:clm_b102b6fbf0dd73b87495b80b328e6fd09ac258d037bc803aa0c14527fd5e220d]
- The agent-canvas CLI starts the full local stack by default and supports --frontend-only and --backend-only flags to run pieces separately. [@claim:clm_b5778ec096c8aedf70bda1d8e9768c89805135737f4f2341627da89487741738]
- Repository development practice: contributors are directed to AGENTS.md for contributor-specific repository boundaries and a required custom code-review guide. [@claim:clm_c4e24fcc04fef0d130e6b37aaa2389bbdbb1304395e66cd59b6820e67fe33d80]
- An Automation Server can be paired with the Agent Server to run agents on a schedule or in response to events, dispatching conversations to the Agent Server/SDK. [@claim:clm_f1c91aec83a0e9718c944ae4ea5faa2012761c4654b0ee3e5d2bc82d01b4a720]
- It can run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. [@claim:clm_fc6129a93846711e98cfe1c967e72301cac361acb4a3e2253bf8319653df7d71]
<!-- rcw:end owner=source:src_1a51db768e475ba89850aa4383e53641 block=evidence -->

## Researcher notes

