---
access: public
aliases: []
claim_ids:
- clm_0467e5bc19b3a45e43bff1bc05753299b7310b6c12af0095373a3cc222736b7a
- clm_386fc9d4e74c5ef4010109d621cb9cb76073f5b88d117fcaa6a1a64633d32f1c
- clm_38a18c6c9de4a306d3a25d9684c82a63c8946b706699db2b706872080f6824aa
- clm_a69d6c2ca96df882fcbbb5de97467aee9b54a11a4aaca1d5fb5285b8037ff1a2
- clm_cdfe672ecf5ab141c77cf8b22a349b9795d7d534e0165fa50c67b85830aada55
- clm_d2c6e93fb7e4dd056658450e268967bf880689f3b9ae8967e599ac55775d985c
- clm_f1eb0e72186048eb8870356c67db3d88b2de21fa84a2d726d25941af04ebb608
maturity: draft
page_id: pg_8e96f1bc9fc4590fa0ccb5e079488d59
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b4c6282aceb75df6b0c0a6c59ecd8ef4
title: Gerome-Elassaad/CodingIT/CHANGELOG.md @ b21eff408c44
updated_at: '2026-09-14T01:50:19Z'
---

# Gerome-Elassaad/CodingIT/CHANGELOG.md @ b21eff408c44

<!-- rcw:begin owner=source:src_b4c6282aceb75df6b0c0a6c59ecd8ef4 block=evidence -->
- Security hardening includes SSRF prevention with domain allowlisting for PyPI/npm requests, input validation, rate limiting, and a centralized lib/security.ts module. [@claim:clm_0467e5bc19b3a45e43bff1bc05753299b7310b6c12af0095373a3cc222736b7a]
- A Stripe payment system provides checkout, billing portal, and webhook handling, with Pro ($9/month) and Enterprise ($25/month) subscription plans. [@claim:clm_386fc9d4e74c5ef4010109d621cb9cb76073f5b88d117fcaa6a1a64633d32f1c]
- Usage limits are enforced per tier: GitHub imports 5/50/unlimited per month, storage 100MB/5GB/unlimited, and execution time 30s/300s/600s for Free/Pro/Enterprise. [@claim:clm_38a18c6c9de4a306d3a25d9684c82a63c8946b706699db2b706872080f6824aa]
- The theme system was simplified to dark mode only; light theme support and the theme toggle were removed. [@claim:clm_a69d6c2ca96df882fcbbb5de97467aee9b54a11a4aaca1d5fb5285b8037ff1a2]
- Chat persistence stores sessions and messages in AWS S3 under a users/{userId}/sessions/{sessionId} layout with metadata.json and messages.json, plus aggregate analytics folders. [@claim:clm_cdfe672ecf5ab141c77cf8b22a349b9795d7d534e0165fa50c67b85830aada55]
- Chat session REST endpoints cover listing/creating sessions, per-session management, messages, cross-history search, analytics, and JSON/CSV export. [@claim:clm_d2c6e93fb7e4dd056658450e268967bf880689f3b9ae8967e599ac55775d985c]
- Workflow builder and deployment features were removed as a breaking change; users can no longer access them, with focus on core AI code generation and sandbox execution. [@claim:clm_f1eb0e72186048eb8870356c67db3d88b2de21fa84a2d726d25941af04ebb608]
<!-- rcw:end owner=source:src_b4c6282aceb75df6b0c0a6c59ecd8ef4 block=evidence -->

## Researcher notes

