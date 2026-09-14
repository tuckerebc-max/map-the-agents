---
access: public
aliases: []
claim_ids:
- clm_0df47d975cdc23dc08387538cf4bb018ab4562951821beca44eadcfd2fd0eba9
- clm_1c7a412d04c6cdc6984942f9a3252677087daf41a45c099cdb49b295a9337fd8
- clm_32903c6fdc7fb3cb06e556856eb61b0ac824ee7b287516b6f0b139169959f8a0
- clm_5f9ce1327f24b7f9591307ecbe9bc2c11354400c959f36a98a49c74e1db70cfe
- clm_794d79b4b52db184fa61c88bf9d639501fb4218950c3db78e5682a94f78c1926
- clm_8a920caed05636898c6195b2cd4c34d6a221c07314b7da9740885be904f8350c
- clm_9997d548a71a51c0ccdd288b03cb4867702b5325eb0de48effdc3d16b335b35a
- clm_b5fad5ae2600cade3b829bb71365a8d5530839beeb2315d312647ed8c9baf659
- clm_dbb3b4a94ff7321d3e0373b92966d5495d7ff303e99f7bc3d503d5c446e30109
- clm_dfbd746dd540f31f691fad9599af24ef14c939ce8c98f83fc97835c678e84005
- clm_f2c947a9f19b1d784c2b0d0e6cd2b452be5122ca16e1475def0aba4e9f4ff19c
maturity: draft
page_id: pg_0a6e9ecd6b275b17a35761b7abd9ac82
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d06575ddd1905a34bb0fef364a09fb9f
title: sumitsingh4411/repo-agent/README.md @ 703c1afdf6f3
updated_at: '2026-09-14T03:15:53Z'
---

# sumitsingh4411/repo-agent/README.md @ 703c1afdf6f3

<!-- rcw:begin owner=source:src_d06575ddd1905a34bb0fef364a09fb9f block=evidence -->
- The extension uses a bring-your-own-key DeepSeek API by default (deepseek-flash default model), and speaks an OpenAI-compatible API so baseUrl can point at OpenAI, OpenRouter, Gemini, or other providers. [@claim:clm_0df47d975cdc23dc08387538cf4bb018ab4562951821beca44eadcfd2fd0eba9]
- A 'Learn this codebase' command writes a knowledge brief to .repo-agent/knowledge.md injected into every prompt, and a memory.md (or .agent.md/.claude.md) at the repo root supplies always-on user rules. [@claim:clm_1c7a412d04c6cdc6984942f9a3252677087daf41a45c099cdb49b295a9337fd8]
- A code-review feature reviews staged changes, files, or branches, runs a second audit pass (review.deepAudit default true), reports Critical/Quality/Architecture/Testing findings, and can enforce user rules from a system-design.md guidelines file. [@claim:clm_32903c6fdc7fb3cb06e556856eb61b0ac824ee7b287516b6f0b139169959f8a0]
- After editing, the agent reportedly runs the project's typecheck/build, reads errors, and fixes them before declaring a task done (self-verification). [@claim:clm_5f9ce1327f24b7f9591307ecbe9bc2c11354400c959f36a98a49c74e1db70cfe]
- The product ships as a VS Code extension ('free-repo-agent' on the Marketplace) with a chat panel opened via Cmd/Ctrl+Shift+A or a docked icon, plus 'Agent:' commands in the command palette. [@claim:clm_794d79b4b52db184fa61c88bf9d639501fb4218950c3db78e5682a94f78c1926]
- Plugins are MCP servers addable from a built-in catalog of ~20 servers, from npm/GitHub packages (run via npx), custom stdio commands, or remote URLs over Streamable HTTP with optional bearer tokens. [@claim:clm_8a920caed05636898c6195b2cd4c34d6a221c07314b7da9740885be904f8350c]
- A terminal CLI ships inside the extension (v0.10.0+), runnable via an alias to dist/cli.js, with flags like --model, --effort, --cwd, --base-url, --yes, and in-session commands such as /model, /effort, /login. [@claim:clm_9997d548a71a51c0ccdd288b03cb4867702b5325eb0de48effdc3d16b335b35a]
- The agent indexes the repository (symbols, structure, optional AI per-file summaries) into a local .agent-cache/ cache and injects the most relevant files (default 8 via repoAgent.retrieval.maxFiles) into each prompt. [@claim:clm_b5fad5ae2600cade3b829bb71365a8d5530839beeb2315d312647ed8c9baf659]
- Plugin tools run without a confirmation prompt by default (repoAgent.plugins.autoRun = true); turning it off yields a Run/Reject prompt per external tool call. File edits are blocked from absolute paths and '..' traversal per the README. [@claim:clm_dbb3b4a94ff7321d3e0373b92966d5495d7ff303e99f7bc3d503d5c446e30109]
- An autonomous agent mode reads files, edits across many files with inline Keep/Undo review, and runs terminal commands with user approval, tracked by a live checklist that can be stopped. [@claim:clm_dfbd746dd540f31f691fad9599af24ef14c939ce8c98f83fc97835c678e84005]
- API keys and plugin tokens are stored in VS Code SecretStorage rather than settings or repo files; the CLI keeps its own key store (~/.repo-agent.json, chmod 600, opt-in) since it cannot read VS Code SecretStorage. [@claim:clm_f2c947a9f19b1d784c2b0d0e6cd2b452be5122ca16e1475def0aba4e9f4ff19c]
<!-- rcw:end owner=source:src_d06575ddd1905a34bb0fef364a09fb9f block=evidence -->

## Researcher notes

