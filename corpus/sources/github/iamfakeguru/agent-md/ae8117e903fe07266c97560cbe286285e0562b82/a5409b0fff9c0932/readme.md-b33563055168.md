# agent-md

Portable contracts for coding agents.

`agent-md` installs one source-of-truth rules file, repo-local hooks,
persistent task state, and a few helper scripts so agents can stop
guessing and start proving their work.

Honest scope:

- Markdown rules are advisory. The agent has to read and follow them.
- Hooks and git hooks are enforceable where the host agent supports them.
- Tests, type-checks, screenshots, and evidence notes are stronger than
  model self-assessment.

## Quickstart

```bash
# From inside your project directory
curl -sL https://raw.githubusercontent.com/iamfakeguru/agent-md/main/install.sh | bash
```

Installs support for Claude Code, Codex, Cursor, and Windsurf by default.

## What You Get

```text
your-project/
  AGENT.md                         # source of truth
  AGENTS.md                        # Codex / Cursor / Windsurf
  CLAUDE.md                        # Claude Code
  agent-md.toml.example            # deterministic verification config

  .claude/
    settings.json
    hooks/                         # Claude Code enforcement

  .codex/
    hooks.json
    hooks/                         # Codex hook wrappers

  .agents/skills/                  # native Codex skills
    agent-md-verify/
    visual-evidence/

  .cursor/rules/agent-md.mdc       # Cursor project rule
  .windsurf/rules/agent-md.md      # Windsurf workspace rule

  .agent-md/
    bin/
      discover_helpers.sh
      doctor.sh
      playwright-capture.sh

  memory/
    agents.md
    plan.md
    progress.md
    verify.md
    gotchas.md

  .githooks/pre-commit             # optional fallback for any agent
```

## The Core Idea

Agent guidance has two layers:

| Layer | Purpose | Reliability |
|---|---|---|
| Rules files | Judgment, planning, style, process | Advisory |
| Hooks/artifacts | Type-checks, tests, lint, state updates, visual evidence | Enforceable where supported |

If something can be forgotten or rationalized away, move it out of prose
and into a checked artifact.

## Runtime Lessons Applied

The production-agent lessons that fit this repo are applied as contracts,
not as copied API boilerplate:

- **Cost/context discipline** — concise directives, helper discovery, and
  durable `memory/` files instead of giant repeated prompts.
- **Reliability** — structured hook JSON, deterministic checks,
  destructive-command blocks, and explicit unverified-state warnings.
- **Performance** — bounded work slices, selective context loading, safe
  parallel tool use, and truncation warnings.
- **Tool use** — structured tool-result guidance, validation before
  execution, and clear helper boundaries.
- **Output quality** — tests, runtime evidence, visual artifacts, and
  independent/adversarial verification.

API-specific features such as prompt caching, streaming display,
provider retries, idempotency keys, temperature tuning, and batch
processing belong in the application or host runtime. `agent-md` tells
the coding agent to document and verify those choices when the project
uses them; it does not pretend to enforce provider behavior from a rules
file.

## Enforcement Matrix

| Check | Claude Code | Codex | Cursor / Windsurf / Other |
|---|---|---|---|
| Bash safety | Hard block via `.claude/hooks/block-destructive.sh` | Hard block via `.codex/hooks/pre-tool-use.sh` | Not covered |
| Type-check/lint/tests at finish | Hard block via `stop-verify.sh` | Continuation via `.codex/hooks/stop.sh` | Optional `.githooks/pre-commit` |
| `memory/progress.md` updated | Hard block via `state-enforcement.sh` | Continuation via `.codex/hooks/stop.sh` | Optional `.githooks/pre-commit` |
| UI visual evidence | Advisory by default, hard block when `[visual].required = true` | Same through Codex Stop wrapper | Advisory through rules |
| New export without nearby test | Advisory | Advisory through rules/skills | Advisory through rules |
| Truncated Bash output | Advisory | Advisory through Codex PostToolUse | Not covered |
| Planning, context, edit safety | Advisory | Advisory | Advisory |

Codex hooks are experimental and require:

```toml
[features]
codex_hooks = true
```

in `~/.codex/config.toml`.

## Install Options

```bash
# All supported agents
./install.sh .

# Specific agents
./install.sh --agent=claude .
./install.sh --agent=codex,cursor .

# Git hook fallback
./install.sh --githooks .
./install.sh --no-githooks .

# Claude settings handling
./install.sh --claude-settings=skip .
./install.sh --claude-settings=merge .
./install.sh --claude-settings=replace .
```

The installer backs up existing top-level rule files before replacing
them. Existing `memory/*.md` files are never overwritten. Existing
`.claude/settings.json` is skipped by default unless you choose `merge`
or `replace`.

## Deterministic Verification

Heuristics are useful, but explicit commands are better. Copy the example
config and declare your project checks:

```bash
cp agent-md.toml.example agent-md.toml
```

```toml
[verify]
typecheck = "npx --no-install tsc --noEmit"
lint      = "npx --no-install eslint ."
test      = "pnpm test"
lint_file = "npx --no-install eslint {file}"

[visual]
required          = true
artifacts_dir     = ".agent/visual"
freshness_seconds = 3600
```

When no checks are detected, hooks allow completion but warn that the
work is unverified.

## Visual Evidence

UI work needs more than passing tests. Capture a screenshot:

```bash
./.agent-md/bin/playwright-capture.sh http://localhost:3000 .agent/visual/home.png
```

Then write `.agent/visual/home.md`:

```markdown
# Visual Check

Changed files:
- src/app/page.tsx

Route: /
Viewport: 1280x800
Artifact: home.png
Observed result: layout renders without overlap at desktop width.
```

The strict visual hook requires a fresh non-empty markdown file that
references a fresh non-empty image by filename and includes the required
fields.

## Memory Files

`memory/` is the durable handoff surface between sessions:

- `agents.md` — active agents, MCPs, tech stack, tooling
- `plan.md` — macro design and vertical slices
- `progress.md` — current task, completed tasks, backlog, blocked work
- `verify.md` — definition of done
- `gotchas.md` — mistakes already corrected by the human

The state hook blocks completion when source files changed but
`memory/progress.md` did not.

## Helper Scripts vs Codex Skills

`agent-md` intentionally separates plain helper scripts from Codex-native
skills.

- `.agent-md/bin/*` are shell helpers any agent can run.
- `.agents/skills/<name>/SKILL.md` are native Codex skills.

Discover helpers:

```bash
./.agent-md/bin/discover_helpers.sh
./.agent-md/bin/doctor.sh
```

Use Codex skills with `$agent-md-verify` or `$visual-evidence`.

## What This Does Not Fix

- A rules file cannot force judgment by itself.
- Hooks only cover events exposed by the host agent.
- Pre-commit hooks can be bypassed with `git commit --no-verify`.
- Bash safety hooks are guardrails, not a sandbox.
- Cursor and Windsurf get rules plus optional git-hook fallback, not
  native runtime enforcement from this repo.

## Development

```bash
bats tests/
shellcheck .claude/hooks/*.sh .codex/hooks/*.sh .agent-md/bin/*.sh .githooks/pre-commit install.sh
```

CI runs Bats, ShellCheck, JSON validation, alias-sync checks, and
installer smoke tests.

## License

MIT.
