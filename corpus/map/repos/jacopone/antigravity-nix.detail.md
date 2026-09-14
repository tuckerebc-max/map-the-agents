# jacopone/antigravity-nix -- full detail

[Back to orientation](antigravity-nix.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jacopone/antigravity-nix/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/29a598b1659b814e.json](../../../wiki/dossiers/jacopone/antigravity-nix/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/29a598b1659b814e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The flake provides three packages: the Antigravity 2.0 Base App (default), the Antigravity IDE, and the `agy` CLI, with GUI binaries wrapped in an FHS environment. -- evidence: [README.md#L11-L15](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L11-L15), [CLAUDE.md#L15-L18](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L15-L18) (`clm_1f0fac13c7f89852bf6109b57f39634dfd2ddb4b8adc113ccc7a0bfe87ef6a9d`)

## design-choices (2 claim(s))

- [observation/documented] GUI packages come in two strategies: a default `buildFHSEnv` + bubblewrap sandbox (which sets `no_new_privileges`, blocking sudo/pkexec) and a `no-fhs` variant using `autoPatchelfHook` without sandboxing. -- evidence: [README.md#L127-L130](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L127-L130), [README.md#L134-L134](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L134-L134), [README.md#L132-L132](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L132-L132) (`clm_5355d1f0e93bd81232483b2cca20f51f845da70ea08615528769c32c3f0865b0`)
- [observation/documented] By default GUI apps use the system Chrome profile; a `useSystemChromeProfile = false` override omits `--user-data-dir`/`--profile-directory` flags for an isolated profile, working with both variants. -- evidence: [README.md#L153-L155](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L153-L155), [README.md#L157-L157](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L157-L157), [README.md#L151-L151](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L151-L151) (`clm_35f7070ba2428eef907a820b31640903df0103c077af318f1a9e3ffff0d0eced`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork, create a feature branch, test with `nix build` and `nix flake check`, and submit a PR; CLAUDE.md adds build, version-update, and workflow-testing checklists. -- evidence: [README.md#L222-L225](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L222-L225), [CLAUDE.md#L51-L51](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L51-L51), [CLAUDE.md#L67-L68](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L67-L68), [CLAUDE.md#L118-L118](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L118-L118), [CLAUDE.md#L138-L139](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L138-L139), [CLAUDE.md#L64-L64](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L64-L64), [CLAUDE.md#L43-L43](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L43-L43) (`clm_f1d6bd894219c79a39c6f6aaef054f2bccbb9fb0a387112fa3d265ea7862a016`)
- [observation/documented] Repository development practice: hashes in `artifacts/versions.json` must be real SRI hashes obtained via `nix-prefetch-url` and `nix hash to-sri`; placeholder hashes fail CI before reaching users. -- evidence: [CLAUDE.md#L87-L87](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L87-L87), [CLAUDE.md#L93-L93](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L93-L93), [CLAUDE.md#L89-L91](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L89-L91) (`clm_a13609ffb8e96fe43912f5298ebef616c01b55b35ba7fb3a9e6667df47103a0b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Packages are runnable via `nix run github:jacopone/antigravity-nix` (default), `#google-antigravity-ide`, and `#google-antigravity-cli`, and installable through NixOS, Home Manager, or an overlay. -- evidence: [README.md#L109-L113](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L109-L113), [README.md#L60-L75](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L60-L75), [README.md#L39-L42](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L39-L42), [README.md#L90-L105](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L90-L105), [README.md#L29-L32](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L29-L32), [README.md#L34-L37](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L34-L37) (`clm_4636bfe62efdf8addc4a7db92fc112ad1d4ecda4a158654be2299311c3d9cb00`)
- [observation/documented] A `srcOverride` package option lets users supply a local tarball when fetchurl fails (CDN unreachable, hash drift), bypassing fetchurl while keeping FHS wrapping, Chrome integration, and desktop entry intact. -- evidence: [README.md#L208-L208](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L208-L208), [README.md#L202-L206](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L202-L206), [README.md#L197-L197](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L197-L197) (`clm_5efad9bcf2d152d0febe7790027312e0f00787ebb4fd927ad66a9d3e67c9c845`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A daily GitHub Actions workflow (07:00 UTC) checks Google Cloud Run endpoints for new versions, verifies hashes, builds, and opens auto-merge PRs; release and branch-cleanup workflows follow. -- evidence: [README.md#L11-L15](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L11-L15), [CLAUDE.md#L31-L31](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L31-L31), [CLAUDE.md#L108-L110](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L108-L110), [CLAUDE.md#L33-L35](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/CLAUDE.md#L33-L35) (`clm_e8db7a7c2c4bc2de2eddcb8c56946fbaea75725eb0228aeb8fdeb7ab85771980`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements include Nix with flakes, `allowUnfree = true` since Antigravity is proprietary, and Chromium is used automatically on aarch64-linux where Google Chrome is unavailable. -- evidence: [README.md#L212-L214](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L212-L214) (`clm_87bef0b0f5dda557a49082947679443347f916c4faf798de0c714c864884fafb`)

## limitations (2 claim(s))

- [observation/documented] macOS (darwin) packages evaluate and fetch official builds but are untested; CI verifies Linux only, and GUI apps lack code-signing/quarantine handling so may not launch cleanly. -- evidence: [README.md#L11-L15](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L11-L15), [README.md#L218-L218](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L218-L218) (`clm_476048f0d59cb62abd070a2b74856b98e45db5173bd4060d035a4844c25ce97d`)
- [observation/documented] The Antigravity IDE has a known upstream bug on all Linux distributions where it may freeze the system on close; the documented workaround is force-killing the process after closing the window. -- evidence: [README.md#L189-L189](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L189-L189), [README.md#L191-L193](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L191-L193) (`clm_fc72694a8e04443edc22831421e634b74066792ac51af7b20456b08bb3c9c36b`)

## relevance (1 claim(s))

- [observation/documented] This is an unofficial MIT-licensed packaging of Google's proprietary Antigravity, not affiliated with or endorsed by Google; the CLI is described as successor to the Gemini CLI. -- evidence: [README.md#L231-L231](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L231-L231), [README.md#L229-L229](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L229-L229), [README.md#L21-L23](https://github.com/jacopone/antigravity-nix/blob/0d6f9760ee4d685c6e75faeafb5055b93c4bc4aa/README.md#L21-L23) (`clm_d4ee9a73e626ce4f71e036b007c7ece3e3233d1ac6f40e12da9f0e8be52a02f6`)

