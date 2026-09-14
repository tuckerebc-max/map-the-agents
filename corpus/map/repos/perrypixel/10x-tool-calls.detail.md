# perrypixel/10x-tool-calls -- full detail

[Back to orientation](10x-tool-calls.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/perrypixel/10x-tool-calls/55d14636308467aa43c206c3826906f4eee54684/2864faeddf1e18b7.json](../../../wiki/dossiers/perrypixel/10x-tool-calls/55d14636308467aa43c206c3826906f4eee54684/2864faeddf1e18b7.json)

## specifications (1 claim(s))

- [observation/documented] 10x-Tool-Calls is a rules setup intended for Cursor IDE, Windsurf, or other agent-based coding assistants that support tool calls, and it only works in Agent Mode. -- evidence: [readme.md#L5-L6](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L5-L6), [readme.md#L3-L3](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L3-L3) (`clm_5fb7ef59d0c84154c4345b850177d2cddd8fd6b02f29eaee4f86799e4efb6043`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] After the AI completes a task, it runs a small Python script that prompts the user; the typed instruction drives continued work in a loop until the user stops manually or the tool call limit is reached. -- evidence: [readme.md#L10-L10](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L10-L10), [readme.md#L18-L22](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L18-L22) (`clm_a2f172ca607cc19a525859c5730ec340f9b799ffa6329ba0b95c02f7b520e4aa`)
- [observation/documented] The setup targets tools with tool-call-based quotas (e.g. 500 monthly requests with up to 25 tool calls each), letting multiple follow-ups run within one request; it is not intended to minimize token usage on token-based pricing. -- evidence: [readme.md#L28-L28](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L28-L28), [readme.md#L67-L67](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L67-L67), [readme.md#L30-L34](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L30-L34) (`clm_45a1f2068e712fd94d3370f3f988829f4114b751bbaad4ec966779cb92d5d54f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [inference/documented] The setup likely requires a Python runtime, since the loop mechanism runs a Python script (userinput.py) between tasks. -- evidence: [readme.md#L10-L10](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L10-L10), [readme.md#L42-L42](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L42-L42) (`clm_67c4ec886563b9b0e9064c43fadf0f604cf9670e4af6f7b7a6a426b69bd4bb21`)

## limitations (1 claim(s))

- [observation/documented] The current version supports plain text input only; image uploads and file drops are not yet supported but are planned for a more advanced version. -- evidence: [readme.md#L60-L61](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L60-L61), [readme.md#L58-L58](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L58-L58), [readme.md#L55-L56](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L55-L56) (`clm_d200bfbd438b4ea2be1589555adaf1be46fec4ae46c8705a628514b0c05f6d3b`)

## relevance (1 claim(s))

- [observation/documented] The project targets users of AI coding assistants with bundled tool-call quotas who want to get more work done per request without restarting the chat. -- evidence: [readme.md#L3-L3](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L3-L3), [readme.md#L30-L34](https://github.com/perrypixel/10x-Tool-Calls/blob/55d14636308467aa43c206c3826906f4eee54684/readme.md#L30-L34) (`clm_acfc23017d275400c85c1bc2c10e4de7120461772d84159eae1bbd86339c4737`)

