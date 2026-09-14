---
access: public
aliases: []
claim_ids:
- clm_0a7b6de554c258f32c18c631c3c20e806aee9f5ef28226d6a280de51b5ba2d60
- clm_18c50b72d9123ea51d53be3fb79454c694eb7450885887748382c855e40195a4
- clm_2cc10d005820d402676175a8ba9fcb9644c521314f5c3f30c96efbefcefda56b
- clm_3ec46cb45c1bcd26af6b4dc981554e100dc97fbe14ef87b1d2ee1713dd0a7879
- clm_532165133fb109047382f4333d8581b2b904206d7f352374f0530bf4dc611ec0
- clm_8cd44cb541843f568717e5cff92150ffbeded0639e94da8c6af4c99ff7e97b3b
- clm_93df243fd0776a85038cecb6efd0e0e9235b2d2a96fe34e8403fceec5d96ea59
- clm_9fb38b8298be70b9dca5051fb4211d968b51a37d9903d76a678c4d839cf7cf14
- clm_b45b67a03f6146c5c26ee10da5261417333507217ddfc0780cac5837812b2ae4
- clm_fa7636a79bf5f4f2d2facca4b7a82f9ab91b04e133a340938a3c476bac1b788c
maturity: draft
page_id: pg_5bdda38cf66f53389009fc9b507b2674
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_633bf2f81c4a5d0789c9720fa188ae1b
title: CogitatorTech/binharic-cli/README.md @ 52ccca70bdad
updated_at: '2026-09-14T01:42:54Z'
---

# CogitatorTech/binharic-cli/README.md @ 52ccca70bdad

<!-- rcw:begin owner=source:src_633bf2f81c4a5d0789c9720fa188ae1b block=evidence -->
- Configuration is done via the ~/.config/binharic/config.json5 file, and environment variables are also supported for configuration. [@claim:clm_0a7b6de554c258f32c18c631c3c20e806aee9f5ef28226d6a280de51b5ba2d60]
- Documented features include models from OpenAI, Google, Anthropic, and Ollama; a keyword-based RAG pipeline; built-in tools for file reading and Bash commands; and MCP-based external tools. [@claim:clm_18c50b72d9123ea51d53be3fb79454c694eb7450885887748382c855e40195a4]
- The project is MIT-licensed, published on npm, and positions itself as a general-purpose coding agent able to analyze projects, run tests, find bugs, and perform code review. [@claim:clm_2cc10d005820d402676175a8ba9fcb9644c521314f5c3f30c96efbefcefda56b]
- The architecture reportedly follows recommendations from Anthropic's 'building effective agents' article to a good degree. [@claim:clm_3ec46cb45c1bcd26af6b4dc981554e100dc97fbe14ef87b1d2ee1713dd0a7879]
- The README states Binharic is in early development, so bugs and breaking changes are expected. [@claim:clm_532165133fb109047382f4333d8581b2b904206d7f352374f0530bf4dc611ec0]
- The project is written in TypeScript and uses the AI SDK framework for much of its agentic logic such as tool calling and workflow management. [@claim:clm_8cd44cb541843f568717e5cff92150ffbeded0639e94da8c6af4c99ff7e97b3b]
- Binharic is a terminal-based AI coding assistant with the persona of a Tech-Priest of the Adeptus Mechanicus, comparable to Codex, Gemini CLI, and Claude Code. [@claim:clm_93df243fd0776a85038cecb6efd0e0e9235b2d2a96fe34e8403fceec5d96ea59]
- Users install the npm package @cogitator/binharic-cli globally and launch the agent with the 'binharic' command in a terminal. [@claim:clm_9fb38b8298be70b9dca5051fb4211d968b51a37d9903d76a678c4d839cf7cf14]
- A Docker image is published to GitHub Container Registry with multi-arch builds (linux/amd64 and linux/arm64), and the agent can be run in a container mounting the working directory at /workspace. [@claim:clm_b45b67a03f6146c5c26ee10da5261417333507217ddfc0780cac5837812b2ae4]
- API keys for OpenAI, Anthropic, and Google are supplied through environment variables when running the agent. [@claim:clm_fa7636a79bf5f4f2d2facca4b7a82f9ab91b04e133a340938a3c476bac1b788c]
<!-- rcw:end owner=source:src_633bf2f81c4a5d0789c9720fa188ae1b block=evidence -->

## Researcher notes

