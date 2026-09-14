# harishkotra/gaia-meme-coin-generator -- full detail

[Back to orientation](gaia-meme-coin-generator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/harishkotra/gaia-meme-coin-generator/32907e4a57bf575ba58dc32883e018009ec98246/9bcfbd96fb6b2613.json](../../../wiki/dossiers/harishkotra/gaia-meme-coin-generator/32907e4a57bf575ba58dc32883e018009ec98246/9bcfbd96fb6b2613.json)

## specifications (1 claim(s))

- [observation/documented] The tool automates meme token creation: it uses Gaia's AI node to generate token names and themes, computes tokenomics, and deploys a limit-based token contract. -- evidence: [README.md#L7-L11](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L7-L11) (`clm_08a5664c91b722949f727cff1fad8ad68822f7817d4ad1850d0a9de7d28021e5`)

## components (2 claim(s))

- [observation/documented] Generated tokens include safety features: maximum transaction limits, maximum wallet limits, and excludable addresses for CEX/DEX purposes. -- evidence: [README.md#L74-L78](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L74-L78), [README.md#L15-L22](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L15-L22) (`clm_456bcdc421f64885f73f4b1faf14e4814129ab9ff3c6c33a171d1558910e6072`)
- [observation/documented] The deployed contract is described as ERC20-compliant with ownership controls, a transaction limit system, wallet restrictions, and an address exclusion mechanism. -- evidence: [README.md#L82-L87](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L82-L87) (`clm_b2c2e3fcc8d731e43ecbcb866e6bac8d2afc51d09674fa02a5304b8ba42151f4`)

## design-choices (1 claim(s))

- [observation/documented] Tokenomics are auto-generated with example values of 500,000,000 total supply, 75% initial liquidity, 1% transaction limit, and 2% max wallet. -- evidence: [README.md#L146-L151](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L146-L151), [README.md#L123-L130](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L123-L130) (`clm_7651cdd6a09a600105d1ea05d5d6155025415f624b09c17d00b2fd2a9b395e43`)

## workflows (2 claim(s))

- [observation/documented] Setup workflow: clone the repo, run npm install, create a .env file, then run the generator with npm start. -- evidence: [README.md#L32-L35](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L32-L35), [README.md#L45-L48](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L45-L48), [README.md#L26-L30](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L26-L30), [README.md#L37-L43](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L37-L43) (`clm_600e65b51ce5786526bec0d389cbf687371886cec9e6ad7f556aae4199742e54`)
- [observation/documented] Repository development practice: contributions are welcomed via opening issues, submitting PRs, suggesting improvements, and adding new features. -- evidence: [README.md#L99-L103](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L99-L103) (`clm_72c17d4a1e5de96e6d9dbbdc49e0f5adb07f4df83e70ae7cc844deed67aaae44`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Configuration is via a .env file with GAIA_URL, GAIA_MODEL, BASE_NODE_URL, and PRIVATE_KEY variables; the tool is run with npm start. -- evidence: [README.md#L45-L48](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L45-L48), [README.md#L37-L43](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L37-L43) (`clm_c7b18bf8319471c7b471be9b03c89651b4f6bb989a67b334557737fac9d6a114`)
- [observation/documented] Example output shows the tool prints generated coin details, deployment address and transaction hash, tokenomics, a deployment_details.json record, and a Base Sepolia explorer verification link. -- evidence: [README.md#L146-L151](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L146-L151), [README.md#L153-L155](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L153-L155), [README.md#L110-L121](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L110-L121), [README.md#L137-L144](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L137-L144) (`clm_2ae4418941f6c3ce58b32e453869c5e08286055a6c50bbf6867b2669247e02ad`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool calls a Gaia AI node at the llama3b.gaia.domains/v1 endpoint for creative naming, per the README. -- evidence: [README.md#L7-L11](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L7-L11) (`clm_c5d0b60e33ab546081d11c93c9c2a86ed9343fd99febc7d2a3d124a2fae61568`)
- [observation/documented] The project targets Base Sepolia by default but is described as easily adaptable to other networks. -- evidence: [README.md#L3-L3](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L3-L3) (`clm_82b956559b621dfdc0bf80b136329fa6ac62ebd7f06232338a480f68d0581e16`)

## limitations (1 claim(s))

- [observation/documented] The README positions the tool for testnet experimentation and advises thorough testing, contract review, and regulatory-compliance consideration before mainnet use. -- evidence: [README.md#L91-L95](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L91-L95) (`clm_766e8ae6676bd63b92404c6fa566d6810a2c6bef927e11fd21ae09ca078035bf`)

## relevance (1 claim(s))

- [observation/documented] Stated use cases include token launch platforms, community/fan tokens, educational testnet practice, and marketing campaign tokens. -- evidence: [README.md#L62-L65](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L62-L65), [README.md#L57-L60](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L57-L60), [README.md#L67-L70](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L67-L70), [README.md#L52-L55](https://github.com/harishkotra/gaia-meme-coin-generator/blob/32907e4a57bf575ba58dc32883e018009ec98246/README.md#L52-L55) (`clm_4a2ef527ad0f22222bf6260b8a5f710448dbecdac7cbc72c40c5add310558291`)

