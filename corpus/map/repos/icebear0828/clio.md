# icebear0828/clio

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e3f5864678d1 @ 8da84aac3b00a168

## Summary (orientation draft, not independently verified)

Clio is a terminal-based Claude Code clone written in TypeScript (~9.2k lines, 46 files) whose only runtime dependency is fast-glob, offering an agentic coding loop with 21 tools, permission modes, MCP support, sessions, and hooks. Evidence is mostly README documentation plus contributor instructions in CLAUDE.md.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Clio is a feature-rich terminal Claude Code clone connecting to the Anthropic API or compatible endpoints, providing an interactive agentic coding assistant with local tool execution. -- evidence: [README.md#L5-L5](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] The tool set includes 21 tools spanning Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch, Agent, task tracking tools, Skill, ToolSearch, team tools, and SendMessage, categorized as safe, write, or dangerous. -- evidence: [README.md#L36-L66](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L36-L66), [README.md#L188-L210](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L188-L210)
  - [inference/documented] The codebase appears organized into core engine modules (agent loop, streaming client, permissions, sandbox, session, settings) and a tools layer including checkpoint, hooks, MCP, LSP, subagent, tasks, teams, and worktree files. -- evidence: [README_zh.md#L313-L367](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README_zh.md#L313-L367), [README.md#L313-L367](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L313-L367)
- design-choices (3 claim(s)):
  - [observation/documented] Settings use a four-level hierarchy (global and project, each with committed and gitignored local files) where arrays concatenate across layers and scalars override. -- evidence: [README.md#L102-L102](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L102-L102), [README.md#L135-L135](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L135-L135), [README.md#L104-L109](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L104-L109)
  - [observation/documented] Hooks run shell commands before or after tool execution; a non-zero pre-hook exit blocks the tool while post-hook failures only log a warning, with CLIO_TOOL_NAME, CLIO_TOOL_INPUT, and CLIO_HOOK_PHASE environment variables. -- evidence: [README.md#L273-L276](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L273-L276), [README.md#L258-L258](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L258-L258)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.md instructs contributors to run npm run dev/build/test (vitest), keep TypeScript strict with no any, use ESM .js import extensions, and add tests per module. -- evidence: [CLAUDE.md#L148-L153](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L148-L153), [CLAUDE.md#L7-L13](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L7-L13), [CLAUDE.md#L138-L141](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L138-L141), [CLAUDE.md#L95-L99](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L95-L99)
  - [observation/documented] Repository development practice: the project is intended for self-modification by Clio (dogfooding), with .clio/settings.json hooks running tsc and test gates after edits and writes, and a 3-strike rollback rule. -- evidence: [CLAUDE.md#L106-L107](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L106-L107), [CLAUDE.md#L117-L120](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L117-L120), [CLAUDE.md#L103-L103](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L103-L103)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes flags including --api-url, --api-key, --api-format (anthropic|openai), --model, --resume, --fork-session, --thinking, --permission-mode, --allow/--deny patterns, --allow-outside-cwd, and --dangerously-skip-permissions. -- evidence: [README.md#L72-L87](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L72-L87)
  - [observation/documented] The REPL provides 17 slash commands such as /commit, /pr, /review, /compact, /context, /cost, /doctor, /init, /model, /sessions, /settings, and /theme. -- evidence: [README.md#L139-L157](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L139-L157), [README.md#L313-L367](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L313-L367)
- memory-state (1 claim(s)):
  - [observation/documented] Conversations auto-save to ~/.clio/sessions/{id}.json after each turn and can be resumed with --resume or forked with --fork-session. -- evidence: [README.md#L305-L305](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L305-L305), [README.md#L298-L298](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L298-L298), [README.md#L308-L309](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L308-L309)
- orchestration (3 claim(s)):
More evidence: [full detail](clio.detail.md)

Metadata and full claim list: [full detail](clio.detail.md)
Human notes ([notes](clio.notes.md), never overwritten by build)

[Back to map index](../../index.md)
