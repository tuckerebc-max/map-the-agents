---
access: public
aliases: []
claim_ids:
- clm_411f234ba47e2b9aa89b952c8cc6146e38f6e9d879301e54efcee4206e0293ab
- clm_584185621e65a5da728527bd1cb2dfe83a01b7ac29ef448f26d5ccb3b3bbfbe8
- clm_5ff90ecc16983fdaedf282d8c9094acfbd941281b3bdd94b006417a2ae7fbb7b
- clm_64653353ca8da447f4a4ba884515fc556945824ab132da7f8f41c7ef6493ff98
- clm_7690a1605aa9636a6b79c4646b81f7440fc476eda6c11ff053a5ceddcd1e7850
- clm_aabd013dc46c2cb796d9ffda0973ad3f64ce925657bf582c5225eed4243bf84a
- clm_cfa7fd7c30c573a9868f44c37b9bc64b1e00770bd589a52ff6310ee9eec4d32c
- clm_e7d362946342bf2b8eaf672a141782180ab49ede03bf899c014c55a8dbcfc5ed
maturity: draft
page_id: pg_0018f3769605561dab649bba7913d9e5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c9098ce3c4405c8c8eb35e3894c9a7f8
title: KunAgent/Kun/README.md @ e67f656bca57
updated_at: '2026-09-14T02:10:53Z'
---

# KunAgent/Kun/README.md @ e67f656bca57

<!-- rcw:begin owner=source:src_c9098ce3c4405c8c8eb35e3894c9a7f8 block=evidence -->
- The project is licensed under PolyForm Noncommercial 1.0.0 for learning, research, and noncommercial use; commercial use, SaaS/hosting, or resale requires separate written authorization from the author. [@claim:clm_411f234ba47e2b9aa89b952c8cc6146e38f6e9d879301e54efcee4206e0293ab]
- Running from source requires Node.js 22.19+ and npm plus at least one working model connection; the project is built with npm scripts including dev, typecheck, lint, test, and build. [@claim:clm_584185621e65a5da728527bd1cb2dfe83a01b7ac29ef448f26d5ccb3b3bbfbe8]
- Kun is not tied to one model; presets cover ChatGPT/Codex, Claude, Gemini, Cursor, Ollama, DeepSeek, Kimi, GLM, Qwen, MiniMax, and Xiaomi MiMo ecosystems via provider configuration. [@claim:clm_5ff90ecc16983fdaedf282d8c9094acfbd941281b3bdd94b006417a2ae7fbb7b]
- The desktop GUI and terminal TUI share a single local `kun serve` runtime, sharing threads, goals, plans, approvals, and background tasks rather than separate sessions. [@claim:clm_64653353ca8da447f4a4ba884515fc556945824ab132da7f8f41c7ef6493ff98]
- Kun is described as a local-first AI agent workbench with two main modes: Code for software delivery (with a Design canvas in the same task) and Work for writing, document analysis, and presentations. [@claim:clm_7690a1605aa9636a6b79c4646b81f7440fc476eda6c11ff053a5ceddcd1e7850]
- Sessions, preferences, logs, and runtime data are stored locally by default; when a cloud model is chosen, prompts, attachments, and task context are sent to the selected provider, and tool/extension permissions are surfaced in the UI for user approval. [@claim:clm_aabd013dc46c2cb796d9ffda0973ad3f64ce925657bf582c5225eed4243bf84a]
- Repository development practice: contributions target the `develop` branch, contributors should read the contributing guide, and external contributions require signing a CLA; the CLA grants the project owner broad relicensing rights while contributors retain copyright. [@claim:clm_cfa7fd7c30c573a9868f44c37b9bc64b1e00770bd589a52ff6310ee9eec4d32c]
- Repository development practice: README documents npm commands for development (`npm run dev`, `dev:tui`), typecheck, ESLint with file-size checks, tests, production build, and per-platform distribution builds. [@claim:clm_e7d362946342bf2b8eaf672a141782180ab49ede03bf899c014c55a8dbcfc5ed]
<!-- rcw:end owner=source:src_c9098ce3c4405c8c8eb35e3894c9a7f8 block=evidence -->

## Researcher notes

