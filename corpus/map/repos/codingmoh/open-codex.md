# codingmoh/open-codex

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 87aaaed1cea9 @ c33d98a8cb95d40b

## Summary (orientation draft, not independently verified)

The snapshot contains only README and license files for Open Codex, a terminal-based CLI coding agent that translates natural-language prompts into shell commands using local or Ollama-hosted LLMs, with confirmation before executing commands.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The workflow sends the prompt to the Ollama API, returns a shell command suggestion, then prompts the user to execute, copy, or abort. -- evidence: [README.md#L41-L43](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L41-L43)
- design-choices (1 claim(s)):
  - [observation/documented] The tool is designed to run fully locally with no OpenAI API key, sending no data to the cloud; models run locally. -- evidence: [README.md#L111-L111](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L111-L111), [README.md#L11-L11](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L11-L11), [README.md#L13-L13](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L13-L13), [README.md#L26-L31](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L26-L31)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README invites pull requests, welcoming ideas, issues, and improvements from contributors. -- evidence: [README.md#L117-L117](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L117-L117)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product is a CLI named open-codex that accepts a natural-language prompt and returns a suggested shell command, e.g. open-codex "list all folders". -- evidence: [README.md#L3-L5](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L3-L5), [README.md#L19-L21](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L19-L21)
  - [observation/documented] Ollama-backed models are selected via flags such as --ollama --model llama3, as shown in documented example invocations. -- evidence: [README.md#L103-L105](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L103-L105), [README.md#L35-L37](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L35-L37), [README.md#L26-L31](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L26-L31)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Per the README, suggested commands are executed only after the user's explicit confirmation, with options to copy to clipboard or abort instead. -- evidence: [README.md#L111-L111](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L111-L111), [README.md#L41-L43](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L41-L43), [README.md#L94-L99](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L94-L99), [README.md#L26-L31](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L26-L31)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Using the Ollama feature requires Ollama to be installed and running locally (e.g. on localhost:11434); local models like phi-4-mini are also supported. -- evidence: [README.md#L11-L11](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L11-L11), [README.md#L45-L45](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L45-L45), [README.md#L41-L43](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L41-L43)
  - [observation/documented] Installation options include Homebrew (recommended for macOS), pipx for cross-platform install, or cloning and running pip install. -- evidence: [README.md#L74-L76](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L74-L76), [README.md#L80-L84](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L80-L84), [README.md#L66-L69](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L66-L69)
- limitations (1 claim(s)):
  - [observation/documented] The README lists interactive context-aware mode, full chat mode, function calling, voice input, command history/undo, and a plugin system as future plans, implying they are not yet available. -- evidence: [README.md#L51-L57](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L51-L57)
- relevance (1 claim(s)):
  - [observation/documented] The project is MIT-licensed (copyright 2025 codingmo) and positions itself as a fully open-source CLI AI assistant inspired by OpenAI Codex. -- evidence: [README.md#L11-L11](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L11-L11), [LICENSE.md#L1-L1](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/LICENSE.md#L1-L1), [README.md#L123-L123](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/README.md#L123-L123), [LICENSE.md#L3-L3](https://github.com/codingmoh/open-codex/blob/87aaaed1cea96cb1cc2be6b44d91858122d982a9/LICENSE.md#L3-L3)

(1 additional claim(s) omitted for length; see [full detail](open-codex.detail.md) for every claim.)

Metadata and full claim list: [full detail](open-codex.detail.md)
Human notes ([notes](open-codex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
