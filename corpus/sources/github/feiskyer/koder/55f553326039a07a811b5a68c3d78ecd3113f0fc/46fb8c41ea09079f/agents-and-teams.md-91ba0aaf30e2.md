# Agents And Teams

Koder can delegate work to local background agents and teams. Use this when a task can be split into focused investigations, reviews, or implementation branches while the main session keeps coordinating.

## Project And User Agents

Agents are loaded from:

1. `.koder/agents/` in the current project
2. `~/.koder/agents/` for user-level agents

Inspect them with:

```bash
/agents
/agents summary
```

Use a specific agent from the CLI:

```bash
koder --agent reviewer "review the current diff"
```

Project agents are useful for repeated roles such as reviewer, test fixer, documentation writer, or release assistant.

## Background Subagents

Use `/fork` for a background subagent:

```bash
/fork "investigate why the import-order test is failing"
/fork --context "review the current diff for docs regressions"
```

Default subagent context is isolated from the main agent. The main session receives the result and can inspect runtime summaries. When you need the subagent to see current conversation context, pass an explicit context-bearing mode or prompt that names the files and facts it needs.

Subagents inherit the active model configuration, including model name, base URL, reasoning effort, and OAuth-style provider routing where supported. That keeps background work on the same provider family as the main session unless you intentionally override it.

An agent definition with `isolation: worktree` in its frontmatter runs in its own git worktree under `.koder/worktrees/`, so its edits cannot collide with your working tree. When the run finishes and the worktree contains no changes, Koder removes it automatically (firing the `WorktreeRemove` hook); a worktree with uncommitted work is kept for you to inspect or merge. See [Hooks](hooks.md) for the `SubagentStart`, `SubagentStop`, `WorktreeCreate`, and `WorktreeRemove` events.

## Task Delegate Tool

During normal model execution, Koder may expose `task_delegate` for bounded background work. Treat it like `/fork`: delegate concrete tasks with clear outputs, keep the main session responsible for integration, and avoid asking a subagent to guess unstated context.

Good prompts:

```text
Inspect docs/configuration.md and report any provider setup gaps. Do not edit files.
```

```text
Update only tests/test_sessions.py to cover resume-by-title ambiguity. Run the focused test and report changed files.
```

## Agent Teams

Use `/peers` for team workflows:

```bash
/peers create migration-review
/peers spawn reviewer "check the docs links"
/peers spawn tester "run focused docs tests"
/peers inbox
/peers history
/peers tasks
```

Teams provide local records for members, mailbox messages, task history, and shared memory. They are useful for multi-agent discussion, coordinator-plus-reviewer workflows, or repeated project teams.

## Teammate Modes

Koder supports two teammate execution modes:

| Mode | Start With | Best For |
|---|---|---|
| `in-process` | `koder --teammate-mode in-process` | Fast local teammate execution inside the Koder process. This is the default for ordinary team work. |
| `tmux` | `koder --teammate-mode tmux` | Visible teammate panes, debugging team UX, or watching separate agents work in real terminal sessions. |

Keep `tmux` for cases where you need terminal-pane visibility. Use the default in-process mode for most user workflows.

## Team Memory

Team memory can be synchronized between project-local files and runtime state:

```bash
/peers memory <team-id> sync
```

Project memory path:

```text
.koder/team-memory/<team-id>/
```

Runtime memory path:

```text
~/.koder/teams/<team-id>/memory/
```

Use team memory for decisions, shared constraints, investigation findings, or handoff notes that several teammates should see.

## Inspect And Clean Up

Useful commands:

```bash
/agents summary
/tasks
/peers history
/peers inbox
/peers kill <member-id>
```

Persistent runtime state normally lives under `~/.koder/agents/`, `~/.koder/teams/`, and `~/.koder/tasks/`. Tests and temporary harnesses should use temporary directories instead of writing product state into the repository root.
