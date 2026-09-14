# aannoo/hcom -- full detail

[Back to orientation](hcom.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aannoo/hcom/fabb309b57cb33b39c69b773cd759723a10e94b5/66e9c15eec3dd6cb.json](../../../wiki/dossiers/aannoo/hcom/fabb309b57cb33b39c69b773cd759723a10e94b5/66e9c15eec3dd6cb.json)

## specifications (1 claim(s))

- [observation/documented] hcom is a CLI that coding agents use to message, watch, and spawn each other across terminals, implemented as a single Rust binary with no background services. -- evidence: [README.md#L9-L9](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L9-L9), [README.md#L15-L15](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L15-L15) (`clm_37dd72edb7ff77fa16409f33278ef4fd2cc14c047786447fadf94987699568d3`)

## components (5 claim(s))

- [observation/documented] Hooks record agent activity to a local SQLite database and deliver messages from it; messages arrive mid-turn between tool calls or wake idle agents. -- evidence: [README.md#L97-L97](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L97-L97), [README.md#L103-L103](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L103-L103) (`clm_a598292ae6f0588a3badeba3360062180c7a314b8a22d51c6e1cb80a8ceb3230`)
- [observation/documented] Hooks are installed into config dirs under ~/ (or HCOM_DIR) on first run, and hook-less AI tools can join by running `hcom start`. -- evidence: [README.md#L116-L116](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L116-L116), [README.md#L114-L114](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L114-L114) (`clm_dedda869c28e0ac87601917a6d13b92019398deef61d1ac0f2c33333d32e7a91`)
- [observation/documented] Cross-device sync uses an MQTT relay with subcommands such as new and connect; relay payloads are end-to-end encrypted with XChaCha20-Poly1305 under a shared PSK. -- evidence: [README.md#L136-L139](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L136-L139), [README.md#L134-L134](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L134-L134), [README.md#L160-L160](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L160-L160) (`clm_90f5959273c8f08623c1822137d41f6797100439a2dfa82863892e24afed75b9`)
- [observation/code-inspected] The relay command implementation parses --broker and --password flags, pings brokers over TCP/TLS, and derives relay health states (connected, starting, stale, waiting, error) from a shared RelayHealth type. -- evidence: [src/commands/relay.rs#L20-L39](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/src/commands/relay.rs#L20-L39), [src/commands/relay.rs#L41-L45](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/src/commands/relay.rs#L41-L45), [src/commands/relay.rs#L148-L197](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/src/commands/relay.rs#L148-L197) (`clm_4146b20f4d3b8b612adbebad9cfcb6be6f99753dbfbce39a85929787c7711a8b`)
- [observation/code-inspected] Join tokens encode relay_id and broker URL and always carry a PSK (v0x04); legacy PSK-less tokens are rejected by relay_connect, and status shows only a key fingerprint. -- evidence: [src/commands/relay.rs#L334-L340](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/src/commands/relay.rs#L334-L340), [src/commands/relay.rs#L55-L60](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/src/commands/relay.rs#L55-L60), [src/commands/relay.rs#L62-L66](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/src/commands/relay.rs#L62-L66) (`clm_852977b1e6615537e33b5cf81dca6d38365ce2fc233fc5f3e75cc80ed3ab156f`)

## design-choices (1 claim(s))

- [observation/documented] Collision detection is on by default: if two agents edit the same file within 30 seconds, both are notified. -- evidence: [README.md#L112-L112](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L112-L112) (`clm_01f002ccad709f128c20d8e76a022bf4de710bf2c3dcf7e6dbbd4cd7f497623b`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors build with cargo build && cargo test, set dev_root to run a local build, and run `just ci` as the local CI gate; the codebase is Rust. -- evidence: [README.md#L432-L432](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L432-L432), [README.md#L434-L439](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L434-L439) (`clm_606018ccff73eb3a52b0f1ba6137b586272b2be150aa41c46f000666243f298e`)
- [observation/documented] Repository development practice: building from source uses git clone, cargo build, and cargo test; local builds can be symlinked into ~/.cargo/bin or selected via the dev_root config. -- evidence: [README.md#L395-L399](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L395-L399), [README.md#L407-L409](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L407-L409), [README.md#L413-L417](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L413-L417) (`clm_39a85315757091b8f90f96c0064af323f82b51da8494cf1c3e9c0bf113d54e5b`)

## skills-patterns (1 claim(s))

- [observation/documented] Bundled workflow scripts include `hcom run confess` (honesty self-eval with an independent calibrator and judge), `debate` (judge-coordinated rounds), and `fatcow` (headless file-reading agent); custom *.sh/*.py scripts in ~/.hcom/scripts/ are auto-discovered. -- evidence: [README.md#L381-L381](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L381-L381), [README.md#L383-L383](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L383-L383), [README.md#L377-L377](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L377-L377), [README.md#L379-L379](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L379-L379) (`clm_25a9c90e97437eeace6057b4cf9eff9c1966c897b0083bc0d08e5d4a2f531c3a`)

## interfaces (3 claim(s))

- [observation/documented] The CLI includes commands such as hcom send, list, term, events --wait, kill, r (resume), f (fork), config, and a TUI dashboard launched by bare `hcom`. -- evidence: [README.md#L272-L277](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L272-L277), [README.md#L295-L302](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L295-L302) (`clm_29eea2d0b8fc172a40b75f106fe88d1b9805d203b4c5f10866b53b0463e20f46`)
- [observation/documented] Launch flags include --tag, --terminal, --dir, --headless, --device (remote spawn via relay), --hcom-prompt, and --hcom-system-prompt; unknown flags are forwarded to the underlying tool. -- evidence: [README.md#L281-L289](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L281-L289), [README.md#L291-L291](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L291-L291) (`clm_686ae608f1a1c6be186ec338a47ffb07e4bd0fade65f9f11d3b7a8437b6fe547`)
- [observation/documented] Configuration lives in ~/.hcom/config.toml with precedence defaults < config.toml < env vars, supports per-agent overrides via `hcom config -i`, and per-project isolation via HCOM_DIR. -- evidence: [README.md#L349-L352](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L349-L352), [README.md#L315-L321](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L315-L321), [README.md#L313-L313](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L313-L313) (`clm_46f8a2c8e41bc20322c3ccfc5636892e23d7e53a929fb431c4769d9dedaadbfe`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Remote config_get/config_set refuse relay_psk, relay_token, relay_id, and the broker URL; the PSK is stored in config.toml with mode 0600 on Unix and kept out of environment variables. -- evidence: [README.md#L183-L183](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L183-L183), [README.md#L181-L181](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L181-L181) (`clm_b254f0f0bd9899f20d19f4027df8666b6fb02c289d076b9ff9c52061b15a82b0`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Supported tools include Claude Code, Gemini CLI, Codex, Antigravity, OpenCode, Kilo Code, Pi, Oh My Pi, Cursor, Kimi, and Copilot with automatic message delivery; anything else connects manually via `hcom listen`. -- evidence: [README.md#L227-L240](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L227-L240) (`clm_e8a450ba1698a7c2d19ff9764285c6a755c017e0d88f4991aea9b6edc1f0fb57`)
- [observation/documented] Install options include Homebrew (aannoo/hcom/hcom), pip/uv, a shell installer script, and a native PowerShell installer for Windows; `hcom update` upgrades an existing install. -- evidence: [README.md#L23-L25](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L23-L25), [README.md#L46-L47](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L46-L47), [README.md#L41-L42](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L41-L42), [README.md#L31-L32](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L31-L32), [README.md#L36-L37](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L36-L37) (`clm_f5029e14e0f2fc6bd0ee8a06f9db566f84d4a6cae870b5bf0a8fff3370926af6`)

## limitations (2 claim(s))

- [observation/documented] The relay is a single all-or-nothing trust domain with no scoped roles, read-only peers, or per-device permissions; a leaked PSK cannot be revoked and exposes old captured traffic (no forward secrecy). -- evidence: [README.md#L174-L177](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L174-L177), [README.md#L158-L158](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L158-L158), [README.md#L191-L191](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L191-L191) (`clm_f4294712e12296364d70d2264aa6197b6079edadd658b4187cdabcebfb482a8e`)
- [observation/documented] hcom trusts the local user account and ~/.hcom/config.toml and does not defend against another user on the same account or malware with filesystem access. -- evidence: [README.md#L174-L177](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L174-L177) (`clm_086878beb276760d53017acaef7a876adbeb9a2921ede887a5300a48d305b0ee`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

