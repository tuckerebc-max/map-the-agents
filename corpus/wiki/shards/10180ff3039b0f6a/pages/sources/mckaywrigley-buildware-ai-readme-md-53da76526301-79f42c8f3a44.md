---
access: public
aliases: []
claim_ids:
- clm_04d368341d06cdbba513c5956bd15f56ce0107b6bac1081b82b85e485f77cb5d
- clm_0d9ee264ba7f102657708ba7a0533f5b922cce5548f5775b19f839bb7fc1325e
- clm_24d22e720752d631be02128004f2d975ce02a8504dad4a8cb1bb6c0e7b38d31d
- clm_3566883c5e8247f720030876ea8f043badf36d59a0566cc8c58f7da217c16418
- clm_3f9ac076dd55e02a0b93efd8760db0893192d55a4284f844b0507aa38a42a34e
- clm_9eaab1decb27641dd58e86e6eeb8b4ea896ff998e6c697ab0b0aadde57370148
- clm_c18b846cf99fc4841630555bb7192df89e31a9429bdf19027e1b9e92fb60b525
- clm_e0f505688514cde7a6fc49535a3bbb941b79afc86ad32024939a956952624042
maturity: draft
page_id: pg_7cbd169cea1d5a99a15779f42c8f3a44
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0d9535dea8a85568a8596d0d6ef7e7c8
title: mckaywrigley/buildware-ai/README.md @ 53da76526301
updated_at: '2026-09-14T02:17:31Z'
---

# mckaywrigley/buildware-ai/README.md @ 53da76526301

<!-- rcw:begin owner=source:src_0d9535dea8a85568a8596d0d6ef7e7c8 block=evidence -->
- The project appears to be a Next.js application, based on the NEXT_PUBLIC_APP_MODE variable and .env.local convention used in setup instructions. [@claim:clm_04d368341d06cdbba513c5956bd15f56ce0107b6bac1081b82b85e485f77cb5d]
- The product uses a GitHub personal access token that must have read/write access to Contents and Pull Requests, plus read-only Metadata, scoped to selected or all repositories. [@claim:clm_0d9ee264ba7f102657708ba7a0533f5b922cce5548f5775b19f839bb7fc1325e]
- The simple version can be deployed to Vercel via a one-click deploy button that preconfigures the five required environment variables. [@claim:clm_24d22e720752d631be02128004f2d975ce02a8504dad4a8cb1bb6c0e7b38d31d]
- Buildware is described as a tool for shipping code faster with AI: users build a code instruction system, give it an issue, and receive an AI-generated pull request. [@claim:clm_3566883c5e8247f720030876ea8f043badf36d59a0566cc8c58f7da217c16418]
- The simple version requires a Postgres database (Supabase or Neon recommended), a DATABASE_URL, and API keys for Anthropic and OpenAI. [@claim:clm_3f9ac076dd55e02a0b93efd8760db0893192d55a4284f844b0507aa38a42a34e]
- As of the README's July 17, 2024 update, the advanced setup guide was not yet available; Linear integration, local codebase mode, and team support were listed as coming soon. [@claim:clm_9eaab1decb27641dd58e86e6eeb8b4ea896ff998e6c697ab0b0aadde57370148]
- An app mode environment variable NEXT_PUBLIC_APP_MODE=simple indicates the product ships in a 'simple' mode, with an advanced version referenced but not yet documented. [@claim:clm_c18b846cf99fc4841630555bb7192df89e31a9429bdf19027e1b9e92fb60b525]
- Setup involves cloning the repo, running npm install, copying .env.example to .env.local with required variables, running migrations, and starting the app with npm run dev. [@claim:clm_e0f505688514cde7a6fc49535a3bbb941b79afc86ad32024939a956952624042]
<!-- rcw:end owner=source:src_0d9535dea8a85568a8596d0d6ef7e7c8 block=evidence -->

## Researcher notes

