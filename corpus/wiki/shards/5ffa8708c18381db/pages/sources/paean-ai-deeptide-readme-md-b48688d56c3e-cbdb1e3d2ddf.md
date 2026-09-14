---
access: public
aliases: []
claim_ids:
- clm_12194fbe820b2259db492dff0cda5274c345046a191e1856f1c72fd122ae9cf3
- clm_27f327dd6ad63736d4f211e373dc56b9262582e4f758a197116465eb937f0994
- clm_7755b96dec60b4b49e49995c580fe658e22ab47a352fddafd92f12cda2e81bc4
- clm_79dc8dd248488e7e39470c24db26e8b3275730bed49b959ebc07f3762c2c0ffe
- clm_7bb767a79497261e7693acccbdb0945fa970c7d4369ee76b1af5b27a8de53732
- clm_857bfcda8b534e951d3bd382dba190f8be110c8190368fa36037245476f53e94
- clm_95bc9a895857b64e8407fb3617264079e97ace343941401fb16e001dd3ca7e22
- clm_aa2f60178a1f2bd60e3f20d90c41b240a59054fac10e3a737aa0bee7a8fa7e16
- clm_f14462c48b03ff756a5d8f9f3b761451c8cea55dc97931676973ed9b8f104857
maturity: draft
page_id: pg_482d0d814bf0598e9727cbdb1e3d2ddf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_494442f144e9507ca69f92e0f116cfbc
title: paean-ai/deeptide/README.md @ b48688d56c3e
updated_at: '2026-09-14T02:28:52Z'
---

# paean-ai/deeptide/README.md @ b48688d56c3e

<!-- rcw:begin owner=source:src_494442f144e9507ca69f92e0f116cfbc block=evidence -->
- DeepTide is an agentic coding assistant in which the model plans, calls tools, observes results, and adapts; it ships as a macOS native app, a cross-platform Bun CLI, and a Rust CLI with an optional desktop GUI. [@claim:clm_12194fbe820b2259db492dff0cda5274c345046a191e1856f1c72fd122ae9cf3]
- Repository development practice: contributors build the Rust GUI from the crates/ workspace with cargo run/build -p deeptide-gui, build native components with npm run build:ds4 / build:dsgo, and report security vulnerabilities via private vulnerability reporting, redacting sensitive data from logs. [@claim:clm_27f327dd6ad63736d4f211e373dc56b9262582e4f758a197116465eb937f0994]
- The repository also contains a native local inference runtime under native/: a hard-forked ds4 DeepSeek V4 Flash Metal engine and dsgo, an OpenAI/Anthropic-compatible local gateway, built via npm run build:native on macOS. [@claim:clm_7755b96dec60b4b49e49995c580fe658e22ab47a352fddafd92f12cda2e81bc4]
- The CLI installs `deeptide` and `tide` commands supporting an interactive REPL, one-shot mode via `-p`, `--base-url`/`--api-key` for BYOK providers, `tide auth login`, and `tide doctor` diagnostics. [@claim:clm_79dc8dd248488e7e39470c24db26e8b3275730bed49b959ebc07f3762c2c0ffe]
- The product offers 30+ built-in tools (file I/O, shell, web, tasks, MCP, scheduling, sub-agents), 25+ slash commands, and four permission modes: default, accept-edits, plan, and bypass. [@claim:clm_7bb767a79497261e7693acccbdb0945fa970c7d4369ee76b1af5b27a8de53732]
- The repo hosts two npm packages: `deeptide`, a thin redirect to @paean-ai/zero-cli, and `deeptide-rs`, which ships a native Rust binary via GitHub Releases postinstall; the Rust port lives under crates/. [@claim:clm_857bfcda8b534e951d3bd382dba190f8be110c8190368fa36037245476f53e94]
- DeepTide includes a persistent project memory system across sessions, and GUI and CLI conversations share the same on-disk session store so chats started in either can be resumed in the other. [@claim:clm_95bc9a895857b64e8407fb3617264079e97ace343941401fb16e001dd3ca7e22]
- The Rust GUI shares the CLI's configuration (~/.config/tide/settings.json and project .deeptide/settings.json), on-disk session store resumable via `--resume`, and full tool set; it is launched with `deeptide-rs --gui` or the `deeptide-gui` binary. [@claim:clm_aa2f60178a1f2bd60e3f20d90c41b240a59054fac10e3a737aa0bee7a8fa7e16]
- The cross-platform CLI requires Bun installed and on PATH at runtime (even when installed via npm), matching its underlying Zero CLI engine; Bun sits alongside Node rather than replacing it. [@claim:clm_f14462c48b03ff756a5d8f9f3b761451c8cea55dc97931676973ed9b8f104857]
<!-- rcw:end owner=source:src_494442f144e9507ca69f92e0f116cfbc block=evidence -->

## Researcher notes

