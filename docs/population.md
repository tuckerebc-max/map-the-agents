# Portable population execution path

Three repo-owned modules package the bounded population pipeline: `map_agents/populate.py`,
`map_agents/source_review.py`, and `map_agents/proposal_recovery.py`. `source_review`'s model
critique is a fresh, source-anchored assessment of one proposal against its own cited slices, not
proof of correctness; a separate commissioned-seat review assessed an early
pilot sample. Final release sampling is recorded with the release evidence. Source collection uses a
separate, per-repository network budget (`snapshot`/`maintain`, see
[operations](operations.md)) from the model/review budgets described below; the two are never
combined into one ceiling.

## Run

```sh
uv run --python 3.12 python -m map_agents.populate --root corpus --group work/group.json --receipts work/population --concurrency 4
```

After the desired groups finish, rebuild the Markdown views and audit the complete corpus:

```sh
uv run --python 3.12 python -m map_agents --root corpus build
uv run --python 3.12 python -m map_agents --root corpus audit --level pr
```

`current` means a dossier matches the latest locally collected snapshot. It does not mean
the upstream repository's live HEAD was checked during a lookup; refresh metadata and collect
new snapshots before decisions that depend on changes since collection. A current dossier can
still cover only part of that snapshot's candidate files.

`work/group.json` is a JSON list of 1..8 repository keys (`["owner/repo", ...]`) — plain data,
never executable configuration. `--receipts` is a directory for resumable per-repository job,
usage and review receipts; reuse the same directory across resumed runs of the same group.

Each repository moves through: `prepare` (real kernel packet + envelope) -> the optional trusted
`map_agents.lunaroute` GLM Flash adapter (requires `LUNAROUTE_API_KEY` already set in the
environment; the key is read from the environment only and never written to a receipt or file)
-> a fresh source review of the exact sealed proposal
(`map_agents.source_review.review_proposal`) -> canonical `wiki.apply`, only if that review's
verdict is `pass` and is bound by SHA-256 to the exact proposal about to be applied.

The optional `--quarantine-invalid-claims` flag retains individual claims that pass the existing
citation, contributor-context and quotation checks when other claims in a completed response fail.
Rejected positions and reasons remain in the usage receipt. The summary is rebuilt from whole
retained claims, and every retained claim and summary still needs a fresh source assessment.
An all-invalid response remains a failure. The default omits this flag and rejects the whole
response when any claim fails those checks.

## Recovery

`map_agents.populate` never silently retries a job it left in a completed-failure stage
(`model-failed`, `review-failed`) or an uncertain outcome (a timed-out or non-`drain_complete`
model call, or a reviewer left `status: running`) — those are held for explicit reconciliation.
Two bounded, one-round recovery operations are available, never invoked automatically:

```sh
uv run --python 3.12 python -m map_agents.proposal_recovery --root corpus --group work/group.json --receipts work/population --repair
uv run --python 3.12 python -m map_agents.proposal_recovery --root corpus --group work/group.json --receipts work/population --retain
```

- `--repair` sends one corrected request (with the prior claims and source-review feedback) for a
  completed `model-failed`/`review-failed` job, then a fresh source review of the corrected
  proposal. It refuses a job that isn't in one of those two stages, and refuses an uncertain
  provider outcome — no automatic retry.
- `--retain` is a recovery step **after a completed correction failure**, not a way to relabel a
  rejected claim as supported. It requires an already-completed source assessment exactly bound
  (by SHA-256) to the proposal being retained, quarantines every clause verdicted `revise` or
  `unsupported` into the receipt, rebuilds the summary only from retained claims, and always
  requires a **new** source review of the retained proposal before it can reach `apply`.

## Preserved gates

- One global corpus `workers.Lease` per operation (`population-batch`,
  `completed-source-correction`, `supported-observation-retention`): one writer at a time, plus at
  most 4 concurrent model (author) calls and, in its own later stage, at most 4 concurrent
  source-review (reviewer) calls -- both bounded by the same `--concurrency` (1..4).
- Groups of 1..8 distinct known repository keys.
- `prepare` uses the same pinned Research Corpus Wiki kernel and `apply` path as manual
  distillation (`wiki.prepare`/`wiki.apply`, unmodified); nothing here is a second write path.
  Every stored source's bytes are re-verified against their recorded SHA-256 and Git blob hash
  before a packet is prepared (`wiki.verify_snapshot`), and source text is evidence data only --
  no command, path or argument is ever derived from it.
- Proposals are validated against the exact sealed packet and persisted to disk before any
  `wiki.apply` call; `wiki.apply` itself reconciles a kernel receipt for an already-applied
  operation rather than re-applying.
- A source review must reach `status: reviewed`, `verdict: pass`, covering every claim and the
  summary exactly once, bound by SHA-256 to the exact canonical proposal about to be applied.
- No uncertain provider or reviewer call is ever retried automatically; only explicit `--repair`/
  `--retain` act on already-completed failures, and each only once. `--retain` always requires a
  fresh summary and a fresh claim-by-claim review of the retained proposal before it can reach
  `apply` -- it never reuses the review that rejected the original claims.
- Vendor and canonical kernel JSONL are never written directly — only through `wiki.apply`.

## Partitioning

`populate.batch()` requires the opt-in partitioned kernel layout: it reads `wiki.load_layout(root)`
and refuses to run at all unless it reports `partitioned`. Enable it once, before the corpus's
first `prepare` call, on a fresh corpus intended for `populate`:

```sh
uv run --python 3.12 python -m map_agents --root corpus wiki-layout --enable-partitioned
```

`populate` never runs that command itself and never forces the switch on an already-initialized
shared corpus -- the kernel's own `enable_partitioned` refuses if the shared kernel is already
initialized or any repository already has indexed dossier evidence (see
[operations](operations.md#opt-in-partitioned-wiki-layout)). Manual `worker`/`apply` calls are
unaffected by layout either way. **Current caveat:** an existing shared-layout corpus cannot be
switched to partitioned once it holds any distilled evidence, so `populate` cannot be used against
it without a fresh corpus or the same manual migration limits the kernel itself imposes; this is a
real constraint of the shipped code, not a documentation gap.

## Not included here

BSE (the batch/step-execution operator layer) is not a dependency of any of these three modules;
it remains an optional external orchestrator that may call `map_agents.populate` as a subprocess.
This document does not cover collection, snapshotting, or the adapter's own contract — see
[operations.md](operations.md) and the [map-the-agents skill](../skills/map-the-agents/SKILL.md)
for those.
