---
access: public
aliases: []
claim_ids:
- clm_8141ac0b14231c34891f04b36e5d88977d6b87daaf4c3a01491b032603aa6c72
- clm_ced59a7192c83745f8472f380955637039c2e38d8ff74f098112075da7924777
- clm_d047a4e819a9404006cb9dcd01b8ab54e6ed2c63f46b08f437e0b5c53b6e97a8
maturity: draft
page_id: pg_c561de93e1865979bef5b5a7e7937ee1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_54765066e7db500a9bc7357a310fcf15
title: yashdev9274/supercli/cortex-sdk.md @ fbc5af280127
updated_at: '2026-09-14T03:24:55Z'
---

# yashdev9274/supercli/cortex-sdk.md @ fbc5af280127

<!-- rcw:begin owner=source:src_54765066e7db500a9bc7357a310fcf15 block=evidence -->
- cortex-sdk exposes createGateway() returning a Vercel AI SDK LanguageModel with listModels() discovery, supporting eight gateway providers including ConcentrateAI, OpenRouter, Gemini, MiniMax, NVIDIA NIM, and a server-proxied Supercode Cloud. [@claim:clm_8141ac0b14231c34891f04b36e5d88977d6b87daaf4c3a01491b032603aa6c72]
- cortex-sdk provides tool modules: createAgentHandler() (MergeDev MCP tool packs), createWebSearch() (Exa, Firecrawl, Context.dev), createComposio() (local SDK or server-proxied modes), createMcpManager() (GitHub/Linear/Slack/custom), and voice STT/TTS, all returning AI SDK Tool records. [@claim:clm_ced59a7192c83745f8472f380955637039c2e38d8ff74f098112075da7924777]
- A SupercodeAgent class combines gateway, agent-handler, composio, web search, MCP servers, and voice configuration in a single constructor object. [@claim:clm_d047a4e819a9404006cb9dcd01b8ab54e6ed2c63f46b08f437e0b5c53b6e97a8]
<!-- rcw:end owner=source:src_54765066e7db500a9bc7357a310fcf15 block=evidence -->

## Researcher notes

