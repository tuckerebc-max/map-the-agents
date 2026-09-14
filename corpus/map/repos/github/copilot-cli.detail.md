# github/copilot-cli -- full detail

[Back to orientation](copilot-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/github/copilot-cli/b49df25cafe802d2012876c8703332064237c7e3/bb11b5b4363508e2.json](../../../wiki/dossiers/github/copilot-cli/b49df25cafe802d2012876c8703332064237c7e3/bb11b5b4363508e2.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The agent ships with GitHub's MCP server by default and supports adding custom MCP servers to extend its capabilities. -- evidence: [README.md#L16-L20](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L16-L20) (`clm_2cc582112bf37de6e49f82990ba6b3037b71aa56e91dab63988949f039ec7736`)
- [observation/documented] It uses the same agentic harness as GitHub's Copilot coding agent, working locally and synchronously in the terminal. -- evidence: [README.md#L14-L14](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L14-L14), [README.md#L5-L5](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L5-L5) (`clm_89eb8a456c13f9e497dcb8ed8364a31b217b91e37f0e10fff0a382d7be13d8cc`)

## design-choices (2 claim(s))

- [observation/documented] The CLI previews every action before execution and requires explicit user approval, so nothing runs without consent. -- evidence: [README.md#L16-L20](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L16-L20) (`clm_b939717ed8ebab2d7756343ccae25547f8143c9920764e03d4b238bce8d49fa5`)
- [observation/documented] An experimental mode, enabled via the `--experimental` flag or `/experimental` command and persisted in config, unlocks in-development features like Autopilot mode cycled with Shift+Tab. -- evidence: [README.md#L126-L126](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L126-L126), [README.md#L135-L135](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L135-L135), [README.md#L128-L129](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L128-L129), [README.md#L131-L131](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L131-L131) (`clm_36e3fb628626eb1f605020bd4d97ef34115b013520bc6bbdbdac705269553d3e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Copilot CLI is a terminal application launched with the `copilot` command, offering natural-language conversations to build, debug, and understand code. -- evidence: [README.md#L101-L103](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L101-L103), [README.md#L120-L120](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L120-L120), [README.md#L3-L3](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L3-L3), [README.md#L5-L5](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L5-L5) (`clm_da860a3e29d6a6e11a2424d7284ef3b24a5a71e841e32daaddfe931d7a7ffb2f`)
- [observation/documented] Slash commands include `/login` for authentication, `/model` for model selection, `/experimental`, `/lsp` for LSP status, and `/feedback` for a confidential survey. -- evidence: [README.md#L194-L194](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L194-L194), [README.md#L107-L107](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L107-L107), [README.md#L128-L129](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L128-L129), [README.md#L184-L184](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L184-L184), [README.md#L122-L122](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L122-L122) (`clm_6e691c77568270a4b4fe0e52594e69333f2c834c511ebb552ead9284362d89af`)
- [observation/documented] LSP support provides go-to-definition, hover information, and diagnostics; servers are configured in `~/.copilot/lsp-config.json` (user level) or `.github/lsp.json` (repository level). -- evidence: [README.md#L159-L160](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L159-L160), [README.md#L143-L143](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L143-L143), [README.md#L157-L157](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L157-L157), [README.md#L162-L163](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L162-L163) (`clm_5e7f30b9b2ed81dd7587fed1aad297df587c1782344ab1d6baff21eaf80c2f80`)
- [observation/documented] Authentication uses GitHub account login or a fine-grained PAT with the 'Copilot Requests' permission, supplied via `GH_TOKEN` or `GITHUB_TOKEN` (in that precedence order). -- evidence: [README.md#L107-L107](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L107-L107), [README.md#L111-L111](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L111-L111), [README.md#L113-L116](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L113-L116) (`clm_1452fa9735708195c43a44bc44fe8a0fe11c6051aded5261b21f65ba8d47163c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] By default the CLI uses Claude Sonnet 4.5, with other models such as Claude Sonnet 4 and GPT-5 selectable via `/model`. -- evidence: [README.md#L122-L122](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L122-L122) (`clm_764d416c745379f0a1888ede3abcf4ccfc173c9140d551001ec409104646ecec`)
- [observation/documented] Each submitted prompt reduces the user's monthly premium-requests quota by one, requiring an active Copilot subscription. -- evidence: [README.md#L137-L137](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L137-L137), [README.md#L34-L35](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L34-L35) (`clm_3258a2086b6292153bc148f74b67c37d71a2888dd2c50b2fdfea6bc88714b21f`)

## limitations (2 claim(s))

- [observation/documented] The CLI does not bundle LSP servers; users must install language servers such as typescript-language-server separately. -- evidence: [README.md#L147-L147](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L147-L147), [README.md#L149-L151](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L149-L151) (`clm_c5f48f9b5728efeffe61568054bf7fd697f8efb2af7c5db5b95aa37e8f1c44d4`)
- [observation/documented] Organization or enterprise administrators can disable Copilot CLI access for their members via policy settings. -- evidence: [README.md#L37-L37](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L37-L37) (`clm_d50c7e68a25fb2e2cc8b9b143fc20640537c27999caaee9141287c9270f5e2aa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

