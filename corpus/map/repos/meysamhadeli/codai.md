# meysamhadeli/codai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4949b5ccfab7 @ afc03d192cf149bb

## Summary (orientation draft, not independently verified)

Selected evidence records: Codai is described as an AI coding agent that runs in the terminal, invoked with the command 'codai code' from a working directory. The project is written in Go, with a badge indicating a required Go version of at least 1.23.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The README states codai summarizes full project context using Tree-sitter. -- evidence: [README.md#L21-L21](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L21-L21)
- design-choices (2 claim(s)):
  - [observation/documented] A .codai-gitignore file in the working directory root lets users specify files codai should ignore. -- evidence: [README.md#L101-L101](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L101-L101), [README.md#L103-L105](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L103-L105)
  - [observation/documented] The README claims context-aware code completions and per-session maintenance of conversational and code context. -- evidence: [README.md#L17-L17](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L17-L17), [README.md#L19-L19](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L19-L19)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Advertised coding capabilities include adding features or tests, refactoring, describing and suggesting bug fixes, code review assistance, applying AI-generated changes, and generating documentation. -- evidence: [README.md#L25-L25](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L25-L25), [README.md#L29-L29](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L29-L29), [README.md#L31-L31](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L31-L31), [README.md#L27-L27](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L27-L27), [README.md#L23-L23](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L23-L23), [README.md#L33-L33](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L33-L33)
- interfaces (5 claim(s)):
  - [observation/documented] Codai is described as an AI coding agent that runs in the terminal, invoked with the command 'codai code' from a working directory. -- evidence: [README.md#L8-L8](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L8-L8), [README.md#L110-L113](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L110-L113), [README.md#L108-L108](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L108-L108)
  - [observation/documented] Users select an LLM provider with a '--provider' flag and a model with '--model'; OpenAI is stated as the default provider, with listed providers including Ollama, Azure OpenAI, Anthropic, Gemini, Mistral, Grok, Qwen, DeepSeek, and OpenRouter. -- evidence: [README.md#L58-L69](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L58-L69)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The project is written in Go, with a badge indicating a required Go version of at least 1.23. -- evidence: [README.md#L1-L4](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L1-L4)
  - [observation/documented] Codai can be installed globally via 'go install github.com/meysamhadeli/codai@latest'. -- evidence: [README.md#L46-L48](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L46-L48), [README.md#L44-L44](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L44-L44)
- limitations (1 claim(s)):
  - [observation/documented] The README notes the project is a work in progress with new features to be added over time. -- evidence: [README.md#L116-L116](https://github.com/meysamhadeli/codai/blob/4949b5ccfab7312d0527235ceb4b45ca39d437df/README.md#L116-L116)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](codai.detail.md) for every claim.)

Metadata and full claim list: [full detail](codai.detail.md)
Human notes ([notes](codai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
