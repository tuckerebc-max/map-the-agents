# youssefvdel/qwengate

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5220f7d3c50c @ f54d993c12067f27

## Summary (orientation draft, not independently verified)

Selected evidence records: The product exposes OpenAI-compatible endpoints POST /v1/chat/completions and GET /v1/models at base URL http://localhost:26405/v1, documented as working with OpenAI SDKs and HTTP clients. Chat completions accept model, messages, stream (default true), temperature, max_tokens, top_p, tools, tool_choice, and stream_options with include_usage for usage data in the final chunk.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The architecture comprises an API layer (Hono, src/routes/), a Session Pool Manager (src/services/sessionPool.ts with SessionPool, Session, and AccountManager classes), a Qwen API transport layer, a configuration service, and a dashboard frontend. -- evidence: [docs/ARCHITECTURE.md#L143-L143](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L143-L143), [docs/ARCHITECTURE.md#L137-L139](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L137-L139), [docs/ARCHITECTURE.md#L102-L102](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L102-L102), [docs/ARCHITECTURE.md#L187-L187](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L187-L187), [docs/ARCHITECTURE.md#L166-L166](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L166-L166), [docs/ARCHITECTURE.md#L185-L185](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L185-L185), [docs/ARCHITECTURE.md#L123-L123](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L123-L123), [docs/ARCHITECTURE.md#L108-L111](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L108-L111)
- design-choices (5 claim(s)):
  - [observation/documented] A dual-transport design uses Node.js fetch via wreq-js (with TLS fingerprinting) for API calls and reserves Playwright browser automation only for login/auth and initial header extraction. -- evidence: [docs/ARCHITECTURE.md#L145-L145](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L145-L145), [docs/ARCHITECTURE.md#L157-L160](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L157-L160), [docs/ARCHITECTURE.md#L149-L153](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L149-L153)
  - [observation/documented] A content-filter pipeline (cleanTextOfXmlArtifacts, filterContent, cleanThinkTags) strips thinking tags and XML artifacts from streamed output, with per-chunk and flush paths plus an amplification guard. -- evidence: [docs/ARCHITECTURE.md#L372-L372](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L372-L372), [docs/ARCHITECTURE.md#L358-L366](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L358-L366), [docs/ARCHITECTURE.md#L382-L382](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L382-L382), [docs/ARCHITECTURE.md#L330-L330](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L330-L330)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: installation is via an install.sh one-liner (or install.ps1 on Windows) that clones the repo, installs dependencies with bun install, creates config.json, and symlinks the qg/qwengate/qwen-gate CLI commands. -- evidence: [README.md#L72-L76](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L72-L76), [README.md#L46-L48](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L46-L48), [README.md#L62-L66](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L62-L66), [README.md#L56-L58](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L56-L58), [README.md#L50-L50](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L50-L50)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The product exposes OpenAI-compatible endpoints POST /v1/chat/completions and GET /v1/models at base URL http://localhost:26405/v1, documented as working with OpenAI SDKs and HTTP clients. -- evidence: [docs/API.md#L7-L15](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L7-L15), [docs/API.md#L53-L53](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L53-L53), [docs/API.md#L286-L286](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L286-L286), [docs/API.md#L19-L21](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L19-L21), [docs/API.md#L480-L483](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L480-L483), [docs/API.md#L543-L550](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L543-L550)
  - [observation/documented] Chat completions accept model, messages, stream (default true), temperature, max_tokens, top_p, tools, tool_choice, and stream_options with include_usage for usage data in the final chunk. -- evidence: [docs/API.md#L64-L74](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L64-L74)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Multiple Qwen accounts are rotated round-robin with automatic failover, health-weighted load balancing, rate-limit tracking, and a configurable cooldown (default 2 minutes via RATE_LIMIT_COOLDOWN_MS); sessions are pooled, reused, auto-scaled, and idle-cleaned. -- evidence: [docs/ARCHITECTURE.md#L321-L324](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L321-L324), [docs/API.md#L575-L575](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L575-L575), [docs/API.md#L45-L47](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L45-L47), [docs/ARCHITECTURE.md#L129-L133](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L129-L133)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](qwengate.detail.md)

Metadata and full claim list: [full detail](qwengate.detail.md)
Human notes ([notes](qwengate.notes.md), never overwritten by build)

[Back to map index](../../index.md)
