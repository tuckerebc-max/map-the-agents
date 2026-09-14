---
access: public
aliases: []
claim_ids:
- clm_0b1554e8b231179756ffad361f6bd64d6631e948134b62112cc7f07611e09c2b
- clm_1b72a4d026ce0ce80d19d89a28cffc7bdf9ec9bcbd6a52fca48016e50739d95f
- clm_36ce7f34f5dc2ccd950d5d0e9ee69f10e66fbd4d330bb171043a576634e07d39
- clm_5e5c9911d1db9d0ea5b66361f035ee1f7370a4f096981dd8f849b0bf2d18b8e4
- clm_5f6d17bd470abb1cb40ad92ef567440f381e4a30d7f7a5656d2eb10ec10da925
- clm_874b4bfc3d4d8709f5db802555ac1fae55199e8a7b9bec3516d42360bc39bbcc
- clm_af52e26dded544f1e9344a8e63340e87eb06697a39b31e3a9c11e0b5f863b558
- clm_d937a316be820bfa268a9922d46f964857cdc41018e450df7a36cbe1981385e3
- clm_dfd3d700facb847df55d031de518534d764fc9e08928c73fb8ea4759d941020c
- clm_f3a8808dfbccf47f484fffc3fca49e060595647ff1cd29c6d848cc92af9a7ba3
- clm_f5c74921209acfcf7e8451eb875046977c993b6e9d6f5e354629238e22caa099
maturity: draft
page_id: pg_12b487d157f85c599993a05b0023f3d9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c05da2e14faf5e7097c1bff3bafe4364
title: AI4Finance-Foundation/FinRobot/README.md @ 6d6ccd32c1b8
updated_at: '2026-09-14T03:32:47Z'
---

# AI4Finance-Foundation/FinRobot/README.md @ 6d6ccd32c1b8

<!-- rcw:begin owner=source:src_c05da2e14faf5e7097c1bff3bafe4364 block=evidence -->
- The README's disclaimer states the code is Apache-2.0 licensed and must not be construed as financial counsel or trading recommendations. [@claim:clm_0b1554e8b231179756ffad361f6bd64d6631e948134b62112cc7f07611e09c2b]
- A stated core principle is strict separation of deterministic financial computation from LLM narration: valuation numbers (DCF, DDM, LBO, WACC, comps, Monte Carlo) come from pure-Python code paths, while the LLM handles reasoning and report writing, with provenance tracking. [@claim:clm_1b72a4d026ce0ce80d19d89a28cffc7bdf9ec9bcbd6a52fca48016e50739d95f]
- The desktop product's multi-agent architecture uses one Lead Agent orchestrating five role-based sub-agents (data, analysis, modeling, synthesis, reporting) plus three debate agents (bull, bear, judge) in a pipeline flow. [@claim:clm_36ce7f34f5dc2ccd950d5d0e9ee69f10e66fbd4d330bb171043a576634e07d39]
- The codebase snapshot lists 9 agents, 7 research pipelines (company research, DCF, comps, LBO, DDM, earnings, IC memo), 30 pure-Python compute operators with 7 coordinators, and 7 data providers with failover including FMP, Finnhub, yfinance, and SEC EDGAR. [@claim:clm_5e5c9911d1db9d0ea5b66361f035ee1f7370a4f096981dd8f849b0bf2d18b8e4]
- The project deliberately avoids tying itself to one agent framework; each generation adopts new agent architectures while keeping the financial domain layer, tools, and deterministic computation at the core. [@claim:clm_5f6d17bd470abb1cb40ad92ef567440f381e4a30d7f7a5656d2eb10ec10da925]
- FinRobot Desktop v0.1.0 supports only Apple Silicon Macs (M1-M3 or later) with no Intel builds, and the app is not yet Apple-notarized, so users must clear the quarantine attribute via xattr before first launch. [@claim:clm_874b4bfc3d4d8709f5db802555ac1fae55199e8a7b9bec3516d42360bc39bbcc]
- The finrobot_equity CLI exposes scripts such as generate_financial_analysis.py and create_equity_report.py taking flags like --company-ticker, --peer-tickers, and --analysis-csv, and a web app accessible at http://127.0.0.1:8001. [@claim:clm_af52e26dded544f1e9344a8e63340e87eb06697a39b31e3a9c11e0b5f863b558]
- The repository hosts V0 (AutoGen-based FinRobot) and V1 (finrobot_equity, equity-research agents and report generation) as open source; V2 is online-only with source not yet open-sourced, and V3 is in development. [@claim:clm_d937a316be820bfa268a9922d46f964857cdc41018e450df7a36cbe1981385e3]
- FinRobot is described as an AI agent platform for financial applications that unifies LLMs, reinforcement learning, and quantitative analytics for investment research, trading strategies, and risk assessment. [@claim:clm_dfd3d700facb847df55d031de518534d764fc9e08928c73fb8ea4759d941020c]
- The legacy finrobot package is organized into agents (agent_library.py, workflow.py), data_source (finnhub, finnlp, fmp, sec, yfinance utils), and functional modules (analyzer, charting, coding, quantitative, reportlab, text), with beginner and advanced tutorial notebooks. [@claim:clm_f3a8808dfbccf47f484fffc3fca49e060595647ff1cd29c6d848cc92af9a7ba3]
- Setup involves copying config.ini.example and OAI_CONFIG_LIST_sample / config_api_keys_sample templates and adding OpenAI, Finnhub, FMP, and SEC API keys; deployment is via deploy.sh start/stop/restart/status or a manual venv plus run_web_app.py. [@claim:clm_f5c74921209acfcf7e8451eb875046977c993b6e9d6f5e354629238e22caa099]
<!-- rcw:end owner=source:src_c05da2e14faf5e7097c1bff3bafe4364 block=evidence -->

## Researcher notes

