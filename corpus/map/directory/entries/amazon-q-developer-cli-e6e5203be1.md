# Amazon Q Developer CLI (`amazon-q-developer-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: aws
- License: MIT,Apache-2.0
- Language: Rust
- Interface: platforms=CLI; install=brew install --cask amazon-q (macOS), DMG, AppImage (Linux)
- Model providers: Amazon
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [aws/amazon-q-developer-cli](../../repos/aws/amazon-q-developer-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AWS's agentic terminal chat for building applications with natural language; succeeded by the closed-source Kiro CLI. README notes it is no longer actively maintained.

(captured site page body (agents/amazon-q-developer-cli.md), not a verified repo-code finding)
Amazon Q Developer CLI brought agentic coding to the terminal for AWS developers: \`q chat\` provided an agentic experience with MCP support, built on a Rust codebase (crates/chat-cli) and authenticated through AWS login. It ran on macOS (brew cask or DMG) and Linux (deb/AppImage), with documentation in AWS's developer guide. The project accumulated roughly 2k stars and 1,100 commits before AWS announced it would receive only critical security fixes, directing users to Kiro CLI — the closed-source successor maintained at kiro.dev/cli, with issues tracked under kirodotdev/Kiro. Existing installs keep working, but feature development now happens in the proprietary successor, making this repo the last open-source artifact of that product line.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/amazon-q-developer-cli.md)
