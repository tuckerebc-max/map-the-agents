# valuecell-ai/valuecell

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9793e9c0563f @ c342e1b889781940

## Summary (orientation draft, not independently verified)

ValueCell is a Python-based multi-agent financial platform with a web UI, configurable LLM providers via a three-tier config system, and crypto trading integrations with several exchanges. Evidence is mostly README and configuration documentation; no code or evaluation results are included. Evidence coverage: 168 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The README describes a multi-agent system including a DeepResearch Agent for analyzing fundamental documents, a Strategy Agent for multi-strategy crypto trading, and a News Retrieval Agent for scheduled news delivery, with more agents planned. -- evidence: [README.md#L78-L81](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L78-L81)
- design-choices (3 claim(s)):
  - [observation/documented] Configuration uses a three-tier system: environment variables override .env file settings, which override YAML defaults stored under python/configs/. -- evidence: [docs/CONFIGURATION_GUIDE.md#L3-L3](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L3-L3), [docs/CONFIGURATION_GUIDE.md#L9-L11](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L9-L11)
  - [observation/documented] The system auto-detects a primary provider from available API keys in a priority order starting with OpenRouter, SiliconFlow, Google, OpenAI, OpenAI-compatible, and Azure; this can be overridden via PRIMARY_PROVIDER or disabled with AUTO_DETECT_PROVIDER=false. -- evidence: [docs/CONFIGURATION_GUIDE.md#L339-L341](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L339-L341), [docs/CONFIGURATION_GUIDE.md#L323-L323](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L323-L323), [docs/CONFIGURATION_GUIDE.md#L345-L347](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L345-L347), [docs/CONFIGURATION_GUIDE.md#L329-L335](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L329-L335)
- workflows (1 claim(s)):
  - [observation/documented] Repository setup instructions: clone the repo, copy .env.example to .env and add API keys, then launch everything with bash start.sh (Linux/macOS) or .\start.ps1 (Windows PowerShell). -- evidence: [docs/CONFIGURATION_GUIDE.md#L34-L35](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L34-L35), [README.md#L169-L171](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L169-L171), [README.md#L154-L157](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L154-L157), [README.md#L164-L166](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L164-L166), [docs/CONFIGURATION_GUIDE.md#L38-L38](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L38-L38)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] When launched, the application serves a web UI at http://localhost:1420 and streams backend and agent logs to the terminal. -- evidence: [README.md#L175-L176](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L175-L176)
  - [observation/documented] Users configure AI model API keys and exchange credentials (Binance, HyperLiquid, OKX, Coinbase) through the web interface, then create strategies combining models with exchanges and start/stop traders with real-time monitoring. -- evidence: [README.md#L99-L103](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L99-L103)
- memory-state (1 claim(s)):
  - [observation/documented] The application stores local data in a LanceDB directory, a knowledge directory, and a SQLite database file (valuecell.db) under the system application directory, and users may delete these to reset state. -- evidence: [docs/CONFIGURATION_GUIDE.md#L62-L74](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L62-L74), [README.md#L129-L141](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/README.md#L129-L141)
- orchestration (1 claim(s)):
  - [observation/documented] If the primary provider fails, the system automatically tries fallback providers built from other enabled providers with valid keys, stopping at the first successful model creation; fallback can be overridden or disabled per agent with use_fallback: false. -- evidence: [docs/CONFIGURATION_GUIDE.md#L353-L355](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L353-L355), [docs/CONFIGURATION_GUIDE.md#L351-L351](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L351-L351), [docs/CONFIGURATION_GUIDE.md#L367-L368](https://github.com/ValueCell-ai/valuecell/blob/9793e9c0563fbf56fc096757d8bb80e209ac7aab/docs/CONFIGURATION_GUIDE.md#L367-L368)
- tools-permissions (1 claim(s)):
More evidence: [full detail](valuecell.detail.md)

Metadata and full claim list: [full detail](valuecell.detail.md)
Human notes ([notes](valuecell.notes.md), never overwritten by build)

[Back to map index](../../index.md)
