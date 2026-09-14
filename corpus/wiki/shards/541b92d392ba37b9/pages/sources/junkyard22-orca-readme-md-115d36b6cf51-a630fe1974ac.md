---
access: public
aliases: []
claim_ids:
- clm_535e1bfb1eab9bace3ae8c248b38fb7a67f3e9f44a911fe520ad1305fce40421
- clm_694d6565274dc346fd837da59454ac7a77ec868ab0c740616abdab1ca043a6b7
- clm_7aefcefb2fb27703cfa27afeb5109acce9b9c2443bf02780a24db51691efd7a0
- clm_db101c06b220ca423ece0da336cf784530718a49b4604c5ad283184a3281a9b5
- clm_faaffa4602291bda137cbc7b1805486c72599f759b38ee556bebde40da8255c8
maturity: draft
page_id: pg_6a6b1a3a0595508aac4ba630fe1974ac
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2f97b24b62ef54f7ac0a6d1290da55f9
title: junkyard22/Orca/README.md @ 115d36b6cf51
updated_at: '2026-09-14T02:08:27Z'
---

# junkyard22/Orca/README.md @ 115d36b6cf51

<!-- rcw:begin owner=source:src_2f97b24b62ef54f7ac0a6d1290da55f9 block=evidence -->
- The desktop composer's Cargo tray accepts /repo, /file, /task, /connect, /context, /status commands plus @repo/@file/@task/@connector references, storing resources as typed references rather than raw contents. [@claim:clm_535e1bfb1eab9bace3ae8c248b38fb7a67f3e9f44a911fe520ad1305fce40421]
- The product ships two frontends: an Electron desktop GUI (settings UI, chat view, session history) and a CLI runner that accepts prompts as arguments or via stdin piping. [@claim:clm_694d6565274dc346fd837da59454ac7a77ec868ab0c740616abdab1ca043a6b7]
- LLM providers are configurable via env: OpenRouter (OPENROUTER_API_KEY) or local Ollama (base URL and model), with role-to-model mappings in orca-settings.json. [@claim:clm_7aefcefb2fb27703cfa27afeb5109acce9b9c2443bf02780a24db51691efd7a0]
- The runtime is organized as packages: benson-core (intent parsing), orca-core (runtime, event bus, SQLite persistence), maestro-core (role routing), pappy-core (QC verdicts), miranda-core (compliance gate), workbench-core (tool execution), and dewey-core (context store). [@claim:clm_db101c06b220ca423ece0da336cf784530718a49b4604c5ad283184a3281a9b5]
- The pipeline routes user input through Benson (intent parsing) to an Orca Runtime that orchestrates Maestro role routing, Pappy QC (PASS/WARN/FAIL), and Miranda compliance with a repair loop. [@claim:clm_faaffa4602291bda137cbc7b1805486c72599f759b38ee556bebde40da8255c8]
<!-- rcw:end owner=source:src_2f97b24b62ef54f7ac0a6d1290da55f9 block=evidence -->

## Researcher notes

