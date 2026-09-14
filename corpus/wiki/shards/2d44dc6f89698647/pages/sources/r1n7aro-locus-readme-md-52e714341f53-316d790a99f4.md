---
access: public
aliases: []
claim_ids:
- clm_0c9b5cf3f7bf15e0e6e6d6b1472df5aa7b8f851db66c437a1b011b8a85c9f338
- clm_2301e84ba5f4f7279399246922cc7c894900af424874ada3df0efcb3e7617af8
- clm_31a70f82f792a455d9c908412da97675b06fa300e8bc54710337a49e3c7921a5
- clm_4a3ab10fd2898cc205fb24a241f32c58333be3c09cc292611d3e82b76fe72b4a
- clm_5afff191276ff45a3185a1f93db846068af7c82054a56271a206f0af473ef4c6
- clm_72ecad8cddcae22c42856274e8adae8435baf944bd3d7c46496839c6ecfddd74
- clm_73801947855eac71a7291c4c1111c9d4c7beaa66f34bdb4f1192db62200a99ac
- clm_74c748b57053e1e9f438df8002bf97fa142b6c9fd5625e746e29acc76373ad7d
- clm_980a99c616bd85c891a3a2db5a4db722b62b3c3a83b56ba89b57ec7538a70cdf
- clm_b85060e84b857792128704c504fc2a630db5a5d97de119e31f1501997147290b
- clm_e6c1f4a086d9554c6f65b3cc2f090a5604650647ddb8f2d4be2e093eef8f59cd
- clm_e6e92411d8fd4be696f4a9d5295f21749d34c8c1a1448e2cf0352b9f432c96cf
- clm_ef87e67fe948a85cd15bf00a36ea8b87bf7c52cd947b25b9d8efe958ad0c167a
- clm_f1e1655403ec5b79a1d77e61262ca459da291a408187d2968993f55f08983abc
- clm_fcdb8d634878be58386046298e05b9ffb2070756ef4e9d3ec80a4212d8d6c5f5
maturity: draft
page_id: pg_03fe728fe2855dd7b2f5316d790a99f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_311cabd7969555edb39cf27ab48c21f7
title: r1n7aro/Locus/README.md @ 52e714341f53
updated_at: '2026-09-14T02:33:39Z'
---

# r1n7aro/Locus/README.md @ 52e714341f53

<!-- rcw:begin owner=source:src_311cabd7969555edb39cf27ab48c21f7 block=evidence -->
- Locus uses a proprietary intermediate representation so agents can progressively read large scenes and assets, paired with retrieval tools to quickly locate target objects. [@claim:clm_0c9b5cf3f7bf15e0e6e6d6b1472df5aa7b8f851db66c437a1b011b8a85c9f338]
- Locus currently supports Unity 2021 or later on Windows, and compatibility fixes for older versions may be handled as branch-specific solutions. [@claim:clm_2301e84ba5f4f7279399246922cc7c894900af424874ada3df0efcb3e7617af8]
- Locus for Unity is described as an open-source AI Agent for Unity projects, currently in early testing with feedback welcomed via Issues. [@claim:clm_31a70f82f792a455d9c908412da97675b06fa300e8bc54710337a49e3c7921a5]
- The project is a free open-source tool for the Unity Editor and is not affiliated with Unity Technologies. [@claim:clm_4a3ab10fd2898cc205fb24a241f32c58333be3c09cc292611d3e82b76fe72b4a]
- The product is a standalone Rust + Tauri + Vue.js application that runs as an independent process rather than inside the Unity Editor or as an MCP server. [@claim:clm_5afff191276ff45a3185a1f93db846068af7c82054a56271a206f0af473ef4c6]
- Repository development practice: `bun run locus:test:app` launches an isolated test instance with separate database, config, logs, workspace, WebView2 profile, and temp directories, printing LOCUS_RUNTIME_JSON at startup. [@claim:clm_72ecad8cddcae22c42856274e8adae8435baf944bd3d7c46496839c6ecfddd74]
- The /view command lets the agent build Unity editor interfaces with Vue.js, free of IMGUI constraints, with data binding and interpreted C# execution. [@claim:clm_73801947855eac71a7291c4c1111c9d4c7beaa66f34bdb4f1192db62200a99ac]
- C# changes apply via built-in hot reload without recompiling the assembly or domain reload, preserving Play Mode state, and the agent can immediately confirm whether a change landed. [@claim:clm_74c748b57053e1e9f438df8002bf97fa142b6c9fd5625e746e29acc76373ad7d]
- Repository development practice: dev installers are built with `bun run build:installers` (no-embedded Python/Git by default) and ThinLTO release installers with `bun run release:installers`. [@claim:clm_980a99c616bd85c891a3a2db5a4db722b62b3c3a83b56ba89b57ec7538a70cdf]
- Repository development practice: the repo uses bun + Tauri 2 with Windows as the primary platform; `bun tauri dev` starts a Vite dev server and opens the Tauri desktop app. [@claim:clm_b85060e84b857792128704c504fc2a630db5a5d97de119e31f1501997147290b]
- The main source is licensed GPL-3.0-or-later; third-party notices cover Roslyn/.NET dependencies and a private JSON parser bundle under locus_unity/Editor. [@claim:clm_e6c1f4a086d9554c6f65b3cc2f090a5604650647ddb8f2d4be2e093eef8f59cd]
- Built-in Roslyn semantic analysis runs in Locus's own process, providing go-to-definition, find-references, hover info, and live compiler-grade diagnostics without waiting for Unity to compile. [@claim:clm_e6e92411d8fd4be696f4a9d5295f21749d34c8c1a1448e2cf0352b9f432c96cf]
- Windows is currently the only supported platform; macOS support is planned but not yet available. [@claim:clm_ef87e67fe948a85cd15bf00a36ea8b87bf7c52cd947b25b9d8efe958ad0c167a]
- Installers come in two flavors: one without embedded Python/Git and a full flavor with embedded Python and Git for validating the bundled runtime. [@claim:clm_f1e1655403ec5b79a1d77e61262ca459da291a408187d2968993f55f08983abc]
- An automated knowledge system summarizes conversation requirements into design documents and preserves project understanding in long-term memory. [@claim:clm_fcdb8d634878be58386046298e05b9ffb2070756ef4e9d3ec80a4212d8d6c5f5]
<!-- rcw:end owner=source:src_311cabd7969555edb39cf27ab48c21f7 block=evidence -->

## Researcher notes

