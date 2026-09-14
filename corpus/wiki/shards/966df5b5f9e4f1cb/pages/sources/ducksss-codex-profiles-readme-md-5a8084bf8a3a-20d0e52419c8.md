---
access: public
aliases: []
claim_ids:
- clm_1d3d37944a9a4dad2d2ca9f3a88528ce45f18beff46a40e384be9a2e376b6f28
- clm_47b39d0ba69be4f8423713ecdc48992e04c1bd68d5e3534109889f194ca1d7a9
- clm_6cc76ea236a81e7f87a9c7b02224983ae390c13acb0fe94cc105f26ff30a41b8
- clm_927d02ad5a8e4edc5170e94819acfe5bc9dcdfaa5923881bd104e9b9c758cde6
- clm_92a19bdf503e03dbdf0e66439ea4297bbe355af6a01e23c30d4481cfd8da3a77
- clm_a3b2f69fb1896faca299c689d3a14010d2cd3521f153ba3a3f5a9284256f90ed
- clm_d460a1787f8ec9bce381627583d0067c1b41d34802ca86000983d00433f23bc7
- clm_e749ca8a51eaee584b966fb2e9fc4824c812e2702e70ca39e2a2f5fa0a58c146
maturity: draft
page_id: pg_f04213f172635ae5b3ba20d0e52419c8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dd79c0d5699a52d0b24066bca296ce55
title: Ducksss/codex-profiles/README.md @ 5a8084bf8a3a
updated_at: '2026-09-14T03:49:01Z'
---

# Ducksss/codex-profiles/README.md @ 5a8084bf8a3a

<!-- rcw:begin owner=source:src_dd79c0d5699a52d0b24066bca296ce55 block=evidence -->
- The project states local-state separation is not an account, OS, or server-side security boundary; OS credentials, network, keychain, and other tool credentials remain shared or outside its control. [@claim:clm_1d3d37944a9a4dad2d2ca9f3a88528ce45f18beff46a40e384be9a2e376b6f28]
- The tool does not verify that CLI and Desktop sign-ins use the same account, and does not change or inspect server-side ChatGPT workspaces, policies, histories, or plans. [@claim:clm_47b39d0ba69be4f8423713ecdc48992e04c1bd68d5e3534109889f194ca1d7a9]
- The tool is described as a single Bash script with no runtime dependencies beyond standard system tools; it requires Bash and a working upstream Codex CLI, and does not install Codex itself. [@claim:clm_6cc76ea236a81e7f87a9c7b02224983ae390c13acb0fe94cc105f26ff30a41b8]
- Profile selection maps the name 'default' to ~/.codex and any other name <x> to ~/.codex-<x>, so each profile gets its own Codex home. [@claim:clm_927d02ad5a8e4edc5170e94819acfe5bc9dcdfaa5923881bd104e9b9c758cde6]
- CLI commands work on macOS and Linux, but the app and launcher create commands require macOS. [@claim:clm_92a19bdf503e03dbdf0e66439ea4297bbe355af6a01e23c30d4481cfd8da3a77]
- Repository development practice: contributors are pointed to a contributor guide and coding-agent instructions; there is no build step, and the README instructs running 'make check' as the complete local gate before submitting changes. [@claim:clm_a3b2f69fb1896faca299c689d3a14010d2cd3521f153ba3a3f5a9284256f90ed]
- The tool exposes a CLI with commands including setup, init, login, cli, app, run, list, status, doctor, path, shell-init, workspace bind, launcher create, env, and detach. [@claim:clm_d460a1787f8ec9bce381627583d0067c1b41d34802ca86000983d00433f23bc7]
- init --share-with links only a fixed allowlist of configuration entries (config.toml, AGENTS.md, instructions.md, rules/, plugins/, etc.) while auth.json, sessions, and Electron data stay per-profile; the tool never reads or copies authentication tokens or cookies. [@claim:clm_e749ca8a51eaee584b966fb2e9fc4824c812e2702e70ca39e2a2f5fa0a58c146]
<!-- rcw:end owner=source:src_dd79c0d5699a52d0b24066bca296ce55 block=evidence -->

## Researcher notes

