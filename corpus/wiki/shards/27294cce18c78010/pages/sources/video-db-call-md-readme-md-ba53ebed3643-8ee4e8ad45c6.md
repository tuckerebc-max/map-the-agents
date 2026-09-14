---
access: public
aliases: []
claim_ids:
- clm_0928075ce4a76a9f991ba185fc89e97711028ea3bf3ac3f413500bb09277cbaf
- clm_133e45acc52c91edd4a294d6076351f201b3ec89b047cfccda84bd6c9a41cd99
- clm_1eb204a3db70618284403cbbb0b2d64a2fa37a325d4aa4673923c6d40effda84
- clm_1f182be3d50e3e31a8418b20090ea9c4eb222d31dfbb3bc71cc9d76262ea3655
- clm_2bff59c89b7480bfe29daae53f4c81361b1d51d878b5550f52b53b0fff2f2598
- clm_2e6f06e119543be536be7eab86eccb999cad9ec20bb2e0df2ece44bb969ceccb
- clm_326bdf7ceb967e7077d71210d4165f3616fe05694fa79c1d42c195ca026daa7d
- clm_374355244bf3d49d1badc1ef491f747ecd279f8ba12cc1a049bf8d47604aec0d
- clm_411c649ecc86d1080b39a80f066d5a95e67c2986f26f009d5cb253339d06ac0b
- clm_4739103950f61a872224960c203a8d7b4e8a41ea632396f4b75807a9857a0f97
- clm_4f15d69feb7bd154426550f34cdb5d2d6a71911269e33ef5f52b45d3283c2842
- clm_65bc015366746f57daf2b4e3a1786cfe1d91ca111c7e8d98ef7869c4877f5ee3
- clm_785c34b80d1676cd5ff06bc0fefa006b2215f0b335886417a9f1cfd06834614c
- clm_a214ade13e6cfd90e5b53473874667306efa3449cc319b0317c565f807d988ff
- clm_a790eeccad003cb24beb0da2af8c830415b59e7b669b81da539337e6d8884755
- clm_aa2a9591e82f3d0a44b7d413e82c95ebdad2ab9388b329ddb885808425f8f393
- clm_c8991f69a445ab256d5506385302d9bd2e5c5995222e1248b0928f14ace9b026
- clm_c905c242f1b3c92d274e8df8b75fd71aa3601a9ce9f38286ee355c1ab74c8314
- clm_ed3639c4bcafeb352be188f17c1a6a1b8df976646ce4704ab5a389501acfdf05
maturity: draft
page_id: pg_ce1610dcde9d516eb5de8ee4e8ad45c6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7f3f8b526c3d5d9d899d03091f5c6e54
title: video-db/call.md/README.md @ ba53ebed3643
updated_at: '2026-09-14T04:30:03Z'
---

# video-db/call.md/README.md @ ba53ebed3643

<!-- rcw:begin owner=source:src_7f3f8b526c3d5d9d899d03091f5c6e54 block=evidence -->
- After a meeting, the app generates three parallel extractions (narrative overview, participant-attributed key points, action items), exports markdown, and can send data to workflow webhooks like n8n and Zapier. [@claim:clm_0928075ce4a76a9f991ba185fc89e97711028ea3bf3ac3f413500bb09277cbaf]
- MCP servers are configured in Settings with a choice of stdio (local) or http (remote) transport, and tool results appear inline in an MCP Results panel during meetings. [@claim:clm_133e45acc52c91edd4a294d6076351f201b3ec89b047cfccda84bd6c9a41cd99]
- The local tRPC server binds to 127.0.0.1 only, accepts CORS from loopback origins, and every procedure except registration requires a valid access token; renderer windows run with contextIsolation and no Node integration. [@claim:clm_1eb204a3db70618284403cbbb0b2d64a2fa37a325d4aa4673923c6d40effda84]
- The renderer accesses MCP functionality via preload-exposed IPC APIs: window.electronAPI.mcp for server/tool operations and window.electronAPI.mcpOn for event subscriptions. [@claim:clm_1f182be3d50e3e31a8418b20090ea9c4eb222d31dfbb3bc71cc9d76262ea3655]
- The project targets users who want meeting capture with live AI assistance and post-meeting automation handoff, made by the VideoDB team with documentation at docs.videodb.io and community support via Discord and GitHub Issues. [@claim:clm_2bff59c89b7480bfe29daae53f4c81361b1d51d878b5550f52b53b0fff2f2598]
- Repository development practice: developers clone the repo, run npm install, rebuild native modules with npm run rebuild, and start dev mode with npm run dev; scripts exist for typecheck, unit tests, lint, database migrations, and platform-specific distributable builds. [@claim:clm_2e6f06e119543be536be7eab86eccb999cad9ec20bb2e0df2ece44bb969ceccb]
- A VideoDB API key is required for registration, and transcription and AI features require internet connectivity; Google Calendar integration is optional. [@claim:clm_326bdf7ceb967e7077d71210d4165f3616fe05694fa79c1d42c195ca026daa7d]
- The main process contains a copilot service layer with context-manager, conversation-metrics, nudge-engine, sales-copilot orchestrator, summary-generator, and transcript-buffer services, plus an MCP orchestration set including intent-detector and tool-aggregator services. [@claim:clm_374355244bf3d49d1badc1ef491f747ecd279f8ba12cc1a049bf8d47604aec0d]
- The stack includes Electron 42, TypeScript 5.8, React 19, Tailwind with shadcn/ui, tRPC 11 over a Hono HTTP server, Drizzle ORM with SQLite, Zustand, VideoDB SDK 0.3.0, MCP SDK 1.0.0, OpenAI SDK 6.19.0, and Vite. [@claim:clm_411c649ecc86d1080b39a80f066d5a95e67c2986f26f009d5cb253339d06ac0b]
- Repository development practice: cross-packaging a Windows x64 build from macOS is possible for structural verification using published prebuilds, but the README notes this does not replace native Windows testing or installer signing. [@claim:clm_4739103950f61a872224960c203a8d7b4e8a41ea632396f4b75807a9857a0f97]
- The app requires microphone and screen-recording permissions before the first recording; onboarding can skip permission setup, but recording stays unavailable until they are granted. [@claim:clm_4f15d69feb7bd154426550f34cdb5d2d6a71911269e33ef5f52b45d3283c2842]
- Credentials are protected with layered encryption: the SQLite user row is the sole authority for the VideoDB API key, Google tokens use Electron safeStorage, and MCP secrets use AES-256-GCM under a keychain-wrapped key, failing closed when strong OS-backed storage is unavailable. [@claim:clm_65bc015366746f57daf2b4e3a1786cfe1d91ca111c7e8d98ef7869c4877f5ee3]
- Recording is supported on macOS 12+ (Apple Silicon and Intel) and Windows x64; Linux and Windows ARM64 builds run the UI, MCP servers, workflows, history, and exports but reject recording because no capture binary exists, and no hosted Windows installer is published. [@claim:clm_785c34b80d1676cd5ff06bc0fefa006b2215f0b335886417a9f1cfd06834614c]
- During meetings the app offers dual-channel transcription, live AI assist suggestions, conversation metrics (talk ratio, WPM, monologue detection), coaching nudges, MCP auto-triggering, and bookmarking. [@claim:clm_a214ade13e6cfd90e5b53473874667306efa3449cc319b0317c565f807d988ff]
- Recordings are capped at 2 hours of active recording time, stop automatically with a warning 5 minutes prior, and paused or system-sleep time does not count toward the limit. [@claim:clm_a790eeccad003cb24beb0da2af8c830415b59e7b669b81da539337e6d8884755]
- Pre-meeting features include an AI-generated setup wizard with probing questions, a dynamic discussion checklist, and optional Google Calendar sync. [@claim:clm_aa2a9591e82f3d0a44b7d413e82c95ebdad2ab9388b329ddb885808425f8f393]
- Settings, meeting history, transcripts, and generated metadata are stored locally in a SQLite database under the application-data directory, with daily log files and encrypted Google OAuth tokens alongside. [@claim:clm_c8991f69a445ab256d5506385302d9bd2e5c5995222e1248b0928f14ace9b026]
- Call.md records meetings locally, transcribes in real time distinguishing the user from other participants, provides live in-call intelligence, and generates post-meeting summaries with action items. [@claim:clm_c905c242f1b3c92d274e8df8b75fd71aa3601a9ce9f38286ee355c1ab74c8314]
- Dual-channel audio (user mic vs system audio) is sent to VideoDB over WebSocket for real-time transcription, and the app sends a language_code parameter, falling back to the engine default rather than failing for unsupported languages. [@claim:clm_ed3639c4bcafeb352be188f17c1a6a1b8df976646ce4704ab5a389501acfdf05]
<!-- rcw:end owner=source:src_7f3f8b526c3d5d9d899d03091f5c6e54 block=evidence -->

## Researcher notes

