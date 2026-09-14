---
access: public
aliases: []
claim_ids:
- clm_1fc47716ca4b45f065ea8e07ee736ebbfe058da967728431cee52df7cf8fdeeb
- clm_2c962fe3fb8b0e08eb4bdf0e27182a7f2325d4d2afd11a5fc27945859c97a218
- clm_66444387b3258616d3bbadd052d91a323811eb6e43a72b0c2af8738ebbdebae4
- clm_66e6bb78e704f367e2b9a731507899d964beeab371eee0a20ceaa69f9ebe1572
- clm_6d48cb196ea12f9523eb26ff71576bfdc99d70e096073bb8b715deb5ada93811
- clm_9a747d4b3299db6f04e4ef4107e25799d1f69e8bf800cd34ecc57a3b1b2f7fbf
- clm_a59cd720f80a3546294818c84947c582c058c394fd37939bb205a65e92046e7a
- clm_a69b4f8637668c206f48411b24049dc5fa7d07abf8d9bd116ac5ec19364de449
- clm_abd22f7ea7acdd2a5dc01c842a56c88e8cbb9d7956ee370b44548ea42dbc5730
- clm_b06e6c4010e23dfcb83ee5b4f1fc476d9626a873362249d303b7b150748598d7
- clm_d7a1ffcb8a8c306e0b48d2a89a74ef43c3ab9877882a23caaa64246620817d9a
- clm_da3186d6d657068d89b343e6e34d5752d1349c292065e6b460461d58d35cc523
maturity: draft
page_id: pg_529fd0df331957f1a183bf1b92dee830
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ff9a427c49fc59cc8faf4740846b85d5
title: 5dive-ai/5dive/README.md @ 420651c634b0
updated_at: '2026-09-14T01:28:46Z'
---

# 5dive-ai/5dive/README.md @ 420651c634b0

<!-- rcw:begin owner=source:src_ff9a427c49fc59cc8faf4740846b85d5 block=evidence -->
- Requirements are a Linux host with systemd (Ubuntu 22.04+ recommended) and root for install; the installer apt-installs jq, tmux, and other dependencies, and a Docker image exists for hosts without systemd or root. [@claim:clm_1fc47716ca4b45f065ea8e07ee736ebbfe058da967728431cee52df7cf8fdeeb]
- `5dive ui` serves a local, read-only web UI on loopback (default port 8735) with org chart, queue, gates, and triggers views; it refuses routable --host addresses unless FIVE_UI_ALLOW_REMOTE=1 is set. [@claim:clm_2c962fe3fb8b0e08eb4bdf0e27182a7f2325d4d2afd11a5fc27945859c97a218]
- Delegated git push uses the operator's own GitHub App: the agent never holds a token; pushes are gate-gated on a human- or reviewer-cleared ship gate, restricted to one non-protected branch, and executed in a root-only helper with a repo-scoped short-lived token. [@claim:clm_66444387b3258616d3bbadd052d91a323811eb6e43a72b0c2af8738ebbdebae4]
- 5dive does not auto-update; operators run `5dive self-update` manually or on a cron schedule, which refreshes the CLI, hooks, skills, and plugins and restarts running agents. [@claim:clm_66e6bb78e704f367e2b9a731507899d964beeab371eee0a20ceaa69f9ebe1572]
- The orchestrator is deliberately just bash: each agent is its own Linux user running an official coding CLI as a systemd service, with no framework, protocol, or broker; agents coordinate by invoking one shared 5dive CLI. [@claim:clm_6d48cb196ea12f9523eb26ff71576bfdc99d70e096073bb8b715deb5ada93811]
- Multiple agent types are supported, including claude, codex, antigravity, grok, devin, hermes, openclaw, opencode, and pi, each with its own auth options and channel support (Telegram and/or Discord). [@claim:clm_9a747d4b3299db6f04e4ef4107e25799d1f69e8bf800cd34ecc57a3b1b2f7fbf]
- The CLI offers durable team memory with provenance via `5dive memory search`, and Claude-runtime agents keep project memory under ~/.claude/projects/<dir>/memory/ across restarts. [@claim:clm_a59cd720f80a3546294818c84947c582c058c394fd37939bb205a65e92046e7a]
- The repo publishes a 'zero-human' badge measured as releases shipped versus decisions escalated to a human, presented as evidence that the agents building 5dive.ai operate autonomously on the same binary. [@claim:clm_a69b4f8637668c206f48411b24049dc5fa7d07abf8d9bd116ac5ec19364de449]
- Agents take work from a shared SQLite task queue on one host, report up an org chart, hand work to each other, and escalate to a human via Telegram only when a decision is needed. [@claim:clm_abd22f7ea7acdd2a5dc01c842a56c88e8cbb9d7956ee370b44548ea42dbc5730]
- Each agent runs as its own Linux user under one of three isolation tiers: standard (shared read, limited write), admin (full host, auto-granted to the first agent on a fresh box), or sandboxed (own home, no sudo, systemd resource limits). [@claim:clm_b06e6c4010e23dfcb83ee5b4f1fc476d9626a873362249d303b7b150748598d7]
- Repository development practice: the 5dive bundle at the repo root is built from src/ via ./build.sh, and CI enforces that the bundle does not drift; contributing guidance lives in CONTRIBUTING.md. [@claim:clm_d7a1ffcb8a8c306e0b48d2a89a74ef43c3ab9877882a23caaa64246620817d9a]
- The 5dive CLI exposes verbs for agent lifecycle (create/start/stop/logs/config), tasks, goals, loops, council, trace, run metrics, memory search, triggers, heartbeat, org, ui, account, and team import; every command accepts --json with an {ok,data}/{ok:false,error} envelope and exit codes matching error.code. [@claim:clm_da3186d6d657068d89b343e6e34d5752d1349c292065e6b460461d58d35cc523]
<!-- rcw:end owner=source:src_ff9a427c49fc59cc8faf4740846b85d5 block=evidence -->

## Researcher notes

