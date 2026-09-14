---
access: public
aliases: []
claim_ids:
- clm_31b6a4b0c1ce574ed9ae994fa86be01b29cc059c9729b7bd3f4c6cf0a0dc36f1
- clm_4a11d99b58dee6a10a0333147bc03c3d6c71d737e65e2e519732872f43bab6b4
- clm_585e6782acb0c8494b60f8ead209e8e776a125511b6395d26a10a26c25e7de39
- clm_59aaa9bbd5212179867626b3db6ed82760c0a176ba749c657a5cc315806b8449
- clm_5edadca7d368cae93da13666235d11c6f318f95953cb3e95712d699b44c82618
- clm_a09cd3ad3b5258c6d7805f362061e65343fbc6c9c74d2e450adffbd5873e284b
- clm_b6103ce019f3f96fba8e601eb08f91fc6d96b77fd6b98f7b6c894b1da705805c
- clm_e721df561eeacba4c47142f3afc0c9ab6b09088d17ef1c3cac5edbc580a469d9
- clm_f68e3fc9817198e49428809fe178d0caca78ea8295accdf2c2b0749680d9df01
maturity: draft
page_id: pg_502bf40b1c02572c883a5643e415de20
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2d56c04eca73554e98f71095f3f89c10
title: swapperfinance/swapper-toolkit/README.md @ deb74c56d9db
updated_at: '2026-09-14T04:24:40Z'
---

# swapperfinance/swapper-toolkit/README.md @ deb74c56d9db

<!-- rcw:begin owner=source:src_2d56c04eca73554e98f71095f3f89c10 block=evidence -->
- The product relies on Chainlink CRE for deposit/compliance/settlement orchestration, Chainlink CCIP for cross-chain interoperability (60+ blockchains), and Mastercard for card processing in 170+ countries. [@claim:clm_31b6a4b0c1ce574ed9ae994fa86be01b29cc059c9729b7bd3f4c6cf0a0dc36f1]
- The toolkit is installed into agents via 'npx skills add swapperfinance/swapper-toolkit' and advertises compatibility with Claude Code, Cursor, Windsurf, Copilot, CrewAI, AutoGPT and any framework supporting the open skills standard. [@claim:clm_4a11d99b58dee6a10a0333147bc03c3d6c71d737e65e2e519732872f43bab6b4]
- Supported deposit chains are listed as Ethereum, Base, Arbitrum, Optimism, Polygon, Fast, Solana, HyperEVM, BNB Chain and Avalanche. [@claim:clm_585e6782acb0c8494b60f8ead209e8e776a125511b6395d26a10a26c25e7de39]
- The deposit flow is link-based: the skill generates a deposit link for browser confirmation rather than executing transactions itself, and every transaction requires explicit user approval with fees and risks surfaced beforehand. [@claim:clm_59aaa9bbd5212179867626b3db6ed82760c0a176ba749c657a5cc315806b8449]
- An npm SDK, @swapper-finance/deposit-sdk, exposes openSwapperModal accepting integratorId, destination chain ID and token address, deposit wallet address, theme styles, and supported deposit options like transferCrypto and depositWithCash. [@claim:clm_5edadca7d368cae93da13666235d11c6f318f95953cb3e95712d699b44c82618]
- The toolkit states private keys are never stored or accessed and transactions are never auto-approved. [@claim:clm_a09cd3ad3b5258c6d7805f362061e65343fbc6c9c74d2e450adffbd5873e284b]
- Deposits support direct transfers to any wallet address, cross-chain bridging via CCIP, protocol deposits into lending, staking and liquidity pools, and fiat on-ramps via Mastercard, Visa, Apple Pay and Google Pay. [@claim:clm_b6103ce019f3f96fba8e601eb08f91fc6d96b77fd6b98f7b6c894b1da705805c]
- An example deposit interaction shows the skill resolving chain (Base 8453), token (USDC), protocol (Aave) and amount, then producing a deposit link the user confirms in a browser. [@claim:clm_e721df561eeacba4c47142f3afc0c9ab6b09088d17ef1c3cac5edbc580a469d9]
- The /swapper-deposit skill triggers when a user asks to deposit, fund, top-up or bridge assets, when an agent detects insufficient wallet funds mid-task, or when fiat-to-crypto funding is wanted before a strategy. [@claim:clm_f68e3fc9817198e49428809fe178d0caca78ea8295accdf2c2b0749680d9df01]
<!-- rcw:end owner=source:src_2d56c04eca73554e98f71095f3f89c10 block=evidence -->

## Researcher notes

