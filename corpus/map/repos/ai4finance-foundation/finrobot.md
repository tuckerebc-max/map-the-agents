# ai4finance-foundation/finrobot

Status: distilled - Freshness: stale
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6d6ccd32c1b8 @ b5c82f0881e281ff

## Summary (orientation draft, not independently verified)

The snapshot is README-and-manifest evidence for FinRobot, an open-source AI agent platform for financial applications spanning a legacy AutoGen-based framework, a finrobot_equity research pipeline, and a PydanticAI/FastAPI/React/Tauri desktop product. Claims below rest on documented README text and dependency listings; no code was inspected.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] FinRobot is described as an AI agent platform for financial applications that unifies LLMs, reinforcement learning, and quantitative analytics for investment research, trading strategies, and risk assessment. -- evidence: [README.md#L19-L19](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L19-L19)
- components (3 claim(s)):
  - [observation/documented] The repository hosts V0 (AutoGen-based FinRobot) and V1 (finrobot_equity, equity-research agents and report generation) as open source; V2 is online-only with source not yet open-sourced, and V3 is in development. -- evidence: [README.md#L33-L38](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L33-L38), [README.md#L44-L47](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L44-L47)
  - [observation/documented] The codebase snapshot lists 9 agents, 7 research pipelines (company research, DCF, comps, LBO, DDM, earnings, IC memo), 30 pure-Python compute operators with 7 coordinators, and 7 data providers with failover including FMP, Finnhub, yfinance, and SEC EDGAR. -- evidence: [README.md#L127-L134](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L127-L134)
- design-choices (2 claim(s)):
  - [observation/documented] The project deliberately avoids tying itself to one agent framework; each generation adopts new agent architectures while keeping the financial domain layer, tools, and deterministic computation at the core. -- evidence: [README.md#L31-L31](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L31-L31), [README.md#L40-L40](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L40-L40)
  - [observation/documented] A stated core principle is strict separation of deterministic financial computation from LLM narration: valuation numbers (DCF, DDM, LBO, WACC, comps, Monte Carlo) come from pure-Python code paths, while the LLM handles reasoning and report writing, with provenance tracking. -- evidence: [README.md#L114-L114](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L114-L114), [README.md#L120-L124](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L120-L124), [README.md#L116-L116](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L116-L116)
- workflows (1 claim(s)):
  - [observation/documented] Setup involves copying config.ini.example and OAI_CONFIG_LIST_sample / config_api_keys_sample templates and adding OpenAI, Finnhub, FMP, and SEC API keys; deployment is via deploy.sh start/stop/restart/status or a manual venv plus run_web_app.py. -- evidence: [README.md#L180-L185](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L180-L185), [README.md#L330-L352](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L330-L352), [README.md#L155-L165](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L155-L165), [README.md#L173-L178](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L173-L178)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The finrobot_equity CLI exposes scripts such as generate_financial_analysis.py and create_equity_report.py taking flags like --company-ticker, --peer-tickers, and --analysis-csv, and a web app accessible at http://127.0.0.1:8001. -- evidence: [README.md#L190-L195](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L190-L195), [README.md#L198-L204](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L198-L204), [README.md#L173-L178](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L173-L178)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The desktop product's multi-agent architecture uses one Lead Agent orchestrating five role-based sub-agents (data, analysis, modeling, synthesis, reporting) plus three debate agents (bull, bear, judge) in a pipeline flow. -- evidence: [README.md#L100-L110](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L100-L110), [README.md#L94-L96](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L94-L96), [README.md#L90-L90](https://github.com/AI4Finance-Foundation/FinRobot/blob/6d6ccd32c1b8b1904dc656cf06897438aba3daec/README.md#L90-L90)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](finrobot.detail.md)

Metadata and full claim list: [full detail](finrobot.detail.md)
Human notes ([notes](finrobot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
