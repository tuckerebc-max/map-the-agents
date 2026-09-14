---
access: public
aliases: []
claim_ids:
- clm_0f0a755eeb5c2d671f665b20821b2f7e79f5893373d55de6ae4a30ec4efca252
- clm_1d3d37944a9a4dad2d2ca9f3a88528ce45f18beff46a40e384be9a2e376b6f28
- clm_47b39d0ba69be4f8423713ecdc48992e04c1bd68d5e3534109889f194ca1d7a9
- clm_5cae3c65513751e7ecb2aac094d699c95a7da37e5cc5227c18ced9c46871fa06
- clm_736af6f8f0fbb86328234119a715ed4f034224e12a0b2bf18630d677d641fee9
- clm_8280cb2416789a2dcb3962829abfd0f3c4c68e7cdb5a009e79afd8b4fcb28712
- clm_927d02ad5a8e4edc5170e94819acfe5bc9dcdfaa5923881bd104e9b9c758cde6
- clm_c9215aa4dc531c6a0aac96aae0e6fa696f64252bf080a8f03be13cd9e28e7f89
- clm_d460a1787f8ec9bce381627583d0067c1b41d34802ca86000983d00433f23bc7
- clm_e749ca8a51eaee584b966fb2e9fc4824c812e2702e70ca39e2a2f5fa0a58c146
maturity: draft
page_id: pg_be55e5c66bbf506d809ca02f4b301ee3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dcd44452d4db5c80b50d8129e610e8fe
title: Ducksss/codex-profiles/docs/llms.txt @ 5a8084bf8a3a
updated_at: '2026-09-14T03:49:01Z'
---

# Ducksss/codex-profiles/docs/llms.txt @ 5a8084bf8a3a

<!-- rcw:begin owner=source:src_dcd44452d4db5c80b50d8129e610e8fe block=evidence -->
- shell-init prints shell code for bash/zsh/fish that enables 'use <profile>' in the current shell, with optional --prompt and --completions; it never edits shell startup files. [@claim:clm_0f0a755eeb5c2d671f665b20821b2f7e79f5893373d55de6ae4a30ec4efca252]
- The project states local-state separation is not an account, OS, or server-side security boundary; OS credentials, network, keychain, and other tool credentials remain shared or outside its control. [@claim:clm_1d3d37944a9a4dad2d2ca9f3a88528ce45f18beff46a40e384be9a2e376b6f28]
- The tool does not verify that CLI and Desktop sign-ins use the same account, and does not change or inspect server-side ChatGPT workspaces, policies, histories, or plans. [@claim:clm_47b39d0ba69be4f8423713ecdc48992e04c1bd68d5e3534109889f194ca1d7a9]
- The project recommends itself for people using multiple Codex contexts who want separate Codex homes or named ChatGPT windows with separate local state on macOS, without copying authentication files. [@claim:clm_5cae3c65513751e7ecb2aac094d699c95a7da37e5cc5227c18ced9c46871fa06]
- A workspace guard defaults to warn mode; strict mode rejects mismatched cli, env/use, and app selections before side effects, and off disables checks. [@claim:clm_736af6f8f0fbb86328234119a715ed4f034224e12a0b2bf18630d677d641fee9]
- launcher create builds a small unsigned macOS app in ~/Applications (overridable via CODEX_PROFILE_LAUNCHER_ROOT) that calls codex-profile app <profile>, with named/color-coded identities and list/path/remove subcommands. [@claim:clm_8280cb2416789a2dcb3962829abfd0f3c4c68e7cdb5a009e79afd8b4fcb28712]
- Profile selection maps the name 'default' to ~/.codex and any other name <x> to ~/.codex-<x>, so each profile gets its own Codex home. [@claim:clm_927d02ad5a8e4edc5170e94819acfe5bc9dcdfaa5923881bd104e9b9c758cde6]
- Workspace bindings store only a canonical path and profile name under ${XDG_CONFIG_HOME:-~/.config}/codex-profile with private permissions, relocatable via CODEX_PROFILE_CONFIG_HOME; nested bindings override ancestors. [@claim:clm_c9215aa4dc531c6a0aac96aae0e6fa696f64252bf080a8f03be13cd9e28e7f89]
- The tool exposes a CLI with commands including setup, init, login, cli, app, run, list, status, doctor, path, shell-init, workspace bind, launcher create, env, and detach. [@claim:clm_d460a1787f8ec9bce381627583d0067c1b41d34802ca86000983d00433f23bc7]
- init --share-with links only a fixed allowlist of configuration entries (config.toml, AGENTS.md, instructions.md, rules/, plugins/, etc.) while auth.json, sessions, and Electron data stay per-profile; the tool never reads or copies authentication tokens or cookies. [@claim:clm_e749ca8a51eaee584b966fb2e9fc4824c812e2702e70ca39e2a2f5fa0a58c146]
<!-- rcw:end owner=source:src_dcd44452d4db5c80b50d8129e610e8fe block=evidence -->

## Researcher notes

