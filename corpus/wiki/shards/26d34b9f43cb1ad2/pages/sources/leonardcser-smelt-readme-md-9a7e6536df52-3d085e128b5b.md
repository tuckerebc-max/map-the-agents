---
access: public
aliases: []
claim_ids:
- clm_23ec5129778e3078951204d7d3ef4a105c6b4b2b3ac1d99b19a7efb7cfbb3ab8
- clm_42bb5d43ada0617fcf111a5d7a4d308506224d9f1127c50fee6486bed7f3e584
- clm_47accdd61b9129ca1481c8ce92e68259b2a051f44884572e63ef59a8a73aff5c
- clm_66a78b864f25d3c1cd27c47bb99e942d70e47a7e2ea125985d5ece1345a6a2bb
- clm_824f2a058b3741e4db0a62d37a1bc26776b57e3232fc339d8940fb799e9072fc
- clm_acbce7f7e4efc9de0b1797f4bc411228bd9c7f65c7e84b181ad59099e8bc1cd6
- clm_b0efe2776c7fb3c82a3b7415cdacdaee59ee8940d2b92d7293699a2547de174c
- clm_bd6dcefa5ffa7807ab0f95ab46f17c85fd7badf0d7d7ddf9300bf463fed0ba6c
maturity: draft
page_id: pg_9ecd74fe8d2c5d5c82ce3d085e128b5b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5fba37715dec57a3970e0654d6cf6105
title: leonardcser/smelt/README.md @ 9a7e6536df52
updated_at: '2026-09-14T02:12:19Z'
---

# leonardcser/smelt/README.md @ 9a7e6536df52

<!-- rcw:begin owner=source:src_5fba37715dec57a3970e0654d6cf6105 block=evidence -->
- The product includes Lua plugins (keymaps, commands, autocmds, custom tools, custom modes), a self-built terminal grid/layout renderer, a vim-style editor with motions, text objects, registers and undo, and deterministic fuzzing with a fixed clock and stubbed I/O so crashes can be replayed. [@claim:clm_23ec5129778e3078951204d7d3ef4a105c6b4b2b3ac1d99b19a7efb7cfbb3ab8]
- API-key providers are configured with `--model`, `--api-base`, and `--api-key-env`, supporting any OpenAI-compatible endpoint such as a local Ollama server or OpenAI/Anthropic/OpenRouter. [@claim:clm_42bb5d43ada0617fcf111a5d7a4d308506224d9f1127c50fee6486bed7f3e584]
- smelt is described as beta software until 1.0, released with normal 0.x.y versions rather than SemVer prereleases, and interfaces may still change between releases. [@claim:clm_47accdd61b9129ca1481c8ce92e68259b2a051f44884572e63ef59a8a73aff5c]
- The project is MIT-licensed and states it is inspired by Claude Code and Neovim, with documentation hosted at leonardcser.github.io/smelt. [@claim:clm_66a78b864f25d3c1cd27c47bb99e942d70e47a7e2ea125985d5ece1345a6a2bb]
- smelt is installable from source with cargo install --locked from its GitHub repository, and prebuilt binaries are offered for Linux and macOS (x86_64, aarch64) plus Windows x86_64. [@claim:clm_824f2a058b3741e4db0a62d37a1bc26776b57e3232fc339d8940fb799e9072fc]
- smelt can run with no config, using flags alone, or via `smelt auth` for ChatGPT, GitHub Copilot, and Kimi Code; running bare `smelt` auto-detects the provider from credentials. [@claim:clm_acbce7f7e4efc9de0b1797f4bc411228bd9c7f65c7e84b181ad59099e8bc1cd6]
- The project positions itself as a small, fast coding agent scriptable in Lua like Neovim, built from scratch rather than on an existing framework. [@claim:clm_b0efe2776c7fb3c82a3b7415cdacdaee59ee8940d2b92d7293699a2547de174c]
- The default mode cycle is Normal → Plan → Apply → Yolo, with Plan mode bundled and autoloaded; optional bundled plugins include which_key, a local request inspector, and LSP-backed semantic code tools enabled from init.lua. [@claim:clm_bd6dcefa5ffa7807ab0f95ab46f17c85fd7badf0d7d7ddf9300bf463fed0ba6c]
<!-- rcw:end owner=source:src_5fba37715dec57a3970e0654d6cf6105 block=evidence -->

## Researcher notes

