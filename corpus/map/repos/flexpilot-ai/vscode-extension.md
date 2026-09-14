# flexpilot-ai/vscode-extension

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 360af0191b36 @ 0da3c6244cc4ceb7

## Summary (orientation draft, not independently verified)

Flexpilot is a VS Code extension described as an open-source, native alternative to GitHub Copilot, distributed via the VS Code Marketplace. The extension is no longer actively maintained; the project says it will still try to address issues and pull requests but will not add new features.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Flexpilot is a VS Code extension described as an open-source, native alternative to GitHub Copilot, distributed via the VS Code Marketplace. -- evidence: [README.md#L23-L25](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L23-L25), [README.md#L3-L3](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The README emphasizes a native VS Code experience without webviews and lets users supply their own API keys and choose their preferred AI providers and models. -- evidence: [README.md#L29-L33](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L29-L33), [README.md#L19-L19](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L19-L19)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to fork and clone the repo, run npm install, debug the extension in VS Code, then run npm run lint and npm run format before opening a pull request. -- evidence: [CONTRIBUTING.md#L61-L66](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/CONTRIBUTING.md#L61-L66)
  - [observation/documented] Repository development practice: contributing requires agreeing to a Contributor License Agreement that grants Flexpilot rights to use contributions commercially and to potentially change the license away from GPLv3. -- evidence: [CONTRIBUTING.md#L55-L57](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/CONTRIBUTING.md#L55-L57), [CONTRIBUTING.md#L37-L39](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/CONTRIBUTING.md#L37-L39), [CONTRIBUTING.md#L7-L7](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/CONTRIBUTING.md#L7-L7), [CONTRIBUTING.md#L78-L78](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/CONTRIBUTING.md#L78-L78)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README lists supported AI providers including Anthropic, OpenAI, Azure OpenAI, Groq, Google Gemini, Mistral AI, Ollama, and several self-hosted backends such as vLLM and llama-cpp-python. -- evidence: [README.md#L93-L108](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L93-L108)
- limitations (1 claim(s)):
  - [observation/documented] The extension is no longer actively maintained; the project says it will still try to address issues and pull requests but will not add new features. -- evidence: [README.md#L5-L12](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L5-L12)
- relevance (1 claim(s)):
  - [observation/documented] The project positions itself as relevant to developers wanting flexible, provider-agnostic AI assistance in VS Code, with a roadmap pointing to multi-file edits and workspace-agent features in the successor product. -- evidence: [README.md#L19-L19](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L19-L19), [README.md#L112-L115](https://github.com/flexpilot-ai/vscode-extension/blob/360af0191b369dceb714b5838ff745d201260f3f/README.md#L112-L115)

(1 additional claim(s) omitted for length; see [full detail](vscode-extension.detail.md) for every claim.)

Metadata and full claim list: [full detail](vscode-extension.detail.md)
Human notes ([notes](vscode-extension.notes.md), never overwritten by build)

[Back to map index](../../index.md)
