---
access: public
aliases: []
claim_ids:
- clm_16deed8a2612548e48257be0810050eea35f78cebbd5b760d9ea4d86046d89a1
- clm_1fcfc26e753786f09c570b54eb2b2704ec4c21d9c2767af698644316a1315aca
- clm_4cdf94b760a195a2b3959e44a305bdfe09943b843439c98a51ee1afbab222b31
- clm_5a809f8d877300eaa620fbe4799da15e458ab6ace8bb8525735d81c96b6e594c
- clm_b3504277c27aa4649ffd15b827c3f78a5b528562e3431fb2e514733cca2ecc58
- clm_bf8f8b57007986f1ad5d712f00ecfcf67668a290832baf109edd7d0023008037
- clm_dc94f19a8d5716d4c22bb8c9e4d60b00b209905d4a517e7d8395e95510d34493
- clm_e0e69fe17f088275a5236923036589b46d34d9d614ba50369f0d6156ca66c424
- clm_ec0e79cadce8a4949affda4c97fb06a160f4bb6876835e4e0ec15c2c5442a216
maturity: draft
page_id: pg_907f35719f8c5cd4b80c0684903bcea8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8d99c6014e5e5fe5aa437b8983edac23
title: ValueCell-ai/valuecell/README.md @ 9793e9c0563f
updated_at: '2026-09-14T04:28:53Z'
---

# ValueCell-ai/valuecell/README.md @ 9793e9c0563f

<!-- rcw:begin owner=source:src_8d99c6014e5e5fe5aa437b8983edac23 block=evidence -->
- Users configure AI model API keys and exchange credentials (Binance, HyperLiquid, OKX, Coinbase) through the web interface, then create strategies combining models with exchanges and start/stop traders with real-time monitoring. [@claim:clm_16deed8a2612548e48257be0810050eea35f78cebbd5b760d9ea4d86046d89a1]
- Exchange connectivity is documented for OKX, Binance, and Hyperliquid as fully tested, with Coinbase, Gate.io, MEXC, and a Blockchain option listed as partially tested. [@claim:clm_1fcfc26e753786f09c570b54eb2b2704ec4c21d9c2767af698644316a1315aca]
- The project targets Python 3.12+ and is licensed under Apache 2.0, which applies only to original ValueCell code; third-party components like TradingView widgets and exchange/LLM APIs are governed by their own terms. [@claim:clm_4cdf94b760a195a2b3959e44a305bdfe09943b843439c98a51ee1afbab222b31]
- The product supports multiple LLM providers including OpenRouter, SiliconFlow, Azure, Google, OpenAI-compatible endpoints, OpenAI, and DeepSeek, per the README's integrations section. [@claim:clm_5a809f8d877300eaa620fbe4799da15e458ab6ace8bb8525735d81c96b6e594c]
- The application stores local data in a LanceDB directory, a knowledge directory, and a SQLite database file (valuecell.db) under the system application directory, and users may delete these to reset state. [@claim:clm_b3504277c27aa4649ffd15b827c3f78a5b528562e3431fb2e514733cca2ecc58]
- When launched, the application serves a web UI at http://localhost:1420 and streams backend and agent logs to the terminal. [@claim:clm_bf8f8b57007986f1ad5d712f00ecfcf67668a290832baf109edd7d0023008037]
- Repository setup instructions: clone the repo, copy .env.example to .env and add API keys, then launch everything with bash start.sh (Linux/macOS) or .\start.ps1 (Windows PowerShell). [@claim:clm_dc94f19a8d5716d4c22bb8c9e4d60b00b209905d4a517e7d8395e95510d34493]
- Live trading currently supports only contract (leverage) trading, with spot implemented as 1X contracts, so users must maintain sufficient contract account balance. [@claim:clm_e0e69fe17f088275a5236923036589b46d34d9d614ba50369f0d6156ca66c424]
- The README describes a multi-agent system including a DeepResearch Agent for analyzing fundamental documents, a Strategy Agent for multi-strategy crypto trading, and a News Retrieval Agent for scheduled news delivery, with more agents planned. [@claim:clm_ec0e79cadce8a4949affda4c97fb06a160f4bb6876835e4e0ec15c2c5442a216]
<!-- rcw:end owner=source:src_8d99c6014e5e5fe5aa437b8983edac23 block=evidence -->

## Researcher notes

