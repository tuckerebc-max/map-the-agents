# codealmanac (`codealmanac`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: AlmanacCode
- License: Apache-2.0
- Language: Python
- Interface: install=pip (uv tool install)
- Model providers: Codex, Claude (via Yoke Python Agent SDK)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: partial (skills/subagents/workflows folders) (reported)
  - claude_code_plugin: no (no)
  - subagents: yes (Yoke native subagents/ folder) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [almanaccode/codealmanac](../../repos/almanaccode/codealmanac.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-maintained wiki that lives in your repo as plain markdown, committed and reviewed like code, giving agents durable context the codebase can't encode. Auto-ingests from agent conversations (syncs local Codex/Claude transcripts). Garden mode schedules agent runs to prune stale pages, fix weak links, dedupe knowledge. Local-first, no cloud upload. Y Combinator S26-backed.

(captured site page body (agents/codealmanac.md), not a verified repo-code finding)
Codealmanac gives coding agents durable project knowledge that the code itself cannot express — rationale, invariants, incident history, cross-file workflows — by maintaining a markdown wiki inside the repository that agents read as context and humans review as ordinary commits. The tool syncs local Codex and Claude Code transcripts on a schedule, extracting durable knowledge into the wiki, and runs scheduled garden passes in which agents prune outdated pages, fix weak links, and merge duplicates. Everything stays local: indexing, storage, and the scheduled launchd jobs run on the developer's machine, with changes committed through git for normal review. It runs lifecycle agents through a Yoke provider boundary supporting Codex and Claude Code, installs via uv from PyPI (the legacy npm package is retired), and requires macOS and Python 3.12 or later.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codealmanac.md)
