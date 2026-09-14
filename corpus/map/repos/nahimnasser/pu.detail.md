# nahimnasser/pu -- full detail

[Back to orientation](pu.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nahimnasser/pu/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/07d31fc542e82339.json](../../../wiki/dossiers/nahimnasser/pu/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/07d31fc542e82339.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product is a single shell script, pu.sh, described as under 50KB with zero package dependencies, relying on curl, awk, common Unix tools, and an API key. -- evidence: [README.md#L14-L14](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L14-L14), [README.md#L5-L5](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L5-L5), [README.md#L166-L166](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L166-L166) (`clm_0e12b42128982ccd353390ab600e8e309a961944f182f74c570567a2fd8517c8`)

## design-choices (2 claim(s))

- [observation/documented] JSON handling uses targeted awk parsing rather than a general JSON parser or jq, a deliberate choice to keep the install dependency-free. -- evidence: [README.md#L211-L217](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L211-L217), [README.md#L168-L168](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L168-L168), [README.md#L79-L87](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L79-L87) (`clm_1f7a063cba3f8645c37209eec0ab806ab5ad9571b978a5d951bc326e3111df67`)
- [observation/documented] File writes and edits use mktemp temp files, preserve trailing newlines via sentinel capture, keep executable mode on edits, and edit requires a unique oldText match. -- evidence: [bugs.md#L168-L168](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L168-L168), [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [bugs.md#L265-L265](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L265-L265), [bugs.md#L180-L180](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L180-L180) (`clm_0e8569c145933e4a051bdbecfc26e541704088fb667eb05bdb166e28387b44bd`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The agent exposes seven tools: bash, read, write, edit, grep, find, and ls, described as a Pi-shaped tool surface. -- evidence: [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [README.md#L221-L221](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L221-L221) (`clm_7e58d101d574324e7e9c35aed41665f7c477d2d38a68ab75c0135466f164413c`)
- [observation/documented] It offers an interactive REPL with commands including /model, /effort, /login, /logout, /flush, /compact, /export, /skill:name, /quit, and !cmd for inline shell execution. -- evidence: [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [README.md#L133-L146](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L133-L146) (`clm_9e5e3e6575b1a0008d9254552127a72454431655ace264803f2f4fba9b73d181`)
- [observation/documented] The CLI accepts a one-shot task argument, an interactive multi-turn mode, and a --pipe mode for chaining agent outputs, e.g. piping a write task into a security review. -- evidence: [README.md#L26-L26](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L26-L26), [README.md#L29-L32](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L29-L32), [README.md#L35-L35](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L35-L35) (`clm_cab2eb7aac798984571282d87c74a2a95754be62d32c5968fe6253d1e1b40deb`)

## memory-state (1 claim(s))

- [observation/documented] Sessions persist to .pu-history.json for resumable memory and .pu-events.jsonl for event replay/export; long sessions auto-compact by summarizing older transcript entries while keeping a bounded recent tail. -- evidence: [README.md#L178-L178](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L178-L178), [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73) (`clm_e496a4a437195d971538982c16ff16b00f3cd7acd2a9b1ccbe05874f394529eb`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The bash tool executes model-provided commands unsandboxed via a temp script; AGENT_CONFIRM=1 can be set to ask before each tool call. -- evidence: [README.md#L107-L129](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L107-L129), [bugs.md#L368-L368](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L368-L368) (`clm_5b332f4c08569f771d957d3dbc900d04c5c9628cd47bf9bbbccb67c255028760`)

## evaluation (1 claim(s))

- [inference/documented] The README references 30+ experiments in final_report.md on harness portability and an eval/COMPARISON.md feature-by-feature comparison against Pi, suggesting evaluation effort beyond unit tests, though no scored agent benchmarks appear in the provided slices. -- evidence: [README.md#L44-L44](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L44-L44), [README.md#L223-L223](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L223-L223) (`clm_50ec630a018d822b3d13910c3143d12b3f61bcf341a99f98653a0a7f48b8ffd8`)

## dependencies (1 claim(s))

- [observation/documented] It targets two providers: Anthropic via /v1/messages and OpenAI via /v1/responses, with API keys supplied via environment variables or a first-run login wizard saving ~/.pu.env. -- evidence: [README.md#L38-L40](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L38-L40), [README.md#L52-L73](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L52-L73), [README.md#L168-L168](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L168-L168) (`clm_92504300d97300e83c6850719c6f8c691918ecfae991857cb16ba0c2c8fe7f67`)

## limitations (3 claim(s))

- [observation/documented] Documented gaps include no TUI, no streaming display, no image input, no OAuth login, no native Windows support, and no general JSON parser. -- evidence: [README.md#L79-L87](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/README.md#L79-L87) (`clm_69e27dce557db67449db79e4d67f34fbf5394ab99d65255b38ad6cc10c9b233f`)
- [observation/documented] API keys are passed as curl header arguments, so on systems where process arguments are visible they can be exposed to other users during requests. -- evidence: [bugs.md#L306-L306](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L306-L306), [bugs.md#L308-L311](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L308-L311), [bugs.md#L313-L313](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L313-L313) (`clm_cde53d810c2aee4e4130e9f9859d932b517c2b6fce9859b2e8ab05da4765df5a`)
- [observation/documented] Context budgeting is approximate bytes/chars rather than tokens, and compaction boundaries are heuristic, so transcripts can still be malformed or exceed budget after compaction. -- evidence: [bugs.md#L337-L337](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L337-L337), [bugs.md#L331-L331](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L331-L331), [bugs.md#L325-L325](https://github.com/NahimNasser/pu/blob/9be54622ba1b458af1d34ba58bc43e4ea88ae1e9/bugs.md#L325-L325) (`clm_55fa73644f0427cc7e9f3d1013ffed740becadadaa2e6414557abb4cc9b8194c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

