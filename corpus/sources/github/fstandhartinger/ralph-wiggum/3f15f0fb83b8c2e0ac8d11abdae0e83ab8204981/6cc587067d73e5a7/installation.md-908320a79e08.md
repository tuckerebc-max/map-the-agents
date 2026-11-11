# AI Agent: Ralph Wiggum Setup

> **You're an AI coding agent.** Follow these instructions to set up Ralph Wiggum.
>
> **Actually execute these steps** — don't just describe them.

---

## Overview: What You'll Do

1. **Quick Setup** — Create directories and download scripts (1 minute)
2. **Project Interview** — Learn about the user's project vision (3-5 minutes)
3. **Constitution** — Create the project's guiding document
4. **Next Steps** — Explain how to create specs and start Ralph

The goal: Make this feel **lightweight, pleasant, and professional**. Focus on understanding the *project*, not interrogating about technical minutiae.

---

## Phase 1: Create Structure

```bash
mkdir -p .specify/memory specs scripts logs history completion_log .cursor/commands .claude/commands
```

---

## Phase 2: Download Scripts

Fetch from GitHub raw URLs:

| Script | URL | Save To |
|--------|-----|---------|
| ralph-loop.sh | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop.sh` | `scripts/ralph-loop.sh` |
| ralph-loop.ps1 | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop.ps1` | `scripts/ralph-loop.ps1` |
| ralph-loop-codex.sh | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop-codex.sh` | `scripts/ralph-loop-codex.sh` |
| ralph-loop-codex.ps1 | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop-codex.ps1` | `scripts/ralph-loop-codex.ps1` |
| ralph-loop-gemini.sh | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop-gemini.sh` | `scripts/ralph-loop-gemini.sh` |
| ralph-loop-gemini.ps1 | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop-gemini.ps1` | `scripts/ralph-loop-gemini.ps1` |
| ralph-loop-copilot.sh | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop-copilot.sh` | `scripts/ralph-loop-copilot.sh` |
| ralph-loop-copilot.ps1 | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/ralph-loop-copilot.ps1` | `scripts/ralph-loop-copilot.ps1` |
| RalphLoop.ps1 | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/lib/RalphLoop.ps1` | `scripts/lib/RalphLoop.ps1` |
| SpecQueue.ps1 | `https://raw.githubusercontent.com/fstandhartinger/ralph-wiggum/main/scripts/lib/SpecQueue.ps1` | `scripts/lib/SpecQueue.ps1` |

```bash
chmod +x scripts/ralph-loop*.sh
```

On Windows PowerShell, no executable bit is needed. Run the `.ps1` variant that
matches your agent, for example `.\scripts\ralph-loop.ps1` or
`.\scripts\ralph-loop-copilot.ps1 20`.

---

## Phase 3: Get Version Info

```bash
git ls-remote https://github.com/fstandhartinger/ralph-wiggum.git HEAD | cut -f1
```

Store the commit hash for the constitution.

---

## Phase 4: Project Interview

### Introduction

Start with a warm, brief introduction:

> "I'll ask a few quick questions to understand your project. This creates a **constitution** — a short document that helps me stay aligned with your goals across all future sessions.
>
> Don't worry about getting everything perfect — we can always refine it later."

### The Questions

Present these conversationally, one at a time. **Keep it lightweight.**

---

#### 1. Project Name
> "What's the name of your project?"

---

#### 2. Project Vision (MOST IMPORTANT)

> "Tell me about your project — what is it, what problem does it solve, who is it for?
>
> This is the most important question. The more I understand your vision, the better I can help build it."

**Note to AI:** This is the heart of the interview. Encourage the user to share context. A few sentences to a paragraph is ideal.

---

#### 3. Core Principles

> "What 2-3 principles should guide development? Think about what matters most.
>
> Examples: 'User experience first', 'Keep it simple', 'Security above all', 'Move fast', 'Quality over speed'"

**Note to AI:** If the user struggles, offer to suggest principles based on their project description.

---

#### 4. Technical Stack (OPTIONAL)

> "What's the tech stack? (Or should I figure it out from the codebase?)"

**Note to AI:** For existing projects, analyze the codebase yourself. Don't pressure the user.

---

#### 5. Autonomy Settings

> "Two quick settings:
>
> **YOLO Mode** (recommended): Execute commands, modify files, run tests without asking each time.
>
> **Git Autonomy** (recommended): Commit and push automatically after each spec.
>
> Enable both? (yes/no)"

**Note to AI:** Default to YES for both if the user seems agreeable.

---

#### 6. Optional Features

Present as a quick yes/no checklist:

> "A couple of optional features:"

**a) Telegram Notifications** — Progress updates (completions, failures) sent to a Telegram chat.

> "Want Telegram notifications? (yes/no)"

If yes, ask for `TG_BOT_TOKEN` and `TG_CHAT_ID` (env vars, never put tokens in files).

**b) GitHub Issues** — Work on GitHub issues in addition to spec files.

> "Should Ralph also work on GitHub Issues? (yes/no)"

If yes, ask for the repository (e.g. `owner/repo`) and whether issues need approval first.

**c) Completion Logs** — Keep a log of completed specs in `completion_log/`.

> "Keep a completion log? (yes/no)"

---

### Interview Complete

> "That's all I need. Let me set up your project..."

---

## Phase 5: Create Constitution

Create `.specify/memory/constitution.md` using the interview answers.

The constitution must be **concise**. It's the single source of truth — the agent reads it every iteration.

**Template** (fill in bracketed values, include optional sections only if user opted in):

```markdown
# {PROJECT_NAME} Constitution

> {PROJECT_VISION}

---

## Context Detection

**Ralph Loop Mode** (started by ralph-loop*.sh):
- Pick highest priority incomplete spec from `specs/`
- Implement, test, commit, push
- Output `<promise>DONE</promise>` only when 100% complete
- Output `<promise>ALL_DONE</promise>` when no work remains

**Interactive Mode** (normal conversation):
- Be helpful, guide decisions, create specs

---

## Core Principles

{List the user's principles, one per line}

---

## Technical Stack

{List or "Detected from codebase"}

---

## Autonomy

YOLO Mode: {ENABLED/DISABLED}
Git Autonomy: {ENABLED/DISABLED}

---

## Specs

Specs live in `specs/` as markdown files. Pick the highest priority incomplete spec (lower number = higher priority). A spec is incomplete if it lacks `## Status: COMPLETE`.

Spec template: https://raw.githubusercontent.com/github/spec-kit/refs/heads/main/templates/spec-template.md

When all specs are complete, re-verify a random one before signaling done.

---

## NR_OF_TRIES

Track attempts per spec via `<!-- NR_OF_TRIES: N -->` at the bottom of the spec file. Increment each attempt. At 10+, the spec is too hard — split it into smaller specs.

---

## History

Append a 1-line summary to `history.md` after each spec completion. For details, create `history/YYYY-MM-DD--spec-name.md` with lessons learned, decisions made, and issues encountered. Check history before starting work on any spec.

---

## Completion Signal

All acceptance criteria verified, tests pass, changes committed and pushed → output `<promise>DONE</promise>`. Never output this until truly complete.
```

### Optional Sections (add to constitution only if user opted in)

#### If Telegram: YES

```markdown
---

## Telegram Notifications

Send progress via Telegram using env vars `TG_BOT_TOKEN` and `TG_CHAT_ID`.

After completing a spec:
  curl -s -X POST "https://api.telegram.org/bot$TG_BOT_TOKEN/sendMessage" \
    -d chat_id="$TG_CHAT_ID" -d parse_mode=Markdown \
    -d text="✅ *Completed:* {spec name}%0A{one-line summary}"

Also notify on: 3+ consecutive failures, stuck specs (NR_OF_TRIES >= 10).
```

#### If GitHub Issues: YES

```markdown
---

## GitHub Issues

Work on issues from `{OWNER/REPO}` in addition to specs. Use `gh` CLI:
  gh issue list --repo {OWNER/REPO} --state open
  gh issue close <number> --repo {OWNER/REPO}

{If approval required: Only work on issues approved by **{APPROVER}**.}
```

#### If Completion Logs: YES

```markdown
---

## Completion Logs

After each spec, create `completion_log/YYYY-MM-DD--HH-MM-SS--spec-name.md` with a brief summary.
```

---

## Phase 6: Create Agent Entry Files

### AGENTS.md (project root)

```markdown
# Agent Instructions

**Read:** `.specify/memory/constitution.md`

That file is your source of truth for this project.
```

### CLAUDE.md (project root)

Same content as AGENTS.md.

---

## Phase 7: Explain Next Steps

> **Ralph Wiggum is ready!**
>
> **To create a spec:** Describe what you want built. I'll create a spec file in `specs/` with acceptance criteria.
>
> **To start the loop:** `./scripts/ralph-loop.sh`
>
> Ralph picks specs, implements them, verifies acceptance criteria, commits, pushes, and moves to the next — all autonomously.

| Task | Command |
|------|---------|
| Start building | `./scripts/ralph-loop.sh` |
| Use Codex | `./scripts/ralph-loop-codex.sh` |
| Use Gemini | `./scripts/ralph-loop-gemini.sh` |
| Use Copilot | `./scripts/ralph-loop-copilot.sh` |
| Limit iterations | `./scripts/ralph-loop.sh 20` |

PowerShell equivalents use the same arguments with `.ps1`, for example
`.\scripts\ralph-loop.ps1 20`.

Ready to create your first specification?
