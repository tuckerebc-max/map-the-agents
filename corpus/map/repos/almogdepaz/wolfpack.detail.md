# almogdepaz/wolfpack -- full detail

[Back to orientation](wolfpack.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/almogdepaz/wolfpack/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/1ef435f5947eaa2c.json](../../../wiki/dossiers/almogdepaz/wolfpack/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/1ef435f5947eaa2c.json)

## specifications (1 claim(s))

- [observation/documented] Wolfpack is a self-hosted control room for running coding agents remotely, letting users monitor and control persistent agent terminals from a desktop or phone. -- evidence: [README.md#L8-L8](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L8-L8), [README.md#L10-L10](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L10-L10) (`clm_6933f3720f210b8a6857ae4e11e2a83bc70dc19497de91927f86a7a6fa7baf10`)

## components (1 claim(s))

- [observation/documented] Sessions run in a Rust PTY broker separate from the web server, so closing the browser or restarting only the web server does not end sessions; a broker restart or login-service reinstall can terminate them. -- evidence: [README.md#L14-L14](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L14-L14) (`clm_902ef62c1703f863b0a8dddd1b789fdbd0162d71bd4ce77e3588973f70f59b4b`)

## design-choices (1 claim(s))

- [observation/documented] Remote access is designed to go directly over a private Tailscale network with no Wolfpack-hosted relay or account, and the phone client is a PWA with touch-friendly controls and optional notifications. -- evidence: [README.md#L86-L89](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L86-L89), [README.md#L10-L10](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L10-L10) (`clm_0fa108caa900742341b04ccb4580e7a452cfa5660e137fc235ae9f71966f3943`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors need Bun (v1.4.2+ pinned in CI) and a Rust toolchain, plus a pinned Zig toolchain and Ghostty VT build only for source builds of the broker; release-install users need neither Zig nor Ghostty. -- evidence: [CONTRIBUTING.md#L5-L6](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L5-L6) (`clm_ab7a08ce2dce81b49d82b4737793755b3a55f6a6f232f4e74ac83685c3058514`)
- [observation/documented] Repository development practice: tests run via bun test (unit/integration/snapshot under tests/), Playwright for e2e, and cargo test for the Rust broker; PRs must branch off main, pass bun test, and stay focused. -- evidence: [CONTRIBUTING.md#L32-L35](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L32-L35), [CONTRIBUTING.md#L76-L79](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L76-L79), [CONTRIBUTING.md#L23-L28](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L23-L28), [CONTRIBUTING.md#L37-L37](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L37-L37) (`clm_e23b9376c60c35e5917ae0b6e257860391cac79f320c98fc7b3e350e12c6fe8e`)
- [observation/documented] Repository development practice: frontend assets in public/ are embedded into the binary via scripts/gen-assets.ts, and src/public-assets.ts must not be edited manually. -- evidence: [CONTRIBUTING.md#L41-L41](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L41-L41), [CONTRIBUTING.md#L43-L45](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/CONTRIBUTING.md#L43-L45) (`clm_ed3869a6e44fde4fddcaa6526ccddb963a3d73868141f9c4d5ccfda3a57348c6`)

## skills-patterns (1 claim(s))

- [observation/documented] Wolfpack ships agent skills: wolfpack-tailnet-control for session control across Agent Skills-compatible harnesses, and wolfpack-pi-task-delegation teaching Pi durable task routing via agent_task_* commands. -- evidence: [README.md#L103-L103](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L103-L103) (`clm_ed0c78d742e2cb47f9906201e0935ca093c7c812fdf5ebce513bc1e413bcd6af`)

## interfaces (2 claim(s))

- [observation/documented] The product supports built-in coding-agent providers Claude Code, Codex, Gemini CLI, Cursor, and Pi, with shell as an always-available fallback and custom PATH commands configurable in Settings → Agents. -- evidence: [README.md#L86-L89](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L86-L89), [README.md#L12-L12](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L12-L12) (`clm_216c859cc158079d8c730e03a1d0d0d173946fb3509052258955304cf524b348`)
- [observation/documented] A CLI exposes JSON session control, e.g. wolfpack --machine <peer> list --json, session status, session create with --harness and --plan, and agent spawn with --notify-parent. -- evidence: [README.md#L126-L128](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L126-L128), [README.md#L111-L114](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L111-L114), [README.md#L120-L122](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L120-L122) (`clm_761d356669adf9a507d1eda599c92ff49f7ce5bb34c1565d329bebda5a05963b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The tool grants browser users shell-level control over configured projects; session control follows the global API auth policy and has no inter-session authorization layer, so it should be kept on a trusted Tailnet with ACLs or JWT. -- evidence: [README.md#L33-L33](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L33-L33) (`clm_509700169736615b2f314d3025837f8e38210ea583917ad88ff8b5c9ef068414`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Remote access depends on a Tailscale network; machine targeting uses configured tailscaleHostname suffixes, and the CLI sends JWT authorization on a bounded GET /api/machine handshake, failing closed on invalid or unreachable targets. -- evidence: [README.md#L116-L116](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L116-L116), [README.md#L10-L10](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L10-L10) (`clm_c10bb93fe6e4ecbcb1249b68d42a7377fd448532265faea577d25dc073a84aff`)

## limitations (1 claim(s))

- [observation/documented] Session persistence has boundaries: a broker restart or login-service reinstallation can terminate sessions, per the README's lifecycle description. -- evidence: [README.md#L14-L14](https://github.com/almogdepaz/wolfpack/blob/0c7ee60e7163435a849a3a7f9ce662f7dd2fe869/README.md#L14-L14) (`clm_fdf737ac4f634f099d284d68a77bb026bc35d6e5f714d1f7ce7e886bfe79bbf7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

