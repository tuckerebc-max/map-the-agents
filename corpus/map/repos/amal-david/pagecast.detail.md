# amal-david/pagecast -- full detail

[Back to orientation](pagecast.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/amal-david/pagecast/aa48964e7ca33c95a329fad0766d127bd0ef617b/1679bbc806747467.json](../../../wiki/dossiers/amal-david/pagecast/aa48964e7ca33c95a329fad0766d127bd0ef617b/1679bbc806747467.json)

## specifications (1 claim(s))

- [observation/documented] Pagecast is a local-first publishing tool for agent-generated reports and small static web projects, supporting preview, publish, re-sync, rename, password protection, and URL revocation. -- evidence: [README.md#L14-L19](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L14-L19) (`clm_ba0959e46034531419d3207d1622a194b98a1f9946857322f615c6c267c5fd50`)

## components (2 claim(s))

- [observation/documented] Password protection and link expiry are enforced at the edge by a generated Cloudflare Pages Function covering every file of a multi-file report. -- evidence: [CHANGELOG.md#L202-L204](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/CHANGELOG.md#L202-L204), [README.md#L127-L131](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L127-L131) (`clm_e3398880db828075731712692441b5c282889e5608dcb3bbc68fcab3f5968c86`)
- [observation/documented] Optional analytics deploys a Cloudflare Worker plus D1 database showing views, anonymous uniques, and recent events; raw IPs are HMACed with a per-Home secret and detailed events expire after 30 days. -- evidence: [ARCHITECTURE.md#L84-L89](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L84-L89), [README.md#L111-L116](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L111-L116) (`clm_64e83370fdf4dab1cd06a1405bde61e11698f79bde41735c679819444c155e6e`)

## design-choices (3 claim(s))

- [observation/documented] New unlisted links combine a memorable prefix with 128 bits of entropy; unlisted is a bearer capability, not authentication, while password protection is the access-control feature and short vanity slugs are intentionally public drops. -- evidence: [ARCHITECTURE.md#L100-L111](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L100-L111), [README.md#L93-L107](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L93-L107), [ARCHITECTURE.md#L16-L27](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L16-L27) (`clm_73ded06d5466c3940b395905e7e1219f667e7ae68f3adbc86b763b783509db83`)
- [observation/documented] Publishing is context-aware: repeating a publish in the same agent context (via --context-id, PAGECAST_CONTEXT_ID, CODEX_THREAD_ID, CLAUDE_SESSION_ID, or workspace fallback) updates the existing URL. -- evidence: [README.md#L93-L107](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L93-L107), [CHANGELOG.md#L47-L58](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/CHANGELOG.md#L47-L58) (`clm_264eff79fb71f91930adb23b9a197f06d32ce1ef73b3efea4f670c1d673e955c`)
- [observation/documented] Telemetry is anonymous (command name, versions, OS/arch only), default-on for fresh interactive installs with a one-time disclosure, off in CI, and controllable via pagecast telemetry or DO_NOT_TRACK=1. -- evidence: [README.md#L283-L287](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L283-L287), [CHANGELOG.md#L62-L69](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/CHANGELOG.md#L62-L69) (`clm_e048163639735c0859eaa792c3e11de71dbc056ebec4db5b7eae9472bf9bc32e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: UI work uses pnpm 10 with a frozen-lockfile, ignore-scripts install; the repo layout separates src/, public/, web/, plugin/, .codex/skills/, and test/. -- evidence: [README.md#L302-L307](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L302-L307) (`clm_e3a8a49006992e4db110e307cbfb667e330f9c9142a4e99653a7803e5d1c30f2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands such as publish (with --json, --expires, --new-link, --update, --password), pages deploy, pages deployments list/delete/prune, background, telemetry, and mcp. -- evidence: [README.md#L176-L185](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L176-L185), [README.md#L75-L75](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L75-L75), [README.md#L139-L143](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L139-L143), [README.md#L289-L290](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L289-L290), [README.md#L78-L78](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L78-L78), [README.md#L81-L82](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L81-L82), [README.md#L88-L89](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L88-L89) (`clm_8e38dab30f96190e5faeadfbc3da58bd0df95eea8c4b2303bdcb41117417be43`)
- [observation/documented] The admin UI runs at pagecast.localhost:4173 with a separate preview/public origin on port 4174, and workspace metadata is stored in a local .pagecast/ directory. -- evidence: [README.md#L31-L34](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L31-L34) (`clm_f0b0d1cfc5e38fb0870bb9ab3932614f2322b524bcc41a54077686b3a26bf80b`)
- [observation/documented] Pagecast ships a publish-report agent skill installable via Skills.sh, a Claude Code plugin, and a Chrome extension (experimental, load-unpacked) adding a one-click publish button on file:/// HTML pages. -- evidence: [README.md#L160-L161](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L160-L161), [README.md#L248-L253](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L248-L253), [README.md#L246-L246](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L246-L246), [README.md#L157-L157](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L157-L157), [README.md#L151-L153](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L151-L153) (`clm_2bb3096e4c6aa9819d3e6e81ef84e616f76fd020a8ba63c5bfc90d562719bf76`)

## memory-state (1 claim(s))

- [observation/documented] A user-level ~/.pagecast/home/ owns the managed Cloudflare target, publication registry, analytics config, operation journal, and exclusive lease; workspace .pagecast/ holds only identity and Home mappings. -- evidence: [ARCHITECTURE.md#L33-L40](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L33-L40), [README.md#L31-L34](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L31-L34) (`clm_9a3b8265e207bfdfd82e32542c9e08f8bd6b3f8999c3fe06c8901fd7f19c06ea`)

## orchestration (1 claim(s))

- [observation/documented] Cross-system managed mutations write durable intent before remote side effects, checkpoint remote success, and retry or compensate; incomplete reconciliation stays visible in an operation journal. -- evidence: [ARCHITECTURE.md#L42-L49](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L42-L49), [ARCHITECTURE.md#L66-L73](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L66-L73) (`clm_41379d14674209083b678ced0e72c0744b2a85dbf605a76c8a69045abf00c80f`)

## tools-permissions (2 claim(s))

- [observation/documented] The MCP server exposes a bounded tool surface (status, list_pages, publish_content, publish_file, revoke_publication) with safety gates like confirm flags and asset-confirmation requirements; outputs are redacted by default. -- evidence: [README.md#L191-L197](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L191-L197) (`clm_c16786f28ada19e983817fe1ea5a635d442603910fff1e8ff39792f425582733`)
- [observation/documented] The admin API is loopback-only and separate from MCP; non-loopback binds are rejected, with an explicit wildcard exception only for the packaged loopback-mapped Docker proxy. -- evidence: [CHANGELOG.md#L75-L94](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/CHANGELOG.md#L75-L94), [README.md#L235-L242](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L235-L242), [README.md#L199-L204](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L199-L204), [ARCHITECTURE.md#L16-L27](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L16-L27) (`clm_c1e12176466c486a3e5c9a2eb3838b4deaca4620f87dc347a35c8bd96bcf508d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requires Node.js 20.19+ and a Cloudflare account for publishing; runs via npx with no global install. -- evidence: [README.md#L23-L23](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L23-L23), [README.md#L25-L27](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L25-L27) (`clm_9ee39afa30bc92e193796d0e11843f79532847316e4ed887a713e7312983b235`)
- [observation/documented] Wrangler is pinned at 4.86.0 in src/platform.js and baked into the Docker image so deploys do not contact npm at runtime; the root CLI/server has no runtime npm dependencies. -- evidence: [README.md#L235-L242](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L235-L242), [CHANGELOG.md#L98-L122](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/CHANGELOG.md#L98-L122), [README.md#L302-L307](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L302-L307) (`clm_0df49829d21c23d1879aa2b58c1e86c6ab12e7a5aa0fa3ec3c5ecc464654975e`)

## limitations (1 claim(s))

- [observation/documented] Server-rendered apps needing a running backend are not supported; users must export static assets first. -- evidence: [README.md#L14-L19](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L14-L19) (`clm_0b6bd81e60b894784b4cbdb5856aa18cf25ea9b8e2faa1623aaddefd9d529328`)

## relevance (1 claim(s))

- [observation/documented] Suited to sharing HTML reports, dashboards, Markdown docs, and built static dist/build/out folders via memorable Cloudflare Pages links, including from coding agents through skills, plugin, or MCP. -- evidence: [README.md#L172-L174](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L172-L174), [README.md#L14-L19](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L14-L19), [README.md#L151-L153](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L151-L153) (`clm_1acc0b6bad4d5297736e3b3b456a5c5f43cac28234689aab4186ed6e3babc385`)

