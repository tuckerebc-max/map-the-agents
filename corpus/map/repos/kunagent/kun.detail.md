# kunagent/kun -- full detail

[Back to orientation](kun.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kunagent/kun/e67f656bca573d5e6a4970a5094a30f3afd09011/2169da6efe174106.json](../../../wiki/dossiers/kunagent/kun/e67f656bca573d5e6a4970a5094a30f3afd09011/2169da6efe174106.json)

## specifications (2 claim(s))

- [observation/documented] Kun is described as a local-first AI agent workbench with two main modes: Code for software delivery (with a Design canvas in the same task) and Work for writing, document analysis, and presentations. -- evidence: [README.md#L35-L35](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L35-L35) (`clm_7690a1605aa9636a6b79c4646b81f7440fc476eda6c11ff053a5ceddcd1e7850`)
- [observation/documented] The project is licensed under PolyForm Noncommercial 1.0.0 for learning, research, and noncommercial use; commercial use, SaaS/hosting, or resale requires separate written authorization from the author. -- evidence: [CLA.md#L59-L61](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/CLA.md#L59-L61), [README.md#L153-L153](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L153-L153) (`clm_411f234ba47e2b9aa89b952c8cc6146e38f6e9d879301e54efcee4206e0293ab`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The extension platform is documented as not creating a second agent runtime; extensions reach agent, tool, approval, and provider capabilities only through a public Host Context and Broker. -- evidence: [docs/extensions/architecture.md#L9-L9](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L9-L9) (`clm_1079f0f1c270f7ffb2fd232ea071d9e8042de8b457a1407e4280626b596223b6`)
- [observation/documented] Sessions, preferences, logs, and runtime data are stored locally by default; when a cloud model is chosen, prompts, attachments, and task context are sent to the selected provider, and tool/extension permissions are surfaced in the UI for user approval. -- evidence: [README.md#L84-L84](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L84-L84) (`clm_aabd013dc46c2cb796d9ffda0973ad3f64ce925657bf582c5225eed4243bf84a`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions target the `develop` branch, contributors should read the contributing guide, and external contributions require signing a CLA; the CLA grants the project owner broad relicensing rights while contributors retain copyright. -- evidence: [CLA.md#L20-L24](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/CLA.md#L20-L24), [README.md#L149-L149](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L149-L149), [CLA.md#L14-L16](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/CLA.md#L14-L16) (`clm_cfa7fd7c30c573a9868f44c37b9bc64b1e00770bd589a52ff6310ee9eec4d32c`)
- [observation/documented] Repository development practice: README documents npm commands for development (`npm run dev`, `dev:tui`), typecheck, ESLint with file-size checks, tests, production build, and per-platform distribution builds. -- evidence: [README.md#L123-L131](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L123-L131) (`clm_e7d362946342bf2b8eaf672a141782180ab49ede03bf899c014c55a8dbcfc5ed`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The desktop GUI and terminal TUI share a single local `kun serve` runtime, sharing threads, goals, plans, approvals, and background tasks rather than separate sessions. -- evidence: [README.md#L104-L104](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L104-L104), [README.md#L37-L37](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L37-L37) (`clm_64653353ca8da447f4a4ba884515fc556945824ab132da7f8f41c7ef6493ff98`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] ExtensionManager runs one Node child process per active Node extension over versioned private JSON IPC, lazily starts hosts on activation, merges concurrent activations, and enforces bounded time, concurrency, rate, and memory limits. -- evidence: [docs/extensions/architecture.md#L11-L29](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L11-L29), [docs/extensions/architecture.md#L48-L54](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L48-L54), [docs/extensions/architecture.md#L56-L56](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L56-L56) (`clm_ab761180148e462781f85e3e894b9001c2d26683ceb7597c452a5ada6deec468`)

## tools-permissions (1 claim(s))

- [observation/documented] Each Broker operation re-checks extension enablement, workspace trust and permission grants, resource ownership, request schema/rate limits, and whether protected user confirmation via an ApprovalGate is required. -- evidence: [docs/extensions/architecture.md#L62-L66](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L62-L66), [docs/extensions/architecture.md#L60-L60](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L60-L60) (`clm_52ea4a9340407fe75eaa81afd541104c98d277673f14c5f1ce1dc4840ec7321a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Running from source requires Node.js 22.19+ and npm plus at least one working model connection; the project is built with npm scripts including dev, typecheck, lint, test, and build. -- evidence: [README.md#L114-L114](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L114-L114), [README.md#L116-L121](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L116-L121), [README.md#L123-L131](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L123-L131) (`clm_584185621e65a5da728527bd1cb2dfe83a01b7ac29ef448f26d5ccb3b3bbfbe8`)
- [observation/documented] Kun is not tied to one model; presets cover ChatGPT/Codex, Claude, Gemini, Cursor, Ollama, DeepSeek, Kimi, GLM, Qwen, MiniMax, and Xiaomi MiMo ecosystems via provider configuration. -- evidence: [README.md#L86-L86](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/README.md#L86-L86) (`clm_5ff90ecc16983fdaedf282d8c9094acfbd941281b3bdd94b006417a2ae7fbb7b`)

## limitations (1 claim(s))

- [observation/documented] Node extensions run with the current user's OS permissions, and the docs state that process isolation is not a security sandbox; Node can bypass the Broker to call OS file, network, and process APIs directly. -- evidence: [docs/extensions/architecture.md#L35-L40](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L35-L40), [docs/extensions/architecture.md#L68-L68](https://github.com/KunAgent/Kun/blob/e67f656bca573d5e6a4970a5094a30f3afd09011/docs/extensions/architecture.md#L68-L68) (`clm_feacdc7b0bdb590ea341c1be5d53a973d8b08b144a4ee04cff384c31bcd1fb65`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

