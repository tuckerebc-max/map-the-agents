# catatafishen/agentbridge -- full detail

[Back to orientation](agentbridge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/catatafishen/agentbridge/124f7c082dc33a583a9f834b4c4765133e3d745c/b1b11b5b76643edd.json](../../../wiki/dossiers/catatafishen/agentbridge/124f7c082dc33a583a9f834b4c4765133e3d745c/b1b11b5b76643edd.json)

## specifications (1 claim(s))

- [observation/documented] AgentBridge is a JetBrains IDE plugin that bridges AI coding agents to IntelliJ platform APIs through 120+ native MCP tools, letting agents use inspections, refactorings, test runner, build system, and Git. -- evidence: [README.md#L14-L17](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/README.md#L14-L17) (`clm_ed4818d03f7661d2cfd36990f33326d945a6494211b133a47371424f74092505`)

## components (3 claim(s))

- [observation/documented] PsiBridgeService is a project-level HTTP server exposing 92 IntelliJ-native MCP tools; it starts on a dynamic localhost port and accesses PSI, VFS, Document API, and Git4Idea. -- evidence: [docs/ARCHITECTURE.md#L107-L109](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L107-L109), [docs/ARCHITECTURE.md#L105-L105](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L105-L105) (`clm_b39b57cee49e9ff1b17db2ac48e16e7a2b3d66fd2da8d38db51a63fe42cb2f02`)
- [observation/documented] ActiveAgentManager is a project-level service that stores the active AgentProfile, owns the AbstractAgentClient, and handles client start/stop/restart/dispose. -- evidence: [docs/ARCHITECTURE.md#L82-L86](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L82-L86), [docs/ARCHITECTURE.md#L77-L80](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L77-L80), [docs/ARCHITECTURE.md#L75-L75](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L75-L75) (`clm_7339f8d9961d29657d3a874ee10528a3ccee764aa73bc3f3561efb95c4fd9cea`)
- [observation/documented] Agent clients extend AbstractAgentClient, which provides session management (create, prompt, cancel), model selection, event streaming, and connection lifecycle; ACP clients include CopilotClient, JunieClient, KiroClient, and OpenCodeClient. -- evidence: [docs/ARCHITECTURE.md#L113-L113](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L113-L113), [docs/ARCHITECTURE.md#L124-L129](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L124-L129), [docs/ARCHITECTURE.md#L115-L118](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L115-L118) (`clm_8220283b6f24daf8fa48bee41bdffcb9db8036298ee3188d63201bfaf39d9bbc`)

## design-choices (2 claim(s))

- [observation/documented] For Copilot, built-in file operations are denied so all writes route through IntelliJ's Document API; denied permission kinds include edit, create, read, execute, and runInTerminal, with an auto-retry prompting the agent to use write_file instead. -- evidence: [DEVELOPMENT.md#L230-L245](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L230-L245), [DEVELOPMENT.md#L247-L249](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L247-L249), [DEVELOPMENT.md#L228-L228](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L228-L228) (`clm_b76aa0aae8156d0a5b9ddf1a202b2192834f734a633e1001149ec94f2d921dfe`)
- [observation/documented] Every file write via write_file triggers document commit, import optimization, and reformatting inside a single undoable command group on the EDT. -- evidence: [DEVELOPMENT.md#L271-L271](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L271-L271), [DEVELOPMENT.md#L265-L265](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L265-L265), [DEVELOPMENT.md#L267-L269](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L267-L269) (`clm_f0cffae3b4741825d2b7ae4b0ab69b235baf9102e1c5a22e4a31b1983a24692e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: tests run via Gradle (./gradlew test, :plugin-core:test, :mcp-server:test, with -Dinclude.integration=true for integration tests), and the project builds two plugin ZIPs (plugin-core and plugin-experimental) via buildPlugin tasks. -- evidence: [DEVELOPMENT.md#L40-L42](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L40-L42), [DEVELOPMENT.md#L180-L185](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L180-L185), [DEVELOPMENT.md#L33-L33](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L33-L33) (`clm_19242d54bb7e1cdfdaef9042ca269d2d7c1ed5697ce38e39aab5664405572981`)
- [observation/documented] Repository development practice: the maintainer reviews agent-authored changes mostly alone and seeks collaborators, believing important agent-made changes should get at least two pairs of human eyes. -- evidence: [README.md#L45-L49](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/README.md#L45-L49) (`clm_b2c9f88286e0deded5400c6cd97b75690e3b0527d5808ef103269b8ee36a9be0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The plugin communicates with agent CLIs over the Agent Client Protocol (JSON-RPC 2.0 via stdin/stdout); the MCP server JAR receives tool calls via stdio and forwards them to the PSI bridge over HTTP POST on localhost. -- evidence: [docs/ARCHITECTURE.md#L122-L122](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L122-L122), [docs/ARCHITECTURE.md#L160-L162](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L160-L162), [docs/ARCHITECTURE.md#L36-L45](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L36-L45) (`clm_12d51da79cca6258d6bdcead0501445207a230da1473ff296b1658fc725cadfb`)
- [observation/documented] The bridge port is shared via a file at ~/.copilot/psi-bridge.json, which the MCP server reads to reach the in-IDE HTTP service. -- evidence: [DEVELOPMENT.md#L259-L261](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L259-L261), [docs/ARCHITECTURE.md#L160-L162](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L160-L162) (`clm_5b755d2d5c4dfc5642a3599e739e4b79e063d95f4e0e5639d93e6ff5937931eb`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The plugin supports nine agents (Copilot, Claude Code, Codex, Kiro, Junie, OpenCode, Hermes Agent, Mistral Vibe, Goose) switchable with one click, each with its own connection settings, tool permissions, and custom instructions. -- evidence: [README.md#L21-L26](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/README.md#L21-L26), [README.md#L71-L72](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/README.md#L71-L72) (`clm_67a1bf0556e9e36bd2a6326ed8f753243c91478c542bafe7076ac745e34a7b72`)

## tools-permissions (1 claim(s))

- [observation/documented] Tool permissions support three modes: deny (never execute), ask (prompt user for approval), and allow (execute without prompt); sensitive operations like force git push, shell commands, file deletions, and out-of-root operations always require approval. -- evidence: [docs/ARCHITECTURE.md#L231-L235](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L231-L235), [docs/ARCHITECTURE.md#L225-L227](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L225-L227) (`clm_d790359331b940c57cec521de6257da3d43a38b8feff8d4d171fe6f4e74db636`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Development requires JDK 21 (Gradle JVM pinned via gradle.properties) and an installed, authenticated GitHub Copilot CLI; the Gradle wrapper JAR is not checked into the repository. -- evidence: [DEVELOPMENT.md#L7-L10](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L7-L10), [DEVELOPMENT.md#L12-L15](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L12-L15) (`clm_9ae6b247be1606d74b118c3c7b06de7a63f3fbb1e482cb2f4141326f43baafd3`)

## limitations (2 claim(s))

- [observation/documented] GitHub Copilot surfaces ACP resource references only as tagged-file metadata without content, so the plugin appends referenced file content as plain text after the user's message as a workaround. -- evidence: [DEVELOPMENT.md#L218-L220](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L218-L220), [DEVELOPMENT.md#L213-L216](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L213-L216) (`clm_2afd9d890f85af613bd60ce8a308e9b5930ea14e3d8641feeee40df233aa7d98`)
- [observation/documented] A prolonged EDT freeze (30+ seconds) can permanently stall the JCEF off-screen renderer; defenses include an EdtFreezeRecovery heartbeat monitor and a 2-second cooldown on file-open navigations to prevent cascading VCS git log/blame operations. -- evidence: [DEVELOPMENT.md#L281-L296](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L281-L296), [DEVELOPMENT.md#L275-L277](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L275-L277), [DEVELOPMENT.md#L300-L304](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L300-L304) (`clm_8a0096434ea9902cf184244dc53bbf0f4ca0357bb2109aee4f0ea8295c34a1e6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

