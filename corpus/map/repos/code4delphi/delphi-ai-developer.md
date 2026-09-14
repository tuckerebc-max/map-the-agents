# code4delphi/delphi-ai-developer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3d979ffc33a8 @ 2d3e54b5de481a65

## Summary (orientation draft, not independently verified)

Delphi AI Developer is a Delphi IDE plugin providing AI chat, code completion, and database chat via OpenAI, Gemini, Mistral, and Groq APIs plus offline support through Ollama; evidence is documentation-only (README and LGPD.md).

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] A Delphi IDE plugin, inspired by GitHub Copilot, that adds AI interaction to the Delphi IDE using the OpenAI, Gemini, Mistral and Groq APIs plus offline AI support. -- evidence: [README.md#L2-L2](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L2-L2)
  - [observation/documented] The plugin aims to assist with generating and refactoring code, and offers suggestions in the IDE plus user-defined predefined questions to speed up searches. -- evidence: [README.md#L4-L4](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L4-L4), [README.md#L6-L6](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L6-L6)
- components (2 claim(s)):
  - [observation/documented] A code completion feature can be toggled on/off, configured with a default AI, suggestion highlight color, and a shortcut (default Alt+Enter, requiring IDE restart); Tab accepts the suggestion. -- evidence: [README.md#L76-L78](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L76-L78), [README.md#L66-L66](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L66-L66), [README.md#L70-L74](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L70-L74)
  - [observation/documented] A database chat lets users register databases, generate a structure reference, ask questions, execute the returned SQL, and view, copy or export results in a grid. -- evidence: [README.md#L119-L136](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L119-L136), [README.md#L104-L105](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L104-L105), [README.md#L107-L109](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L107-L109)
- design-choices (2 claim(s)):
  - [observation/documented] Both chats can optionally include the current unit's source code as prompt context; if code is selected only the selection is used, otherwise the entire unit. -- evidence: [README.md#L119-L136](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L119-L136), [README.md#L87-L99](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L87-L99)
  - [observation/documented] Users can set default prompts sent with every request to improve response quality, and can toggle modes where the AI returns only code or only SQL without comments. -- evidence: [README.md#L119-L136](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L119-L136), [README.md#L44-L47](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L44-L47), [README.md#L70-L74](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L70-L74), [README.md#L87-L99](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L87-L99)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are welcomed via pull requests or by opening an issue in the repository. -- evidence: [README.md#L161-L161](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L161-L161)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Installation is done by opening Package\DelphiAIDeveloper.dpk in Delphi and installing the package; afterwards an "AI Developer" item appears in the IDE's main menu. -- evidence: [README.md#L24-L24](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L24-L24), [README.md#L29-L29](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L29-L29), [README.md#L34-L34](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L34-L34)
  - [observation/documented] An AI chat panel is opened via the "AI Developer" menu or Ctrl+Shift+Alt+A, with prompt and response fields, pre-registered questions, and actions to insert selected text at the cursor, create a new unit, or copy text. -- evidence: [README.md#L84-L85](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L84-L85), [README.md#L87-L99](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L87-L99)
- memory-state (1 claim(s)):
  - [observation/documented] Database structure metadata (database name, table names, field names, types, sizes) is stored locally in a JSON file on the user's computer, not exposed to any server. -- evidence: [LGPD.md#L14-L14](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/LGPD.md#L14-L14)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](delphi-ai-developer.detail.md)

Metadata and full claim list: [full detail](delphi-ai-developer.detail.md)
Human notes ([notes](delphi-ai-developer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
