# MLE-STAR-Open (`mle-star-open`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: WalkingDevFlag
- License: MIT
- Language: Python
- Interface: install=git clone + conda env (Python 3.12) + pip install -r requirements.txt
- Model providers: OpenRouter (free-tier), Ollama (planned/deferred)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [walkingdevflag/mle-star-open](../../repos/walkingdevflag/mle-star-open.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Google-free, local-friendly unofficial reimplementation of MLE-STAR. No API keys required for search (DuckDuckGo) and leverages free-tier LLMs via OpenRouter, making multi-agent AutoML experimentation accessible without enterprise infrastructure. Multi-agent pipeline stages: initialization, refinement, ensembling, submission.

(captured site page body (agents/mle-star-open.md), not a verified repo-code finding)
MLE-STAR demonstrated that search-and-refine loops make LLM agents competitive at machine-learning engineering, but the reference implementation depended on Google infrastructure. MLE-STAR-Open reimplements the pipeline for constrained setups: an initialization agent produces a first solution for a tabular task, refinement agents target specific components identified through web search (DuckDuckGo, no API key), an ensembling stage merges the best candidates, and a submission stage formats predictions.csv for Kaggle. Runs execute through OpenRouter's OpenAI-compatible API on free-tier models, with automated data-leakage and usage checks guarding the generated pipelines and a minimal low-token runner for cheap iteration. Each task gets a workspace directory holding init, refine, ensemble, predictions, and logs. Kaggle competitors and ML practitioners use it to experiment with agent-driven AutoML on a budget, accepting its constraints — roughly 50 free requests per day, an eight-commit codebase from a single maintainer, and an Ollama adapter still deferred.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mle-star-open.md)
