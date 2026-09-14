---
access: public
aliases: []
claim_ids:
- clm_1452fa9735708195c43a44bc44fe8a0fe11c6051aded5261b21f65ba8d47163c
- clm_2cc582112bf37de6e49f82990ba6b3037b71aa56e91dab63988949f039ec7736
- clm_3258a2086b6292153bc148f74b67c37d71a2888dd2c50b2fdfea6bc88714b21f
- clm_36e3fb628626eb1f605020bd4d97ef34115b013520bc6bbdbdac705269553d3e
- clm_5e7f30b9b2ed81dd7587fed1aad297df587c1782344ab1d6baff21eaf80c2f80
- clm_6e691c77568270a4b4fe0e52594e69333f2c834c511ebb552ead9284362d89af
- clm_764d416c745379f0a1888ede3abcf4ccfc173c9140d551001ec409104646ecec
- clm_89eb8a456c13f9e497dcb8ed8364a31b217b91e37f0e10fff0a382d7be13d8cc
- clm_b939717ed8ebab2d7756343ccae25547f8143c9920764e03d4b238bce8d49fa5
- clm_c5f48f9b5728efeffe61568054bf7fd697f8efb2af7c5db5b95aa37e8f1c44d4
- clm_d50c7e68a25fb2e2cc8b9b143fc20640537c27999caaee9141287c9270f5e2aa
- clm_da860a3e29d6a6e11a2424d7284ef3b24a5a71e841e32daaddfe931d7a7ffb2f
maturity: draft
page_id: pg_551b1784106f5553866a72afece03841
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_876858093c1a5d6fbbad71e924b3c865
title: github/copilot-cli/README.md @ b49df25cafe8
updated_at: '2026-09-14T01:52:02Z'
---

# github/copilot-cli/README.md @ b49df25cafe8

<!-- rcw:begin owner=source:src_876858093c1a5d6fbbad71e924b3c865 block=evidence -->
- Authentication uses GitHub account login or a fine-grained PAT with the 'Copilot Requests' permission, supplied via `GH_TOKEN` or `GITHUB_TOKEN` (in that precedence order). [@claim:clm_1452fa9735708195c43a44bc44fe8a0fe11c6051aded5261b21f65ba8d47163c]
- The agent ships with GitHub's MCP server by default and supports adding custom MCP servers to extend its capabilities. [@claim:clm_2cc582112bf37de6e49f82990ba6b3037b71aa56e91dab63988949f039ec7736]
- Each submitted prompt reduces the user's monthly premium-requests quota by one, requiring an active Copilot subscription. [@claim:clm_3258a2086b6292153bc148f74b67c37d71a2888dd2c50b2fdfea6bc88714b21f]
- An experimental mode, enabled via the `--experimental` flag or `/experimental` command and persisted in config, unlocks in-development features like Autopilot mode cycled with Shift+Tab. [@claim:clm_36e3fb628626eb1f605020bd4d97ef34115b013520bc6bbdbdac705269553d3e]
- LSP support provides go-to-definition, hover information, and diagnostics; servers are configured in `~/.copilot/lsp-config.json` (user level) or `.github/lsp.json` (repository level). [@claim:clm_5e7f30b9b2ed81dd7587fed1aad297df587c1782344ab1d6baff21eaf80c2f80]
- Slash commands include `/login` for authentication, `/model` for model selection, `/experimental`, `/lsp` for LSP status, and `/feedback` for a confidential survey. [@claim:clm_6e691c77568270a4b4fe0e52594e69333f2c834c511ebb552ead9284362d89af]
- By default the CLI uses Claude Sonnet 4.5, with other models such as Claude Sonnet 4 and GPT-5 selectable via `/model`. [@claim:clm_764d416c745379f0a1888ede3abcf4ccfc173c9140d551001ec409104646ecec]
- It uses the same agentic harness as GitHub's Copilot coding agent, working locally and synchronously in the terminal. [@claim:clm_89eb8a456c13f9e497dcb8ed8364a31b217b91e37f0e10fff0a382d7be13d8cc]
- The CLI previews every action before execution and requires explicit user approval, so nothing runs without consent. [@claim:clm_b939717ed8ebab2d7756343ccae25547f8143c9920764e03d4b238bce8d49fa5]
- The CLI does not bundle LSP servers; users must install language servers such as typescript-language-server separately. [@claim:clm_c5f48f9b5728efeffe61568054bf7fd697f8efb2af7c5db5b95aa37e8f1c44d4]
- Organization or enterprise administrators can disable Copilot CLI access for their members via policy settings. [@claim:clm_d50c7e68a25fb2e2cc8b9b143fc20640537c27999caaee9141287c9270f5e2aa]
- Copilot CLI is a terminal application launched with the `copilot` command, offering natural-language conversations to build, debug, and understand code. [@claim:clm_da860a3e29d6a6e11a2424d7284ef3b24a5a71e841e32daaddfe931d7a7ffb2f]
<!-- rcw:end owner=source:src_876858093c1a5d6fbbad71e924b3c865 block=evidence -->

## Researcher notes

