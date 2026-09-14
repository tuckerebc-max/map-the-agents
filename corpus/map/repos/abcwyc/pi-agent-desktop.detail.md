# abcwyc/pi-agent-desktop -- full detail

[Back to orientation](pi-agent-desktop.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/abcwyc/pi-agent-desktop/378db4dc27e4d345c12a74c78f4340bbbc47ce24/54f269a83aa71cea.json](../../../wiki/dossiers/abcwyc/pi-agent-desktop/378db4dc27e4d345c12a74c78f4340bbbc47ce24/54f269a83aa71cea.json)

## specifications (1 claim(s))

- [observation/documented] The product is a local AI agent desktop application for macOS and Windows that packages the pi agent's capabilities into a standalone installable app. -- evidence: [README.md#L5-L5](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L5-L5) (`clm_14e96e6a326c7ae9a658306bc71fe3c9a41b9cfb09c971c6e5715de88db63e2e`)

## components (2 claim(s))

- [observation/documented] The app bundles three components: the desktop shell authored in this fork, the pi agent runtime as an npm dependency, and the pi-web UI merged from an upstream release tag. -- evidence: [docs/ownership-boundaries.md#L7-L11](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/ownership-boundaries.md#L7-L11) (`clm_fda93dedc2fe9dc44c65e97d701d8b60eb075c4e637b7c5a3679bcde06471f56`)
- [observation/documented] The desktop package bundles a Next.js standalone server, a Node.js runtime, and the current Pi SDK, so the local server starts with the app without separate installation. -- evidence: [README.md#L38-L38](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L38-L38) (`clm_a1328d147906cc2b906f3313db67094ac302951fd34ce395cb553b00fe5420c1`)

## design-choices (2 claim(s))

- [observation/documented] Updates are whole-app only: the upgrade button installs one complete signed build containing all three components and restarts; it never patches individual JavaScript packages or downloads unsigned files. -- evidence: [README.md#L72-L76](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L72-L76), [README.md#L80-L80](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L80-L80) (`clm_fc4502c336b74932aa7b8d3822a2734f2ac0857f4d3608775371d02bfd273eef`)
- [observation/documented] The web UI uses a small internal i18n layer with English and Simplified Chinese packages, browser-inferred initial locale, and persistence in localStorage under pi-locale. -- evidence: [docs/i18n.md#L3-L6](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/i18n.md#L3-L6), [docs/i18n.md#L12-L13](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/i18n.md#L12-L13), [docs/i18n.md#L15-L17](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/i18n.md#L15-L17) (`clm_03be047afd872a40ac82791c310464f6fe58c72dd8755f3da51ec0c4e069ea8a`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run npm test, tsc --noEmit, npm run lint, cargo fmt/clippy checks, and npm run release:verify; they should avoid next build during normal development. -- evidence: [README.md#L130-L130](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L130-L130), [README.md#L142-L143](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L142-L143), [README.md#L116-L116](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L116-L116), [README.md#L136-L136](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L136-L136), [README.md#L133-L133](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L133-L133), [README.md#L146-L147](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L146-L147) (`clm_0808b10c7b4e58c0c6cf8f6f2428dac5de889fcc913debe8dc83c553bc7b9d9c`)
- [observation/documented] Repository development practice: a nightly component-updates workflow syncs upstream pi and pi-web releases, intersecting changes with fork-ownership.json and running the full gate before pushing to main or opening a PR. -- evidence: [docs/ownership-boundaries.md#L19-L20](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/ownership-boundaries.md#L19-L20), [README.md#L172-L175](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L172-L175), [docs/ownership-boundaries.md#L22-L24](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/docs/ownership-boundaries.md#L22-L24) (`clm_4eb915dd780f40054391d925df0c9cb362363e3758242172a87a8113c12c9d45`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Features include browsing and resuming past Pi sessions, real-time chat with visible thinking/tool calls/cost, branching or forking conversations, and Git worktree switching from the sidebar. -- evidence: [README.md#L9-L17](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L9-L17) (`clm_4981a9df3749bb06b507b8ab92f8f808bc0f91766a7c91d9536c88cc49f6d1b8`)
- [observation/documented] The app can preview source code, diffs, Markdown, images, audio, PDF, and DOCX files, and offers dark mode, automatic session naming, and a completion sound. -- evidence: [README.md#L9-L17](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L9-L17) (`clm_c4f3efd765e2dba08679f7f328c477c4cac16ea1a64d93770ea3c80d9c1545d3`)

## memory-state (1 claim(s))

- [observation/documented] The app reads Pi's local data directory ~/.pi/agent by default, picking up existing sessions, models, and authentication; PI_CODING_AGENT_DIR can point elsewhere. -- evidence: [README.md#L48-L50](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L48-L50), [README.md#L46-L46](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L46-L46), [README.md#L58-L58](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L58-L58) (`clm_14c8597f04bfc0d0cf0b5d5b93433c504b99d82f60dcef54ee9012ac873c77d3`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The file-browsing API restricts access to the current session, the selected project, and explicitly authorized working directories; model keys and session data stay local. -- evidence: [README.md#L60-L60](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L60-L60) (`clm_be689ba1b82b866504cd1a97d9784424191a7485e886d111b79423c63a0ef25c`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building requires Node.js 22 (recommended), npm, Rust 1.85+, plus platform toolchains such as Xcode CLT on macOS and Microsoft C++ Build Tools with WebView2 on Windows. -- evidence: [README.md#L99-L105](https://github.com/abcwyc/pi-agent-desktop/blob/378db4dc27e4d345c12a74c78f4340bbbc47ce24/README.md#L99-L105) (`clm_4f4cd292611887f4327dd9359ceabce5a010029ad44dbd4c84b2c5a8cfa8acd8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

