# video-db/call.md

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ba53ebed3643 @ b93e3320b0cfc245

## Summary (orientation draft, not independently verified)

The snapshot contains only README content for Call.md, an Electron desktop meeting-recording and AI-copilot app by VideoDB. Claims below cover documented product features, architecture, security model, platform limits, and developer workflows; no source code is present in the evidence.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (4 claim(s)):
  - [observation/documented] Call.md records meetings locally, transcribes in real time distinguishing the user from other participants, provides live in-call intelligence, and generates post-meeting summaries with action items. -- evidence: [README.md#L82-L82](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L82-L82)
  - [observation/documented] During meetings the app offers dual-channel transcription, live AI assist suggestions, conversation metrics (talk ratio, WPM, monologue detection), coaching nudges, MCP auto-triggering, and bookmarking. -- evidence: [README.md#L87-L94](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L87-L94)
- components (1 claim(s)):
  - [observation/documented] The main process contains a copilot service layer with context-manager, conversation-metrics, nudge-engine, sales-copilot orchestrator, summary-generator, and transcript-buffer services, plus an MCP orchestration set including intent-detector and tool-aggregator services. -- evidence: [README.md#L253-L302](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L253-L302)
- design-choices (3 claim(s)):
  - [observation/documented] Credentials are protected with layered encryption: the SQLite user row is the sole authority for the VideoDB API key, Google tokens use Electron safeStorage, and MCP secrets use AES-256-GCM under a keychain-wrapped key, failing closed when strong OS-backed storage is unavailable. -- evidence: [README.md#L381-L412](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L381-L412)
  - [observation/documented] The local tRPC server binds to 127.0.0.1 only, accepts CORS from loopback origins, and every procedure except registration requires a valid access token; renderer windows run with contextIsolation and no Node integration. -- evidence: [README.md#L381-L412](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L381-L412)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: developers clone the repo, run npm install, rebuild native modules with npm run rebuild, and start dev mode with npm run dev; scripts exist for typecheck, unit tests, lint, database migrations, and platform-specific distributable builds. -- evidence: [README.md#L187-L190](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L187-L190), [README.md#L171-L175](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L171-L175), [README.md#L182-L185](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L182-L185), [README.md#L196-L208](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L196-L208), [README.md#L177-L180](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L177-L180)
  - [observation/documented] Repository development practice: cross-packaging a Windows x64 build from macOS is possible for structural verification using published prebuilds, but the README notes this does not replace native Windows testing or installer signing. -- evidence: [README.md#L220-L227](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L220-L227)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The renderer accesses MCP functionality via preload-exposed IPC APIs: window.electronAPI.mcp for server/tool operations and window.electronAPI.mcpOn for event subscriptions. -- evidence: [README.md#L308-L309](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L308-L309), [README.md#L306-L306](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L306-L306)
  - [observation/documented] MCP servers are configured in Settings with a choice of stdio (local) or http (remote) transport, and tool results appear inline in an MCP Results panel during meetings. -- evidence: [README.md#L241-L241](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L241-L241), [README.md#L243-L245](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L243-L245), [README.md#L247-L247](https://github.com/video-db/call.md/blob/ba53ebed3643920bb9ef9d08ee33e59bd708c930/README.md#L247-L247)
- memory-state (1 claim(s)):
More evidence: [full detail](call.md.detail.md)

Metadata and full claim list: [full detail](call.md.detail.md)
Human notes ([notes](call.md.notes.md), never overwritten by build)

[Back to map index](../../index.md)
