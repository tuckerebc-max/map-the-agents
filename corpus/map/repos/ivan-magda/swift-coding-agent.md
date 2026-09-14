# ivan-magda/swift-coding-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 88ed290dff95 @ 025e7d256d46b7f0

## Summary (orientation draft, not independently verified)

Selected evidence records: The project's thesis is that coding agents benefit more from a small set of excellent tools and a tight loop than from large orchestration layers, deliberately rebuilding Claude Code's restrained design in Swift. The agent runs a fixed while-true loop: append the user query, call the Anthropic API, and if the stop reason is tool use, execute tools and append results as a user message; otherwise return the text content.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] It is a two-target Swift Package Manager project: a Core library holding the API client, shell executor, agent loop, and tools, plus a thin CLI entry point. -- evidence: [README.md#L101-L101](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L101-L101), [README.md#L97-L97](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L97-L97), [README.md#L99-L99](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L99-L99)
- design-choices (1 claim(s)):
  - [observation/documented] The project's thesis is that coding agents benefit more from a small set of excellent tools and a tight loop than from large orchestration layers, deliberately rebuilding Claude Code's restrained design in Swift. -- evidence: [README.md#L3-L3](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L3-L3), [README.md#L17-L17](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L17-L17), [README.md#L21-L21](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L21-L21)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the stage-0 guide walks contributors through a two-target SPM layout with a Swift Testing test target (CoreTests importing Core), .env-based ANTHROPIC_API_KEY configuration, and swift build/run/test verification commands. -- evidence: [docs/s00.md#L152-L154](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L152-L154), [docs/s00.md#L28-L36](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L28-L36), [docs/s00.md#L167-L167](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L167-L167), [docs/s00.md#L142-L142](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L142-L142), [docs/s00.md#L132-L135](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L132-L135), [docs/s00.md#L162-L164](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s00.md#L162-L164)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The agent communicates with POST https://api.anthropic.com/v1/messages over raw HTTP built on AsyncHTTPClient, and the CLI executable is named `agent`. -- evidence: [README.md#L101-L101](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L101-L101), [README.md#L103-L103](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L103-L103)
- memory-state (1 claim(s)):
  - [observation/documented] The messages array lives on the Agent instance so conversation history persists across REPL turns, and each API call sends the entire accumulated history, which grows without bound until later context compaction. -- evidence: [docs/s01.md#L197-L197](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L197-L197), [docs/s01.md#L199-L199](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L199-L199), [docs/s01.md#L58-L58](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L58-L58)
- orchestration (2 claim(s)):
  - [observation/documented] The agent runs a fixed while-true loop: append the user query, call the Anthropic API, and if the stop reason is tool use, execute tools and append results as a user message; otherwise return the text content. -- evidence: [README.md#L39-L41](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L39-L41), [README.md#L43-L48](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L43-L48), [README.md#L50-L52](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L50-L52), [README.md#L54-L64](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L54-L64)
  - [observation/documented] The loop body is invariant across stages; each stage only adds tool handler entries and injection points before the API call, with tools varying while the loop stays identical. -- evidence: [docs/s01.md#L156-L156](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/docs/s01.md#L156-L156), [README.md#L66-L66](https://github.com/ivan-magda/swift-coding-agent/blob/88ed290dff95789929a823603cc54cf7cc530da2/README.md#L66-L66)
- tools-permissions (3 claim(s)):
More evidence: [full detail](swift-coding-agent.detail.md)

Metadata and full claim list: [full detail](swift-coding-agent.detail.md)
Human notes ([notes](swift-coding-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
