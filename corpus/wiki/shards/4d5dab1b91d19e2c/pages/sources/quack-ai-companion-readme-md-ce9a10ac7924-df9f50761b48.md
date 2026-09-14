---
access: public
aliases: []
claim_ids:
- clm_0a7b2c2a1c47d5470773e1fc2e962cdb5331c1dfa017704324a31ac9c8bb8e4d
- clm_4530cec3cddd4e68c27607137f5dd083f721264c868049af5ec0433fce43a2da
- clm_7cb942447a13189d9f297255c689e772652df493ae1b9c3acd8a1c542e9094a5
- clm_9defe6bf36c82621edfc5fea7eca0ad5ea4085b320ae4fea1315123ad36f3b82
- clm_d0c2a2898f9f9ef3d08827e52a68b8953193e960ded1b6d40c0186ff94f60961
maturity: draft
page_id: pg_7dd2e5698f8c57cb951bdf9f50761b48
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_46bdd9a644f35a928458901f0c83808a
title: quack-ai/companion/README.md @ ce9a10ac7924
updated_at: '2026-09-14T04:17:13Z'
---

# quack-ai/companion/README.md @ ce9a10ac7924

<!-- rcw:begin owner=source:src_46bdd9a644f35a928458901f0c83808a block=evidence -->
- The product exposes a REST API for guideline management and LLM inference, browsable via Swagger docs at localhost:5050/docs or through HTTP requests. [@claim:clm_0a7b2c2a1c47d5470773e1fc2e962cdb5331c1dfa017704324a31ac9c8bb8e4d]
- A code chat endpoint is offered as a coding-specific LLM chat, with the backend API acting as gatekeeper for an Ollama-powered inference container. [@claim:clm_4530cec3cddd4e68c27607137f5dd083f721264c868049af5ec0433fce43a2da]
- Running the service requires Git, Docker, Docker Compose, and the NVIDIA Container Toolkit with a GPU of at least 6 GB VRAM for good latency. [@claim:clm_7cb942447a13189d9f297255c689e772652df493ae1b9c3acd8a1c542e9094a5]
- Quack Companion targets software teams, acting like an onboarded team member with knowledge of internal libraries and coding standards, and is positioned against GitHub Copilot with team-guideline context. [@claim:clm_9defe6bf36c82621edfc5fea7eca0ad5ea4085b320ae4fea1315123ad36f3b82]
- A deployment includes a backend API on port 5050, an APM dashboard on port 3000, and a Gradio chat interface on port 7860. [@claim:clm_d0c2a2898f9f9ef3d08827e52a68b8953193e960ded1b6d40c0186ff94f60961]
<!-- rcw:end owner=source:src_46bdd9a644f35a928458901f0c83808a block=evidence -->

## Researcher notes

