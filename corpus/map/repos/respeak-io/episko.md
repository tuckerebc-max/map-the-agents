# respeak-io/episko

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 974192b540db @ 4ce3ea1d5573290e

## Summary (orientation draft, not independently verified)

Episko is a Tauri v2 desktop app for running many coding-agent sessions in real PTY terminals with live telemetry, in-app permission answering, project dashboards, and task running. Evidence is largely README product documentation plus a release procedure document. Evidence coverage: 102 of 116 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 22 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The app is built on Tauri v2 with a Rust backend and system WebView frontend, uses portable-pty for PTYs (forkpty on macOS, ConPTY on Windows), tiny_http as a localhost telemetry receiver, and xterm.js for terminal rendering. -- evidence: [README.md#L69-L73](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L69-L73)
- design-choices (1 claim(s)):
  - [observation/documented] Task discovery never executes the project: just --dump, task --list and mise tasks ls sit behind a trust gate, Makefiles are parsed statically, and tasks that cannot run are shown greyed with the reason rather than hidden. -- evidence: [README.md#L53-L55](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L53-L55)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: CI runs on every push and PR to dev/main on both macOS and Windows, covering strict tsc typecheck, vitest suites (~1,535 it blocks), cargo check/test --locked (~270 #[test] functions) and clippy with -D warnings. -- evidence: [RELEASE.md#L17-L22](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L17-L22), [RELEASE.md#L15-L15](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L15-L15)
  - [observation/documented] Repository development practice: ignored cargo contract tests against real Claude Code (instrumentation, permission modes, temp-dir layout) are run manually via cargo test -- --ignored because CI lacks claude on PATH; one of them spends tokens and needs authentication. -- evidence: [RELEASE.md#L54-L57](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L54-L57), [RELEASE.md#L61-L82](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/RELEASE.md#L61-L82)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Episko gives each coding-agent session its own real terminal; Claude Code and Codex are first-class integrated providers, while other installed CLIs work through a terminal-only adapter pane. -- evidence: [README.md#L5-L5](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L5-L5)
  - [observation/documented] The app discovers and runs tasks the project already ships — .episko/tasks.toml, .vscode/tasks.json and launch.json, package.json scripts, justfile, Taskfile.yml, mise.toml, Makefile, Cargo.toml — in the same PTY panes as agent sessions. -- evidence: [README.md#L43-L43](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L43-L43), [README.md#L45-L45](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L45-L45)
- memory-state (1 claim(s)):
  - [observation/documented] Personal preferences go to localStorage while project facts go to .episko/tasks.toml, described as the only file the app writes, edited via toml_edit so comments and ordering survive; shared digests and notes can be committed as .episko/digest.md and .episko/notes.toml. -- evidence: [README.md#L34-L37](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L34-L37), [README.md#L53-L55](https://github.com/respeak-io/episko/blob/974192b540db99dd89b2c29adc7e154c1ac287c0/README.md#L53-L55)
- orchestration (2 claim(s)):
More evidence: [full detail](episko.detail.md)

Metadata and full claim list: [full detail](episko.detail.md)
Human notes ([notes](episko.notes.md), never overwritten by build)

[Back to map index](../../index.md)
