# sinameraji/kimiflare -- full detail

[Back to orientation](kimiflare.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sinameraji/kimiflare/efe84a2e65dc04bded92323911df057902de9f7a/7bbdb59552fca939.json](../../../wiki/dossiers/sinameraji/kimiflare/efe84a2e65dc04bded92323911df057902de9f7a/7bbdb59552fca939.json)

## specifications (2 claim(s))

- [observation/documented] KimiFlare is a terminal coding agent powered by Kimi K2.7 on Cloudflare Workers AI, running entirely on the user's own Cloudflare account, with optional AI Gateway routing. -- evidence: [README.md#L14-L17](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L14-L17), [README.md#L28-L28](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L28-L28) (`clm_8c86acb7472e7b6e1c49d2ca389b6ffd69d5c739c1e4e9d3d02f86a0ef7dd934`)
- [observation/documented] The default model is @cf/moonshotai/kimi-k2.7-code with 262k context, reasoning, tools, and vision; kimi-k2.6, kimi-k2.5, and @cf/zai-org/glm-5.2 are also available. -- evidence: [README.md#L129-L130](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L129-L130), [README.md#L127-L127](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L127-L127) (`clm_26438b7217de2457ef070ac80436b1d3bdec8b6addf04bd206dc5b0b30ee5724`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] A custom OpenAI-compatible endpoint can replace all Cloudflare paths via KIMIFLARE_BASE_URL/KIMIFLARE_API_KEY or config.json baseUrl/apiKey, making Cloudflare credentials optional. -- evidence: [README.md#L115-L121](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L115-L121), [README.md#L111-L113](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L111-L113), [README.md#L101-L103](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L101-L103) (`clm_07d62dc45074a543013b1918656f828a91c0770cd34ec093d73cb8f3564a1c58`)
- [observation/documented] Hooks fire shell commands at five turn points (PreToolUse, PostToolUse, UserPromptSubmit, Stop, PreCompact); non-zero exit on veto events cancels the action, with matcher regex, timeoutMs (default 30000), and enable/disable support. -- evidence: [README.md#L355-L361](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L355-L361), [README.md#L363-L366](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L363-L366), [README.md#L411-L420](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L411-L420) (`clm_d58328533dd38191c4459baa40904ff2bb3244c4dc8c9d046cda1c237bdc637c`)
- [inference/documented] Log entries can be shipped to an OpenTelemetry collector via KIMIFLARE_OTEL_ENDPOINT over OTLP/HTTP, batched every 5s or 100 entries, best-effort so the agent loop is never blocked. -- evidence: [README.md#L325-L330](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L325-L330), [README.md#L342-L347](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L342-L347) (`clm_dac6ff2d1ec44e8fc8a5594879e809f85356e2e6b0c0458088abdb226ad37cd2`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors fork, branch, run npm run typecheck and npm run build, commit with Conventional Commits, and open a PR; scripts include tsup build, tsx dev, and npm test. -- evidence: [README.md#L439-L445](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L439-L445), [README.md#L447-L451](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L447-L451), [README.md#L455-L460](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L455-L460) (`clm_820eecef5bb29c1eb29da45ae89a3ac435cd2eb3c000d12a5c4944b2d5c236b9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] A headless SDK exposes createAgentSession with subscribe/prompt/steer/followUp/pause/resume/getStatus/getUsage, typed events, a custom permissionHandler, and optional memoryEnabled/lspEnabled/costAttribution flags. -- evidence: [README.md#L180-L186](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L180-L186), [README.md#L149-L150](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L149-L150), [README.md#L162-L165](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L162-L165) (`clm_a66e8f031201e015b07633a1f7f76dc065cc41a0c9cb1db12459ea134c5fc762`)
- [observation/documented] A JSONL-over-stdio RPC mode (--mode rpc) supports new_session, prompt, resolve_permission, and session resume for non-Node or isolated consumers. -- evidence: [README.md#L242-L244](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L242-L244), [README.md#L251-L254](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L251-L254), [README.md#L246-L249](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L246-L249), [README.md#L215-L215](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L215-L215) (`clm_76ad319cdbe2a0ddfdba07295c4293a9d9aeba398c5ab8445d331ebb0ce8783e`)
- [observation/documented] Slash commands include /mode, /shell, /thinking, /theme, /resume, /compact, /init, /memory, /mcp, /cost, /gateway status, /update, and /help. -- evidence: [README.md#L266-L281](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L266-L281) (`clm_98dc5828badc693b40697232184c9c8c410d7fddcaa784b928f9ef072c61481d`)
- [observation/documented] One-shot CLI usage supports -p prompts, --dangerously-allow-all for auto-approving mutating tools in scripts, and --reasoning to include chain-of-thought on stderr. -- evidence: [README.md#L139-L143](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L139-L143) (`clm_627d10ad186d70aa5f8375151a2179d6cb7fe88605b62c94c0b8912107f4c91f`)

## memory-state (2 claim(s))

- [observation/documented] Agent-side activity logs are written as daily JSONL files under ~/.config/kimiflare/logs with 7-day retention pruned at startup; prompts and completions are deliberately excluded, with Gateway request_id for joining. -- evidence: [README.md#L296-L299](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L296-L299), [README.md#L301-L304](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L301-L304) (`clm_576bf082e937c9eb4c3190084c51dd6d379d895a2f4a4805aead5b0986865d46`)
- [observation/documented] In Camouflage UI mode, every inbound event is persisted to a SQLite WAL database (~/.config/kimiflare/camouflage-sessions.db), making sessions replayable via a --replay flag. -- evidence: [CAMOUFLAGE_MIGRATION.md#L128-L133](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/CAMOUFLAGE_MIGRATION.md#L128-L133) (`clm_3d14e3506855e00df38745874bb293139acd35244e80b9d9cd799a9989e41e92`)

## orchestration (1 claim(s))

- [observation/documented] A multi-agent feature (PR #220, v0.29.0) uses an AgentOrchestrator with per-agent message buffers and built-in research/coding/generalist agents. -- evidence: [incident-report-2026-05-01-multi-agent-resume-regression.md#L22-L22](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/incident-report-2026-05-01-multi-agent-resume-regression.md#L22-L22), [incident-report-2026-05-01-multi-agent-resume-regression.md#L18-L18](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/incident-report-2026-05-01-multi-agent-resume-regression.md#L18-L18), [incident-report-2026-05-01-multi-agent-resume-regression.md#L14-L14](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/incident-report-2026-05-01-multi-agent-resume-regression.md#L14-L14) (`clm_d9b8792bee3ab4db4dc5b5adf94a8cd63853fa1d4d88b126ae3fad6ab5dc2595`)

## tools-permissions (1 claim(s))

- [observation/documented] Three permission modes exist: plan (read-only tools only, blocking writes, mutating bash, MCP, and LSP renames), edit (default, prompts per mutating call), and auto (approves everything). -- evidence: [README.md#L40-L51](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L40-L51) (`clm_0e2b0b10cb7ef6a90713d5daee8c342d5ee2d4a19631338f9a67c684b5422cbc`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool requires Node.js >= 20 and is distributed via npm (installable globally or run with npx). -- evidence: [README.md#L5-L12](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L5-L12), [README.md#L70-L73](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L70-L73), [README.md#L83-L83](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L83-L83) (`clm_3d4c28a2cdbc936efb309d08cd1cfb41ed66a1d4f7eeb93d63314c5628e939de`)
- [observation/documented] The experimental Camouflage renderer is an external package (camouflage-tui, e.g. 2.1.0-beta.1 as an optionalDependency) whose upstream capabilities gate some features like renderer-side mouse events. -- evidence: [CAMOUFLAGE_MIGRATION.md#L136-L138](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/CAMOUFLAGE_MIGRATION.md#L136-L138), [CAMOUFLAGE_MIGRATION.md#L141-L154](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/CAMOUFLAGE_MIGRATION.md#L141-L154) (`clm_cea5a85715c07cf110ae0802d469ae9def4b93a50072fecbff71061f0a73329d`)

## limitations (1 claim(s))

- [observation/documented] An incident report documents that v0.29.0's multi-agent mode broke legacy /resume context, omitted system prompts for built-in agents, and crashed auto-compact; a fix was implemented but pending merge at report time. -- evidence: [incident-report-2026-05-01-multi-agent-resume-regression.md#L3-L8](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/incident-report-2026-05-01-multi-agent-resume-regression.md#L3-L8), [incident-report-2026-05-01-multi-agent-resume-regression.md#L18-L18](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/incident-report-2026-05-01-multi-agent-resume-regression.md#L18-L18), [incident-report-2026-05-01-multi-agent-resume-regression.md#L20-L20](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/incident-report-2026-05-01-multi-agent-resume-regression.md#L20-L20), [incident-report-2026-05-01-multi-agent-resume-regression.md#L16-L16](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/incident-report-2026-05-01-multi-agent-resume-regression.md#L16-L16) (`clm_1e20bc3a0b273bd7210aaf6f7b0403fe91970a482a0f70ddd8ce043006ea3741`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

