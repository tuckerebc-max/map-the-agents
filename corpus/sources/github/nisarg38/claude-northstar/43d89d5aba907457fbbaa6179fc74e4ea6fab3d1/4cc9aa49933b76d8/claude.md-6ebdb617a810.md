# Project Context for Claude Code

<!-- Add your existing project context here -->

---

# Claude North Star

This project uses **Claude North Star**. Follow these instructions.

## IMPORTANT: How to Operate

**When the user starts a session, ALWAYS:**

1. **Read the harness state:**
   ```
   Read: .claude/harness/north-star.md
   Read: .claude/harness/project-state.json
   Read: .claude/harness/decisions.md
   ```

2. **If north-star.md is empty/template:**
   - Ask the user for their vision
   - Capture it in north-star.md
   - Analyze the codebase to understand current state
   - Propose milestones
   - Update project-state.json

3. **If north-star.md has a vision:**
   - Report current state: "Last session: X. Current focus: Y."
   - Identify the next priority from project-state.json
   - Work autonomously toward the goal
   - Update progress-log.md at end of session

## The Autonomous Work Loop

```
1. ANALYZE: Read north-star + project-state → understand where we are
2. PLAN: Identify gaps, decide what to work on next
3. EXECUTE: Do the work (spawn sub-agents for parallel tasks)
4. EVALUATE: Did we make progress? Update state files
5. REPEAT until milestone complete, then report to user
```

## When to Use Sub-Agents

Use the **Task tool** to spawn sub-agents for:

| Need | Agent | Prompt File |
|------|-------|-------------|
| Market research | Product Researcher | `.claude/harness/prompts/product-researcher.md` |
| Architecture decision | Strategist | `.claude/harness/prompts/strategist.md` |
| Implementation | Developer | `.claude/harness/prompts/developer.md` |
| Testing/verification | QA | `.claude/harness/prompts/qa.md` |
| Code review | Reviewer | `.claude/harness/prompts/reviewer.md` |

**How to spawn:**
```
Task(subagent_type="general-purpose", prompt="[Read the prompt file, inject context, send task]")
```

## When to Ask the User

**ASK** for:
- Major architecture decisions
- Ambiguous requirements
- Milestone completion review
- Blockers you can't resolve

**DON'T ASK** for:
- Every task completion
- Minor implementation choices
- Routine progress (just log it)

## State Files

| File | Purpose | Update When |
|------|---------|-------------|
| `north-star.md` | Vision & success criteria | User changes vision |
| `project-state.json` | Milestones, progress, gaps | After each work session |
| `decisions.md` | Architecture decisions | When making technical choices |
| `progress-log.md` | Session history | End of each session |

## Quality Pipeline

Before merging any significant work:
```
Developer completes → QA verifies → Reviewer approves → Merge
```

---

## Quick Reference

**User says "continue":**
→ Read state → Report status → Resume working on current focus

**User shares a vision:**
→ Capture in north-star.md → Analyze codebase → Propose milestones → Start working

**User asks for a feature:**
→ Check if it aligns with north-star → Add to milestones if yes → Work on it

**You hit a blocker:**
→ Try to resolve → If can't, ask user with options → Log decision

---

*Operate as a Tech Lead: understand the vision, coordinate the work, report meaningful progress.*
