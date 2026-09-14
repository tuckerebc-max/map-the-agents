---
access: public
aliases: []
claim_ids:
- clm_07d62dc45074a543013b1918656f828a91c0770cd34ec093d73cb8f3564a1c58
- clm_0e2b0b10cb7ef6a90713d5daee8c342d5ee2d4a19631338f9a67c684b5422cbc
- clm_26438b7217de2457ef070ac80436b1d3bdec8b6addf04bd206dc5b0b30ee5724
- clm_3d4c28a2cdbc936efb309d08cd1cfb41ed66a1d4f7eeb93d63314c5628e939de
- clm_576bf082e937c9eb4c3190084c51dd6d379d895a2f4a4805aead5b0986865d46
- clm_627d10ad186d70aa5f8375151a2179d6cb7fe88605b62c94c0b8912107f4c91f
- clm_76ad319cdbe2a0ddfdba07295c4293a9d9aeba398c5ab8445d331ebb0ce8783e
- clm_820eecef5bb29c1eb29da45ae89a3ac435cd2eb3c000d12a5c4944b2d5c236b9
- clm_8c86acb7472e7b6e1c49d2ca389b6ffd69d5c739c1e4e9d3d02f86a0ef7dd934
- clm_98dc5828badc693b40697232184c9c8c410d7fddcaa784b928f9ef072c61481d
- clm_a66e8f031201e015b07633a1f7f76dc065cc41a0c9cb1db12459ea134c5fc762
- clm_d58328533dd38191c4459baa40904ff2bb3244c4dc8c9d046cda1c237bdc637c
- clm_dac6ff2d1ec44e8fc8a5594879e809f85356e2e6b0c0458088abdb226ad37cd2
maturity: draft
page_id: pg_bbbf3cdaca2c57be9792d8bf31f76939
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a5d39445c3335202af8a4235edbd6a05
title: sinameraji/kimiflare/README.md @ efe84a2e65dc
updated_at: '2026-09-14T02:40:52Z'
---

# sinameraji/kimiflare/README.md @ efe84a2e65dc

<!-- rcw:begin owner=source:src_a5d39445c3335202af8a4235edbd6a05 block=evidence -->
- A custom OpenAI-compatible endpoint can replace all Cloudflare paths via KIMIFLARE_BASE_URL/KIMIFLARE_API_KEY or config.json baseUrl/apiKey, making Cloudflare credentials optional. [@claim:clm_07d62dc45074a543013b1918656f828a91c0770cd34ec093d73cb8f3564a1c58]
- Three permission modes exist: plan (read-only tools only, blocking writes, mutating bash, MCP, and LSP renames), edit (default, prompts per mutating call), and auto (approves everything). [@claim:clm_0e2b0b10cb7ef6a90713d5daee8c342d5ee2d4a19631338f9a67c684b5422cbc]
- The default model is @cf/moonshotai/kimi-k2.7-code with 262k context, reasoning, tools, and vision; kimi-k2.6, kimi-k2.5, and @cf/zai-org/glm-5.2 are also available. [@claim:clm_26438b7217de2457ef070ac80436b1d3bdec8b6addf04bd206dc5b0b30ee5724]
- The tool requires Node.js >= 20 and is distributed via npm (installable globally or run with npx). [@claim:clm_3d4c28a2cdbc936efb309d08cd1cfb41ed66a1d4f7eeb93d63314c5628e939de]
- Agent-side activity logs are written as daily JSONL files under ~/.config/kimiflare/logs with 7-day retention pruned at startup; prompts and completions are deliberately excluded, with Gateway request_id for joining. [@claim:clm_576bf082e937c9eb4c3190084c51dd6d379d895a2f4a4805aead5b0986865d46]
- One-shot CLI usage supports -p prompts, --dangerously-allow-all for auto-approving mutating tools in scripts, and --reasoning to include chain-of-thought on stderr. [@claim:clm_627d10ad186d70aa5f8375151a2179d6cb7fe88605b62c94c0b8912107f4c91f]
- A JSONL-over-stdio RPC mode (--mode rpc) supports new_session, prompt, resolve_permission, and session resume for non-Node or isolated consumers. [@claim:clm_76ad319cdbe2a0ddfdba07295c4293a9d9aeba398c5ab8445d331ebb0ce8783e]
- Repository development practice: contributors fork, branch, run npm run typecheck and npm run build, commit with Conventional Commits, and open a PR; scripts include tsup build, tsx dev, and npm test. [@claim:clm_820eecef5bb29c1eb29da45ae89a3ac435cd2eb3c000d12a5c4944b2d5c236b9]
- KimiFlare is a terminal coding agent powered by Kimi K2.7 on Cloudflare Workers AI, running entirely on the user's own Cloudflare account, with optional AI Gateway routing. [@claim:clm_8c86acb7472e7b6e1c49d2ca389b6ffd69d5c739c1e4e9d3d02f86a0ef7dd934]
- Slash commands include /mode, /shell, /thinking, /theme, /resume, /compact, /init, /memory, /mcp, /cost, /gateway status, /update, and /help. [@claim:clm_98dc5828badc693b40697232184c9c8c410d7fddcaa784b928f9ef072c61481d]
- A headless SDK exposes createAgentSession with subscribe/prompt/steer/followUp/pause/resume/getStatus/getUsage, typed events, a custom permissionHandler, and optional memoryEnabled/lspEnabled/costAttribution flags. [@claim:clm_a66e8f031201e015b07633a1f7f76dc065cc41a0c9cb1db12459ea134c5fc762]
- Hooks fire shell commands at five turn points (PreToolUse, PostToolUse, UserPromptSubmit, Stop, PreCompact); non-zero exit on veto events cancels the action, with matcher regex, timeoutMs (default 30000), and enable/disable support. [@claim:clm_d58328533dd38191c4459baa40904ff2bb3244c4dc8c9d046cda1c237bdc637c]
- Log entries can be shipped to an OpenTelemetry collector via KIMIFLARE_OTEL_ENDPOINT over OTLP/HTTP, batched every 5s or 100 entries, best-effort so the agent loop is never blocked. [@claim:clm_dac6ff2d1ec44e8fc8a5594879e809f85356e2e6b0c0458088abdb226ad37cd2]
<!-- rcw:end owner=source:src_a5d39445c3335202af8a4235edbd6a05 block=evidence -->

## Researcher notes

