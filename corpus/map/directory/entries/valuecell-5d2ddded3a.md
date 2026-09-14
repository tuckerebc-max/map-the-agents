# valuecell (`valuecell`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ValueCell-ai
- License: Apache-2.0
- Language: Python, React
- Interface: install=binary
- Model providers: OpenRouter, SiliconFlow, Azure, OpenAI, Google, DeepSeek
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [valuecell-ai/valuecell](../../repos/valuecell-ai/valuecell.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Community-driven multi-agent platform for financial applications (stock selection, research, tracking, trading). Live exchange routing (Binance, OKX, Hyperliquid) with built-in guardrails. All sensitive user data stored locally. Multi-agent system with DeepResearch, Strategy, and News Retrieval agents. Plugin architecture and Agent Registry planned for third-party agents.

(captured site page body (agents/valuecell.md), not a verified repo-code finding)
ValueCell applies the multi-agent pattern to investing rather than software development: specialized agents perform fundamental document research, execute multi-strategy trading across crypto assets, and deliver scheduled personalized news, coordinated on a platform the community extends. Market data covers US, crypto, Hong Kong, and China markets, with live routing to Binance, OKX, and Hyperliquid (Coinbase, Gate.io, and MEXC partially tested) under built-in guardrails, and agents interoperate with LangChain and Agno through the A2A protocol. Sensitive data — LanceDB vectors, SQLite, the knowledge base — stays on the user's machine, while a hosted instance at valuecell.ai serves A-share research. Retail and semi-professional traders, particularly in Chinese markets, use it for research and strategy execution; it is Apache-2.0 licensed (original code), Python 3.12+ with a React frontend, and actively developed.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/valuecell.md)
