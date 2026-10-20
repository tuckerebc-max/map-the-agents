# Borrowed search execution investigation (F-1)

Investigated at base commit `ae446bc3b2adb46b3b16304b6818c8e63fc0a009` on
2026-07-14.

## Conclusion

The proposed drift-proportional fallback mechanism does **not** exist. A borrowed
`SearchIndex` does not receive a drift mask or delta, and the grep fallback walk
is not entered. The N=0/250/1,000 experiment was flat.

The actual large, unbounded request-path cost is more direct: every external
search reloads the borrowed index and performs a full strict freshness census.
That census walks the complete root and serially reads and hashes every indexed
file under the content-hash size cap, including files whose size and mtime match.
It is proportional to the borrowed corpus's file count and bytes, not to the
number of drifted files. Heavy CPU or I/O contention amplifies this full-corpus
work on every query.

There is a second unbounded path after the census: a stale posting list can make
literal/regex search reread every candidate that no longer contains the query.
That work scales with query-matching stale postings, not with the root's global
`drift_count`. It was not the dominant cost in the synthetic measurement.

## Exact call chain

Line references below are for the investigated base commit.

### Full-corpus work before lane selection

1. `handle_semantic_search` resolves an external Git root and calls
   `handle_external_search` at
   `crates/aft/src/commands/semantic_search.rs:195-228`.
2. Before choosing literal, regex, semantic, or hybrid mode,
   `handle_external_search` calls `open_search_index_read_only` at
   `semantic_search.rs:278-321`. Consequently every external search lane pays
   the opener cost.
3. `open_search_index_read_only` resolves the shared cache and calls
   `SearchIndex::read_from_disk_borrow_tolerant` at
   `crates/aft/src/readonly_artifacts.rs:64-90`.
4. The tolerant reader delegates to `read_from_disk_with_policy` at
   `crates/aft/src/search_index.rs:981-1012`. Each request:
   - reparses all file records and reroots every path at
     `search_index.rs:1084-1123`;
   - reads the lookup section to EOF, verifies its CRC, and rebuilds the lookup
     vector at `search_index.rs:1135-1192`; and
   - constructs a new in-memory index with empty `delta_postings` and an empty
     `superseded` set at `search_index.rs:1215-1229`.
5. After loading, the opener synchronously calls `search_drift_count` at
   `readonly_artifacts.rs:90`. The census:
   - performs an unbounded `walk_project_files` and builds a set of the complete
     root at `readonly_artifacts.rs:144-147`;
   - serially visits every indexed file at `readonly_artifacts.rs:150-168`; and
   - scans the complete walked set again for additions at
     `readonly_artifacts.rs:170-174`.
6. Every existing indexed file is passed to `verify_file_strict` at
   `readonly_artifacts.rs:158-166`. Strict verification reaches
   `verify_file_inner` through
   `crates/aft/src/cache_freshness.rs:198-205`. When size and mtime match, it
   still calls `hash_file_if_small` and reads the complete file at
   `cache_freshness.rs:312-330` and `cache_freshness.rs:81-100`. A same-size file
   with a different mtime is also hashed at `cache_freshness.rs:334-342`.
7. `search_drift_count` treats every verdict other than `HotFresh` as drift.
   Thus a byte-identical sibling file whose mtime differs produces
   `ContentFresh` and is counted as drift after being fully hashed. More
   importantly for latency, even N=0 hashes every file.

`cache_freshness.rs:208-266` has a bounded-size Rayon pool for bulk strict
verification, but `search_drift_count` does not use it. It invokes
`verify_file_strict` serially and has no file or wall-clock bound.

A semantic/hybrid external query can pay a second census. After the search-index
opener, `handle_external_semantic_or_hybrid_search` calls
`open_semantic_index_read_only` at `semantic_search.rs:487-548`. That opener
calls `semantic_drift_count` at `readonly_artifacts.rs:103-140`, which performs
another unbounded root walk and strict per-file verification at
`readonly_artifacts.rs:177-210`.

### Stale postings are not masked

The drift count is only recorded in response/log metadata at
`semantic_search.rs:308-315`; it is not passed to the query engine.

For a literal or regex external search:

1. `handle_external_grep_search` snapshots the newly loaded index and calls
   `search_grep` at `semantic_search.rs:443-448`.
2. `SearchIndexSnapshot::candidates` reads base posting lists at
   `search_index.rs:1736-1792`.
3. Posting lookup checks `superseded` at `search_index.rs:1821-1856`, but the
   tolerant disk reader initialized that set empty. There is no borrowed-root
   delta, stale-file mask, repair, or fallback walk.
4. `search_grep_profiled` materializes all candidates and scans them at
   `search_index.rs:1517-1626`. `search_candidate_file` rereads current disk
   bytes at `search_index.rs:1881-1903`. A stale posting that no longer matches
   therefore consumes a disk read without advancing the match-based stop
   condition.
5. Dead-file result filtering is after the index query at
   `semantic_search.rs:449-452`. It protects returned results; it does not bound
   candidate verification.

The only candidate stop condition is match based (`2 * max_results`). There is
no candidate file-count or time deadline, so a posting list made entirely stale
can be scanned in full.

### Existing fallback budgets do not apply

`MAX_FALLBACK_WALK_FILES` (50,000) and `FALLBACK_WALK_BUDGET` (10 seconds) are
defined at `crates/aft/src/grep_executor.rs:23-26`. They are used only by the
index-unavailable fallback walk (`grep_executor.rs:483-596`). External search
successfully loads a ready borrowed snapshot and directly invokes its query
methods, so it never passes through that fallback. The budgets constrain
neither:

- borrowed index deserialization;
- `search_drift_count` or `semantic_drift_count`; nor
- stale posting candidate verification.

## Reproduction

The reusable harness is `benchmarks/borrowed-search-drift.py`:

```sh
cargo build --release -p agent-file-tools
python3 benchmarks/borrowed-search-drift.py \
  --binary target/release/aft \
  --work-dir /tmp/aft-borrow-search-measure \
  --keep
```

The measured corpus contained 4,000 text files of 128 KiB each (500 MiB total),
plus a tracked `.aftignore`. The owner checkout built the shared index. Three
sibling Git worktrees borrowed it. Worktree mtimes were normalized to the owner
before editing so the opener reported exactly N=0, 250, and 1,000 rather than
counting Git checkout-time mtime differences.

For N=250 and N=1,000, exactly N files had a same-length query token replaced
while size and mtime were preserved. Each measured query selected only that
scenario's posting group. Therefore the changed cases are intentionally hostile:
every selected stale posting must be checked against current disk and returns no
match. N=0 selected 40 unchanged files and returned 20 results.

Measurements used a persistent AFT process, one warmup per case, seven serial
interleaved samples, and the release binary built from the investigated commit.
Latency is wall time from writing the NDJSON `semantic_search` request through
receiving its response. It includes local pipe transport, so it is not the
module log's internal `exec` timer; the 1.1 ms owner control below shows that the
transport contribution is negligible relative to the borrowed path.

### M1 measurement

Host: `tests-MacBook-Pro.local`, Apple M1 Max, 10 logical CPUs. The AFT
measurement lock contained `bg_282cadfb` for the build and all timed runs. Runs
were serial. The final drift run's one-minute load remained 1.58-1.80; the
five-minute value was 3.21 and the fifteen-minute value was 3.64-3.65, retaining
history from the preceding release build. Every timed sample and its load is
shown below as `latency_ms @ 1m/5m/15m load`.

Warmups (not included in summaries):

| N | Warmup |
|---:|---:|
| 0 | 500.155 @ 1.58/3.21/3.65 |
| 250 | 494.936 @ 1.58/3.21/3.65 |
| 1,000 | 492.351 @ 1.58/3.21/3.65 |

Raw measured samples:

| Repeat | N=0 | N=250 | N=1,000 |
|---:|---:|---:|---:|
| 1 | 477.440 @ 1.58/3.21/3.65 | 464.927 @ 1.58/3.21/3.65 | 483.511 @ 1.58/3.21/3.65 |
| 2 | 461.749 @ 1.70/3.21/3.65 | 472.612 @ 1.58/3.21/3.65 | 465.938 @ 1.58/3.21/3.65 |
| 3 | 473.975 @ 1.70/3.21/3.65 | 473.313 @ 1.70/3.21/3.65 | 472.476 @ 1.70/3.21/3.65 |
| 4 | 477.574 @ 1.70/3.21/3.65 | 463.558 @ 1.70/3.21/3.65 | 468.675 @ 1.70/3.21/3.65 |
| 5 | 468.683 @ 1.70/3.21/3.65 | 461.411 @ 1.70/3.21/3.65 | 475.491 @ 1.70/3.21/3.65 |
| 6 | 462.891 @ 1.80/3.21/3.64 | 463.388 @ 1.80/3.21/3.64 | 467.272 @ 1.70/3.21/3.65 |
| 7 | 455.542 @ 1.80/3.21/3.64 | 470.988 @ 1.80/3.21/3.64 | 471.068 @ 1.80/3.21/3.64 |

| Drift N | Raw ms | Median | Min-max |
|---:|---|---:|---:|
| 0 | 477.440, 461.749, 473.975, 477.574, 468.683, 462.891, 455.542 | 468.683 | 455.542-477.574 |
| 250 | 464.927, 472.612, 473.313, 463.558, 461.411, 463.388, 470.988 | 464.927 | 461.411-473.313 |
| 1,000 | 483.511, 465.938, 472.476, 468.675, 475.491, 467.272, 471.068 | 471.068 | 465.938-483.511 |

This is flat: N=1,000 is only 2.385 ms (+0.5%) above N=0, N=250 is
3.756 ms below N=0, and all ranges overlap. There is no monotonic drift-count
scaling law even though the changed queries selected only stale postings.

### Control that isolates the real mechanism

A follow-up used the same corpus and load window. The owner query used the
already resident index. `borrow_hash_all` was the N=0 worktree, where strict
verification hashes all 4,001 indexed files. For `borrow_skip_1000`, 1,000 files
had one byte appended; the query still matched the same 40 files. The size
mismatch makes `verify_file_inner` return `Stale` before hashing those 1,000
files. Counterintuitively, the worktree with more drift is faster because it
avoids 1,000 full-file hashes.

Every cell is again `latency_ms @ 1m/5m/15m load`:

| Repeat | Owner | Borrow, hash all | Borrow, skip 1,000 hashes |
|---:|---:|---:|---:|
| 1 | 1.113 @ 1.62/3.01/3.55 | 458.571 @ 1.62/3.01/3.55 | 371.335 @ 1.62/3.01/3.55 |
| 2 | 1.229 @ 1.65/2.99/3.54 | 458.175 @ 1.65/2.99/3.54 | 375.969 @ 1.62/3.01/3.55 |
| 3 | 1.099 @ 1.65/2.99/3.54 | 467.342 @ 1.65/2.99/3.54 | 370.553 @ 1.65/2.99/3.54 |
| 4 | 1.043 @ 1.65/2.99/3.54 | 462.095 @ 1.65/2.99/3.54 | 371.380 @ 1.65/2.99/3.54 |
| 5 | 0.963 @ 1.65/2.99/3.54 | 456.840 @ 1.65/2.99/3.54 | 386.535 @ 1.65/2.99/3.54 |
| 6 | 1.219 @ 1.65/2.99/3.54 | 470.479 @ 1.65/2.99/3.54 | 367.192 @ 1.65/2.99/3.54 |
| 7 | 0.931 @ 1.65/2.99/3.54 | 455.167 @ 1.65/2.99/3.54 | 372.097 @ 1.65/2.99/3.54 |

| Case | Median | Min-max |
|---|---:|---:|
| Owner resident index | 1.099 ms | 0.931-1.229 ms |
| Borrow, hash all | 458.571 ms | 455.167-470.479 ms |
| Borrow, skip 1,000 hashes | 371.380 ms | 367.192-386.535 ms |

The borrowed N=0 path is 417x the owner control. Skipping one quarter of the
strict hashes saves 87.191 ms (19.0%) despite increasing drift from 0 to 1,000.
This both reproduces the owner/borrow gap and identifies full-corpus strict
hashing as its dominant cause.

The raw M1 outputs were retained during the investigation at:

- `/tmp/aft-f1-final-results.jsonl`
- `/tmp/aft-f1-mechanism-results.jsonl`

## Implemented fix

The request-path census removal and rerooted-artifact cache are implemented.
The cache is bounded to four search/semantic entries, participates in the
existing idle-artifact eviction sweep, and uses canonical external root plus
artifact path, length, and modification time as its generation key. The external
Git-root and artifact-identity probes are also memoized so a cache hit does not
replace the removed corpus scan with per-query subprocess work.

The design has three parts:

1. **Remove strict drift census from the request path.** Treat a borrowed
   artifact as conservatively stale when it is opened; freshness classification
   does not change query behavior. Do not call `search_drift_count` or
   `semantic_drift_count` synchronously from an external search. Preserve the
   current contract: serve the shared stale index read-only, do not repair it,
   and do not add agent-facing stale warnings.
2. **Cache rerooted borrowed artifacts.** Keep a small `AppContext` cache keyed
   by canonical external root plus shared artifact generation (cache path,
   length, and modification time). Reuse the parsed read-only index until that
   generation changes. This removes per-query file-table/lookup deserialization
   without writing to or repairing shared artifacts.
3. **Bound optional diagnostics and candidate verification.** Exact drift
   telemetry was dropped from the request path. Borrowed literal/regex candidate
   verification now receives the existing file/deadline budget; exhaustion sets
   `truncated`/`engine_capped` so `more_available` remains honest.

Do not populate `delta_postings` or `superseded` from the drift audit. That would
be per-borrow repair/masking and would silently change which stale results the
borrow contract serves. Current-disk candidate verification, dead-file result
filtering, and disk-derived snippets should remain in place.

Implemented regression coverage:

- repeated external searches load/strict-audit a borrowed artifact at most once
  per artifact generation and an owner rebuild invalidates it once;
- the first external search performs no full-corpus strict hash census, with an
  instrumented strict-verification counter that proves the assertion is live;
- a stale posting list stops at injected file/time budgets and reports
  truncation;
- literal, hybrid, and semantic borrowed results keep current-disk dead-file and
  snippet behavior;
- agent-facing output contains no stale-index warning;
- the cache cap and idle eviction behavior are exercised; and
- a before/after byte snapshot proves the shared artifact directory is unchanged.

## Fixed-build M1 measurement

The final build was measured serially under the same lock convention on
`tests-MacBook-Pro.local` (Apple M1 Max, 10 logical CPUs). The run started at
one/five/fifteen-minute load `1.37/1.59/1.73` and ended at
`1.98/1.71/1.77`; every timed sample observed `1.54/1.62/1.74`. Warmups include
the one-time rerooted artifact load and were 99.400 ms, 109.358 ms, and
145.452 ms for N=0, 250, and 1,000 respectively.

| Repeat | N=0 | N=250 | N=1,000 |
|---:|---:|---:|---:|
| 1 | 1.289 | 3.429 | 11.249 |
| 2 | 1.233 | 3.480 | 12.237 |
| 3 | 1.198 | 3.532 | 11.046 |
| 4 | 1.331 | 3.397 | 11.766 |
| 5 | 1.254 | 3.448 | 11.508 |
| 6 | 1.277 | 3.512 | 12.254 |
| 7 | 1.167 | 3.305 | 11.711 |

| Drift N | Before median | Fixed median | Fixed min-max |
|---:|---:|---:|---:|
| 0 | 468.683 ms | 1.254 ms | 1.167-1.331 ms |
| 250 | 464.927 ms | 3.448 ms | 3.305-3.532 ms |
| 1,000 | 471.068 ms | 11.711 ms | 11.046-12.254 ms |

The borrowed N=0 median is now within 0.155 ms of the earlier 1.099 ms resident
owner control. Residual growth for N=250 and N=1,000 comes from bounded
current-disk verification of the stale posting candidates selected by those
queries, not from a corpus-wide drift census. The raw fixed-build output was
retained on the M1 and copied locally as
`/tmp/bg_282cadfb-final-benchmark.ndjson`.

## Generation-reload follow-up

A scaled debug-build replay used 30,001 indexed files, a session rooted in a
sibling checkout, and an explicit external path into the artifact owner's
checkout. A warm borrowed query took 3.965 ms. After rewriting 15,000 files and
letting the artifact owner persist the new generation, the next borrowed query
took 521.466 ms; the following query was warm again at 2.398 ms. The same first
borrowed load reached 3,359.653 ms during a high-load run.

A two-second macOS thread sample localized the reload cost before query mode
selection:

1. `handle_external_search` calls `AppContext::open_borrowed_search_index`.
2. An artifact generation change misses `BorrowedIndexCache` and enters
   `SearchIndex::read_from_disk_with_policy`.
3. Its `for file_id in 0..file_count` loop rebuilds every file record. Each
   record calls `cached_path_under_root`, which canonicalizes the existing
   path to reject symlink escapes. In the sample, 96 of 122 on-CPU reload
   samples were in that function's `fs::canonicalize`/`realpath` call.
4. The same reader then rebuilds the complete path map and lookup table. Legacy
   artifacts can additionally enter `compute_file_trigram_counts_from_base`,
   which visits every posting in every lookup entry.

These loops have no file-count, elapsed-time, or cancellation checkpoint. The
borrow cache removed repeated parsing, but corpus churn can replace the owner
artifact, change its generation key, and synchronously re-enter the full parse
while the interactive executor still holds the PureRead gate.

`MAX_FALLBACK_WALK_FILES` and `FALLBACK_WALK_BUDGET` do not constrain this work.
They are passed to candidate verification only after the borrowed index has
finished opening, and the unindexed fallback is not selected when `cache.bin`
exists. A generation reload therefore has to be bounded at the borrowed opener,
not only in the later grep walk.


## Parent-directory reload measurement

A release-build replay measured artifact-generation reloads with 30,001 indexed
entries (30,000 text files plus `.aftignore`). The borrowed worktree was warmed
before churn, then deleted 9,000 files and rewrote the next 9,000 files. The
owner rewrote that second range without deleting it and waited for its watcher
to publish a new artifact generation, so the reloaded borrowed artifact still
contained the deleted paths. The query targeted 40 unchanged files at the end
of the corpus.

The replay is available through the existing harness:

```sh
python3 benchmarks/borrowed-search-drift.py \
  --binary target/release/aft \
  --work-dir .borrowed-reload \
  --file-count 30000 \
  --file-size 256 \
  --repeats 1 \
  --generation-reload
```

The first row is the already-warm borrowed query before churn; the second is
the query that misses the borrowed-artifact cache after the owner publishes its
new generation.

| Build | Warm before churn | Reload after 30% delete + 30% rewrite |
|---|---:|---:|
| Base `aef4a250` | 0.300 ms | 1,254.426 ms |
| Parent-directory memo | 0.316 ms | 256.383 ms |

Both runs were serial on the same host with the 30,001-entry artifact. The
baseline run observed one/five/fifteen-minute load `8.85/10.08/11.14`; the
memo run observed `16.75/9.68/10.29`, so these single samples are directional
rather than an interleaved latency distribution. Even with the higher
one-minute load, the deletion-shaped reload fell by 998.043 ms (79.6%, 4.89x).
