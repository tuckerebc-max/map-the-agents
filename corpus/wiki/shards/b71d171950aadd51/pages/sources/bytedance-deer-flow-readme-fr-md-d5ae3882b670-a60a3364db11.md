---
access: public
aliases: []
claim_ids:
- clm_15f65575ecc3b5d8090e4243a00316e6d21d32b7db1a350225f91af8884c3e75
- clm_1803af411e1dce5ee868bc04a7f004a57255fa94c223b891e8abfeecca8bf82e
- clm_3d57d70b7cbe0a2375d3e65fe93901931f1253958cda949ea3eee9e7c93ccb6b
maturity: draft
page_id: pg_2c3d732ff45c5e278640a60a3364db11
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a75a00c68a8e5ea6a03dd380496f62d2
title: bytedance/deer-flow/README_fr.md @ d5ae3882b670
updated_at: '2026-09-14T01:38:55Z'
---

# bytedance/deer-flow/README_fr.md @ d5ae3882b670

<!-- rcw:begin owner=source:src_a75a00c68a8e5ea6a03dd380496f62d2 block=evidence -->
- DeerFlow 2.0 is a ground-up rewrite sharing no code with the original v1 Deep Research framework, which per the French README is maintained on a separate 1.x branch. [@claim:clm_15f65575ecc3b5d8090e4243a00316e6d21d32b7db1a350225f91af8884c3e75]
- Repository development practice: the documented setup flow recommends make setup, an interactive wizard generating a minimal config.yaml and writing keys to .env, with make doctor for configuration checks and make support-bundle producing sanitized diagnostics (no .env, raw conversations, or user file contents) for GitHub issues. [@claim:clm_1803af411e1dce5ee868bc04a7f004a57255fa94c223b891e8abfeecca8bf82e]
- The frontend uses Next.js 16, React 19, TypeScript and Tailwind v4, with the LangGraph SDK for orchestration/streaming and TanStack Query for server state, requiring Node 22+ and pnpm 10.26.2+; a README badge indicates Python 3.12+ for the backend. [@claim:clm_3d57d70b7cbe0a2375d3e65fe93901931f1253958cda949ea3eee9e7c93ccb6b]
<!-- rcw:end owner=source:src_a75a00c68a8e5ea6a03dd380496f62d2 block=evidence -->

## Researcher notes

