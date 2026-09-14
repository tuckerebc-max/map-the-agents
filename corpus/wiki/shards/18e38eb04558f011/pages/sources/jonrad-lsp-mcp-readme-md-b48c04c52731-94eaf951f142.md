---
access: public
aliases: []
claim_ids:
- clm_0e41b1e0b59e1c235eacedd874c1feb971eba48c298231e03695e339e4ea8867
- clm_7ac9c5e9d3cdf7fbb68376db80d5a0af1e279e715039e1c03f38e65d93eb842c
- clm_7f14446f9dfb0466f11e096ee035cb15d8f4dd2a31895e1fca281eca806828df
- clm_a0efb12e9e8f9537f4925c26a1dfe723e8b2f89636e88f1bf292b2bc756a4115
- clm_ace771e8056e8d3e27bf7320f6aaebbc76ef10ae37df5f3b36743b0816009a5b
- clm_c49579329106011f1cfa76f26ba541b6714f5bd9574c89198bf3f55e666321ff
- clm_daa160d7de488a829c0bcb1c4a90de9bedad4d4a6c95dace3050832077d0e9cf
- clm_eb4037c326f2b383594dfa4b82cd702d3ea7d902f8cad90b33d77ad03ec147d4
- clm_f02546f16784f4ae62a27c3f4d17992a176b3effa1d482f122c714a5bf65d232
- clm_f9217b1e89207c4a99f7f0e03ac00ba940e7e01ab9282a4653626f7cecb208f8
maturity: draft
page_id: pg_a68d322aa6a650c6a78a94eaf951f142
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_30eaad3b363555d0a49f863b2662109e
title: jonrad/lsp-mcp/README.md @ b48c04c52731
updated_at: '2026-09-14T04:01:33Z'
---

# jonrad/lsp-mcp/README.md @ b48c04c52731

<!-- rcw:begin owner=source:src_30eaad3b363555d0a49f863b2662109e block=evidence -->
- The project is an MCP server that gives LLMs and AI agents access to language server protocol (LSP) capabilities, providing language-aware context from a codebase. [@claim:clm_0e41b1e0b59e1c235eacedd874c1feb971eba48c298231e03695e339e4ea8867]
- The README states the project is in a POC (proof-of-concept) state. [@claim:clm_7ac9c5e9d3cdf7fbb68376db80d5a0af1e279e715039e1c03f38e65d93eb842c]
- The features list says the server supports multiple LSPs (multiple programming languages) at the same time, referencing a sample config file. [@claim:clm_7f14446f9dfb0466f11e096ee035cb15d8f4dd2a31895e1fca281eca806828df]
- The server is configured as an MCP server via mcpServers JSON config using a command (docker or npx) plus an --lsp argument specifying the language server command to launch. [@claim:clm_a0efb12e9e8f9537f4925c26a1dfe723e8b2f89636e88f1bf292b2bc756a4115]
- The example npx setup launches typescript-language-server 4.3.3 with typescript 5.7.3 via npx, communicating over stdio. [@claim:clm_ace771e8056e8d3e27bf7320f6aaebbc76ef10ae37df5f3b36743b0816009a5b]
- The README notes that running multiple LSPs at the same time is not yet supported, in the section following the npx example. [@claim:clm_c49579329106011f1cfa76f26ba541b6714f5bd9574c89198bf3f55e666321ff]
- Recorded design decisions include switching from Python to Node (vscode's LSP library over multilspy), using the low-level MCP SDK rather than FastMCP, and using zod for config validation. [@claim:clm_daa160d7de488a829c0bcb1c4a90de9bedad4d4a6c95dace3050832077d0e9cf]
- Repository development practice: development commands include 'yarn', 'yarn mcp-cli' (an interactive MCP tool for development help), and 'yarn dev --help' for CLI help. [@claim:clm_eb4037c326f2b383594dfa4b82cd702d3ea7d902f8cad90b33d77ad03ec147d4]
- Supported LSP methods are dynamically generated from an LSP JSON Schema stored at src/resources/generated.protocol.schema.json. [@claim:clm_f02546f16784f4ae62a27c3f4d17992a176b3effa1d482f122c714a5bf65d232]
- The language server can be changed by switching the --lsp argument and then restarting the client (e.g. Claude Desktop). [@claim:clm_f9217b1e89207c4a99f7f0e03ac00ba940e7e01ab9282a4653626f7cecb208f8]
<!-- rcw:end owner=source:src_30eaad3b363555d0a49f863b2662109e block=evidence -->

## Researcher notes

