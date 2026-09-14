---
access: public
aliases: []
claim_ids:
- clm_54dbea4180ee8566b6b015034185e0fffa7c623697be356becec4f660b1f0ce4
- clm_9d194bb0ee338f0b176325a2cdf72524d348d7d5e02515a0dea182fa11703d6b
- clm_a03dabd60352c3d0a2411f6216043256f18d058526e1b72aff97fe68ad362454
- clm_eb697444ddf96211dbc3b7a78818c29ac3ba2f69415f94c3da1138448098928d
maturity: draft
page_id: pg_8cc08a34f27b56218e1ddb5c50fed7ec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b65f4224efb65ca9a4f8af4c142e5d1a
title: humanlayer/humanlayer/docs/docs.knowledge.md @ 99abe673498c
updated_at: '2026-09-14T02:04:25Z'
---

# humanlayer/humanlayer/docs/docs.knowledge.md @ 99abe673498c

<!-- rcw:begin owner=source:src_b65f4224efb65ca9a4f8af4c142e5d1a block=evidence -->
- Docs knowledge describes a three-level contact-channel configuration hierarchy (operation, SDK, project) where operation-level settings override SDK-level, which override project defaults. [@claim:clm_54dbea4180ee8566b6b015034185e0fffa7c623697be356becec4f660b1f0ce4]
- Repository development practice: documentation is built on Mintlify, previewed locally via 'mintlify dev' (Node.js 19+ required), and deployed automatically to docs.humanlayer.dev through a Vercel integration. [@claim:clm_9d194bb0ee338f0b176325a2cdf72524d348d7d5e02515a0dea182fa11703d6b]
- Repository development practice: docs.knowledge.md records a release process using semver tags, jointly versioned Python and TypeScript packages, pyproject.toml/package.json version edits, and make build-and-publish / npm publish steps. [@claim:clm_a03dabd60352c3d0a2411f6216043256f18d058526e1b72aff97fe68ad362454]
- Internal docs knowledge describes contact channels (Slack, email, web embeds, SMS/WhatsApp in beta) as composable, with web embeds requiring a backend proxy so HumanLayer API keys are never exposed to the frontend. [@claim:clm_eb697444ddf96211dbc3b7a78818c29ac3ba2f69415f94c3da1138448098928d]
<!-- rcw:end owner=source:src_b65f4224efb65ca9a4f8af4c142e5d1a block=evidence -->

## Researcher notes

