# pasky/claude.vim -- full detail

[Back to orientation](claude.vim.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pasky/claude.vim/06baac1ed4503e6c642193c56a27238ca67b5911/ab4d248724fbd4e3.json](../../../wiki/dossiers/pasky/claude.vim/06baac1ed4503e6c642193c56a27238ca67b5911/ab4d248724fbd4e3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The plugin is explicitly not code completion like Copilot; it provides a chat/instruction-centric interface optimized for human collaboration, with chat history access and vimdiff review as key features. -- evidence: [README.md#L12-L19](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L12-L19) (`clm_517af2b4125878100c8cbde83c2e48511aef95c9f18dcdb2ef122a5e167df5f0`)
- [observation/documented] Because Sonnet 3.5 is not deemed capable of fully autonomous complex tasks, the design keeps the human in control: users chat, review, and can reject changes and tool execution attempts. -- evidence: [README.md#L58-L60](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L58-L60) (`clm_1bed4b64f90aa730550980d6038a12ae1b89a4f7b6e93917efa00c2098c63947`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The plugin offers two main interaction modes: a simple implementation assistant (ClaudeImplement) and a chat interface (ClaudeChat). -- evidence: [README.md#L133-L134](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L133-L134), [README.md#L131-L131](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L131-L131) (`clm_4923a2a6b08b23d4247ede45e8b579681767f28167a0d3466c2ad141d0f1083b`)
- [observation/documented] ClaudeImplement works on a visual-mode selection: the selected block is all Claude sees, with no additional context, and proposed changes are reviewed in diff mode. -- evidence: [README.md#L141-L147](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L141-L147), [README.md#L138-L139](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L138-L139) (`clm_a132885a2e579777985788b683f9fae055de7ef82cef7db8797388673df713de`)
- [observation/documented] In chat mode Claude sees the full content of all buffers listed in :buffers, and proposed code changes pop up a diff mode for review when possible. -- evidence: [README.md#L151-L153](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L151-L153), [README.md#L155-L159](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L155-L159) (`clm_102203d8abce7135a0eda9395204ea40176213c405f41e2ddd949ec85a883032`)

## memory-state (1 claim(s))

- [observation/documented] Chat history is sent to Claude with each request; previous interactions are folded in the buffer and users can edit or delete the history to redact it. -- evidence: [README.md#L174-L177](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L174-L177) (`clm_7a7f496c7ca0f7e03673acdcd4dc8a08960f48a0ba2816147f5b25b490769ab7`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The plugin can open files and execute vim commands via a Claude Tools interface, and can evaluate Python expressions only with the user's case-by-case consent. -- evidence: [README.md#L39-L40](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L39-L40), [README.md#L35-L35](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L35-L35) (`clm_f8a16fedbc10325381988940ccf8620333b547224957949982543fab8ebe159c`)
- [observation/documented] The current version can also execute shell scripts, and the plugin can search the web when it lacks knowledge, with web access requiring elinks or felinks installed. -- evidence: [README.md#L52-L52](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L52-L52), [README.md#L90-L93](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L90-L93), [README.md#L48-L48](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L48-L48) (`clm_2d71c488f932588b7bc7560de473d884f49277e963c58828ca1d89853f9e43f8`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Web access depends on installing elinks or felinks; Google search additionally requires a one-time manual cookie-consent step in elinks. -- evidence: [README.md#L90-L93](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L90-L93) (`clm_b5abb95f3f3e6459767f2ef32c921303392f5208cc71734431185a594b389226`)
- [observation/documented] The plugin uses the Anthropic Claude API by default (API key set via g:claude_api_key), with AWS Bedrock available as an alternative provider via g:claude_use_bedrock. -- evidence: [README.md#L107-L109](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L107-L109), [README.md#L97-L99](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L97-L99), [README.md#L111-L111](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L111-L111) (`clm_b3d2a3a113433b0327b82fa572039d0c4b5894c27b9ac6db331414f61fdd689d`)

## limitations (2 claim(s))

- [observation/documented] The README warns this is early alpha software expected to evolve rapidly, possibly in backwards-incompatible ways. -- evidence: [README.md#L65-L68](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L65-L68) (`clm_a7e1944d19dafdbc9423b023d42332b8175d6210863e4cd985c584943fdb9b5c`)
- [observation/documented] Every Q&A roundtrip sends full chat history and all buffer content, which can consume tokens quickly and incur real API costs; users are advised to prune history and watch billing. -- evidence: [README.md#L101-L103](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L101-L103), [README.md#L179-L182](https://github.com/pasky/claude.vim/blob/06baac1ed4503e6c642193c56a27238ca67b5911/README.md#L179-L182) (`clm_c69732881bc932410b70b0e14693d641e63037117e45487d31382d250f02d5e9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

