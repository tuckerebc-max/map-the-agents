---
access: public
aliases: []
claim_ids:
- clm_03cc7b432c12c3be37e9a8870a9edf744179ae78dfb98bb3dfb1ab2b00c6e3f3
- clm_18ed2feda03bc1f4f46b297704a9367036b2020add5c72963f017106970c6599
- clm_4506f8b38ee393ced746c211673e7b403dcdd1482331c2dabe45e77338399461
- clm_51006d9adba37f417f12e4232d397046d0326a05d0c8b0ba8ff167d975246c30
- clm_b3504277c27aa4649ffd15b827c3f78a5b528562e3431fb2e514733cca2ecc58
- clm_dc94f19a8d5716d4c22bb8c9e4d60b00b209905d4a517e7d8395e95510d34493
- clm_f2c77567cc1282f620102fd97e3cb101abd5a8eaf77548312e477c73d6ef9e70
maturity: draft
page_id: pg_b190b6976bba5733a84feac209b39809
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6345424397fd56d0aff4255986966f5e
title: ValueCell-ai/valuecell/docs/CONFIGURATION_GUIDE.md @ 9793e9c0563f
updated_at: '2026-09-14T04:28:53Z'
---

# ValueCell-ai/valuecell/docs/CONFIGURATION_GUIDE.md @ 9793e9c0563f

<!-- rcw:begin owner=source:src_6345424397fd56d0aff4255986966f5e block=evidence -->
- Configuration uses a three-tier system: environment variables override .env file settings, which override YAML defaults stored under python/configs/. [@claim:clm_03cc7b432c12c3be37e9a8870a9edf744179ae78dfb98bb3dfb1ab2b00c6e3f3]
- OKX trading defaults to a paper environment, and OKX_ALLOW_LIVE_TRADING defaults to false and must be set to true before orders are routed to mainnet. [@claim:clm_18ed2feda03bc1f4f46b297704a9367036b2020add5c72963f017106970c6599]
- The system auto-detects a primary provider from available API keys in a priority order starting with OpenRouter, SiliconFlow, Google, OpenAI, OpenAI-compatible, and Azure; this can be overridden via PRIMARY_PROVIDER or disabled with AUTO_DETECT_PROVIDER=false. [@claim:clm_4506f8b38ee393ced746c211673e7b403dcdd1482331c2dabe45e77338399461]
- If the primary provider fails, the system automatically tries fallback providers built from other enabled providers with valid keys, stopping at the first successful model creation; fallback can be overridden or disabled per agent with use_fallback: false. [@claim:clm_51006d9adba37f417f12e4232d397046d0326a05d0c8b0ba8ff167d975246c30]
- The application stores local data in a LanceDB directory, a knowledge directory, and a SQLite database file (valuecell.db) under the system application directory, and users may delete these to reset state. [@claim:clm_b3504277c27aa4649ffd15b827c3f78a5b528562e3431fb2e514733cca2ecc58]
- Repository setup instructions: clone the repo, copy .env.example to .env and add API keys, then launch everything with bash start.sh (Linux/macOS) or .\start.ps1 (Windows PowerShell). [@claim:clm_dc94f19a8d5716d4c22bb8c9e4d60b00b209905d4a517e7d8395e95510d34493]
- Agent YAML configs support per-provider model mappings (provider_models) and env_overrides, suggesting agents can run different models per provider and be tuned at runtime without code changes. [@claim:clm_f2c77567cc1282f620102fd97e3cb101abd5a8eaf77548312e477c73d6ef9e70]
<!-- rcw:end owner=source:src_6345424397fd56d0aff4255986966f5e block=evidence -->

## Researcher notes

