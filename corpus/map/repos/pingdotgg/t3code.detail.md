# pingdotgg/t3code -- full detail

[Back to orientation](t3code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pingdotgg/t3code/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/9b65991334d57d26.json](../../../wiki/dossiers/pingdotgg/t3code/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/9b65991334d57d26.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The project charges nothing for the product and states it aims to be performant, remote-ready, and open enough that users can fork and build their own editor. -- evidence: [README.md#L11-L11](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L11-L11), [README.md#L9-L9](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L9-L9) (`clm_f654f61bea6cd3c806d7085c4563465f094f8acecc114e9b31f4151746ebf036`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: AGENTS.md forbids killing processes by name/path matching, forbids starting servers against or writing to the live ~/.t3/userdata database, and forbids setting VITE_HTTP_URL/VITE_WS_URL in dev because Vite proxies /api, /ws, /oauth, and /.well-known. -- evidence: [AGENTS.md#L61-L63](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/AGENTS.md#L61-L63) (`clm_21c6581f38a29aa5ddaa97430425b0326517ea7485a8c3e357aaa150b2dc2583`)
- [observation/documented] Repository development practice: agents must never open a PR unless the developer explicitly asks; PRs use conventional-commit titles, one concern per PR, before/after images for UI changes, and evidence uploaded to GitHub rather than committed. -- evidence: [AGENTS.md#L115-L121](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/AGENTS.md#L115-L121) (`clm_d5b2b4134a6b5dd9ec3222f3cc9fe8550bc87ad39ddf5c511a70c21578b55ab7`)
- [observation/documented] Repository development practice: verification uses targeted `vp test run` on touched files plus scoped lint/typecheck; repo-wide checks like `vp check` are reserved for CI, and tests must wait on typed receipts rather than sleeps or timeouts. -- evidence: [AGENTS.md#L106-L111](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/AGENTS.md#L106-L111) (`clm_434357f4a42766d3350f3bc159773965380f148534972aebbff6fd38da314547`)
- [observation/documented] Repository development practice: PRs are auto-labeled with a vouch:* trust status and size:* diff size, and external contributors should expect vouch:unvouched until added to .github/VOUCHED.td. -- evidence: [CONTRIBUTING.md#L18-L18](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/CONTRIBUTING.md#L18-L18), [CONTRIBUTING.md#L20-L20](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/CONTRIBUTING.md#L20-L20) (`clm_a0a60fa0bcb1f555103d525de3cced06616a10cfdc658a1661e0bd2332c81a1f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] T3 Code lets users control coding agents remotely through an iOS app, Android app, web app, and an Electron-based desktop app. -- evidence: [README.md#L3-L3](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L3-L3) (`clm_56216ed74264ad1203570acd775ac246facc74a89f9ffb826afb5979b8062800`)
- [observation/documented] Running `npx t3@latest` launches the T3 Code backend on the local machine plus a local web app for controlling agents; a `--help` flag exposes the full CLI reference. -- evidence: [README.md#L35-L35](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L35-L35), [README.md#L33-L33](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L33-L33), [README.md#L29-L31](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L29-L31) (`clm_367ea2af261c8f52680fdfb981124361c6ced9fbf1ce390fc00f91e4c1cddcd6`)
- [observation/documented] The install-free server mode requires Node.js 22.16+, 23.11+, or 24.10+. -- evidence: [README.md#L27-L27](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L27-L27) (`clm_e8c4185acbf2aaa06a34f53a4d82017e1b0ef100debb00a923b0907c3b550169`)
- [observation/documented] The desktop app is distributed via GitHub Releases and package registries including winget (T3Tools.T3Code), Homebrew cask t3-code, and AUR packages for both stable and nightly builds. -- evidence: [README.md#L63-L65](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L63-L65), [README.md#L49-L51](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L49-L51), [README.md#L43-L45](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L43-L45), [README.md#L39-L39](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L39-L39), [README.md#L57-L59](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L57-L59) (`clm_5d183be87510a17766de246b4015947eeb2d86f103231fe7efb8103634ce1d88`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The product works with existing subscriptions to Claude Code, Codex, Cursor, Grok Build, OpenCode, and Google Antigravity, controlling those agents when set up on the user's computer. -- evidence: [README.md#L5-L5](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L5-L5) (`clm_a90ec8c4f5a55439ecb62a29a8960a915bda536db9df6524c074f5abfb3c5a11`)
- [observation/documented] At least one provider must be installed and authenticated before use; each provider names a CLI and login command, while Antigravity is enabled in Settings with Google sign-in and needs no CLI. -- evidence: [README.md#L15-L23](https://github.com/pingdotgg/t3code/blob/66e39ca2aabde054bc50312a9c34f05dbd1f6f9e/README.md#L15-L23) (`clm_c506279bb5c893287914e4cd0173e9cb6bf7032827dc32809f4e5d070cb634ad`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

