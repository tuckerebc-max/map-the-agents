# valuecell-ai/valuecell -- full detail

[Back to orientation](valuecell.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/valuecell-ai/valuecell/9793e9c0563fbf56fc096757d8bb80e209ac7aab/c342e1b889781940.json](../../../wiki/dossiers/valuecell-ai/valuecell/9793e9c0563fbf56fc096757d8bb80e209ac7aab/c342e1b889781940.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The README describes a multi-agent system including a DeepResearch Agent for analyzing fundamental documents, a Strategy Agent for multi-strategy crypto trading, and a News Retrieval Agent for scheduled news delivery, with more agents planned. -- evidence: [README.md#L78-L81](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L78-L81) (`clm_ec0e79cadce8a4949affda4c97fb06a160f4bb6876835e4e0ec15c2c5442a216`)

## design-choices (3 claim(s))

- [observation/documented] Configuration uses a three-tier system: environment variables override .env file settings, which override YAML defaults stored under python/configs/. -- evidence: [docs/CONFIGURATION_GUIDE.md#L3-L3](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L3-L3), [docs/CONFIGURATION_GUIDE.md#L9-L11](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L9-L11) (`clm_03cc7b432c12c3be37e9a8870a9edf744179ae78dfb98bb3dfb1ab2b00c6e3f3`)
- [observation/documented] The system auto-detects a primary provider from available API keys in a priority order starting with OpenRouter, SiliconFlow, Google, OpenAI, OpenAI-compatible, and Azure; this can be overridden via PRIMARY_PROVIDER or disabled with AUTO_DETECT_PROVIDER=false. -- evidence: [docs/CONFIGURATION_GUIDE.md#L339-L341](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L339-L341), [docs/CONFIGURATION_GUIDE.md#L323-L323](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L323-L323), [docs/CONFIGURATION_GUIDE.md#L345-L347](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L345-L347), [docs/CONFIGURATION_GUIDE.md#L329-L335](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L329-L335) (`clm_4506f8b38ee393ced746c211673e7b403dcdd1482331c2dabe45e77338399461`)
- [inference/documented] Agent YAML configs support per-provider model mappings (provider_models) and env_overrides, suggesting agents can run different models per provider and be tuned at runtime without code changes. -- evidence: [docs/CONFIGURATION_GUIDE.md#L381-L385](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L381-L385), [docs/CONFIGURATION_GUIDE.md#L158-L161](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L158-L161), [docs/CONFIGURATION_GUIDE.md#L304-L309](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L304-L309), [docs/CONFIGURATION_GUIDE.md#L148-L156](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L148-L156) (`clm_f2c77567cc1282f620102fd97e3cb101abd5a8eaf77548312e477c73d6ef9e70`)

## workflows (1 claim(s))

- [observation/documented] Repository setup instructions: clone the repo, copy .env.example to .env and add API keys, then launch everything with bash start.sh (Linux/macOS) or .\start.ps1 (Windows PowerShell). -- evidence: [docs/CONFIGURATION_GUIDE.md#L34-L35](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L34-L35), [README.md#L169-L171](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L169-L171), [README.md#L154-L157](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L154-L157), [README.md#L164-L166](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L164-L166), [docs/CONFIGURATION_GUIDE.md#L38-L38](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L38-L38) (`clm_dc94f19a8d5716d4c22bb8c9e4d60b00b209905d4a517e7d8395e95510d34493`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] When launched, the application serves a web UI at http://localhost:1420 and streams backend and agent logs to the terminal. -- evidence: [README.md#L175-L176](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L175-L176) (`clm_bf8f8b57007986f1ad5d712f00ecfcf67668a290832baf109edd7d0023008037`)
- [observation/documented] Users configure AI model API keys and exchange credentials (Binance, HyperLiquid, OKX, Coinbase) through the web interface, then create strategies combining models with exchanges and start/stop traders with real-time monitoring. -- evidence: [README.md#L99-L103](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L99-L103) (`clm_16deed8a2612548e48257be0810050eea35f78cebbd5b760d9ea4d86046d89a1`)

## memory-state (1 claim(s))

- [observation/documented] The application stores local data in a LanceDB directory, a knowledge directory, and a SQLite database file (valuecell.db) under the system application directory, and users may delete these to reset state. -- evidence: [docs/CONFIGURATION_GUIDE.md#L62-L74](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L62-L74), [README.md#L129-L141](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L129-L141) (`clm_b3504277c27aa4649ffd15b827c3f78a5b528562e3431fb2e514733cca2ecc58`)

## orchestration (1 claim(s))

- [observation/documented] If the primary provider fails, the system automatically tries fallback providers built from other enabled providers with valid keys, stopping at the first successful model creation; fallback can be overridden or disabled per agent with use_fallback: false. -- evidence: [docs/CONFIGURATION_GUIDE.md#L353-L355](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L353-L355), [docs/CONFIGURATION_GUIDE.md#L351-L351](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L351-L351), [docs/CONFIGURATION_GUIDE.md#L367-L368](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L367-L368) (`clm_51006d9adba37f417f12e4232d397046d0326a05d0c8b0ba8ff167d975246c30`)

## tools-permissions (1 claim(s))

- [observation/documented] OKX trading defaults to a paper environment, and OKX_ALLOW_LIVE_TRADING defaults to false and must be set to true before orders are routed to mainnet. -- evidence: [docs/CONFIGURATION_GUIDE.md#L504-L512](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L504-L512), [docs/CONFIGURATION_GUIDE.md#L514-L515](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L514-L515) (`clm_18ed2feda03bc1f4f46b297704a9367036b2020add5c72963f017106970c6599`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The product supports multiple LLM providers including OpenRouter, SiliconFlow, Azure, Google, OpenAI-compatible endpoints, OpenAI, and DeepSeek, per the README's integrations section. -- evidence: [README.md#L84-L87](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L84-L87) (`clm_5a809f8d877300eaa620fbe4799da15e458ab6ace8bb8525735d81c96b6e594c`)
- [observation/documented] Exchange connectivity is documented for OKX, Binance, and Hyperliquid as fully tested, with Coinbase, Gate.io, MEXC, and a Blockchain option listed as partially tested. -- evidence: [README.md#L117-L120](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L117-L120), [README.md#L107-L115](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L107-L115) (`clm_1fcfc26e753786f09c570b54eb2b2704ec4c21d9c2767af698644316a1315aca`)
- [observation/documented] The project targets Python 3.12+ and is licensed under Apache 2.0, which applies only to original ValueCell code; third-party components like TradingView widgets and exchange/LLM APIs are governed by their own terms. -- evidence: [README.md#L256-L256](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L256-L256), [README.md#L5-L28](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L5-L28), [README.md#L262-L266](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L262-L266) (`clm_4cdf94b760a195a2b3959e44a305bdfe09943b843439c98a51ee1afbab222b31`)

## limitations (1 claim(s))

- [observation/documented] Live trading currently supports only contract (leverage) trading, with spot implemented as 1X contracts, so users must maintain sufficient contract account balance. -- evidence: [README.md#L123-L125](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L123-L125), [README.md#L99-L103](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L99-L103) (`clm_e0e69fe17f088275a5236923036589b46d34d9d614ba50369f0d6156ca66c424`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

