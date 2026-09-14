# Autospec (`autospec`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: zachblume
- License: MIT
- Language: TypeScript
- Interface: platforms=Autonomous, Web; install=npx autospecai
- Model providers: Anthropic, OpenAI, Google Gemini
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [zachblume/autospec](../../repos/zachblume/autospec.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI agent that autonomously explores a web app URL, generates commonsense e2e test specifications, executes them, and saves passing tests as reusable Playwright .spec.js files

(captured site page body (agents/autospec.md), not a verified repo-code finding)
autospec addresses the bootstrap problem in end-to-end testing: writing the first meaningful Playwright specs for a web app is tedious, so the agent does it. Given just a URL, it crawls up to three pages, generates commonsense test specifications via an LLM, executes them in parallel with semantic browser actions (click by role, fill by label), and judges correctness from accessibility snapshots rather than rigid prior-state comparison. Passing tests are saved as standard Playwright .spec.js files in a trajectories/ folder, ready to run with npx playwright test and extend manually. Model choice (Claude, GPT, Gemini) is pluggable via the Vercel AI SDK, and no configuration beyond a URL and API key is required. QA engineers and developers use it to bootstrap e2e coverage quickly before refining specs by hand.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/autospec.md)
