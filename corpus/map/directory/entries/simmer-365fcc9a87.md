# Simmer (`simmer`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: MIT
- Language: unknown
- Interface: platforms=IDE; install=/plugin marketplace add 2389-research/claude-plugins, then /plugin install simmer@2389-research
- Model providers: Claude (via Claude Code)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Claude Code plugin) (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (judge board of multiple agents) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/simmer](../../repos/2389-research/simmer.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Iterative artifact refinement for Claude Code where a judge board constructs problem-specific judges that read the code, understand the problem, and propose one high-leverage fix per round (ASI), with best-so-far always preserved. Works on any artifact — documents, prompts, pipelines, configs, workspaces.

(captured site page body (agents/simmer.md), not a verified repo-code finding)
Simmer is a Claude Code plugin for iterative artifact refinement, and the agent loop stays with Claude Code. Its mechanism is a judge board that constructs problem-specific judges: each judge reads the code, understands the problem at hand, and proposes exactly one high-leverage fix per round — the Asymmetric Single Improvement (ASI) step — with the best-so-far artifact always preserved so rounds can only improve, never regress. The refinement target is not limited to code; it works on documents, prompts, pipelines, configs, and whole workspaces. Sibling plugins in the same family, like cookoff and omakase-off, take related approaches. The audience is Claude Code users who want a structured, non-destructive improvement loop for any artifact they care about.
Sources: [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/simmer.md)
