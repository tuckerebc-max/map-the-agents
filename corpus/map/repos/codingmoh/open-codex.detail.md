# codingmoh/open-codex -- full detail

[Back to orientation](open-codex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codingmoh/open-codex/87aaaed1cea96cb1cc2be6b44d91858122d982a9/c33d98a8cb95d40b.json](../../../wiki/dossiers/codingmoh/open-codex/87aaaed1cea96cb1cc2be6b44d91858122d982a9/c33d98a8cb95d40b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The workflow sends the prompt to the Ollama API, returns a shell command suggestion, then prompts the user to execute, copy, or abort. -- evidence: [README.md#L41-L43](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L41-L43) (`clm_4499c0933821ec968476d473cd6d5ebda00766c945fa6c9cc114b684d43154a3`)

## design-choices (1 claim(s))

- [observation/documented] The tool is designed to run fully locally with no OpenAI API key, sending no data to the cloud; models run locally. -- evidence: [README.md#L111-L111](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L111-L111), [README.md#L11-L11](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L11-L11), [README.md#L13-L13](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L13-L13), [README.md#L26-L31](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L26-L31) (`clm_3c8597706cef7550f3c17ccbaa10c7073897474bce29a2b7a92682866ca07846`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README invites pull requests, welcoming ideas, issues, and improvements from contributors. -- evidence: [README.md#L117-L117](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L117-L117) (`clm_0cd8b1768ab0a987e875f6177d8da2afd804a072e43b1f82e6093d28436edc8f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product is a CLI named open-codex that accepts a natural-language prompt and returns a suggested shell command, e.g. open-codex "list all folders". -- evidence: [README.md#L3-L5](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L3-L5), [README.md#L19-L21](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L19-L21) (`clm_8287ecb9283d7f6d7134077d0b58886f4f1cf8c0b43f97d1c094961eea04cde0`)
- [observation/documented] Ollama-backed models are selected via flags such as --ollama --model llama3, as shown in documented example invocations. -- evidence: [README.md#L103-L105](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L103-L105), [README.md#L35-L37](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L35-L37), [README.md#L26-L31](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L26-L31) (`clm_389960a00fbcaa45c19256f1b51d05756440f3486066e346606d8126250e1f9f`)
- [observation/documented] The tool provides colored terminal output for readability and can copy suggested commands to the clipboard. -- evidence: [README.md#L26-L31](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L26-L31) (`clm_0f797c30b3207becbc9f9202930e7bc619e50887fd7cbbc8cfa83b842400fca6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Per the README, suggested commands are executed only after the user's explicit confirmation, with options to copy to clipboard or abort instead. -- evidence: [README.md#L111-L111](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L111-L111), [README.md#L41-L43](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L41-L43), [README.md#L94-L99](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L94-L99), [README.md#L26-L31](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L26-L31) (`clm_b13caeab24680b6bd9783e13f95477478ca9bf580c463df8324ce76855d3a427`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Using the Ollama feature requires Ollama to be installed and running locally (e.g. on localhost:11434); local models like phi-4-mini are also supported. -- evidence: [README.md#L11-L11](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L11-L11), [README.md#L45-L45](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L45-L45), [README.md#L41-L43](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L41-L43) (`clm_2d2b6e94cc669471028786e6a9b9b87fc3d8d71a71ca04da798f7c6c91c5b8ab`)
- [observation/documented] Installation options include Homebrew (recommended for macOS), pipx for cross-platform install, or cloning and running pip install. -- evidence: [README.md#L74-L76](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L74-L76), [README.md#L80-L84](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L80-L84), [README.md#L66-L69](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L66-L69) (`clm_e958592e5a6c015519ce6be7d000cdb473c108f96fb77c6360dc429d8cff38bc`)

## limitations (1 claim(s))

- [observation/documented] The README lists interactive context-aware mode, full chat mode, function calling, voice input, command history/undo, and a plugin system as future plans, implying they are not yet available. -- evidence: [README.md#L51-L57](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L51-L57) (`clm_9419446b1e1cb3da63eb324ec1590b4461a49df55b9ca683484e448e7a517996`)

## relevance (1 claim(s))

- [observation/documented] The project is MIT-licensed (copyright 2025 codingmo) and positions itself as a fully open-source CLI AI assistant inspired by OpenAI Codex. -- evidence: [README.md#L11-L11](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L11-L11), [LICENSE.md#L1-L1](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/LICENSE.md#L1-L1), [README.md#L123-L123](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L123-L123), [LICENSE.md#L3-L3](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/LICENSE.md#L3-L3) (`clm_50e947a35618105cc778aa6581da8f51a1f1bc3eaebf619752095cc0900c7da8`)

