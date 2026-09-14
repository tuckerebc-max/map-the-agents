# seandavi/agentic-coding-intro -- full detail

[Back to orientation](agentic-coding-intro.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/seandavi/agentic-coding-intro/f3a290d2df4330184dee9b413b20663e56c26181/88727176f78e91bf.json](../../../wiki/dossiers/seandavi/agentic-coding-intro/f3a290d2df4330184dee9b413b20663e56c26181/88727176f78e91bf.json)

## specifications (5 claim(s))

- [observation/documented] The document's stated tool is Google Antigravity, described as Google's agentic development platform where an agent can plan, edit files, run commands, and drive a browser; the official download link is provided. -- evidence: [README.md#L5-L5](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L5-L5) (`clm_b12d3939de92810272ac8350ac8eae7ea253e04c5566756493dcad43c197b74d`)
- [observation/documented] The handout teaches a conceptual distinction between the LLM (reasoning engine) and the agentic framework layer, which supplies the plan/act/observe/revise loop, tool routing, session memory, and permission guardrails. -- evidence: [README.md#L217-L217](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L217-L217), [README.md#L251-L255](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L251-L255), [README.md#L215-L215](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L215-L215) (`clm_0436209ef852dd338c900e39c51d48a306cf3a966dc2918c489f69eef0125c6e`)
- [observation/documented] The handout explains tokens and the context window, including the ~4-characters-per-token rule of thumb, higher tokenization cost for code, and that output tokens typically cost 4x-8x more than input tokens. -- evidence: [README.md#L192-L192](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L192-L192), [README.md#L183-L183](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L183-L183), [README.md#L185-L185](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L185-L185) (`clm_ed0e187f0f434b0fcbc5e29f295ff9e2bf9df6f9b6b4eeada36d4a42539ee90c`)
- [observation/documented] The document cites research findings ('Lost in the Middle', Liu et al. 2023, and 2025 'context rot' work) showing model attention degrades on long inputs, so large advertised context windows do not guarantee reliable attention. -- evidence: [README.md#L208-L209](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L208-L209) (`clm_a241be97bb6392c5c92af01a4325785a07afe6971d37be755619c05464f9a5cf`)
- [observation/documented] A worked hello-world exercise walks through creating a small Python file, then prompts to explain, edit with a CLI argument, add a pytest test, and extend to an R package structure with DESCRIPTION, NAMESPACE, and tests/. -- evidence: [README.md#L452-L454](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L452-L454), [README.md#L474-L476](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L474-L476), [README.md#L456-L458](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L456-L458), [README.md#L466-L468](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L466-L468), [README.md#L430-L430](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L430-L430) (`clm_458290ce0cec9216c8529a93ea557244643ee0ea10748d51bf418aba8b1832b4`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The title deliberately strikes through 'Gemini CLI' to illustrate that specific tools change within months, so the handout emphasizes slowly-changing concepts like agents, context, tokens, and file-based habits. -- evidence: [README.md#L7-L7](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L7-L7) (`clm_4da748aae36a90b763a4ba489d4c77c9e8dacfc8aa4f443de44255eea849fd69`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The handout recommends keeping broadly applicable facts in one stable instruction file while moving task-specific procedures into skills or separate documents that load on demand, to conserve context budget. -- evidence: [README.md#L394-L394](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L394-L394), [README.md#L384-L385](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L384-L385), [README.md#L391-L392](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L391-L392) (`clm_ca3a616c6fd860ddc4d82c8d2bcaa9dd0a61063ee489c742f945655ee36fb377`)

## interfaces (1 claim(s))

- [observation/documented] The handout describes MCP (Model Context Protocol) as an open standard for connecting AI applications to external tools and data, letting agents reach beyond the local filesystem to services like GitHub or databases. -- evidence: [README.md#L312-L312](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L312-L312), [README.md#L321-L321](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L321-L321), [README.md#L317-L317](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L317-L317) (`clm_a9d862bd996c17a0cc96d717d242af9d59c40dded5027b9eea95079926d1d6c8`)

## memory-state (1 claim(s))

- [observation/documented] The document advocates Markdown files as project memory and decision records, noting Antigravity's Artifacts and Knowledge Base and its reported automatic pickup of AGENTS.md, GEMINI.md, and CLAUDE.md instruction files. -- evidence: [README.md#L331-L331](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L331-L331), [README.md#L335-L335](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L335-L335) (`clm_7c3c8e33ea673ee045120f56fd2f7f5d3fa44547b5052051ad11eb443dd5adc2`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Antigravity is a downloadable desktop application for macOS, Windows, and Linux requiring sign-in with a Google account; it is model-flexible, with Gemini 3 Pro, Claude Sonnet 4.5, and open models mentioned as options. -- evidence: [README.md#L418-L418](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L418-L418), [README.md#L413-L416](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L413-L416), [README.md#L406-L406](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L406-L406) (`clm_6f46da09f01f8f4fbb504f94ec6ba6954cada1f6c12de35fe1a79fc90d8e500d`)

## limitations (1 claim(s))

- [observation/documented] The handout warns that Antigravity's free tier is rate-limited with unpublished, changing limits and a reported weekly ceiling (roughly 20 requests per day on the fast model, described as unofficial), so sustained work can exhaust it quickly. -- evidence: [README.md#L422-L422](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L422-L422) (`clm_2b22143d3cf95c1ad03c3f603d1a011fbbaa82ed5abd65f03e7dff85519072ea`)

## relevance (1 claim(s))

- [observation/documented] The handout targets developers already comfortable writing code in R and/or Python who are new to AI coding tools, aiming to teach the agentic interface rather than replace programming skill. -- evidence: [README.md#L3-L3](https://github.com/seandavi/agentic-coding-intro/blob/f3a290d2df4330184dee9b413b20663e56c26181/README.md#L3-L3) (`clm_3c5eb670348609270c58dd03f215b215170a981fa86e4873bcd2f8f709c47e32`)

