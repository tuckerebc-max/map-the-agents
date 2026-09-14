# varie-ai/workstation -- full detail

[Back to orientation](workstation.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/varie-ai/workstation/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/225530cf02383a58.json](../../../wiki/dossiers/varie-ai/workstation/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/225530cf02383a58.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A built-in bridge watches Claude Code sessions and sends notifications with screenshots when Claude finishes, requests plan approval, or asks a question. -- evidence: [README.md#L148-L148](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L148-L148), [README.md#L150-L154](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L150-L154) (`clm_3f40c0a853b4240e1bad9b4e0b7ce6388c82a6c26b6349e0e4a0a4aba98893a0`)

## design-choices (2 claim(s))

- [observation/documented] The app claims to run entirely locally with no telemetry or analytics; checkpoints, session data, and configuration live in ~/.varie/ and are not synced or uploaded. -- evidence: [README.md#L277-L280](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L277-L280), [README.md#L275-L275](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L275-L275) (`clm_cd24e80e5f82a371a78f8db48cc15d8b5e513198026b1a8c6ce437b2ea282934`)
- [observation/documented] Voice audio is processed on-device via Apple Speech or WhisperKit, while LLM-based voice routing and OpenClaw agent integration are opt-in features that are off by default. -- evidence: [README.md#L277-L280](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L277-L280) (`clm_7785b688ed7f9c3bfa41769ff29915425f6836aa9448d09710d6369b7fe840dc`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors build from source with npm install and npm run dev, run tests via npm run test, and package for macOS with npm run package:mac. -- evidence: [README.md#L88-L93](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L88-L93), [README.md#L297-L302](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L297-L302) (`clm_7ce3008e2f654dc55a8408535297418effaf7becc66a83c965b413a5bb15ff43`)

## skills-patterns (1 claim(s))

- [observation/documented] The plugin provides work-tracking skills such as /work-resume with fuzzy matching, /work-recover for post-crash checkpoint comparison, /work-stats for token usage, and /discover-projects to scan for new repos. -- evidence: [README.md#L252-L269](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L252-L269) (`clm_62086a27ed101af178fb8563ea49a4d5c53757405dcd1fe40132626868d4b12e`)

## interfaces (2 claim(s))

- [observation/documented] The product exposes slash commands including /work-start, /work-checkpoint, /work-report, /work-sessions, /route, /dispatch, /projects, and /workstation for session tracking, routing, and configuration. -- evidence: [README.md#L242-L246](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L242-L246), [README.md#L252-L269](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L252-L269), [README.md#L237-L239](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L237-L239) (`clm_a2b86b492164dbc5c0c0ae608eb0903f6cf0d7e30e888ac178f29ad523152e51`)
- [observation/documented] Screenshot capture supports three modes: session (Electron built-in, no permission), session plus multi-page scrollback via --pages N (max 10), and full-screen capture requiring macOS Screen Recording. -- evidence: [README.md#L187-L187](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L187-L187), [README.md#L181-L185](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L181-L185) (`clm_95432d4abf23910412895f00d58af8dec3c3b57c5d21c77794b6888a58379a0b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (3 claim(s))

- [observation/documented] Sessions are identified by repo/project name, and commands like 'run tests in my-app' are routed to the matching session automatically without needing session IDs. -- evidence: [README.md#L165-L168](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L165-L168), [README.md#L138-L138](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L138-L138) (`clm_68b14ea6f3db612a08093ac44838119765a610bed18d46589bfc0d11dbb439ca`)
- [observation/documented] A manager terminal serves as a central hub for cross-project commands, and multiple Claude Code sessions can run side-by-side with auto-dispatch by repo name, task ID, or context. -- evidence: [README.md#L47-L51](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L47-L51) (`clm_5b61714f336aa29e3a394092cfca07e54f91c3827823fca3e27e1b7dd37f3ae5`)
- [observation/documented] Remote mode turns on automatically when the agent dispatches or creates a session, can be toggled manually from the top bar, and turning it off stops phone notifications. -- evidence: [README.md#L144-L146](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L144-L146) (`clm_dfb840c9d874c7017eb239e4a942abd2737c5b7cab30de6635043f15370b6394`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requirements are macOS 12 or later and the Claude Code CLI; remote control additionally depends on installing OpenClaw globally and running its gateway. -- evidence: [README.md#L57-L57](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L57-L57), [README.md#L120-L123](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L120-L123) (`clm_e6529f096555a5988eb60322282d314226ef6aaa1c9f32cdf8ad8684f5053ff2`)
- [observation/documented] Voice routing via LLM providers (Gemini, Claude, GPT) uses the user's own API key, and Gemini direct-audio transcription requires a Gemini API key. -- evidence: [README.md#L219-L223](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L219-L223), [README.md#L277-L280](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L277-L280), [README.md#L41-L44](https://github.com/varie-ai/workstation/blob/96d500b5cbb04cd9e6d7fe1c489b3e7224685953/README.md#L41-L44) (`clm_9720598889587e92f96ca81c59bc5b750d78f5a11366b3e6e471b38e7f56bbf1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

