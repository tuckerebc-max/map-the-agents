# almogdepaz/wolfpack

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0c7ee60e7163 @ 1ef435f5947eaa2c

## Summary (orientation draft, not independently verified)

Wolfpack is a self-hosted browser/phone control room for persistent AI coding-agent terminals, with sessions owned by a Rust PTY broker separate from the web server, direct Tailscale remote access, a JSON CLI for session control, and bundled agent skills. Contributor docs describe Bun/Rust/Zig build and test workflows.

## Source coverage

Source coverage (partial): 3 of 26 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Wolfpack is a self-hosted control room for running coding agents remotely, letting users monitor and control persistent agent terminals from a desktop or phone. -- evidence: [README.md#L8-L8](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L8-L8), [README.md#L10-L10](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L10-L10)
- components (1 claim(s)):
  - [observation/documented] Sessions run in a Rust PTY broker separate from the web server, so closing the browser or restarting only the web server does not end sessions; a broker restart or login-service reinstall can terminate them. -- evidence: [README.md#L14-L14](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L14-L14)
- design-choices (1 claim(s)):
  - [observation/documented] Remote access is designed to go directly over a private Tailscale network with no Wolfpack-hosted relay or account, and the phone client is a PWA with touch-friendly controls and optional notifications. -- evidence: [README.md#L86-L89](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L86-L89), [README.md#L10-L10](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L10-L10)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors need Bun (v1.4.2+ pinned in CI) and a Rust toolchain, plus a pinned Zig toolchain and Ghostty VT build only for source builds of the broker; release-install users need neither Zig nor Ghostty. -- evidence: [CONTRIBUTING.md#L5-L6](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L5-L6)
  - [observation/documented] Repository development practice: tests run via bun test (unit/integration/snapshot under tests/), Playwright for e2e, and cargo test for the Rust broker; PRs must branch off main, pass bun test, and stay focused. -- evidence: [CONTRIBUTING.md#L32-L35](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L32-L35), [CONTRIBUTING.md#L76-L79](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L76-L79), [CONTRIBUTING.md#L23-L28](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L23-L28), [CONTRIBUTING.md#L37-L37](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L37-L37)
- skills-patterns (1 claim(s)):
  - [observation/documented] Wolfpack ships agent skills: wolfpack-tailnet-control for session control across Agent Skills-compatible harnesses, and wolfpack-pi-task-delegation teaching Pi durable task routing via agent_task_* commands. -- evidence: [README.md#L103-L103](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L103-L103)
- interfaces (2 claim(s)):
  - [observation/documented] The product supports built-in coding-agent providers Claude Code, Codex, Gemini CLI, Cursor, and Pi, with shell as an always-available fallback and custom PATH commands configurable in Settings → Agents. -- evidence: [README.md#L86-L89](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L86-L89), [README.md#L12-L12](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L12-L12)
  - [observation/documented] A CLI exposes JSON session control, e.g. wolfpack --machine <peer> list --json, session status, session create with --harness and --plan, and agent spawn with --notify-parent. -- evidence: [README.md#L126-L128](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L126-L128), [README.md#L111-L114](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L111-L114), [README.md#L120-L122](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L120-L122)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](wolfpack.detail.md)

Metadata and full claim list: [full detail](wolfpack.detail.md)
Human notes ([notes](wolfpack.notes.md), never overwritten by build)

[Back to map index](../../index.md)
