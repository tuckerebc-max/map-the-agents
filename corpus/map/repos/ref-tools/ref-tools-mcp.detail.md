# ref-tools/ref-tools-mcp -- full detail

[Back to orientation](ref-tools-mcp.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ref-tools/ref-tools-mcp/83970a35627785a0589ae2dbe5510b4a3dd04146/42028e6fd913d6f0.json](../../../wiki/dossiers/ref-tools/ref-tools-mcp/83970a35627785a0589ae2dbe5510b4a3dd04146/42028e6fd913d6f0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (4 claim(s))

- [observation/documented] Ref uses MCP sessions to track search trajectory and minimize context usage. -- evidence: [README.md#L37-L37](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L37-L37) (`clm_0c1acfce035cac258a4252b9795239285620ac5e4a1367ab0e9a9fe8cc4645eb`)
- [observation/documented] Within a session, repeated similar searches never return duplicate results, letting the agent both page deeper and adjust its prompt. -- evidence: [README.md#L40-L40](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L40-L40) (`clm_5f3b5c11ac21fd3f6fb9fd5eb94b91361a6111842ccea9df18f910b5b6711447`)
- [observation/documented] When reading a documentation page, Ref uses the session's search history to drop less relevant sections and return the most relevant 5k tokens instead of pulling in 20k+ tokens. -- evidence: [README.md#L43-L43](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L43-L43) (`clm_10625900b6bcd50ce341aace770a2ffee83746f000eff44217c40b045277c762`)
- [observation/documented] The tools are designed to match how models search while minimizing context, aiming to reduce context rot and find exactly the context a coding agent needs. -- evidence: [README.md#L15-L15](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L15-L15) (`clm_d4600d40b4ec87764d5a4e3d2bbc4a44181c480908cffe2605fadba37a617de5`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: local development uses npm install/build/watch/dev, and the MCP Inspector (npm run inspect) is suggested for debugging server interactions. -- evidence: [README.md#L133-L136](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L133-L136), [README.md#L128-L131](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L128-L131), [README.md#L117-L120](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L117-L120), [README.md#L140-L152](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L140-L152) (`clm_8d0ebe51fa2e298efbe5d7827e8c40102e0618c67ad9d86e13bec686a68c300a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] Ref is a Model Context Protocol server that gives AI coding tools or agents access to documentation for APIs, services, and libraries in a token-efficient way. -- evidence: [README.md#L9-L9](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L9-L9) (`clm_00b64d4fc89cbbac4d61f0c72a9c8d63a830d5186df13ed4079c9dd0f673e806`)
- [observation/documented] The server exposes a ref_search_documentation tool with a required query parameter, described as a full sentence or question, for searching public web/GitHub docs and private resources like repos and PDFs. -- evidence: [README.md#L95-L96](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L95-L96), [README.md#L93-L93](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L93-L93), [README.md#L110-L113](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L110-L113) (`clm_abb9184e4f4e1323a35e46449a81b612ceb78060e0b602414552e5712ead0c36`)
- [observation/documented] A ref_read_url tool fetches a URL, converts the content to markdown, takes a required url parameter, and is designed to pair with search results. -- evidence: [README.md#L102-L103](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L102-L103), [README.md#L100-L100](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L100-L100) (`clm_973419ecabeb941eff6d37a2020ab402bec76b60777e073359002896a9082282`)
- [observation/documented] For OpenAI deep-research clients, the same tools are provided under different names: ref_search_documentation(query) becomes search(query) and ref_read_url(url) becomes fetch(id). -- evidence: [README.md#L108-L108](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L108-L108), [README.md#L110-L113](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L110-L113) (`clm_222183e44d19853f990d7750bf7056b4fd3433af45a89f83f67ab478896adfe9`)
- [observation/documented] Two setup modes exist: a recommended streamable-HTTP server and a legacy local stdio server, which is what this repository contains. -- evidence: [README.md#L58-L58](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L58-L58), [README.md#L60-L60](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L60-L60) (`clm_5bd86a176b0ca6d102fefff6471bb8064b4f4c545edde3058e3b2673df1f123e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The README describes coding agents performing one or more searches and then reading a few resources in depth, refining queries iteratively for complex prompts. -- evidence: [README.md#L17-L17](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L17-L17), [README.md#L25-L35](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L25-L35) (`clm_8374dc02f69b3172629dc4caa07855541a082f9fd28b09a67d82c0f2116f1d40`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stdio server runs via npx ref-tools-mcp@latest with a REF_API_KEY environment variable; the hosted HTTP endpoint at api.ref.tools/mcp also uses an API key. -- evidence: [README.md#L77-L85](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L77-L85), [README.md#L66-L71](https://github.com/ref-tools/ref-tools-mcp/blob/83970a35627785a0589ae2dbe5510b4a3dd04146/README.md#L66-L71) (`clm_e0965db7b31f26265365f50a28c564600061b44d6920c277ed06128da701d620`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

