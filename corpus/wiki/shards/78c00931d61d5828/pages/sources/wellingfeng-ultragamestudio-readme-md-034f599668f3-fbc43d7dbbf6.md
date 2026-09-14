---
access: public
aliases: []
claim_ids:
- clm_322478ee9294fd68dadfe7516285ccf3206f89c5046b34aaec97722196127a5b
- clm_515824913163e5afa7d73f33f7697120c7c9619afb69adab39c6bb59027c37ed
- clm_548618c90af4c1a89aaefdcffc39efb3ff3156501eb9cfaa369a7796c65c6503
- clm_587a3b3bdfffa88a4fd1a1cd60f840dbe048965f4dc6cc57362c2812f7aa592c
- clm_7942c565752f3d37f0cb9021bad2e02682e869d5b220ad8cf34cce6b5b7096b4
- clm_7e84c9bdf4f55d12a16e1bb2ae41e88816c4cc4fa28666df3057b5ecd9a564ca
- clm_93a2f19a2722cf1e1db90b738671f4460fafe7bf4eae4e7ae4673dab23409aaf
- clm_947bcb067c6603f001ca66d896e113baf273ac50251fd2a1e4bf9ee0d0c36143
- clm_a417f8bd57b85928f4ac80cd3c0d5a677e7962fc4d0515c83217e40e7dd3cf7a
- clm_c7ebfc5f4c708c03640b862adfd4dfbf3d2f5a68a470ad28c8b7ac1a17533ee0
- clm_ca34d827653f2bf0eae583919f995abb4e891ed7d6bedcb1013fcb271370d7f2
- clm_f2befee603eba2c798721201d2639b80a623459ee046a467f4f403cc8148d4c8
maturity: draft
page_id: pg_9f57fe5094915da9b1b6fbc43d7dbbf6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a3b2dc981cf7590e9eeb6fef609c4211
title: wellingfeng/UltraGameStudio/README.md @ 034f599668f3
updated_at: '2026-09-14T03:22:47Z'
---

# wellingfeng/UltraGameStudio/README.md @ 034f599668f3

<!-- rcw:begin owner=source:src_a3b2dc981cf7590e9eeb6fef609c4211 block=evidence -->
- The agent ships a roster of 40+ game-development specialist roles spanning engine, programming, design, art/audio, and production categories, configurable in Settings including engine and council mode. [@claim:clm_322478ee9294fd68dadfe7516285ccf3206f89c5046b34aaec97722196127a5b]
- The /studio command generates an on-the-fly execution harness with parallel subagents, adversarial verification, and acceptance gates, choosing among six internal strategies automatically. [@claim:clm_515824913163e5afa7d73f33f7697120c7c9619afb69adab39c6bb59027c37ed]
- The product is local-first: sessions, favorites, scheduled prompts, API keys, and workspace history are stored locally and no hosted server is required. [@claim:clm_548618c90af4c1a89aaefdcffc39efb3ff3156501eb9cfaa369a7796c65c6503]
- An Auto channel (freecc:auto) rotates through configured free channels, skipping those returning 429 or 5xx, applying per-channel cooldown backoff, and returning 503 with a failure log when all are exhausted. [@claim:clm_587a3b3bdfffa88a4fd1a1cd60f840dbe048965f4dc6cc57362c2812f7aa592c]
- Asset generation is exposed through slash commands: /image, /sprite, /music, /video, /mesh-mode-start, /comfyui-mode-start, /speech-mode-start, with matching *-mode-end commands to exit. [@claim:clm_7942c565752f3d37f0cb9021bad2e02682e869d5b220ad8cf34cce6b5b7096b4]
- A local Rust reverse proxy binds to 127.0.0.1, routes per channel at /ch/<channelId>, and translates between Anthropic and OpenAI-compatible streaming protocols so Claude Code can use non-Anthropic providers. [@claim:clm_7e84c9bdf4f55d12a16e1bb2ae41e88816c4cc4fa28666df3057b5ecd9a564ca]
- Each /studio run is logged under .ugs-run/<run-id>/ with a task ledger, events, verdict, and final result, and reuses local claude CLI credentials without extra config. [@claim:clm_93a2f19a2722cf1e1db90b738671f4460fafe7bf4eae4e7ae4673dab23409aaf]
- Harness plans support per-step model overrides, enabling multi-provider chains such as DeepSeek for drafting and CodeX for refinement or consensus verification. [@claim:clm_947bcb067c6603f001ca66d896e113baf273ac50251fd2a1e4bf9ee0d0c36143]
- Routing supports 20+ remote channels (NVIDIA NIM, OpenRouter, GitHub Models, Hugging Face Router, Together AI, Gemini, DeepSeek, Groq, Cerebras, and others) plus local runtimes Ollama, LM Studio, and llama.cpp. [@claim:clm_a417f8bd57b85928f4ac80cd3c0d5a677e7962fc4d0515c83217e40e7dd3cf7a]
- Repository development practice: contributors run npm run dev/typecheck/lint/test/desktop/package from app/, and PRs should describe behavior changes, list verification commands, link issues, and include screenshots for UI changes. [@claim:clm_c7ebfc5f4c708c03640b862adfd4dfbf3d2f5a68a470ad28c8b7ac1a17533ee0]
- A CLI form exists for the studio harness: ugs studio "<task>" with --json, --interactive, and --cwd options, runnable alongside the desktop app. [@claim:clm_ca34d827653f2bf0eae583919f995abb4e891ed7d6bedcb1013fcb271370d7f2]
- The stack comprises a Tauri 2/Rust desktop shell, React 18 with Vite 5 and TypeScript 5, Zustand state, Tailwind styling, and a Rust tiny_http+ureq free-channel proxy. [@claim:clm_f2befee603eba2c798721201d2639b80a623459ee046a467f4f403cc8148d4c8]
<!-- rcw:end owner=source:src_a3b2dc981cf7590e9eeb6fef609c4211 block=evidence -->

## Researcher notes

