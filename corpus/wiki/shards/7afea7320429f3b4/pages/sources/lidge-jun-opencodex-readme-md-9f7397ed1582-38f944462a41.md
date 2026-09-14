---
access: public
aliases: []
claim_ids:
- clm_3d487f157fa9c38f65f19c90f7d8b5624c9d8e739860fff0ed6459160dfe44da
- clm_3f420b19841d6e0c6f7fa840ccfc05c25f8038b0cf85495c69bc5369fb7c9f1c
- clm_4693d1cbb9ea8aaa67cc8aab0d05126d48132d4c15fb33e37ca2106285c5dab6
- clm_574a4a9d05c6adc6cee83da3237d13974a067c6eead44a672081af1c207e9bfd
- clm_5e4e3312513e7689faceaf727c36469b390712f4042e6640005fdef7df813732
- clm_7cd40746fdc8c97761169b413aa712e807933bf95f18a882b3228b51084b9d72
- clm_8e15bb6a783e8b1e534381dc9458c5e65d563b6c43a9634ee2555f091ffffdd4
- clm_9f4a7a386e93bbe17d59a42945df75697074332dfb854400cce04978625fbc62
- clm_ace621e3a99791d266c18fbe2e8437a97b2aa7bfda5e41018b2b6228ebbe9e43
- clm_e051d2f06c9c6681665a728e2c1e7938c74947be8a01a3bd78a219813f39afea
- clm_f191ab9b9bf78fe94c2d944c012709b165babae3cd0b3163c6e102e2c9493375
maturity: draft
page_id: pg_4096a469f8a95d2cacf138f944462a41
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a158f48d66a65c32b7711029e4a77da5
title: lidge-jun/opencodex/README.md @ 9f7397ed1582
updated_at: '2026-09-14T04:06:51Z'
---

# lidge-jun/opencodex/README.md @ 9f7397ed1582

<!-- rcw:begin owner=source:src_a158f48d66a65c32b7711029e4a77da5 block=evidence -->
- The product exposes a CLI including `ocx init`, `start`, `stop`, `service`, `codex-shim install`, `health`, `ready`, `status`, `gui`, plus subcommands for providers, accounts, combos, and v2 surface controls. [@claim:clm_3d487f157fa9c38f65f19c90f7d8b5624c9d8e739860fff0ed6459160dfe44da]
- The proxy can manage a ChatGPT account pool for Codex auth: quota-aware routing sends new sessions to the lowest-usage healthy account under quota policy, while existing threads normally keep affinity to their starting account, with rebinding on failover, exclusion, affinity expiry, or 401/403/429 recovery. [@claim:clm_3f420b19841d6e0c6f7fa840ccfc05c25f8038b0cf85495c69bc5369fb7c9f1c]
- The management API refuses agent-driven star requests with `403 agent_consent_required`, and the CLI suppresses the interactive star prompt when an agent is detected, leaving the decision to the user. [@claim:clm_4693d1cbb9ea8aaa67cc8aab0d05126d48132d4c15fb33e37ca2106285c5dab6]
- Combos provide a single virtual model id with failover or weighted round-robin across providers. [@claim:clm_574a4a9d05c6adc6cee83da3237d13974a067c6eead44a672081af1c207e9bfd]
- Models are targeted with a `provider/model` syntax (e.g. `codex -m "anthropic/claude-opus-5"`); omitting the prefix uses the default provider or name-pattern auto-matching, and inner slashes in provider model ids are aliased to `-`. [@claim:clm_5e4e3312513e7689faceaf727c36469b390712f4042e6640005fdef7df813732]
- Repository development practice: source development requires the bun CLI on PATH (separate from the bundled runtime), and contributors run `bun install`, `bun run typecheck`, and `bun run test`; contributor setup lives in CONTRIBUTING.md. [@claim:clm_7cd40746fdc8c97761169b413aa712e807933bf95f18a882b3228b51084b9d72]
- By default the proxy binds to 127.0.0.1 without authentication; binding beyond loopback requires OPENCODEX_API_AUTH_TOKEN, which every client request must carry as the `x-opencodex-api-key` header. [@claim:clm_8e15bb6a783e8b1e534381dc9458c5e65d563b6c43a9634ee2555f091ffffdd4]
- The package requires Node 18+ and bundles the Bun runtime on npm install, so no separate Bun installation (or WSL on Windows) is needed; supported OSes are macOS, Linux, and Windows x64 with launchd, systemd user units, or Task Scheduler/WinSW respectively. [@claim:clm_9f4a7a386e93bbe17d59a42945df75697074332dfb854400cce04978625fbc62]
- The runtime tracks 36 categories of retained process state: 12 byte-accounted stores evicted under a default 256 MiB budget, 4 monitored buffers, 24 state-store registrations with 60s expiry sweeps, and LRU-capped memos; live bytes are inspectable via GET /api/system/memory with the admin token. [@claim:clm_ace621e3a99791d266c18fbe2e8437a97b2aa7bfda5e41018b2b6228ebbe9e43]
- The project warns it is community-maintained and unaffiliated with OpenAI or Anthropic, and that providers such as Anthropic may suspend accounts routing through third-party proxies, so use is at the user's own risk. [@claim:clm_e051d2f06c9c6681665a728e2c1e7938c74947be8a01a3bd78a219813f39afea]
- The proxy serves `GET /healthz` for liveness and an unauthenticated `GET /readyz` returning a sanitized JSON identity; ready returns 200 while pending/failed return 503 with Retry-After: 1. [@claim:clm_f191ab9b9bf78fe94c2d944c012709b165babae3cd0b3163c6e102e2c9493375]
<!-- rcw:end owner=source:src_a158f48d66a65c32b7711029e4a77da5 block=evidence -->

## Researcher notes

