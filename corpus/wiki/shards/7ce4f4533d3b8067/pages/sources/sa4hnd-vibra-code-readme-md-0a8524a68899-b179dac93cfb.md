---
access: public
aliases: []
claim_ids:
- clm_0e75c6122e9494b0ab34b9fd39c54374007406a4e99b7707177fde2ce8f0aa59
- clm_1d9380c1291c81122dadb9580c9a762d3e92d3f7676a016cd0c487d38887e7d7
- clm_445804377daa31d0e9b21d2ebe36cd33324a0cf2295744c91f6c4b09e337bf3d
- clm_5625c342cdfd7f6e6a0b8c3a6f3f1b6eb387742043d92186fde32e3de7859cc9
- clm_6b91b195d318c0d2d0e68d8cac7582c16be658cfa2a30d697f1f39836965398d
- clm_734af18fee98c96bef519d6e82a00427728c9502813ab750ba1362b9f533cdb3
- clm_79062d92b4b0075f561ad1c80f8f1dd3a935486c9abb070efaf93bdcbdbae02a
- clm_c95997c3b33926e0be620488cf9839a1e86e92b65f9571b81c6a16982d43927e
- clm_d0c23800c7a6a68117821473a482035ed58133629e9448735eb5c0bf7e4b53dd
- clm_d6d41f0cd3270c0f3df8d842973b47e73926df195c37e0635240ce3d1650bb02
- clm_da348189e82c6d871ea166c3aeea220bba0ab26e0974ddd3ba249d3b87364a3a
- clm_e80fa95b83428210a0afb5e27216a39ef33389677390623f540b2ee6b8632af6
maturity: draft
page_id: pg_23e55a80d1ca53a6b1abb179dac93cfb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_98f0d367e9995225afb58cb97dfddc81
title: sa4hnd/vibra-code/README.md @ 0a8524a68899
updated_at: '2026-09-14T02:37:53Z'
---

# sa4hnd/vibra-code/README.md @ 0a8524a68899

<!-- rcw:begin owner=source:src_98f0d367e9995225afb58cb97dfddc81 block=evidence -->
- Vibra Code is an open-source AI app builder: users describe mobile apps in plain English, a backend runs Claude Code inside an E2B cloud sandbox to generate apps, and a live preview appears on the phone. [@claim:clm_0e75c6122e9494b0ab34b9fd39c54374007406a4e99b7707177fde2ce8f0aa59]
- The mobile app's core is a native iOS chat UI built with Texture (AsyncDisplayKit) and IGListKit, described as off-main-thread rendering targeting 60fps scrolling. [@claim:clm_1d9380c1291c81122dadb9580c9a762d3e92d3f7676a016cd0c487d38887e7d7]
- Users can describe apps by voice or attach mockup screenshots as input, and generated projects can be pushed directly to GitHub. [@claim:clm_445804377daa31d0e9b21d2ebe36cd33324a0cf2295744c91f6c4b09e337bf3d]
- The product supports multiple AI providers — Claude (default), Cursor, and Gemini — switchable with a single environment variable. [@claim:clm_5625c342cdfd7f6e6a0b8c3a6f3f1b6eb387742043d92186fde32e3de7859cc9]
- The iOS client exposes modals for selecting the AI provider, browsing generated files, viewing live sandbox logs, publishing to GitHub, haptic settings, and editing environment variables. [@claim:clm_6b91b195d318c0d2d0e68d8cac7582c16be658cfa2a30d697f1f39836965398d]
- The README positions Vibra Code as an open-source, self-hostable alternative to closed-source AI app builders such as Vibe Code App, Rork, Lovable, and Bolt.new, focused on native mobile apps built with Expo. [@claim:clm_734af18fee98c96bef519d6e82a00427728c9502813ab750ba1362b9f533cdb3]
- Documented flow: the backend creates a Convex session, Inngest spawns an E2B sandbox where the AI agent generates code, updates stream back via Convex, and the phone opens a live preview through a tunnel URL. [@claim:clm_79062d92b4b0075f561ad1c80f8f1dd3a935486c9abb070efaf93bdcbdbae02a]
- Real-time synchronization is handled by Convex, with changes streaming from the sandbox to the phone instantly. [@claim:clm_c95997c3b33926e0be620488cf9839a1e86e92b65f9571b81c6a16982d43927e]
- Chat messages from Convex are rendered as distinct node types: text with markdown, file reads (blue), edits (orange), bash commands (green), todo task cards, and a working-status indicator. [@claim:clm_d0c23800c7a6a68117821473a482035ed58133629e9448735eb5c0bf7e4b53dd]
- Required configuration includes ANTHROPIC_API_KEY for AI generation, E2B_API_KEY for sandboxes, Clerk keys for authentication, and a Convex deployment URL; Stripe and RevenueCat keys are optional, only for payments. [@claim:clm_d6d41f0cd3270c0f3df8d842973b47e73926df195c37e0635240ce3d1650bb02]
- The architecture diagram shows three tiers: an Expo iOS app talking over an API to a Next.js + Convex server, which queues work via Inngest to an E2B sandbox running the AI agent. [@claim:clm_da348189e82c6d871ea166c3aeea220bba0ab26e0974ddd3ba249d3b87364a3a]
- The project is licensed under AGPL-3.0 and is positioned as self-hostable with customizable AI prompts and swappable AI providers. [@claim:clm_e80fa95b83428210a0afb5e27216a39ef33389677390623f540b2ee6b8632af6]
<!-- rcw:end owner=source:src_98f0d367e9995225afb58cb97dfddc81 block=evidence -->

## Researcher notes

