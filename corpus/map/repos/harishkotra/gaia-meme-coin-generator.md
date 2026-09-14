# harishkotra/gaia-meme-coin-generator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 32907e4a57bf @ 9bcfbd96fb6b2613

## Summary (orientation draft, not independently verified)

README-only evidence for a Gaia-powered meme coin generator that uses an AI node to name tokens and generate tokenomics, then deploys an ERC20 contract with transaction/wallet limits to Base Sepolia. No source code is present in the snapshot, so claims rest on documentation.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The tool automates meme token creation: it uses Gaia's AI node to generate token names and themes, computes tokenomics, and deploys a limit-based token contract. -- evidence: [README.md#L7-L11](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L7-L11)
- components (2 claim(s)):
  - [observation/documented] Generated tokens include safety features: maximum transaction limits, maximum wallet limits, and excludable addresses for CEX/DEX purposes. -- evidence: [README.md#L74-L78](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L74-L78), [README.md#L15-L22](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L15-L22)
  - [observation/documented] The deployed contract is described as ERC20-compliant with ownership controls, a transaction limit system, wallet restrictions, and an address exclusion mechanism. -- evidence: [README.md#L82-L87](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L82-L87)
- design-choices (1 claim(s)):
  - [observation/documented] Tokenomics are auto-generated with example values of 500,000,000 total supply, 75% initial liquidity, 1% transaction limit, and 2% max wallet. -- evidence: [README.md#L146-L151](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L146-L151), [README.md#L123-L130](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L123-L130)
- workflows (2 claim(s)):
  - [observation/documented] Setup workflow: clone the repo, run npm install, create a .env file, then run the generator with npm start. -- evidence: [README.md#L32-L35](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L32-L35), [README.md#L45-L48](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L45-L48), [README.md#L26-L30](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L26-L30), [README.md#L37-L43](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L37-L43)
  - [observation/documented] Repository development practice: contributions are welcomed via opening issues, submitting PRs, suggesting improvements, and adding new features. -- evidence: [README.md#L99-L103](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L99-L103)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Configuration is via a .env file with GAIA_URL, GAIA_MODEL, BASE_NODE_URL, and PRIVATE_KEY variables; the tool is run with npm start. -- evidence: [README.md#L45-L48](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L45-L48), [README.md#L37-L43](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L37-L43)
  - [observation/documented] Example output shows the tool prints generated coin details, deployment address and transaction hash, tokenomics, a deployment_details.json record, and a Base Sepolia explorer verification link. -- evidence: [README.md#L146-L151](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L146-L151), [README.md#L153-L155](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L153-L155), [README.md#L110-L121](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L110-L121), [README.md#L137-L144](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L137-L144)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The tool calls a Gaia AI node at the llama3b.gaia.domains/v1 endpoint for creative naming, per the README. -- evidence: [README.md#L7-L11](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L7-L11)
  - [observation/documented] The project targets Base Sepolia by default but is described as easily adaptable to other networks. -- evidence: [README.md#L3-L3](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L3-L3)
- limitations (1 claim(s)):
  - [observation/documented] The README positions the tool for testnet experimentation and advises thorough testing, contract review, and regulatory-compliance consideration before mainnet use. -- evidence: [README.md#L91-L95](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L91-L95)
- relevance (1 claim(s)):
More evidence: [full detail](gaia-meme-coin-generator.detail.md)

Metadata and full claim list: [full detail](gaia-meme-coin-generator.detail.md)
Human notes ([notes](gaia-meme-coin-generator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
