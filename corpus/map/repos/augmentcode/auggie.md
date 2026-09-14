# augmentcode/auggie

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9cc3ead419db @ ba3e31b0ac8fb359

## Summary (orientation draft, not independently verified)

Auggie is Augment's agentic coding CLI distributed on npm for Node.js 22+, with a terminal TUI, headless/print mode, MCP and ACP modes, a daemon component, cloud subcommands, sub-agents, skills, and a runtime tool-permission model. Claims below rest only on the supplied README and CHANGELOG slices. Evidence coverage: 108 of 136 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A daemon component validates the host's Git version at startup, can be configured with a custom worktree directory, and can auto-discover git workspaces under a non-git container. -- evidence: [CHANGELOG.md#L107-L114](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L107-L114), [CHANGELOG.md#L91-L91](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L91-L91), [CHANGELOG.md#L6-L14](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L6-L14)
- design-choices (1 claim(s)):
  - [observation/documented] Plan mode saves plans to ~/.augment/plans/ and enforces strict read-only access; tool permissions default to denylist mode to prevent accidental lockout from all tools. -- evidence: [CHANGELOG.md#L369-L378](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L369-L378), [CHANGELOG.md#L342-L351](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L342-L351)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The CLI loads specialized domain knowledge from SKILL.md files following the agentskills.io specification, and a /skills command shows loaded skills with approximate token usage. -- evidence: [CHANGELOG.md#L482-L484](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L482-L484)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI supports a login command, running with an optional initial prompt, a --print mode that runs once and writes to stdout (suited to CI), and --quiet to return only final output. -- evidence: [README.md#L22-L24](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L22-L24), [README.md#L28-L31](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L28-L31), [README.md#L33-L34](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L33-L34)
  - [observation/documented] Reusable prompts stored as markdown files with frontmatter under .augment/commands/ become slash commands such as /code-review. -- evidence: [README.md#L38-L38](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L38-L38), [README.md#L42-L51](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L42-L51)
- memory-state (1 claim(s)):
  - [observation/documented] Agent progress is saved incrementally after each LLM exchange to prevent loss on crashes, and queued messages persist in the session file across CLI restarts. -- evidence: [CHANGELOG.md#L395-L404](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L395-L404)
- orchestration (1 claim(s)):
  - [observation/documented] The agent supports built-in sub-agents including explore, auggie-guide, and a general-purpose sub-agent, and the agent loop executes independent tools in parallel. -- evidence: [CHANGELOG.md#L148-L148](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L148-L148), [CHANGELOG.md#L22-L26](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L22-L26), [CHANGELOG.md#L127-L129](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L127-L129), [CHANGELOG.md#L342-L351](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L342-L351)
- tools-permissions (1 claim(s)):
  - [observation/documented] Saving files to sensitive paths requires approval, and denying a tool permission request provides clearer feedback, indicating a runtime permission model over tool use. -- evidence: [CHANGELOG.md#L297-L301](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L297-L301), [CHANGELOG.md#L36-L38](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L36-L38)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The package is published as @augmentcode/auggie on npm and requires Node.js 22 or later. -- evidence: [README.md#L3-L3](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L3-L3), [README.md#L16-L18](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L16-L18), [README.md#L14-L14](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L14-L14)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](auggie.detail.md)

Metadata and full claim list: [full detail](auggie.detail.md)
Human notes ([notes](auggie.notes.md), never overwritten by build)

[Back to map index](../../index.md)
