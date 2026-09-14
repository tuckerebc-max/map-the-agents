# Claude North Star

> Transform CLI agents from task executors into autonomous project partners

[![npm version](https://img.shields.io/npm/v/claude-northstar.svg)](https://www.npmjs.com/package/claude-northstar)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What is this?

**Claude North Star** is a goal-oriented development framework for CLI agents like [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and OpenCode. Instead of giving your AI agent task after task, you share a **vision** and it works autonomously toward it.

### Before (Task-Based)
```
You: "Create the user model"
Agent: "Done. What's next?"
You: "Add authentication"
Agent: "Done. What's next?"
You: "Write tests"
... (repeat forever)
```

### After (Goal-Oriented)
```
You: "I want to build a fitness app with workout tracking and Watch sync"
North Star: Plans milestones → Works autonomously → Reports progress → Asks strategic questions only
```

## Installation

### One command (recommended)

```bash
npx claude-northstar init
```

### Other options

```bash
# Check status
npx claude-northstar status

# Uninstall
npx claude-northstar uninstall
```

### Alternative: curl

```bash
curl -fsSL https://raw.githubusercontent.com/nisarg38/claude-northstar/main/install.sh | bash
```

## Quick Start

1. **Install North Star** in your project (see above)

2. **Start Claude Code** and share your vision:
   ```
   I want to build a fitness app with workout tracking.
   Success looks like: users can log workouts on their phone and see progress over time.
   ```

3. **North Star will:**
   - Capture your vision in `north-star.md`
   - Analyze your codebase
   - Propose milestones
   - Start working autonomously

4. **Resume anytime** by saying `continue`

## How It Works

### The Main Agent as Tech Lead

The Claude Code session acts as a **Tech Lead** that:
- Understands your vision
- Plans milestones and priorities
- Coordinates a team of sub-agents
- Reports meaningful progress
- Asks only strategic questions

### The Team (Sub-Agents)

| Role | Purpose | When Used |
|------|---------|-----------|
| **Product Researcher** | Market research, competitors | Early planning |
| **Strategist** | Architecture decisions | Technical crossroads |
| **Developer** | Implementation | Building features |
| **QA** | Testing, verification | After implementation |
| **Reviewer** | Code review | Before merging |

### The Autonomous Work Loop

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│ ANALYZE │ ──▶ │  PLAN   │ ──▶ │ EXECUTE │ ──▶ │ EVALUATE│
│ state   │     │ next    │     │ work    │     │ progress│
└─────────┘     └─────────┘     └─────────┘     └─────────┘
     ▲                                               │
     └───────────────────────────────────────────────┘
```

## North Star Files

After installation, you'll have:

```
.claude/harness/
├── north-star.md           # Your project vision (THE source of truth)
├── project-state.json      # Current state, milestones, progress
├── decisions.md            # Architecture decisions log
├── progress-log.md         # Session-by-session progress
└── prompts/                # Sub-agent prompt templates
    ├── product-researcher.md
    ├── strategist.md
    ├── developer.md
    ├── qa.md
    └── reviewer.md
```

### north-star.md

The vision document. Define what you're building and what success looks like:

```markdown
# Project North Star

## Vision
Build a fitness app with workout tracking and Apple Watch sync.

## Success Criteria
- [ ] User can log workouts on iPhone
- [ ] Workouts sync to Apple Watch
- [ ] Clean, intuitive UI

## Constraints
- iOS 17+ only
- SwiftUI preferred
```

### project-state.json

Tracks progress across sessions:

```json
{
  "milestones": [
    {"id": "m1", "title": "Core models", "status": "done"},
    {"id": "m2", "title": "Workout UI", "status": "in_progress", "progress": 0.6}
  ],
  "currentFocus": "m2",
  "gaps": ["Missing HealthKit integration"]
}
```

## Key Behaviors

| Behavior | Description |
|----------|-------------|
| **Goal-Oriented** | Refers to `north-star.md` constantly |
| **Self-Directing** | Figures out what to do, doesn't wait for tasks |
| **Progress Tracking** | Tracks milestones, not individual tasks |
| **Strategic Questions** | Asks only for major decisions |
| **Session Continuity** | State persists, say "continue" to resume |
| **Quality Pipeline** | Dev → QA → Review → Merge |

## When North Star Asks You

North Star will only interrupt for:

- **Major architecture decisions**: "Should we use PostgreSQL or SQLite?"
- **Ambiguous requirements**: "Should workout history be editable?"
- **Milestone reviews**: "Milestone 1 complete. Here's what I built. Review?"

It will **NOT** ask for:
- Every task completion
- Minor implementation choices
- Routine progress updates

## Recommended Setup

### With Jujutsu (jj)

For better workspace isolation during parallel work:

```bash
# Install jj
brew install jj

# Initialize in your repo
jj git init --colocate
```

North Star works with plain git, but jj enables:
- Isolated workspaces for parallel tasks
- Conflicts as data (operations never fail)
- Easy rollback via operation log

### CLAUDE.md

North Star adds a section to your `CLAUDE.md` (or creates one) explaining how to use it. This gives Claude Code the context it needs.

## Examples

### Starting a New Project

```
You: "I want to build a CLI tool for managing dotfiles.
     It should support multiple machines, git sync, and templating."

North Star: "I'll capture this vision. Here's my proposed milestone plan:
         M1: Core dotfile linking
         M2: Git sync integration
         M3: Multi-machine profiles
         M4: Template system

         Does this align with your vision?"

You: "Yes, start with M1"

North Star: [Works for 30 minutes]
         "M1 complete. Created symlink manager with conflict detection.
          Tests passing. Ready for M2?"
```

### Resuming Work

```
You: "continue"

North Star: "Last session: Completed M1 (dotfile linking).
         Current: M2 (git sync) at 40%.
         Continuing with git sync integration..."
```

### Strategic Question

```
North Star: "For git sync, I can either:
         A) Use libgit2 - faster, but adds dependency
         B) Shell out to git - simpler, requires git installed

         Given your goal of easy installation, which approach?"

You: "B, keep it simple"

North Star: "Noted in decisions.md. Continuing..."
```

## Uninstalling

```bash
rm -rf .claude/harness
# Optionally remove the North Star section from CLAUDE.md
```

## Contributing

Contributions welcome! Areas of interest:

- [ ] More sub-agent prompts (security auditor, documentation writer)
- [ ] Better milestone planning heuristics
- [ ] Integration with more CLI agents
- [ ] Headless mode for extended operation

## License

MIT

---

*North Star thinks about what to do, not just does what it's told.*
