---
access: public
aliases: []
claim_ids:
- clm_01f002ccad709f128c20d8e76a022bf4de710bf2c3dcf7e6dbbd4cd7f497623b
- clm_086878beb276760d53017acaef7a876adbeb9a2921ede887a5300a48d305b0ee
- clm_25a9c90e97437eeace6057b4cf9eff9c1966c897b0083bc0d08e5d4a2f531c3a
- clm_29eea2d0b8fc172a40b75f106fe88d1b9805d203b4c5f10866b53b0463e20f46
- clm_37dd72edb7ff77fa16409f33278ef4fd2cc14c047786447fadf94987699568d3
- clm_39a85315757091b8f90f96c0064af323f82b51da8494cf1c3e9c0bf113d54e5b
- clm_46f8a2c8e41bc20322c3ccfc5636892e23d7e53a929fb431c4769d9dedaadbfe
- clm_606018ccff73eb3a52b0f1ba6137b586272b2be150aa41c46f000666243f298e
- clm_686ae608f1a1c6be186ec338a47ffb07e4bd0fade65f9f11d3b7a8437b6fe547
- clm_90f5959273c8f08623c1822137d41f6797100439a2dfa82863892e24afed75b9
- clm_a598292ae6f0588a3badeba3360062180c7a314b8a22d51c6e1cb80a8ceb3230
- clm_b254f0f0bd9899f20d19f4027df8666b6fb02c289d076b9ff9c52061b15a82b0
- clm_dedda869c28e0ac87601917a6d13b92019398deef61d1ac0f2c33333d32e7a91
- clm_e8a450ba1698a7c2d19ff9764285c6a755c017e0d88f4991aea9b6edc1f0fb57
- clm_f4294712e12296364d70d2264aa6197b6079edadd658b4187cdabcebfb482a8e
- clm_f5029e14e0f2fc6bd0ee8a06f9db566f84d4a6cae870b5bf0a8fff3370926af6
maturity: draft
page_id: pg_1eaf6c0766bd51ce830ff950f53ce5e2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ef241e95b3835eb7839c37b7e4cf6dda
title: aannoo/hcom/README.md @ fabb309b57cb
updated_at: '2026-09-14T01:58:54Z'
---

# aannoo/hcom/README.md @ fabb309b57cb

<!-- rcw:begin owner=source:src_ef241e95b3835eb7839c37b7e4cf6dda block=evidence -->
- Collision detection is on by default: if two agents edit the same file within 30 seconds, both are notified. [@claim:clm_01f002ccad709f128c20d8e76a022bf4de710bf2c3dcf7e6dbbd4cd7f497623b]
- hcom trusts the local user account and ~/.hcom/config.toml and does not defend against another user on the same account or malware with filesystem access. [@claim:clm_086878beb276760d53017acaef7a876adbeb9a2921ede887a5300a48d305b0ee]
- Bundled workflow scripts include `hcom run confess` (honesty self-eval with an independent calibrator and judge), `debate` (judge-coordinated rounds), and `fatcow` (headless file-reading agent); custom *.sh/*.py scripts in ~/.hcom/scripts/ are auto-discovered. [@claim:clm_25a9c90e97437eeace6057b4cf9eff9c1966c897b0083bc0d08e5d4a2f531c3a]
- The CLI includes commands such as hcom send, list, term, events --wait, kill, r (resume), f (fork), config, and a TUI dashboard launched by bare `hcom`. [@claim:clm_29eea2d0b8fc172a40b75f106fe88d1b9805d203b4c5f10866b53b0463e20f46]
- hcom is a CLI that coding agents use to message, watch, and spawn each other across terminals, implemented as a single Rust binary with no background services. [@claim:clm_37dd72edb7ff77fa16409f33278ef4fd2cc14c047786447fadf94987699568d3]
- Repository development practice: building from source uses git clone, cargo build, and cargo test; local builds can be symlinked into ~/.cargo/bin or selected via the dev_root config. [@claim:clm_39a85315757091b8f90f96c0064af323f82b51da8494cf1c3e9c0bf113d54e5b]
- Configuration lives in ~/.hcom/config.toml with precedence defaults < config.toml < env vars, supports per-agent overrides via `hcom config -i`, and per-project isolation via HCOM_DIR. [@claim:clm_46f8a2c8e41bc20322c3ccfc5636892e23d7e53a929fb431c4769d9dedaadbfe]
- Repository development practice: contributors build with cargo build && cargo test, set dev_root to run a local build, and run `just ci` as the local CI gate; the codebase is Rust. [@claim:clm_606018ccff73eb3a52b0f1ba6137b586272b2be150aa41c46f000666243f298e]
- Launch flags include --tag, --terminal, --dir, --headless, --device (remote spawn via relay), --hcom-prompt, and --hcom-system-prompt; unknown flags are forwarded to the underlying tool. [@claim:clm_686ae608f1a1c6be186ec338a47ffb07e4bd0fade65f9f11d3b7a8437b6fe547]
- Cross-device sync uses an MQTT relay with subcommands such as new and connect; relay payloads are end-to-end encrypted with XChaCha20-Poly1305 under a shared PSK. [@claim:clm_90f5959273c8f08623c1822137d41f6797100439a2dfa82863892e24afed75b9]
- Hooks record agent activity to a local SQLite database and deliver messages from it; messages arrive mid-turn between tool calls or wake idle agents. [@claim:clm_a598292ae6f0588a3badeba3360062180c7a314b8a22d51c6e1cb80a8ceb3230]
- Remote config_get/config_set refuse relay_psk, relay_token, relay_id, and the broker URL; the PSK is stored in config.toml with mode 0600 on Unix and kept out of environment variables. [@claim:clm_b254f0f0bd9899f20d19f4027df8666b6fb02c289d076b9ff9c52061b15a82b0]
- Hooks are installed into config dirs under ~/ (or HCOM_DIR) on first run, and hook-less AI tools can join by running `hcom start`. [@claim:clm_dedda869c28e0ac87601917a6d13b92019398deef61d1ac0f2c33333d32e7a91]
- Supported tools include Claude Code, Gemini CLI, Codex, Antigravity, OpenCode, Kilo Code, Pi, Oh My Pi, Cursor, Kimi, and Copilot with automatic message delivery; anything else connects manually via `hcom listen`. [@claim:clm_e8a450ba1698a7c2d19ff9764285c6a755c017e0d88f4991aea9b6edc1f0fb57]
- The relay is a single all-or-nothing trust domain with no scoped roles, read-only peers, or per-device permissions; a leaked PSK cannot be revoked and exposes old captured traffic (no forward secrecy). [@claim:clm_f4294712e12296364d70d2264aa6197b6079edadd658b4187cdabcebfb482a8e]
- Install options include Homebrew (aannoo/hcom/hcom), pip/uv, a shell installer script, and a native PowerShell installer for Windows; `hcom update` upgrades an existing install. [@claim:clm_f5029e14e0f2fc6bd0ee8a06f9db566f84d4a6cae870b5bf0a8fff3370926af6]
<!-- rcw:end owner=source:src_ef241e95b3835eb7839c37b7e4cf6dda block=evidence -->

## Researcher notes

