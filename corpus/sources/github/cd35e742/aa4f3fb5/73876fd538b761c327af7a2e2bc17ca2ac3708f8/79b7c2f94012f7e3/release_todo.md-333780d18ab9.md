# Release, Issue, and Dependency TODO

## Operating Constraints

- [x] Stay on `main`; do not create a branch.
- [x] Read AGENTS.md instructions supplied for this repo.
- [x] Read the full README.md.
- [x] Read `$library-updater`, `$release-preparations`, `$dsr`, `$gh-cli`, and `$rust-crates-publishing` skill instructions.
- [x] Do not delete files or run destructive cleanup commands.
- [x] Do not overwrite `.env`.
- [x] Preserve unrelated dirty work and untracked files unless explicitly directed otherwise.
- [x] Use `rch exec -- env CARGO_TARGET_DIR=... cargo ...` for Rust gates.

## Dependency Updater

- [x] Detect manifests and package managers.
- [x] Inspect current dependency graph and direct dependencies.
- [x] Run outdated/update discovery.
- [x] Research each dependency with an available update or blocker.
- [x] Update one dependency at a time where safe.
- [x] Log every update, skip, blocker, and test result in `UPGRADE_LOG.md`.
- [x] Update `claude-upgrade-progress.json` after each dependency decision.
- [x] Run focused verification after each accepted update.
- [x] Run initial dependency/security audit.
- [x] Run a final dependency/security audit.

## GitHub Issues

- [x] Authenticate and inspect repo identity through `gh`.
- [x] List open issues, with issue 218 inspected first.
- [x] Build an issue ledger of every open or recent unresolved issue.
- [x] For each issue, identify the exact expected behavior and proof needed.
- [x] #218 watcher OOM: chunk watch ingest, split OOM batches, advance HWM after partial success, and chunk cass#202 orphan cleanup.
  - Proof: `cargo test --lib watch_reindex_splits_oom_batches_and_still_advances_state`; `cargo test --lib cleanup_orphan_fk_rows_handles_more_than_one_delete_chunk`.
- [x] #222 token column drift: ensure `conversations.total_*` columns exist after downgrade/rebuild so frankensqlite snapshot updates do not fail.
  - Proof: `cargo test --lib schema_repair_adds_missing_conversations_token_columns`.
- [x] #212 shard invariant / UNIQUE cluster: prevent stale-low shard message counts and keep duplicate-idx merge decisions aligned with SQL inserts.
  - Proof: `cargo test --lib insert_conversations_batched_refreshes_partial_pending_message_lookup`; `cargo test --lib insert_conversations_batched_reprocessing_conversation_is_idempotent`; `cargo test --lib list_conversation_footprints_for_lexical_rebuild_raises_stale_low_tail_cache`; `cargo test --lib shard_validate`.
- [x] #226 install/doctor UNIQUE+wedge: prove the duplicate-idx path no longer submits conflicting rows; remove bogus `--mode lexical` status hints; surface raw-mirror disk usage.
  - Proof: duplicate-idx tests above; `rg -n "or use --mode lexical|Try --mode lexical|use --mode lexical" src/lib.rs src/search src/indexer tests/golden` returned no matches; `cargo test --lib raw_mirror::tests::prune`.
- [x] #213 post-rebuild stall: prove producer/byte-limiter wakeups cannot park until the 120s watchdog timeout.
  - Proof: `cargo test --lib streaming_byte_limiter_update_does_not_lose_wakeup_under_repeated_shrink_grow`.
- [x] #221 raw-mirror bloat: provide `cass mirror prune` dry-run/apply plan with audit log, `--keep-tag`, 7-day recent-capture hold-down, doctor `raw_mirror.size` warning, and `cass stats` raw-mirror totals.
  - Proof: `cargo test --lib raw_mirror::tests::prune`; `cargo test --lib raw_mirror_report_warns_when_verified_blob_bytes_cross_threshold`; README and robot-docs command surface updated.
- [x] #227 OpenCode Drizzle SQLite: pin cass to a franken_agent_detection revision that ingests `opencode.db`, with cass-side regression coverage.
  - Proof: `cargo test --test connector_opencode opencode_parses_drizzle_sqlite_schema`; `cargo test --test agent_detection_completeness`; build contract now pins `franken-agent-detection` `3ad1970` (`v0.1.6`) after adding Hermes/OpenCode inventory coverage and restoring Claude Code home fallback discovery when `XDG_CONFIG_HOME` is set upstream.
- [x] #228 Codex superlinear indexing: prove the O(N^2) duplicate/merge paths were removed or bounded with targeted regression/perf evidence.
  - Proof: `cargo test --lib modern_codex_duplicate_detection_uses_precomputed_sets`; duplicate-idx pending lookup tests above; `cargo test --test cli_index index_robot_trace_ingest` proves `--robot-trace-ingest` emits per-batch `{batch_n,batch_msgs,wall_ms,lookups_against_global}` plus lookup counters for future perf bisection.
- [x] #229 public embedding surfaces: promote `raw_mirror` and `doctor` from crate-private modules to public library modules and expose the intended raw-mirror capture/summary/prune APIs plus the typed doctor request/execute boundary.
  - Proof: `cargo test --test cli_refresh_contract raw_mirror_and_doctor_modules_are_public_embedding_surfaces -- --nocapture`; `cargo check --all-targets`; `cargo clippy --all-targets -- -D warnings`.
- [x] Release artifact follow-up: avoid rewriting the already-pushed `v0.4.3` tag and prepare `v0.4.4` with a macOS-only `CoreML` link hint for the aarch64 ONNX Runtime static archive.
  - Proof: `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-check-target cargo fmt --check`; `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-check-target cargo check --all-targets`; `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-check-target cargo clippy --all-targets -- -D warnings`.
- [x] Map each issue to existing code/tests when already fixed.
- [x] Implement missing fixes for any issue that is not truly resolved.
- [x] Add or adjust tests/goldens for each fixed behavior.
  - Proof: `UPDATE_GOLDENS=1 cargo test --test golden_robot_json --test golden_robot_docs` passed after the final CLI/docs changes.
- [x] Close only issues with concrete proof from code, tests, commits, or release artifacts.
  - Closed with proof comments: #229, #228, #227, #226, #222, #221, #218, #213.
  - Current open issues by public GitHub REST as of 2026-05-13 23:38 UTC: none (`[]`). Authenticated `gh issue list` is temporarily blocked by the account's GraphQL rate limit.
  - Rechecked open issues by public GitHub REST as of 2026-05-14 00:23 UTC: none (`[]`).

## Local Verification

- [x] Run `cargo fmt --check` through `rch`.
  - v0.4.5 metadata rerun: `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-check-target-v045 cargo fmt --check` exited 0.
- [x] Run `cargo check --all-targets` through `rch`.
  - Note: final remote `cargo check` exited 0; local `rch` `.rch-target` artifact retrieval wedged and was terminated after the successful remote result.
  - v0.4.5 metadata rerun: `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-check-target-v045 cargo check --all-targets` remote exit 0.
- [x] Run `cargo clippy --all-targets -- -D warnings` through `rch`.
  - Note: first clippy pass found two `filter_map_bool_then` findings in `src/raw_mirror.rs`; fixed and reran. Final remote clippy exited 0; local `rch` `.rch-target` artifact retrieval wedged and was terminated after the successful remote result.
  - v0.4.5 metadata rerun: `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-check-target-v045 cargo clippy --all-targets -- -D warnings` remote exit 0; local `rch` `.rch-target` artifact retrieval wedged and was terminated after the successful remote result.
- [x] Run release-appropriate tests through `rch`.
  - Full `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-test-target cargo test` remote exit 0 after the lifecycle matrix telemetry scrub fix; doc tests also passed (7 passed, 20 ignored). The local `rch` wrapper wedged only during `.rch-target` artifact retrieval after remote success and was terminated.
  - Focused #229 rerun after the public API change: `cargo test --test cli_refresh_contract raw_mirror_and_doctor_modules_are_public_embedding_surfaces -- --nocapture` passed (1 passed).
  - Final full #229-inclusive rerun: `rch exec -- env CARGO_TARGET_DIR=/tmp/cass-test-target cargo test` remote exit 0 in 1,214,384ms; doctests passed (7 passed, 20 ignored). Artifact retrieval completed for the repo tree, then the local wrapper was terminated during `.rch-target` retrieval after the successful remote result.
- [x] Run UBS on changed files or staged files.
  - Current local result: UBS still exits 1 on the changed-file set. A baseline-vs-current shadow run showed the gate is dominated by inherited/noisy touched-file findings (unwrap/expect/assert/vector-collect/token-comparison style warnings) rather than a clean pass. Do not claim UBS passed; resolve through policy/baseline work before treating this gate as green.
- [x] Run any issue-specific regression tests.
- [x] Inspect `git diff --check`.
  - v0.4.5 metadata rerun: `git diff --check` exited 0.
- [x] Fresh-eyes reread new/modified release/updater code and docs.
  - Re-read the #229 public API patch after implementation: kept manifest/layout helper internals private, avoided exposing CLI wrap plumbing publicly, and added a public function-pointer assertion for `doctor::execute_doctor_command`.

## Release Preparation

- [x] Inspect latest tags and GitHub releases.
  - Latest GitHub release/tag: `v0.4.2`, published 2026-05-08.
- [x] Count and summarize commits since the latest release.
  - `git rev-list --count v0.4.2..HEAD` reported 308 committed changes before this release commit.
- [x] Determine the next version from release scope.
  - Selected `v0.4.3` because this is a bugfix/diagnostic/dependency release in the pre-1.0 series.
- [x] Update Cargo.toml version.
- [x] Update Cargo.lock through a cargo command.
- [x] Update CHANGELOG.md with useful release notes.
- [x] Check install scripts and package metadata for version/asset expectations.
  - Release workflow expects `cass-linux-amd64.tar.gz`, `cass-linux-arm64.tar.gz`, `cass-darwin-arm64.tar.gz`, `cass-windows-amd64.zip`, per-asset `.sha256`, signatures/certificates, installers, SBOM, and aggregate `SHA256SUMS.txt`.
- [x] Commit release-ready v0.4.3 issue fixes on `main`.
  - Pushed commit: `613edf56 fix(v0.4.3): expose doctor and raw mirror APIs`.
- [x] Push `main`.
- [x] If origin `master` exists, mirror `main` to `master`.
- [x] Create and push the v0.4.3 release tag.
  - Note: `v0.4.3` is pushed and its GitHub release workflow is still queued; no GitHub release exists for that tag.
- [x] Commit release-publication v0.4.4 macOS link fix on `main`.
  - Pushed commit: `88ed86bb fix(release): link CoreML for macOS release builds`.
- [x] Push `main` and mirror to `master`.
- [x] Create and push the `v0.4.4` release tag.
  - GitHub Actions run: `25831721749`, still queued at `Validate Release Config` as of 2026-05-13 23:38 UTC.
- [x] Detect post-`v0.4.4` main movement before artifact publication.
  - `main` advanced to `fb962a5b` (`fix(doctor/cleanup-apply): log when journal RunStarted/RunEnded append fails so the run isn't silently dropped from the journal`) after the immutable `v0.4.4` tag at `88ed86bb`.
  - Do not upload fallback artifacts built from `fb962a5b` under the `v0.4.4` release name.
- [x] Prepare `v0.4.5` release metadata on `main`.
  - Version bumped in `Cargo.toml` and `Cargo.lock`; changelog documents the release-integrity fix and doctor cleanup journaling diagnostics.
- [x] Commit release-integrity v0.4.5 metadata on `main`.
  - Pushed commit: `f088963b chore(release): prepare v0.4.5`.
- [x] Push `main` and mirror to `master`.
- [x] Create and push the `v0.4.5` release tag.
  - Superseded before publication after the Windows fallback build exposed a real MSVC release-build blocker.
- [x] Commit release-build v0.4.6 Windows fix on `main`.
  - Pushed commit: `849bf2a9 fix(release): unblock Windows MSVC builds`.
  - Fix: direct vendored OpenSSL dependency is now scoped to non-Windows targets; Linux/macOS static OpenSSL packaging remains intact while Windows MSVC no longer attempts an OpenSSL source build.
- [x] Push `main`, mirror to `master`, and create/push `v0.4.6`.

## DSR and GitHub Release

- [x] Run `dsr doctor`.
  - Passed: git/gh/jq/curl/yq/docker/act/ssh/minisign/syft/GitHub/disk/config checks were healthy.
- [x] Confirm the project is registered or add/update dsr configuration if needed.
  - `dsr repos list --json` shows `coding_agent_session_search` registered for linux/amd64, linux/arm64, darwin/arm64, and windows/amd64.
- [x] Run `dsr check` for release infrastructure status.
  - `dsr check coding_agent_session_search` reports GitHub Actions throttling (`THROTTLED: 4 runs queued`), so fallback release infrastructure may be needed after commit/tag.
- [x] Prefer GitHub Actions release flow when healthy.
  - Not healthy during this release: tag release runs remained queued even after stale/non-release workflow runs were cancelled.
- [x] Use dsr fallback only if Actions is throttled, blocked, or path dependency constraints require it.
  - DSR fallback built linux/amd64 and linux/arm64 raw binaries and packaged windows/amd64 for `v0.4.3`.
  - DSR native macOS build on `mmini` is blocked by host dyld state: newly linked Rust binaries hang at `_dyld_start` even for a trivial hello-world.
  - Linux-hosted `cargo zigbuild` fallback reached the macOS release link problem and motivated the `CoreML` link fix.
  - A follow-up `/tmp` cross-build progressed past OpenSSL and into final binary LTO, then failed because `/tmp/cass-darwin-zig-target` disappeared mid-link (`couldn't create a temp dir: No such file or directory`). Retrying with durable `/data/tmp` target/prefixes.
  - Durable OpenSSL prefix work: `Configure darwin64-arm64-cc` and `make -j1 build_libs install_dev` succeeded under `/data/tmp/cass-openssl-aarch64-apple-darwin-build-20260513`, installing `libcrypto.a`, `libssl.a`, headers, and pkg-config files to `/data/tmp/cass-openssl-aarch64-apple-darwin-3.6.2`.
  - Current local fallback command is rebuilding `v0.4.4` for `aarch64-apple-darwin` with `CARGO_TARGET_DIR=/data/tmp/cass-darwin-zig-target-v044` and `OPENSSL_DIR=/data/tmp/cass-openssl-aarch64-apple-darwin-3.6.2`.
  - Durable macOS fallback completed for the superseded v0.4.4 version: `/data/tmp/cass-darwin-zig-target-v044/aarch64-apple-darwin/release/cass` is `Mach-O 64-bit arm64 executable`; packaged checksum `a976d037128810c01ce449e4a2d6c9924f2ed35dd84ada1ca31ee72a07c6f4d0`. Rebuild for v0.4.5 before publishing.
  - DSR packaged `windows/amd64` for v0.4.4, but the resulting `cass.exe` is an ELF Linux x86-64 binary, not a PE/Windows executable. Treat that asset as invalid; v0.4.5 needs a real Windows cross-build or a documented blocker.
  - v0.4.6 DSR fallback built Linux amd64/arm64 successfully and packaged `cass-linux-amd64.tar.gz` / `cass-linux-arm64.tar.gz`.
  - v0.4.6 macOS arm64 fallback built a valid `Mach-O 64-bit arm64 executable` via cargo-zigbuild and packaged `cass-darwin-arm64.tar.gz`.
  - v0.4.6 Windows MSVC fallback built a valid `PE32+ executable for MS Windows 6.00 (console), x86-64` after adding xwin SDK case-compat symlinks for `DirectML.lib` and `PathCch.lib`; packaged `cass-windows-amd64.zip`.
- [x] Verify GitHub release exists.
  - Release: <https://github.com/Dicklesworthstone/coding_agent_session_search/releases/tag/v0.4.6>
- [x] Verify all expected assets and checksums are present.
  - Release assets: `cass-linux-amd64.tar.gz`, `cass-linux-arm64.tar.gz`, `cass-darwin-arm64.tar.gz`, `cass-windows-amd64.zip`, per-asset `.sha256`, installers, `SHA256SUMS.txt`, plus DSR raw `cass`.
  - Checksums: Linux amd64 `af4de4c880aadd41d6d882fd8d559195d7abd85fe8216eed82b3dfdee1f5fe04`; Linux arm64 `6e45b4bd2456fb4aeea22ca60c5abc222a334827e7782a26005a2e83331b61f9`; macOS arm64 `c5e6d69227db35306dcd419e83cb8a4b30902362b806a2d26f995d027fd53581`; Windows amd64 `bb2878345fa5dad201258ab316957caac49397e4e4c8c9d0cf4483618be48108`.
- [x] Download at least one release asset and verify `cass --version`.
  - Downloaded `cass-linux-amd64.tar.gz`, verified its `.sha256`, extracted, and ran `./cass --version` -> `cass 0.4.6`.
- [x] Run `dsr release verify coding_agent_session_search <version>` or the correct dsr repo key.
  - `dsr release verify coding_agent_session_search 0.4.6` passed after adjusting the local DSR manifest to verify packaged Linux archives rather than the extensionless raw intermediate binary.

## crates.io

- [ ] Check whether `coding-agent-search` is already published on crates.io.
- [ ] Validate crate metadata: repository, license, README, include/exclude behavior.
- [x] Run `cargo package`.
  - `cargo package --locked --no-verify` refused because the working tree is dirty, including unrelated untracked files `test_dir_symlink.rs` and `test_xss.rs`.
  - `cargo package --locked --no-verify --allow-dirty` failed because the currently published `franken-agent-detection` crate does not expose the `chatgpt` feature required by cass.
  - v0.4.4 retry: `cargo package --locked --no-verify --allow-dirty` failed because crates.io only offers `franken-agent-detection` up to `0.1.3`, which lacks the required `chatgpt` feature. `franken-agent-detection v0.1.6` is available only from the pinned git rev until crates.io publish auth is fixed.
  - v0.4.6 retry: `cargo package --locked --no-verify --allow-dirty` still fails because crates.io only offers `franken-agent-detection` up to `0.1.3`, which lacks the required `chatgpt` feature.
- [ ] Run `cargo publish --dry-run`.
- [ ] If publishable and token is available, publish the crate.
- [x] If blocked, record the precise blocker and the work needed to make it publishable.
  - Blocker: publish registry-compatible sibling crates first, starting with `franken-agent-detection v0.1.6` (`3ad1970`) with the `connectors`, `cursor`, `chatgpt`, `opencode`, `crush`, and `hermes` features available from crates.io; then rerun cass package/publish dry-run to expose any next registry-only blockers.
  - Follow-up attempted: prepared, verified, pushed, mirrored, and tagged `franken-agent-detection v0.1.6` (`cargo test --all-features` passed). Earlier actual `cargo publish --all-features` for `v0.1.4` reached upload and failed with crates.io `403 Forbidden: authentication failed`; retry `v0.1.6` publishing after the release gates, but a valid crates.io token may still be required.
  - Latest retry: `franken-agent-detection v0.1.6` `cargo publish --allow-dirty --all-features` now fails before upload during crate verification because the published `fsqlite-pager 0.1.2` crate cannot resolve `fsqlite_types`, `fsqlite_vfs`, and `fsqlite_wal` from its own registry dependency graph. CASS registry packaging is blocked until the frankensqlite crate family is registry-coherent and FAD v0.1.6 can be published with the required features.

## Homebrew

- [x] Locate the Homebrew tap/formula for `cass`.
  - Local tap checkout: `/data/projects/homebrew-tap`; formula: `Formula/cass.rb`.
- [x] Inspect current formula version and asset URL pattern.
  - Formula currently points to `v0.4.2` assets and cannot be updated until `v0.4.3` release assets/checksums exist.
- [x] Refresh local tap checkout.
  - `git -C /data/projects/homebrew-tap pull --ff-only` succeeded; tap is clean at `origin/main`.
- [x] Compute SHA256 values for the released assets Homebrew uses.
- [x] Update formula version, URLs, checksums, and bottle metadata if applicable.
  - Updated `/data/projects/homebrew-tap/Formula/cass.rb` to `0.4.6` with verified Linux/macOS checksums. No bottle metadata exists in the formula.
- [x] Run formula audit/test where available.
  - `ruby -c Formula/cass.rb` passed. `brew` is not installed in this environment, so `brew audit` / `brew test` could not be run locally.
- [x] Commit and push tap changes if this repo owns the tap or if the tap checkout is available.
  - Pushed `/data/projects/homebrew-tap` commit `946e4dc cass 0.4.6`.
- [x] Verify `brew install` or `brew upgrade` path as far as the local environment permits.
  - Release tarballs/checksums are public and formula syntax is valid; local `brew` binary is unavailable.

## Final Closeout

- [x] Confirm `git status --short --branch`.
- [x] Confirm GitHub release, tag, and assets.
- [x] Confirm crates.io/Homebrew final state or documented blocker.
- [x] Confirm GitHub issue closure state.
- [x] Summarize exact verification commands and results.
