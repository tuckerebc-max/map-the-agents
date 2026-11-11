# WebCode (`webcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: shuyu-labs
- License: AGPL-3.0
- Language: C#
- Interface: platforms=CLI, Web; install=docker compose up -d; or dotnet run --project WebCodeCli; or Windows installer from GitHub Releases
- Model providers: Claude Code, Codex, OpenCode (via cc-switch)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [shuyu-labs/webcode](../../repos/shuyu-labs/webcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Browser-based AI CLI work platform that wraps Claude Code, Codex, and OpenCode into a manageable, deployable, collaborative, remotely-accessible system with Web, mobile, and Feishu (Lark) unified session flow. Supports multi-user, permissions, external session import/recovery, Superpowers workflows, Codex /goal, and cc-switch as the sole provider authority.

(captured site page body (agents/webcode.md), not a verified repo-code finding)
WebCode addresses the operational problem of running AI coding CLIs for a team or across machines: sessions are tied to local terminals and hard to share, secure, or reach remotely. It wraps Claude Code, Codex, and OpenCode into a self-hostable Blazor Server (.NET 10) platform where sessions can be created, restored from raw CLI transcripts, bound to workspaces, and accessed from web, mobile, or Feishu (Lark) chats with streaming card output. Multi-user support includes per-user CLI restrictions, directory whitelists, and Feishu bot bindings, with provider switching centralized through cc-switch. An office-assistant mode extends the same session infrastructure to planning, summaries, and document drafting. It is self-hosted via Docker or Windows installers under AGPLv3, aimed at teams wanting shared, remotely accessible agent sessions.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/webcode.md)
