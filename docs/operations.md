# Operations

Run commands from the repository checkout. All corpus paths use `--root corpus`.

## Check a checkout

```sh
uv run --python 3.12 python -c "from pathlib import Path; Path('work').mkdir(exist_ok=True)"
uv run --python 3.12 --extra dev python -m pytest tests -q --basetemp=work/pt
uv run --python 3.12 python scripts/verify_vendor.py
uv run --python 3.12 python scripts/demo_synthetic.py --root work/demo-synthetic
```

Use a new or empty demo root. The demo refuses to remove existing data. It uses fabricated
repositories, two classes, actual kernel writes and a rejected unsupported proposal; its
output must stay separate from the live corpus. The vendor verifier checks all 72 recorded
Git blob and SHA-256 identities against [the pin](../vendor-pin.json).

## GitHub maintenance

[CI](../.github/workflows/ci.yml) runs offline tests, vendor verification and the synthetic
demo on Ubuntu and Windows for pushes to main and pull requests, with read-only permissions.

[Maintenance](../.github/workflows/maintenance.yml) runs daily at 09:17 UTC, by manual dispatch,
on `research-completed` repository dispatch, and on main-branch pushes under
`corpus/inbox/public/**`. Schedules can be delayed or dropped by GitHub. The writer checks out
main, serializes runs, has only contents write permission, and has a 15-minute job ceiling.
Its token is used for public GitHub API requests; source and payload text never become commands.

The trusted [runner](../scripts/run_maintenance.py) reads a dispatch event from GitHub's event
file, ingests the public inbox, refreshes at most five repositories and 50 catalog entries,
captures at most 25 directory site pages under a separate finite budget (`directory.capture`,
resumable, honest backlog/failure counts), builds the map and audits the wiki. Repository refresh
has a 420-second metadata deadline (reserving headroom under the job's 15-minute ceiling for the
directory step, build and audit), with default 12 MB/120-request aggregate network ceilings for
refresh and a separate ~4 MB/60-second ceiling for directory capture, plus 12 files/400 KB per
snapshot. A missing backing-feed commit (no `catalog` run has ever succeeded yet) is an honest,
non-fatal skip for the directory step, recorded in the summary; a tampered/corrupt directory cache
is not swallowed and blocks publication like any other integrity failure.

After a successful capture, `directory.ingest_new_leads` sends any newly resolved, normalized
public repository key (from published/page-only entries with no backing-feed counterpart, and not
already tracked directly or through a verified alias) into the same canonical intake as a manual
`intake` call, up to 50 per run, reporting `deferred` honestly when there are more. This is
automatic ingestion into the metadata queue only -- new leads land as `discovered` and wait for the
existing bounded snapshot/distillation path; it does not itself run a worker or any model call, and
an optional model worker still requires its own separately configured execution.

The audit stage is `full` (every initialized kernel, shared or partitioned) unless the wiki module
exposes an optional `repos=` filter and the corpus uses the opt-in partitioned layout, in which case
it audits only the partitions for repositories this run actually changed (`audit_scope: "scoped"` in
the summary) -- a narrower, cheaper check meant only for frequent hosted runs. `maps.build` always
independently byte-verifies and structurally validates every dossier regardless of audit scope, and
either check failing blocks publication. Releases and any full-corpus review still require a full,
unscoped `audit` run; do not treat a scoped hosted pass as a substitute.

Fatal receive/build/audit errors prevent publication. Valid partial refreshes publish their
fair cursor, failure counts and retained older evidence, then report a failing partial run.
This prevents one inaccessible repository from forcing every future run to restart at it.
The workflow stages only the named data directories, queue files and the two directory-layer
state files (`corpus/state/directory-cursor.json`, `corpus/state/directory-published.json`),
pushes normally to main, and retains a summary and narrow state artifacts for 14 days. Inspect
those artifacts after a partial run. A concurrent main change may reject the push; retry from the
new main normally.

GitHub token pushes do not trigger another push CI run. Maintenance therefore validates its own
generated data before committing. Actions are pinned to full commits; see their version comments.

## Research and inbox intake

Every researched public GitHub candidate should reach intake, including candidates omitted from
a final top-ten recommendation. Project tags retain the research context alongside the shared map.

```sh
uv run --python 3.12 python -m map_agents --root corpus intake --file work/research-links.md --origin research --project navy-yard
uv run --python 3.12 python -m map_agents --root corpus inbox --lane private --max-files 20
gh api repos/tuckerebc-max/map-the-agents/dispatches --input samples/research-dispatch.json
```

The first command needs a supplied research file. Inbox paths have exactly this shape:
`corpus/inbox/<public|private>/<project>/<origin>.md` (also `.txt` or `.json`). Public files
may be committed; private exports stay local and ignored. Use neutral tags because tags persist.
Only normalized public links and associations enter canonical intake; raw conversations do not.
Per-lane digests and persistent cursors bound each call and avoid starvation by unchanged files.
Files are read at most the byte limit plus one and linked directories are rejected or skipped.

[research-dispatch.json](../samples/research-dispatch.json) is a runnable API request body using
a real public repository. GitHub delivers `event_type` as `action` in its event file. The separate
[research-completed.json](../samples/research-completed.json) is a synthetic received-event test
fixture. The receiver allows up to 200 URLs and a 200 KB event file; unsupported payloads are data
errors. Research producers must invoke this contract. No global hook or live chat connector is installed.

## Bounded collection and model work

```sh
uv run --python 3.12 python -m map_agents --root corpus maintain --max-repos 2 --max-files 4 --max-bytes 60000 --catalog-entries 10 --max-seconds 60 --net-bytes 5000000 --net-requests 40
```

These are byte and attempt ceilings, not model token counts or completion guarantees. The backing
feed itself must fit the aggregate allowance. Default collection reads README/docs; inspect selected
code only through explicit `snapshot --path` requests. A reduced budget or removed explicit path
retains old valid evidence and reports the gap. `--max-seconds` is cooperative: no new stage starts
past its deadline. Model/network waits are clamped, each kernel call has a 300-second timeout, and
local map building has no hard time kill. Use the outer job timeout for a hard deployment ceiling.

Inspect `maintain` JSON: status may be `quiescent`, `needs-distillation`, `degraded` or `stopped` even
when the CLI returns zero. Repeatedly failed repositories park after three consecutive failures;
`--retry-parked` explicitly retries them. There is no automatic timed backoff or model provider setup.
See the [skill](../skills/map-the-agents/SKILL.md) for bounded worker and proposal instructions.

## Optional LunaRoute GLM Flash worker adapter

[`map_agents/lunaroute.py`](../map_agents/lunaroute.py) is an optional trusted argv for `worker`.
It reads one worker envelope on stdin, calls LunaRoute's `https://gw.lunaroute.com/v1/chat/completions`
with the `LUNAROUTE_API_KEY` environment variable (never passed on argv), and writes exactly one
dossier proposal on stdout:

```sh
uv run --python 3.12 python -m map_agents --root corpus worker --repo openai/codex \
  -- uv run --python 3.12 python -m map_agents.lunaroute --model glm-5.3-flash --timeout-seconds 120 --max-output-tokens 5000
```

Only `glm-5.3-flash` and `glm-5.3-flash-background` are allowed; no Gemini model is served by this
endpoint. The model replies with a reduced `{summary, claims}` object that cites evidence slices by
integer index (not the full slice ID) to keep the prompt and reply short; the adapter resolves those
indices back to the packet's real slice IDs and binding fields (`operation_id`, `repo`, `commit`,
`snapshot_id`, `base_digest`) before emitting the exact proposal schema. Slice text is untrusted
evidence, never instructions. Every request sends `reasoning_effort: "low"`; the default costly
reasoning otherwise burns the whole `--max-output-tokens` budget on hidden reasoning and returns
no JSON. A response that is truncated (`finish_reason: "length"`) is refused before it is even
parsed, whether or not the truncated text happens to look like valid JSON.

The adapter preflights every claim against the pinned kernel's own `RCW_QUOTE_LIMIT` check
(`vendor/research-corpus-wiki/scripts/rcw_core/knowledge.py:check_reproduction`, never modified or
weakened here) before ever emitting a proposal: no claim may copy more than 20 consecutive words
verbatim from a cited slice. It also rejects a claim whose cited slices are *all* contributor
instruction files (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, any nesting depth, case-insensitive,
`.markdown` too) unless its facet is exactly `workflows` and its text starts exactly `Repository
development practice:` -- a prefix alone never excuses a false runtime facet. A claim mixing one
contributor-file citation with real product/code evidence is not subject to this rule. If the first
response is a completed (HTTP 200, not length-truncated) but unusable reply -- an over-quotation, a
contributor-gate violation, or a malformed/unsupported shape -- the adapter sends exactly one
correction request with the same evidence plus the exact validation problems, and uses that
corrected reply if and only if it also passes; otherwise it fails. A provider timeout, non-200
status, or truncated response is never retried and never gets a correction call. Both attempts'
usage and status are kept in the receipt.

Prompt slice selection prioritizes README and other product/runtime evidence over contributor-
instruction files, so a budget-forced omission drops contributor files first. `--usage-file PATH`
writes a local receipt (model, per-attempt status/finish_reason/timing/usage, and the exact
packet-vs-shown slice counts) that never contains source text or the key, and nothing else reads it
back. When evidence actually had to be reduced, the proposal's summary carries a deterministic
coverage notice appended to (never replacing) the model's own evidence-only summary, within the
existing 800-character bound. Only known numeric usage counters (`prompt_tokens`,
`completion_tokens`, `total_tokens`, `reasoning_tokens`) are copied from the provider's response;
any other provider-supplied field is dropped. A failed local receipt write is reported on stderr,
not silently swallowed.

## Recover interrupted work

Keep one writer per corpus. Leases from a confirmed dead local process can be reclaimed; an active
or uncertain owner blocks another orchestrator. Verify the owning process before manually removing
a lock. After an interrupted apply, rerun the same trusted worker command against the same corpus;
the worker reconciles its saved packet and proposal before another model call.

Back up the complete local corpus for pending model jobs: ignored packets, envelopes, proposals,
packet seals, worker job records and kernel operation state must travel together. Git alone omits
these recovery files. Do not copy isolated job pointers into a new clone and expect recovery.
Published metadata-only maintenance needs only its tracked cursor/state; it creates no model jobs.

## Directory catalog layer

```sh
uv run --python 3.12 python -m map_agents --root corpus catalog --limit 50
uv run --python 3.12 python -m map_agents --root corpus directory --limit 50
uv run --python 3.12 python -m map_agents --root corpus build
```

`directory` preserves the entire alltheagents.org site as concise catalog-evidence Markdown under
`map/directory/`, separate from source-supported repo dossiers under `map/repos/`. Its feature/interface
flags are the site's own self-reported observations, attributed to `directory`, never claims verified
against repository code; only `map/repos/` dossiers carry code-inspected evidence. Hosted maintenance
also runs a small bounded `directory` capture (see GitHub maintenance above) in addition to this manual
command. It requires a prior
`catalog` run: it reads the backing-feed commit from `state/catalog-cursor.json`, fetches the published
index (`https://alltheagents.org/agents.json`) fresh every call, and fetches every `agents/<slug>.md`
site page at that same immutable commit, verified against its Git blob SHA. `--limit` bounds pages per
call; state in `state/directory-cursor.json` makes repeat calls resume without refetching the site tree
at an unchanged commit or re-downloading an already-captured page; the tree's own `truncated` flag is
persisted and surfaced, so a partial GitHub listing is never reported as full site coverage. A per-page
fetch or hash-mismatch failure is recorded against its slug and does not stop the rest of the batch, but
hitting the network/time/request budget or a 403/429 stops issuing new requests for the rest of that call
instead of stamping every remaining, never-attempted page a failure; rerun `directory` to retry or resume.
Every previously captured page is re-verified against its recorded Git blob SHA before being treated as
already done, on every call and again inside `resolve`; a mismatch raises loudly during `capture` (fix the
corpus before continuing) and is reported as a `cache-tampered` gap, not silently trusted, during `resolve`.
The published index and backing feed are likewise hash-checked against their own recorded digests before
their facts are used.

`map_agents.directory.resolve(root)` is the read-only, no-network method for the union of
published/backing/page slugs, each with attributed facts, membership labels, evidence-level markers and
explicit cross-source discrepancies covering name/category/maker/license/language/model_providers,
platforms+install interface, every feature flag (including "yes (details)"-shaped values, distinguished
from an explicit "no" and from "unknown"/absent), and repository identity. A normalized repository lead
(`source_code_url`, falling back to `url`, exactly like the collector) is always exposed as `repo_key`
even when this corpus has not intaken it yet (`repo_tracked=False`); the renderer only links into
`map/repos/` when the repository is tracked, otherwise it shows the plain normalized GitHub lead so a
parent process can intake it. `maps.build` folds `directory.render(root)`'s pages into `map/build.json`'s
file manifest and its own `directory_digest`, so `query` and the map index/pointer include them
automatically and `query`'s `stale_view` flips true after any new `directory` capture, even one that
touches no repository record, until the next `build`.

Packaging the ready library/workbench into a distributable ZIP for a GitHub update is a separate,
later step outside this workbench's commands; it is not implemented here.

## Opt-in partitioned wiki layout

By default every repository shares one pinned kernel at `wiki/`, rooted at the whole `sources/` tree;
`prepare` scans every stored repository's sources each call. `python -m map_agents --root corpus
wiki-layout --enable-partitioned` switches new `prepare`/`apply` calls to one pinned kernel per
repository, under `wiki/shards/<stable-hash>/`, rooted only at that repository's own snapshot
directory (`sources/github/<owner>/<repo>/`) — so a `prepare` call only ever inventories its own
repository, not the whole corpus. `wiki-layout` with no flag shows the current layout. `audit` and
`build`/`query` are unaffected: dossiers and the generated map stay unified regardless of layout, and
`audit` aggregates every initialized kernel, shared or partitioned.

The switch is opt-in, versioned (`corpus/state/wiki-layout.json`, Git-tracked) and one-way per corpus:
it refuses if the shared kernel is already initialized or any repository already has indexed dossier
evidence, since migrating that evidence into partitions is not automatic. Enable it before the first
`prepare` call on a fresh corpus.

Repository identifiers whose combined `owner`+`repo` length exceeds 40 characters get a short,
deterministic hash-derived pair of storage directories instead of their real names, both under
`sources/github/` and in the per-repository dossier path, to stay well under Windows' path-length
ceiling; the full identity is unaffected and stays in snapshot/dossier metadata and URLs.
