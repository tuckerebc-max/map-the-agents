# Gap Analysis: yoyo vs Claude Code

Last updated: Day 1 (reset)

This document tracks the feature gap between yoyo and Claude Code. Use it to guide improvements when there are no community issues to address.

**Important:** Only mark features as implemented if they actually work in the code TODAY. Don't claim features you haven't built yet.

## Legend
- ✅ **Implemented** — yoyo has this and it works
- 🟡 **Partial** — yoyo has a basic version
- ❌ **Missing** — yoyo doesn't have this yet

---

## Core Agent Loop

| Feature | yoyo | Claude Code | Notes |
|---------|------|-------------|-------|
| Streaming text output | ✅ | ✅ | Both stream tokens as they arrive |
| Tool execution | ✅ | ✅ | bash, read_file, write_file, edit_file, search, list_files |
| Multi-turn conversation | ✅ | ✅ | Via yoagent conversation history |
| Error recovery / auto-retry | 🟡 | ✅ | yoagent has basic retry; no smart recovery |
| Parallel tool execution | ❌ | ✅ | Claude Code runs multiple tools in parallel |
| Tool output streaming | ❌ | ✅ | Claude Code streams long-running tool output |

## CLI & UX

| Feature | yoyo | Claude Code | Notes |
|---------|------|-------------|-------|
| Interactive REPL | ✅ | ✅ | Basic — /quit, /clear, /model, /help |
| Piped/stdin mode | ✅ | ✅ | Used by evolve.sh |
| Model selection | ✅ | ✅ | --model flag and /model command |
| Readline / line editing | ❌ | ✅ | yoyo uses raw stdin, no arrow keys/history |
| Tab completion | ❌ | ✅ | Claude Code completes file paths |
| Syntax highlighting | ❌ | ✅ | Claude Code highlights code in output |
| Markdown rendering | ❌ | ✅ | Claude Code renders markdown |
| Progress indicators | 🟡 | ✅ | yoyo shows tool names with ✓/✗; no spinners |

## Context Management

| Feature | yoyo | Claude Code | Notes |
|---------|------|-------------|-------|
| Token usage display | 🟡 | ✅ | Shows input/output counts, no cost estimate |
| Auto-compaction | ❌ | ✅ | Claude Code auto-compacts at context limits |
| Context window awareness | ❌ | ✅ | No tracking of how full the context is |

## Permission System

| Feature | yoyo | Claude Code | Notes |
|---------|------|-------------|-------|
| Tool approval prompts | ❌ | ✅ | Claude Code asks before destructive commands |
| Allowlist/blocklist | ❌ | ✅ | No permission configuration |
| Directory restrictions | ❌ | ✅ | No file access controls |

## Project Understanding

| Feature | yoyo | Claude Code | Notes |
|---------|------|-------------|-------|
| Auto-detect project type | ❌ | ✅ | Claude Code detects language/framework |
| Git-aware context | ❌ | ✅ | Claude Code knows branch, recent changes |
| Codebase indexing | ❌ | ✅ | Claude Code indexes for faster search |

## Error Handling

| Feature | yoyo | Claude Code | Notes |
|---------|------|-------------|-------|
| API error display | ✅ | ✅ | Shows error messages |
| Network retry | 🟡 | ✅ | yoagent has basic retry |
| Graceful degradation | ❌ | ✅ | No fallback on partial failures |

---

## Priority Queue

**Remember rule 9: prioritize the evolution loop.** The most impactful improvements are ones that make each evolution cycle better, not ones that improve interactive UX.

### High impact (used every evolution cycle):
1. **Better error recovery in piped mode** — When cargo build/test fails, can you extract the error and retry intelligently?
2. **Context awareness** — Track how much of the context window you've used; avoid wasting tokens reading files you've already seen
3. **Smarter self-assessment** — Can you identify which of your changes actually helped vs. were neutral?

### Medium impact (improves agent quality):
4. **Parallel tool execution** — Speed up multi-tool workflows
5. **Git-aware context** — Know what branch you're on, what changed recently
6. **Auto-detect project type** — Better defaults for different codebases

### Lower priority (interactive UX — no user at terminal yet):
7. Readline/line editing
8. Syntax highlighting
9. Permission system
10. Tab completion

## Stats

Update these after each session:
- Lines of Rust: ___ across ___ source files
- Tests passing: ___
- REPL commands: 4 (/quit, /clear, /model, /help)
