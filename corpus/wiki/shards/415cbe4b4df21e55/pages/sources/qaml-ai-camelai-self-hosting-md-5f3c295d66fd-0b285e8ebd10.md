---
access: public
aliases: []
claim_ids:
- clm_198b9a40b18c3500cb4fc900d0af22c77ad2701cca1e757db87c1059f458473d
- clm_5e9a0e1144ca8ecfcf0f277d84ab7888b113a30856e9e2e6247ae9c928aaea16
- clm_fd39b50ab4b25439b54249e86633fb6b220564146828fb0f3fbef988780abae6
maturity: draft
page_id: pg_01ced01e1cbf56bd8b390b285e8ebd10
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4c125861811955f6a4df678d2909abe8
title: qaml-ai/camelAI/SELF_HOSTING.md @ 5f3c295d66fd
updated_at: '2026-09-14T02:33:58Z'
---

# qaml-ai/camelAI/SELF_HOSTING.md @ 5f3c295d66fd

<!-- rcw:begin owner=source:src_4c125861811955f6a4df678d2909abe8 block=evidence -->
- Self-hosted deployments expose GET /api/selfhost/health as both the readiness endpoint and a versioned machine-readable capability contract; failed runtime checks return HTTP 503 with status fail. [@claim:clm_198b9a40b18c3500cb4fc900d0af22c77ad2701cca1e757db87c1059f458473d]
- In self-host mode the application container has read-write Docker-socket access so workerd can manage sandbox containers; anyone controlling that container should be treated as having root-equivalent VM control. [@claim:clm_5e9a0e1144ca8ecfcf0f277d84ab7888b113a30856e9e2e6247ae9c928aaea16]
- Development requires Node.js 22+, Bun, a Cloudflare account, and Docker for sandbox-backed features and agent evals; in the self-host target the application runs under workerd. [@claim:clm_fd39b50ab4b25439b54249e86633fb6b220564146828fb0f3fbef988780abae6]
<!-- rcw:end owner=source:src_4c125861811955f6a4df678d2909abe8 block=evidence -->

## Researcher notes

