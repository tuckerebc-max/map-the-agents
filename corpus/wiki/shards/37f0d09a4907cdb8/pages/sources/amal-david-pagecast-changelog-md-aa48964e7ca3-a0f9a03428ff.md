---
access: public
aliases: []
claim_ids:
- clm_0df49829d21c23d1879aa2b58c1e86c6ab12e7a5aa0fa3ec3c5ecc464654975e
- clm_264eff79fb71f91930adb23b9a197f06d32ce1ef73b3efea4f670c1d673e955c
- clm_c1e12176466c486a3e5c9a2eb3838b4deaca4620f87dc347a35c8bd96bcf508d
- clm_e048163639735c0859eaa792c3e11de71dbc056ebec4db5b7eae9472bf9bc32e
- clm_e3398880db828075731712692441b5c282889e5608dcb3bbc68fcab3f5968c86
maturity: draft
page_id: pg_dba057f1381c5b619288a0f9a03428ff
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_63eac2ec1c805c878004950a6f14d64f
title: Amal-David/pagecast/CHANGELOG.md @ aa48964e7ca3
updated_at: '2026-09-14T03:33:49Z'
---

# Amal-David/pagecast/CHANGELOG.md @ aa48964e7ca3

<!-- rcw:begin owner=source:src_63eac2ec1c805c878004950a6f14d64f block=evidence -->
- Wrangler is pinned at 4.86.0 in src/platform.js and baked into the Docker image so deploys do not contact npm at runtime; the root CLI/server has no runtime npm dependencies. [@claim:clm_0df49829d21c23d1879aa2b58c1e86c6ab12e7a5aa0fa3ec3c5ecc464654975e]
- Publishing is context-aware: repeating a publish in the same agent context (via --context-id, PAGECAST_CONTEXT_ID, CODEX_THREAD_ID, CLAUDE_SESSION_ID, or workspace fallback) updates the existing URL. [@claim:clm_264eff79fb71f91930adb23b9a197f06d32ce1ef73b3efea4f670c1d673e955c]
- The admin API is loopback-only and separate from MCP; non-loopback binds are rejected, with an explicit wildcard exception only for the packaged loopback-mapped Docker proxy. [@claim:clm_c1e12176466c486a3e5c9a2eb3838b4deaca4620f87dc347a35c8bd96bcf508d]
- Telemetry is anonymous (command name, versions, OS/arch only), default-on for fresh interactive installs with a one-time disclosure, off in CI, and controllable via pagecast telemetry or DO_NOT_TRACK=1. [@claim:clm_e048163639735c0859eaa792c3e11de71dbc056ebec4db5b7eae9472bf9bc32e]
- Password protection and link expiry are enforced at the edge by a generated Cloudflare Pages Function covering every file of a multi-file report. [@claim:clm_e3398880db828075731712692441b5c282889e5608dcb3bbc68fcab3f5968c86]
<!-- rcw:end owner=source:src_63eac2ec1c805c878004950a6f14d64f block=evidence -->

## Researcher notes

