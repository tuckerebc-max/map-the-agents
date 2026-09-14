# sinameraji/kimiflare

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit efe84a2e65dc @ 7bbdb59552fca939

## Summary (orientation draft, not independently verified)

KimiFlare is a terminal coding agent (Node.js ≥20, TypeScript) powered by Kimi K2.7 on Cloudflare Workers AI, with optional AI Gateway routing, a headless SDK, RPC mode, hooks, and an experimental Camouflage UI renderer. Evidence is mostly README documentation plus a migration tracker and an incident report; no evaluation or runtime code is shown. Evidence coverage: 138 of 267 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 55 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] KimiFlare is a terminal coding agent powered by Kimi K2.7 on Cloudflare Workers AI, running entirely on the user's own Cloudflare account, with optional AI Gateway routing. -- evidence: [README.md#L14-L17](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L14-L17), [README.md#L28-L28](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L28-L28)
  - [observation/documented] The default model is @cf/moonshotai/kimi-k2.7-code with 262k context, reasoning, tools, and vision; kimi-k2.6, kimi-k2.5, and @cf/zai-org/glm-5.2 are also available. -- evidence: [README.md#L129-L130](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L129-L130), [README.md#L127-L127](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L127-L127)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] A custom OpenAI-compatible endpoint can replace all Cloudflare paths via KIMIFLARE_BASE_URL/KIMIFLARE_API_KEY or config.json baseUrl/apiKey, making Cloudflare credentials optional. -- evidence: [README.md#L115-L121](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L115-L121), [README.md#L111-L113](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L111-L113), [README.md#L101-L103](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L101-L103)
  - [observation/documented] Hooks fire shell commands at five turn points (PreToolUse, PostToolUse, UserPromptSubmit, Stop, PreCompact); non-zero exit on veto events cancels the action, with matcher regex, timeoutMs (default 30000), and enable/disable support. -- evidence: [README.md#L355-L361](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L355-L361), [README.md#L363-L366](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L363-L366), [README.md#L411-L420](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L411-L420)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, branch, run npm run typecheck and npm run build, commit with Conventional Commits, and open a PR; scripts include tsup build, tsx dev, and npm test. -- evidence: [README.md#L439-L445](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L439-L445), [README.md#L447-L451](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L447-L451), [README.md#L455-L460](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L455-L460)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] A headless SDK exposes createAgentSession with subscribe/prompt/steer/followUp/pause/resume/getStatus/getUsage, typed events, a custom permissionHandler, and optional memoryEnabled/lspEnabled/costAttribution flags. -- evidence: [README.md#L180-L186](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L180-L186), [README.md#L149-L150](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L149-L150), [README.md#L162-L165](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L162-L165)
  - [observation/documented] A JSONL-over-stdio RPC mode (--mode rpc) supports new_session, prompt, resolve_permission, and session resume for non-Node or isolated consumers. -- evidence: [README.md#L242-L244](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L242-L244), [README.md#L251-L254](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L251-L254), [README.md#L246-L249](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L246-L249), [README.md#L215-L215](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L215-L215)
- memory-state (2 claim(s)):
  - [observation/documented] Agent-side activity logs are written as daily JSONL files under ~/.config/kimiflare/logs with 7-day retention pruned at startup; prompts and completions are deliberately excluded, with Gateway request_id for joining. -- evidence: [README.md#L296-L299](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L296-L299), [README.md#L301-L304](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/README.md#L301-L304)
  - [observation/documented] In Camouflage UI mode, every inbound event is persisted to a SQLite WAL database (~/.config/kimiflare/camouflage-sessions.db), making sessions replayable via a --replay flag. -- evidence: [CAMOUFLAGE_MIGRATION.md#L128-L133](https://github.com/sinameraji/kimiflare/blob/efe84a2e65dc04bded92323911df057902de9f7a/CAMOUFLAGE_MIGRATION.md#L128-L133)
- orchestration (1 claim(s)):
More evidence: [full detail](kimiflare.detail.md)

Metadata and full claim list: [full detail](kimiflare.detail.md)
Human notes ([notes](kimiflare.notes.md), never overwritten by build)

[Back to map index](../../index.md)
