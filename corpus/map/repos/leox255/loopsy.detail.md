# leox255/loopsy -- full detail

[Back to orientation](loopsy.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/leox255/loopsy/73c1654762797ebeac252a875022256f5a15f822/1ed6aebb8112bb9a.json](../../../wiki/dossiers/leox255/loopsy/73c1654762797ebeac252a875022256f5a15f822/1ed6aebb8112bb9a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is a pnpm monorepo with packages for shared protocol types, mDNS discovery, a Fastify daemon, a Cloudflare Worker relay, a deploy-relay npx CLI, the loopsy CLI, an MCP server, a dashboard, and a Flutter mobile app. -- evidence: [README.md#L259-L271](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L259-L271) (`clm_082fb5b31269dcbddacc35cf9e72974486d72f93a293a063e22a61500756edcd`)

## design-choices (3 claim(s))

- [observation/documented] Phone control works by the daemon opening an outbound WebSocket to a Cloudflare Worker (Durable Object) that the phone also connects to; the Worker splices the two connections, requiring no port forwarding, public IP, or VPN. -- evidence: [README.md#L52-L52](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L52-L52), [README.md#L44-L50](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L44-L50) (`clm_47d4107dfde5c40e1fabdb13267b5f0d6c1f6ee6b7bbfdd9dd4a177f86e0492f`)
- [observation/documented] Security design includes HMAC-signed pair tokens, SHA-256 hashing of secrets at rest, bearer tokens carried in Sec-WebSocket-Protocol headers rather than query strings, and constant-time bearer comparison. -- evidence: [README.md#L54-L54](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L54-L54), [README.md#L211-L218](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L211-L218) (`clm_7ed2a853df3eaec0eaf7a08ea589d8face604ff2548673bd6e7d14920ee87c89`)
- [observation/documented] The daemon binds to 127.0.0.1 by default; LAN exposure for peer-to-peer is opt-in via `loopsy start --lan` or setting server.host to 0.0.0.0 in config. -- evidence: [README.md#L203-L203](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L203-L203), [README.md#L187-L187](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L187-L187) (`clm_3e1b96832e6506e7a62c205732b85f78cc5c21c2022cacc72feb660c4cc14547`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors build with pnpm install and pnpm build, and releases are tag-driven — pushing a v* tag publishes loopsy and @loopsy/deploy-relay to npm via OIDC Trusted Publisher with provenance attestations. -- evidence: [AGENTS.md#L376-L379](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/AGENTS.md#L376-L379), [README.md#L275-L282](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L275-L282), [README.md#L284-L284](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L284-L284) (`clm_6abd789d7c4143b4e0caaa939e5f35d6046a9126e0cd0ef2f815090bdba1d4df`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The loopsy CLI includes daemon lifecycle commands (init, start, stop, status, doctor, enable/disable), phone pairing and revocation, relay reconfiguration, log viewing, and API-key show/rotate commands. -- evidence: [README.md#L92-L97](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L92-L97), [README.md#L101-L109](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L101-L109), [README.md#L113-L117](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L113-L117) (`clm_963e359ee9cecdd0a6126206d6b8d4316b952e002d4e41c54a025c89f094dedf`)
- [observation/documented] When wired into an agent, the Loopsy MCP server exposes tools for peer listing, remote command execution, long-lived PTY sessions, file transfer, a shared key/value context store, messaging with ACKs, and read receipts. -- evidence: [README.md#L150-L162](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L150-L162) (`clm_58118e66b9cdd82cfe274b076ab84c4f2078146c0307351b4fd3fb416757e0a8`)

## memory-state (1 claim(s))

- [observation/documented] State lives under ~/.loopsy/ in config.yaml, context.json (key-value store), peers.json, logs/audit.jsonl, and relay.json; the messaging protocol stores inbox, outbox, and ack entries as context keys with TTLs. -- evidence: [README.md#L249-L255](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L249-L255), [README.md#L177-L181](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L177-L181), [AGENTS.md#L120-L124](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/AGENTS.md#L120-L124), [README.md#L247-L247](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L247-L247) (`clm_5b3b5433c2b48c40bfd491696a0965a9ad702eab4ddace943cb84072138d513e`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Per-session auto-approve lets a user opt in to skipping agent confirmation prompts; it defaults to off and enabling it the first time requires a macOS confirmation dialog (the user's password). -- evidence: [README.md#L199-L199](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L199-L199), [README.md#L58-L61](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L58-L61), [README.md#L197-L197](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L197-L197) (`clm_c020f1519a5e914fc2bece30e49ad0c67463d446fb129949d73266a50f681f14`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Self-hosting the relay uses the @loopsy/deploy-relay npx CLI, which runs wrangler deploy against the user's Cloudflare account; Workers free tier and SQLite-backed Durable Objects are stated to cover personal use. -- evidence: [README.md#L76-L76](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L76-L76), [README.md#L69-L74](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L69-L74), [README.md#L65-L67](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L65-L67) (`clm_4fe1ee2828a8dd54ffdc4835c4e6e7d7afec27ab134d46c6778a2f9865f72b90`)

## limitations (1 claim(s))

- [observation/documented] TLS terminates at the relay, so the relay operator can read and modify terminal traffic including passwords; end-to-end phone-daemon encryption is deferred to the v1.1 roadmap, and self-hosting is the recommended mitigation. -- evidence: [README.md#L30-L40](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L30-L40), [README.md#L195-L195](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L195-L195) (`clm_5f9ce24018cc75edd9deb13c9921776fbd31ff6592b58cd100a1138be9c84fb7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

