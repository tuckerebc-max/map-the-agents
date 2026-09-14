# swapperfinance/swapper-toolkit -- full detail

[Back to orientation](swapper-toolkit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/swapperfinance/swapper-toolkit/deb74c56d9db8e853a42fed7253aa760848ae821/fbc5afd676962fd5.json](../../../wiki/dossiers/swapperfinance/swapper-toolkit/deb74c56d9db8e853a42fed7253aa760848ae821/fbc5afd676962fd5.json)

## specifications (2 claim(s))

- [observation/documented] Deposits support direct transfers to any wallet address, cross-chain bridging via CCIP, protocol deposits into lending, staking and liquidity pools, and fiat on-ramps via Mastercard, Visa, Apple Pay and Google Pay. -- evidence: [README.md#L21-L24](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L21-L24) (`clm_b6103ce019f3f96fba8e601eb08f91fc6d96b77fd6b98f7b6c894b1da705805c`)
- [observation/documented] Supported deposit chains are listed as Ethereum, Base, Arbitrum, Optimism, Polygon, Fast, Solana, HyperEVM, BNB Chain and Avalanche. -- evidence: [README.md#L47-L47](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L47-L47) (`clm_585e6782acb0c8494b60f8ead209e8e776a125511b6395d26a10a26c25e7de39`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The deposit flow is link-based: the skill generates a deposit link for browser confirmation rather than executing transactions itself, and every transaction requires explicit user approval with fees and risks surfaced beforehand. -- evidence: [README.md#L44-L45](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L44-L45), [README.md#L90-L93](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L90-L93) (`clm_59aaa9bbd5212179867626b3db6ed82760c0a176ba749c657a5cc315806b8449`)
- [observation/documented] The toolkit states private keys are never stored or accessed and transactions are never auto-approved. -- evidence: [README.md#L90-L93](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L90-L93) (`clm_a09cd3ad3b5258c6d7805f362061e65343fbc6c9c74d2e450adffbd5873e284b`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: CLAUDE.md instructs that the deposit skill builds a Swapper deeplink with a hardcoded integratorId, uses the zero address for native tokens, and that agents must display the full deeplink URL, never auto-approve transactions, surface fees and risks, and never store or access private keys. -- evidence: [CLAUDE.md#L60-L64](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/CLAUDE.md#L60-L64), [CLAUDE.md#L36-L38](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/CLAUDE.md#L36-L38), [CLAUDE.md#L40-L41](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/CLAUDE.md#L40-L41) (`clm_b22d0316aaa81831498e8675d4894f0362fad00469007437eb218765b3a30bd0`)

## skills-patterns (2 claim(s))

- [observation/documented] The /swapper-deposit skill triggers when a user asks to deposit, fund, top-up or bridge assets, when an agent detects insufficient wallet funds mid-task, or when fiat-to-crypto funding is wanted before a strategy. -- evidence: [README.md#L26-L30](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L26-L30) (`clm_f68e3fc9817198e49428809fe178d0caca78ea8295accdf2c2b0749680d9df01`)
- [observation/documented] An example deposit interaction shows the skill resolving chain (Base 8453), token (USDC), protocol (Aave) and amount, then producing a deposit link the user confirms in a browser. -- evidence: [README.md#L34-L35](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L34-L35), [README.md#L37-L42](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L37-L42), [README.md#L44-L45](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L44-L45) (`clm_e721df561eeacba4c47142f3afc0c9ab6b09088d17ef1c3cac5edbc580a469d9`)

## interfaces (2 claim(s))

- [observation/documented] The toolkit is installed into agents via 'npx skills add swapperfinance/swapper-toolkit' and advertises compatibility with Claude Code, Cursor, Windsurf, Copilot, CrewAI, AutoGPT and any framework supporting the open skills standard. -- evidence: [README.md#L11-L13](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L11-L13), [README.md#L5-L5](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L5-L5) (`clm_4a11d99b58dee6a10a0333147bc03c3d6c71d737e65e2e519732872f43bab6b4`)
- [observation/documented] An npm SDK, @swapper-finance/deposit-sdk, exposes openSwapperModal accepting integratorId, destination chain ID and token address, deposit wallet address, theme styles, and supported deposit options like transferCrypto and depositWithCash. -- evidence: [README.md#L78-L86](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L78-L86), [README.md#L75-L76](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L75-L76), [README.md#L71-L73](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L71-L73) (`clm_5edadca7d368cae93da13666235d11c6f318f95953cb3e95712d699b44c82618`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product relies on Chainlink CRE for deposit/compliance/settlement orchestration, Chainlink CCIP for cross-chain interoperability (60+ blockchains), and Mastercard for card processing in 170+ countries. -- evidence: [README.md#L7-L7](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L7-L7), [README.md#L97-L99](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L97-L99) (`clm_31b6a4b0c1ce574ed9ae994fa86be01b29cc059c9729b7bd3f4c6cf0a0dc36f1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

