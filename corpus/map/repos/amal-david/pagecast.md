# amal-david/pagecast

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit aa48964e7ca3 @ 1679bbc806747467

## Summary (orientation draft, not independently verified)

Pagecast is a local-first publishing tool for agent-generated reports and small static web projects, supporting preview, publish, re-sync, rename, password protection, and URL revocation. Server-rendered apps needing a running backend are not supported; users must export static assets first.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Pagecast is a local-first publishing tool for agent-generated reports and small static web projects, supporting preview, publish, re-sync, rename, password protection, and URL revocation. -- evidence: [README.md#L14-L19](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L14-L19)
- components (2 claim(s)):
  - [observation/documented] Password protection and link expiry are enforced at the edge by a generated Cloudflare Pages Function covering every file of a multi-file report. -- evidence: [CHANGELOG.md#L202-L204](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/CHANGELOG.md#L202-L204), [README.md#L127-L131](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L127-L131)
  - [observation/documented] Optional analytics deploys a Cloudflare Worker plus D1 database showing views, anonymous uniques, and recent events; raw IPs are HMACed with a per-Home secret and detailed events expire after 30 days. -- evidence: [ARCHITECTURE.md#L84-L89](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L84-L89), [README.md#L111-L116](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L111-L116)
- design-choices (3 claim(s)):
  - [observation/documented] New unlisted links combine a memorable prefix with 128 bits of entropy; unlisted is a bearer capability, not authentication, while password protection is the access-control feature and short vanity slugs are intentionally public drops. -- evidence: [ARCHITECTURE.md#L100-L111](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L100-L111), [README.md#L93-L107](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L93-L107), [ARCHITECTURE.md#L16-L27](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L16-L27)
  - [observation/documented] Publishing is context-aware: repeating a publish in the same agent context (via --context-id, PAGECAST_CONTEXT_ID, CODEX_THREAD_ID, CLAUDE_SESSION_ID, or workspace fallback) updates the existing URL. -- evidence: [README.md#L93-L107](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L93-L107), [CHANGELOG.md#L47-L58](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/CHANGELOG.md#L47-L58)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: UI work uses pnpm 10 with a frozen-lockfile, ignore-scripts install; the repo layout separates src/, public/, web/, plugin/, .codex/skills/, and test/. -- evidence: [README.md#L302-L307](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L302-L307)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands such as publish (with --json, --expires, --new-link, --update, --password), pages deploy, pages deployments list/delete/prune, background, telemetry, and mcp. -- evidence: [README.md#L176-L185](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L176-L185), [README.md#L75-L75](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L75-L75), [README.md#L139-L143](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L139-L143), [README.md#L289-L290](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L289-L290), [README.md#L78-L78](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L78-L78), [README.md#L81-L82](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L81-L82), [README.md#L88-L89](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L88-L89)
  - [observation/documented] The admin UI runs at pagecast.localhost:4173 with a separate preview/public origin on port 4174, and workspace metadata is stored in a local .pagecast/ directory. -- evidence: [README.md#L31-L34](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L31-L34)
- memory-state (1 claim(s)):
  - [observation/documented] A user-level ~/.pagecast/home/ owns the managed Cloudflare target, publication registry, analytics config, operation journal, and exclusive lease; workspace .pagecast/ holds only identity and Home mappings. -- evidence: [ARCHITECTURE.md#L33-L40](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L33-L40), [README.md#L31-L34](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/README.md#L31-L34)
- orchestration (1 claim(s)):
  - [observation/documented] Cross-system managed mutations write durable intent before remote side effects, checkpoint remote success, and retry or compensate; incomplete reconciliation stays visible in an operation journal. -- evidence: [ARCHITECTURE.md#L42-L49](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L42-L49), [ARCHITECTURE.md#L66-L73](https://github.com/Amal-David/pagecast/blob/aa48964e7ca33c95a329fad0766d127bd0ef617b/ARCHITECTURE.md#L66-L73)
- tools-permissions (2 claim(s)):
More evidence: [full detail](pagecast.detail.md)

Metadata and full claim list: [full detail](pagecast.detail.md)
Human notes ([notes](pagecast.notes.md), never overwritten by build)

[Back to map index](../../index.md)
