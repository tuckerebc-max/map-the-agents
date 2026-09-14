# Agent Instructions

**Read the constitution**: `.specify/memory/constitution.md`

That file contains ALL instructions for working on this project, including:
- Project principles and constraints
- Ralph Wiggum workflow configuration
- Autonomy settings (YOLO mode, git autonomy)
- How to run the Ralph loop
- Specification or issue tracking approach
- Context detection (Ralph loop vs interactive chat)

The constitution is the single source of truth. Read it on every chat session.

---

## Quick Reference

### You're in a Ralph Loop if:
- Started by `ralph-loop.sh`, `ralph-loop-codex.sh`, or their PowerShell `.ps1` equivalents
- Prompt mentions "implement spec" or "work through all"
- You see `<promise>` completion signals

**Action**: Focus on implementation. Complete acceptance criteria. Output `<promise>DONE</promise>`.

### You're in Interactive Chat if:
- User is asking questions or discussing ideas
- Helping set up the project or create specs
- No Ralph loop was started

**Action**: Be helpful. Guide the user. Create specs. Explain how to start Ralph loop.

---

## The Magic Word

When the user says **"Ralph, start working"**, tell them the terminal commands to run the Ralph loop.
