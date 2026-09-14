# klaatai/klaatcode -- full detail

[Back to orientation](klaatcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/klaatai/klaatcode/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/ff92e7ef075c9d71.json](../../../wiki/dossiers/klaatai/klaatcode/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/ff92e7ef075c9d71.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (5 claim(s))

- [observation/documented] The client is described as a thin terminal to the hosted Klaatu service, which performs routing, model health tracking, pricing, and code-graph indexing server-side. -- evidence: [README.md#L46-L46](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L46-L46) (`clm_9e1ce6e90d5000dc0b22dcb63c983acdf3eaf601982f9e03dbfa878e84c4e251`)
- [observation/documented] Requests are classified and routed across cost tiers (nano, fast, code, reason, heavy, opt-in titan), with automatic escalation on harder tasks and de-escalation when the daily cap is spent. -- evidence: [README.md#L150-L150](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L150-L150), [README.md#L169-L169](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L169-L169), [README.md#L160-L167](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L160-L167) (`clm_7bf1525dc58d12798b333e1825a85db76aa1a16e48902b4f67cf4475afabe279`)
- [observation/documented] Plan mode (Tab) restricts the model to read-only tools until the user approves a plan, after which it returns to Build mode with the full toolset. -- evidence: [README.md#L196-L196](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L196-L196) (`clm_580d1987a554f294d8ac11e7b8d9c61d7c68402a63ded77aadea7879f81ef24a`)
- [observation/documented] Cost guards include a burn-rate monitor warning at 3x session average, per-task/per-phase cost breakdowns, per-phase budgets that pause stuck exploration, hard session caps, and a doom-loop breaker after three repeated identical tool rounds. -- evidence: [README.md#L249-L253](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L249-L253) (`clm_6fe93e93cdf58c4c884daca54235cf532b70bb1deb541e03e8d9f99fd66a6b2f`)
- [observation/documented] Telemetry sends four headers per request (client version, platform, install channel, random install UUID); opting out via KLAATAI_TELEMETRY=0, DO_NOT_TRACK=1, or config stops the install id but version and platform still travel. -- evidence: [README.md#L524-L526](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L524-L526), [README.md#L534-L534](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L534-L534), [README.md#L511-L511](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L511-L511), [README.md#L520-L520](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L520-L520), [README.md#L513-L518](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L513-L518), [README.md#L530-L532](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L530-L532) (`clm_c5b54264f3e19b35ad4f7e36c8794ecb73588247c7863f2a2d4f545c6a863302`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions follow CONTRIBUTING.md for dev setup and the PR process, and `bun run bench:selfcheck` must pass before a PR is reviewed. -- evidence: [README.md#L542-L542](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L542-L542) (`clm_27998476abe03ae93094a549e7da228c0e886ee3b91b6445304aa5ab194440d3`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are reusable prompt templates saved as .md files in .klaatai/skills/ (project) or ~/.klaatai/skills/ (global), invoked via /skill commands; hooks run shell commands on lifecycle events and before_tool hooks can block tool calls. -- evidence: [README.md#L327-L327](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L327-L327), [README.md#L304-L304](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L304-L304), [README.md#L306-L310](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L306-L310), [README.md#L314-L314](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L314-L314) (`clm_681e867f7714c2c4245ad762aeb76084c4ecc1b2af0f96e0db8ba020d458ae3a`)

## interfaces (4 claim(s))

- [observation/documented] The CLI can run as an HTTP server (`klaatcode serve --port 4200`) exposing /v1/health, /v1/info, /v1/chat and /v1/run with SSE streaming, and `klaatcode web` serves a browser UI on the same server. -- evidence: [README.md#L425-L427](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L425-L427), [README.md#L434-L434](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L434-L434), [README.md#L429-L432](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L429-L432) (`clm_4f1114463af60f96c2dd3515bab3e48424ba46e195831b6b521f16e748d6915b`)
- [observation/documented] The CLI is a full MCP client supporting stdio and Streamable HTTP transports, with OAuth 2.1 (discovery, dynamic client registration, PKCE) for remote servers requiring auth, managed via /mcp. -- evidence: [README.md#L286-L287](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L286-L287), [README.md#L289-L289](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L289-L289), [README.md#L284-L284](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L284-L284) (`clm_edc5877a104e794d659714cc7d255db91450c4a697a2e7e66109d6a31844a86c`)
- [observation/documented] Headless mode (`klaatcode run`) supports --json JSONL event streams, --output-schema JSON Schema validation with exit 2 on mismatch, --allow-tools autonomy bounding, --max-turns, and deterministic exit codes 0-4. -- evidence: [CHANGELOG.md#L54-L60](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/CHANGELOG.md#L54-L60) (`clm_986daad22c33ed4cc8ce80d341d54b39f65788b8be0fd639b172612f62544c9a`)
- [observation/documented] Authentication is browser-based OAuth against a KlaatAI account storing a short-lived JWT and refresh token in ~/.klaatai/credentials.json (mode 0600), with silent background refresh; no API keys are required. -- evidence: [README.md#L538-L538](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L538-L538) (`clm_af2dcb4ae650dd0fa3d4de6887d67f46dd0db37736e24c0f2bd78b378199e5cd`)

## memory-state (2 claim(s))

- [observation/documented] Sessions are saved as transcripts in ~/.klaatai/sessions/ with /sessions, /resume, and /export commands; a background pass distills durable project and user facts into ~/.klaatai/memory/ that loads at session start. -- evidence: [CHANGELOG.md#L12-L14](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/CHANGELOG.md#L12-L14), [README.md#L259-L264](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L259-L264), [README.md#L257-L257](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L257-L257) (`clm_ea3c147689496afb15e4a14a0c468b77e8f11b6bdc6b0f84ddcc1faf81641e8a`)
- [observation/documented] Context management includes mechanical per-request compaction, noise-filtered command output, attention-ordered history, tier-scaled compaction budgets, and a self-check that snapshots critical state before summarizing and verifies it after. -- evidence: [README.md#L236-L243](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L236-L243) (`clm_44e59c9d03413aa303d01f19485bc0050ecb37b81d06e9b98b306b2d6538d03d`)

## orchestration (1 claim(s))

- [observation/documented] The agent can delegate scoped work to sub-agents with their own context, optionally in the background, with results injected into the conversation when they finish and a chip tracking running background agents. -- evidence: [README.md#L230-L230](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L230-L230), [README.md#L222-L222](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L222-L222) (`clm_bfafe847a60338fc40445f4880e3c2364b0e62ce62a01575659f6b0effdd538f`)

## tools-permissions (2 claim(s))

- [observation/documented] A three-layer permission model runs safe read-only tools silently, prompts for everything else with allow/deny options persisted to ~/.klaatai/permissions.json, supports glob command allow/deny lists, and sandboxes writes to the project directory with hard-denied system paths. -- evidence: [README.md#L270-L272](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L270-L272), [README.md#L268-L268](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L268-L268), [README.md#L274-L280](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L274-L280) (`clm_e35bfd4ee002800c8e2dc5141be599d96c36368ca5e1a68112b5aabe61172260`)
- [observation/documented] Built-in tools include file read/write/edit, apply_patch, glob/grep, permission-gated run_command, web fetch/search, todo tracking, ask_user, delegate_task, code-graph queries, impact_check, and five browser tools. -- evidence: [README.md#L200-L218](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L200-L218) (`clm_a6776255bee0237e4e7f2aa173566230c77731f47d6ebec20dcca0a5cad22048`)

## evaluation (1 claim(s))

- [observation/documented] A benchmark harness runs 33 fixtures against KlaatCode, Claude Code, opencode, Cursor, and Grok Build; the reported latest run (2026-07-20) shows 33/33 solved at $0.027 per solved task and 51.7K tokens per task, with reproduction instructions via bun run bench. -- evidence: [README.md#L69-L74](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L69-L74), [README.md#L80-L85](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L80-L85), [README.md#L63-L63](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L63-L63), [README.md#L67-L67](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L67-L67) (`clm_1d9e5b84993a03d2aef27eb296ff41cc5abccde460ab4e6905c76d2b10b6f372`)

## dependencies (1 claim(s))

- [observation/documented] Installed binaries are standalone compiled executables requiring no Node or Bun runtime at runtime; npm installation requires Node >= 18 or Bun >= 1, and the repo uses bun for development and benchmarking. -- evidence: [README.md#L93-L101](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L93-L101), [README.md#L80-L85](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L80-L85), [README.md#L91-L91](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L91-L91) (`clm_5824bfb8c38f0a681664124952d6ef526ad4f6755e0e3bede5aca6a3dd28b33a`)

## limitations (1 claim(s))

- [observation/documented] Semantic code search via project_semantic_search is noted as a Pro-tier feature, and the titan tier is capped per day (Starter access only during a promo window). -- evidence: [README.md#L200-L218](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L200-L218), [README.md#L160-L167](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L160-L167) (`clm_48b646588cce51f3d56c35d4ac9c5009b848a5778717ed6e048d0f26f382acc5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

