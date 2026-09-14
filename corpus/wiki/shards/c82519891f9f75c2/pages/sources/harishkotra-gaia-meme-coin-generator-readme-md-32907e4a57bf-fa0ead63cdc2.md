---
access: public
aliases: []
claim_ids:
- clm_08a5664c91b722949f727cff1fad8ad68822f7817d4ad1850d0a9de7d28021e5
- clm_2ae4418941f6c3ce58b32e453869c5e08286055a6c50bbf6867b2669247e02ad
- clm_456bcdc421f64885f73f4b1faf14e4814129ab9ff3c6c33a171d1558910e6072
- clm_4a2ef527ad0f22222bf6260b8a5f710448dbecdac7cbc72c40c5add310558291
- clm_600e65b51ce5786526bec0d389cbf687371886cec9e6ad7f556aae4199742e54
- clm_72c17d4a1e5de96e6d9dbbdc49e0f5adb07f4df83e70ae7cc844deed67aaae44
- clm_7651cdd6a09a600105d1ea05d5d6155025415f624b09c17d00b2fd2a9b395e43
- clm_766e8ae6676bd63b92404c6fa566d6810a2c6bef927e11fd21ae09ca078035bf
- clm_82b956559b621dfdc0bf80b136329fa6ac62ebd7f06232338a480f68d0581e16
- clm_b2c2e3fcc8d731e43ecbcb866e6bac8d2afc51d09674fa02a5304b8ba42151f4
- clm_c5d0b60e33ab546081d11c93c9c2a86ed9343fd99febc7d2a3d124a2fae61568
- clm_c7b18bf8319471c7b471be9b03c89651b4f6bb989a67b334557737fac9d6a114
maturity: draft
page_id: pg_9c7cc28e551b5b0987b4fa0ead63cdc2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_509412f0923a57d595c41aa6de538218
title: harishkotra/gaia-meme-coin-generator/README.md @ 32907e4a57bf
updated_at: '2026-09-14T03:56:05Z'
---

# harishkotra/gaia-meme-coin-generator/README.md @ 32907e4a57bf

<!-- rcw:begin owner=source:src_509412f0923a57d595c41aa6de538218 block=evidence -->
- The tool automates meme token creation: it uses Gaia's AI node to generate token names and themes, computes tokenomics, and deploys a limit-based token contract. [@claim:clm_08a5664c91b722949f727cff1fad8ad68822f7817d4ad1850d0a9de7d28021e5]
- Example output shows the tool prints generated coin details, deployment address and transaction hash, tokenomics, a deployment_details.json record, and a Base Sepolia explorer verification link. [@claim:clm_2ae4418941f6c3ce58b32e453869c5e08286055a6c50bbf6867b2669247e02ad]
- Generated tokens include safety features: maximum transaction limits, maximum wallet limits, and excludable addresses for CEX/DEX purposes. [@claim:clm_456bcdc421f64885f73f4b1faf14e4814129ab9ff3c6c33a171d1558910e6072]
- Stated use cases include token launch platforms, community/fan tokens, educational testnet practice, and marketing campaign tokens. [@claim:clm_4a2ef527ad0f22222bf6260b8a5f710448dbecdac7cbc72c40c5add310558291]
- Setup workflow: clone the repo, run npm install, create a .env file, then run the generator with npm start. [@claim:clm_600e65b51ce5786526bec0d389cbf687371886cec9e6ad7f556aae4199742e54]
- Repository development practice: contributions are welcomed via opening issues, submitting PRs, suggesting improvements, and adding new features. [@claim:clm_72c17d4a1e5de96e6d9dbbdc49e0f5adb07f4df83e70ae7cc844deed67aaae44]
- Tokenomics are auto-generated with example values of 500,000,000 total supply, 75% initial liquidity, 1% transaction limit, and 2% max wallet. [@claim:clm_7651cdd6a09a600105d1ea05d5d6155025415f624b09c17d00b2fd2a9b395e43]
- The README positions the tool for testnet experimentation and advises thorough testing, contract review, and regulatory-compliance consideration before mainnet use. [@claim:clm_766e8ae6676bd63b92404c6fa566d6810a2c6bef927e11fd21ae09ca078035bf]
- The project targets Base Sepolia by default but is described as easily adaptable to other networks. [@claim:clm_82b956559b621dfdc0bf80b136329fa6ac62ebd7f06232338a480f68d0581e16]
- The deployed contract is described as ERC20-compliant with ownership controls, a transaction limit system, wallet restrictions, and an address exclusion mechanism. [@claim:clm_b2c2e3fcc8d731e43ecbcb866e6bac8d2afc51d09674fa02a5304b8ba42151f4]
- The tool calls a Gaia AI node at the llama3b.gaia.domains/v1 endpoint for creative naming, per the README. [@claim:clm_c5d0b60e33ab546081d11c93c9c2a86ed9343fd99febc7d2a3d124a2fae61568]
- Configuration is via a .env file with GAIA_URL, GAIA_MODEL, BASE_NODE_URL, and PRIVATE_KEY variables; the tool is run with npm start. [@claim:clm_c7b18bf8319471c7b471be9b03c89651b4f6bb989a67b334557737fac9d6a114]
<!-- rcw:end owner=source:src_509412f0923a57d595c41aa6de538218 block=evidence -->

## Researcher notes

