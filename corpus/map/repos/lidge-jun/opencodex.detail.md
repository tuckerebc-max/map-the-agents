# lidge-jun/opencodex -- full detail

[Back to orientation](opencodex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lidge-jun/opencodex/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/37d187e8e70b0f0a.json](../../../wiki/dossiers/lidge-jun/opencodex/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/37d187e8e70b0f0a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Integration with Codex works by writing Codex-native config and catalog files under CODEX_HOME (config.toml, opencodex.config.toml, opencodex-catalog.json, models_cache.json), so routed models appear in Codex's picker without patching Codex itself. -- evidence: [docs/codex-app-model-catalog.md#L19-L22](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L19-L22), [docs/codex-app-model-catalog.md#L16-L17](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L16-L17), [docs/codex-app-model-catalog.md#L11-L12](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L11-L12), [docs/codex-app-model-catalog.md#L24-L25](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/docs/codex-app-model-catalog.md#L24-L25) (`clm_702709e4a1e295802072691dd637512dd7591828f2785eb8c77794f8de98ffb7`)

## design-choices (1 claim(s))

- [observation/documented] By default the proxy binds to 127.0.0.1 without authentication; binding beyond loopback requires OPENCODEX_API_AUTH_TOKEN, which every client request must carry as the `x-opencodex-api-key` header. -- evidence: [README.md#L355-L358](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L355-L358) (`clm_8e15bb6a783e8b1e534381dc9458c5e65d563b6c43a9634ee2555f091ffffdd4`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: source development requires the bun CLI on PATH (separate from the bundled runtime), and contributors run `bun install`, `bun run typecheck`, and `bun run test`; contributor setup lives in CONTRIBUTING.md. -- evidence: [README.md#L380-L386](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L380-L386), [README.md#L388-L388](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L388-L388), [README.md#L377-L378](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L377-L378) (`clm_7cd40746fdc8c97761169b413aa712e807933bf95f18a882b3228b51084b9d72`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product exposes a CLI including `ocx init`, `start`, `stop`, `service`, `codex-shim install`, `health`, `ready`, `status`, `gui`, plus subcommands for providers, accounts, combos, and v2 surface controls. -- evidence: [README.md#L299-L314](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L299-L314) (`clm_3d487f157fa9c38f65f19c90f7d8b5624c9d8e739860fff0ed6459160dfe44da`)
- [observation/documented] The proxy serves `GET /healthz` for liveness and an unauthenticated `GET /readyz` returning a sanitized JSON identity; ready returns 200 while pending/failed return 503 with Retry-After: 1. -- evidence: [README.md#L321-L324](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L321-L324) (`clm_f191ab9b9bf78fe94c2d944c012709b165babae3cd0b3163c6e102e2c9493375`)
- [observation/documented] Models are targeted with a `provider/model` syntax (e.g. `codex -m "anthropic/claude-opus-5"`); omitting the prefix uses the default provider or name-pattern auto-matching, and inner slashes in provider model ids are aliased to `-`. -- evidence: [README.md#L284-L286](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L284-L286), [README.md#L278-L282](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L278-L282), [README.md#L276-L276](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L276-L276) (`clm_5e4e3312513e7689faceaf727c36469b390712f4042e6640005fdef7df813732`)

## memory-state (1 claim(s))

- [observation/documented] The runtime tracks 36 categories of retained process state: 12 byte-accounted stores evicted under a default 256 MiB budget, 4 monitored buffers, 24 state-store registrations with 60s expiry sweeps, and LRU-capped memos; live bytes are inspectable via GET /api/system/memory with the admin token. -- evidence: [README.md#L269-L270](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L269-L270), [README.md#L254-L267](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L254-L267), [README.md#L252-L252](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L252-L252) (`clm_ace621e3a99791d266c18fbe2e8437a97b2aa7bfda5e41018b2b6228ebbe9e43`)

## orchestration (2 claim(s))

- [observation/documented] The proxy can manage a ChatGPT account pool for Codex auth: quota-aware routing sends new sessions to the lowest-usage healthy account under quota policy, while existing threads normally keep affinity to their starting account, with rebinding on failover, exclusion, affinity expiry, or 401/403/429 recovery. -- evidence: [README.md#L72-L77](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L72-L77), [README.md#L90-L100](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L90-L100) (`clm_3f420b19841d6e0c6f7fa840ccfc05c25f8038b0cf85495c69bc5369fb7c9f1c`)
- [observation/documented] Combos provide a single virtual model id with failover or weighted round-robin across providers. -- evidence: [README.md#L225-L247](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L225-L247) (`clm_574a4a9d05c6adc6cee83da3237d13974a067c6eead44a672081af1c207e9bfd`)

## tools-permissions (1 claim(s))

- [observation/documented] The management API refuses agent-driven star requests with `403 agent_consent_required`, and the CLI suppresses the interactive star prompt when an agent is detected, leaving the decision to the user. -- evidence: [AGENTS_INSTALL.md#L29-L37](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/AGENTS_INSTALL.md#L29-L37), [README.md#L199-L202](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L199-L202) (`clm_4693d1cbb9ea8aaa67cc8aab0d05126d48132d4c15fb33e37ca2106285c5dab6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package requires Node 18+ and bundles the Bun runtime on npm install, so no separate Bun installation (or WSL on Windows) is needed; supported OSes are macOS, Linux, and Windows x64 with launchd, systemd user units, or Task Scheduler/WinSW respectively. -- evidence: [README.md#L214-L216](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L214-L216), [README.md#L208-L212](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L208-L212) (`clm_9f4a7a386e93bbe17d59a42945df75697074332dfb854400cce04978625fbc62`)

## limitations (1 claim(s))

- [observation/documented] The project warns it is community-maintained and unaffiliated with OpenAI or Anthropic, and that providers such as Anthropic may suspend accounts routing through third-party proxies, so use is at the user's own risk. -- evidence: [README.md#L398-L398](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L398-L398), [README.md#L396-L396](https://github.com/lidge-jun/opencodex/blob/9f7397ed1582d95c6c1fcf4ae9951213b3fa2d19/README.md#L396-L396) (`clm_e051d2f06c9c6681665a728e2c1e7938c74947be8a01a3bd78a219813f39afea`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

