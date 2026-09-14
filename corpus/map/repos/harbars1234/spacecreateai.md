# harbars1234/spacecreateai

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 853d1e3d0ac5 @ ecd1a0cf9b948f4b

## Summary (orientation draft, not independently verified)

Selected evidence records: The README describes the project as a Solana agent built with SEND AI technology (solana-agent-kit) that automatically creates the agent, deploys a token, and airdrops tokens once launched. The project builds on the sendaifun/solana-agent-kit library, which the README cites as the underlying SEND AI technology.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes the project as a Solana agent built with SEND AI technology (solana-agent-kit) that automatically creates the agent, deploys a token, and airdrops tokens once launched. -- evidence: [README.md#L3-L3](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Setup prerequisites call for Node.js v14+ (recommended), the Solana CLI, and a newly generated keypair funded via a devnet airdrop of 2 SOL. -- evidence: [README.md#L7-L12](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L7-L12)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The project builds on the sendaifun/solana-agent-kit library, which the README cites as the underlying SEND AI technology. -- evidence: [README.md#L3-L3](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L3-L3)
  - [inference/documented] The CHANGELOG.md appears to be copied wholesale from the ai16z/eliza project (versions v0.0.1 through v0.1.6-alpha.4), suggesting the repo vendors or derives from the Eliza framework rather than having its own release history. -- evidence: [CHANGELOG.md#L399-L399](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L399-L399), [CHANGELOG.md#L1058-L1058](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L1058-L1058), [CHANGELOG.md#L5-L5](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L5-L5)
- limitations (1 claim(s)):
  - [inference/documented] The README's claims about agent creation, token deployment, and airdropping are documentation statements only; the supplied evidence contains no source code demonstrating this behavior, so the described functionality is unverified in this snapshot. -- evidence: [README.md#L3-L3](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/README.md#L3-L3)
- relevance (1 claim(s)):
  - [inference/documented] The upstream Eliza changelog indicates the underlying framework supports Solana token operations such as creating, buying, and selling tokens via a plugin-solana bonding-curve integration, which is relevant to this repo's token-deployment purpose. -- evidence: [CHANGELOG.md#L109-L184](https://github.com/Harbars1234/SpaceCreateAI/blob/853d1e3d0ac53d295fc56fb084d32c0abdb7cdf2/CHANGELOG.md#L109-L184)

Every claim for this repository is shown above and in [full detail](spacecreateai.detail.md).

Metadata and full claim list: [full detail](spacecreateai.detail.md)
Human notes ([notes](spacecreateai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
