---
access: public
aliases: []
claim_ids:
- clm_136f5959512b0b1b3b47a040f9fbe09485f16c53af82f2c84b50a6143134ed98
- clm_1c24b8dc5bbd7045ef5daad7ecc91586c5ec125bdf6122babc2b6ee3f3b5972f
- clm_26ea4b8e4c96bb4befa91c80c196032521164a30da2b4dd579d2876f78b190e5
- clm_4af639c9eed63220200c112e982f2dff31a53644741a2dacf1d3b05c163d2073
- clm_69caefed51c7f3d1bc147cad55f4725f707d3757499f11421f6b0eb0a11a6cc7
- clm_75840d18cec57e0bd8531d0ebfbeb2ee28f2bb455e782e2e9560c1c5c3fa7bc9
- clm_b9100d79b6269b6ade9da5aea61367409065c0e7222473ccf49aeea67bb83e86
- clm_bd293867aa018a52465bad51d9e4d0fa75c9d2172e804131e37a116b6a1f152e
- clm_c2cf56ce38fb284e25d0a636aa8ce7f29d12f2593321324ade2fa5bb3c73de58
- clm_e855b8712a0a9872c789a642884dd3cedfb61cea464cc4fe31f6be8cb1d6fe01
- clm_f505377e1017a89616602a33dedbc65d55d62dd622f44cb9a3ed8cb202ca73eb
- clm_fee646cc0f110e72d051eb5fba9962812a6a6e507441b331524ca8babe6736c8
maturity: draft
page_id: pg_520cde0a09a156b69b0de8dbd87d24d5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e4d20589b1de5a5588bb47040ebdbc97
title: meysamhadeli/codai/README.md @ 4949b5ccfab7
updated_at: '2026-09-14T02:17:53Z'
---

# meysamhadeli/codai/README.md @ 4949b5ccfab7

<!-- rcw:begin owner=source:src_e4d20589b1de5a5588bb47040ebdbc97 block=evidence -->
- The README states codai summarizes full project context using Tree-sitter. [@claim:clm_136f5959512b0b1b3b47a040f9fbe09485f16c53af82f2c84b50a6143134ed98]
- Codai can be installed globally via 'go install github.com/meysamhadeli/codai@latest'. [@claim:clm_1c24b8dc5bbd7045ef5daad7ecc91586c5ec125bdf6122babc2b6ee3f3b5972f]
- The project is written in Go, with a badge indicating a required Go version of at least 1.23. [@claim:clm_26ea4b8e4c96bb4befa91c80c196032521164a30da2b4dd579d2876f78b190e5]
- The README notes the project is a work in progress with new features to be added over time. [@claim:clm_4af639c9eed63220200c112e982f2dff31a53644741a2dacf1d3b05c163d2073]
- The README claims codai can modify several files at once and tracks and displays token consumption for each request. [@claim:clm_69caefed51c7f3d1bc147cad55f4725f707d3757499f11421f6b0eb0a11a6cc7]
- Users select an LLM provider with a '--provider' flag and a model with '--model'; OpenAI is stated as the default provider, with listed providers including Ollama, Azure OpenAI, Anthropic, Gemini, Mistral, Grok, Qwen, DeepSeek, and OpenRouter. [@claim:clm_75840d18cec57e0bd8531d0ebfbeb2ee28f2bb455e782e2e9560c1c5c3fa7bc9]
- Codai is described as an AI coding agent that runs in the terminal, invoked with the command 'codai code' from a working directory. [@claim:clm_b9100d79b6269b6ade9da5aea61367409065c0e7222473ccf49aeea67bb83e86]
- Advertised coding capabilities include adding features or tests, refactoring, describing and suggesting bug fixes, code review assistance, applying AI-generated changes, and generating documentation. [@claim:clm_bd293867aa018a52465bad51d9e4d0fa75c9d2172e804131e37a116b6a1f152e]
- The README claims context-aware code completions and per-session maintenance of conversational and code context. [@claim:clm_c2cf56ce38fb284e25d0a636aa8ce7f29d12f2593321324ade2fa5bb3c73de58]
- A .codai-gitignore file in the working directory root lets users specify files codai should ignore. [@claim:clm_e855b8712a0a9872c789a642884dd3cedfb61cea464cc4fe31f6be8cb1d6fe01]
- The config file supports provider, base_url, model, optional api_version, temperature, and reasoning_effort fields, plus a theme setting; themes come from the Chroma style gallery. [@claim:clm_f505377e1017a89616602a33dedbc65d55d62dd622f44cb9a3ed8cb202ca73eb]
- Configuration can come from a codai-config.yml in the working directory root, from environment variables, or via CLI flags such as --config, --provider, --temperature, and --api_key; defaults apply when no config file is present. [@claim:clm_fee646cc0f110e72d051eb5fba9962812a6a6e507441b331524ca8babe6736c8]
<!-- rcw:end owner=source:src_e4d20589b1de5a5588bb47040ebdbc97 block=evidence -->

## Researcher notes

