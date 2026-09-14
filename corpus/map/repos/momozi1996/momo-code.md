# momozi1996/momo-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6922581961d5 @ 870abd054af90a09

## Summary (orientation draft, not independently verified)

Selected evidence records: Model tiers ultra/standard/lite are selectable via --model with documented use cases (complex tasks, daily coding, quick low-latency tasks), and a `momo models` subcommand lists models, model info, and providers. The README describes an experience fast loop (/evolve) using a KEP protocol: observe session signals, distill tactics, select via Thompson sampling, inject into prompts, solidify stats, and promote high-confidence tactics to the fine-tune curriculum.

## Source coverage

Source coverage (partial): 6 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The README describes an experience fast loop (/evolve) using a KEP protocol: observe session signals, distill tactics, select via Thompson sampling, inject into prompts, solidify stats, and promote high-confidence tactics to the fine-tune curriculum. -- evidence: [README.md#L431-L436](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L431-L436), [README.md#L427-L427](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L427-L427)
  - [observation/documented] A weight slow loop (/fine-tune) is documented to improve model weights at hour-level timescales via signal mining, curriculum synthesis, Monte Carlo Graph Search, LoRA fine-tuning, and a ratchet gate for monotonic improvement. -- evidence: [README.md#L481-L485](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L481-L485), [README.md#L477-L477](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L477-L477)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use bun to install, typecheck, test, and build (bun install, bun typecheck, bun test, bun run build), with a GitHub Actions release workflow that checks for brand leakage, type-checks, builds, bumps version, and publishes to npm. -- evidence: [docs/build-release.md#L17-L18](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L17-L18), [docs/build-release.md#L39-L45](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L39-L45), [docs/build-release.md#L14-L14](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L14-L14), [docs/build-release.md#L24-L24](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L24-L24), [docs/build-release.md#L34-L37](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L34-L37), [docs/build-release.md#L11-L11](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/docs/build-release.md#L11-L11)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Model tiers ultra/standard/lite are selectable via --model with documented use cases (complex tasks, daily coding, quick low-latency tasks), and a `momo models` subcommand lists models, model info, and providers. -- evidence: [README.md#L191-L195](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L191-L195), [README.md#L400-L404](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L400-L404), [README.md#L168-L171](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L168-L171)
  - [observation/documented] A `momo serve` command exposes a local HTTP JSON API plus SSE live feed and a single-file dashboard, defaulting to 127.0.0.1:4097; non-loopback binding requires a --token with Bearer auth. -- evidence: [README.md#L376-L376](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L376-L376), [README.md#L360-L361](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L360-L361), [README.md#L368-L374](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L368-L374), [README.md#L363-L366](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L363-L366)
- memory-state (1 claim(s)):
  - [observation/documented] On first run the tool creates ~/.momo/ containing config (momo.jsonc), sessions, and experience/ with tactics records and a ledger.jsonl audit log; graph state persists to ~/.momo/graphs/<id>.json after each batch so runs survive restarts. -- evidence: [README.md#L269-L274](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L269-L274), [README.md#L177-L185](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L177-L185), [README.md#L175-L175](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L175-L175), [README.md#L464-L466](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L464-L466)
- orchestration (2 claim(s)):
  - [observation/documented] The /agent command decomposes tasks into child momo subagent processes run in parallel with a synthesizer merging results, bounded by env rails MOMO_RLM_MAX_DEPTH (3), MOMO_RLM_BUDGET (8), and MOMO_RLM_TIMEOUT_MS (300000). -- evidence: [README.md#L265-L265](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L265-L265), [README.md#L257-L259](https://github.com/momozi1996/momo-code/blob/6922581961d543850dda9309be7f1e26c77b90d5/README.md#L257-L259)
More evidence: [full detail](momo-code.detail.md)

Metadata and full claim list: [full detail](momo-code.detail.md)
Human notes ([notes](momo-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
