# rustykuntz/clideck -- full detail

[Back to orientation](clideck.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rustykuntz/clideck/2c381835565bf58fcfd50bb5645f13c5429245ee/eb88fdf2ee936171.json](../../../wiki/dossiers/rustykuntz/clideck/2c381835565bf58fcfd50bb5645f13c5429245ee/eb88fdf2ee936171.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Built-in plugins include Git Changes, Supertonic Voice, Emoji, and Smart Dictation, and additional plugins can be built with a plugin SDK. -- evidence: [README.md#L73-L73](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L73-L73), [README.md#L68-L71](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L68-L71) (`clm_297fd424c4293b697b0488edd0dca0424eaa5bffa13bd248c7c67019f34c194b`)

## design-choices (1 claim(s))

- [observation/documented] CliDeck binds to localhost, and agent CLIs use their own network connections rather than going through CliDeck. -- evidence: [README.md#L101-L102](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L101-L102) (`clm_a2e502f09d390980e5d99721c1a5422a20b9cfce317980ab5257ae70908d0861`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use Node.js 22.12+, run npm ci and npm test, start the app with npm start using a separate dev data-dir, run UI checks with node --test, and test interface changes in both light and dark themes. -- evidence: [CONTRIBUTING.md#L5-L9](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L5-L9), [CONTRIBUTING.md#L11-L12](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L11-L12) (`clm_93a28ba807e1aabb2aa26e55178985642cc9640fc985947a4225d8b50f6e2372`)
- [observation/documented] Repository development practice: keep changes simple and focused, open an issue before large changes, and include the problem, resulting behavior, and relevant checks in pull requests. -- evidence: [CONTRIBUTING.md#L3-L3](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L3-L3), [CONTRIBUTING.md#L11-L12](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L11-L12) (`clm_36589420c8d98b2331dbf51cf682394cd90d0f0a83d1e05b11be2e931d6fb8e2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] CliDeck runs Claude Code, Codex, Gemini CLI, OpenCode, Pi, and shell sessions in one browser window, grouped into projects, where each session is the agent's actual terminal with its own tools, configuration, and account. -- evidence: [README.md#L5-L9](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L5-L9) (`clm_81ab657395e3d17ea77cc70b626d3f31cb3f7cc0dd0f3d3cf794bd25c5757a21`)
- [observation/documented] After starting, the web UI is opened at http://127.0.0.1:4000; the tool can also be run via npx. -- evidence: [README.md#L24-L25](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L24-L25) (`clm_b21dc011cfc98509d5aa89a666bfb09f6923767b89f9e024f76cfb0bf53114bc`)
- [observation/documented] The CLI supports --port, --data-dir, and --help flags; CLIDECK_PORT or PORT also sets the port, and data is stored in ~/.clideck-next by default. -- evidence: [README.md#L95-L99](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L95-L99), [README.md#L101-L102](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L101-L102) (`clm_51d6a420e0e1b20f861d93815e1c47247f735f39c311017e98d2b33a372e21ea`)
- [observation/documented] Agents open artifacts in preview tabs beside the terminal via 'clideck show', supporting Markdown, text, logs, JSON, HTML, PDFs, images, video, Mermaid diagrams, diffs, charts, and test results; users can also drop files onto the tab strip. -- evidence: [README.md#L61-L62](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L61-L62), [README.md#L49-L51](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L49-L51), [README.md#L55-L59](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L55-L59), [README.md#L45-L47](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L45-L47) (`clm_e981837b2faee44f44077fa93abe9351b9b65066b03a127ca824682c976ab758`)
- [observation/documented] Plugins are self-contained folders with a clideck-plugin.json manifest plus optional server.js, client.js, and public/ assets; installation validates and atomically copies the folder into the plugin directory and never runs npm. -- evidence: [PLUGIN-SDK.md#L6-L12](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/PLUGIN-SDK.md#L6-L12), [PLUGIN-SDK.md#L47-L49](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/PLUGIN-SDK.md#L47-L49), [PLUGIN-SDK.md#L3-L4](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/PLUGIN-SDK.md#L3-L4) (`clm_e6400827251b143bdcd8a7b94e99971203d7c7e0bb3aba6272671c416147014d`)

## memory-state (1 claim(s))

- [observation/documented] Sessions can be reopened and earlier conversations read, stopped sessions show last-used times, and session backups can be exported for recovery. -- evidence: [README.md#L32-L41](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L32-L41) (`clm_88f3d1edd2f0866f9424168848e72441ec09cc8163dd78f3a524dc2b4f5c8a7f`)

## orchestration (1 claim(s))

- [observation/documented] CliDeck Ask lets agents send requests to other sessions and receive replies, including across providers; users type '@@' to find sessions, and agents discover teammates with 'clideck agents' and contact them with 'clideck ask'. -- evidence: [README.md#L77-L78](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L77-L78), [README.md#L88-L89](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L88-L89) (`clm_d6120aa7f01b74f2cb442a2b65f943e8d1c635691cf1f7aad770998e07db945b`)

## tools-permissions (2 claim(s))

- [observation/documented] Plugin backends run as arbitrary local code with the user's filesystem and network authority; worker isolation protects against accidental crashes but is explicitly not a malicious-code sandbox. -- evidence: [PLUGIN-SDK.md#L223-L225](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/PLUGIN-SDK.md#L223-L225) (`clm_5661d5f17fa58f91fc1ad22afa96997623fcc17d670d37744522f4b6fd6bd167`)
- [observation/documented] Plugin client code runs in a dedicated Worker, never in the CliDeck window, and cannot query or mutate host DOM; secret setting values are never sent to the browser, only a configured flag. -- evidence: [PLUGIN-SDK.md#L120-L126](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/PLUGIN-SDK.md#L120-L126) (`clm_b41f7b6e4b076487810bfa75625b880c113570ad8c9eaffc1d760c576b5bd236`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product requires Node.js 22.12 or newer and an installed agent CLI, and is installed globally via npm as clideck@2. -- evidence: [README.md#L17-L17](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L17-L17), [README.md#L19-L22](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L19-L22) (`clm_db69156ca29eb549d34b91ea8aa2de0194f8bef28be4113c8d61f52485c8721f`)

## limitations (1 claim(s))

- [observation/documented] Autopilot was removed because agents already have sub-agents, and mobile control was removed because harnesses provide their own remote access. -- evidence: [README.md#L112-L113](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L112-L113) (`clm_0888bae78aa741eea48ad5ad94ea31dee9c41bd65c144ae803c415ba77e3c4bc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

