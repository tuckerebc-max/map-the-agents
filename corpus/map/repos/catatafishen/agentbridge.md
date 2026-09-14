# catatafishen/agentbridge

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 124f7c082dc3 @ b1b11b5b76643edd

## Summary (orientation draft, not independently verified)

AgentBridge is a JetBrains IDE plugin that connects AI coding agents to IntelliJ platform APIs via 120+ MCP tools, using ACP/JSON-RPC over stdio to agent CLIs and an HTTP bridge to an in-IDE PSI service. Evidence covers architecture, agent support, permissions, and development workflows. Evidence coverage: 150 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 57 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AgentBridge is a JetBrains IDE plugin that bridges AI coding agents to IntelliJ platform APIs through 120+ native MCP tools, letting agents use inspections, refactorings, test runner, build system, and Git. -- evidence: [README.md#L14-L17](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/README.md#L14-L17)
- components (3 claim(s)):
  - [observation/documented] PsiBridgeService is a project-level HTTP server exposing 92 IntelliJ-native MCP tools; it starts on a dynamic localhost port and accesses PSI, VFS, Document API, and Git4Idea. -- evidence: [docs/ARCHITECTURE.md#L107-L109](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L107-L109), [docs/ARCHITECTURE.md#L105-L105](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L105-L105)
  - [observation/documented] ActiveAgentManager is a project-level service that stores the active AgentProfile, owns the AbstractAgentClient, and handles client start/stop/restart/dispose. -- evidence: [docs/ARCHITECTURE.md#L82-L86](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L82-L86), [docs/ARCHITECTURE.md#L77-L80](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L77-L80), [docs/ARCHITECTURE.md#L75-L75](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L75-L75)
- design-choices (2 claim(s)):
  - [observation/documented] For Copilot, built-in file operations are denied so all writes route through IntelliJ's Document API; denied permission kinds include edit, create, read, execute, and runInTerminal, with an auto-retry prompting the agent to use write_file instead. -- evidence: [DEVELOPMENT.md#L230-L245](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L230-L245), [DEVELOPMENT.md#L247-L249](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L247-L249), [DEVELOPMENT.md#L228-L228](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L228-L228)
  - [observation/documented] Every file write via write_file triggers document commit, import optimization, and reformatting inside a single undoable command group on the EDT. -- evidence: [DEVELOPMENT.md#L271-L271](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L271-L271), [DEVELOPMENT.md#L265-L265](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L265-L265), [DEVELOPMENT.md#L267-L269](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L267-L269)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: tests run via Gradle (./gradlew test, :plugin-core:test, :mcp-server:test, with -Dinclude.integration=true for integration tests), and the project builds two plugin ZIPs (plugin-core and plugin-experimental) via buildPlugin tasks. -- evidence: [DEVELOPMENT.md#L40-L42](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L40-L42), [DEVELOPMENT.md#L180-L185](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L180-L185), [DEVELOPMENT.md#L33-L33](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L33-L33)
  - [observation/documented] Repository development practice: the maintainer reviews agent-authored changes mostly alone and seeks collaborators, believing important agent-made changes should get at least two pairs of human eyes. -- evidence: [README.md#L45-L49](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/README.md#L45-L49)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The plugin communicates with agent CLIs over the Agent Client Protocol (JSON-RPC 2.0 via stdin/stdout); the MCP server JAR receives tool calls via stdio and forwards them to the PSI bridge over HTTP POST on localhost. -- evidence: [docs/ARCHITECTURE.md#L122-L122](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L122-L122), [docs/ARCHITECTURE.md#L160-L162](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L160-L162), [docs/ARCHITECTURE.md#L36-L45](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L36-L45)
  - [observation/documented] The bridge port is shared via a file at ~/.copilot/psi-bridge.json, which the MCP server reads to reach the in-IDE HTTP service. -- evidence: [DEVELOPMENT.md#L259-L261](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/DEVELOPMENT.md#L259-L261), [docs/ARCHITECTURE.md#L160-L162](https://github.com/catatafishen/agentbridge/blob/124f7c082dc33a583a9f834b4c4765133e3d745c/docs/ARCHITECTURE.md#L160-L162)
- memory-state: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agentbridge.detail.md)

Metadata and full claim list: [full detail](agentbridge.detail.md)
Human notes ([notes](agentbridge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
