---
access: public
aliases: []
claim_ids:
- clm_0b6bd81e60b894784b4cbdb5856aa18cf25ea9b8e2faa1623aaddefd9d529328
- clm_0df49829d21c23d1879aa2b58c1e86c6ab12e7a5aa0fa3ec3c5ecc464654975e
- clm_1acc0b6bad4d5297736e3b3b456a5c5f43cac28234689aab4186ed6e3babc385
- clm_264eff79fb71f91930adb23b9a197f06d32ce1ef73b3efea4f670c1d673e955c
- clm_2bb3096e4c6aa9819d3e6e81ef84e616f76fd020a8ba63c5bfc90d562719bf76
- clm_64e83370fdf4dab1cd06a1405bde61e11698f79bde41735c679819444c155e6e
- clm_73ded06d5466c3940b395905e7e1219f667e7ae68f3adbc86b763b783509db83
- clm_8e38dab30f96190e5faeadfbc3da58bd0df95eea8c4b2303bdcb41117417be43
- clm_9a3b8265e207bfdfd82e32542c9e08f8bd6b3f8999c3fe06c8901fd7f19c06ea
- clm_9ee39afa30bc92e193796d0e11843f79532847316e4ed887a713e7312983b235
- clm_ba0959e46034531419d3207d1622a194b98a1f9946857322f615c6c267c5fd50
- clm_c16786f28ada19e983817fe1ea5a635d442603910fff1e8ff39792f425582733
- clm_c1e12176466c486a3e5c9a2eb3838b4deaca4620f87dc347a35c8bd96bcf508d
- clm_e048163639735c0859eaa792c3e11de71dbc056ebec4db5b7eae9472bf9bc32e
- clm_e3398880db828075731712692441b5c282889e5608dcb3bbc68fcab3f5968c86
- clm_e3a8a49006992e4db110e307cbfb667e330f9c9142a4e99653a7803e5d1c30f2
- clm_f0b0d1cfc5e38fb0870bb9ab3932614f2322b524bcc41a54077686b3a26bf80b
maturity: draft
page_id: pg_b18b9d67a0315b74b5e08eb4a28709e6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_39bca3d916f654e698593a5b2caffc62
title: Amal-David/pagecast/README.md @ aa48964e7ca3
updated_at: '2026-09-14T03:33:49Z'
---

# Amal-David/pagecast/README.md @ aa48964e7ca3

<!-- rcw:begin owner=source:src_39bca3d916f654e698593a5b2caffc62 block=evidence -->
- Server-rendered apps needing a running backend are not supported; users must export static assets first. [@claim:clm_0b6bd81e60b894784b4cbdb5856aa18cf25ea9b8e2faa1623aaddefd9d529328]
- Wrangler is pinned at 4.86.0 in src/platform.js and baked into the Docker image so deploys do not contact npm at runtime; the root CLI/server has no runtime npm dependencies. [@claim:clm_0df49829d21c23d1879aa2b58c1e86c6ab12e7a5aa0fa3ec3c5ecc464654975e]
- Suited to sharing HTML reports, dashboards, Markdown docs, and built static dist/build/out folders via memorable Cloudflare Pages links, including from coding agents through skills, plugin, or MCP. [@claim:clm_1acc0b6bad4d5297736e3b3b456a5c5f43cac28234689aab4186ed6e3babc385]
- Publishing is context-aware: repeating a publish in the same agent context (via --context-id, PAGECAST_CONTEXT_ID, CODEX_THREAD_ID, CLAUDE_SESSION_ID, or workspace fallback) updates the existing URL. [@claim:clm_264eff79fb71f91930adb23b9a197f06d32ce1ef73b3efea4f670c1d673e955c]
- Pagecast ships a publish-report agent skill installable via Skills.sh, a Claude Code plugin, and a Chrome extension (experimental, load-unpacked) adding a one-click publish button on file:/// HTML pages. [@claim:clm_2bb3096e4c6aa9819d3e6e81ef84e616f76fd020a8ba63c5bfc90d562719bf76]
- Optional analytics deploys a Cloudflare Worker plus D1 database showing views, anonymous uniques, and recent events; raw IPs are HMACed with a per-Home secret and detailed events expire after 30 days. [@claim:clm_64e83370fdf4dab1cd06a1405bde61e11698f79bde41735c679819444c155e6e]
- New unlisted links combine a memorable prefix with 128 bits of entropy; unlisted is a bearer capability, not authentication, while password protection is the access-control feature and short vanity slugs are intentionally public drops. [@claim:clm_73ded06d5466c3940b395905e7e1219f667e7ae68f3adbc86b763b783509db83]
- The CLI exposes commands such as publish (with --json, --expires, --new-link, --update, --password), pages deploy, pages deployments list/delete/prune, background, telemetry, and mcp. [@claim:clm_8e38dab30f96190e5faeadfbc3da58bd0df95eea8c4b2303bdcb41117417be43]
- A user-level ~/.pagecast/home/ owns the managed Cloudflare target, publication registry, analytics config, operation journal, and exclusive lease; workspace .pagecast/ holds only identity and Home mappings. [@claim:clm_9a3b8265e207bfdfd82e32542c9e08f8bd6b3f8999c3fe06c8901fd7f19c06ea]
- Requires Node.js 20.19+ and a Cloudflare account for publishing; runs via npx with no global install. [@claim:clm_9ee39afa30bc92e193796d0e11843f79532847316e4ed887a713e7312983b235]
- Pagecast is a local-first publishing tool for agent-generated reports and small static web projects, supporting preview, publish, re-sync, rename, password protection, and URL revocation. [@claim:clm_ba0959e46034531419d3207d1622a194b98a1f9946857322f615c6c267c5fd50]
- The MCP server exposes a bounded tool surface (status, list_pages, publish_content, publish_file, revoke_publication) with safety gates like confirm flags and asset-confirmation requirements; outputs are redacted by default. [@claim:clm_c16786f28ada19e983817fe1ea5a635d442603910fff1e8ff39792f425582733]
- The admin API is loopback-only and separate from MCP; non-loopback binds are rejected, with an explicit wildcard exception only for the packaged loopback-mapped Docker proxy. [@claim:clm_c1e12176466c486a3e5c9a2eb3838b4deaca4620f87dc347a35c8bd96bcf508d]
- Telemetry is anonymous (command name, versions, OS/arch only), default-on for fresh interactive installs with a one-time disclosure, off in CI, and controllable via pagecast telemetry or DO_NOT_TRACK=1. [@claim:clm_e048163639735c0859eaa792c3e11de71dbc056ebec4db5b7eae9472bf9bc32e]
- Password protection and link expiry are enforced at the edge by a generated Cloudflare Pages Function covering every file of a multi-file report. [@claim:clm_e3398880db828075731712692441b5c282889e5608dcb3bbc68fcab3f5968c86]
- Repository development practice: UI work uses pnpm 10 with a frozen-lockfile, ignore-scripts install; the repo layout separates src/, public/, web/, plugin/, .codex/skills/, and test/. [@claim:clm_e3a8a49006992e4db110e307cbfb667e330f9c9142a4e99653a7803e5d1c30f2]
- The admin UI runs at pagecast.localhost:4173 with a separate preview/public origin on port 4174, and workspace metadata is stored in a local .pagecast/ directory. [@claim:clm_f0b0d1cfc5e38fb0870bb9ab3932614f2322b524bcc41a54077686b3a26bf80b]
<!-- rcw:end owner=source:src_39bca3d916f654e698593a5b2caffc62 block=evidence -->

## Researcher notes

