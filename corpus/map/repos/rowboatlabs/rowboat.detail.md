# rowboatlabs/rowboat -- full detail

[Back to orientation](rowboat.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rowboatlabs/rowboat/c9ef9e29cea90076f3518f3b263a30659deef13b/f60857d13a04fdf9.json](../../../wiki/dossiers/rowboatlabs/rowboat/c9ef9e29cea90076f3518f3b263a30659deef13b/f60857d13a04fdf9.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Rowboat ships built-in work surfaces including an email client, notes, browser, code mode, meeting note taker, and per-project workspaces. -- evidence: [README.md#L37-L37](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L37-L37) (`clm_bfa152802082c801684cc249c671de796535c4e232ab462bda4bac783bcd45c1`)
- [observation/documented] Background agents can run on events (e.g. new email) or schedules, connect to tools, search the web, use the browser, and write code via Claude Code or Codex. -- evidence: [README.md#L58-L83](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L58-L83) (`clm_7bf18f86d3109cd019521b6bee9ccc4f6a2f7c646aab94679212c50e23b61a03`)
- [observation/documented] A local meeting note-taker captures mic and speaker audio, produces a live transcript, summarizes to a markdown file, and updates the knowledge graph. -- evidence: [README.md#L85-L131](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L85-L131) (`clm_5a65903fed2e11449a1d9a891ae2099b714b058dc6b9f8c773cb7938c58e21c6`)

## design-choices (2 claim(s))

- [observation/documented] Rowboat supports bring-your-own-model: local models via Ollama or LM Studio or hosted providers with the user's own API key, swappable anytime. -- evidence: [README.md#L183-L186](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L183-L186) (`clm_b05bae2cdc053b2594511cfcde4bd63321f391bd82cb0146c326b2350941397e`)
- [inference/documented] A draft proposal (status: Draft for discussion) suggests decoupling Spaces server display names from addresses; since it is explicitly a draft, these changes appear not yet shipped. -- evidence: [proposal.md#L12-L12](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/proposal.md#L12-L12), [proposal.md#L3-L6](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/proposal.md#L3-L6) (`clm_48ae4397743dc5ae9da06bf6c514c2faaf725bfd3b286e360df3ea97cb84123b`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the assistant-bottom-tabs doc instructs running renderer tests for assistant-dock, assistant-chat-dock, chat-sidebar, useSessionChat, and session-chat/store, plus manual desktop QA steps. -- evidence: [docs/assistant-bottom-tabs.md#L20-L20](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/docs/assistant-bottom-tabs.md#L20-L20), [docs/assistant-bottom-tabs.md#L18-L18](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/docs/assistant-bottom-tabs.md#L18-L18) (`clm_b85885221741ffcd82840b50938fc04eda6d743f7072ccba40a3375e32d62824`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] External tools connect via Model Context Protocol; servers are configured under Settings → MCP Servers as an mcpServers JSON object, using an existing Streamable HTTP client. -- evidence: [README.md#L199-L199](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L199-L199), [README.md#L201-L209](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L201-L209), [README.md#L190-L191](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L190-L191), [README.md#L211-L211](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L211-L211) (`clm_485e67bbb31a030edaa0ec59643d1356960419562b52e2023b92e9db0859dfdb`)

## memory-state (2 claim(s))

- [observation/documented] The product indexes email, meetings, Slack and assistant conversations into a living, Obsidian-style backlinked knowledge graph used as long-lived, accumulating context. -- evidence: [README.md#L58-L83](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L58-L83), [README.md#L173-L177](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L173-L177) (`clm_400d016aeab93ea766cd79365bb9b1df2f13650a07eb6b9f53a4c81240f174b6`)
- [observation/documented] All data is stored locally as plain Markdown with no proprietary formats, so users can inspect, edit, back up, or delete everything. -- evidence: [README.md#L217-L219](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L217-L219) (`clm_17845ea1e0a1cbc74a76502d12642592ac0cddb0c1a68f579f9514b0ae03d936`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] MCP tool invocation is subject to the user's MCP tool permissions, per the Parallel web-search example. -- evidence: [README.md#L213-L213](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L213-L213) (`clm_d5039186183a71e0f1ad25ad538694bbd60e8e83262b99077a9c58b4630a4271`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Optional features use API keys in ~/.rowboat/config JSON files: Deepgram (voice input), ElevenLabs (voice output), Exa (search), and Composio (external tools/MCP servers), all sharing an apiKey format. -- evidence: [README.md#L147-L147](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L147-L147), [README.md#L159-L159](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L159-L159), [README.md#L151-L151](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L151-L151), [README.md#L155-L155](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L155-L155), [README.md#L161-L166](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/README.md#L161-L166) (`clm_3edb3165d93930470844bc7caf2b84c78e274f2fa6c8817a57a1e76afb8fced5`)
- [observation/documented] Google integration (Gmail, Calendar, Drive) requires the user to supply their own Google OAuth client ID and secret, with a localhost:8080/oauth/callback redirect URI. -- evidence: [google-setup.md#L140-L140](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/google-setup.md#L140-L140), [google-setup.md#L127-L127](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/google-setup.md#L127-L127), [google-setup.md#L125-L125](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/google-setup.md#L125-L125), [google-setup.md#L3-L3](https://github.com/rowboatlabs/rowboat/blob/c9ef9e29cea90076f3518f3b263a30659deef13b/google-setup.md#L3-L3) (`clm_43a4a503a9068112b3248d6320dc2e745be303f67659381506e84b2f980557f3`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

