---
access: public
aliases: []
claim_ids:
- clm_16d43335a7bcd44660f219cba308ffe4536c5339080eb465f626b5022a30707c
- clm_27928b1a8f71bd1151c07835a1ccf7c68ecdd7652558b8b94a6a2e014bf15d3a
- clm_598591c31020e723ccfe711ca433001074cfef4c3f9841053120198bc15a26e8
- clm_5c22cc44217616e2d5d904e69206b0f7eb528f2deef6a42c5fe78b70315bbb12
- clm_65681661242f27f44d30df6e5eccdbe69e23ebda9676a62bce250c5c465bdca5
- clm_728277689f0f0bdd63bc54d7630decaee69658e9775f2ae2ecda039be7b47c8a
- clm_d975a0b6cdce10dfefc6859497e00509664da66c578689ee0e97c5b38c0e4316
- clm_e4010c7b6011cc99f0b548fc133c4a9b34ece1f04cb5b2df5986df952c6230fa
- clm_ed148cfccefa9fe98049544ee7bfda1add4f97113aa25bf37af9bc16301e3f4e
- clm_eee98137ca9d49a20d6d4e07890519935a319aac12d3a7e9c7b574fbe8889c59
maturity: draft
page_id: pg_3edda6ab134c5ab997a4b3f7eb19e291
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4d24a2ba0f2b5b468f1b59b32a53d94b
title: rizwan3d/StemCode/docs/documentation.md @ dfe4dd789988
updated_at: '2026-09-14T02:36:28Z'
---

# rizwan3d/StemCode/docs/documentation.md @ dfe4dd789988

<!-- rcw:begin owner=source:src_4d24a2ba0f2b5b468f1b59b32a53d94b block=evidence -->
- The CLI binary is documented as self-contained and AOT-compiled, and all installers expose the same `stemcode` command from the same release assets. [@claim:clm_16d43335a7bcd44660f219cba308ffe4536c5339080eb465f626b5022a30707c]
- Desktop sections are saved local conversation threads per workspace that preserve history, active model, profile, thinking mode, plan state, and session state when available. [@claim:clm_27928b1a8f71bd1151c07835a1ccf7c68ecdd7652558b8b94a6a2e014bf15d3a]
- Providers span subscription sign-in (ChatGPT Plus/Pro, Claude Pro/Max, GitHub Copilot), API-key providers (OpenAI, Anthropic, Gemini, OpenRouter, Groq, DeepSeek, and others), OpenAI-compatible endpoints, and local providers such as Ollama. [@claim:clm_598591c31020e723ccfe711ca433001074cfef4c3f9841053120198bc15a26e8]
- The product uses approval prompts, permissions, and profiles to keep actions under human control; `--sandbox-mode` overrides sandbox policy per run with read-only, workspace-write, or danger-full-access values. [@claim:clm_5c22cc44217616e2d5d904e69206b0f7eb528f2deef6a42c5fe78b70315bbb12]
- The npm `stemcode` package is a thin installer that downloads the matching release binary and verifies it against published SHA256SUMS, with no .NET toolchain required; targets include win-x64, osx-x64, osx-arm64, linux-x64, and linux-arm64. [@claim:clm_65681661242f27f44d30df6e5eccdbe69e23ebda9676a62bce250c5c465bdca5]
- Release assets publish SHA256SUMS and GitHub artifact attestations; the release pipeline verifies each checksum before publishing, and `gh attestation verify` is documented for provenance checks. [@claim:clm_728277689f0f0bdd63bc54d7630decaee69658e9775f2ae2ecda039be7b47c8a]
- The CLI supports options including `--acp`, `--stdin`, `--json`, `-p/--prompt`, `--sandbox-mode`, `--session`, `--profile`, `--thinking`, and `--doctor`. [@claim:clm_d975a0b6cdce10dfefc6859497e00509664da66c578689ee0e97c5b38c0e4316]
- Built-in tracked edit tools include `file_write`, `apply_patch`, `insert_content`, and `search_and_replace`, which record before/after state and participate in `/undo`, `/redo`, and edit summaries. [@claim:clm_e4010c7b6011cc99f0b548fc133c4a9b34ece1f04cb5b2df5986df952c6230fa]
- StemCode ships as a desktop app, a `stemcode` terminal command, VS Code and Visual Studio extensions, and an ACP-compatible editor server. [@claim:clm_ed148cfccefa9fe98049544ee7bfda1add4f97113aa25bf37af9bc16301e3f4e]
- Budget controls are disabled by default and activate only via `/budget local`, `/budget cloud`, or an existing `.stemcode/budget-controls.*.json` file; while disabled, no usage is recorded and provider requests are never blocked. [@claim:clm_eee98137ca9d49a20d6d4e07890519935a319aac12d3a7e9c7b574fbe8889c59]
<!-- rcw:end owner=source:src_4d24a2ba0f2b5b468f1b59b32a53d94b block=evidence -->

## Researcher notes

