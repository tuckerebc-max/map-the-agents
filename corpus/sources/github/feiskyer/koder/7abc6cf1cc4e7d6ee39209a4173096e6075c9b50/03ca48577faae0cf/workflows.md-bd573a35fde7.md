# Workflows

Koder includes workflow commands for common engineering tasks. These commands are meant to keep the model grounded in the current repository state and make the next action explicit.

## Review Workflows

Use review commands before committing or opening a PR:

```bash
/diff
/review
/security-review
/pr-comments
```

`/diff` summarizes pending git and conversation edits. `/review` focuses on local or PR diffs. `/security-review` focuses on security-sensitive risks. `/pr-comments` renders GitHub PR comments for the current branch through `gh` when available.

Good prompts after a review command:

```text
Fix the high-severity issues first and run the focused tests.
```

```text
Do not edit yet. Explain which review findings are real and which are false positives.
```

## Planning And Advice

Use planning commands when you want structure before implementation:

```bash
/advisor local fixture
/brief
/torch
/ultraplan
```

`/advisor` reviews session and git context with an advisor model route. `/brief` toggles concise responses. `/torch` explores a codebase topic with a structured plan. `/ultraplan` creates a deeper implementation plan without mutating the workspace.

Use `/goal` for long-running implementation objectives that should keep status, token budget, and continuation state across turns.

## Git Readiness

Use these commands around commits and branches:

```bash
/branch
/commit
/commit-push-pr
/release-notes
```

`/commit` inspects staged, unstaged, and untracked state. `/commit-push-pr` checks branch, remote, diff, and PR readiness without silently publishing changes.

## Issue And PR Helpers

Useful commands:

```bash
/issue
/subscribe-pr
/autofix-pr
/pr-comments
/pr_comments
```

These commands inspect GitHub state through local CLI integrations. They should report missing auth, missing repository context, and empty-state cases rather than pretending remote state is available.

## Verification

For normal code changes in this repository, the project instructions require:

```bash
uv run black . && uv run ruff format && uv run ruff check --fix
uv run pytest
```

For focused work, run the narrowest meaningful test first, then broaden when the affected surface is shared.

Use `/status` and `/summary` to see what the active session believes about the branch before you claim work is done.

## Useful Workflow Combos

Small bug fix:

```bash
/diff
/review
!uv run pytest tests/test_target.py
/commit
```

Security-sensitive change:

```bash
/security-review
/permissions
!uv run pytest tests/security
```

Large refactor:

```bash
/ultraplan
/fork "inspect the test impact of this refactor"
/diff
/review
```
