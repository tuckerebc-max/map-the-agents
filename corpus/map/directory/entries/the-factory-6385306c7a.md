# The Factory (`the-factory`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: akashgit
- License: MIT
- Language: Python
- Interface: platforms=Autonomous; install=uv tool install git+https://github.com/akashgit/remote-factory.git
- Model providers: Claude Code, OpenAI Codex, Bob Shell (IBM)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [akashgit/remote-factory](../../repos/akashgit/remote-factory.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Domain-agnostic multi-agent software design and evolution harness; describes workflows as Pydantic DAG graphs; executes in 3 modes (Headless Executor, Interactive CEO orchestrating specialist subagents, Outer Loop evolving workflow topologies via MAP-Elites); self-evolving via ACE (Autonomous Context Engineering); distributed as a Claude Code plugin

(captured site page body (agents/the-factory.md), not a verified repo-code finding)
The Factory (repo: remote-factory) treats software design itself as something agents can improve: it expresses development workflows as Pydantic DAG graphs whose nodes are agents, functions, gates, forks, and joins, then executes those graphs in two ways — a headless executor that walks the graph deterministically, or an interactive 'CEO' agent that follows SKILL.md playbooks while directing eight specialist subprocesses (Researcher, Strategist, Builder, Health Checker, Code Reviewer, Adversarial Tester, Archivist, Failure Analyst). The distinguishing layer is its Outer Loop: MAP-Elites-style evolution mutates the workflow DAGs themselves — nodes, edges, prompts — and evaluates candidates against benchmarks such as SWE-bench, TerminalBench, and its own FeatureBench, selecting workflows by measured test pass rates; a meta mode applies the same improvement loop to the factory's own codebase via ACE (Autonomous Context Engineering). Distribution is as a Claude Code plugin (uv tool install plus /plugin install) or via uv CLI with a Codex runner option. Researchers and practitioners experimenting with self-improving agent pipelines are the target audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/the-factory.md)
