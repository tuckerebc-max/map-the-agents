# appgram/agentnotch

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4139d6fd7b90 @ e12631ac6603de96

## Summary (orientation draft, not independently verified)

Selected evidence records: AgentNotch is a macOS menu bar app that lives in the Mac's notch and shows real-time telemetry from Claude Code and OpenAI Codex sessions. The app displays each tool call as it happens, including file reads, code edits, and shell commands.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Requires macOS 14.0 (Sonoma) or later; on non-notch Macs the app falls back to the menu bar. -- evidence: [README.md#L114-L115](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L114-L115)
- components (3 claim(s)):
  - [observation/documented] AgentNotch is a macOS menu bar app that lives in the Mac's notch and shows real-time telemetry from Claude Code and OpenAI Codex sessions. -- evidence: [README.md#L23-L23](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L23-L23)
  - [observation/documented] The app displays each tool call as it happens, including file reads, code edits, and shell commands. -- evidence: [README.md#L28-L28](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L28-L28)
- design-choices (3 claim(s)):
  - [observation/documented] Source-aware color coding distinguishes assistants: orange for Claude Code, blue for Codex, and light blue for unknown sources. -- evidence: [README.md#L34-L36](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L34-L36), [README.md#L38-L38](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L38-L38)
  - [observation/documented] Display is configurable: token counts, cost estimates, source filtering (Claude/Codex), and the menu bar icon can be toggled. -- evidence: [README.md#L49-L52](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L49-L52)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the contributor guide documents a release process of building in Xcode, zipping the app, computing SHA256, updating the cask formula, and pushing to the homebrew-tap repo. -- evidence: [CLAUDE.md#L166-L172](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/CLAUDE.md#L166-L172), [CLAUDE.md#L163-L163](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/CLAUDE.md#L163-L163)
  - [observation/documented] Repository development practice: debug logging is wrapped in a debugLog() helper that only prints in DEBUG builds. -- evidence: [CLAUDE.md#L100-L108](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/CLAUDE.md#L100-L108)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] AgentNotch listens for OTLP/HTTP on port 4318 by default and decodes OTLP logs (/v1/logs) and metrics (/v1/metrics). -- evidence: [README.md#L82-L82](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L82-L82)
  - [observation/documented] Interaction model: the notch indicator expands on hover to show recent tool calls, and clicking opens a full view with token breakdown and settings. -- evidence: [README.md#L101-L104](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L101-L104), [README.md#L44-L46](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L44-L46)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](agentnotch.detail.md) for every claim.)

Metadata and full claim list: [full detail](agentnotch.detail.md)
Human notes ([notes](agentnotch.notes.md), never overwritten by build)

[Back to map index](../../index.md)
