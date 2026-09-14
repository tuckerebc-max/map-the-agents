# youssefvdel/qwengate -- full detail

[Back to orientation](qwengate.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/youssefvdel/qwengate/5220f7d3c50c2d9538ec3d6d393aed4f13369950/f54d993c12067f27.json](../../../wiki/dossiers/youssefvdel/qwengate/5220f7d3c50c2d9538ec3d6d393aed4f13369950/f54d993c12067f27.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The architecture comprises an API layer (Hono, src/routes/), a Session Pool Manager (src/services/sessionPool.ts with SessionPool, Session, and AccountManager classes), a Qwen API transport layer, a configuration service, and a dashboard frontend. -- evidence: [docs/ARCHITECTURE.md#L143-L143](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L143-L143), [docs/ARCHITECTURE.md#L137-L139](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L137-L139), [docs/ARCHITECTURE.md#L102-L102](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L102-L102), [docs/ARCHITECTURE.md#L187-L187](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L187-L187), [docs/ARCHITECTURE.md#L166-L166](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L166-L166), [docs/ARCHITECTURE.md#L185-L185](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L185-L185), [docs/ARCHITECTURE.md#L123-L123](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L123-L123), [docs/ARCHITECTURE.md#L108-L111](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L108-L111) (`clm_d781ab921c1f10a9b1ef5d1962f2e8cc901d9cb3dfad0dc24d3e6b0c9bd5c575`)

## design-choices (5 claim(s))

- [observation/documented] A dual-transport design uses Node.js fetch via wreq-js (with TLS fingerprinting) for API calls and reserves Playwright browser automation only for login/auth and initial header extraction. -- evidence: [docs/ARCHITECTURE.md#L145-L145](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L145-L145), [docs/ARCHITECTURE.md#L157-L160](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L157-L160), [docs/ARCHITECTURE.md#L149-L153](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L149-L153) (`clm_5fef9a8fea1659b3d876687b845697d7f5e46eb84f2a1504eeb69e00b56aaf41`)
- [observation/documented] A content-filter pipeline (cleanTextOfXmlArtifacts, filterContent, cleanThinkTags) strips thinking tags and XML artifacts from streamed output, with per-chunk and flush paths plus an amplification guard. -- evidence: [docs/ARCHITECTURE.md#L372-L372](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L372-L372), [docs/ARCHITECTURE.md#L358-L366](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L358-L366), [docs/ARCHITECTURE.md#L382-L382](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L382-L382), [docs/ARCHITECTURE.md#L330-L330](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L330-L330) (`clm_96bd7115dc93855d6278f8d28a63ef4e070d216aca3855267bfdbb6ac49988b1`)
- [observation/documented] Tool call content is gated during streaming via a toolCallDepth counter that suppresses emission inside XML tool-call blocks, delivering the clean tool call as a finish_reason: tool_calls phase. -- evidence: [docs/ARCHITECTURE.md#L378-L378](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L378-L378), [docs/API.md#L567-L567](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L567-L567) (`clm_f88084d2baff02f00726a4855dc9bbfd432e8c16aa0f26e437a3e491ec3edf9b`)
- [observation/documented] Configuration follows a three-tier priority: environment variables highest, then config.json, then defaults, with runtime updates and hot reload supported via a centralized config service. -- evidence: [docs/ARCHITECTURE.md#L178-L181](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L178-L181), [docs/ARCHITECTURE.md#L172-L174](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L172-L174), [docs/ARCHITECTURE.md#L168-L168](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L168-L168) (`clm_c199f8554a6ff4bd1589619f34c8632abc1f85a7bc196b00729667f1d267ba59`)
- [observation/documented] Large context payloads are auto-uploaded as Qwen file attachments, and tool results such as git diffs and JSON arrays are compressed before being sent to the model to reduce token usage. -- evidence: [docs/API.md#L571-L571](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L571-L571), [README.md#L29-L40](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L29-L40), [docs/ARCHITECTURE.md#L149-L153](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L149-L153) (`clm_f9f959f77b73d54da9994773c4ad87ec37f3b90bfd414b30fe7c05d34b95717a`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: installation is via an install.sh one-liner (or install.ps1 on Windows) that clones the repo, installs dependencies with bun install, creates config.json, and symlinks the qg/qwengate/qwen-gate CLI commands. -- evidence: [README.md#L72-L76](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L72-L76), [README.md#L46-L48](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L46-L48), [README.md#L62-L66](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L62-L66), [README.md#L56-L58](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L56-L58), [README.md#L50-L50](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L50-L50) (`clm_163617555a96260058194c1e6591e5bc8ada22510ff828b8d6b3c4f57848f7fc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The product exposes OpenAI-compatible endpoints POST /v1/chat/completions and GET /v1/models at base URL http://localhost:26405/v1, documented as working with OpenAI SDKs and HTTP clients. -- evidence: [docs/API.md#L7-L15](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L7-L15), [docs/API.md#L53-L53](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L53-L53), [docs/API.md#L286-L286](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L286-L286), [docs/API.md#L19-L21](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L19-L21), [docs/API.md#L480-L483](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L480-L483), [docs/API.md#L543-L550](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L543-L550) (`clm_9d950b7126123044d15cfbbab0f6ed8c9cb1458ba273b3e49ce4c257fd086c3e`)
- [observation/documented] Chat completions accept model, messages, stream (default true), temperature, max_tokens, top_p, tools, tool_choice, and stream_options with include_usage for usage data in the final chunk. -- evidence: [docs/API.md#L64-L74](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L64-L74) (`clm_e20abae88fae20a9eb0f940d9f1adacf7409fc9d420e3f35b1b73769dbf87480`)
- [observation/documented] Streaming responses use SSE with an initial heartbeat, OpenAI-format chunks, optional reasoning_content deltas for thinking models, and a data: [DONE] terminator; usage appears in the final chunk when requested. -- evidence: [docs/API.md#L125-L125](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L125-L125), [docs/API.md#L120-L120](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L120-L120), [docs/API.md#L122-L123](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L122-L123), [docs/API.md#L109-L109](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L109-L109), [docs/API.md#L127-L129](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L127-L129) (`clm_c2003f50adea8886875d8e218602a08f4d9bae63ba63996f0f93370a401e46ab`)
- [observation/documented] A built-in dashboard serves vanilla HTML/JS pages at /dashboard, /dashboard/logs, /dashboard/accounts, /dashboard/network, and /dashboard/settings, with live SSE updates at /log/stream and JSON logs at /log/json. -- evidence: [docs/API.md#L347-L354](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L347-L354), [docs/API.md#L345-L345](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L345-L345), [docs/API.md#L360-L363](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L360-L363) (`clm_04f6323a9d373ceacd037d1cb3d374f87b1e9039237a88675cc2e7092b99cd11`)
- [observation/documented] API requests authenticate with an Authorization: Bearer header carrying an API key configured in .env or config.json; leaving API_KEY empty disables authentication. -- evidence: [docs/API.md#L33-L33](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L33-L33), [docs/API.md#L39-L39](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L39-L39), [docs/API.md#L29-L31](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L29-L31), [docs/API.md#L57-L60](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L57-L60), [docs/API.md#L27-L27](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L27-L27) (`clm_f1f3d12802ca6b66a7c0b30c4f3e4ae695990f3cf3e086089527785f3c746be6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Multiple Qwen accounts are rotated round-robin with automatic failover, health-weighted load balancing, rate-limit tracking, and a configurable cooldown (default 2 minutes via RATE_LIMIT_COOLDOWN_MS); sessions are pooled, reused, auto-scaled, and idle-cleaned. -- evidence: [docs/ARCHITECTURE.md#L321-L324](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L321-L324), [docs/API.md#L575-L575](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L575-L575), [docs/API.md#L45-L47](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L45-L47), [docs/ARCHITECTURE.md#L129-L133](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L129-L133) (`clm_af7ff1c591f5c1fdfbf13cdef200f9519480427c2296d09e0322194db337484f`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The documented stack is Bun 1.3+, TypeScript, Hono, wreq-js for HTTP with TLS fingerprinting, Playwright for login/auth only, and tsx; the frontend is vanilla HTML/CSS/JS with no framework dependencies. -- evidence: [docs/ARCHITECTURE.md#L388-L395](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L388-L395), [docs/ARCHITECTURE.md#L399-L403](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/ARCHITECTURE.md#L399-L403), [docs/API.md#L345-L345](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/docs/API.md#L345-L345) (`clm_c399c6e0f7986563cb0691de293ac8e81793039852b2a9af09250d057f4d79ad`)

## limitations (1 claim(s))

- [observation/documented] The project is explicitly for educational and study purposes, is not affiliated with Alibaba Group or Qwen, and requires users to comply with chat.qwen.ai's terms of service. -- evidence: [README.md#L13-L13](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L13-L13) (`clm_aa2446ec3bc7bcff854c4788a83ea46705ae7f41d10e57e1d4b687fab61d6c16`)

## relevance (1 claim(s))

- [observation/documented] The tool targets users of OpenAI-compatible coding clients (Claude Code, OpenCode, Qwen Code, Cursor) who want to route requests to Qwen models through a local proxy without per-token payment. -- evidence: [README.md#L29-L40](https://github.com/youssefvdel/qwengate/blob/5220f7d3c50c2d9538ec3d6d393aed4f13369950/README.md#L29-L40) (`clm_23c8d81af6d8accbb9bbda3c4cd27cb4585549207accb1f10ad3608b04133971`)

