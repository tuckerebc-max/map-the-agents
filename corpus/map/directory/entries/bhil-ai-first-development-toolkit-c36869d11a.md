# BHIL-AI-First-Development-Toolkit (`bhil-ai-first-development-toolkit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: PolymathWizard
- License: MIT
- Language: Markdown, Bash
- Interface: install=git clone; chmod +x tools/scripts/*.sh; ./tools/scripts/init.sh; then run claude
- Model providers: Claude Code
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: yes (.claude/hooks shipped in-repo for Claude Code sessions) (yes)
  - plan_mode: unknown (unknown)

Repository map entry: [polymathwizard/bhil-ai-first-development-toolkit](../../repos/polymathwizard/bhil-ai-first-development-toolkit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Production-grade methodology repository for building AI-native applications using iterative sprints where AI coding agents are primary implementors; provides traceable artifact chain (PRD -\> SPEC -\> ADR -\> TASK -\> CODE -\> REVIEW -\> DEPLOY); optimized for Claude Code with custom subagents in .claude/agents/

(captured site page body (agents/bhil-ai-first-development-toolkit.md), not a verified repo-code finding)
The BHIL toolkit's central claim is that the bottleneck in AI-assisted development is specification quality, not code generation, so it packages a complete methodology for spec-driven sprints where AI agents implement and humans architect and review. Every sprint produces artifacts in a chain from PRD through SPEC, ADR, TASK, CODE, REVIEW, and DEPLOY, linked by asymmetric traceability IDs in YAML frontmatter (PRD-NNN, SPEC-NNN, ADR-NNN, and so on) so any artifact traces back to its parent requirement. AI-native ADR extensions cover model selection benchmarks, prompt strategy versioning with eval thresholds, and orchestration patterns such as orchestrator-worker and swarm. The repository ships guides, templates, a worked end-to-end example, shell scripts for artifact validation, and a .claude directory with hooks, rules, and skills that wire the methodology into Claude Code. It targets solo practitioners building LLM-powered applications with Claude Code as the primary implementor.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bhil-ai-first-development-toolkit.md)
