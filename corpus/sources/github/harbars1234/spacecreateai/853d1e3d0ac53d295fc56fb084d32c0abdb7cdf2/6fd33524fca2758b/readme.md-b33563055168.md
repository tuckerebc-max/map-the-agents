SpaceCreateAI - The best SEND AI agent

This repository contains the first Solana agent built with the SEND AI technology https://github.com/sendaifun/solana-agent-kit that automatically creates the agent and deploys the token. Agent will airdrop tokens once launched.

## Prerequisites

- **Node.js & npm**: Node.js v14+ recommended.
- **Solana CLI**: [Install the Solana CLI](https://docs.solana.com/cli/install-solana-cli) and ensure you can run `solana --version`.
- **Keypair**: Generate a new keypair and fund it on devnet:
  ```bash
  solana-keygen new --outfile keypair.json
  solana airdrop 2 $(solana-keygen pubkey keypair.json)
