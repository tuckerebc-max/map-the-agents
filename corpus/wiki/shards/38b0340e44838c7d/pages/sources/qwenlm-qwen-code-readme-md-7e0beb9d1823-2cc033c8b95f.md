---
access: public
aliases: []
claim_ids:
- clm_087625134d58de08f29b7d6db36d59d42238b63c6209f66d7963572e6ca75ff6
- clm_110a3814d4d12db7b301a02be5711930193930f1730ac15a4b35f6e90ddcae23
- clm_254bea1c00a829fc129a389f13de362f4c10ee854fbfdd18b64958c24034b408
- clm_5e578832269ca9d7a4f80cefa8da12ade2d771e104b97f986b1ab9a323cbda68
- clm_8e0cb7db4b61a63442af47fb149dede015d4c3bfecf21cc08189cabeb5a57040
- clm_cda91ac3d6e68c0fe48d71a3c99e331cf3416a0f6c067eb357cdfd29248ae0c2
- clm_d93e84acb57184c6b602b37a0466ed377676b55cf30dc20766760a81754e90d4
- clm_ea38d7ebb4fdafa5771e94f673c8eb20e4362289e183ac1bb1dd18d6796e71de
maturity: draft
page_id: pg_d3d4c321184153ab8be42cc033c8b95f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0223cfa9e0ba5300ab46d42e77375e48
title: QwenLM/qwen-code/README.md @ 7e0beb9d1823
updated_at: '2026-09-14T02:34:00Z'
---

# QwenLM/qwen-code/README.md @ 7e0beb9d1823

<!-- rcw:begin owner=source:src_0223cfa9e0ba5300ab46d42e77375e48 block=evidence -->
- NPM installation requires Node.js 22+; the project was originally based on Google Gemini CLI v0.8.2 but stopped syncing upstream starting from Qwen Code v0.1. [@claim:clm_087625134d58de08f29b7d6db36d59d42238b63c6209f66d7963572e6ca75ff6]
- Repository development practice: contributions are directed to CONTRIBUTING.md for guidelines. [@claim:clm_110a3814d4d12db7b301a02be5711930193930f1730ac15a4b35f6e90ddcae23]
- The product offers multiple invocation surfaces: an interactive `qwen` TUI started in a project directory, headless `qwen -p "..."` for scripts/CI, and an experimental `qwen serve` daemon exposing HTTP + SSE (ACP). [@claim:clm_254bea1c00a829fc129a389f13de362f4c10ee854fbfdd18b64958c24034b408]
- Inside a session, `/auth` configures the provider and API key; the CLI is started by running `qwen` in a project directory. [@claim:clm_5e578832269ca9d7a4f80cefa8da12ade2d771e104b97f986b1ab9a323cbda68]
- The agent supports multiple model protocols — OpenAI, Anthropic, Gemini, and Qwen APIs — plus third-party or local providers (Ollama/vLLM), switchable at runtime. [@claim:clm_8e0cb7db4b61a63442af47fb149dede015d4c3bfecf21cc08189cabeb5a57040]
- The README reports a SWE-bench Verified evaluation (500 cases, 3 trials per version, model Qwen 3.7 Max) with average scores between roughly 76.4% and 77.8% across seven Qwen Code versions. [@claim:clm_cda91ac3d6e68c0fe48d71a3c99e331cf3416a0f6c067eb357cdfd29248ae0c2]
- Qwen Code is positioned as an open-source AI coding agent for terminal, editor, desktop, browser, and chat, aiming for feature parity with Claude Code plus multi-protocol and daemon-mode extras. [@claim:clm_d93e84acb57184c6b602b37a0466ed377676b55cf30dc20766760a81754e90d4]
- SDKs exist for TypeScript, Python, and Java; the Python SDK exposes an async `query()` taking a cwd and path to the qwen executable, streaming messages from which result messages are printed. [@claim:clm_ea38d7ebb4fdafa5771e94f673c8eb20e4362289e183ac1bb1dd18d6796e71de]
<!-- rcw:end owner=source:src_0223cfa9e0ba5300ab46d42e77375e48 block=evidence -->

## Researcher notes

