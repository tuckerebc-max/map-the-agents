# harbars1234/spacecreateai -- full detail

[Back to orientation](spacecreateai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/harbars1234/spacecreateai/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/ecd1a0cf9b948f4b.json](../../../wiki/dossiers/harbars1234/spacecreateai/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/ecd1a0cf9b948f4b.json)

## specifications (1 claim(s))

- [observation/documented] The README describes the project as a Solana agent built with SEND AI technology (solana-agent-kit) that automatically creates the agent, deploys a token, and airdrops tokens once launched. -- evidence: [README.md#L3-L3](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L3-L3) (`clm_3661a574f76362b787b399df054ac787dd7d6c67030ae8ae0ce2c7afeef9bdb6`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Setup prerequisites call for Node.js v14+ (recommended), the Solana CLI, and a newly generated keypair funded via a devnet airdrop of 2 SOL. -- evidence: [README.md#L7-L12](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L7-L12) (`clm_aec44b0149b6344f50f5ad25eadc054cd7762733e839311f0fadca88081f8c3d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project builds on the sendaifun/solana-agent-kit library, which the README cites as the underlying SEND AI technology. -- evidence: [README.md#L3-L3](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L3-L3) (`clm_9e8733e44c6645801a0856fc0471b8aa899233e7e27b1d3936840a0cd225f75b`)
- [inference/documented] The CHANGELOG.md appears to be copied wholesale from the ai16z/eliza project (versions v0.0.1 through v0.1.6-alpha.4), suggesting the repo vendors or derives from the Eliza framework rather than having its own release history. -- evidence: [CHANGELOG.md#L399-L399](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L399-L399), [CHANGELOG.md#L1058-L1058](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L1058-L1058), [CHANGELOG.md#L5-L5](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L5-L5) (`clm_df91b2f1a846a30b9d3ab57d9f8a0ff9692dfb60adfbd7c70744a699d2ee2bc1`)

## limitations (1 claim(s))

- [inference/documented] The README's claims about agent creation, token deployment, and airdropping are documentation statements only; the supplied evidence contains no source code demonstrating this behavior, so the described functionality is unverified in this snapshot. -- evidence: [README.md#L3-L3](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L3-L3) (`clm_c9c6b4945878881612c9ea890cd232500f6b1ade81827ce001971023268b3fa3`)

## relevance (1 claim(s))

- [inference/documented] The upstream Eliza changelog indicates the underlying framework supports Solana token operations such as creating, buying, and selling tokens via a plugin-solana bonding-curve integration, which is relevant to this repo's token-deployment purpose. -- evidence: [CHANGELOG.md#L109-L184](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L109-L184) (`clm_ecb8e86dc0b98c596cdfad756acb8f54e227ece5cce3e85e57a353af3538480a`)

