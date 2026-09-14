# narcooo/inkos -- full detail

[Back to orientation](inkos.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/narcooo/inkos/091048383f411eb99948a8764f42b6fd13006f9b/856156b1ba1f1007.json](../../../wiki/dossiers/narcooo/inkos/091048383f411eb99948a8764f42b6fd13006f9b/856156b1ba1f1007.json)

## specifications (1 claim(s))

- [observation/documented] InkOS is distributed as the npm package @actalk/inkos, requires Node.js 22 or higher, and is licensed under AGPL-3.0. -- evidence: [README.md#L101-L101](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L101-L101), [README.md#L8-L14](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L8-L14), [README.md#L685-L685](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L685-L685) (`clm_9ac1e3dbec77d1104939c7eca813f193cc5c8d4b47199a93249d58628864603f`)

## components (2 claim(s))

- [observation/documented] The long-form pipeline uses specialized agents: Radar, Planner, Composer, Architect, Writer, Observer, Reflector, Normalizer, Auditor, and Reviser, each with documented responsibilities. -- evidence: [README.md#L437-L448](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L437-L448) (`clm_830a36ac5e6723bf17eb68c410374d624683bc37febdc112bb2d6c3cb9a1d708`)
- [observation/documented] Version 1.8.0 ships 15 built-in professional skills (long-form writing/review, shorts, Play, scripts, storyboards, interactive film, translation, import, covers, de-AI-flavor, etc.), each with its own SKILL.md. -- evidence: [README.md#L58-L67](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L58-L67), [CHANGELOG.en.md#L13-L16](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/CHANGELOG.en.md#L13-L16) (`clm_5b6ae0598c07a64af0973569496d5a6bf417eda076c07696525a8d2a2c6d295e`)

## design-choices (4 claim(s))

- [observation/documented] Chapter production follows plan → compose → write → audit → revise → state sync; context is organized into protected/compressible layers, and runtime artifacts (intent.md, context.json, rule-stack.yaml, trace.json) are compiled per chapter. -- evidence: [README.md#L381-L381](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L381-L381), [README.md#L479-L484](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L479-L484), [README.md#L430-L430](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L430-L430), [README.md#L76-L76](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L76-L76) (`clm_e4cabca259ea2e81744c58a15850502c10c7a5d9a668efee3df5a010f1df23ec`)
- [observation/documented] Prose, state, hooks, and run snapshots are validated in a chapter workspace and atomically committed together, so failures do not leave state advanced without persisted text. -- evidence: [CHANGELOG.en.md#L20-L23](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/CHANGELOG.en.md#L20-L23), [README.md#L58-L67](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L58-L67) (`clm_ef4b9e97508cb52f912eb536c5c775ed395a997e7834e7bd2c1b2d7ee6ee9e5c`)
- [observation/documented] Word-count governance treats --words as a target with an auto-derived allowed range, counts zh_chars or en_words by language, and applies at most one corrective normalization pass rather than hard truncation. -- evidence: [README.md#L387-L390](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L387-L390), [README.md#L385-L385](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L385-L385) (`clm_98fc83e7c1efcdbecd148c40264f2b5a2236ba6c927b4c884a3f45c426f2cf96`)
- [observation/documented] LLM configuration is split: Studio uses visual service config with keys in .inkos/secrets.json and ignores env overrides, while CLI/daemon/deployment supports env and one-shot flags with a documented precedence order. -- evidence: [README.md#L180-L180](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L180-L180), [README.md#L214-L221](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L214-L221), [README.md#L153-L153](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L153-L153), [README.md#L269-L274](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L269-L274) (`clm_545315facf4c5d2e5e2193ceea843fdc9f52282f4184105d69fe97e42b677d83`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors use pnpm install, pnpm dev, pnpm test, and pnpm typecheck, and are invited to open issues or PRs. -- evidence: [README.md#L637-L637](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L637-L637), [README.md#L639-L644](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L639-L644) (`clm_4909859a93ab0f4928e4f4e1b6ede064ba03ea3686b77cb4358d997367c8403b`)

## skills-patterns (2 claim(s))

- [observation/documented] InkOS consumes standard SKILL.md packages directly; skills provide instructions and static references only, add no execution permissions, and can be forced per turn with @skill-id or auto-selected by the chat agent via use_skill. -- evidence: [README.md#L129-L129](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L129-L129), [README.md#L133-L137](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L133-L137) (`clm_92c8a7f52acec7000ff3a73a1afbd68de9cbd05e82e541aa28609f773f4c002d`)
- [observation/documented] Skills can be placed in skills/, .agents/skills/, user directories like ~/.agents/skills/, or pointed to via the INKOS_SKILL_DIRS environment variable; Studio can import full skill folders. -- evidence: [README.md#L133-L137](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L133-L137) (`clm_c15be198da29bb5e00f9ed7f647a440ed3e271f4d5114bb406145824ea22ba2f`)

## interfaces (4 claim(s))

- [observation/documented] The product supports Studio (web workbench), TUI, and CLI interaction forms, all sharing one execution surface for creation tasks. -- evidence: [README.md#L27-L27](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L27-L27), [README.md#L278-L278](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L278-L278) (`clm_3867d90e2cca6167bd7525c91476ad4b3a40478885bd14c6863aa979c924c914`)
- [observation/documented] CLI commands include book create, write next, plan chapter, compose chapter, draft, audit, revise, and export with an EPUB format option; all commands support --json structured output. -- evidence: [README.md#L572-L615](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L572-L615), [README.md#L618-L618](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L618-L618), [README.md#L288-L296](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L288-L296), [README.md#L525-L525](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L525-L525), [README.md#L517-L523](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L517-L523) (`clm_02c2f24af90f671f4d4879ec56116363ac04888a845aa2b4e65a1e23c45ec4ba`)
- [observation/documented] The TUI provides slash commands such as /new, /short, /play, /cover, /write, /confirm, /cancel, and session-level /model switching. -- evidence: [README.md#L58-L67](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L58-L67), [README.md#L280-L284](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L280-L284) (`clm_25aed569f2a9627875720b017a289236e71da9e87655364e247c758957fdf29c`)
- [observation/documented] External agents can invoke InkOS via `inkos interact --json --message`, which shares the same execution kernel as the TUI and Studio and returns assistant text plus interaction session info. -- evidence: [README.md#L123-L123](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L123-L123), [README.md#L280-L284](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L280-L284), [README.md#L119-L121](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L119-L121) (`clm_003e55b3181af87dba75c0b6faafdb93df64e350468952f874be8a0af400287f`)

## memory-state (2 claim(s))

- [observation/documented] Each book's authoritative memory has three layers: Zod-validated JSON state under story/state/, human-readable Markdown projections, and a SQLite time-series memory database (story/memory.db) auto-enabled on Node 22+. -- evidence: [README.md#L469-L469](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L469-L469), [README.md#L458-L462](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L458-L462) (`clm_b89816cba5b19aab6f149fcaee2133b2565eb8d0d858b8b714228869a35326f2`)
- [observation/documented] Story memory, material library, and skill references share a SQLite FTS5/BM25 retrieval projection; source files remain authoritative and indexes are rebuildable, with results retaining source and location. -- evidence: [CHANGELOG.en.md#L20-L23](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/CHANGELOG.en.md#L20-L23), [README.md#L58-L67](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L58-L67) (`clm_68b587e937f3178cfdbc8ac6cf6912d2aac2d56014a11d80afc447f1074cee36`)

## orchestration (1 claim(s))

- [observation/documented] The runtime is built on a pi-agent harness: the agent produces structured actions, and the host executes deterministic tools, manages confirmations and state, and judges completion from real files and tool results rather than model claims. -- evidence: [README.md#L56-L56](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L56-L56), [README.md#L424-L424](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L424-L424), [CHANGELOG.en.md#L9-L9](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/CHANGELOG.en.md#L9-L9) (`clm_f1a54fe597ed80fa1bb23df6b9aa630849996aa2c6c471be10eb3f7a5ad7eeee`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The continuity auditor checks each chapter draft across 37 dimensions (character memory, resource continuity, foreshadowing, pacing, etc.) including AI-trace detection, with default one auto-revision adjustable via writing.reviewRetries. -- evidence: [README.md#L355-L355](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L355-L355), [README.md#L451-L451](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L451-L451) (`clm_ec250fa8776bb3bcc8029c258a284b90721e9d7af0b64c10aff3d417e2bf1dad`)

## dependencies (2 claim(s))

- [observation/documented] The agent runtime builds on the pi project (@mariozechner/pi-ai and @mariozechner/pi-agent-core by Mario Zechner), and the provider bank includes Gemini, Moonshot, MiniMax, OpenRouter, Ollama, and other OpenAI-compatible services. -- evidence: [README.md#L269-L274](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L269-L274), [README.md#L679-L679](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L679-L679) (`clm_f79877e7ef7a5219f645183de6fd144626e24e41686393b5db5a89f8d73c2d1d`)
- [observation/documented] Any OpenAI-compatible endpoint is supported via custom services or --provider custom; service tests probe protocol and streaming combinations and a fallback parser handles non-conforming small-model output. -- evidence: [README.md#L410-L410](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L410-L410) (`clm_63223965ce567fbf6798034e2ed19fa27954071ec6501e8ee784572c533e5792`)

## limitations (1 claim(s))

- [observation/documented] Per the README's compatibility notes, MiniMax M2.x thinking mode cannot be disabled due to upstream limitations, while M3* defaults to thinking disabled. -- evidence: [README.md#L265-L265](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L265-L265) (`clm_bcc5d085b41f5453e40e4a2acee7035778154c34d5c60c9c9f6cea8e2d359039`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

