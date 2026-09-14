---
access: public
aliases: []
claim_ids:
- clm_05adf1dbd5acc75a3ba51bffc8cfb4f07e4c07f801645595fc3e82a593b95ca5
- clm_31c2f30736151c5c29b14451ea58282c1f34b0e1b5ed5db46f4193309f006ba0
- clm_480bb4483b59ecd8f3f493b55e2845d1169cb1af32b4ebc759139612b4e030e4
- clm_6bf53e54f33c3a9316354f670cf4bf87d52e19c91cb99c39e9a9eda248cc2b34
- clm_873b896b0447d5efebc617f6830390d175fce36af2e3cea7443697f22e23b3fc
- clm_97479ad2a9c88ee3de0902260f1a81ed1753c63e9308e3d10d2b43133089d323
- clm_cccb0f6569f54d2856c1eef97db14aa5f0b59343e7526222882d431d4e560744
maturity: draft
page_id: pg_b5fa8af522f8575d92b4fbc752b1094b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9d6ce2b11e9f516b8dc7c2b85a6877b0
title: Nano-Collective/nanocoder/docs/battlemap.md @ 0cb0afb026ef
updated_at: '2026-09-14T02:22:02Z'
---

# Nano-Collective/nanocoder/docs/battlemap.md @ 0cb0afb026ef

<!-- rcw:begin owner=source:src_9d6ce2b11e9f516b8dc7c2b85a6877b0 block=evidence -->
- Tool calling uses three paths: native function calling plus XML and JSON fallbacks, with malformed-output repair on both fallback paths so weaker or non-conforming models still work end to end. [@claim:clm_05adf1dbd5acc75a3ba51bffc8cfb4f07e4c07f801645595fc3e82a593b95ca5]
- A per-project daemon ('nanocoder daemon start') owns file-watch and cron event sources, letting Skills subscribe to file.changed or schedule.cron events and run headless without the TUI; launchd plist and systemd user-unit installers ship in-tree. [@claim:clm_31c2f30736151c5c29b14451ea58282c1f34b0e1b5ed5db46f4193309f006ba0]
- The project's own comparison doc acknowledges being behind peers in community size, surface breadth (no desktop or web app), extension depth relative to Pi, IDE-level code intelligence (LSP client only, no debugger integration), and distribution polish. [@claim:clm_480bb4483b59ecd8f3f493b55e2845d1169cb1af32b4ebc759139612b4e030e4]
- The cron-driven scheduler is documented as powered by the croner library. [@claim:clm_6bf53e54f33c3a9316354f670cf4bf87d52e19c91cb99c39e9a9eda248cc2b34]
- The agent supports 20+ providers: native cloud integrations (e.g. Anthropic, OpenAI, Google Gemini, OpenRouter, Copilot, Mistral, Z.ai), seven documented local servers (Ollama, llama.cpp, llama-swap, LM Studio, LocalAI, MLX Server, vLLM), and any custom OpenAI-compatible endpoint. [@claim:clm_873b896b0447d5efebc617f6830390d175fce36af2e3cea7443697f22e23b3fc]
- Nanocoder can run as an Agent Client Protocol agent via 'nanocoder --acp', exposing conversation, tool-calling, and permission flows to ACP-compatible editors such as Zed. [@claim:clm_97479ad2a9c88ee3de0902260f1a81ed1753c63e9308e3d10d2b43133089d323]
- Stated design principles are zero telemetry, zero tracking, and local-first operation, with the whole loop able to run on-machine against local models with no outbound network traffic. [@claim:clm_cccb0f6569f54d2856c1eef97db14aa5f0b59343e7526222882d431d4e560744]
<!-- rcw:end owner=source:src_9d6ce2b11e9f516b8dc7c2b85a6877b0 block=evidence -->

## Researcher notes

