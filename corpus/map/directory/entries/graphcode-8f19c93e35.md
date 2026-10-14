# GraphCode (`graphcode`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: scgopi
- License: FSL-1.1-MIT
- Language: Swift
- Interface: platforms=CLI, Desktop; install=brew install --cask scgopi/graphcode/graphcode, or the signed .dmg from GitHub Releases
- Model providers: Claude Code, GitHub Copilot CLI, Codex CLI, OpenCode (the agent CLIs bring their own providers)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [scgopi/graphcode](../../repos/scgopi/graphcode.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agent sessions are nodes on a graph and the edges do the coordinating: a hand-off, message, or spawn edge fires when one loop resolves, so a chain of work runs unattended while every node stays a live terminal you can attach to and correct mid-run.

(captured site page body (agents/graphcode.md), not a verified repo-code finding)
GraphCode exists because running one coding-agent session in a terminal is easy and running ten connected ones is not: the moment work fans out, the human becomes the scheduler. It types each loop by what ends it: a turn-based loop pauses for review each turn, a goal-based loop resolves when its done check passes (optionally a shell predicate that exits 0), a time-based loop keeps its cadence inside the agent's own prompt, and a composite loop runs a sub-graph of loops end to end. A launchd daemon fires the edges between loops, polls goal predicates, and keeps unattended sessions alive whether or not the app is open; each terminal is a zmx session that survives quitting the app and rebooting, and the backend's session id is persisted so a relaunch resumes the conversation instead of starting a duplicate. GraphCode bundles no agent: it launches whichever supported CLI is on your PATH, a running loop can create and wire further loops through the bundled graphcode CLI, projects can live on a remote machine over SSH with the Mac only steering, and nothing is ever written inside a project folder you open. Built on Ghostty for terminal rendering and requiring macOS 15 or later on Apple Silicon, it is aimed at developers who already work in Claude Code, Copilot CLI, Codex, or OpenCode and want to hand off whole chains of work and come back to steerable terminals rather than finished ...
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/graphcode.md)
