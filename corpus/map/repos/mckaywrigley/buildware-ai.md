# mckaywrigley/buildware-ai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 53da76526301 @ 346f4b8a723bba60

## Summary (orientation draft, not independently verified)

The evidence consists only of the repository README for Buildware, an AI tool that turns issues into AI-generated pull requests. It documents setup (npm, Postgres, GitHub PAT, API keys) and planned features, but contains no code-level evidence about runtime internals.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Buildware is described as a tool for shipping code faster with AI: users build a code instruction system, give it an issue, and receive an AI-generated pull request. -- evidence: [README.md#L5-L5](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L5-L5), [README.md#L3-L3](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L3-L3)
  - [inference/documented] The project appears to be a Next.js application, based on the NEXT_PUBLIC_APP_MODE variable and .env.local convention used in setup instructions. -- evidence: [README.md#L43-L43](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L43-L43), [README.md#L53-L53](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L53-L53)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Setup involves cloning the repo, running npm install, copying .env.example to .env.local with required variables, running migrations, and starting the app with npm run dev. -- evidence: [README.md#L78-L80](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L78-L80), [README.md#L43-L43](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L43-L43), [README.md#L37-L39](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L37-L39), [README.md#L106-L108](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L106-L108), [README.md#L31-L33](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L31-L33)
  - [observation/documented] The simple version can be deployed to Vercel via a one-click deploy button that preconfigures the five required environment variables. -- evidence: [README.md#L114-L114](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L114-L114), [README.md#L112-L112](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L112-L112)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] An app mode environment variable NEXT_PUBLIC_APP_MODE=simple indicates the product ships in a 'simple' mode, with an advanced version referenced but not yet documented. -- evidence: [README.md#L53-L53](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L53-L53), [README.md#L118-L118](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L118-L118)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product uses a GitHub personal access token that must have read/write access to Contents and Pull Requests, plus read-only Metadata, scoped to selected or all repositories. -- evidence: [README.md#L90-L100](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L90-L100)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The simple version requires a Postgres database (Supabase or Neon recommended), a DATABASE_URL, and API keys for Anthropic and OpenAI. -- evidence: [README.md#L70-L70](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L70-L70), [README.md#L62-L62](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L62-L62), [README.md#L57-L58](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L57-L58), [README.md#L72-L72](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L72-L72)
- limitations (1 claim(s)):
  - [observation/documented] As of the README's July 17, 2024 update, the advanced setup guide was not yet available; Linear integration, local codebase mode, and team support were listed as coming soon. -- evidence: [README.md#L118-L118](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L118-L118), [README.md#L21-L23](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L21-L23)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](buildware-ai.detail.md).

Metadata and full claim list: [full detail](buildware-ai.detail.md)
Human notes ([notes](buildware-ai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
