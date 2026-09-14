---
access: public
aliases: []
claim_ids:
- clm_0bdf3ad755279b20dc2cdf76e202c766c339f8fc0c6fa68dc16d3896c4140f43
- clm_150b395f7f29843d07ce5140d29260b0aef513ddfb0c2c63729c720cad005f29
- clm_2929c9a941b9b177a2c2b23d466b31633afe5495aaf8d48cc5275ed311070e6d
- clm_471bc2006d66076d78180ecdd35f562327cd33eea584472c90ba5205c8beca48
- clm_485351eacc6c4c9e5178ec7a259199c840e61270f7b49d3e2e77bd77589f06ee
- clm_826b4ab57436728791fd3e246da44a122d50fc6f270597566eff4b816809111f
- clm_88f8897dcdd82b2bc128f44a6edd2889a2dd609032981ea5f72c689fa5a80245
- clm_aa91f3cd8e00f1038f0642b4ddad49270ffd46eff271899f42bb88928a5560ef
- clm_f0b286b5159d06786ef6d6efc694c78ef59c848b171f22134e16fd8ccb31ab93
maturity: draft
page_id: pg_1a96d35335635b3985bf0bb88ceecc1a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cf78e11954445d4b8b89cd2fedfc8e17
title: letta-ai/letta-code/README.md @ f2bd2392a824
updated_at: '2026-09-14T02:12:21Z'
---

# letta-ai/letta-code/README.md @ f2bd2392a824

<!-- rcw:begin owner=source:src_cf78e11954445d4b8b89cd2fedfc8e17 block=evidence -->
- Agents can be interacted with through a local CLI, a desktop app for macOS/Windows/Linux, a browser client at chat.letta.com, and messaging integrations such as Telegram, Slack, and Discord. [@claim:clm_0bdf3ad755279b20dc2cdf76e202c766c339f8fc0c6fa68dc16d3896c4140f43]
- Agents rewrite their own context over time, including system-prompt learning via memory blocks and skill learning, with periodic 'dreaming' configurable via /sleeptime. [@claim:clm_150b395f7f29843d07ce5140d29260b0aef513ddfb0c2c63729c720cad005f29]
- Agent context, including memory blocks, is tracked via git under MemFS and can be synced to a user's GitHub repository via /memory-repository set. [@claim:clm_2929c9a941b9b177a2c2b23d466b31633afe5495aaf8d48cc5275ed311070e6d]
- AgentFile (.af) export/import has been removed: /export, /download, --import, and --from-af are no longer supported, though memory and transcript export are unaffected. [@claim:clm_471bc2006d66076d78180ecdd35f562327cd33eea584472c90ba5205c8beca48]
- The CLI exposes slash commands including /sleeptime, /doctor, /palace, /search, /memory-repository, /skills, /skill-creator, /connect, /model, and /login. [@claim:clm_485351eacc6c4c9e5178ec7a259199c840e61270f7b49d3e2e77bd77589f06ee]
- Built-in subagents (general-purpose, forked, recall, history-analyzer) can run in the background, and agents can call any other agent, including themselves, as subagents. [@claim:clm_826b4ab57436728791fd3e246da44a122d50fc6f270597566eff4b816809111f]
- Letta Code is distributed as the npm package @letta-ai/letta-code, installed globally via npm, and run with the `letta` command in a project directory. [@claim:clm_88f8897dcdd82b2bc128f44a6edd2889a2dd609032981ea5f72c689fa5a80245]
- Skills load from global (~/.letta), project-scoped (.agents/skills), and agent-scoped (MemFS) locations, and can be installed from GitHub, ClawHub, or Hermes Skills Hub with `letta skills install`. [@claim:clm_aa91f3cd8e00f1038f0642b4ddad49270ffd46eff271899f42bb88928a5560ef]
- Cloud-stored agents can run on multiple machines: `letta server --computer-name` registers a computer, `letta computers list/current` manage routing, and `--computer` routes headless messages to a specific machine or the cloud sandbox. [@claim:clm_f0b286b5159d06786ef6d6efc694c78ef59c848b171f22134e16fd8ccb31ab93]
<!-- rcw:end owner=source:src_cf78e11954445d4b8b89cd2fedfc8e17 block=evidence -->

## Researcher notes

