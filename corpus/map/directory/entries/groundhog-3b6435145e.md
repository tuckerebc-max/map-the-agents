# groundhog (`groundhog`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ghuntley
- License: AGPL-3.0
- Language: Rust
- Interface: install=cargo build (Rust toolchain)
- Model providers: not yet integrated (early stage)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ghuntley/groundhog](../../repos/ghuntley/groundhog.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Educational AI coding assistant built to teach how Cursor and other coding agents work under the hood; built incrementally as part of an educational series. Not a production tool.

(captured site page body (agents/groundhog.md), not a verified repo-code finding)
groundhog is an educational coding assistant built in public by Ghuntley to show how tools like Cursor actually work under the hood, developed increment-by-increment with its audience following along at ghuntley.com/specs. The implementation is Rust-based with a CLI surface that currently offers an explain command for code snippets and files, with further commands planned and documented in a specs directory covering architecture, CLI, commands, and telemetry. The author explicitly frames it as a teaching artifact rather than a production tool, directing users who need finished software to established agents and asking that bug reports be held while the community model is decided. Development has stalled at a single commit, so it functions today as a reference for anyone studying how agent harnesses are assembled from first principles.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/groundhog.md)
