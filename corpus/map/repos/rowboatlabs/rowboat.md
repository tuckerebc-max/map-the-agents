# rowboatlabs/rowboat

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c9ef9e29cea9 @ f60857d13a04fdf9

## Summary (orientation draft, not independently verified)

Rowboat is a desktop AI coworker that indexes work into a local, plain-Markdown knowledge graph and provides work surfaces (email, browser, notes, code mode, meeting notes, apps). Evidence covers product features, MCP tool integration, optional API-key-based services, Google OAuth setup, and a draft proposal on Spaces naming; development-practice guidance appears only in test/QA instructions. Evidence coverage: 150 of 192 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Rowboat ships built-in work surfaces including an email client, notes, browser, code mode, meeting note taker, and per-project workspaces. -- evidence: [README.md#L37-L37](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L37-L37)
  - [observation/documented] Background agents can run on events (e.g. new email) or schedules, connect to tools, search the web, use the browser, and write code via Claude Code or Codex. -- evidence: [README.md#L58-L83](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L58-L83)
- design-choices (2 claim(s)):
  - [observation/documented] Rowboat supports bring-your-own-model: local models via Ollama or LM Studio or hosted providers with the user's own API key, swappable anytime. -- evidence: [README.md#L183-L186](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L183-L186)
  - [inference/documented] A draft proposal (status: Draft for discussion) suggests decoupling Spaces server display names from addresses; since it is explicitly a draft, these changes appear not yet shipped. -- evidence: [proposal.md#L12-L12](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/proposal.md#L12-L12), [proposal.md#L3-L6](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/proposal.md#L3-L6)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the assistant-bottom-tabs doc instructs running renderer tests for assistant-dock, assistant-chat-dock, chat-sidebar, useSessionChat, and session-chat/store, plus manual desktop QA steps. -- evidence: [docs/assistant-bottom-tabs.md#L20-L20](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/docs/assistant-bottom-tabs.md#L20-L20), [docs/assistant-bottom-tabs.md#L18-L18](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/docs/assistant-bottom-tabs.md#L18-L18)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] External tools connect via Model Context Protocol; servers are configured under Settings → MCP Servers as an mcpServers JSON object, using an existing Streamable HTTP client. -- evidence: [README.md#L199-L199](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L199-L199), [README.md#L201-L209](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L201-L209), [README.md#L190-L191](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L190-L191), [README.md#L211-L211](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L211-L211)
- memory-state (2 claim(s)):
  - [observation/documented] The product indexes email, meetings, Slack and assistant conversations into a living, Obsidian-style backlinked knowledge graph used as long-lived, accumulating context. -- evidence: [README.md#L58-L83](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L58-L83), [README.md#L173-L177](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L173-L177)
  - [observation/documented] All data is stored locally as plain Markdown with no proprietary formats, so users can inspect, edit, back up, or delete everything. -- evidence: [README.md#L217-L219](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L217-L219)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] MCP tool invocation is subject to the user's MCP tool permissions, per the Parallel web-search example. -- evidence: [README.md#L213-L213](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L213-L213)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](rowboat.detail.md)

Metadata and full claim list: [full detail](rowboat.detail.md)
Human notes ([notes](rowboat.notes.md), never overwritten by build)

[Back to map index](../../index.md)
