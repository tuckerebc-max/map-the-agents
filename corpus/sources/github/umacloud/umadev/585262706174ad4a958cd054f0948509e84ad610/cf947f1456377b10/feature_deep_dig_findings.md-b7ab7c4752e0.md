# UmaDev feature-by-feature deep-dig findings (historical audit log)

> This file preserves the discovery history and the reasoning behind individual
> fixes. It is not the current release checklist. The authoritative current
> closure state is §7 of
> [`ENTERPRISE_MATURITY_AUDIT_2026-07-14.md`](ENTERPRISE_MATURITY_AUDIT_2026-07-14.md).
> Entries below that still say “Backlog” describe the state when that audit
> round was written; later resolution notes and regression tests take precedence.

## Fix progress
The initial round recorded 21 verified fixes. Subsequent rounds also closed CLI
H1, router F3/F4, pipeline F4, TUI F2, CLI M1/M2/M6, knowledge #1-#8, DB-M1,
DP-M2/DP-M3, deterministic capped walks, deleted-file run diffs, source-aware PR
staging, and exact non-zero failure semantics. Each closure is locked by a
targeted regression test and the all-features workspace suite.

A 6-lane deep functional audit of every feature area. Status: FIXED = fixed this session;
the rest are a prioritized backlog. All are code-verified, no fabrication.

## Fixed this session (recent half-fixes / regressions I owned)

- FIXED router F1 — `brain_to_route` seated a team on Chat/Fast turns (needs-widening
  guard reached only the fork path). `router.rs` — guarded like `reconcile_team`.
- FIXED router F2 — `BrainRoute.confidence: f32` non-tolerant, a quoted number sank the
  whole parse, build degraded to Chat. Added `de_lenient_f32`.
- FIXED pipeline F2 — the doc-seat source-present exemption existed only in
  `verify_step_evidence`, not `verify_step_acceptance`, so a designer/re-planned doc step
  was falsely rejected. Applied the same exemption to the A::SourcePresent acceptance path.
- FIXED TUI F1 — the 1.0.36 "switch-to-Auto releases the pending approval" was unreachable
  while a pause was active (shift+Tab was swallowed). `resolve_pending_approval` now lets
  `BackTab` fall through to the mode cycle.

## Backlog — HIGH

- CLI H1 `cmd_pr` — `pr --create` stages only `output/`+proof artifacts, never the run's
  real SOURCE changes, so it opens a source-less PR; the has-changes gate ignores `output/`
  so it passes exactly when uncommitted source exists.
- [FIXED] CLI H2 `main.rs:4254` `cmd_verify` — `umadev verify` (no `--runtime`) runs NO
  test/build/lint (pure status report, always Ok), contradicts `.claude/CLAUDE.md`.
- [FIXED] CLI H3 `main.rs:1795` `cmd_init` — the 1.0.34 init upgrade calls `run_adopt`
  unconditionally, writing the brownfield marker, so the NEXT `umadev run` sees
  `is_adopted()==true` and injects "work incrementally, never regenerate" into a fresh
  build, a degraded greenfield. (My 1.0.34 regression.) Fix: init shares only the analysis +
  CLAUDE.md `## Project` refresh, NOT the brownfield marker.
- [FIXED] pipeline F1 `main.rs:3639` `is_pipeline_complete` — only recognizes the legacy
  `"Pipeline complete."` sentinel; the DEFAULT director/continuous finalize writes
  `"Advanced to delivery"`, so CLI `umadev continue` on a cleanly-finished default build
  RE-RUNS backend->quality->delivery (re-invokes the paid base + overwrites the proof-pack).
- knowledge #1 `retrieve.rs:529-538` + `phases.rs:329-335` — promoted GLOBAL lessons
  (slug filenames under `~/.umadev/learned/<domain>/`) are phase/seat-filtered OUT because
  the "always allow lessons" check keys on the `lesson-` filename marker global slugs lack.

## Backlog — MEDIUM

- [FIXED] router F5 `director_loop.rs:760-765` — staleness set carries only SOURCE artifact kinds;
  FrontendEngineer reads the DERIVED `ApiContract`, so editing `architecture.md` never
  reopens the frontend step, frontend builds against a stale contract.
- router F4 `runner.rs:3984-3997` — legacy quality critic team omits arch/prd/uiux
  (BackendCritic judges contract fidelity blind) + runs serially (docstring says concurrent).
- router F3 `plan_state.rs:886-897` — falsifiability backstop runs before the doc floor,
  can pin `BuildClean` onto a PM/architect doc-authoring step.
- [FIXED] pipeline F3 `director_loop.rs:2008-2016` — an empty-team Review step is marked Blocked, a
  fully-successful build finalizes as INCOMPLETE (proof-pack withheld).
- pipeline F4 `main.rs:3881` `cmd_continue` — CLI continue can't resume a director-loop plan;
  always re-runs a legacy gate block, discarding `.umadev/plan.json` Done statuses.
- pipeline F5 `plan_state.rs:251` — a Malformed brain evidence contract is un-passable by the
  doer (only the one re-plan escapes), can hard-block an upstream doc step.
- TUI F2 `app.rs:10890` `steer_plan` — `/plan skip|veto` silently no-ops during a director
  build (queued_steer drains only on legacy events) + leaves a stuck "queued N" chip.
- CLI M1 verify/deploy/report/pr all exit 0 regardless of outcome, unusable as CI gates.
- CLI M2 `runtime_proof.rs:396` `--runtime` hard-sets "Verified" before probing; GET-only
  probes; no backend boot; port-squatter reused as the server.
- CLI M3/M4 init re-run isn't the advertised no-op; a hand-edited manifest blocks the
  `## Project` refresh unless `--force` (which overwrites the edit).
- [FIXED] CLI M5 `uninstall --base pre-commit` doesn't resolve the git root, false "Removed".
- CLI M6 `ci --changed-only` runs a full `npm audit`, a pre-existing CVE aborts every commit.
- [FIXED] CLI M7 `mcp-manage codex` clobbers an inline-table `mcp_servers`.
- [FIXED] CLI M8 `knowledge-manage add` can `remove_dir_all` a colliding same-named entry's files.
- knowledge #2 `phases.rs:209/320` — agentic/seat digest passes the knowledge dir as
  `project_root`, excludes project sediment + rebuilds the BM25 index from scratch EVERY
  work-class firmware compose (perf) + mislocates the cache.
- knowledge #3 `context.rs:339-387` — the RAG tail (pitfall memory + curated knowledge) is
  starved to empty by a growing head (facts/open-decisions/big AGENTS.md) + repo-map-first.
- knowledge #4 `phases.rs:210-212` / `lessons.rs:3287-3289` — retrieval early-returns before
  `record_*` on an empty hit set, defeats the "clear on empty" snapshot invariant,
  cross-step PASS/FAIL mis-attributed to the previous step's chunks/lessons.
- knowledge #5 `repomap.rs:194-235` / `index.rs:678-710` — MAX_FILES cap applied before sort,
  nondeterministic file subset + coverage holes on large repos/corpora.
- knowledge #6 `chunker.rs:416-448` — no max-chunk cap, a giant H2-less doc becomes one huge
  chunk (BM25-penalized, embedder-truncated, only-head in digests).
- knowledge #7 (adopt) `adopt.rs:434-451` ignores `method_known`; `verify.rs` stack precedence
  mislabels Rust+JS repos as node; `adopt.rs:267-286` no per-file byte cap.
- knowledge #8 `retrieve.rs:615-708` — `min_score` gate applied to incompatible BM25-vs-RRF
  score scales, recall depends on query language/path not relevance.

## Backlog — LOW (selected)
- knowledge: dedup after top-k truncation; repo-map memo only checks root mtime; block-comment
  phantom symbols; KV-cache prefix busted by the per-seat persona; lessons ledger
  truncate-then-write (crash = whole-jsonl loss).
- CLI: init `unknown` dead branch; doc drift; `report --review` builds twice; CJK slug branch
  collapse; whitespace-arg acceptance; worktree `.git`-file error.
- router: dead no-op `if` in `for_run` (`router.rs:294-296`).

## Not yet dug
- governance/trust/security/contract lane (the 6th agent) — still running at write time.
- Within knowledge: `vector.rs`/`local_embed.rs`, `error_kb.rs`, `experts.rs` internals were
  checked only from call sites, not line-by-line.

## Backlog — governance / trust / security / contract lane (6th, complete)

SAFETY (classification completeness; enforcement wiring + fail-open are solid):
- [FIXED] T1 [CRITICAL] trust.rs:841 - find is a READ_VERB, so "find . -delete" / -exec rm is
  Read+Reversible and auto-runs a RECURSIVE DELETE in Plan (read-only), Guarded, and Auto.
  Fix: treat find carrying -delete/-exec/-execdir/-ok as Destructive.
- [FIXED] T2 [HIGH] trust.rs:505 - a Shell command redirect/cp/tee destination is never run through
  target_escapes_workspace, so "echo x >> ~/.ssh/authorized_keys" auto-runs in Guarded/Auto.
- [FIXED] T3 [MED] trust.rs:189 - DESTRUCTIVE_TOKENS substrings "dd " / "> /dev" match git add /
  cargo add / > /dev/null, false-confirm ubiquitous commands, Auto-run wedge.
- LOW rules.rs:8360 - "curl url|sh" (no space) bypasses the dangerous-bash block.

SECURITY / REVIEW gates (fail-open, so unsafe-pass or false-alarm, never fail-closed):
- [FIXED] S-H3 [HIGH] security.rs:455 - run_capped merges stdout+stderr, cargo-audit/pip-audit JSON
  parse always fails, dependency scanners functionally dead. (+ pipe deadlock >64KB.)
- [FIXED] R-H1 [HIGH] review.rs:139 - scan_ci_weakening diffs HEAD (uncommitted only); a committed PR
  gives an empty diff and PASSes having verified nothing. Fix: diff vs merge-base.
- [FIXED] R-H2 [HIGH] review.rs:519 - SKIP_MARKERS substring "xit(" matches process.exit / exit,
  false Fail blocks legit PRs. Fix: token boundary.
- [FIXED] R-M3 [MED] review.rs:78 - security_claim caps at Warn even with high/critical findings.
- DB-M1 [MED] review.rs:506 - misses most CI-weakening forms (continue-on-error, || true, etc).

PR / DEPLOY:
- [FIXED] D-H1 [HIGH] pr.rs:96 - git_default_branch hardcodes main; a master-default repo can get
  master returned as the commit head (branch-isolation escape).
- DP-M2 [MED] deploy.rs:139 - StaticHost detects dist/out/build/public but hardcodes surge ./dist.
- DP-M3 [MED] pr.rs:162 - PR readiness reuses git_has_changes (ignores output/), a docs-only
  deliverable blocks the PR.

CONTRACT:
- C1 [MED] backend.rs:265 - backend route extractor still false-flags real registrations
  (custom router names, .route().get() chains, string-concat URLs), all-or-nothing false gaps.

SOLID (verified): fail-open airtight at lib + hook binary; trust FLOOR enforcement structure
correct + ledger cannot relax the floor; runtime_proof never claims Verified without a real
2xx/3xx; emoji/color/AI-slop + rm-rf equivalence detectors well-calibrated.


## Re-review round 2 - agent-assisted (COMPLETE this session)
Four parallel review agents adversarially re-audited: (a) my own 22 fixes for regressions,
(b) knowledge crate internals, (c) the 4 host session drivers, (d) contract/spec/governance.

FIXED this round (14):
- [FIXED] REGRESSION H1 (mine, F1): is_pipeline_complete matched "Advanced to delivery",
  written on EVERY delivery-phase sync -> continue refused to resume an incomplete build.
  Fix: clean finalize (director + continuous) stamps distinct "Pipeline complete.".
- [FIXED] REGRESSION M1 (mine, T2): shell_write_escapes flagged > /dev/null -> Guarded denied
  npm test 2>/dev/null. Fix: benign char-device exemption.
- [FIXED] REGRESSION M2 (mine, DB-M1): || true / if: false false-flagged ordinary source.
  Fix: ambiguous markers only fire in CI/workflow/shell/build files.
- [FIXED] REGRESSION M3 (mine, F3): floor-CORROBORATED review residual marked Done not Blocked.
  Fix: F3 Done only when gap_evidence is empty (true empty-team skip).
- [FIXED] HIGH curl|sh RCE: no-space + sudo spellings bypassed "| sh". Fix: structured floor
  detects network-downloader -> shell-interpreter across pipe segments.
- [FIXED] HIGH C1: custom Express router names missed -> false rework loops. Fix: receiver may
  end in router/route/routes.
- [FIXED] V1 (codex): terminal TurnDone + gating NeedApproval try_send -> hang. Fix: blocking send.
- [FIXED] knowledge #4: empty retrieval clears the surfaced-chunks snapshot.
- [FIXED] knowledge #6: chunker splits oversized section on paragraph boundaries (never a fence).
- [FIXED] V2: stderr drain read_until + from_utf8_lossy (non-UTF-8 no longer aborts).
- [FIXED] flaky x2: chat_first_turn_auto_redrive (locale) + resolve_goal_mode trio (env lock).
- [FIXED] L1: gitleaks count reads stdout+stderr. L2: init keeps a hand-authored UMADEV.md.

STILL OPEN:
- knowledge #1 HIGH: promoted GLOBAL lessons phase-filtered out (needs learned-origin signal;
  retrieve.rs:529 + phases.rs:337).
- P1 HIGH (claude, PLAUSIBLE): --allowedTools may pre-approve Write/Edit/Bash bypassing guarded
  floor - needs a LIVE claude drive to confirm before changing.
- extract.rs MED (concat frontend URL); knowledge #5/#8 MED; dedup-collapse LOW; opencode V3/V4 LOW.
- REFUTED clean: experts/vector/local_embed/tokenizer; spec; governance fail-open; codex.
