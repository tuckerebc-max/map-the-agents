---
access: public
aliases: []
claim_ids:
- clm_10738a84ae8a5c40333dae4b7d234da071e60f149fb3450f0c371add05df5c03
- clm_2574fcc0d7192f0e518aa333e120723f9c1a8689d6402651d23061a52fabb610
- clm_2bcce282001139f87d0a575e4774cc413c81d91cdaecc4310a7eb97d5162b2ca
- clm_4be89e5603cecca9a2c4879c99754cf8ed4e7e9e24820518a2ae7c6cf5181168
- clm_53489c4dc7e5318f25427c5258596f1dae9d64effd323d4f3e81bf4db0bc71f1
- clm_5a72d87d8b89691b749df72ffeb0b5aa3602ad41667d4b164f00e6bf50d47e59
- clm_6a619053d3c8c33b4adc284171e8b6f5c6f605d5a0e7cc31264cc1d85a56445a
- clm_7d546220dc7b7da41cf5bd1779f0cc7c4af72f63c315906bd695e7f53db69d9f
- clm_9200b6d65b1efc5773ad8c317b4870892c38bedd8cb33647f6315960b3616376
- clm_d09ed34ba44adb907c7d58ba2c0a449fe82e5c13fc10a377b34794a33ee20c27
- clm_dae648e1fc1c91a4ae29edac5cb7afd913e049f52fa30b233d767cdc10b40202
maturity: draft
page_id: pg_422de6ef1e715f80a6c8cc4da48679aa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_55e20fb939e354f3980a147d38eab167
title: omnara-ai/omnara/README.md @ 1d62b055ebb4
updated_at: '2026-09-14T02:24:35Z'
---

# omnara-ai/omnara/README.md @ 1d62b055ebb4

<!-- rcw:begin owner=source:src_55e20fb939e354f3980a147d38eab167 block=evidence -->
- Users bring their own API keys and models via compatible endpoints (OpenRouter, LiteLLM, Ollama), with OpenAI Responses, Chat Completions, and Anthropic Messages formats supported. [@claim:clm_10738a84ae8a5c40333dae4b7d234da071e60f149fb3450f0c371add05df5c03]
- The platform includes role-based access control with organization and project roles for users and API keys, separating management, configuration, operation, and viewing. [@claim:clm_2574fcc0d7192f0e518aa333e120723f9c1a8689d6402651d23061a52fabb610]
- Local development defaults are intentionally insecure and the README warns against using them in deployed environments, pointing to the self-hosting guide for production setup. [@claim:clm_2bcce282001139f87d0a575e4774cc413c81d91cdaecc4310a7eb97d5162b2ca]
- Agent state is committed atomically to Postgres, and agents recover automatically from crashes, restarts, and machine disconnects. [@claim:clm_4be89e5603cecca9a2c4879c99754cf8ed4e7e9e24820518a2ae7c6cf5181168]
- Self-hosting requires Docker with Compose; published images can be run or the stack built from source via docker compose with the app profile. [@claim:clm_53489c4dc7e5318f25427c5258596f1dae9d64effd323d4f3e81bf4db0bc71f1]
- Omnara targets developers building agents for internal or customer-facing products and teams interacting with agents through the dashboard or a first-party Slack connector. [@claim:clm_5a72d87d8b89691b749df72ffeb0b5aa3602ad41667d4b164f00e6bf50d47e59]
- The product is usable programmatically via a CLI, a TypeScript CLI, and a REST API; profiles are created and agents launched with npx omnara commands. [@claim:clm_6a619053d3c8c33b4adc284171e8b6f5c6f605d5a0e7cc31264cc1d85a56445a]
- Agents can run on sandboxes from Blaxel, Daytona, Modal, or Unikraft, on user machines, or a mix, and machines can be added or removed while an agent runs. [@claim:clm_7d546220dc7b7da41cf5bd1779f0cc7c4af72f63c315906bd695e7f53db69d9f]
- Repository development practice: source development needs the Go version in go.mod, Node.js 24+ with Corepack, and Docker Compose; verification runs via make verify, with integration, service e2e, and credential-gated live test targets. [@claim:clm_9200b6d65b1efc5773ad8c317b4870892c38bedd8cb33647f6315960b3616376]
- The REST API is defined in api/openapi/openapi.yaml and served under /api/v1. [@claim:clm_d09ed34ba44adb907c7d58ba2c0a449fe82e5c13fc10a377b34794a33ee20c27]
- Agents are defined in an agent.yaml profile containing an instruction and a model section with provider_config and model name. [@claim:clm_dae648e1fc1c91a4ae29edac5cb7afd913e049f52fa30b233d767cdc10b40202]
<!-- rcw:end owner=source:src_55e20fb939e354f3980a147d38eab167 block=evidence -->

## Researcher notes

