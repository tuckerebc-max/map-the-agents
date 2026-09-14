# danilofalcao/jarvis -- full detail

[Back to orientation](jarvis.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/danilofalcao/jarvis/38a7c80794d71a00b61786cc18c92864301e9c27/365be3cf06291d31.json](../../../wiki/dossiers/danilofalcao/jarvis/38a7c80794d71a00b61786cc18c92864301e9c27/365be3cf06291d31.json)

## specifications (1 claim(s))

- [observation/documented] J.A.R.V.I.S. is described as an AI coding assistant leveraging multiple state-of-the-art language models for code generation, modification, and technical discussions. -- evidence: [README.md#L3-L3](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L3-L3) (`clm_ef372a72b2a0b8bc058ff90584b77958fcb389c8c9f583d397c72a282447f3fd`)

## components (2 claim(s))

- [observation/documented] The backend is documented as using the Flask web framework, Flask-SocketIO for WebSocket support, and Eventlet for async operations. -- evidence: [README.md#L72-L75](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L72-L75) (`clm_bb5673640078c1b80868b8530f71dd249e815d3a20b0f2229761219a73ce8f77`)
- [observation/documented] The frontend is documented as pure JavaScript with TailwindCSS, CodeMirror, Socket.IO client, PDF.js, Mammoth.js, XLSX.js, Tesseract.js, and Marked/Unified.js. -- evidence: [README.md#L77-L86](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L77-L86) (`clm_156902ea77f1d0d160b7e6fce4fda19ea389a5d56d59e1d84dcf49372f8ac15f`)

## design-choices (8 claim(s))

- [observation/documented] The product offers selectable AI models including DeepSeek R1/V3, Codestral, Gemini 2.0 Flash Experimental, Grok 2, Claude 3.5 Sonnet, GPT-4 Turbo, GPT-4o variants, and o1 models. -- evidence: [README.md#L18-L29](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L18-L29) (`clm_b1021e1226d838f4ffc5421db7a79c332e80cd14e545bbf36cd662fa45f76891`)
- [observation/documented] The changelog records that Qwen 2.5 Coder and Llama 3.3 70B Instruct support were discontinued and removed from the available model lineup. -- evidence: [CHANGELOG.md#L64-L66](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L64-L66) (`clm_3536279b8f1a85345c8ed92d661fabc256f126f17f7452d22f9d342f2b7f17fb`)
- [observation/documented] Under a 'Removed' changelog heading, archive file support (ZIP, RAR, 7z) is listed as removed. -- evidence: [CHANGELOG.md#L296-L296](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L296-L296) (`clm_da3be26045a96e93274a0dcc8fac6905c07ec6408f44b27895b3cc44d22845b9`)
- [observation/documented] The changelog describes a UI redesign inspired by Cursor IDE with bubble-style panels, a fixed-height chat input, and a reorganized workspace panel. -- evidence: [CHANGELOG.md#L218-L231](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L218-L231) (`clm_5deade71316ccf308821ff4afbb0eea335bd3c0b99b873b928ebb8dc69de20f7`)
- [observation/documented] The changelog lists AI-powered analysis features including code pattern suggestions, dependency analysis and visualization, security vulnerability scanning, and code quality assessment. -- evidence: [CHANGELOG.md#L158-L164](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L158-L164) (`clm_eebaa4209b1c5cef7929c4b74aa0a84dbc8250456dde8e5b6bcef134220eb408`)
- [observation/documented] The changelog records folder import as workspaces with symlink support, plus stricter file path validation and improved symlink handling under enhanced security. -- evidence: [CHANGELOG.md#L206-L213](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L206-L213), [CHANGELOG.md#L195-L203](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L195-L203) (`clm_0278900238645004bb08147f0eba2c1dd48a8fe75cbf0ae1a2cb987322207609`)
- [observation/documented] The changelog notes large-codebase handling via paginated directory browsing, lazy loading of folder contents, and a memory-optimized file tree. -- evidence: [CHANGELOG.md#L167-L172](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L167-L172) (`clm_5bf92b424876eddec5a3cbfd75329d6f667f87f209d4fb145a1450e2f2887708`)
- [observation/documented] The changelog lists SQLite-based history tracking and file diff previews among the initial feature set. -- evidence: [CHANGELOG.md#L323-L329](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/CHANGELOG.md#L323-L329) (`clm_43ca2bed9ab4097e142c182714529ef9a43de0f12db6ce1e330d0d0ebba47fa2`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README invites contributions via pull requests. -- evidence: [README.md#L133-L133](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L133-L133) (`clm_10097a35fadb6844c554c1e28507912a26242dae737bb94b3464457004c84c6f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] The app is started with 'python app.py' and accessed at http://localhost:5000, where users create or select a workspace and choose an AI model. -- evidence: [README.md#L108-L115](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L108-L115) (`clm_5fb462fa8f95119daac248f0641bdf9d42def79cee4473b1817d58fd351c853e`)
- [observation/documented] An integrated terminal is documented with cross-platform support, xterm.js integration, real-time output streaming, command history, and native shells (cmd.exe on Windows, bash on Linux). -- evidence: [README.md#L9-L16](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L9-L16) (`clm_0ec3dce3e6975952bc76929740b1b306f48f4d04d2f0ae813b4bdca3c8a41b6c`)
- [observation/documented] File attachment support covers PDFs with text extraction, .docx, Excel parsing, image OCR, Markdown with GFM, code and config files, with previews and multiple uploads. -- evidence: [README.md#L31-L43](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L31-L43) (`clm_f745b5cac16baae219ea759375e38641e4bb38365e692469a4417ae1ab6d1bcb`)
- [observation/documented] Real-time updates are delivered via WebSocket-based notifications for code changes and workspace updates. -- evidence: [README.md#L45-L49](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L45-L49) (`clm_a3003c1dace6fd341fc5b152539173f444818522c1821627e847ae17a5e80236`)
- [observation/documented] Workspace management lets users create, rename, and delete multiple workspaces, view workspace history, and browse the workspace file structure. -- evidence: [README.md#L51-L56](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L51-L56) (`clm_9915fa9fb4220a1dd280a882cd255b6b0daa2f775df44163d4ad59d5c2ba9ebc`)
- [observation/documented] Code generation features include generating code from natural-language prompts, modifying existing code, previewing changes, and viewing diffs before applying. -- evidence: [README.md#L58-L62](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L58-L62) (`clm_3dbb5a2b9ea18f2fd6b6d14eca04665097fbd94c550298c77ea39b9e660f6a98`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Setup involves pip-installing requirements.txt and setting .env API keys for DeepSeek, Codestral, OpenRouter, Google, Grok, Anthropic, and OpenAI. -- evidence: [README.md#L90-L104](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L90-L104) (`clm_5f59c8fe2fdaf7d528abcbed132a64de26137ffcf5f0521a5ec1667a95bdedd1`)
- [observation/documented] The project is MIT-licensed (copyright 2024-2025 Danilo Falcão) with the standard permission grant and as-is, no-warranty disclaimer. -- evidence: [LICENSE.md#L3-L3](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L3-L3), [LICENSE.md#L15-L21](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L15-L21), [LICENSE.md#L5-L10](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L5-L10), [LICENSE.md#L1-L1](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/LICENSE.md#L1-L1) (`clm_7314dffeba10293e26c0d594d33ecc79a27fc6ca9cec212d2b0efe75b3e20b26`)

## limitations (1 claim(s))

- [observation/documented] The app is documented as tested on Linux, WSL 2, and native Windows, using directory junctions on Windows to avoid requiring admin privileges. -- evidence: [README.md#L150-L150](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L150-L150), [README.md#L145-L148](https://github.com/danilofalcao/jarvis/blob/38a7c80794d71a00b61786cc18c92864301e9c27/README.md#L145-L148) (`clm_8d8dc2c11c536e151873b7bdb3651d5fc3b690f86b0245d3ff65bf8300ed90b4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

