# ai4finance-foundation/finrobot -- full detail

[Back to orientation](finrobot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ai4finance-foundation/finrobot/6d6ccd32c1b8b1904dc656cf06897438aba3daec/41e01cd34f0a44ae.json](../../../wiki/dossiers/ai4finance-foundation/finrobot/6d6ccd32c1b8b1904dc656cf06897438aba3daec/41e01cd34f0a44ae.json)

## specifications (1 claim(s))

- [observation/documented] FinRobot is described as an AI agent platform for financial applications that unifies LLMs, reinforcement learning, and quantitative analytics for investment research, trading strategies, and risk assessment. -- evidence: [README.md#L19-L19](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L19-L19) (`clm_dfd3d700facb847df55d031de518534d764fc9e08928c73fb8ea4759d941020c`)

## components (3 claim(s))

- [observation/documented] The repository hosts V0 (AutoGen-based FinRobot) and V1 (finrobot_equity, equity-research agents and report generation) as open source; V2 is online-only with source not yet open-sourced, and V3 is in development. -- evidence: [README.md#L33-L38](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L33-L38), [README.md#L44-L47](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L44-L47) (`clm_d937a316be820bfa268a9922d46f964857cdc41018e450df7a36cbe1981385e3`)
- [observation/documented] The codebase snapshot lists 9 agents, 7 research pipelines (company research, DCF, comps, LBO, DDM, earnings, IC memo), 30 pure-Python compute operators with 7 coordinators, and 7 data providers with failover including FMP, Finnhub, yfinance, and SEC EDGAR. -- evidence: [README.md#L127-L134](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L127-L134) (`clm_5e5c9911d1db9d0ea5b66361f035ee1f7370a4f096981dd8f849b0bf2d18b8e4`)
- [observation/documented] The legacy finrobot package is organized into agents (agent_library.py, workflow.py), data_source (finnhub, finnlp, fmp, sec, yfinance utils), and functional modules (analyzer, charting, coding, quantitative, reportlab, text), with beginner and advanced tutorial notebooks. -- evidence: [README.md#L274-L274](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L274-L274), [README.md#L276-L314](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L276-L314) (`clm_f3a8808dfbccf47f484fffc3fca49e060595647ff1cd29c6d848cc92af9a7ba3`)

## design-choices (2 claim(s))

- [observation/documented] The project deliberately avoids tying itself to one agent framework; each generation adopts new agent architectures while keeping the financial domain layer, tools, and deterministic computation at the core. -- evidence: [README.md#L31-L31](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L31-L31), [README.md#L40-L40](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L40-L40) (`clm_5f6d17bd470abb1cb40ad92ef567440f381e4a30d7f7a5656d2eb10ec10da925`)
- [observation/documented] A stated core principle is strict separation of deterministic financial computation from LLM narration: valuation numbers (DCF, DDM, LBO, WACC, comps, Monte Carlo) come from pure-Python code paths, while the LLM handles reasoning and report writing, with provenance tracking. -- evidence: [README.md#L114-L114](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L114-L114), [README.md#L120-L124](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L120-L124), [README.md#L116-L116](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L116-L116) (`clm_1b72a4d026ce0ce80d19d89a28cffc7bdf9ec9bcbd6a52fca48016e50739d95f`)

## workflows (1 claim(s))

- [observation/documented] Setup involves copying config.ini.example and OAI_CONFIG_LIST_sample / config_api_keys_sample templates and adding OpenAI, Finnhub, FMP, and SEC API keys; deployment is via deploy.sh start/stop/restart/status or a manual venv plus run_web_app.py. -- evidence: [README.md#L180-L185](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L180-L185), [README.md#L330-L352](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L330-L352), [README.md#L155-L165](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L155-L165), [README.md#L173-L178](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L173-L178) (`clm_f5c74921209acfcf7e8451eb875046977c993b6e9d6f5e354629238e22caa099`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The finrobot_equity CLI exposes scripts such as generate_financial_analysis.py and create_equity_report.py taking flags like --company-ticker, --peer-tickers, and --analysis-csv, and a web app accessible at http://127.0.0.1:8001. -- evidence: [README.md#L190-L195](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L190-L195), [README.md#L198-L204](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L198-L204), [README.md#L173-L178](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L173-L178) (`clm_af52e26dded544f1e9344a8e63340e87eb06697a39b31e3a9c11e0b5f863b558`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The desktop product's multi-agent architecture uses one Lead Agent orchestrating five role-based sub-agents (data, analysis, modeling, synthesis, reporting) plus three debate agents (bull, bear, judge) in a pipeline flow. -- evidence: [README.md#L100-L110](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L100-L110), [README.md#L94-L96](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L94-L96), [README.md#L90-L90](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L90-L90) (`clm_36ce7f34f5dc2ccd950d5d0e9ee69f10e66fbd4d330bb171043a576634e07d39`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] requirements-equity.txt pins pandas 2.x, numpy 1.x, openai 1.x, openai-agents, pydantic 2.x, FastAPI, SQLAlchemy, yfinance, reportlab/weasyprint for PDF, and pg8000 for Cloud SQL PostgreSQL deployment. -- evidence: [requirements-equity.txt#L4-L7](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/requirements-equity.txt#L4-L7), [requirements-equity.txt#L25-L26](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/requirements-equity.txt#L25-L26), [requirements-equity.txt#L11-L13](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/requirements-equity.txt#L11-L13), [requirements-equity.txt#L46-L46](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/requirements-equity.txt#L46-L46), [requirements-equity.txt#L38-L40](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/requirements-equity.txt#L38-L40) (`clm_13d44be4a2a29f5389827f1c7d65d6682b76993bf7c0baff716ecebee6cdc800`)

## limitations (2 claim(s))

- [observation/documented] FinRobot Desktop v0.1.0 supports only Apple Silicon Macs (M1-M3 or later) with no Intel builds, and the app is not yet Apple-notarized, so users must clear the quarantine attribute via xattr before first launch. -- evidence: [README.md#L67-L67](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L67-L67), [README.md#L71-L71](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L71-L71), [README.md#L73-L75](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L73-L75) (`clm_874b4bfc3d4d8709f5db802555ac1fae55199e8a7b9bec3516d42360bc39bbcc`)
- [observation/documented] The README's disclaimer states the code is Apache-2.0 licensed and must not be construed as financial counsel or trading recommendations. -- evidence: [README.md#L408-L416](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L408-L416) (`clm_0b1554e8b231179756ffad361f6bd64d6631e948134b62112cc7f07611e09c2b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

