# Swapper AI Agent Toolkit

This repository contains the Swapper AI Agent Toolkit — skills that give AI agents the ability to deposit funds, swap tokens, and manage wallets in DeFi.

## What is Swapper Finance?

Swapper Finance is the payment infrastructure layer for Web3. It lets users and agents deposit funds into DeFi protocols via payment cards (Mastercard, Visa, Apple Pay, Google Pay), crypto transfers, and wallet connections. Supports 170+ countries. Cross-chain via Chainlink CCIP. End-to-end orchestration via Chainlink CRE. Card processing via Mastercard.

## Repository structure

```
skills/
  swapper-deposit/    # Deposit and bridge funds into DeFi
    skill.md          # Skill definition (read by agents)
  swapper-trade/       # Token swap skill (coming soon)
    skill.md
  swapper-wallet/     # Wallet management skill (coming soon)
    skill.md
CLAUDE.md             # This file (read by Claude Code automatically)
README.md             # Repository overview
package.json          # Skill pack metadata
```

## How the deposit skill works

1. Agent calls `/swapper-deposit` with wallet address, chain, token
2. Skill generates a Swapper deposit deeplink with correct parameters
3. Deeplink opens in user's browser
4. User completes deposit via Swapper widget (card, transfer, or wallet)
5. Funds land in the target wallet or protocol on the target chain

The skill does NOT execute transactions — it generates a link. The user always confirms.

## Deeplink format

```
https://deposit.swapper.finance?integratorId=d6e438dfa14e80709b19&dstChainId=CHAIN_ID&dstTokenAddr=TOKEN_ADDR&depositWalletAddress=WALLET_ADDR&utm_source=swapper-deposit&extendedView=true
```

- `integratorId` is always `d6e438dfa14e80709b19` (hardcoded)
- For native tokens (ETH, POL, BNB), use `0x0000000000000000000000000000000000000000` as token address

## Supported chains

| Chain       | Chain ID |
|-------------|----------|
| Ethereum    | 1        |
| Base        | 8453     |
| Arbitrum    | 42161    |
| Optimism    | 10       |
| Polygon     | 137      |
| Fast        | fast     |
| Solana      | solana   |
| HyperEVM   | 999      |
| BNB Chain   | 56       |
| Avalanche   | 43114    |

## Safety rules

- Every transaction requires explicit user confirmation
- Never auto-approve transactions
- Always surface fees and risks before confirmation
- Never store or access private keys
- Always display the full deeplink URL so user can verify