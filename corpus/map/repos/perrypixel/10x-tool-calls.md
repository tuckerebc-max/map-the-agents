# perrypixel/10x-tool-calls

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 55d146363084 @ 2864faeddf1e18b7

## Summary (orientation draft, not independently verified)

Selected evidence records: 10x-Tool-Calls is a rules setup intended for Cursor IDE, Windsurf, or other agent-based coding assistants that support tool calls, and it only works in Agent Mode. After the AI completes a task, it runs a small Python script that prompts the user; the typed instruction drives continued work in a loop until the user stops manually or the tool call limit is reached.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] 10x-Tool-Calls is a rules setup intended for Cursor IDE, Windsurf, or other agent-based coding assistants that support tool calls, and it only works in Agent Mode. -- evidence: [readme.md#L5-L6](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L5-L6), [readme.md#L3-L3](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] After the AI completes a task, it runs a small Python script that prompts the user; the typed instruction drives continued work in a loop until the user stops manually or the tool call limit is reached. -- evidence: [readme.md#L10-L10](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L10-L10), [readme.md#L18-L22](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L18-L22)
  - [observation/documented] The setup targets tools with tool-call-based quotas (e.g. 500 monthly requests with up to 25 tool calls each), letting multiple follow-ups run within one request; it is not intended to minimize token usage on token-based pricing. -- evidence: [readme.md#L28-L28](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L28-L28), [readme.md#L67-L67](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L67-L67), [readme.md#L30-L34](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L30-L34)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [inference/documented] The setup likely requires a Python runtime, since the loop mechanism runs a Python script (userinput.py) between tasks. -- evidence: [readme.md#L10-L10](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L10-L10), [readme.md#L42-L42](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L42-L42)
- limitations (1 claim(s)):
  - [observation/documented] The current version supports plain text input only; image uploads and file drops are not yet supported but are planned for a more advanced version. -- evidence: [readme.md#L60-L61](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L60-L61), [readme.md#L58-L58](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L58-L58), [readme.md#L55-L56](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L55-L56)
- relevance (1 claim(s)):
  - [observation/documented] The project targets users of AI coding assistants with bundled tool-call quotas who want to get more work done per request without restarting the chat. -- evidence: [readme.md#L3-L3](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L3-L3), [readme.md#L30-L34](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L30-L34)

Every claim for this repository is shown above and in [full detail](10x-tool-calls.detail.md).

Metadata and full claim list: [full detail](10x-tool-calls.detail.md)
Human notes ([notes](10x-tool-calls.notes.md), never overwritten by build)

[Back to map index](../../index.md)
