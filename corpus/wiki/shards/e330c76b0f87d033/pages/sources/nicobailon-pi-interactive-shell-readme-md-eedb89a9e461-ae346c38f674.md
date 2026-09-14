---
access: public
aliases: []
claim_ids:
- clm_074fee30f64bceecf5b2e5c83917cc58bb26a20a47ca2ecd7c8944dcc6eabb63
- clm_2c87f52274ec31bfb8fcc61261fd7d30f4eee95553754ebed60519e9f13cb0ce
- clm_3c9c0a731bac803aa1cd563b081ff32ec90b3ca6afd77f741193c32e839f41a4
- clm_49674c3b4e1baf74032b4badf3ed1990ec5c053b89fa8698a8f450b84323c285
- clm_4e971df15d4055f94e9f1c1a842c03971e817f966d08d111b84f2719ed7a4fa4
- clm_5bd135e3ba8c5868b922e22de54e5891075bbc9d278e993dabe543b05f0a2f59
- clm_5d8555772a36c07ef10408e11a94fba56a15cd188864f5cd7dbb1ac84442a203
- clm_69cb42c1483cd3487995e0efe9bc10b74be112b42a1b396d4e0c857600b4473d
- clm_7367b0209f2dcfe6aeb3e1271efbfcc7170930c9c64079dca0effb754b4aa6dd
- clm_adf54e6f4690db7e13846e00500489c175c3b374dc4a8d8ac1f185b51751daa9
- clm_c2d852a107076826a4d398f6162bdb676474ea38110c6110a27687450522be30
- clm_c91e9785ab38a9075df0b12ba95110d38c57e841fb00f5b0266d9f3e8f5cbe8e
- clm_d790b1ad1adc33da6dc551d3386d6bc8ca4f2d289ae26acd30ea050a16686b6d
- clm_df0a9b46edefb4a0ce689320cfc35b36ee555a17b454ec941136911b51e7aa3e
- clm_ed9c0cf977a6dc33ea7dc07a8fb06c2cb290d8fb658303a44b3ce3e7b8c684f2
- clm_fe6973e4d1a0b30b0a315b5696d76048b124b21c81e61a4dca2cd7fa07a8eed9
maturity: draft
page_id: pg_d7ee6bb1bd485a41a2cfae346c38f674
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_08d8758f0c235db7bc1cdefc998ce549
title: nicobailon/pi-interactive-shell/README.md @ eedb89a9e461
updated_at: '2026-09-14T04:12:52Z'
---

# nicobailon/pi-interactive-shell/README.md @ eedb89a9e461

<!-- rcw:begin owner=source:src_08d8758f0c235db7bc1cdefc998ce549 block=evidence -->
- A `defer: true` config keeps the large tool definition out of the initial model request, exposing a small `enable_interactive_shell` loader instead; slash commands and shortcuts still work directly. [@claim:clm_074fee30f64bceecf5b2e5c83917cc58bb26a20a47ca2ecd7c8944dcc6eabb63]
- Dispatch defaults autoExitOnQuiet with a 15s startup grace period and 8s silence threshold; both are configurable per-call or globally via autoExitGracePeriod. [@claim:clm_2c87f52274ec31bfb8fcc61261fd7d30f4eee95553754ebed60519e9f13cb0ce]
- Monitor mode wakes the agent on configured trigger events (stream, poll-diff, or file-watch strategies) with structured payloads, plus lifecycle notifications when the monitor stops. [@claim:clm_3c9c0a731bac803aa1cd563b081ff32ec90b3ca6afd77f741193c32e839f41a4]
- Structured spawn params can launch coding agents (pi, codex, claude, cursor) with prompts, worktree isolation, and a Pi-only fork mode; extra spawn.commands keys become first-class custom agents. [@claim:clm_49674c3b4e1baf74032b4badf3ed1990ec5c053b89fa8698a8f450b84323c285]
- Repository development practice: the README's example workflow templates are opt-in user-facing prompts to copy into agent config, not contributor contribution rules; no contributor/CI guidance appears in the provided slices. [@claim:clm_4e971df15d4055f94e9f1c1a842c03971e817f966d08d111b84f2719ed7a4fa4]
- Sessions return a stable sessionId; the agent can send input with submit, named keys, bracketed paste, or raw hex bytes, and query status/output. [@claim:clm_5bd135e3ba8c5868b922e22de54e5891075bbc9d278e993dabe543b05f0a2f59]
- The extension exposes an `interactive_shell` tool for the Pi coding agent; end users do not call it directly but ask Pi in natural language or use /spawn, /attach, /dismiss commands. [@claim:clm_5d8555772a36c07ef10408e11a94fba56a15cd188864f5cd7dbb1ac84442a203]
- New sessions use Pi's Bash resolver rather than ambient $SHELL/COMSPEC; on Windows it discovers Git Bash, and legacy WSL stdin-only bash is rejected for interactive PTYs. [@claim:clm_69cb42c1483cd3487995e0efe9bc10b74be112b42a1b396d4e0c857600b4473d]
- The tool supports four modes: interactive (default), hands-free, dispatch, and monitor, all returning immediately without the agent waiting. [@claim:clm_7367b0209f2dcfe6aeb3e1271efbfcc7170930c9c64079dca0effb754b4aa6dd]
- Documented limitations: macOS tested with Linux experimental, a 60-second rate limit between agent queries (configurable), and possible rendering quirks in some TUI apps. [@claim:clm_adf54e6f4690db7e13846e00500489c175c3b374dc4a8d8ac1f185b51751daa9]
- Architecture: interactive_shell routes through zigpty to the subprocess, with xterm-headless terminal emulation feeding a TUI overlay rendered by Pi; the subprocess gets a full PTY. [@claim:clm_c2d852a107076826a4d398f6162bdb676474ea38110c6110a27687450522be30]
- Dispatch mode notifies the agent via triggerTurn on completion with a 5-line output tail; the PTY is preserved for 5 minutes so the agent can attach and review scrollback. [@claim:clm_c91e9785ab38a9075df0b12ba95110d38c57e841fb00f5b0266d9f3e8f5cbe8e]
- Sessions can be backgrounded by user (Ctrl+B/Ctrl+Q) or agent, listed via listBackground, reattached with a chosen mode, and dismissed individually or all at once. [@claim:clm_d790b1ad1adc33da6dc551d3386d6bc8ca4f2d289ae26acd30ea050a16686b6d]
- Output queries default to 20 lines/5KB, support up to 200 lines, incremental pagination, and a raw drain mode. [@claim:clm_df0a9b46edefb4a0ce689320cfc35b36ee555a17b454ec941136911b51e7aa3e]
- Installation symlinks an interactive-shell skill into ~/.pi/agent/skills/, and optional example skills (codex-cli, cursor-cli, prompting skills) and prompt templates ship under examples/ for opt-in copy. [@claim:clm_ed9c0cf977a6dc33ea7dc07a8fb06c2cb290d8fb658303a44b3ce3e7b8c684f2]
- Requires Node.js; PTY support uses prebuilt zigpty binaries, so no node-gyp toolchain is needed on supported platforms. [@claim:clm_fe6973e4d1a0b30b0a315b5696d76048b124b21c81e61a4dca2cd7fa07a8eed9]
<!-- rcw:end owner=source:src_08d8758f0c235db7bc1cdefc998ce549 block=evidence -->

## Researcher notes

