# swapperfinance/swapper-toolkit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit deb74c56d9db @ fbc5afd676962fd5

## Summary (orientation draft, not independently verified)

Selected evidence records: The toolkit is installed into agents via 'npx skills add swapperfinance/swapper-toolkit' and advertises compatibility with Claude Code, Cursor, Windsurf, Copilot, CrewAI, AutoGPT and any framework supporting the open skills standard. The /swapper-deposit skill triggers when a user asks to deposit, fund, top-up or bridge assets, when an agent detects insufficient wallet funds mid-task, or when fiat-to-crypto funding is wanted before a strategy.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Deposits support direct transfers to any wallet address, cross-chain bridging via CCIP, protocol deposits into lending, staking and liquidity pools, and fiat on-ramps via Mastercard, Visa, Apple Pay and Google Pay. -- evidence: [README.md#L21-L24](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L21-L24)
  - [observation/documented] Supported deposit chains are listed as Ethereum, Base, Arbitrum, Optimism, Polygon, Fast, Solana, HyperEVM, BNB Chain and Avalanche. -- evidence: [README.md#L47-L47](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L47-L47)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The deposit flow is link-based: the skill generates a deposit link for browser confirmation rather than executing transactions itself, and every transaction requires explicit user approval with fees and risks surfaced beforehand. -- evidence: [README.md#L44-L45](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L44-L45), [README.md#L90-L93](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L90-L93)
  - [observation/documented] The toolkit states private keys are never stored or accessed and transactions are never auto-approved. -- evidence: [README.md#L90-L93](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L90-L93)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.md instructs that the deposit skill builds a Swapper deeplink with a hardcoded integratorId, uses the zero address for native tokens, and that agents must display the full deeplink URL, never auto-approve transactions, surface fees and risks, and never store or access private keys. -- evidence: [CLAUDE.md#L60-L64](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/CLAUDE.md#L60-L64), [CLAUDE.md#L36-L38](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/CLAUDE.md#L36-L38), [CLAUDE.md#L40-L41](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/CLAUDE.md#L40-L41)
- skills-patterns (2 claim(s)):
  - [observation/documented] The /swapper-deposit skill triggers when a user asks to deposit, fund, top-up or bridge assets, when an agent detects insufficient wallet funds mid-task, or when fiat-to-crypto funding is wanted before a strategy. -- evidence: [README.md#L26-L30](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L26-L30)
  - [observation/documented] An example deposit interaction shows the skill resolving chain (Base 8453), token (USDC), protocol (Aave) and amount, then producing a deposit link the user confirms in a browser. -- evidence: [README.md#L34-L35](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L34-L35), [README.md#L37-L42](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L37-L42), [README.md#L44-L45](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L44-L45)
- interfaces (2 claim(s)):
  - [observation/documented] The toolkit is installed into agents via 'npx skills add swapperfinance/swapper-toolkit' and advertises compatibility with Claude Code, Cursor, Windsurf, Copilot, CrewAI, AutoGPT and any framework supporting the open skills standard. -- evidence: [README.md#L11-L13](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L11-L13), [README.md#L5-L5](https://github.com/swapperfinance/swapper-toolkit/blob/deb74c56d9db8e853a42fed7253aa760848ae821/README.md#L5-L5)
More evidence: [full detail](swapper-toolkit.detail.md)

Metadata and full claim list: [full detail](swapper-toolkit.detail.md)
Human notes ([notes](swapper-toolkit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
