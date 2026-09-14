# GOssip release tooling: goreleaser + homebrew tap

**Date:** 2026-07-16
**Status:** Approved by Doctor Biz
**Outcome:** Tag push `v*` → GitHub Actions → goreleaser builds binaries, creates the
GitHub release, and publishes a formula to `2389-research/homebrew-tap`. This task ends
with v0.1.0 actually released and installable via
`brew install 2389-research/tap/gossip`.

## Context

- Module `github.com/2389-research/gossip`; remote `git@github.com:2389-research/gossip.git`; no tags yet.
- Single binary at `./cmd/gossip` (cobra). Pure-Go SQLite (`modernc.org/sqlite`), so `CGO_ENABLED=0` cross-compiles cleanly.
- `2389-research/homebrew-tap` already exists (public, 18 formulas, all goreleaser-generated). House pattern taken from `2389-research/tracker`.
- `HOMEBREW_TAP_TOKEN` is a repo-level secret on tracker; gossip has no repo secrets yet. Secrets are not readable, so Doctor Biz must set it on gossip manually.
- Existing CI (`.github/workflows/ci.yml`) uses ubuntu-latest, `actions/checkout@v6`, `actions/setup-go@v6` — release workflow matches these, not tracker's older pins.
- Canonical verification is `./scripts/check` (gofmt, vet, test).

## Non-goals (YAGNI)

- No Windows builds, no nfpm (deb/rpm), no homebrew-core submission, no signing/notarization.
- No `version` subcommand — cobra's built-in `--version` flag only.

## Components

### 1. Version plumbing (only code change; TDD)

- `var version = "dev"` declared in package `main` (`cmd/gossip/main.go`).
- `newRootCmd` (`cmd/gossip/commands.go`) sets `Version: version` on the root command.
  Cobra then provides `gossip --version` → `gossip version dev` (or the injected value).
- Goreleaser injects the real value via ldflags `-X main.version={{.Version}}`.
- Failing test first (`cmd/gossip/cli_test.go` pattern): execute root with `--version`,
  assert output contains the version string.

### 2. LICENSE

- MIT, copyright 2026 "2389 Research". Standard text, repo root.

### 3. `.goreleaser.yaml`

Version 2 config, single build (simplified from tracker's two-binary layout):

- `project_name: gossip`
- `before.hooks`: `go mod tidy`, `./scripts/check`
- build: `main: ./cmd/gossip`, `binary: gossip`, `CGO_ENABLED=0`,
  goos `darwin, linux` × goarch `amd64, arm64`,
  ldflags `-s -w -X main.version={{.Version}}`
- archive: tar.gz, `name_template: gossip_{{ .Version }}_{{ .Os }}_{{ .Arch }}`
- `brews`: repository `2389-research/homebrew-tap`, `directory: Formula`,
  token `{{ .Env.HOMEBREW_TAP_TOKEN }}`,
  homepage `https://github.com/2389-research/gossip`,
  description "Labeled, decaying, evidence-badged hearsay in a shared SQLite file",
  license MIT, commit author goreleaserbot,
  `install: bin.install "gossip"`, `test: system "#{bin}/gossip", "--version"`
- `checksum.name_template: checksums.txt`
- snapshot template `{{ incpatch .Version }}-next`
- changelog groups: feat → Features, fix → Fixes, everything else → Other

### 4. `.github/workflows/release.yml`

- Trigger: push of tags matching `v*`. `permissions: contents: write`.
- ubuntu-latest; `actions/checkout@v6` with `fetch-depth: 0`;
  `actions/setup-go@v6` with `go-version-file: go.mod` and cache;
  `goreleaser/goreleaser-action@v6`, `args: release --clean`;
  env `GITHUB_TOKEN` (built-in) + `HOMEBREW_TAP_TOKEN` (repo secret).
- Two `# ABOUTME:` comment lines at top, matching ci.yml style.

### 5. README install section

Short "Install" section: `brew install 2389-research/tap/gossip`, plus `go install`
as the alternative.

## Verification (before tagging)

1. `./scripts/check` green.
2. `goreleaser check` passes.
3. `goreleaser release --snapshot --clean --skip=publish` builds all four binaries;
   run one and confirm `--version` prints the injected snapshot version.

## Release procedure (after tooling lands on main)

1. **Doctor Biz (manual):** `gh secret set HOMEBREW_TAP_TOKEN -R 2389-research/gossip`
   using the same PAT tracker uses (needs write access to homebrew-tap).
2. Tag `v0.1.0`, push the tag (releasing-software skill governs this step).
3. Watch the release workflow; verify the GitHub release exists with 4 archives +
   checksums, and `Formula/gossip.rb` lands in the tap.
4. End-to-end proof: `brew install 2389-research/tap/gossip && gossip --version`.

## Failure modes considered

- Missing/insufficient `HOMEBREW_TAP_TOKEN` → goreleaser fails at publish after the
  GitHub release exists. Recovery: fix secret, delete release + tag, re-tag (or
  `goreleaser release` locally). Mitigated by setting the secret before tagging.
- `scripts/check` failing inside the workflow blocks the release — intended behavior.
