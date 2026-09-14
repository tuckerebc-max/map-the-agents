# mckaywrigley/buildware-ai -- full detail

[Back to orientation](buildware-ai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mckaywrigley/buildware-ai/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/346f4b8a723bba60.json](../../../wiki/dossiers/mckaywrigley/buildware-ai/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/346f4b8a723bba60.json)

## specifications (2 claim(s))

- [observation/documented] Buildware is described as a tool for shipping code faster with AI: users build a code instruction system, give it an issue, and receive an AI-generated pull request. -- evidence: [README.md#L5-L5](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L5-L5), [README.md#L3-L3](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L3-L3) (`clm_3566883c5e8247f720030876ea8f043badf36d59a0566cc8c58f7da217c16418`)
- [inference/documented] The project appears to be a Next.js application, based on the NEXT_PUBLIC_APP_MODE variable and .env.local convention used in setup instructions. -- evidence: [README.md#L43-L43](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L43-L43), [README.md#L53-L53](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L53-L53) (`clm_04d368341d06cdbba513c5956bd15f56ce0107b6bac1081b82b85e485f77cb5d`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Setup involves cloning the repo, running npm install, copying .env.example to .env.local with required variables, running migrations, and starting the app with npm run dev. -- evidence: [README.md#L78-L80](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L78-L80), [README.md#L43-L43](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L43-L43), [README.md#L37-L39](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L37-L39), [README.md#L106-L108](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L106-L108), [README.md#L31-L33](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L31-L33) (`clm_e0f505688514cde7a6fc49535a3bbb941b79afc86ad32024939a956952624042`)
- [observation/documented] The simple version can be deployed to Vercel via a one-click deploy button that preconfigures the five required environment variables. -- evidence: [README.md#L114-L114](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L114-L114), [README.md#L112-L112](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L112-L112) (`clm_24d22e720752d631be02128004f2d975ce02a8504dad4a8cb1bb6c0e7b38d31d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] An app mode environment variable NEXT_PUBLIC_APP_MODE=simple indicates the product ships in a 'simple' mode, with an advanced version referenced but not yet documented. -- evidence: [README.md#L53-L53](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L53-L53), [README.md#L118-L118](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L118-L118) (`clm_c18b846cf99fc4841630555bb7192df89e31a9429bdf19027e1b9e92fb60b525`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The product uses a GitHub personal access token that must have read/write access to Contents and Pull Requests, plus read-only Metadata, scoped to selected or all repositories. -- evidence: [README.md#L90-L100](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L90-L100) (`clm_0d9ee264ba7f102657708ba7a0533f5b922cce5548f5775b19f839bb7fc1325e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The simple version requires a Postgres database (Supabase or Neon recommended), a DATABASE_URL, and API keys for Anthropic and OpenAI. -- evidence: [README.md#L70-L70](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L70-L70), [README.md#L62-L62](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L62-L62), [README.md#L57-L58](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L57-L58), [README.md#L72-L72](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L72-L72) (`clm_3f9ac076dd55e02a0b93efd8760db0893192d55a4284f844b0507aa38a42a34e`)

## limitations (1 claim(s))

- [observation/documented] As of the README's July 17, 2024 update, the advanced setup guide was not yet available; Linear integration, local codebase mode, and team support were listed as coming soon. -- evidence: [README.md#L118-L118](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L118-L118), [README.md#L21-L23](https://github.com/mckaywrigley/buildware-ai/blob/53da76526301e16bdcbd7db1d4ec548e4d9f1c86/README.md#L21-L23) (`clm_9eaab1decb27641dd58e86e6eeb8b4ea896ff998e6c697ab0b0aadde57370148`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

