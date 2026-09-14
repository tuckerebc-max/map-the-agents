# touwaeriol/claude-code-plus

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d1e1622cb773 @ ed5501d0dd0f5d30

## Summary (orientation draft, not independently verified)

The product is an IntelliJ IDEA plugin that integrates Claude AI into the IDE, offering code assistance via natural-language chat. A model selector lets users switch between Claude models (Opus 4.5, Sonnet 4.5, Haiku 4.5), including a /model slash command and default model in settings. Evidence coverage: 150 of 182 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 33 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is an IntelliJ IDEA plugin that integrates Claude AI into the IDE, offering code assistance via natural-language chat. -- evidence: [README.md#L7-L9](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L7-L9), [README.md#L24-L24](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L24-L24)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [inference/documented] The architecture appears to use RSocket over WebSocket for streaming chat and plain HTTP for non-streaming IDE actions, per the changelog's RSocket migration notes and AGENTS.md protocol descriptions. -- evidence: [AGENTS.md#L50-L53](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/AGENTS.md#L50-L53), [AGENTS.md#L182-L182](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/AGENTS.md#L182-L182), [CHANGELOG.md#L129-L136](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L129-L136)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to communicate in Simplified Chinese while writing git commits and changelog entries in English. -- evidence: [AGENTS.md#L1-L2](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/AGENTS.md#L1-L2)
  - [observation/documented] Repository development practice: the README welcomes contributions via pull requests, and the changelog records CI verification-matrix and caching build practices. -- evidence: [CHANGELOG.md#L14-L17](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L14-L17), [CHANGELOG.md#L345-L353](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L345-L353), [README.md#L134-L134](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L134-L134)
- skills-patterns (1 claim(s)):
  - [observation/documented] The plugin supports MCP (Model Context Protocol) servers to extend Claude's capabilities, with status monitoring, reconnect, and enable/disable controls. -- evidence: [CHANGELOG.md#L76-L79](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L76-L79), [README.md#L75-L75](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L75-L75)
- interfaces (1 claim(s)):
  - [observation/documented] A model selector lets users switch between Claude models (Opus 4.5, Sonnet 4.5, Haiku 4.5), including a /model slash command and default model in settings. -- evidence: [README.md#L50-L50](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L50-L50), [CHANGELOG.md#L82-L85](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L82-L85)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions support reconnection: the plugin resumes a session using a stored conversation ID and auto-reconnects when the frontend becomes visible again. -- evidence: [CHANGELOG.md#L105-L108](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L105-L108)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] File write operations go through a secure authorization dialog, and the plugin added a dynamic MCP tool allowlist for flexible tool permissions. -- evidence: [CHANGELOG.md#L473-L476](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/CHANGELOG.md#L473-L476), [README.md#L55-L55](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L55-L55)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The plugin requires a JetBrains IDE (builds 242-253) and Node.js v18 or higher with node on PATH, and bundles a Claude CLI so no separate CLI install is needed. -- evidence: [README.md#L94-L99](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L94-L99), [README.md#L101-L101](https://github.com/touwaeriol/claude-code-plus/blob/d1e1622cb7731afc0e7d9abfc278def225ac7535/README.md#L101-L101)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](claude-code-plus.detail.md)

Metadata and full claim list: [full detail](claude-code-plus.detail.md)
Human notes ([notes](claude-code-plus.notes.md), never overwritten by build)

[Back to map index](../../index.md)
