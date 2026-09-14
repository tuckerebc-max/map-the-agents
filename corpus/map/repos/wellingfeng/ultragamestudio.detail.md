# wellingfeng/ultragamestudio -- full detail

[Back to orientation](ultragamestudio.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/wellingfeng/ultragamestudio/034f599668f3221891764eb6ea5b966eb496e868/5040c6a7d94315f8.json](../../../wiki/dossiers/wellingfeng/ultragamestudio/034f599668f3221891764eb6ea5b966eb496e868/5040c6a7d94315f8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The stack comprises a Tauri 2/Rust desktop shell, React 18 with Vite 5 and TypeScript 5, Zustand state, Tailwind styling, and a Rust tiny_http+ureq free-channel proxy. -- evidence: [README.md#L47-L55](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L47-L55), [README.md#L320-L328](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L320-L328) (`clm_f2befee603eba2c798721201d2639b80a623459ee046a467f4f403cc8148d4c8`)
- [observation/documented] A local Rust reverse proxy binds to 127.0.0.1, routes per channel at /ch/<channelId>, and translates between Anthropic and OpenAI-compatible streaming protocols so Claude Code can use non-Anthropic providers. -- evidence: [README.md#L313-L316](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L313-L316), [README.md#L144-L148](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L144-L148) (`clm_7e84c9bdf4f55d12a16e1bb2ae41e88816c4cc4fa28666df3057b5ecd9a564ca`)

## design-choices (1 claim(s))

- [observation/documented] The product is local-first: sessions, favorites, scheduled prompts, API keys, and workspace history are stored locally and no hosted server is required. -- evidence: [README.md#L206-L208](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L206-L208) (`clm_548618c90af4c1a89aaefdcffc39efb3ff3156501eb9cfaa369a7796c65c6503`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run npm run dev/typecheck/lint/test/desktop/package from app/, and PRs should describe behavior changes, list verification commands, link issues, and include screenshots for UI changes. -- evidence: [README.md#L377-L377](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L377-L377), [README.md#L361-L368](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L361-L368) (`clm_c7ebfc5f4c708c03640b862adfd4dfbf3d2f5a68a470ad28c8b7ac1a17533ee0`)
- [observation/documented] Repository development practice: SELF-DEV.md advises running workflows from a packaged standalone exe via run.bat rather than tauri dev, since dev mode watches source and hot-reloads would interrupt running workflows; a copy-workspace approach is recommended for self-modification. -- evidence: [SELF-DEV.md#L36-L36](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L36-L36), [SELF-DEV.md#L29-L32](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L29-L32), [SELF-DEV.md#L3-L3](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L3-L3), [SELF-DEV.md#L9-L13](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/SELF-DEV.md#L9-L13) (`clm_badf96a20a9f857a7e17b9d1a4d984042532ddab3b4390ea7972f21e3d31826a`)

## skills-patterns (1 claim(s))

- [observation/documented] The agent ships a roster of 40+ game-development specialist roles spanning engine, programming, design, art/audio, and production categories, configurable in Settings including engine and council mode. -- evidence: [README.md#L140-L140](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L140-L140), [README.md#L134-L138](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L134-L138), [README.md#L132-L132](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L132-L132) (`clm_322478ee9294fd68dadfe7516285ccf3206f89c5046b34aaec97722196127a5b`)

## interfaces (2 claim(s))

- [observation/documented] Asset generation is exposed through slash commands: /image, /sprite, /music, /video, /mesh-mode-start, /comfyui-mode-start, /speech-mode-start, with matching *-mode-end commands to exit. -- evidence: [README.md#L292-L294](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L292-L294), [README.md#L128-L128](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L128-L128), [README.md#L118-L126](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L118-L126) (`clm_7942c565752f3d37f0cb9021bad2e02682e869d5b220ad8cf34cce6b5b7096b4`)
- [observation/documented] A CLI form exists for the studio harness: ugs studio "<task>" with --json, --interactive, and --cwd options, runnable alongside the desktop app. -- evidence: [README.md#L170-L174](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L170-L174) (`clm_ca34d827653f2bf0eae583919f995abb4e891ed7d6bedcb1013fcb271370d7f2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (4 claim(s))

- [observation/documented] The /studio command generates an on-the-fly execution harness with parallel subagents, adversarial verification, and acceptance gates, choosing among six internal strategies automatically. -- evidence: [README.md#L170-L174](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L170-L174), [README.md#L168-L168](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L168-L168) (`clm_515824913163e5afa7d73f33f7697120c7c9619afb69adab39c6bb59027c37ed`)
- [observation/documented] Each /studio run is logged under .ugs-run/<run-id>/ with a task ledger, events, verdict, and final result, and reuses local claude CLI credentials without extra config. -- evidence: [README.md#L170-L174](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L170-L174) (`clm_93a2f19a2722cf1e1db90b738671f4460fafe7bf4eae4e7ae4673dab23409aaf`)
- [observation/documented] An Auto channel (freecc:auto) rotates through configured free channels, skipping those returning 429 or 5xx, applying per-channel cooldown backoff, and returning 503 with a failure log when all are exhausted. -- evidence: [README.md#L178-L178](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L178-L178), [README.md#L180-L183](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L180-L183) (`clm_587a3b3bdfffa88a4fd1a1cd60f840dbe048965f4dc6cc57362c2812f7aa592c`)
- [observation/documented] Harness plans support per-step model overrides, enabling multi-provider chains such as DeepSeek for drafting and CodeX for refinement or consensus verification. -- evidence: [README.md#L189-L191](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L189-L191), [README.md#L187-L187](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L187-L187) (`clm_947bcb067c6603f001ca66d896e113baf273ac50251fd2a1e4bf9ee0d0c36143`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Routing supports 20+ remote channels (NVIDIA NIM, OpenRouter, GitHub Models, Hugging Face Router, Together AI, Gemini, DeepSeek, Groq, Cerebras, and others) plus local runtimes Ollama, LM Studio, and llama.cpp. -- evidence: [README.md#L144-L148](https://github.com/wellingfeng/UltraGameStudio/blob/034f599668f3221891764eb6ea5b966eb496e868/README.md#L144-L148) (`clm_a417f8bd57b85928f4ac80cd3c0d5a677e7962fc4d0515c83217e40e7dd3cf7a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

