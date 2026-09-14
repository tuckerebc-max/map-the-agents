# claude-northstar (`claude-northstar`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Nisarg38
- License: MIT
- Language: JavaScript, Node.js
- Interface: platforms=Autonomous, CLI; install=npx claude-northstar init (recommended), or curl -fsSL https://raw.githubusercontent.com/nisarg38/claude-northstar/main/install.sh | bash
- Model providers: Claude Code, OpenCode
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [nisarg38/claude-northstar](../../repos/nisarg38/claude-northstar.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Goal-oriented development framework for CLI agents that shifts them from task-based to vision-based autonomous workflows; main agent acts as 'Tech Lead' coordinating sub-agents (Product Researcher, Strategist, Developer, QA, Reviewer) with persistent state across sessions (north-star.md, project-state.json), strategic-question-only interruptions, and a continuous Analyze -\> Plan -\> Execute -\> Evaluate work loop. Very early stage (5 commits, 1 star).

(captured site page body (agents/claude-northstar.md), not a verified repo-code finding)
The framework targets the failure mode where CLI agents complete individual tasks but lose sight of project intent: instead of issuing tasks, the developer writes a north-star vision document, and the agent plans milestones against it, executing through a develop-QA-review-merge pipeline and asking only strategic questions. State lives in project-state.json and a progress log so sessions resume coherently, and the quality pipeline gates merges behind review. It installs via npx claude-northstar init for Claude Code and OpenCode. The repository is minimal (five commits, a single star), so adoption is essentially nil, but the design documents a vision-driven alternative to task-by-task prompting.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-northstar.md)
