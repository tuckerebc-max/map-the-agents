# bumpgen (`bumpgen`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: xeol-io
- License: MIT
- Language: TypeScript
- Interface: install=npm install -g bumpgen; also available as a GitHub Action (xeol-io/bumpgen@v0.0.1)
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [xeol-io/bumpgen](../../repos/xeol-io/bumpgen.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI agent that bumps npm dependencies and automatically fixes breaking code changes using AST analysis (ts-morph) and a plan graph DAG (based on Microsoft's codeplan paper) to propagate fixes across the codebase. Roadmap includes Java, Go, C#, Python support.

(captured site page body (agents/bumpgen.md), not a verified repo-code finding)
bumpgen exists because dependency upgrades break code in ways that simple 'bump and pray' tools ignore: the version change succeeds but the build fails, and someone must trace every downstream use of the changed API. The agent builds the project to detect what breaks, uses ts-morph to analyze the AST and pull type definitions for the new package version, and consults an LLM for fixes; its distinctive piece is a plan-graph DAG adapted from Microsoft's CodePlan research, which lets it chain fixes so that a repair's own second-order breakage also gets addressed. Scope is deliberately narrow — npm/TypeScript only, build-error breakage only — and the tool ships both as a CLI and a GitHub Action intended to run on Dependabot or Renovate pull requests, committing fixes to the PR branch. xeol-io, the supply-chain security company behind it, used it to demonstrate AI-assisted upgrades; the repository has not seen commits since 2024 and the roadmap items (more languages, test oracles, GitHub App) were never completed.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/bumpgen.md)
