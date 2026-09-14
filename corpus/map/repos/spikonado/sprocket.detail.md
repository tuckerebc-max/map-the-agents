# spikonado/sprocket -- full detail

[Back to orientation](sprocket.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/spikonado/sprocket/f705b4375ade23ebcf6e30c082f977e42297cc12/a70a95cc62364459.json](../../../wiki/dossiers/spikonado/sprocket/f705b4375ade23ebcf6e30c082f977e42297cc12/a70a95cc62364459.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The system has three planes: a Svelte/Electron/CLI client plane, a local Rust execution plane that authenticates requests and runs tools, and a Convex cloud coordination plane with an AI gateway for completions. -- evidence: [ARCHITECTURE.md#L48-L53](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L48-L53), [ARCHITECTURE.md#L27-L44](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L27-L44) (`clm_65c69b9d8c0b6a1ca9722907e644442d7645ad39a8242fe08bfaca3f5f36504b`)

## design-choices (1 claim(s))

- [observation/documented] Stated design principles include local execution of file and shell operations by a Rust process, durable coordination that survives interruptions, and layered implementation where workspace primitives avoid HTTP, Convex, and provider dependencies. -- evidence: [ARCHITECTURE.md#L14-L23](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L14-L23) (`clm_9fd792a930f63d154ac48393eb5a42389b2fd4925b49c959d2e4c000b006deea`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: building and testing use bun install, bun dev, cargo test, bun run test, bun run build, and prek run -a, with Bun 1.3.9+, Node.js 24.14+, and a stable Rust toolchain required. -- evidence: [README.md#L140-L145](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L140-L145), [README.md#L108-L110](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L108-L110), [README.md#L116-L118](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L116-L118), [README.md#L102-L104](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L102-L104) (`clm_c005a2f376c25e924f4df3ca345e6311a15d4a670b4ed6b7bf6b4f4abdd63fb1`)
- [observation/documented] Repository development practice: BACKWARDS_COMPATIBILITY.md instructs that each compatibility layer's entry be removed when its removal PR merges, and that schema fields be dropped only after migrations complete and production scans find no remaining values. -- evidence: [BACKWARDS_COMPATIBILITY.md#L174-L177](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/BACKWARDS_COMPATIBILITY.md#L174-L177), [BACKWARDS_COMPATIBILITY.md#L44-L44](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/BACKWARDS_COMPATIBILITY.md#L44-L44), [BACKWARDS_COMPATIBILITY.md#L80-L83](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/BACKWARDS_COMPATIBILITY.md#L80-L83) (`clm_69323f11f85543076f0a2d071191ae382c2186e81f52834afb879bbde9dfd558`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI supports commands such as login, run (with --thread), update/upgrade, serve (--api-only), and --web, and accepts a directory argument to attach a workspace. -- evidence: [README.md#L43-L43](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L43-L43), [README.md#L65-L68](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L65-L68), [README.md#L76-L82](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L76-L82), [README.md#L36-L39](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L36-L39), [README.md#L51-L55](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L51-L55) (`clm_1f1398bb65e383824d479e3a94e61e3476a93f7ec143702f485ac1532c62d2a2`)
- [observation/documented] Server behavior is configurable via environment variables including SPROCKET_DATA_DIR, SPROCKET_PORT (default 17731), SPROCKET_HOST (default 127.0.0.1), and SPROCKET_DESKTOP_EXECUTABLE. -- evidence: [README.md#L88-L96](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/README.md#L88-L96) (`clm_59409e350d1c608d1ee2310a718ac6fd7c20e00ab02f799bc673f55c497020ce`)
- [observation/documented] Artifact tools include add_artifact, edit_artifact, list_artifacts, and save_artifact; save_artifact accepts an existing file only when its content is identical and never overwrites differing content. -- evidence: [ARCHITECTURE.md#L142-L147](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L142-L147) (`clm_7fb3923df2fd1b7b5ae8fa22654da66957d938d8fd53d35ec51545b4ac3ad5cc`)

## memory-state (1 claim(s))

- [observation/documented] State is split by owner: Convex holds users, threads, durable transcript parts, runs, and tool-job records, while the local server keeps a thread summary cache, transcript replica, folder list, and pairing credentials; the WorkOS refresh token lives in the OS credential store. -- evidence: [ARCHITECTURE.md#L109-L127](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L109-L127), [ARCHITECTURE.md#L253-L280](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L253-L280) (`clm_1c50d5a0b542952087f765f2d08359e99c69a7f20db29f7786ad6d65ee7cf463`)

## orchestration (1 claim(s))

- [observation/documented] Agent runs use idempotent creation keyed by a submission identifier, renewable run claims that reject stale workers, durable tool-job records taken before and after execution, and cancellation propagated from durable state to local operations. -- evidence: [ARCHITECTURE.md#L236-L238](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L236-L238), [ARCHITECTURE.md#L314-L321](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L314-L321), [ARCHITECTURE.md#L231-L234](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L231-L234) (`clm_065f2fe477a18683bce6f91d9a58df7e4fa9e1f865d7b3d715ea1823dd1dd085`)

## tools-permissions (1 claim(s))

- [observation/documented] Workspace patches and shell commands are not sandboxed; they run with the permissions of the local Sprocket process and are confined only by the OS user. -- evidence: [ARCHITECTURE.md#L306-L307](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L306-L307) (`clm_2f6e4ed21fe4740b106ff75adc7cfaf94200325c793442e6835caac4b0afa56b`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product depends on an external private AI gateway (spikonado/ai-gateway) at https://ai-gateway.spikonado.com for model routing and quota checks, plus Convex and WorkOS AuthKit for state and identity. -- evidence: [ARCHITECTURE.md#L340-L342](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L340-L342), [ARCHITECTURE.md#L48-L53](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L48-L53), [ARCHITECTURE.md#L27-L44](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L27-L44) (`clm_4487cb3d0b9c46823931d6da034bedda3370f0ef42f8b51e41df96cb30944dfa`)

## limitations (2 claim(s))

- [observation/documented] Artifact-bound files must be UTF-8 text within 500,000 bytes; missing or unreadable files report an error while keeping their last readable content, and the server does not recreate missing files from the cloud copy. -- evidence: [ARCHITECTURE.md#L175-L178](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L175-L178) (`clm_7e7429d39d5824217c3c5522aecdd1ad5e1cf43414c23621966a5af0faaf5129`)
- [observation/documented] The native authentication migration is incomplete: thread-cache registration, thread commands, cancellation, lifecycle, transcript synchronization, and attachments still pass browser access tokens or user IDs to Rust. -- evidence: [ARCHITECTURE.md#L300-L304](https://github.com/spikonado/sprocket/blob/f705b4375ade23ebcf6e30c082f977e42297cc12/ARCHITECTURE.md#L300-L304) (`clm_bc05466cf9f537bf91f1aaed05978117d6b15f6ff52d762484349a3b989231e9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

