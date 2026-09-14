# GOssip Release Tooling (goreleaser + homebrew) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tag push `v*` → GitHub Actions → goreleaser builds darwin/linux binaries, creates the GitHub release, and publishes a formula to `2389-research/homebrew-tap`; ends with v0.1.0 live and `brew install 2389-research/tap/gossip` working.

**Architecture:** One new code seam (a `version` var stamped via ldflags, exposed as cobra's `--version`), plus declarative config: `.goreleaser.yaml` (build matrix + brew formula publication) and `.github/workflows/release.yml` (tag-triggered runner). Everything else is docs (LICENSE, README).

**Tech Stack:** Go 1.26 / cobra v1.10, goreleaser v2 (2.17.0 verified locally), GitHub Actions, existing tap repo `2389-research/homebrew-tap`.

**Spec:** `docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md`

## Global Constraints

- All `.go` files start with two `// ABOUTME:` lines; YAML files in this repo carry two `# ABOUTME:` lines (see `.github/workflows/ci.yml`).
- Canonical gate is `./scripts/check` (gofmt, vet, test). Run it before every commit.
- Conventional commits, imperative mood, present tense. Never bypass hooks.
- Module path: `github.com/2389-research/gossip`. Binary: `gossip` from `./cmd/gossip`.
- House release pattern (from `2389-research/tracker`): goreleaser v2, `CGO_ENABLED=0`, goos `darwin,linux` × goarch `amd64,arm64`, tar.gz, brew formula pushed to `2389-research/homebrew-tap` `Formula/` with token env `HOMEBREW_TAP_TOKEN`, commit author goreleaserbot.
- The `brews` stanza is deprecated in goreleaser v2.x in favor of `homebrew_casks`, but it is what the entire tap uses (tracker published with it 2026-07-14 on `version: latest`). Use `brews`; a deprecation NOTICE in goreleaser output is expected and acceptable. An ERROR is not.
- Action pins match this repo's `ci.yml`: `actions/checkout@v6`, `actions/setup-go@v6` (NOT tracker's older v4/v5). goreleaser action: `goreleaser/goreleaser-action@v6`.
- No Windows builds, no nfpm, no `version` subcommand (cobra's `--version` flag only), no homebrew-core.

---

### Task 1: `--version` flag stamped at release time

**Files:**
- Modify: `cmd/gossip/main.go` (add `version` var)
- Modify: `cmd/gossip/commands.go:69-75` (set `Version` on root command)
- Test: `cmd/gossip/cli_test.go`

**Interfaces:**
- Consumes: `runCLI(t, env, now, args...)` test helper already in `cmd/gossip/cli_test.go:18`.
- Produces: package-level `var version = "dev"` in package `main` — goreleaser stamps it via `-X main.version={{ .Version }}` (Task 3), and the brew formula test runs `gossip --version` (Task 3).

- [x] **Step 1: Write the failing test**

Append to `cmd/gossip/cli_test.go`:

```go
func TestVersionFlag(t *testing.T) {
	now := time.Date(2026, 7, 16, 3, 0, 0, 0, time.UTC)
	out, err := runCLI(t, nil, now, "--version")
	if err != nil {
		t.Fatalf("--version: %v\n%s", err, out)
	}
	want := "gossip version " + version
	if !strings.Contains(out, want) {
		t.Fatalf("version output missing %q:\n%s", want, out)
	}
}
```

(Passing `nil` for env is safe: reads from a nil map return `""`.)

- [x] **Step 2: Run test to verify it fails**

Run: `go test ./cmd/gossip/ -run TestVersionFlag -v`
Expected: FAIL — compile error `undefined: version`. Fix nothing yet; if instead you add only the var and re-run, it fails with `unknown flag: --version` (cobra only registers the flag when `Version` is set). Both failure modes are the test doing its job.

- [x] **Step 3: Write minimal implementation**

In `cmd/gossip/main.go`, after the `import` block:

```go
// version is stamped by goreleaser at release time via -X main.version=.
var version = "dev"
```

In `cmd/gossip/commands.go`, add one field to the root command literal (lines 69-75):

```go
	root := &cobra.Command{
		Use:           "gossip",
		Short:         "Share gossip at the agentic watercooler",
		Long:          "GOssip: labeled, decaying, evidence-badged hearsay in a shared SQLite file.\nIdentity is DECLARED via GOSSIP_ACTOR_ID/GOSSIP_PRINCIPAL_ID, not authenticated.",
		Version:       version,
		SilenceUsage:  true,
		SilenceErrors: true,
	}
```

- [x] **Step 4: Run test to verify it passes**

Run: `go test ./cmd/gossip/ -run TestVersionFlag -v`
Expected: PASS (cobra prints `gossip version dev` to the command's out writer).

- [x] **Step 5: Run the canonical gate**

Run: `./scripts/check`
Expected: `check: OK`

- [x] **Step 6: Commit**

```bash
git add cmd/gossip/main.go cmd/gossip/commands.go cmd/gossip/cli_test.go
git commit -m "feat: add --version flag stamped at release time"
```

---

### Task 2: LICENSE and README install section

**Files:**
- Create: `LICENSE`
- Modify: `README.md` (new "Install" section between "Retry scope" and "Use")

**Interfaces:**
- Consumes: nothing.
- Produces: `LICENSE` (MIT) — the formula's `license: MIT` field (Task 3) must match it.

- [x] **Step 1: Create LICENSE**

Create `LICENSE` (no ABOUTME lines — license files are verbatim legal text):

```text
MIT License

Copyright (c) 2026 2389 Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [x] **Step 2: Add README install section**

In `README.md`, insert between the "Retry scope" section and the "Use" section:

```markdown
## Install

    brew install 2389-research/tap/gossip

Or with Go:

    go install github.com/2389-research/gossip/cmd/gossip@latest
```

- [x] **Step 3: Verify the gate still passes**

Run: `./scripts/check`
Expected: `check: OK` (docs-only change; this guards against accidental code edits).

- [x] **Step 4: Commit**

```bash
git add LICENSE README.md
git commit -m "docs: add MIT license and install instructions"
```

---

### Task 3: goreleaser config + local snapshot verification

**Files:**
- Create: `.goreleaser.yaml`
- Modify: `.gitignore` (add `dist/`)

**Interfaces:**
- Consumes: `version` var from Task 1 (ldflags `-X main.version={{ .Version }}`); `LICENSE` from Task 2 (`license: MIT`); `./scripts/check` as before-hook.
- Produces: build id/archive consumed by the release workflow (Task 4) via `goreleaser release --clean`; env contract `HOMEBREW_TAP_TOKEN` consumed by Task 4/5.

- [x] **Step 1: Create `.goreleaser.yaml`**

```yaml
# ABOUTME: GoReleaser config: builds gossip for darwin/linux and cuts GitHub releases.
# ABOUTME: Publishes the brew formula to 2389-research/homebrew-tap on tagged releases.
version: 2

project_name: gossip

before:
  hooks:
    - go mod tidy
    - ./scripts/check

builds:
  - binary: gossip
    main: ./cmd/gossip
    env:
      - CGO_ENABLED=0
    goos:
      - darwin
      - linux
    goarch:
      - amd64
      - arm64
    ldflags:
      - -s -w -X main.version={{ .Version }}

archives:
  - formats: [tar.gz]
    name_template: >-
      {{ .ProjectName }}_
      {{- .Version }}_
      {{- .Os }}_
      {{- .Arch }}

brews:
  - repository:
      owner: 2389-research
      name: homebrew-tap
      token: "{{ .Env.HOMEBREW_TAP_TOKEN }}"
    directory: Formula
    homepage: https://github.com/2389-research/gossip
    description: "Labeled, decaying, evidence-badged hearsay in a shared SQLite file"
    license: MIT
    commit_author:
      name: goreleaserbot
      email: bot@goreleaser.com
    install: |
      bin.install "gossip"
    test: |
      system "#{bin}/gossip", "--version"

checksum:
  name_template: checksums.txt

snapshot:
  version_template: "{{ incpatch .Version }}-next"

changelog:
  sort: asc
  groups:
    - title: Features
      regexp: '^feat'
    - title: Fixes
      regexp: '^fix'
    - title: Other
      order: 999
```

- [x] **Step 2: Add `dist/` to `.gitignore`**

Append this line to `.gitignore`:

```text
dist/
```

- [x] **Step 3: Validate the config**

Run: `goreleaser check`
Expected: exit 0, "1 configuration file(s) validated". A DEPRECATION notice about `brews` is expected and acceptable (house style — see Global Constraints). Any ERROR means fix the config before proceeding.

- [x] **Step 4: Snapshot build (no publish)**

Run: `goreleaser release --snapshot --clean --skip=publish`
Expected: exit 0; `dist/` contains 4 binaries (darwin/linux × amd64/arm64), 4 tar.gz archives, and `checksums.txt`. The `before` hooks run `go mod tidy` + `./scripts/check` first — if the gate fails, the build fails (intended).

- [x] **Step 5: Smoke-test the built binary**

Run: `./dist/gossip_darwin_arm64*/gossip --version`
Expected: `gossip version 0.0.1-next` (no tags exist yet, so goreleaser bases the snapshot on v0.0.0 and `incpatch` yields `0.0.1-next`). This proves ldflags injection works end to end.

Also confirm `git status` shows no tracked-file changes from the build (only the ignored `dist/`); if `go mod tidy` changed `go.mod`/`go.sum`, include those changes in the commit and say so.

- [x] **Step 6: Commit**

```bash
git add .goreleaser.yaml .gitignore
git commit -m "build: add goreleaser config publishing to 2389-research homebrew tap"
```

---

### Task 4: release workflow

**Files:**
- Create: `.github/workflows/release.yml`

**Interfaces:**
- Consumes: `.goreleaser.yaml` from Task 3; repo secret `HOMEBREW_TAP_TOKEN` (set by Doctor Biz in Task 5); built-in `GITHUB_TOKEN`.
- Produces: tag-triggered release automation used in Task 5.

- [x] **Step 1: Create `.github/workflows/release.yml`**

```yaml
# ABOUTME: GitHub Actions release workflow for GOssip — goreleaser on v* tag pushes.
# ABOUTME: Publishes GitHub releases and the brew formula to 2389-research/homebrew-tap.

name: release

on:
  push:
    tags:
      - "v*"

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - uses: actions/setup-go@v6
        with:
          go-version-file: go.mod
      - uses: goreleaser/goreleaser-action@v6
        with:
          distribution: goreleaser
          version: latest
          args: release --clean
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          HOMEBREW_TAP_TOKEN: ${{ secrets.HOMEBREW_TAP_TOKEN }}
```

(`fetch-depth: 0` because goreleaser needs full history + tags for the changelog. `contents: write` lets `GITHUB_TOKEN` create the release; the tap push uses `HOMEBREW_TAP_TOKEN` because `GITHUB_TOKEN` cannot write to other repos.)

- [x] **Step 2: Lint the workflow**

Run: `actionlint .github/workflows/release.yml`
Expected: exit 0, no output.

- [x] **Step 3: Commit**

```bash
git add .github/workflows/release.yml
git commit -m "ci: add tag-triggered release workflow running goreleaser"
```

---

### Task 5: land on main, set secret, cut v0.1.0, verify end to end

This task has a HUMAN GATE (step 3) and must run in the orchestrating session, not a subagent — it needs Doctor Biz and the releasing-software skill.

**Files:**
- None created; operates on git remotes, GitHub, and the tap.

**Interfaces:**
- Consumes: everything from Tasks 1-4, merged to `main`.
- Produces: git tag `v0.1.0`, GitHub release `v0.1.0` (4 archives + checksums.txt), `Formula/gossip.rb` in `2389-research/homebrew-tap`, installed `gossip` binary via brew.

- [x] **Step 1: Push branch and open PR**

```bash
git push -u origin release-tooling
gh pr create --title "build: goreleaser + homebrew release tooling" --body "Implements docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md: --version flag, MIT LICENSE, goreleaser config publishing to 2389-research/homebrew-tap, tag-triggered release workflow."
```

- [x] **Step 2: Wait for CI, then merge**

Run: `gh pr checks --watch`
Expected: `ci` check passes.

```bash
gh pr merge --rebase --delete-branch
git checkout main && git pull
```

(If GitHub rejects `--rebase` because the repo's merge settings disallow it, use `gh pr merge --merge --delete-branch` instead and say so.)

- [x] **Step 3: HUMAN GATE — Doctor Biz sets the tap token**

Doctor Biz runs (with the same PAT tracker uses — needs write access to `2389-research/homebrew-tap`):

```bash
gh secret set HOMEBREW_TAP_TOKEN -R 2389-research/gossip
```

Verify before proceeding: `gh secret list -R 2389-research/gossip` must show `HOMEBREW_TAP_TOKEN`. Do NOT tag until it does — goreleaser would create the GitHub release and then fail at the tap push, leaving a half-published release.

- [x] **Step 4: Tag and push v0.1.0**

Invoke the releasing-software skill for this step (it governs pre-tag verification). Then, from up-to-date `main`:

```bash
git tag v0.1.0
git push origin v0.1.0
```

- [x] **Step 5: Watch the release workflow**

Run: `gh run watch $(gh run list --workflow=release --limit 1 --json databaseId --jq '.[0].databaseId')`
Expected: job `release` succeeds. On failure: read the log (`gh run view --log-failed`), fix the root cause; if the release half-published, delete the GitHub release and tag (`gh release delete v0.1.0 --yes && git push --delete origin v0.1.0 && git tag -d v0.1.0`) before re-tagging.

- [x] **Step 6: Verify the artifacts**

```bash
gh release view v0.1.0 --json assets --jq '.assets[].name'
gh api repos/2389-research/homebrew-tap/contents/Formula/gossip.rb --jq '.name'
```

Expected: 4 `gossip_0.1.0_*.tar.gz` assets + `checksums.txt`; `gossip.rb` exists in the tap.

- [x] **Step 7: End-to-end proof**

```bash
brew install 2389-research/tap/gossip
gossip --version
```

Expected: `gossip version 0.1.0`. (If a locally built `gossip` shadows the brew one on PATH, run `$(brew --prefix)/bin/gossip --version` to disambiguate.)

- [x] **Step 8: Record the release**

Log the release in chronicle (activity log) and update the plan checkboxes. No code commit needed unless files changed.
