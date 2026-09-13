# Operations

## Local development

```
uv run --python 3.12 --extra dev python -m pytest tests -q --basetemp=work/pt
uv run --python 3.12 python scripts/verify_vendor.py
uv run --python 3.12 python scripts/demo_synthetic.py --root work/demo-synthetic
```

`verify_vendor.py` recomputes the Git blob SHA-1 and SHA-256 of every file recorded in
`vendor-pin.json` and flags anything unexpected under `vendor/research-corpus-wiki/` (ignoring only
runtime caches). It must report `"ok": true` before any release; it is also the first step of both
GitHub workflows.

## GitHub automation

Two workflows, both pinning every action to a full commit SHA (see the comment on each `uses:`
line) rather than a floating tag:

- **`ci.yml`** — `pull_request` and `push` to `main`. Read-only (`permissions: contents: read`).
  Runs the offline test suite and the synthetic demo on Ubuntu and Windows. No writes, no
  `pull_request_target`.
- **`maintenance.yml`** — `schedule` (one fixed daily UTC cron; GitHub may delay or drop a
  scheduled run under load, so this is not a real-time poller), `workflow_dispatch` (manual), and
  `repository_dispatch` with `types: [research-completed]`. `permissions: contents: write` only.
  Serialized via a single `concurrency` group (`cancel-in-progress: false`) so runs queue instead
  of overlapping or clobbering each other. A 15-minute job timeout is the hard deployment ceiling
  that every cooperative `--max-seconds` budget stays under.

  Steps: verify vendor → (if `repository_dispatch`) ingest the event JSON from `$GITHUB_EVENT_PATH`
  → ingest queued `inbox/public/` files → bounded `maintain` → `build` → `audit` → commit+push only
  if `git diff --cached` is non-empty, using a normal (non-forced) push. **The event file is read by
  `map_agents` itself; nothing from the payload is ever substituted into a shell command or a
  workflow expression.** A failing `audit` or `maintain` step stops the job before any commit; on
  any failure, `corpus/state` (never `packets/`, `proposals/`, or `inbox/private/`) is uploaded as an
  artifact so the fair cursor and failure counts are inspectable without another run.

### `research-completed` payload

```json
{
  "event_type": "research-completed",
  "client_payload": {
    "project": "navy-yard",
    "origin": "research-completed",
    "urls": ["https://github.com/org-a/alpha"],
    "text": "optional free text also scanned for links"
  }
}
```

Send it with `gh api repos/OWNER/REPO/dispatches -f event_type=research-completed -f 'client_payload[project]=navy-yard' ...`
or the REST API directly. `project` is required; `origin` defaults to `research-completed`; at
least one of `urls`/`text` is required. GitHub itself bounds `client_payload` to 10 top-level keys
and 65,535 characters and `event_type` to 100 characters — `map_agents.automation` enforces its own
smaller limits (`MAX_URLS`, `MAX_URL_CHARS`, `MAX_TEXT_CHARS`) inside that envelope and rejects
anything outside its supported shape with `EventRejected` before any write. See
`samples/research-completed.json` for a runnable fixture (used by `tests/test_automation.py`).

## Bounded limits, in practice

Every `maintain`/`worker` limit is a finite ceiling, not a target — the CLI validates them
(`InvalidLimits`) as finite, non-negative, and typed before any stage runs. A small, deliberately
tight recipe, safe to run against any corpus:

```
uv run --python 3.12 python -m map_agents --root corpus maintain \
  --max-repos 2 --max-files 4 --max-bytes 60000 --catalog-entries 10 \
  --max-seconds 60 --net-bytes 500000 --net-requests 40
```

This requires real network access (it fetches the live `alltheagents.org` backing feed) and is
verified to enforce its own ceiling honestly: run against the actual feed, the tight
`--net-bytes 500000` example above hits `BudgetExceeded` on the feed fetch itself and reports
`status: degraded`, `stopped: network-budget` rather than silently truncating or fabricating a
partial catalog. Raise `--net-bytes` (the feed is bounded at 8,000,000 bytes server-side) for a
recipe that completes a catalog pass; for a guaranteed fully offline run of the equivalent
pipeline, use `scripts/demo_synthetic.py` instead. That is at most 2 repository attempts, 4 files and 60,000 bytes of snapshot per repository, 10
catalog feed entries, a 60-second cooperative deadline, and a 500,000-byte/40-request network
ceiling for the whole run. **These are storage/network byte ceilings, not model tokens.** A
too-large packet or worker envelope means "narrow the snapshot selection" (fewer files, an explicit
`--path`, a smaller `--max-bytes`), not "use a model with a bigger context window." The default
`worker_seconds` (180s) and `max_seconds` (600s) are themselves clamped to whatever time remains in
the cooperative deadline; individual kernel calls (`prepare`/`apply`) each carry their own 300-second
hard timeout regardless of the run's remaining budget.

`maintain` records per-repository failures in `failures[]` and still exits 0 — inspect `status`
(`quiescent` / `needs-distillation` / `degraded` / `stopped`) and `failures`/`stopped` yourself; a
zero exit code alone does not mean nothing went wrong. A repository that fails `max_failures`
consecutive times is parked (skipped) until `--retry-parked`; the fair cursor and parked/failure
counts persist in `state/` across runs specifically so one bad repository never starves the rest of
the rotation, and a shrinking budget or a since-removed path degrades to a `refresh-failed`,
old-snapshot-retained receipt rather than dropping evidence.

## Attribution and vendor integrity

`vendor/research-corpus-wiki/` is vendored unmodified, Apache-2.0 licensed, pinned to the commit
recorded in `vendor-pin.json` (`repository`, `commit`, and a per-file Git blob SHA-1 + SHA-256).
Its upstream PR 1 is reviewed with passing CI but intentionally left open — do not merge it here.
Run `scripts/verify_vendor.py` after any change that touches `vendor/` or before trusting a
checkout; CI runs it on every push and PR. See `docs/observatory-manifest.json` for this
workbench's registration under the Stargazer Observatory, and `vendor/research-corpus-wiki/LICENSE`
/ `THIRD_PARTY_NOTICES.md` for the dependency's own attribution.

## What is not yet connected

- No live model or provider SDK is configured. `worker` without a small agent or an explicitly
  configured trusted command only returns manual envelopes; nothing is distilled automatically.
- No live WhatsApp or other chat connector exists. Private leads only ever reach this workbench as
  files under `inbox/private/` that a human or agent places there deliberately.
- The full corpus campaign (researching and seeding a broad set of real agent repositories) is
  separate follow-on work; this build ships the pipeline and a small, clearly synthetic
  demonstration, not a populated map.
- Publication to GitHub, independent review of this code, and enabling the scheduled workflow on a
  live repository are coordinator-side steps that happen after this unit is accepted.
