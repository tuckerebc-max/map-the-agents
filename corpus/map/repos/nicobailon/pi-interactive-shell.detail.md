# nicobailon/pi-interactive-shell -- full detail

[Back to orientation](pi-interactive-shell.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nicobailon/pi-interactive-shell/eedb89a9e4618d7416326d9387085a756a2125ee/8fd72b37ae0f9648.json](../../../wiki/dossiers/nicobailon/pi-interactive-shell/eedb89a9e4618d7416326d9387085a756a2125ee/8fd72b37ae0f9648.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Architecture: interactive_shell routes through zigpty to the subprocess, with xterm-headless terminal emulation feeding a TUI overlay rendered by Pi; the subprocess gets a full PTY. -- evidence: [README.md#L556-L556](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L556-L556), [README.md#L548-L554](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L548-L554) (`clm_c2d852a107076826a4d398f6162bdb676474ea38110c6110a27687450522be30`)

## design-choices (2 claim(s))

- [observation/documented] New sessions use Pi's Bash resolver rather than ambient $SHELL/COMSPEC; on Windows it discovers Git Bash, and legacy WSL stdin-only bash is rejected for interactive PTYs. -- evidence: [README.md#L442-L446](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L442-L446), [README.md#L457-L462](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L457-L462), [CHANGELOG.md#L15-L17](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/CHANGELOG.md#L15-L17) (`clm_69cb42c1483cd3487995e0efe9bc10b74be112b42a1b396d4e0c857600b4473d`)
- [observation/documented] Dispatch defaults autoExitOnQuiet with a 15s startup grace period and 8s silence threshold; both are configurable per-call or globally via autoExitGracePeriod. -- evidence: [README.md#L156-L156](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L156-L156), [README.md#L295-L295](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L295-L295), [README.md#L305-L305](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L305-L305) (`clm_2c87f52274ec31bfb8fcc61261fd7d30f4eee95553754ebed60519e9f13cb0ce`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's example workflow templates are opt-in user-facing prompts to copy into agent config, not contributor contribution rules; no contributor/CI guidance appears in the provided slices. -- evidence: [README.md#L582-L582](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L582-L582) (`clm_4e971df15d4055f94e9f1c1a842c03971e817f966d08d111b84f2719ed7a4fa4`)

## skills-patterns (1 claim(s))

- [observation/documented] Installation symlinks an interactive-shell skill into ~/.pi/agent/skills/, and optional example skills (codex-cli, cursor-cli, prompting skills) and prompt templates ship under examples/ for opt-in copy. -- evidence: [README.md#L594-L595](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L594-L595), [README.md#L582-L582](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L582-L582), [README.md#L589-L591](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L589-L591), [README.md#L33-L33](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L33-L33), [README.md#L86-L86](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L86-L86) (`clm_ed9c0cf977a6dc33ea7dc07a8fb06c2cb290d8fb658303a44b3ce3e7b8c684f2`)

## interfaces (5 claim(s))

- [observation/documented] The extension exposes an `interactive_shell` tool for the Pi coding agent; end users do not call it directly but ask Pi in natural language or use /spawn, /attach, /dismiss commands. -- evidence: [README.md#L15-L15](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L15-L15), [README.md#L7-L7](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L7-L7) (`clm_5d8555772a36c07ef10408e11a94fba56a15cd188864f5cd7dbb1ac84442a203`)
- [observation/documented] The tool supports four modes: interactive (default), hands-free, dispatch, and monitor, all returning immediately without the agent waiting. -- evidence: [README.md#L39-L44](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L39-L44) (`clm_7367b0209f2dcfe6aeb3e1271efbfcc7170930c9c64079dca0effb754b4aa6dd`)
- [observation/documented] Sessions return a stable sessionId; the agent can send input with submit, named keys, bracketed paste, or raw hex bytes, and query status/output. -- evidence: [README.md#L318-L320](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L318-L320), [README.md#L311-L313](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L311-L313), [README.md#L101-L101](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L101-L101), [README.md#L322-L323](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L322-L323), [README.md#L325-L326](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L325-L326) (`clm_5bd135e3ba8c5868b922e22de54e5891075bbc9d278e993dabe543b05f0a2f59`)
- [observation/documented] Output queries default to 20 lines/5KB, support up to 200 lines, incremental pagination, and a raw drain mode. -- evidence: [README.md#L340-L341](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L340-L341), [README.md#L336-L338](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L336-L338), [README.md#L343-L344](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L343-L344), [README.md#L346-L348](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L346-L348) (`clm_df0a9b46edefb4a0ce689320cfc35b36ee555a17b454ec941136911b51e7aa3e`)
- [observation/documented] A `defer: true` config keeps the large tool definition out of the initial model request, exposing a small `enable_interactive_shell` loader instead; slash commands and shortcuts still work directly. -- evidence: [README.md#L420-L420](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L420-L420), [README.md#L428-L428](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L428-L428) (`clm_074fee30f64bceecf5b2e5c83917cc58bb26a20a47ca2ecd7c8944dcc6eabb63`)

## memory-state (1 claim(s))

- [observation/documented] Sessions can be backgrounded by user (Ctrl+B/Ctrl+Q) or agent, listed via listBackground, reattached with a chosen mode, and dismissed individually or all at once. -- evidence: [README.md#L370-L370](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L370-L370), [README.md#L385-L388](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L385-L388), [README.md#L377-L378](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L377-L378), [README.md#L380-L383](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L380-L383) (`clm_d790b1ad1adc33da6dc551d3386d6bc8ca4f2d289ae26acd30ea050a16686b6d`)

## orchestration (3 claim(s))

- [observation/documented] Dispatch mode notifies the agent via triggerTurn on completion with a 5-line output tail; the PTY is preserved for 5 minutes so the agent can attach and review scrollback. -- evidence: [README.md#L50-L50](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L50-L50), [README.md#L154-L154](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L154-L154) (`clm_c91e9785ab38a9075df0b12ba95110d38c57e841fb00f5b0266d9f3e8f5cbe8e`)
- [observation/documented] Monitor mode wakes the agent on configured trigger events (stream, poll-diff, or file-watch strategies) with structured payloads, plus lifecycle notifications when the monitor stops. -- evidence: [README.md#L203-L217](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L203-L217), [README.md#L246-L255](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L246-L255), [README.md#L257-L257](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L257-L257), [README.md#L219-L228](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L219-L228), [README.md#L52-L52](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L52-L52) (`clm_3c9c0a731bac803aa1cd563b081ff32ec90b3ca6afd77f741193c32e839f41a4`)
- [observation/documented] Structured spawn params can launch coding agents (pi, codex, claude, cursor) with prompts, worktree isolation, and a Pi-only fork mode; extra spawn.commands keys become first-class custom agents. -- evidence: [README.md#L78-L80](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L78-L80), [README.md#L75-L76](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L75-L76), [README.md#L84-L84](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L84-L84), [README.md#L60-L60](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L60-L60), [README.md#L66-L67](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L66-L67) (`clm_49674c3b4e1baf74032b4badf3ed1990ec5c053b89fa8698a8f450b84323c285`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requires Node.js; PTY support uses prebuilt zigpty binaries, so no node-gyp toolchain is needed on supported platforms. -- evidence: [README.md#L35-L35](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L35-L35) (`clm_fe6973e4d1a0b30b0a315b5696d76048b124b21c81e61a4dca2cd7fa07a8eed9`)

## limitations (1 claim(s))

- [observation/documented] Documented limitations: macOS tested with Linux experimental, a 60-second rate limit between agent queries (configurable), and possible rendering quirks in some TUI apps. -- evidence: [README.md#L653-L655](https://github.com/nicobailon/pi-interactive-shell/blob/eedb89a9e4618d7416326d9387085a756a2125ee/README.md#L653-L655) (`clm_adf54e6f4690db7e13846e00500489c175c3b374dc4a8d8ac1f185b51751daa9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

