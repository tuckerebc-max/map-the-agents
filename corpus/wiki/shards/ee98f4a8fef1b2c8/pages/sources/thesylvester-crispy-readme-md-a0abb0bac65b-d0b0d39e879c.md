---
access: public
aliases: []
claim_ids:
- clm_2c0036dac8036e23e5ab46bc8b73f5ccf3c698a4572b6df12d9c29380f4c1b20
- clm_51e275040077a908f7f40b476e9491dfdc3697b12aa3feac6e1daa72f4ef6e74
- clm_7273e54032990d00833896455c0012f6bc36d00419dc74e6d846a0df9b98a497
- clm_78a23726e10d5758a231084fe7e0a58db96d0a0bd355375d3be4185f3ab9152b
- clm_9f1a326baced9df668784628df7d439c1222532ccfd7eb77d1f4b2e76d37633c
- clm_a60400ef709db3506b802e53231cd9ead249c9b7297d388dee795827ca7c2e7a
- clm_ae864fe566106b10b679583a1fa5acec78a9bc9e259563b7dc474cf5790d3ca0
- clm_b752527e5b50a24c7c5b0ed3160935ebe3091c8b74d718479b2dfb74da3220c8
- clm_cdbcee30d34a2edf073e048143b5007994e69dc0733789bf3b89e0126e1b5fba
- clm_d02e948032a95abfcfd04ce905af03614878ccf94d51637b68d165a32ad37334
maturity: draft
page_id: pg_71a5fdea13cf50e1acc5d0b0d39e879c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_22de63cd85ad5c6aa2e78c8129030fd9
title: TheSylvester/crispy/README.md @ a0abb0bac65b
updated_at: '2026-09-14T03:18:51Z'
---

# TheSylvester/crispy/README.md @ a0abb0bac65b

<!-- rcw:begin owner=source:src_22de63cd85ad5c6aa2e78c8129030fd9 block=evidence -->
- Runtime requirements are Node.js 18+ for standalone use or VS Code 1.94+ for the extension, plus the Claude Code and/or Codex CLIs for whichever vendors are used. [@claim:clm_2c0036dac8036e23e5ab46bc8b73f5ccf3c698a4572b6df12d9c29380f4c1b20]
- Agent memory indexes every session transcript locally with full-text and semantic search, backfills existing Claude Code and Codex transcripts, and recall results show match provenance with date/recency filters. [@claim:clm_51e275040077a908f7f40b476e9491dfdc3697b12aa3feac6e1daa72f4ef6e74]
- Per the architecture doc, only the Claude adapter is wired up today, and the roadmap lists Gemini CLI and OpenCode support as coming soon. [@claim:clm_7273e54032990d00833896455c0012f6bc36d00419dc74e6d846a0df9b98a497]
- The standalone dev/standalone server listens on HTTP + WebSocket at port 3456 and serves the static webview bundle, auto-registering the Claude adapter at startup. [@claim:clm_78a23726e10d5758a231084fe7e0a58db96d0a0bd355375d3be4185f3ab9152b]
- The Windows desktop app auto-provisions WSL and the Crispy daemon; v0.3.4 fixed a WSL detection loop caused by reading an orphaned pre-rename node_modules/crispy/ directory. [@claim:clm_9f1a326baced9df668784628df7d439c1222532ccfd7eb77d1f4b2e76d37633c]
- The Claude adapter depends on Anthropic's proprietary @anthropic-ai/claude-agent-sdk (required for Claude Code integration); Codex protocol types are generated from the Apache-2.0 OpenAI Codex CLI project. [@claim:clm_a60400ef709db3506b802e53231cd9ead249c9b7297d388dee795827ca7c2e7a]
- /superthink pits Claude and Codex against each other on the same question and converges into a unified verdict, with sub-agents opening as live watchable tabs; /super-implement, /reflect, /handoff, and /spec-mode support planning workflows. [@claim:clm_ae864fe566106b10b679583a1fa5acec78a9bc9e259563b7dc474cf5790d3ca0]
- Agency modes (plan, auto-accept, --dangerously-skip-permissions) are one-click toggles persisted per session, and a per-host Discord bot toggle lets multiple instances share one server with only one posting. [@claim:clm_b752527e5b50a24c7c5b0ed3160935ebe3091c8b74d718479b2dfb74da3220c8]
- Crispy ships in three form factors: a VS Code/Cursor extension (also on OpenVSX), a standalone npm package (crispy-code) opening in the browser, and a Windows Tauri desktop installer with auto-update. [@claim:clm_cdbcee30d34a2edf073e048143b5007994e69dc0733789bf3b89e0126e1b5fba]
- Tool use can be approved or denied remotely via inline Discord approval buttons, and the Discord integration uses fail-closed auth with an allowlist and a setup wizard. [@claim:clm_d02e948032a95abfcfd04ce905af03614878ccf94d51637b68d165a32ad37334]
<!-- rcw:end owner=source:src_22de63cd85ad5c6aa2e78c8129030fd9 block=evidence -->

## Researcher notes

