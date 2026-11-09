# Koder Command Reference

Generated: `2026-07-03T14:45:29+00:00`

This reference lists the live Koder slash-command registry with usage examples and concise descriptions. For task-oriented guidance, start with the topic guides in [Feature Guide](features.md).

## Summary

- Runtime slash commands: `79`
- Common workflow rows: `25`
- Missing runtime command entries: `0`

## Slash Commands

| Command | Usage Example | Typical Use | Steps | Description |
|---|---|---|---|---|
| `/add-dir` | `/add-dir /tmp` | Validate workspace directory admission, permissions visibility, non-directory guidance, and missing-path errors. | `4` | Add a workspace directory to the active session |
| `/advisor` | `/advisor focus on tmux validation` | Run an advisor review over the session transcript and git diff, with an optional focus argument and a short circuit when there is no context. | `8` | Run an advisor review over session and git context |
| `/agents` | `/agents` | List project agents, report malformed files, create and inspect a project agent, verify runtime summary output, and delete the agent. | `9` | List, inspect, create, and manage local agents |
| `/assistant` | `/assistant` | Inspect active assistant status, list agent-backed profiles, show project profile metadata, and handle usage/not-found edges. | `5` | Inspect active Koder assistant profiles |
| `/autofix-pr` | `/autofix-pr` | Validate autofix command usage and gh-backed PR diff handling without mutating a PR or workspace files. | `7` | Inspect a PR diff size and get fix-request guidance |
| `/backfill-sessions` | `/backfill-sessions` | Migrate legacy ctx sessions, list migrated metadata, and prove the command is idempotent. | `5` | Backfill legacy session metadata |
| `/branch` | `/branch` | Inspect dirty git branch state, reject invalid names, and create a new branch from the TUI. | `5` | Inspect or create working branches |
| `/brief` | `/brief` | Toggle brief-only mode on and off while proving config.yaml persistence. | `5` | Toggle brief-only assistant responses |
| `/bughunter` | `/bughunter division regression` | Run local bug-triage diagnostics over workspace status, diff stat, diff evidence, and clean-repo state. | `5` | Run local bug-triage diagnostics |
| `/btw` | `/btw` | Ask a quick side question that uses recent session context without mutating conversation history. | `6` | Ask a quick side question using session context |
| `/buddy` | `/buddy status` | Inspect, hatch, pet, and mute or unmute the local buddy companion. | `10` | Manage the local buddy companion state |
| `/channels` | `/channels` | Launch Koder with server, plugin, and development channel entries, then verify /channels state and CLI UX. | `4` | Inspect configured MCP/plugin channels |
| `/clear` | `/clear` | Clear current workflow state, reset prompt history, switch to a fresh session, and keep the previous named session resumable. | `10` | Clear current workflow state |
| `/color` | `/color` | Set, display, persist, reject invalid, and reset the active session color. | `7` | Set the current session color |
| `/commit` | `/commit` | Inspect commit readiness across staged, unstaged, untracked, and clean git states without creating a commit through Koder itself. | `5` | Inspect git commit readiness |
| `/commit-push-pr` | `/commit-push-pr` | Inspect branch, remote, status, staged diff, unstaged diff, and clean readiness without pushing or opening a PR. | `4` | Inspect branch, diff, and PR publish readiness |
| `/compact` | `/compact unexpected` | Seed session history, run manual compaction, prove persisted compacted transcript shape, and keep the TUI usable. | `5` | Compact the active conversation state |
| `/config` | `/config` | Inspect runtime configuration after live model and reasoning-effort changes, including persisted YAML state. | `7` | Inspect and update runtime configuration |
| `/context` | `/context` | Render context-token categories for instructions, conversation, and files; cross-check details with /ctx_viz. | `4` | Inspect injected context |
| `/cost` | `/cost` | Display zero, known-model, and unknown-model session cost data from durable usage snapshots. | `6` | Show usage cost information |
| `/ctx_viz` | `/ctx_viz` | Render project context, exact session message counts, seeded session files, recent transcript lines, and /context cross-checks. | `4` | Render loaded context and recent transcript details |
| `/diff` | `/diff` | Report git diff state and seeded conversation edit summaries in one TUI flow, including a clean-git edge. | `5` | Show pending diffs |
| `/debug-tool-call` | `/debug-tool-call` | Inspect empty and seeded tool-call debug records with redacted argument and output previews plus invalid selection handling. | `8` | Inspect recorded tool-call context |
| `/doctor` | `/doctor` | Run local environment diagnostics, assert healthy runtime fields, and cross-check the same TUI session with shell, version, and status output. | `4` | Run environment diagnostics |
| `/effort` | `/effort` | Inspect, set, persist, inherit, reject invalid, and reset reasoning effort through the TUI. | `7` | Show or change reasoning effort |
| `/reasoning` | `/reasoning` | Inspect, set, persist, reject invalid, and disable reasoning display through the TUI. | `8` | Show or change reasoning display |
| `/env` | `/env` | Inspect, persist, unset, reject invalid, and clear session-scoped environment variables through the TUI. | `7` | Inspect selected environment state |
| `/exit` | `/exit` | Exit the interactive session and prove the tmux-backed TUI process terminates cleanly. | `3` | Exit the active workflow |
| `/export` | `/export` | Export seeded session metadata and transcript content to screen, JSON, and Markdown while handling invalid paths. | `9` | Export session artifacts |
| `/feedback` | `/feedback` | Capture a redacted feedback event with repository context and durable local storage. | `3` | Capture feedback with repository context |
| `/files` | `/files` | Report seeded session context files with exact relative paths, de-duplication, and exists/missing status. | `6` | Inspect workspace files |
| `/fork` | `/fork` | Launch background subagents with usage guidance, isolated default context, explicit fork context, inherited model/base URL/reasoning config, and redacted runtime records. | `4` | Launch or resume a background subagent |
| `/goal` | `/goal` | Inspect and manage a durable session goal without invoking a provider-backed turn. | `8` | Set or view the goal for a long-running task |
| `/help` | `/help` | Display the full command catalog with real descriptions, command-specific help, and unknown-command guidance. | `5` | Show help for commands |
| `/hooks` | `/hooks` | List project-configured hook events, matchers, and commands from the real TUI. | `2` | List configured runtime hooks |
| `/init` | `/init` | Generate a local AGENTS.md guide when missing, report Magic Docs, and refuse overwriting existing files. | `6` | Generate an AGENTS.md project guide |
| `/init-verifiers` | `/init-verifiers cli` | Create a project verifier skill, inspect its generated SKILL.md contract, prove /skills discovers it, and rerun the idempotent exists path. | `5` | Create project verifier skills |
| `/insights` | `/insights` | Display current session analytics for transcript items, role counts, tool activity, context files, and usage counters. | `4` | Show current session analytics |
| `/issue` | `/issue` | List GitHub issues via the gh CLI, show creation guidance, and report empty and failure states accurately. | `7` | Inspect internal issue metadata |
| `/keybindings` | `/keybindings` | List, persist, reject invalid, and re-read interactive keybindings through the TUI. | `5` | Inspect and update interactive keybindings |
| `/magic-docs` | `/magic-docs` | List Magic Docs, refresh the managed section, verify file content, remove the header, and prove the tracked record is cleaned up. | `8` | Inspect or refresh tracked Magic Docs |
| `/mcp` | `/mcp` | Round-trip project MCP configuration through the CLI, TUI listing, diagnostics, and cleanup. | `8` | Inspect MCP integration settings |
| `/memory` | `/memory` | Inspect empty, seeded project/user, index-ignored, and /remember-created memory files through the real TUI. | `5` | Inspect stored runtime memories |
| `/model` | `/model` | Change the active model/provider, prove status and subagent inheritance use it, then reset to the default OpenAI model. | `6` | Show or change the active model |
| `/oauth-refresh` | `/oauth-refresh` | Inspect local OAuth token-store diagnostics for empty, valid, expired, malformed, and usage states without network refresh. | `4` | Inspect OAuth token expiry and refresh guidance |
| `/onboarding` | `/onboarding` | Validate onboarding checklist against real API-key, model, and workspace state transitions. | `8` | Show local setup checklist status |
| `/output-style` | `/output-style` | Inspect, update, and reset terminal output style controls across theme, color, vim, statusline, and persisted settings. | `8` | Inspect and update terminal output styling |
| `/peers` | `/peers create peers-scenario` | Create and inspect an agent team, consume mailbox work, record history, and complete a persisted team task. | `11` | Create and manage local agent teams |
| `/permissions` | `/permissions` | Inspect permission status and verify permission-engine decisions across default and enabled sandbox policy. | `5` | Inspect runtime permission behavior |
| `/plan` | `/plan` | Enter and exit plan mode while proving read-only permission enforcement through the TUI. | `6` | Enter read-only plan mode |
| `/plugin` | `/plugin` | List installed plugins, toggle a plugin off and on, and persist the enabled state. | `6` | Inspect and manage installed plugins |
| `/pr-comments` | `/pr-comments` | Fetch and render PR comments via the gh CLI, including threaded review comments and failure states. | `8` | Render GitHub PR comments for the current branch |
| `/pr_comments` | `/pr_comments` | Underscore alias for /pr-comments; both names share the same gh-backed renderer. | `4` | Render GitHub PR comments for the current branch |
| `/release-notes` | `/release-notes` | Seed cached changelog state before launch, render filtered release notes, persist last-seen version, and cross-check runtime version. | `3` | Show recent Koder release notes or commits |
| `/reload-plugins` | `/reload-plugins` | Reload plugin registry after adding and removing a plugin during the TUI session, proving plugin and skill visibility update. | `9` | Reload installed plugins |
| `/rename` | `/rename` | Rename the active session, verify visible session metadata, and assert SQLite persistence. | `3` | Rename the active session |
| `/resume` | `/resume missing-session` | Resume existing sessions by exact title and id while rejecting missing and ambiguous targets. | `7` | Resume a previous session |
| `/review` | `/review` | Review local and PR diffs, including clean-worktree and gh-failure states. | `8` | Start a review-oriented workflow |
| `/rewind` | `/rewind` | Seed conversation history, list rewind targets, restore a selected prompt into input, and prove session history is trimmed. | `9` | Rewind recent workflow state |
| `/sandbox` | `/sandbox` | Inspect and configure sandbox settings through one /sandbox command. | `5` | Inspect and configure sandbox settings |
| `/schedule` | `/schedule extra` | Inspect the scheduled task registry from real cron storage, including empty, created, deleted, and malformed states. | `8` | Inspect scheduled task registry |
| `/loop` | `/loop` | Create, inspect, and delete scheduled loop jobs through the real slash command backed by cron storage. | `7` | Create, list, and delete scheduled loop jobs |
| `/security-review` | `/security-review` | Run a security review over pending git changes; clean worktrees short-circuit without a model call. | `5` | Run a security-focused review of pending changes |
| `/session` | `/session` | Inspect active session identifiers and metadata before and after a title rename. | `3` | Inspect the current session |
| `/skills` | `/skills` | List project, user, and plugin skills with precedence, then verify plugin disable/reload hides and restores plugin skills. | `9` | Inspect available skills |
| `/status` | `/status` | Show live runtime status for version, effective model, provider, session id, command count, connectivity, and cwd after model changes. | `5` | Show runtime status |
| `/statusline` | `/statusline` | Import a shell prompt into statusline settings, verify output-style resolution, clear it, and assert persisted settings are clean. | `5` | Configure or clear the terminal status line |
| `/subscribe-pr` | `/subscribe-pr` | List open pull requests via the gh CLI and report subscription guidance, empty state, and failure state. | `6` | Inspect open PRs and subscription guidance |
| `/summary` | `/summary` | Summarize the current session title, usage counters, git diff stat, and recent commits from local state. | `2` | Emit internal program summary data |
| `/tasks` | `/tasks` | Inspect runtime task tracker empty state, persisted AutoDream task rows, and malformed task diagnostics. | `3` | Inspect active runtime tasks |
| `/theme` | `/theme` | Set, persist, inspect, reject invalid, and reset terminal theme value. | `6` | Change terminal theme settings |
| `/thinkback` | `/thinkback nope` | Review local session counts, title, and recent prompts without model execution. | `4` | Review recent local session context |
| `/thinkback-play` | `/thinkback-play` | Replay recent local session turns with empty-state, invalid-limit, ordering, and limit handling. | `4` | Replay recent local session turns |
| `/torch` | `/torch` | Generate a provider-backed exploration plan for a codebase topic. | `5` | Explore a codebase topic with a structured plan |
| `/ultraplan` | `/ultraplan` | Generate a provider-backed implementation plan without mutating the workspace. | `6` | Create a comprehensive implementation plan |
| `/usage` | `/usage` | Show persisted session token, context, and cost totals and reset them across a new session. | `6` | Show session usage totals |
| `/version` | `/version` | Render detailed runtime version information and compare it with status and CLI version output. | `3` | Show detailed runtime version info |
| `/vim` | `/vim on` | Toggle vim input mode, prove persistence, reject invalid input, and reset state. | `5` | Toggle vim input mode |
| `/voice` | `/voice status` | Configure the voice provider, enable and disable provider-backed voice mode, handle unsupported providers, and persist configuration without leaking secrets. | `8` | Configure or toggle provider-backed voice mode |

## Common Interactive Workflows

| Suite | Scenario | Primary Commands | Purpose | Turns |
|---|---|---|---|---|
| agents | project-agent-detail | /agents | Load project agent metadata, report malformed agent files, create and inspect a project agent, delete it, and assert the backing file is removed. | `8` |
| agents | background-fork | /fork, /agents | Launch background subagents with isolated default context, explicit fork context, inherited model/base URL/reasoning config, and redacted persisted runtime records. | `3` |
| teams | mailbox-and-task | /peers | Create a team, route a mailbox message, consume it, handle an empty inbox edge, and complete a persisted team task across turns. | `10` |
| teams | team-memory | /peers | Create a team, write project-local team memory, sync it into runtime memory, and verify a tmux teammate can read the synced content. | `5` |
| teams | tmux-pane | /peers | Spawn two tmux-backed teammate panes, preserve completed pane output, verify inherited model config, inspect member state, kill one pane, and verify the missing-pane UX. | `6` |
| teams | tmux-discussion | /peers | Spawn multiple tmux-backed teammates that send attributed proposals to the lead and verify the discussion history through the CLI and persisted team store. | `6` |
| teams | in-process-discussion | /peers, /agents | Spawn multiple in-process teammates, route mailbox work to them, collect attributed proposals and a coordinator summary, and verify persisted discussion history. | `15` |
| skills | project-and-plugin-skill-listing | /skills, /demo-plugin:plugin-skill, /plugin, /reload-plugins | Verify project and plugin skills are listed with namespaces, plugin skills execute locally, disabling hides and blocks them, and re-enabling restores them. | `9` |
| skills | manual-skill-command | /demo-skill, /skills | Invoke a project manual-only skill and prove it renders local content without model execution. | `2` |
| features | auto-dream-task | /tasks | Run an AutoDream consolidation, verify task and memory persistence, update task metadata, and report malformed task records through /tasks. | `4` |
| features | settings-bundle | /config | Export and import local settings bundles, covering dry-run behavior, project scope filtering, token/cache exclusion, restore, and backup UX. | `5` |
| features | slash-completion | shell mode | Filter slash completions in the real prompt, survive a small terminal resize without layout errors, and execute the selected completion. | `3` |
| features | memory-and-session | /memory, /remember, /rename, /session, /clear, /resume | Save project memory, verify memory listing, rename the active session, switch away, resume by title, and confirm durable session metadata. | `9` |
| features | prompt-suggestion | /clear | Generate a post-turn ghost suggestion, accept it into the prompt, clear it, and verify stale suggestions do not survive a session clear. | `7` |
| features | permissions-and-sandbox | /permissions, /sandbox | Exercise sandbox policy changes and permission-engine decisions for approval-required, sandboxed, and excluded shell tool calls. | `8` |
| features | sandbox-backends | /sandbox | List user-facing sandbox backend choices and show actionable availability reasons through the TUI. | `2` |
| features | sandbox-unix-local-shell | /sandbox | Prove foreground shell execution uses the Unix local sandbox and blocks an outside-workspace write. | `2` |
| features | sandbox-unavailable-backend | /permissions | Prove sandbox mode denies shell execution when the configured backend is unavailable. | `2` |
| features | sandbox-exclusions | /sandbox, /permissions | Prove excluded command behavior remains explicit under sandbox policy. | `4` |
| features | sandbox-protected-paths | /sandbox | Prove protected metadata path writes are blocked before sandbox execution mutates the path. | `2` |
| features | sandbox-network-policy | /sandbox | Show network policy state and the current enforcement status for the selected backend. | `3` |
| features | sandbox-hosted-backend-status | /sandbox | Show hosted sandbox providers as unconfigured without leaking credential values. | `2` |
| features | fixed-bottom-queued-input | shell mode | Validate that interactive streaming keeps output above a fixed bottom input/status area, accepts mid-stream input, displays queued rows, and injects queued prompts into the next tool result. | `5` |
| features | fixed-bottom-idle-tip | shell mode | Validate that a short response leaves the tip, input frame, and status line together at the bottom of the visible terminal. | `2` |
| features | terminal-resize-reflow | / | Resize after Rich command output and while editing prompt input, verifying visible transcript reflow without layout errors. | `5` |

## Maintainer Verification

Regenerate and verify this reference with:

```bash
uv run scripts/tmux_feature_scenarios.py --check
uv run scripts/tmux_feature_scenarios.py --check --strict-acceptance
```
