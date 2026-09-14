# opencode-plusplus (`opencode-plusplus`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: whut09
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=Download opencode-plusplus-setup-win-x64.exe from GitHub Releases; quit OpenCode Desktop; double-click EXE; reopen OpenCode Desktop (no admin rights needed, writes to %USERPROFILE%/.config/opencode)
- Model providers: none of its own (works offline against the single active OpenCode model)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [whut09/opencode-plusplus](../../repos/whut09/opencode-plusplus.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Narrow-scope reliability harness/plugin for OpenCode Desktop (Windows) that patches the command dispatcher (only 3 exact command names) to enable model-free local state control; adds guard rails (edit boundaries, dangerous command blocking, protected paths), evidence capture (redacted, hashed), and a closed-loop verify-and-repair workflow via /plusplus-task and /plusplus-verify slash commands; user-level Windows plugin requiring no admin privileges and no second desktop shell; ...

(captured site page body (agents/opencode-plusplus.md), not a verified repo-code finding)
OpenCode Desktop's agent produces diffs, but nothing forces it to work from verified repository context or to prove its commands actually ran against the current tree. OpenCode++ inserts that layer as an in-process Windows plugin: a context registry selects files with justification, a guard layer enforces protected paths and command policies, and an evidence module matches command and CI results to the working-tree hash before any decision is recorded. Work flows through a dashboard pipeline — Plan, Prepare, Retrieve, Execute, Collect, Evaluate, Decide, Persist, Finalize — with an intervention ledger tracking what was observed, prevented, repaired, or verified, and sanitized artifacts written to .agent-context/ for audit. Installation is a signed Windows x64 setup EXE from GitHub Releases that requires no admin, followed by selecting the OpenCode++ mode. It stays offline by default, operating on whatever model OpenCode already has, and bilingual English/Chinese docs serve its mixed audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencode-plusplus.md)
