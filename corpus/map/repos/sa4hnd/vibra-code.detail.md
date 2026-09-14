# sa4hnd/vibra-code -- full detail

[Back to orientation](vibra-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sa4hnd/vibra-code/0a8524a68899e7d98bdd12787f624fdcd062c74c/1b89e3adc0f154c1.json](../../../wiki/dossiers/sa4hnd/vibra-code/0a8524a68899e7d98bdd12787f624fdcd062c74c/1b89e3adc0f154c1.json)

## specifications (1 claim(s))

- [observation/documented] Vibra Code is an open-source AI app builder: users describe mobile apps in plain English, a backend runs Claude Code inside an E2B cloud sandbox to generate apps, and a live preview appears on the phone. -- evidence: [README.md#L70-L70](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L70-L70) (`clm_0e75c6122e9494b0ab34b9fd39c54374007406a4e99b7707177fde2ce8f0aa59`)

## components (2 claim(s))

- [observation/documented] The architecture diagram shows three tiers: an Expo iOS app talking over an API to a Next.js + Convex server, which queues work via Inngest to an E2B sandbox running the AI agent. -- evidence: [README.md#L132-L140](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L132-L140) (`clm_da348189e82c6d871ea166c3aeea220bba0ab26e0974ddd3ba249d3b87364a3a`)
- [observation/documented] The mobile app's core is a native iOS chat UI built with Texture (AsyncDisplayKit) and IGListKit, described as off-main-thread rendering targeting 60fps scrolling. -- evidence: [README.md#L100-L100](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L100-L100), [README.md#L258-L258](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L258-L258) (`clm_1d9380c1291c81122dadb9580c9a762d3e92d3f7676a016cd0c487d38887e7d7`)

## design-choices (2 claim(s))

- [observation/documented] The product supports multiple AI providers — Claude (default), Cursor, and Gemini — switchable with a single environment variable. -- evidence: [README.md#L102-L102](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L102-L102) (`clm_5625c342cdfd7f6e6a0b8c3a6f3f1b6eb387742043d92186fde32e3de7859cc9`)
- [observation/documented] The project is licensed under AGPL-3.0 and is positioned as self-hostable with customizable AI prompts and swappable AI providers. -- evidence: [README.md#L24-L26](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L24-L26), [README.md#L346-L346](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L346-L346), [README.md#L72-L72](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L72-L72) (`clm_e80fa95b83428210a0afb5e27216a39ef33389677390623f540b2ee6b8632af6`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Users can describe apps by voice or attach mockup screenshots as input, and generated projects can be pushed directly to GitHub. -- evidence: [README.md#L113-L113](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L113-L113), [README.md#L111-L111](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L111-L111) (`clm_445804377daa31d0e9b21d2ebe36cd33324a0cf2295744c91f6c4b09e337bf3d`)

## interfaces (2 claim(s))

- [observation/documented] Chat messages from Convex are rendered as distinct node types: text with markdown, file reads (blue), edits (orange), bash commands (green), todo task cards, and a working-status indicator. -- evidence: [README.md#L310-L317](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L310-L317) (`clm_d0c23800c7a6a68117821473a482035ed58133629e9448735eb5c0bf7e4b53dd`)
- [observation/documented] The iOS client exposes modals for selecting the AI provider, browsing generated files, viewing live sandbox logs, publishing to GitHub, haptic settings, and editing environment variables. -- evidence: [README.md#L297-L304](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L297-L304) (`clm_6b91b195d318c0d2d0e68d8cac7582c16be658cfa2a30d697f1f39836965398d`)

## memory-state (1 claim(s))

- [observation/documented] Real-time synchronization is handled by Convex, with changes streaming from the sandbox to the phone instantly. -- evidence: [README.md#L106-L106](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L106-L106) (`clm_c95997c3b33926e0be620488cf9839a1e86e92b65f9571b81c6a16982d43927e`)

## orchestration (1 claim(s))

- [observation/documented] Documented flow: the backend creates a Convex session, Inngest spawns an E2B sandbox where the AI agent generates code, updates stream back via Convex, and the phone opens a live preview through a tunnel URL. -- evidence: [README.md#L142-L147](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L142-L147) (`clm_79062d92b4b0075f561ad1c80f8f1dd3a935486c9abb070efaf93bdcbdbae02a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Required configuration includes ANTHROPIC_API_KEY for AI generation, E2B_API_KEY for sandboxes, Clerk keys for authentication, and a Convex deployment URL; Stripe and RevenueCat keys are optional, only for payments. -- evidence: [README.md#L162-L162](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L162-L162), [README.md#L155-L160](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L155-L160) (`clm_d6d41f0cd3270c0f3df8d842973b47e73926df195c37e0635240ce3d1650bb02`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The README positions Vibra Code as an open-source, self-hostable alternative to closed-source AI app builders such as Vibe Code App, Rork, Lovable, and Bolt.new, focused on native mobile apps built with Expo. -- evidence: [README.md#L331-L336](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L331-L336), [README.md#L82-L88](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L82-L88), [README.md#L72-L72](https://github.com/sa4hnd/vibra-code/blob/0a8524a68899e7d98bdd12787f624fdcd062c74c/README.md#L72-L72) (`clm_734af18fee98c96bef519d6e82a00427728c9502813ab750ba1362b9f533cdb3`)

