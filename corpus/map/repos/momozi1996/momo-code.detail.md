# momozi1996/momo-code -- full detail

[Back to orientation](momo-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/momozi1996/momo-code/6922581961d543850dda9309be7f1e26c77b90d5/870abd054af90a09.json](../../../wiki/dossiers/momozi1996/momo-code/6922581961d543850dda9309be7f1e26c77b90d5/870abd054af90a09.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The README describes an experience fast loop (/evolve) using a KEP protocol: observe session signals, distill tactics, select via Thompson sampling, inject into prompts, solidify stats, and promote high-confidence tactics to the fine-tune curriculum. -- evidence: [README.md#L431-L436](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L431-L436), [README.md#L427-L427](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L427-L427) (`clm_0f0c61c13a67061253c8049431529122170ac90bd9c359da43e9e28855347741`)
- [observation/documented] A weight slow loop (/fine-tune) is documented to improve model weights at hour-level timescales via signal mining, curriculum synthesis, Monte Carlo Graph Search, LoRA fine-tuning, and a ratchet gate for monotonic improvement. -- evidence: [README.md#L481-L485](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L481-L485), [README.md#L477-L477](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L477-L477) (`clm_91557e6776df095f30d2ba63f69d540eabbc4d9ae4ed754f66a2cf179929f204`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors use bun to install, typecheck, test, and build (bun install, bun typecheck, bun test, bun run build), with a GitHub Actions release workflow that checks for brand leakage, type-checks, builds, bumps version, and publishes to npm. -- evidence: [docs/build-release.md#L17-L18](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L17-L18), [docs/build-release.md#L39-L45](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L39-L45), [docs/build-release.md#L14-L14](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L14-L14), [docs/build-release.md#L24-L24](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L24-L24), [docs/build-release.md#L34-L37](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L34-L37), [docs/build-release.md#L11-L11](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L11-L11) (`clm_3fc40634539b3161ef6a24d8e9cecdfcf0051ed61aa803c2e7efc483b028a156`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Model tiers ultra/standard/lite are selectable via --model with documented use cases (complex tasks, daily coding, quick low-latency tasks), and a `momo models` subcommand lists models, model info, and providers. -- evidence: [README.md#L191-L195](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L191-L195), [README.md#L400-L404](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L400-L404), [README.md#L168-L171](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L168-L171) (`clm_92117918843caf4b21cc6b602294bdffba998d8c2afd2ab0ad3a592403079fdf`)
- [observation/documented] A `momo serve` command exposes a local HTTP JSON API plus SSE live feed and a single-file dashboard, defaulting to 127.0.0.1:4097; non-loopback binding requires a --token with Bearer auth. -- evidence: [README.md#L376-L376](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L376-L376), [README.md#L360-L361](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L360-L361), [README.md#L368-L374](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L368-L374), [README.md#L363-L366](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L363-L366) (`clm_636ce741eaae905a70798e6da1a77b051d314c48352098915229985fd20889f5`)

## memory-state (1 claim(s))

- [observation/documented] On first run the tool creates ~/.momo/ containing config (momo.jsonc), sessions, and experience/ with tactics records and a ledger.jsonl audit log; graph state persists to ~/.momo/graphs/<id>.json after each batch so runs survive restarts. -- evidence: [README.md#L269-L274](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L269-L274), [README.md#L177-L185](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L177-L185), [README.md#L175-L175](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L175-L175), [README.md#L464-L466](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L464-L466) (`clm_86e5a6dd80f74dae7c8ca679ff663df4840dc84dcd5efc102fb1c83e226d054c`)

## orchestration (2 claim(s))

- [observation/documented] The /agent command decomposes tasks into child momo subagent processes run in parallel with a synthesizer merging results, bounded by env rails MOMO_RLM_MAX_DEPTH (3), MOMO_RLM_BUDGET (8), and MOMO_RLM_TIMEOUT_MS (300000). -- evidence: [README.md#L265-L265](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L265-L265), [README.md#L257-L259](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L257-L259) (`clm_03f6ee3cb3216d76e21e79fc386b899aab1ca17a9e25b3f6fd38c04e9683e26d`)
- [observation/documented] The /graph command plans a directed acyclic graph of subagent tasks, runs nodes in parallel per topological level with retries and downstream dependency outputs, supports resume/status/list, and can mark nodes as simulation agents driving the Genesis world via /sim. -- evidence: [README.md#L283-L285](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L283-L285), [README.md#L269-L274](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L269-L274), [README.md#L276-L281](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L276-L281) (`clm_f7255d40d6ab206af355d2742af583fe5f591c86b70533defbd9722e61445080`)

## tools-permissions (1 claim(s))

- [observation/documented] The /refine command reviews session trajectories and proposes tactic or prompt-patch improvements, and nothing is applied without explicit human approval via approve/apply review-gate subcommands. -- evidence: [README.md#L246-L253](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L246-L253), [README.md#L243-L244](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L243-L244) (`clm_ecf49c6fe076b578689ec5bef16e653457d1d0f10ecbcef0a3c208bdec4cf70b`)

## evaluation (1 claim(s))

- [observation/documented] The product includes task-level evaluation features: `momo /sim eval --tasks=tasks.json` runs batch evaluation with a fresh world per episode, and /optim studies score configurations via a --cmd metric from stdout or --sim Genesis experiments. -- evidence: [README.md#L311-L319](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L311-L319), [README.md#L351-L354](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L351-L354) (`clm_1d0be991eb85aa51a36239d001c41c71a81a197c4511d1c57bd6eb1dbb22ef8c`)

## dependencies (1 claim(s))

- [observation/documented] Runtime prerequisites are macOS or Linux (Windows via WSL), Node.js >= 20, git, and curl; the /sim feature additionally requires Python with genesis-world installed, and /voice requires sounddevice and scipy plus an OpenAI-compatible speech-to-text endpoint. -- evidence: [README.md#L86-L88](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L86-L88), [README.md#L307-L309](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L307-L309), [README.md#L380-L381](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L380-L381) (`clm_f99b53b80156215ccaf5821524acac143920045a548ff550f4055c14fefc51fe`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

