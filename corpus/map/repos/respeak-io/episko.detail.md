# respeak-io/episko -- full detail

[Back to orientation](episko.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/respeak-io/episko/974192b540db99dd89b2c29adc7e154c1ac287c0/4ce3ea1d5573290e.json](../../../wiki/dossiers/respeak-io/episko/974192b540db99dd89b2c29adc7e154c1ac287c0/4ce3ea1d5573290e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The app is built on Tauri v2 with a Rust backend and system WebView frontend, uses portable-pty for PTYs (forkpty on macOS, ConPTY on Windows), tiny_http as a localhost telemetry receiver, and xterm.js for terminal rendering. -- evidence: [README.md#L69-L73](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L69-L73) (`clm_f723a986601aab63a03fdc1f1d0673b3deb16cf23fb23408fb86a3e98396b525`)

## design-choices (1 claim(s))

- [observation/documented] Task discovery never executes the project: just --dump, task --list and mise tasks ls sit behind a trust gate, Makefiles are parsed statically, and tasks that cannot run are shown greyed with the reason rather than hidden. -- evidence: [README.md#L53-L55](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L53-L55) (`clm_02a67e5fbd8668710ef87e77d6a7f37949cf8271012baeaaa6a29ba1a0cc7255`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: CI runs on every push and PR to dev/main on both macOS and Windows, covering strict tsc typecheck, vitest suites (~1,535 it blocks), cargo check/test --locked (~270 #[test] functions) and clippy with -D warnings. -- evidence: [RELEASE.md#L17-L22](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L17-L22), [RELEASE.md#L15-L15](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L15-L15) (`clm_ea76b3cd23d31bb7c1bd2f03431942a813d45aae3a2ed963f18ed0290a1ef2fb`)
- [observation/documented] Repository development practice: ignored cargo contract tests against real Claude Code (instrumentation, permission modes, temp-dir layout) are run manually via cargo test -- --ignored because CI lacks claude on PATH; one of them spends tokens and needs authentication. -- evidence: [RELEASE.md#L54-L57](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L54-L57), [RELEASE.md#L61-L82](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L61-L82) (`clm_f91685431e1d62c25b8b3b80a97ba9903b98796c4b53200736b3eeef2492cb50`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Episko gives each coding-agent session its own real terminal; Claude Code and Codex are first-class integrated providers, while other installed CLIs work through a terminal-only adapter pane. -- evidence: [README.md#L5-L5](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L5-L5) (`clm_2dcc3989d0b6b40663e797f5005a2a58a72f5c14f8a00c44668b7b263e68a213`)
- [observation/documented] The app discovers and runs tasks the project already ships — .episko/tasks.toml, .vscode/tasks.json and launch.json, package.json scripts, justfile, Taskfile.yml, mise.toml, Makefile, Cargo.toml — in the same PTY panes as agent sessions. -- evidence: [README.md#L43-L43](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L43-L43), [README.md#L45-L45](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L45-L45) (`clm_3fc01ec2cf3f6d16e7e7d84b6c7883a00215834cb8cdad4775c380061ee79393`)
- [observation/documented] Each project gets a dashboard with per-day commit and session summaries, issues with triage suggestions, GitHub claims that mark an issue as taken by an agent, and worktree checkouts; feature depth degrades for plain git repos and bare folders. -- evidence: [README.md#L34-L37](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L34-L37), [README.md#L39-L39](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L39-L39) (`clm_a6b21826e31b91d28a20606c7db0ad041f1309935f98c49d0766efa6068f5a83`)
- [observation/documented] The app detects external Claude sessions started outside Episko and shows them as read-only mirrors in the sidebar, and can jump to the terminal tab or window hosting such a session. -- evidence: [RELEASE.md#L460-L467](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L460-L467) (`clm_f0ead2dfe1eb6f65a6454b29a6307f741f7cd1533a730aa3dea386e76c6535bc`)

## memory-state (1 claim(s))

- [observation/documented] Personal preferences go to localStorage while project facts go to .episko/tasks.toml, described as the only file the app writes, edited via toml_edit so comments and ordering survive; shared digests and notes can be committed as .episko/digest.md and .episko/notes.toml. -- evidence: [README.md#L34-L37](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L34-L37), [README.md#L53-L55](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L53-L55) (`clm_68b982be134a8e8f6e2c67f9ad093146411768073c38a57ca7321ec7be2855b5`)

## orchestration (2 claim(s))

- [observation/documented] On each Claude launch the app writes a throwaway --settings file whose statusLine command and lifecycle hooks POST to a tiny_http server on an ephemeral localhost port; Codex launches use a loopback App Server, and both transports feed one provider-neutral event reducer. -- evidence: [README.md#L61-L61](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L61-L61) (`clm_e49b74051b68b59b2510320f15ea466d3feb96182df10ee601e2eb6e1d9226fe`)
- [observation/documented] Telemetry POSTs are tagged with a launch id so events route to the correct pane, and routing survives /clear, /compact and /resume, each of which makes Claude mint a new runtime session_id; the permission hook is a blocking call held open until answered. -- evidence: [README.md#L63-L63](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L63-L63) (`clm_58d49cb0f4bbf07aa2f5bbceb66c3bb570d386c58df373e7437011bad4b2d702`)

## tools-permissions (1 claim(s))

- [observation/documented] When Claude or Codex requests to run something, the app surfaces the command with a risk read and lets the user allow, deny, or hand it to the terminal; starting permission/sandbox policy is stored per integrated agent. -- evidence: [README.md#L13-L28](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L13-L28) (`clm_5fdb4a55b5f93b8e54ab4685d3897a0a1f243dcb65affd7316d34188af16d0ca`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building from source requires Node.js 18+, pnpm, stable Rust with Tauri system dependencies, and at least one supported coding-agent CLI on PATH. -- evidence: [README.md#L103-L105](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L103-L105) (`clm_5166c510d594cfebe5ac17cd5ea67ddfbf4a3f819e189c51f5806b84a072ea55`)

## limitations (1 claim(s))

- [observation/documented] Release builds target Apple-silicon macOS and Windows x64; Intel Macs are not covered and Linux is not packaged. The macOS build is self-signed but not notarized, so Gatekeeper quarantines the download and users must clear the quarantine flag before opening. -- evidence: [README.md#L81-L81](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L81-L81), [README.md#L137-L137](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L137-L137) (`clm_308719839b799042f0d33499aa4b79f1fcaa4c07a263ae45f87f5b02c9a32039`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

