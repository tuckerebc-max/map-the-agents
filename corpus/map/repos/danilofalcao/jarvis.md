# danilofalcao/jarvis

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 38a7c80794d7 @ 365be3cf06291d31

## Summary (orientation draft, not independently verified)

The evidence is documentation-only (README, CHANGELOG, LICENSE) describing J.A.R.V.I.S., a Flask-based web AI coding assistant with multi-model support, workspace management, file attachments, an integrated terminal, and WebSocket updates. All claims below rest on these product docs; no runtime code is in the snapshot.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 21 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

21 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] J.A.R.V.I.S. is described as an AI coding assistant leveraging multiple state-of-the-art language models for code generation, modification, and technical discussions. -- evidence: [README.md#L3-L3](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] The backend is documented as using the Flask web framework, Flask-SocketIO for WebSocket support, and Eventlet for async operations. -- evidence: [README.md#L72-L75](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L72-L75)
  - [observation/documented] The frontend is documented as pure JavaScript with TailwindCSS, CodeMirror, Socket.IO client, PDF.js, Mammoth.js, XLSX.js, Tesseract.js, and Marked/Unified.js. -- evidence: [README.md#L77-L86](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L77-L86)
- design-choices (8 claim(s)):
  - [observation/documented] The product offers selectable AI models including DeepSeek R1/V3, Codestral, Gemini 2.0 Flash Experimental, Grok 2, Claude 3.5 Sonnet, GPT-4 Turbo, GPT-4o variants, and o1 models. -- evidence: [README.md#L18-L29](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L18-L29)
  - [observation/documented] The changelog records that Qwen 2.5 Coder and Llama 3.3 70B Instruct support were discontinued and removed from the available model lineup. -- evidence: [CHANGELOG.md#L64-L66](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L64-L66)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README invites contributions via pull requests. -- evidence: [README.md#L133-L133](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L133-L133)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] The app is started with 'python app.py' and accessed at http://localhost:5000, where users create or select a workspace and choose an AI model. -- evidence: [README.md#L108-L115](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L108-L115)
  - [observation/documented] An integrated terminal is documented with cross-platform support, xterm.js integration, real-time output streaming, command history, and native shells (cmd.exe on Windows, bash on Linux). -- evidence: [README.md#L9-L16](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L9-L16)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Setup involves pip-installing requirements.txt and setting .env API keys for DeepSeek, Codestral, OpenRouter, Google, Grok, Anthropic, and OpenAI. -- evidence: [README.md#L90-L104](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L90-L104)
  - [observation/documented] The project is MIT-licensed (copyright 2024-2025 Danilo Falcão) with the standard permission grant and as-is, no-warranty disclaimer. -- evidence: [LICENSE.md#L3-L3](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L3-L3), [LICENSE.md#L15-L21](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L15-L21), [LICENSE.md#L5-L10](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L5-L10), [LICENSE.md#L1-L1](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L1-L1)
- limitations (1 claim(s)):
  - [observation/documented] The app is documented as tested on Linux, WSL 2, and native Windows, using directory junctions on Windows to avoid requiring admin privileges. -- evidence: [README.md#L150-L150](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L150-L150), [README.md#L145-L148](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L145-L148)
More evidence: [full detail](jarvis.detail.md)

Metadata and full claim list: [full detail](jarvis.detail.md)
Human notes ([notes](jarvis.notes.md), never overwritten by build)

[Back to map index](../../index.md)
