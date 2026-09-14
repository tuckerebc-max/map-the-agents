---
access: public
aliases: []
claim_ids:
- clm_0cd8b1768ab0a987e875f6177d8da2afd804a072e43b1f82e6093d28436edc8f
- clm_0f797c30b3207becbc9f9202930e7bc619e50887fd7cbbc8cfa83b842400fca6
- clm_2d2b6e94cc669471028786e6a9b9b87fc3d8d71a71ca04da798f7c6c91c5b8ab
- clm_389960a00fbcaa45c19256f1b51d05756440f3486066e346606d8126250e1f9f
- clm_3c8597706cef7550f3c17ccbaa10c7073897474bce29a2b7a92682866ca07846
- clm_4499c0933821ec968476d473cd6d5ebda00766c945fa6c9cc114b684d43154a3
- clm_50e947a35618105cc778aa6581da8f51a1f1bc3eaebf619752095cc0900c7da8
- clm_8287ecb9283d7f6d7134077d0b58886f4f1cf8c0b43f97d1c094961eea04cde0
- clm_9419446b1e1cb3da63eb324ec1590b4461a49df55b9ca683484e448e7a517996
- clm_b13caeab24680b6bd9783e13f95477478ca9bf580c463df8324ce76855d3a427
- clm_e958592e5a6c015519ce6be7d000cdb473c108f96fb77c6360dc429d8cff38bc
maturity: draft
page_id: pg_8207567773795bac816ca8c6f089f937
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5d69bcead1a057f8aa26fe96ee63d791
title: codingmoh/open-codex/README.md @ 87aaaed1cea9
updated_at: '2026-09-14T01:42:52Z'
---

# codingmoh/open-codex/README.md @ 87aaaed1cea9

<!-- rcw:begin owner=source:src_5d69bcead1a057f8aa26fe96ee63d791 block=evidence -->
- Repository development practice: the README invites pull requests, welcoming ideas, issues, and improvements from contributors. [@claim:clm_0cd8b1768ab0a987e875f6177d8da2afd804a072e43b1f82e6093d28436edc8f]
- The tool provides colored terminal output for readability and can copy suggested commands to the clipboard. [@claim:clm_0f797c30b3207becbc9f9202930e7bc619e50887fd7cbbc8cfa83b842400fca6]
- Using the Ollama feature requires Ollama to be installed and running locally (e.g. on localhost:11434); local models like phi-4-mini are also supported. [@claim:clm_2d2b6e94cc669471028786e6a9b9b87fc3d8d71a71ca04da798f7c6c91c5b8ab]
- Ollama-backed models are selected via flags such as --ollama --model llama3, as shown in documented example invocations. [@claim:clm_389960a00fbcaa45c19256f1b51d05756440f3486066e346606d8126250e1f9f]
- The tool is designed to run fully locally with no OpenAI API key, sending no data to the cloud; models run locally. [@claim:clm_3c8597706cef7550f3c17ccbaa10c7073897474bce29a2b7a92682866ca07846]
- The workflow sends the prompt to the Ollama API, returns a shell command suggestion, then prompts the user to execute, copy, or abort. [@claim:clm_4499c0933821ec968476d473cd6d5ebda00766c945fa6c9cc114b684d43154a3]
- The project is MIT-licensed (copyright 2025 codingmo) and positions itself as a fully open-source CLI AI assistant inspired by OpenAI Codex. [@claim:clm_50e947a35618105cc778aa6581da8f51a1f1bc3eaebf619752095cc0900c7da8]
- The product is a CLI named open-codex that accepts a natural-language prompt and returns a suggested shell command, e.g. open-codex "list all folders". [@claim:clm_8287ecb9283d7f6d7134077d0b58886f4f1cf8c0b43f97d1c094961eea04cde0]
- The README lists interactive context-aware mode, full chat mode, function calling, voice input, command history/undo, and a plugin system as future plans, implying they are not yet available. [@claim:clm_9419446b1e1cb3da63eb324ec1590b4461a49df55b9ca683484e448e7a517996]
- Per the README, suggested commands are executed only after the user's explicit confirmation, with options to copy to clipboard or abort instead. [@claim:clm_b13caeab24680b6bd9783e13f95477478ca9bf580c463df8324ce76855d3a427]
- Installation options include Homebrew (recommended for macOS), pipx for cross-platform install, or cloning and running pip install. [@claim:clm_e958592e5a6c015519ce6be7d000cdb473c108f96fb77c6360dc429d8cff38bc]
<!-- rcw:end owner=source:src_5d69bcead1a057f8aa26fe96ee63d791 block=evidence -->

## Researcher notes

