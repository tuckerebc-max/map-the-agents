# swapper-toolkit (`swapper-toolkit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: swapperfinance
- License: MIT
- Language: JavaScript/TypeScript
- Interface: install=npm (npx skills add)
- Model providers: any (model-agnostic)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [swapperfinance/swapper-toolkit](../../repos/swapperfinance/swapper-toolkit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A DeFi payment layer for AI agents — lets coding assistants deposit fiat/crypto, bridge cross-chain via Chainlink CCIP, and fund DeFi protocols directly. Fiat on-ramp in 170+ countries, 10 chains supported, explicit confirmation model (no auto-approved transactions, keys never stored). Uses the open skills standard.

(captured site page body (agents/swapper-toolkit.md), not a verified repo-code finding)
swapper-toolkit addresses the fact that coding agents and autonomous agents have no native way to move money: it ships as Claude-standard skills (installable via npx skills add) that let assistants deposit funds through a fiat on-ramp in 170+ countries, bridge across Ethereum, Base, Arbitrum, Solana, BNB Chain and others through Chainlink CCIP, and fund DeFi protocols directly. Only the deposit skill is live so far — trading and wallet management are listed as coming soon — and every transaction requires explicit user confirmation with keys never stored, using Chainlink CRE and Mastercard rails under the hood. It integrates with Claude Code, Cursor, Windsurf, Copilot, CrewAI, and AutoGPT through the skills standard plus an npm SDK. The repository is young (eight commits), so it is best treated as an early integration layer rather than mature infrastructure.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swapper-toolkit.md)
