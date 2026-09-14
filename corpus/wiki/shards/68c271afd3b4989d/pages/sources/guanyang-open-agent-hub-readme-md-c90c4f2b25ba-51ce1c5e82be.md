---
access: public
aliases: []
claim_ids:
- clm_03243d4a4a8589c88a69b0266e1a9fb1d75106a6e6143e991dfad6a5b013d91e
- clm_05ead86cc9099c73b7454b891c51f24213613ef455f421f28e347b70e53432c1
- clm_2a24b0d54acef71baa62a0642f967e44a946db75a1e9d62fbde2eb5c81c6a629
- clm_4d7f59ce6db9a2a0085ede3639ae87b2597fed536e2c41ff078eaa4fb43a1e6d
- clm_7b4d2adfb07d2156621f177dccfe6d17a5b52ddf3dd77a9e936efed4df5441c6
- clm_95df2b689817c869eef4a8e3a7b09da3077b3e886284d83ede2c9ed549791f9c
- clm_a1f72dca6c30518bf8dc05977680759a2e33d68ee3f195d9b44b81808c6a6687
- clm_d84a5fc1d2e34b5563dd03f8bc0b7f9916b30fd4fdcc14f2567ea130005c8117
maturity: draft
page_id: pg_15de4f2269195134ab9d51ce1c5e82be
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_030de828c05c55128ca80ea7478b1e40
title: guanyang/open-agent-hub/README.md @ c90c4f2b25ba
updated_at: '2026-09-14T03:56:25Z'
---

# guanyang/open-agent-hub/README.md @ c90c4f2b25ba

<!-- rcw:begin owner=source:src_030de828c05c55128ca80ea7478b1e40 block=evidence -->
- Activation works by dynamically symlinking Skills, Agents, and Commands into subdirectories (skills/, agents/, commands/) of each assistant's project or global config directory. [@claim:clm_03243d4a4a8589c88a69b0266e1a9fb1d75106a6e6143e991dfad6a5b013d91e]
- Besides directory linking, native plugin configurations are provided for Claude Code (.claude-plugin/), Codex (.codex-plugin/), and Cursor (.cursor-plugin/). [@claim:clm_05ead86cc9099c73b7454b891c51f24213613ef455f421f28e347b70e53432c1]
- Skills can alternatively be installed via Vercel's `skills` CLI (npx skills@latest add guanyang/open-agent-hub) without cloning the repository. [@claim:clm_2a24b0d54acef71baa62a0642f967e44a946db75a1e9d62fbde2eb5c81c6a629]
- Repository development practice: GEMINI.md provides project-level LLM coding behavioral guidelines (think before coding, simplicity first, surgical changes, goal-driven execution) derived from andrej-karpathy-skills, and CONTRIBUTING.md covers contribution guidelines. [@claim:clm_4d7f59ce6db9a2a0085ede3639ae87b2597fed536e2c41ff078eaa4fb43a1e6d]
- Components use standardized Markdown prompts with YAML frontmatter metadata, which host agents parse to decide when to trigger and load skills. [@claim:clm_7b4d2adfb07d2156621f177dccfe6d17a5b52ddf3dd77a9e936efed4df5441c6]
- The tool is described as a lightweight, zero-dependency CLI for managing and activating AI coding assistant capabilities. [@claim:clm_95df2b689817c869eef4a8e3a7b09da3077b3e886284d83ede2c9ed549791f9c]
- The --target option supports claude, antigravity, gemini, codex, cursor, trae, opencode, kiro, and all, defaulting to claude. [@claim:clm_a1f72dca6c30518bf8dc05977680759a2e33d68ee3f195d9b44b81808c6a6687]
- The `oah` CLI provides list, status, enable, disable, and sync commands, with filters (--skills/--agents/--commands), --global, --target, and --path options. [@claim:clm_d84a5fc1d2e34b5563dd03f8bc0b7f9916b30fd4fdcc14f2567ea130005c8117]
<!-- rcw:end owner=source:src_030de828c05c55128ca80ea7478b1e40 block=evidence -->

## Researcher notes

