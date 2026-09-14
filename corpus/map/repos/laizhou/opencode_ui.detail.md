# laizhou/opencode_ui -- full detail

[Back to orientation](opencode_ui.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/laizhou/opencode_ui/453afb7cc9fc3da1e24180166bca7337e076b16a/3b903129d6dc525f.json](../../../wiki/dossiers/laizhou/opencode_ui/453afb7cc9fc3da1e24180166bca7337e076b16a/3b903129d6dc525f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] When OpenCode edits files, the plugin opens a native IDE diff viewer showing changes chronologically with navigation, progress count, and accept (write to disk and git add) or reject (restore pre-edit state) actions. -- evidence: [README.md#L90-L90](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L90-L90), [README.md#L92-L98](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L92-L98) (`clm_f3ad5b1ba6459ba94d125443ccb4d2e6f9c6cba715b54d2978591cc01da43113`)
- [observation/documented] The plugin sends a system notification when OpenCode transitions from Busy to Idle, and supports auto-resume of the last session, clickable file-path links in terminal output, and remembered connection settings. -- evidence: [README.md#L111-L111](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L111-L111), [README.md#L10-L19](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L10-L19), [README.md#L59-L59](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L59-L59), [README.md#L105-L105](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L105-L105) (`clm_4c659e5453f2d3bbf804db99fc5e3cc597b2d7d75d3579033a43e1191c39c1c2`)

## design-choices (2 claim(s))

- [observation/documented] Terminal management uses a single persistent terminal tab per project named OpenCode({port}); closing it causes a new one to be created on next launch. -- evidence: [README.md#L124-L124](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L124-L124), [README.md#L126-L128](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L126-L128) (`clm_7037ef48717412d06df0a7a43f0a6103b330152c719e5d2a8550456da26ab406`)
- [observation/documented] Keyboard shortcuts are customizable through the IDE's Settings > Keymap by searching for 'OpenCode'. -- evidence: [README.md#L115-L115](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L115-L115) (`clm_3075399ab082c7bf0b56a04e51bdb7292c2d46f40005f688c06628dc6a181232`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to build with the Gradle wrapper (./gradlew build, runIde, clean build), run tests via ./gradlew test with class/method/pattern filters, and verify with ./gradlew check for lint. -- evidence: [AGENTS.md#L24-L35](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L24-L35), [AGENTS.md#L38-L53](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L38-L53), [AGENTS.md#L56-L59](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L56-L59), [AGENTS.md#L21-L21](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L21-L21) (`clm_c2c03fb18922272f1f1669db829790bce742395b101ed648d4d104a5ebfb15b0`)
- [observation/documented] Repository development practice: the guide mandates Kotlin coding conventions, 4-space indentation, 120-char lines, no wildcard imports, English-only comments and strings, and avoiding double-bang null operators. -- evidence: [AGENTS.md#L63-L63](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L63-L63), [AGENTS.md#L74-L75](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L74-L75), [AGENTS.md#L78-L82](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L78-L82), [AGENTS.md#L66-L71](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L66-L71) (`clm_fd42184e5ecf38ae5859b240d62bf205ede171e66906b3d094727dadedf4edfb`)
- [observation/documented] Repository development practice: IntelliJ-specific rules require UI updates on the EDT, network/IO on background threads, Disposable implementation for resource-holding services, and Logger.getInstance instead of println. -- evidence: [AGENTS.md#L85-L94](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/AGENTS.md#L85-L94) (`clm_e9a833c6449c12b31217650dc134fb55d54e1bf7f48c912722d13d84d139bdcc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The product is a JetBrains IDE plugin integrating the OpenCode open-source AI coding agent into the development workflow. -- evidence: [README.md#L6-L6](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L6-L6) (`clm_7e25e208166cb5dc1c1319bb78f939e0b82e4298ecd02a0c2f57ad46d0ee3b04`)
- [observation/documented] Quick Launch opens a connection dialog via Cmd+Esc (Mac) or Ctrl+\ (Win/Linux), letting users connect to an existing OpenCode server by host:port with optional password, or create a new local terminal session on default port 127.0.0.1:4096. -- evidence: [README.md#L56-L57](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L56-L57), [README.md#L54-L54](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L54-L54), [README.md#L10-L19](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L10-L19) (`clm_62693995a7cda1947e2628d6322e9d29d62a2fd097dd264e7f5aa536d05048d4`)
- [observation/documented] An 'Add to Terminal' shortcut (Opt+Cmd+K / Ctrl+Alt+K) sends the current file or selection to OpenCode as @path references, with line ranges like @file.kt#L10-25 when text is selected, and opens/focuses the terminal if needed. -- evidence: [README.md#L74-L76](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L74-L76), [README.md#L10-L19](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L10-L19), [README.md#L67-L68](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L67-L68), [README.md#L65-L65](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L65-L65) (`clm_3f8a08c6c2bf80b33696ce9d6ee8f5cc936cc76ee8c3a6c7911200cdbee7d649`)
- [observation/documented] Context can also be added via right-click menus: 'OpenCode: Add Context' in the editor and 'OpenCode: Add File(s)' in Project View. -- evidence: [README.md#L36-L37](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L36-L37) (`clm_8b77dd19e5dbbd1cc3e1e0c6058b9ece3d09ceaa9a63f1c8425b1d560dd292b8`)
- [inference/documented] The plugin appears to detect server authentication automatically when connecting to a running OpenCode server, and supports an optional password for the server. -- evidence: [README.md#L56-L57](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L56-L57), [README.md#L10-L19](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L10-L19) (`clm_ade1e4a868f9f75f1ffa85e288b4c11297093fd1c566e3535decb2adb7786985`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The plugin requires a JetBrains IDE (2025.2+ per README) and the OpenCode CLI, installable via npm or from opencode.ai/download. -- evidence: [README.md#L41-L42](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L41-L42) (`clm_ca7bf6032a54297a3670afef99f389a443ce764586ea39df64827f3bd98b5513`)

## limitations (1 claim(s))

- [observation/documented] Compared with Claude Code, the plugin lacks diagnostic sharing and instead uses the IDE's built-in LSP, per the feature comparison table. -- evidence: [README.md#L23-L28](https://github.com/LaiZhou/OpenCode_UI/blob/453afb7cc9fc3da1e24180166bca7337e076b16a/README.md#L23-L28) (`clm_20a009df664e61bfc1fab5883ffdaf18122e1848d14ec0abaa395fba87551768`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

