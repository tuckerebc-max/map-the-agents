# r1n7aro/locus -- full detail

[Back to orientation](locus.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/r1n7aro/locus/52e714341f5331e26cdfeff39bcbefc549cf24c7/4404142f5255491b.json](../../../wiki/dossiers/r1n7aro/locus/52e714341f5331e26cdfeff39bcbefc549cf24c7/4404142f5255491b.json)

## specifications (2 claim(s))

- [observation/documented] Locus for Unity is described as an open-source AI Agent for Unity projects, currently in early testing with feedback welcomed via Issues. -- evidence: [README.md#L19-L19](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L19-L19), [README.md#L30-L30](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L30-L30) (`clm_31a70f82f792a455d9c908412da97675b06fa300e8bc54710337a49e3c7921a5`)
- [observation/documented] Locus currently supports Unity 2021 or later on Windows, and compatibility fixes for older versions may be handled as branch-specific solutions. -- evidence: [README.md#L59-L59](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L59-L59), [README.md#L57-L57](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L57-L57) (`clm_2301e84ba5f4f7279399246922cc7c894900af424874ada3df0efcb3e7617af8`)

## components (2 claim(s))

- [observation/documented] The product is a standalone Rust + Tauri + Vue.js application that runs as an independent process rather than inside the Unity Editor or as an MCP server. -- evidence: [README.md#L34-L34](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L34-L34), [README.md#L47-L47](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L47-L47) (`clm_5afff191276ff45a3185a1f93db846068af7c82054a56271a206f0af473ef4c6`)
- [observation/documented] Built-in Roslyn semantic analysis runs in Locus's own process, providing go-to-definition, find-references, hover info, and live compiler-grade diagnostics without waiting for Unity to compile. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45) (`clm_e6e92411d8fd4be696f4a9d5295f21749d34c8c1a1448e2cf0352b9f432c96cf`)

## design-choices (2 claim(s))

- [observation/documented] Locus uses a proprietary intermediate representation so agents can progressively read large scenes and assets, paired with retrieval tools to quickly locate target objects. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45) (`clm_0c9b5cf3f7bf15e0e6e6d6b1472df5aa7b8f851db66c437a1b011b8a85c9f338`)
- [observation/documented] C# changes apply via built-in hot reload without recompiling the assembly or domain reload, preserving Play Mode state, and the agent can immediately confirm whether a change landed. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45), [README.md#L21-L28](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L21-L28) (`clm_74c748b57053e1e9f438df8002bf97fa142b6c9fd5625e746e29acc76373ad7d`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the repo uses bun + Tauri 2 with Windows as the primary platform; `bun tauri dev` starts a Vite dev server and opens the Tauri desktop app. -- evidence: [README.md#L67-L69](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L67-L69), [README.md#L71-L71](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L71-L71), [README.md#L63-L63](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L63-L63) (`clm_b85060e84b857792128704c504fc2a630db5a5d97de119e31f1501997147290b`)
- [observation/documented] Repository development practice: `bun run locus:test:app` launches an isolated test instance with separate database, config, logs, workspace, WebView2 profile, and temp directories, printing LOCUS_RUNTIME_JSON at startup. -- evidence: [README.md#L79-L79](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L79-L79), [README.md#L75-L77](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L75-L77) (`clm_72ecad8cddcae22c42856274e8adae8435baf944bd3d7c46496839c6ecfddd74`)
- [observation/documented] Repository development practice: dev installers are built with `bun run build:installers` (no-embedded Python/Git by default) and ThinLTO release installers with `bun run release:installers`. -- evidence: [README.md#L121-L123](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L121-L123), [README.md#L105-L105](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L105-L105), [README.md#L119-L119](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L119-L119), [README.md#L101-L103](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L101-L103) (`clm_980a99c616bd85c891a3a2db5a4db722b62b3c3a83b56ba89b57ec7538a70cdf`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The /view command lets the agent build Unity editor interfaces with Vue.js, free of IMGUI constraints, with data binding and interpreted C# execution. -- evidence: [README.zh-CN.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.zh-CN.md#L36-L45), [README.md#L21-L28](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L21-L28) (`clm_73801947855eac71a7291c4c1111c9d4c7beaa66f34bdb4f1192db62200a99ac`)

## memory-state (1 claim(s))

- [observation/documented] An automated knowledge system summarizes conversation requirements into design documents and preserves project understanding in long-term memory. -- evidence: [README.md#L36-L45](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L36-L45), [README.md#L21-L28](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L21-L28) (`clm_fcdb8d634878be58386046298e05b9ffb2070756ef4e9d3ec80a4212d8d6c5f5`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (4 claim(s))

- [observation/documented] Tool execution has two modes: Auto runs all tools without approval, while Ask requires per-tool confirmation; read tools default to auto-run and modifying tools (write, edit, bash, web_fetch, unity_execute, unity_run_states, subagent) default to confirmation. -- evidence: [docs/en/sessions/permissions.mdx#L14-L15](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L14-L15), [docs/sessions/permissions.mdx#L14-L15](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L14-L15), [docs/sessions/permissions.mdx#L19-L21](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L19-L21), [docs/en/sessions/permissions.mdx#L19-L21](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L19-L21) (`clm_d5711a0312ab356d119a9d610212c77b2824bbffd49a9f75ccc48da68e50cc01`)
- [observation/documented] Approval cards support single and batch confirmation with diff previews, and a feedback field lets the agent revise and re-request a rejected proposal. -- evidence: [docs/sessions/permissions.mdx#L27-L29](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L27-L29), [docs/en/sessions/permissions.mdx#L27-L29](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L27-L29), [docs/en/sessions/permissions.mdx#L25-L25](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L25-L25), [docs/sessions/permissions.mdx#L25-L25](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L25-L25) (`clm_0cb635a690c92d397dfb9447e8e4d96937d86c8ffaa8500a5684cb44d40a9864`)
- [observation/documented] A File Tool Boundary setting can restrict file tools to the current project directory; by default (All) paths outside the workspace are allowed. -- evidence: [docs/sessions/permissions.mdx#L42-L43](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L42-L43), [docs/sessions/permissions.mdx#L40-L40](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L40-L40), [docs/en/sessions/permissions.mdx#L42-L43](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L42-L43), [docs/en/sessions/permissions.mdx#L40-L40](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L40-L40) (`clm_ff9ba47623d7dd3751177d295a7962f6593f4acf8f4c1b7add564eb754cfa22f`)
- [observation/documented] Behavior approvals are independent of global mode: even in Auto, switching Unity Editor/Play Mode state or editing protected knowledge folders can be set to require confirmation. -- evidence: [docs/sessions/permissions.mdx#L35-L36](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L35-L36), [docs/sessions/permissions.mdx#L33-L33](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/sessions/permissions.mdx#L33-L33), [docs/en/sessions/permissions.mdx#L35-L36](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L35-L36), [docs/en/sessions/permissions.mdx#L33-L33](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/docs/en/sessions/permissions.mdx#L33-L33) (`clm_33d1f7d42d10d23d0ee7ab7dd06a7c41055de93b3c857fd8cc2e34277083a46f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Installers come in two flavors: one without embedded Python/Git and a full flavor with embedded Python and Git for validating the bundled runtime. -- evidence: [README.md#L105-L105](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L105-L105), [README.md#L125-L125](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L125-L125), [README.md#L107-L107](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L107-L107) (`clm_f1e1655403ec5b79a1d77e61262ca459da291a408187d2968993f55f08983abc`)
- [observation/documented] The main source is licensed GPL-3.0-or-later; third-party notices cover Roslyn/.NET dependencies and a private JSON parser bundle under locus_unity/Editor. -- evidence: [README.md#L129-L129](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L129-L129), [README.md#L141-L141](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L141-L141) (`clm_e6c1f4a086d9554c6f65b3cc2f090a5604650647ddb8f2d4be2e093eef8f59cd`)

## limitations (2 claim(s))

- [observation/documented] Windows is currently the only supported platform; macOS support is planned but not yet available. -- evidence: [README.md#L51-L51](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L51-L51) (`clm_ef87e67fe948a85cd15bf00a36ea8b87bf7c52cd947b25b9d8efe958ad0c167a`)
- [observation/documented] The project is a free open-source tool for the Unity Editor and is not affiliated with Unity Technologies. -- evidence: [README.md#L147-L147](https://github.com/r1n7aro/Locus/blob/52e714341f5331e26cdfeff39bcbefc549cf24c7/README.md#L147-L147) (`clm_4a3ab10fd2898cc205fb24a241f32c58333be3c09cc292611d3e82b76fe72b4a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

