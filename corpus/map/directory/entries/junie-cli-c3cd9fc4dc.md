# Junie CLI (`junie-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: unknown
- License: Proprietary (© JetBrains s.r.o. — subject to JetBrains AI Service Terms)
- Language: unknown
- Interface: platforms=Autonomous, CLI, IDE; install=curl -fsSL https://junie.jetbrains.com/install.sh | bash; Homebrew (brew tap jetbrains-junie/junie && brew install junie); npm install -g @jetbrains/junie
- Model providers: JetBrains Account, Junie API Key, BYOK: Anthropic, OpenAI, Google, xAI, OpenRouter, Copilot (10+ models including GPT-5.6, Claude Opus 4.8, Gemini 3.1 Pro, Grok 4.5)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Agent Skills packages and /commands shared across CLI + IDE via ACP) (yes)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: yes (Advanced Plan Mode writes structured plan — requirements, design, delivery — before touching code; plans stored in .junie/plans; strategy: plan on Opus, implement on Flash) (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): LLM-agnostic coding agent powered by IntelliJ IDEA Engine (top performer on SWE-Rebench); model-agnostic BYOK with cost-efficient 'plan on Opus, implement on Flash' strategy; Live Prompting to steer agent mid-task in real time; remote async execution via CLI + web app; human-in-the-loop with dynamic allowlist; SOC 2 certified.

(captured site page body (agents/junie-cli.md), not a verified repo-code finding)
Junie CLI brings JetBrains' coding agent out of the IDE and into terminals, CI, and a phone-monitorable web app. Plans are first-class artifacts — written to .junie/plans before any code changes, reviewable and committable — which enables the deliberate strategy of planning on a frontier model and implementing on a cheap one. Live Prompting lets the user redirect a running task without restarting it. Skills packages and /commands sync between CLI and IDE over ACP, a GitHub Action auto-responds to issues, PRs, and CI failures, and remote execution continues server-side while the user checks progress from another device. Pricing starts at 5 free credits with BYOK at provider rates and tops out at AI Ultimate $25/user/month.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/junie-cli.md)
