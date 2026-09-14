# jonrad/lsp-mcp -- full detail

[Back to orientation](lsp-mcp.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jonrad/lsp-mcp/b48c04c52731e3e499352fc644992dcce6202db2/a955f65a50821306.json](../../../wiki/dossiers/jonrad/lsp-mcp/b48c04c52731e3e499352fc644992dcce6202db2/a955f65a50821306.json)

## specifications (1 claim(s))

- [observation/documented] The project is an MCP server that gives LLMs and AI agents access to language server protocol (LSP) capabilities, providing language-aware context from a codebase. -- evidence: [README.md#L2-L2](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L2-L2) (`clm_0e41b1e0b59e1c235eacedd874c1feb971eba48c298231e03695e339e4ea8867`)

## components (1 claim(s))

- [observation/documented] The features list says the server supports multiple LSPs (multiple programming languages) at the same time, referencing a sample config file. -- evidence: [README.md#L73-L74](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L73-L74) (`clm_7f14446f9dfb0466f11e096ee035cb15d8f4dd2a31895e1fca281eca806828df`)

## design-choices (2 claim(s))

- [observation/documented] Supported LSP methods are dynamically generated from an LSP JSON Schema stored at src/resources/generated.protocol.schema.json. -- evidence: [README.md#L73-L74](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L73-L74) (`clm_f02546f16784f4ae62a27c3f4d17992a176b3effa1d482f122c714a5bf65d232`)
- [observation/documented] Recorded design decisions include switching from Python to Node (vscode's LSP library over multilspy), using the low-level MCP SDK rather than FastMCP, and using zod for config validation. -- evidence: [README.md#L135-L142](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L135-L142) (`clm_daa160d7de488a829c0bcb1c4a90de9bedad4d4a6c95dace3050832077d0e9cf`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: development commands include 'yarn', 'yarn mcp-cli' (an interactive MCP tool for development help), and 'yarn dev --help' for CLI help. -- evidence: [README.md#L128-L132](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L128-L132) (`clm_eb4037c326f2b383594dfa4b82cd702d3ea7d902f8cad90b33d77ad03ec147d4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The server is configured as an MCP server via mcpServers JSON config using a command (docker or npx) plus an --lsp argument specifying the language server command to launch. -- evidence: [README.md#L98-L107](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L98-L107), [README.md#L109-L109](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L109-L109), [README.md#L81-L91](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L81-L91) (`clm_a0efb12e9e8f9537f4925c26a1dfe723e8b2f89636e88f1bf292b2bc756a4115`)
- [observation/documented] The language server can be changed by switching the --lsp argument and then restarting the client (e.g. Claude Desktop). -- evidence: [README.md#L109-L109](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L109-L109) (`clm_f9217b1e89207c4a99f7f0e03ac00ba940e7e01ab9282a4653626f7cecb208f8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The example npx setup launches typescript-language-server 4.3.3 with typescript 5.7.3 via npx, communicating over stdio. -- evidence: [README.md#L98-L107](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L98-L107) (`clm_ace771e8056e8d3e27bf7320f6aaebbc76ef10ae37df5f3b36743b0816009a5b`)
- [observation/documented] The project is MIT licensed, permitting use, copying, modification, and redistribution with the copyright notice retained, and is provided as-is without warranty. -- evidence: [LICENSE.txt#L1-L1](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L1-L1), [LICENSE.txt#L3-L6](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L3-L6), [LICENSE.txt#L10-L13](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L10-L13), [LICENSE.txt#L8-L8](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L8-L8) (`clm_aad3c3ff69d86bcbdd6d10258f6de28e269923f7d75e81376407ee61f767b5be`)

## limitations (2 claim(s))

- [observation/documented] The README states the project is in a POC (proof-of-concept) state. -- evidence: [README.md#L70-L70](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L70-L70) (`clm_7ac9c5e9d3cdf7fbb68376db80d5a0af1e279e715039e1c03f38e65d93eb842c`)
- [observation/documented] The README notes that running multiple LSPs at the same time is not yet supported, in the section following the npx example. -- evidence: [README.md#L111-L111](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L111-L111) (`clm_c49579329106011f1cfa76f26ba541b6714f5bd9574c89198bf3f55e666321ff`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

