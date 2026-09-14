# jacopone/antigravity-nix

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0d6f9760ee4d @ 29a598b1659b814e

## Summary (orientation draft, not independently verified)

antigravity-nix is an auto-updating Nix flake packaging Google Antigravity 2.0 (Base App, IDE, CLI) for Linux and experimental macOS, with FHS/no-FHS variants, version pinning, and a daily GitHub Actions update pipeline.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The flake provides three packages: the Antigravity 2.0 Base App (default), the Antigravity IDE, and the `agy` CLI, with GUI binaries wrapped in an FHS environment. -- evidence: [README.md#L11-L15](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L11-L15), [CLAUDE.md#L15-L18](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L15-L18)
- design-choices (2 claim(s)):
  - [observation/documented] GUI packages come in two strategies: a default `buildFHSEnv` + bubblewrap sandbox (which sets `no_new_privileges`, blocking sudo/pkexec) and a `no-fhs` variant using `autoPatchelfHook` without sandboxing. -- evidence: [README.md#L127-L130](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L127-L130), [README.md#L134-L134](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L134-L134), [README.md#L132-L132](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L132-L132)
  - [observation/documented] By default GUI apps use the system Chrome profile; a `useSystemChromeProfile = false` override omits `--user-data-dir`/`--profile-directory` flags for an isolated profile, working with both variants. -- evidence: [README.md#L153-L155](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L153-L155), [README.md#L157-L157](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L157-L157), [README.md#L151-L151](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L151-L151)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, create a feature branch, test with `nix build` and `nix flake check`, and submit a PR; CLAUDE.md adds build, version-update, and workflow-testing checklists. -- evidence: [README.md#L222-L225](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L222-L225), [CLAUDE.md#L51-L51](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L51-L51), [CLAUDE.md#L67-L68](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L67-L68), [CLAUDE.md#L118-L118](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L118-L118), [CLAUDE.md#L138-L139](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L138-L139), [CLAUDE.md#L64-L64](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L64-L64), [CLAUDE.md#L43-L43](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L43-L43)
  - [observation/documented] Repository development practice: hashes in `artifacts/versions.json` must be real SRI hashes obtained via `nix-prefetch-url` and `nix hash to-sri`; placeholder hashes fail CI before reaching users. -- evidence: [CLAUDE.md#L87-L87](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L87-L87), [CLAUDE.md#L93-L93](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L93-L93), [CLAUDE.md#L89-L91](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L89-L91)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Packages are runnable via `nix run github:jacopone/antigravity-nix` (default), `#google-antigravity-ide`, and `#google-antigravity-cli`, and installable through NixOS, Home Manager, or an overlay. -- evidence: [README.md#L109-L113](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L109-L113), [README.md#L60-L75](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L60-L75), [README.md#L39-L42](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L39-L42), [README.md#L90-L105](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L90-L105), [README.md#L29-L32](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L29-L32), [README.md#L34-L37](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L34-L37)
  - [observation/documented] A `srcOverride` package option lets users supply a local tarball when fetchurl fails (CDN unreachable, hash drift), bypassing fetchurl while keeping FHS wrapping, Chrome integration, and desktop entry intact. -- evidence: [README.md#L208-L208](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L208-L208), [README.md#L202-L206](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L202-L206), [README.md#L197-L197](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L197-L197)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A daily GitHub Actions workflow (07:00 UTC) checks Google Cloud Run endpoints for new versions, verifies hashes, builds, and opens auto-merge PRs; release and branch-cleanup workflows follow. -- evidence: [README.md#L11-L15](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L11-L15), [CLAUDE.md#L31-L31](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L31-L31), [CLAUDE.md#L108-L110](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L108-L110), [CLAUDE.md#L33-L35](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L33-L35)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Requirements include Nix with flakes, `allowUnfree = true` since Antigravity is proprietary, and Chromium is used automatically on aarch64-linux where Google Chrome is unavailable. -- evidence: [README.md#L212-L214](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L212-L214)
- limitations (2 claim(s)):
More evidence: [full detail](antigravity-nix.detail.md)

Metadata and full claim list: [full detail](antigravity-nix.detail.md)
Human notes ([notes](antigravity-nix.notes.md), never overwritten by build)

[Back to map index](../../index.md)
