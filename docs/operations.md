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
builds the map and audits the wiki. Its metadata deadline is 480 seconds, with default
12 MB/120-request aggregate network ceilings and 12 files/400 KB per snapshot.

Fatal receive/build/audit errors prevent publication. Valid partial refreshes publish their
fair cursor, failure counts and retained older evidence, then report a failing partial run.
This prevents one inaccessible repository from forcing every future run to restart at it.
The workflow stages only the named data directories and queue files, pushes normally to main,
and retains a summary and narrow state artifacts for 14 days. Inspect those artifacts after
a partial run. A concurrent main change may reject the push; retry from the new main normally.

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

## Recover interrupted work

Keep one writer per corpus. Leases from a confirmed dead local process can be reclaimed; an active
or uncertain owner blocks another orchestrator. Verify the owning process before manually removing
a lock. After an interrupted apply, rerun the same trusted worker command against the same corpus;
the worker reconciles its saved packet and proposal before another model call.

Back up the complete local corpus for pending model jobs: ignored packets, envelopes, proposals,
packet seals, worker job records and kernel operation state must travel together. Git alone omits
these recovery files. Do not copy isolated job pointers into a new clone and expect recovery.
Published metadata-only maintenance needs only its tracked cursor/state; it creates no model jobs.
