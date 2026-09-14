# jazzenchen/vibearound

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1654259bbb0e @ 7297fd70b15bc22e

## Summary (orientation draft, not independently verified)

VibeAround is a local hub for AI coding agents (Claude Code, Codex CLI, Gemini CLI, and others) providing agent launch with API profiles, an API bridge between provider shapes, host-side web search, IM channel plugins, web terminal/hub, tunnels, and live preview, with execution kept on the local machine. Evidence coverage: 125 of 200 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 131 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The API bridge (va-ai-api-bridge, VAAAB) translates between OpenAI Responses, OpenAI Chat Completions, Anthropic Messages, and Gemini Generate Content shapes using profile-scoped local routes and model aliases. -- evidence: [README.md#L87-L95](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L87-L95), [README.md#L112-L114](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L112-L114), [README.md#L97-L97](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L97-L97)
  - [observation/documented] Host-side web search runs through the standalone va-search-tool project, supporting Exa, Tavily, Grok/xAI, and Brave Search, and can run as a stdio plugin, CLI, or local /v1/search HTTP service. -- evidence: [README.md#L124-L124](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L124-L124), [README.md#L120-L120](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L120-L120), [README.md#L126-L130](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L126-L130)
- design-choices (2 claim(s)):
  - [observation/documented] The security model keeps execution local: the daemon listens on loopback unless a tunnel is enabled, dashboard APIs require a local auth token, tunnel owner surfaces require browser pairing, and Share links use six-digit access codes expiring after 10 minutes. -- evidence: [README.md#L323-L330](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L323-L330)
  - [observation/documented] Server Share previews are a page-preview transport forwarding authenticated GET/HEAD paths only; writes, protocol upgrades, service workers, WebSockets, and HMR are unsupported, and /va/*, owner pages, chat, and review controls are excluded. -- evidence: [README.md#L323-L330](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L323-L330), [README.md#L253-L256](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L253-L256)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: local development is done from the src directory with bun install, bun run prebuild, and bun run dev; Windows and Linux packages are built by GitHub Actions. -- evidence: [README.md#L357-L357](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L357-L357), [README.md#L379-L384](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L379-L384)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] VibeAround exposes local agents as OpenAI/Anthropic-compatible endpoints under /local-agent/{agent_id}/{profile_id}/..., including responses, chat completions, messages, and models routes, with an x-vibearound-cwd header for workspace selection. -- evidence: [README.md#L142-L147](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L142-L147), [README.md#L136-L136](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L136-L136), [README.md#L149-L153](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L149-L153)
  - [observation/documented] The npm CLI installs both `va` and `vibearound` commands, with subcommands such as `va serve`, `va tui`, and `va launch --profile ...`. -- evidence: [README.md#L367-L371](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L367-L371), [README.md#L361-L361](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L361-L361)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
More evidence: [full detail](vibearound.detail.md)

Metadata and full claim list: [full detail](vibearound.detail.md)
Human notes ([notes](vibearound.notes.md), never overwritten by build)

[Back to map index](../../index.md)
