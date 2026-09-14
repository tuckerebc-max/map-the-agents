# spikonado/sprocket

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f705b4375ade @ a70a95cc62364459

## Summary (orientation draft, not independently verified)

Sprocket is an agentic hardware/software development platform combining a Svelte web UI, Electron desktop shell, npm CLI, local Rust server, Convex cloud backend, and an external AI gateway. Evidence covers CLI usage, architecture, state ownership, authentication, artifact tooling, and extensive backwards-compatibility migrations; no agent performance evaluation is documented. Evidence coverage: 127 of 192 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The system has three planes: a Svelte/Electron/CLI client plane, a local Rust execution plane that authenticates requests and runs tools, and a Convex cloud coordination plane with an AI gateway for completions. -- evidence: [ARCHITECTURE.md#L48-L53](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L48-L53), [ARCHITECTURE.md#L27-L44](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L27-L44)
- design-choices (1 claim(s)):
  - [observation/documented] Stated design principles include local execution of file and shell operations by a Rust process, durable coordination that survives interruptions, and layered implementation where workspace primitives avoid HTTP, Convex, and provider dependencies. -- evidence: [ARCHITECTURE.md#L14-L23](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L14-L23)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: building and testing use bun install, bun dev, cargo test, bun run test, bun run build, and prek run -a, with Bun 1.3.9+, Node.js 24.14+, and a stable Rust toolchain required. -- evidence: [README.md#L140-L145](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L140-L145), [README.md#L108-L110](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L108-L110), [README.md#L116-L118](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L116-L118), [README.md#L102-L104](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L102-L104)
  - [observation/documented] Repository development practice: BACKWARDS_COMPATIBILITY.md instructs that each compatibility layer's entry be removed when its removal PR merges, and that schema fields be dropped only after migrations complete and production scans find no remaining values. -- evidence: [BACKWARDS_COMPATIBILITY.md#L174-L177](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/BACKWARDS_COMPATIBILITY.md#L174-L177), [BACKWARDS_COMPATIBILITY.md#L44-L44](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/BACKWARDS_COMPATIBILITY.md#L44-L44), [BACKWARDS_COMPATIBILITY.md#L80-L83](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/BACKWARDS_COMPATIBILITY.md#L80-L83)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI supports commands such as login, run (with --thread), update/upgrade, serve (--api-only), and --web, and accepts a directory argument to attach a workspace. -- evidence: [README.md#L43-L43](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L43-L43), [README.md#L65-L68](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L65-L68), [README.md#L76-L82](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L76-L82), [README.md#L36-L39](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L36-L39), [README.md#L51-L55](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L51-L55)
  - [observation/documented] Server behavior is configurable via environment variables including SPROCKET_DATA_DIR, SPROCKET_PORT (default 17731), SPROCKET_HOST (default 127.0.0.1), and SPROCKET_DESKTOP_EXECUTABLE. -- evidence: [README.md#L88-L96](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L88-L96)
- memory-state (1 claim(s)):
  - [observation/documented] State is split by owner: Convex holds users, threads, durable transcript parts, runs, and tool-job records, while the local server keeps a thread summary cache, transcript replica, folder list, and pairing credentials; the WorkOS refresh token lives in the OS credential store. -- evidence: [ARCHITECTURE.md#L109-L127](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L109-L127), [ARCHITECTURE.md#L253-L280](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L253-L280)
- orchestration (1 claim(s)):
More evidence: [full detail](sprocket.detail.md)

Metadata and full claim list: [full detail](sprocket.detail.md)
Human notes ([notes](sprocket.notes.md), never overwritten by build)

[Back to map index](../../index.md)
