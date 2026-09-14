# oh-my-claudecode v5.4.0: respect CLAUDE_CODE_OAUTH_TOKEN when, add agent-doc-discipline skill, pre-flight danger scan

## Release Notes

Release with **5 new features**, **10 bug fixes** across **16 merged PRs**.

### Highlights

- **feat(hud): respect CLAUDE_CODE_OAUTH_TOKEN when reading usage** (#4004)
- **feat(shipyard): add agent-doc-discipline skill and two-axis review gate** (#4003)
- **feat(lookout): pre-flight danger scan for autonomous runs (advisory)** (#3994)
- **feat(skills): add harbor — shipyard intake gate for external issues and PRs (opt-in)** (#3982)
- **feat(hooks): make the SessionStart context budget configurable via OMC_SESSION_START_CONTEXT_BUDGET** (#3981)

### New Features

- **feat(hud): respect CLAUDE_CODE_OAUTH_TOKEN when reading usage** (#4004)
- **feat(shipyard): add agent-doc-discipline skill and two-axis review gate** (#4003)
- **feat(lookout): pre-flight danger scan for autonomous runs (advisory)** (#3994)
- **feat(skills): add harbor — shipyard intake gate for external issues and PRs (opt-in)** (#3982)
- **feat(hooks): make the SessionStart context budget configurable via OMC_SESSION_START_CONTEXT_BUDGET** (#3981)

### Bug Fixes

- **fix: remove false Ralph Ruby prerequisite and bad plan citation** (#4000)
- **fix(team): preserve reap ownership during leader cleanup** (#3997)
- **fix(hud): exclude release dates from model versions** (#3999)
- **fix(team): validate effective providers and harden launch gate ownership** (#3993)
- **fix(worktree-paths): treat a bare repository as a work-tree-less repo, not a failed probe** (#3991)
- **fix(release): cover version-coupled surfaces in the release runbook** (#3989)
- **fix(inventory): re-anchor inventory-graph provenance to the current dev head** (#3987)
- **fix(setup): continue with canonical plugin root when launcher path is a compat symlink** (#3986)
- **fix(worktree-paths): force LC_ALL=C on git probe spawns** (#3979)
- **fix(team): bound Cursor/Codex startup grace and verify provider cleanup** (#3983)

### Documentation

- **docs: replace retired mode guidance with the shipped 5.3.0 surface** (#3985)

### Stats

- **16 PRs merged** | **5 new features** | **10 bug fixes** | **0 security/hardening improvements** | **0 other changes**
