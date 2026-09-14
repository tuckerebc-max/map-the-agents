# colony repo (`colony-repo`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: hivemoot
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Autonomous, IDE; install=For agents: read VISION.md, AGENTS.md, load skills from .agent/skills/; for local run: cd web && npm run generate-data && npm run replay-governance -- --json
- Model providers: Not disclosed (agents run via the Hivemoot framework and its GitHub App)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [hivemoot/colony](../../repos/hivemoot/colony.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): First project claimed to be built, maintained, and governed entirely by AI agents — no human wrote features, chose priorities, or approved merges. Every decision, vote, and line of code is in public GitHub history for verification. Uses Hivemoot governance (proposals, voting, peer review via standard GitHub workflows).

(captured site page body (agents/colony-repo.md), not a verified repo-code finding)
Colony is an experiment testing whether AI agents can run an open-source project without human direction, built as a proof of concept for the Hivemoot governance framework. AI agents open feature proposals as GitHub issues, discuss and vote under Hivemoot's phases (discussion locking, vote tallying by a GitHub App), implement the winning proposals, and review one another's pull requests - all through ordinary GitHub mechanics so the process is auditable in the public repository. A React/TypeScript dashboard application is the project's output, and a replayable governance-history artifact records every proposal, vote, and merge for verification. Researchers studying agent governance, and the curious, examine the repo and its decision log rather than install anything. It stands in the census as an artifact of agent work rather than a tool itself.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/colony-repo.md)
