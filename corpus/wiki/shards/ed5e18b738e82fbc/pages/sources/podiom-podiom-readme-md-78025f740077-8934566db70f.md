---
access: public
aliases: []
claim_ids:
- clm_0464bd7c1caae66a132c5829bca2041f41dd5249ed25e236212e939ee8b18f60
- clm_4fdf498203856b650c8e8c6c71458f9585a556b079b559c5b904387b1cf8196c
- clm_5e8e3a9635acf947cdc2955879fa04f99cb272a4b432ede53b7e636e4efa1d5c
- clm_66d8978da7faff08f30f285bd52810e420214e5d3982b88a2cf7b8d7e74aec09
- clm_8040fb01daba8a75b63cd13f5668dd58ccb3ab9b1192368a0c4adbe336e8d767
- clm_a93c12d1c4874d76db8dd80f5a75b5ca0fb7015820cb0ceee237d2f625173ee7
- clm_c08851172ef66a32e702defd2c6498a685fa13b306492abbd9b6f965034fc58a
- clm_c7978f1f3f7cee387ead86ac6a5fc25a82c330faea9d2540c15615fc2ecab7fc
- clm_ddf17bd31007bce13bf48a694c7530e45d25b953694cec5b3261ded43d03c321
- clm_fb975e63c4deff15c7cbd8230e1d99226cd9ed3b8423ea3a2c574c84df73bd52
- clm_fbd6e12dc15f991c4eadb946711ba4e393557d97a47701d38f23e4d0c5d1eeb8
maturity: draft
page_id: pg_d0ccd95f6cc2529baf828934566db70f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bddcfe8e41e758169cb1ca925f75f8b9
title: Podiom/Podiom/README.md @ 78025f740077
updated_at: '2026-09-14T02:31:29Z'
---

# Podiom/Podiom/README.md @ 78025f740077

<!-- rcw:begin owner=source:src_bddcfe8e41e758169cb1ca925f75f8b9 block=evidence -->
- Goals run deliberately autonomously: the lead agent and linked tasks or schedules run with full access and no per-action approval prompts, while tool activity is recorded on the goal timeline. [@claim:clm_0464bd7c1caae66a132c5829bca2041f41dd5249ed25e236212e939ee8b18f60]
- The layout includes a thin CLI client (cmd/podiom), a daemon combining web server, scheduler, and core (cmd/podiomd), internal packages, and a Svelte/Vite/TypeScript/Tailwind web UI built into podiomd. [@claim:clm_4fdf498203856b650c8e8c6c71458f9585a556b079b559c5b904387b1cf8196c]
- Podiom stores a canonical history for every session and can replay that history onto a fresh backing CLI session when the provider or profile changes. [@claim:clm_5e8e3a9635acf947cdc2955879fa04f99cb272a4b432ede53b7e636e4efa1d5c]
- The web UI defaults to 127.0.0.1:8787, with bind address and port configurable via server.bind and server.port in config.yaml; a browser-native WebSocket endpoint at /api/ws is also documented. [@claim:clm_66d8978da7faff08f30f285bd52810e420214e5d3982b88a2cf7b8d7e74aec09]
- The project targets developers already using Claude Code or OpenAI Codex locally who want persistent, reviewable agent work, recurring jobs, project context, and an audit trail in one workspace. [@claim:clm_8040fb01daba8a75b63cd13f5668dd58ccb3ab9b1192368a0c4adbe336e8d767]
- The podiomd daemon embeds the web SPA and uses pure-Go SQLite, so it needs no external web assets or cgo at runtime. [@claim:clm_a93c12d1c4874d76db8dd80f5a75b5ca0fb7015820cb0ceee237d2f625173ee7]
- Native iOS and Android mobile apps can connect to standalone daemons or an opt-in, API-only Home Assistant LAN endpoint, and the same core can run as a Home Assistant add-on or in a container. [@claim:clm_c08851172ef66a32e702defd2c6498a685fa13b306492abbd9b6f965034fc58a]
- Podiom is local-first: all runtime state lives under one overridable root ($PODIOM_HOME, defaulting to ~/.podiom/), and provider CLIs keep their native authentication and policy controls. [@claim:clm_c7978f1f3f7cee387ead86ac6a5fc25a82c330faea9d2540c15615fc2ecab7fc]
- The repository points to docs/requirements/foundation.md as the authoritative foundation specification, at version v1.6. [@claim:clm_ddf17bd31007bce13bf48a694c7530e45d25b953694cec5b3261ded43d03c321]
- Podiom does not replace the provider runtime; it shells out to the native claude and codex CLIs and reuses their models, MCP servers, tools, skills, and authentication. [@claim:clm_fb975e63c4deff15c7cbd8230e1d99226cd9ed3b8423ea3a2c574c84df73bd52]
- A goal gives one lead agent an outcome to own over days or weeks; the agent turns it into roadmap tasks and schedules, delegates work, and records periodic reviews with progress, evidence, and next steps. [@claim:clm_fbd6e12dc15f991c4eadb946711ba4e393557d97a47701d38f23e4d0c5d1eeb8]
<!-- rcw:end owner=source:src_bddcfe8e41e758169cb1ca925f75f8b9 block=evidence -->

## Researcher notes

