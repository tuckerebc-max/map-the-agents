# lidge-jun/opencodex

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9f7397ed1582 @ 37d187e8e70b0f0a

## Summary (orientation draft, not independently verified)

opencodex is a local proxy (npm package, Node 18+, Bun runtime bundled) that translates Codex's Responses API to many LLM providers, with a CLI (`ocx`), web dashboard, ChatGPT account pooling, and Codex model-catalog integration. Evidence is mostly README/docs documentation; no code inspection and no agent-performance evaluation evidence is present. Evidence coverage: 135 of 213 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 42 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Integration with Codex works by writing Codex-native config and catalog files under CODEX_HOME (config.toml, opencodex.config.toml, opencodex-catalog.json, models_cache.json), so routed models appear in Codex's picker without patching Codex itself. -- evidence: [docs/codex-app-model-catalog.md#L19-L22](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L19-L22), [docs/codex-app-model-catalog.md#L16-L17](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L16-L17), [docs/codex-app-model-catalog.md#L11-L12](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L11-L12), [docs/codex-app-model-catalog.md#L24-L25](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L24-L25)
- design-choices (1 claim(s)):
  - [observation/documented] By default the proxy binds to 127.0.0.1 without authentication; binding beyond loopback requires OPENCODEX_API_AUTH_TOKEN, which every client request must carry as the `x-opencodex-api-key` header. -- evidence: [README.md#L355-L358](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L355-L358)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: source development requires the bun CLI on PATH (separate from the bundled runtime), and contributors run `bun install`, `bun run typecheck`, and `bun run test`; contributor setup lives in CONTRIBUTING.md. -- evidence: [README.md#L380-L386](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L380-L386), [README.md#L388-L388](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L388-L388), [README.md#L377-L378](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L377-L378)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes a CLI including `ocx init`, `start`, `stop`, `service`, `codex-shim install`, `health`, `ready`, `status`, `gui`, plus subcommands for providers, accounts, combos, and v2 surface controls. -- evidence: [README.md#L299-L314](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L299-L314)
  - [observation/documented] The proxy serves `GET /healthz` for liveness and an unauthenticated `GET /readyz` returning a sanitized JSON identity; ready returns 200 while pending/failed return 503 with Retry-After: 1. -- evidence: [README.md#L321-L324](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L321-L324)
- memory-state (1 claim(s)):
  - [observation/documented] The runtime tracks 36 categories of retained process state: 12 byte-accounted stores evicted under a default 256 MiB budget, 4 monitored buffers, 24 state-store registrations with 60s expiry sweeps, and LRU-capped memos; live bytes are inspectable via GET /api/system/memory with the admin token. -- evidence: [README.md#L269-L270](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L269-L270), [README.md#L254-L267](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L254-L267), [README.md#L252-L252](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L252-L252)
- orchestration (2 claim(s)):
  - [observation/documented] The proxy can manage a ChatGPT account pool for Codex auth: quota-aware routing sends new sessions to the lowest-usage healthy account under quota policy, while existing threads normally keep affinity to their starting account, with rebinding on failover, exclusion, affinity expiry, or 401/403/429 recovery. -- evidence: [README.md#L72-L77](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L72-L77), [README.md#L90-L100](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L90-L100)
  - [observation/documented] Combos provide a single virtual model id with failover or weighted round-robin across providers. -- evidence: [README.md#L225-L247](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L225-L247)
More evidence: [full detail](opencodex.detail.md)

Metadata and full claim list: [full detail](opencodex.detail.md)
Human notes ([notes](opencodex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
