# nisarg38/claude-northstar

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 43d89d5aba90 @ 4cc9aa49933b76d8

## Summary (orientation draft, not independently verified)

Claude North Star is an npm-distributed goal-oriented framework for CLI agents like Claude Code and OpenCode, installing a .claude/harness state directory and instructing the agent session to act as a Tech Lead coordinating five sub-agent roles through an autonomous analyze-plan-execute-evaluate loop.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Installation creates a .claude/harness directory containing north-star.md, project-state.json, decisions.md, progress-log.md, and five sub-agent prompt templates under prompts/. -- evidence: [README.md#L106-L118](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L106-L118)
- design-choices (4 claim(s)):
  - [observation/documented] The framework positions the CLI agent session as a Tech Lead that understands the vision, plans milestones, coordinates sub-agents, and asks only strategic questions. -- evidence: [README.md#L74-L79](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L74-L79)
  - [observation/documented] The autonomous work loop is documented as a repeating cycle of ANALYZE state, PLAN next work, EXECUTE, and EVALUATE progress. -- evidence: [README.md#L93-L100](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L93-L100)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the installed CLAUDE.md instructs the agent to always read north-star.md, project-state.json, and decisions.md at session start, then either capture a new vision or report state and work autonomously. -- evidence: [CLAUDE.md#L29-L33](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L29-L33), [CLAUDE.md#L22-L27](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L22-L27), [CLAUDE.md#L13-L13](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L13-L13), [CLAUDE.md#L15-L20](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L15-L20)
  - [observation/documented] Repository development practice: sub-agents are spawned via the Task tool with subagent_type 'general-purpose', using prompt files from .claude/harness/prompts/ with injected context. -- evidence: [CLAUDE.md#L49-L55](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L49-L55), [CLAUDE.md#L57-L60](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L57-L60), [CLAUDE.md#L47-L47](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/CLAUDE.md#L47-L47)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The tool is distributed as the npm package claude-northstar and operated via npx commands: init, status, and uninstall. -- evidence: [README.md#L32-L34](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L32-L34), [README.md#L43-L44](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L43-L44), [README.md#L40-L40](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L40-L40), [README.md#L5-L6](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L5-L6)
  - [observation/documented] An alternative install path fetches an install.sh script from the GitHub repository via curl and pipes it to bash. -- evidence: [README.md#L48-L50](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L48-L50)
- memory-state (1 claim(s)):
  - [observation/documented] project-state.json persists milestones with status and progress values, the current focus, and identified gaps, enabling sessions to resume when the user says 'continue'. -- evidence: [README.md#L157-L164](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L157-L164), [README.md#L144-L153](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L144-L153), [README.md#L142-L142](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L142-L142), [README.md#L68-L68](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L68-L68)
- orchestration (1 claim(s)):
  - [observation/documented] Work is delegated to five sub-agent roles: Product Researcher, Strategist, Developer, QA, and Reviewer, each used at a specific phase such as planning, implementation, or pre-merge review. -- evidence: [README.md#L83-L89](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L83-L89)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Jujutsu (jj) is an optional companion tool: North Star works with plain git, while jj enables isolated workspaces for parallel tasks, conflicts-as-data, and rollback via an operation log. -- evidence: [README.md#L193-L196](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L193-L196), [README.md#L183-L183](https://github.com/Nisarg38/claude-northstar/blob/43d89d5aba907457fbbaa6179fc74e4ea6fab3d1/README.md#L183-L183)
More evidence: [full detail](claude-northstar.detail.md)

Metadata and full claim list: [full detail](claude-northstar.detail.md)
Human notes ([notes](claude-northstar.notes.md), never overwritten by build)

[Back to map index](../../index.md)
