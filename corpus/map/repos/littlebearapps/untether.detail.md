# littlebearapps/untether -- full detail

[Back to orientation](untether.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/littlebearapps/untether/4285dad5a12e4e4113c9cc5240972a67bbb5e218/0436e3cf05c6d927.json](../../../wiki/dossiers/littlebearapps/untether/4285dad5a12e4e4113c9cc5240972a67bbb5e218/0436e3cf05c6d927.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Configuration lives in ~/.untether/untether.toml with sections for default engine, Telegram transport, projects, and cost budgets (per-run and daily limits). -- evidence: [README.md#L214-L218](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L214-L218), [README.md#L210-L212](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L210-L212), [README.md#L205-L208](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L205-L208), [README.md#L200-L200](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L200-L200) (`clm_aca1767cd9d8929f9e05307db2817ab2ff1f939eef3904df91511b568702ac3d`)

## design-choices (1 claim(s))

- [observation/documented] The setup wizard offers three workflow modes: Assistant (ongoing chat with auto-resume), Workspace (forum topics bound to project/branch), and Handoff (reply-to-continue). -- evidence: [README.md#L73-L77](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L73-L77) (`clm_a819b4da41daf5c2dbe1db3e709b06ac0bdb4e969f1223a5ee8d366f48a88d60`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors use Python 3.12+, anyio, msgspec, structlog, Ruff linting, pytest with an 80% coverage threshold, Australian English in user-facing text, and conventional commits on feature/*, fix/*, docs/* branches. -- evidence: [AGENTS.md#L21-L25](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/AGENTS.md#L21-L25) (`clm_87ea772b021742f0f67028c4bdf2c33ba73685758949616319c4c8ccef7e2463`)
- [observation/documented] Repository development practice: every runner must emit exactly one StartedEvent, zero or more ActionEvents, and exactly one final CompletedEvent, constructed via EventFactory rather than directly. -- evidence: [AGENTS.md#L29-L32](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/AGENTS.md#L29-L32), [AGENTS.md#L34-L34](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/AGENTS.md#L34-L34) (`clm_41631d2f3a7955ab436b180210962da24879eeb96a6559fcab06afb1c1296be6`)
- [observation/documented] Repository development practice: a mandatory three-phase release workflow (dev, TestPyPI rc fleet rollout, PyPI release) requires integration testing against @untether_dev_bot before releases, enforced by a fleet-rollout attestation gate. -- evidence: [CLAUDE.md#L261-L261](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/CLAUDE.md#L261-L261), [CLAUDE.md#L255-L257](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/CLAUDE.md#L255-L257) (`clm_56011007b0fc28fc8e938cfe09cee27f15f08cbf3718448235f4210f631dd928`)
- [observation/documented] Repository development practice: project hooks block pushes to master/main, tag creation, PR merges, and releases, and GitHub rulesets plus CODEOWNERS require PR review for master changes. -- evidence: [CLAUDE.md#L282-L284](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/CLAUDE.md#L282-L284), [CLAUDE.md#L163-L173](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/CLAUDE.md#L163-L173) (`clm_bfaf6223089274045f647b53f105d40ef4e27b4fe764e4fbddd36246a1e4d796`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Users interact via Telegram bot commands including /cancel, /agent, /model, /planmode, /usage, /export, /browse, /config, /continue, /file put/get, /topic, /restart, /stats, and /auth. -- evidence: [README.md#L167-L190](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L167-L190) (`clm_f382a85c34006e18520b3e2a88346d45e32c42de27b2042721812aafac564c79`)
- [observation/documented] Messages can be prefixed with /<engine> to pick an engine for that task, or /<project> to target a specific repository. -- evidence: [README.md#L192-L192](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L192-L192) (`clm_9445284e2146a59245061fe01141bbd51f4ef4b6e8db1bc58657abea916ef249`)

## memory-state (1 claim(s))

- [observation/documented] Untether stores chat preferences, session state, and usage stats as JSON files under ~/.untether/, plus an optional per-project .untether-outbox/ directory for agent-delivered files. -- evidence: [README.md#L307-L320](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L307-L320) (`clm_ab0639465f1e7fff79e5cec4903ced71ec8b736dc0dfdfacdfbb862d4acaa208`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Interactive permission buttons let users approve plan transitions and answer clarifying questions; tools auto-execute, and a 'Pause & Outline Plan' option holds the session open for plan review. -- evidence: [README.md#L89-L110](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L89-L110) (`clm_49501f1b98b09b75d69a22cab16b61dd0d53928aaaab173f2bbcc1ca0b05e2e0`)
- [observation/documented] Interactive permissions, plan mode, ask mode, diff preview, and auto-approve of safe tools are Claude Code-only; other engines use pre-run approval policies or none. -- evidence: [README.md#L154-L159](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L154-L159), [README.md#L129-L152](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L129-L152) (`clm_05da2199c8cbefd3d715c7fc7795486b35a72e2e67b2780131609550d4708336`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requirements are Python 3.12+, uv, and at least one agent CLI (claude, codex, opencode, pi, gemini, or amp) on PATH. -- evidence: [README.md#L252-L254](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L252-L254) (`clm_1471504e3f262621d255002347a22c61acf67e4e95af3d8185a31e9b8fa7dc7e`)
- [observation/documented] Voice transcription uses a configurable Whisper-compatible endpoint and is disabled by default, opt-in via config. -- evidence: [README.md#L89-L110](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L89-L110), [README.md#L307-L320](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L307-L320) (`clm_e2553660f069fc179c37fc6b213858c828575630d6d1313facd0a9d1b242b063`)

## limitations (1 claim(s))

- [observation/documented] For several engines (Codex, Pi, Gemini, Amp), cost tracking reports token usage counts only, with no USD cost reporting. -- evidence: [README.md#L154-L159](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L154-L159), [README.md#L129-L152](https://github.com/littlebearapps/untether/blob/4285dad5a12e4e4113c9cc5240972a67bbb5e218/README.md#L129-L152) (`clm_ffb49ff8ed633bd5177c42c0238ce0db7a3f945904cda8a03ef1490b2f242399`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

