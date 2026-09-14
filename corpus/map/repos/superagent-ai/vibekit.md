# superagent-ai/vibekit

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c670afd2e332 @ 0959511238b49f06

## Summary (orientation draft, not independently verified)

Selected evidence records: VibeKit is described as a TypeScript SDK for running AI coding agents (Claude, Codex, Gemini, OpenCode) in secure sandboxes with GitHub integration. The core package is @vibe-kit/vibekit at version 0.0.43 with main entry dist/index.js.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] VibeKit is described as a TypeScript SDK for running AI coding agents (Claude, Codex, Gemini, OpenCode) in secure sandboxes with GitHub integration. -- evidence: [LLM.md#L4-L4](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L4-L4)
  - [observation/documented] The core package is @vibe-kit/vibekit at version 0.0.43 with main entry dist/index.js. -- evidence: [LLM.md#L6-L8](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L6-L8)
- components (1 claim(s)):
  - [observation/documented] The README advertises related packages installable as @vibe-kit/sdk (run coding agents in secure sandboxes) and @vibe-kit/auth (handle authentication flows for VibeKit-powered applications). -- evidence: [README.md#L48-L48](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L48-L48), [README.md#L50-L52](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L50-L52), [README.md#L59-L61](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L59-L61), [README.md#L63-L63](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L63-L63), [README.md#L57-L57](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L57-L57)
- design-choices (2 claim(s)):
  - [observation/documented] The CLI positions itself as a safety layer: it runs agent output in isolated Docker containers locally, auto-redacts secrets and API keys, and provides observability via real-time logs, traces, and metrics. -- evidence: [README.md#L32-L32](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L32-L32), [README.md#L36-L36](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L36-L36), [README.md#L34-L34](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L34-L34)
  - [observation/documented] The CLI claims to work entirely offline and locally with no cloud dependencies, and to support Claude Code, Gemini CLI, Grok CLI, Codex CLI, OpenCode, and more. -- evidence: [README.md#L40-L40](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L40-L40), [README.md#L38-L38](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/README.md#L38-L38)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The SDK uses a builder pattern: new VibeKit() configured via withAgent (type, provider, apiKey, model), withSandbox, withGithub, withSecrets, and withWorkingDirectory. -- evidence: [LLM.md#L263-L274](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L263-L274), [LLM.md#L40-L52](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L40-L52), [LLM.md#L94-L107](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L94-L107)
  - [observation/documented] Documented SDK methods include generateCode(prompt, mode) with 'code' or 'ask' modes, executeCommand, getHost(port), pause, resume, createPullRequest, and kill. -- evidence: [LLM.md#L113-L117](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L113-L117), [LLM.md#L291-L293](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L291-L293), [LLM.md#L286-L289](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L286-L289), [LLM.md#L279-L280](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L279-L280), [LLM.md#L63-L67](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L63-L67), [LLM.md#L119-L126](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L119-L126), [LLM.md#L282-L284](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L282-L284)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Sandbox providers are separate packages: @vibe-kit/e2b, @vibe-kit/daytona, @vibe-kit/northflank, @vibe-kit/cloudflare (Workers only), and @vibe-kit/modal. -- evidence: [LLM.md#L22-L27](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L22-L27), [LLM.md#L10-L15](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L10-L15)
  - [observation/documented] Common environment variables include OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, E2B_API_KEY, DAYTONA_API_KEY, NORTHFLANK_API_KEY, and GITHUB_TOKEN. -- evidence: [LLM.md#L546-L553](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L546-L553)
- limitations (1 claim(s)):
  - [observation/documented] Cloudflare sandboxes only work inside Cloudflare Workers and cannot be used in regular Node.js applications or other environments; they use Durable Object bindings instead of API keys. -- evidence: [LLM.md#L297-L297](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L297-L297), [LLM.md#L502-L508](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L502-L508), [LLM.md#L555-L555](https://github.com/superagent-ai/vibekit/blob/c670afd2e332037cd591209b7df1ff48ab7162ee/LLM.md#L555-L555)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](vibekit.detail.md)

Metadata and full claim list: [full detail](vibekit.detail.md)
Human notes ([notes](vibekit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
