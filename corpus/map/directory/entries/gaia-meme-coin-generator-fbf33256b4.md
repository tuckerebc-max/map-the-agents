# Gaia-Meme-Coin-Generator (`gaia-meme-coin-generator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: harishkotra
- License: MIT
- Language: JavaScript
- Interface: install=git clone https://github.com/harishkotra/gaia-meme-coin-generator && cd gaia-meme-coin-generator && npm install; create .env with GAIA_URL, GAIA_MODEL, BASE_NODE_URL, PRIVATE_KEY; npm start
- Model providers: Gaia AI node (llama3b via https://llama3b.gaia.domains/v1)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [harishkotra/gaia-meme-coin-generator](../../repos/harishkotra/gaia-meme-coin-generator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-powered creative token naming and automatic tokenomics generation using Gaia's AI Agent. Deploys secure ERC20 contracts with built-in anti-whale protections (max transaction limits, max wallet limits, CEX/DEX exclusions). Full deployment record saved to JSON. Built for Base Sepolia testnet. Only 3 commits — hackathon/proof-of-concept project.

(captured site page body (agents/gaia-meme-coin-generator.md), not a verified repo-code finding)
The tool automates the mechanical parts of launching a testnet meme token: a Gaia-hosted Llama 3B node proposes the branding and supply limits, and a fixed contract template with max-transaction, max-wallet, and exchange-exclusion guards is compiled and deployed to Base Sepolia. Configuration flows through environment variables for the Gaia endpoint, model, RPC node, and deployer key, and the full deployment record lands in a JSON file. Three commits, no releases, and a testnet-only disclaimer mark it as a November 2024 hackathon proof of concept demonstrating Gaia node integration rather than a maintained product.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gaia-meme-coin-generator.md)
