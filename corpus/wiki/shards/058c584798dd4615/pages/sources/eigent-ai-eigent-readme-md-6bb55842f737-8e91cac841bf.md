---
access: public
aliases: []
claim_ids:
- clm_0ab86833e6e549ddf792003e7b969a19691d2b71bf393cfa5d2df659608d989a
- clm_0cd1cfba6dc6c4de7008977af3236f8fe7838de1843c877af098eab435172096
- clm_108e42a45a15a216322d2142ab3cc82dabcd518cb3d0f2ac330d8a3a39d141fe
- clm_36f76731b7f637e0c9704612d5725b8cec9547cd996805606e70da93e9fda16e
- clm_3ddca9421ca9d823ab50eb698e2b57535c00f670b98948439c2e2107d9734d0b
- clm_558e64a638d1e4bf58cc9ddc47b2c286bfdd8a1534d496465c6eda0c5fe73a5d
- clm_5e89279db8a8c38249c09d3ca72fe98ccb4515a475f9c93f80f6818020a80cff
- clm_b7ec62227388422a78b4c64e18238f81600a2d5a3a5b32f5e91188cc1674ce12
- clm_bc70d67b67758725482d6cbe426c0108e785faa7ddbd66d27c4fd4c94933ef90
- clm_fccba73c762e329c65466b47e46329450495d51d8ef2216839039a64e1a37fe7
maturity: draft
page_id: pg_e5316ab284e6529db2ec8e91cac841bf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_48d331a0d37657eaaf6626ff4f92e431
title: eigent-ai/eigent/README.md @ 6bb55842f737
updated_at: '2026-09-14T01:47:11Z'
---

# eigent-ai/eigent/README.md @ 6bb55842f737

<!-- rcw:begin owner=source:src_48d331a0d37657eaaf6626ff4f92e431 block=evidence -->
- The roadmap table lists items such as prompt caching, context compression, fixed-workflow workforce support, and forbidding repeated page visits as future work, suggesting these capabilities are not yet present. [@claim:clm_0ab86833e6e549ddf792003e7b969a19691d2b71bf393cfa5d2df659608d989a]
- The product is stated to be model agnostic, supporting cloud APIs, enterprise gateways, or local inference without vendor lock-in. [@claim:clm_0cd1cfba6dc6c4de7008977af3236f8fe7838de1843c877af098eab435172096]
- The product advertises a multi-agent workforce that divides work among specialized agents, collaborates in parallel, and executes multi-step workflows, alongside a single-agent mode for focused tasks. [@claim:clm_108e42a45a15a216322d2142ab3cc82dabcd518cb3d0f2ac330d8a3a39d141fe]
- The backend stack is documented as FastAPI with uv as package manager, Uvicorn as async server, OAuth 2.0 and Passlib for authentication, and CAMEL as the multi-agent framework. [@claim:clm_36f76731b7f637e0c9704612d5725b8cec9547cd996805606e70da93e9fda16e]
- Eigent is described as an open-source Cowork desktop application for building, managing, and deploying a custom AI workforce that automates complex workflows. [@claim:clm_3ddca9421ca9d823ab50eb698e2b57535c00f670b98948439c2e2107d9734d0b]
- The README lists built-in browser and terminal toolkits, MCP integration, and skill integration as product capabilities. [@claim:clm_558e64a638d1e4bf58cc9ddc47b2c286bfdd8a1534d496465c6eda0c5fe73a5d]
- Local deployment is the recommended mode: a local backend server with full API, local model integration (vLLM, Ollama, LM Studio, etc.), and complete isolation from cloud services with no account required. [@claim:clm_5e89279db8a8c38249c09d3ca72fe98ccb4515a475f9c93f80f6818020a80cff]
- Repository development practice: the cloud-connected quick start instructs cloning the repo, running npm install and npm run dev (Node.js 18-22 required), and notes this mode connects to Eigent cloud services and needs account registration. [@claim:clm_b7ec62227388422a78b4c64e18238f81600a2d5a3a5b32f5e91188cc1674ce12]
- Repository development practice: after pulling new code, contributors are told to update frontend dependencies with npm install and backend Python dependencies via 'cd backend && uv sync'. [@claim:clm_bc70d67b67758725482d6cbe426c0108e785faa7ddbd66d27c4fd4c94933ef90]
- The frontend is documented as React with Electron for the desktop app, TypeScript, Tailwind CSS, Radix UI, Zustand for state, and React Flow as flow editor. [@claim:clm_fccba73c762e329c65466b47e46329450495d51d8ef2216839039a64e1a37fe7]
<!-- rcw:end owner=source:src_48d331a0d37657eaaf6626ff4f92e431 block=evidence -->

## Researcher notes

