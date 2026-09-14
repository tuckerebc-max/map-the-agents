---
access: public
aliases: []
claim_ids:
- clm_1f0fac13c7f89852bf6109b57f39634dfd2ddb4b8adc113ccc7a0bfe87ef6a9d
- clm_35f7070ba2428eef907a820b31640903df0103c077af318f1a9e3ffff0d0eced
- clm_4636bfe62efdf8addc4a7db92fc112ad1d4ecda4a158654be2299311c3d9cb00
- clm_476048f0d59cb62abd070a2b74856b98e45db5173bd4060d035a4844c25ce97d
- clm_5355d1f0e93bd81232483b2cca20f51f845da70ea08615528769c32c3f0865b0
- clm_5efad9bcf2d152d0febe7790027312e0f00787ebb4fd927ad66a9d3e67c9c845
- clm_87bef0b0f5dda557a49082947679443347f916c4faf798de0c714c864884fafb
- clm_d4ee9a73e626ce4f71e036b007c7ece3e3233d1ac6f40e12da9f0e8be52a02f6
- clm_e8db7a7c2c4bc2de2eddcb8c56946fbaea75725eb0228aeb8fdeb7ab85771980
- clm_f1d6bd894219c79a39c6f6aaef054f2bccbb9fb0a387112fa3d265ea7862a016
- clm_fc72694a8e04443edc22831421e634b74066792ac51af7b20456b08bb3c9c36b
maturity: draft
page_id: pg_a3bb24015477522886f9efef96290a1c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eb33fc5e2be05c0798af1c255a21efc1
title: jacopone/antigravity-nix/README.md @ 0d6f9760ee4d
updated_at: '2026-09-14T04:00:19Z'
---

# jacopone/antigravity-nix/README.md @ 0d6f9760ee4d

<!-- rcw:begin owner=source:src_eb33fc5e2be05c0798af1c255a21efc1 block=evidence -->
- The flake provides three packages: the Antigravity 2.0 Base App (default), the Antigravity IDE, and the `agy` CLI, with GUI binaries wrapped in an FHS environment. [@claim:clm_1f0fac13c7f89852bf6109b57f39634dfd2ddb4b8adc113ccc7a0bfe87ef6a9d]
- By default GUI apps use the system Chrome profile; a `useSystemChromeProfile = false` override omits `--user-data-dir`/`--profile-directory` flags for an isolated profile, working with both variants. [@claim:clm_35f7070ba2428eef907a820b31640903df0103c077af318f1a9e3ffff0d0eced]
- Packages are runnable via `nix run github:jacopone/antigravity-nix` (default), `#google-antigravity-ide`, and `#google-antigravity-cli`, and installable through NixOS, Home Manager, or an overlay. [@claim:clm_4636bfe62efdf8addc4a7db92fc112ad1d4ecda4a158654be2299311c3d9cb00]
- macOS (darwin) packages evaluate and fetch official builds but are untested; CI verifies Linux only, and GUI apps lack code-signing/quarantine handling so may not launch cleanly. [@claim:clm_476048f0d59cb62abd070a2b74856b98e45db5173bd4060d035a4844c25ce97d]
- GUI packages come in two strategies: a default `buildFHSEnv` + bubblewrap sandbox (which sets `no_new_privileges`, blocking sudo/pkexec) and a `no-fhs` variant using `autoPatchelfHook` without sandboxing. [@claim:clm_5355d1f0e93bd81232483b2cca20f51f845da70ea08615528769c32c3f0865b0]
- A `srcOverride` package option lets users supply a local tarball when fetchurl fails (CDN unreachable, hash drift), bypassing fetchurl while keeping FHS wrapping, Chrome integration, and desktop entry intact. [@claim:clm_5efad9bcf2d152d0febe7790027312e0f00787ebb4fd927ad66a9d3e67c9c845]
- Requirements include Nix with flakes, `allowUnfree = true` since Antigravity is proprietary, and Chromium is used automatically on aarch64-linux where Google Chrome is unavailable. [@claim:clm_87bef0b0f5dda557a49082947679443347f916c4faf798de0c714c864884fafb]
- This is an unofficial MIT-licensed packaging of Google's proprietary Antigravity, not affiliated with or endorsed by Google; the CLI is described as successor to the Gemini CLI. [@claim:clm_d4ee9a73e626ce4f71e036b007c7ece3e3233d1ac6f40e12da9f0e8be52a02f6]
- A daily GitHub Actions workflow (07:00 UTC) checks Google Cloud Run endpoints for new versions, verifies hashes, builds, and opens auto-merge PRs; release and branch-cleanup workflows follow. [@claim:clm_e8db7a7c2c4bc2de2eddcb8c56946fbaea75725eb0228aeb8fdeb7ab85771980]
- Repository development practice: contributors fork, create a feature branch, test with `nix build` and `nix flake check`, and submit a PR; CLAUDE.md adds build, version-update, and workflow-testing checklists. [@claim:clm_f1d6bd894219c79a39c6f6aaef054f2bccbb9fb0a387112fa3d265ea7862a016]
- The Antigravity IDE has a known upstream bug on all Linux distributions where it may freeze the system on close; the documented workaround is force-killing the process after closing the window. [@claim:clm_fc72694a8e04443edc22831421e634b74066792ac51af7b20456b08bb3c9c36b]
<!-- rcw:end owner=source:src_eb33fc5e2be05c0798af1c255a21efc1 block=evidence -->

## Researcher notes

