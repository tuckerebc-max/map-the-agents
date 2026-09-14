# aider-ai/aider -- full detail

[Back to orientation](aider.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aider-ai/aider/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/0f2903302b000314.json](../../../wiki/dossiers/aider-ai/aider/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/0f2903302b000314.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Aider builds a map of the entire codebase (repo map) to work well in larger projects, with tree-sitter based support for many languages including Fortran, Haskell, Julia, Zig, Kotlin, Scala, OCaml, Dart and MATLAB. -- evidence: [README.md#L51-L52](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L51-L52), [HISTORY.md#L307-L320](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L307-L320), [HISTORY.md#L574-L584](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L574-L584), [HISTORY.md#L439-L447](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L439-L447), [HISTORY.md#L5-L20](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L5-L20) (`clm_c527cd885acece952ead5836dcc5051135f126b3c9a9e85f92015429de1d6baf`)
- [observation/documented] Aider integrates with git, automatically committing changes with generated commit messages so users can diff, manage and undo AI edits with normal git tools. -- evidence: [README.md#L65-L66](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L65-L66) (`clm_131cd072eefb6531c8a7fa73ea71d89e27afb8fa1db278358505e460549ee56a`)

## design-choices (2 claim(s))

- [observation/documented] Aider supports multiple edit formats per model family, including diff, udiff-simple, patch, editor-diff, editor-whole and editor-diff-fenced, and can auto-select the best format in architect mode. -- evidence: [HISTORY.md#L154-L163](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L154-L163), [HISTORY.md#L180-L186](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L180-L186) (`clm_03a7158d89e6bacf74bd5b958629670b055c8180ab8496acbc559e9706606918`)
- [observation/documented] Model-specific behaviors are configurable: thinking-tokens and reasoning-effort settings, temperature disabling for GPT-5 models, and per-model weak/editor model defaults. -- evidence: [HISTORY.md#L39-L41](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L39-L41), [HISTORY.md#L62-L87](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L62-L87), [HISTORY.md#L307-L320](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L307-L320), [HISTORY.md#L285-L297](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L285-L297), [HISTORY.md#L24-L24](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L24-L24) (`clm_78145070fba69f2d173d5a216dca54c3329b9c27dd660f8d03730ea3b7613bd9`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: release notes state that Aider itself wrote a large share of each release's code (e.g. 88% in v0.86.0 and 92% in v0.82.0), indicating heavy dogfooding of the tool in its own development. -- evidence: [HISTORY.md#L180-L186](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L180-L186), [HISTORY.md#L28-L29](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L28-L29) (`clm_ee21edf5f502abee4183d2bf0cbf5db3d7512f0ac7cea0c5745a43b7c443c4d1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Aider is a terminal application for AI pair programming with LLMs, usable to start new projects or work on existing codebases. -- evidence: [README.md#L5-L7](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L5-L7), [README.md#L10-L12](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L10-L12) (`clm_e154632775f096e2ac5c66041bccac217a2b4215f09372ff4ef6121147812bfe`)
- [observation/documented] The CLI accepts --model and --api-key flags, e.g. aider --model deepseek --api-key deepseek=<key>, and models can be selected via short aliases like sonnet or o3-mini. -- evidence: [README.md#L119-L120](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L119-L120), [README.md#L113-L113](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L113-L113), [README.md#L116-L116](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L116-L116) (`clm_9023d5a1e58b9cae3e007214a6d8ffc8fc9f258bd542abdbec892a58c78320c0`)
- [observation/documented] Aider provides slash commands such as /model, /undo, /clear, /run, /test, /diff, /editor, /copy-context, /save and /load for in-session control. -- evidence: [HISTORY.md#L240-L259](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L240-L259), [HISTORY.md#L49-L54](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L49-L54), [HISTORY.md#L501-L513](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L501-L513), [HISTORY.md#L592-L605](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L592-L605), [HISTORY.md#L58-L58](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L58-L58), [HISTORY.md#L538-L549](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L538-L549), [HISTORY.md#L649-L665](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L649-L665) (`clm_fb941bb5e91e20baa0148d463c45ba18af0ed02c88388be7e11fba5b5c186d21`)
- [observation/documented] A watch-files mode lets users add AI-prefixed comments in any file from their IDE or editor to trigger aider, and a --copy-paste mode streamlines working with LLM web chat UIs. -- evidence: [HISTORY.md#L517-L534](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L517-L534), [HISTORY.md#L501-L513](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L501-L513), [README.md#L100-L101](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L100-L101), [README.md#L72-L73](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L72-L73) (`clm_db369e10891cc1804f16eabb655f543d6c0f68789c639ecca92ea63a26f48b2c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The project maintains a public code-editing leaderboard; release notes cite model scores on it (e.g. Claude 3.5 Haiku at 75%) and benchmark statistics include token counts. -- evidence: [README.md#L136-L140](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L136-L140), [HISTORY.md#L118-L150](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L118-L150), [HISTORY.md#L634-L645](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L634-L645) (`clm_d1cc5dadf9eb1d6e5dffebd7572c3d6e16b487a6f3aaf1961c60b243e2550b03`)

## dependencies (1 claim(s))

- [observation/documented] Aider depends on litellm for LLM connectivity; several releases bumped litellm (e.g. 1.75.0) to pick up provider fixes, and the deprecated google-generativeai dependency was removed. -- evidence: [HISTORY.md#L45-L45](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L45-L45), [HISTORY.md#L5-L20](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L5-L20), [HISTORY.md#L301-L303](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L301-L303), [HISTORY.md#L221-L221](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L221-L221) (`clm_cbea6b719deefdd1e687304fd00b32e40375e52d034d5ad81e5605f34c067c49`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Aider connects to a wide range of LLM providers (Anthropic, OpenAI, DeepSeek, Gemini, OpenRouter, Bedrock, Vertex AI, Ollama, xAI) and works with most popular programming languages. -- evidence: [HISTORY.md#L62-L87](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L62-L87), [HISTORY.md#L361-L365](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L361-L365), [HISTORY.md#L91-L99](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L91-L99), [README.md#L58-L59](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L58-L59), [HISTORY.md#L195-L202](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/HISTORY.md#L195-L202), [README.md#L44-L45](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md#L44-L45) (`clm_8b82a09e4e018106e3a4669f45a48ac1782f2f47ab0ae029df06319b6299ad91`)

