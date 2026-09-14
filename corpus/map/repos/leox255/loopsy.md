# leox255/loopsy

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 73c165476279 @ 1ed6aebb8112bb9a

## Summary (orientation draft, not independently verified)

The loopsy CLI includes daemon lifecycle commands (init, start, stop, status, doctor, enable/disable), phone pairing and revocation, relay reconfiguration, log viewing, and API-key show/rotate commands. When wired into an agent, the Loopsy MCP server exposes tools for peer listing, remote command execution, long-lived PTY sessions, file transfer, a shared key/value context store, messaging with ACKs, and read receipts.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is a pnpm monorepo with packages for shared protocol types, mDNS discovery, a Fastify daemon, a Cloudflare Worker relay, a deploy-relay npx CLI, the loopsy CLI, an MCP server, a dashboard, and a Flutter mobile app. -- evidence: [README.md#L259-L271](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L259-L271)
- design-choices (3 claim(s)):
  - [observation/documented] Phone control works by the daemon opening an outbound WebSocket to a Cloudflare Worker (Durable Object) that the phone also connects to; the Worker splices the two connections, requiring no port forwarding, public IP, or VPN. -- evidence: [README.md#L52-L52](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L52-L52), [README.md#L44-L50](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L44-L50)
  - [observation/documented] Security design includes HMAC-signed pair tokens, SHA-256 hashing of secrets at rest, bearer tokens carried in Sec-WebSocket-Protocol headers rather than query strings, and constant-time bearer comparison. -- evidence: [README.md#L54-L54](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L54-L54), [README.md#L211-L218](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L211-L218)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors build with pnpm install and pnpm build, and releases are tag-driven — pushing a v* tag publishes loopsy and @loopsy/deploy-relay to npm via OIDC Trusted Publisher with provenance attestations. -- evidence: [AGENTS.md#L376-L379](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/AGENTS.md#L376-L379), [README.md#L275-L282](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L275-L282), [README.md#L284-L284](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L284-L284)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The loopsy CLI includes daemon lifecycle commands (init, start, stop, status, doctor, enable/disable), phone pairing and revocation, relay reconfiguration, log viewing, and API-key show/rotate commands. -- evidence: [README.md#L92-L97](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L92-L97), [README.md#L101-L109](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L101-L109), [README.md#L113-L117](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L113-L117)
  - [observation/documented] When wired into an agent, the Loopsy MCP server exposes tools for peer listing, remote command execution, long-lived PTY sessions, file transfer, a shared key/value context store, messaging with ACKs, and read receipts. -- evidence: [README.md#L150-L162](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L150-L162)
- memory-state (1 claim(s)):
  - [observation/documented] State lives under ~/.loopsy/ in config.yaml, context.json (key-value store), peers.json, logs/audit.jsonl, and relay.json; the messaging protocol stores inbox, outbox, and ack entries as context keys with TTLs. -- evidence: [README.md#L249-L255](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L249-L255), [README.md#L177-L181](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L177-L181), [AGENTS.md#L120-L124](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/AGENTS.md#L120-L124), [README.md#L247-L247](https://github.com/leox255/loopsy/blob/73c1654762797ebeac252a875022256f5a15f822/README.md#L247-L247)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](loopsy.detail.md)

Metadata and full claim list: [full detail](loopsy.detail.md)
Human notes ([notes](loopsy.notes.md), never overwritten by build)

[Back to map index](../../index.md)
