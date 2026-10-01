# Token Budget

AI agents have finite context windows. The `--max-tokens` flag tells indxr to intelligently truncate output to fit within a token budget.

## Usage

```bash
indxr --max-tokens 4000
indxr --max-tokens 8000 --public-only
indxr --max-tokens 15000 -o INDEX.md
```

## Token Estimation

indxr uses the approximation of **1 token ≈ 4 characters**, which is a reasonable average for English text and code with most tokenizers. The budget is applied to the total output size.

## Progressive Truncation Strategy

When the output exceeds the budget, indxr progressively removes information in this order, stopping as soon as the output fits:

### 1. Truncate Long Doc Comments

Doc comments are shortened to their first line, capped at 80 characters. Multi-paragraph documentation is reduced to a one-line summary.

### 2. Strip All Doc Comments

If truncating isn't enough, all doc comments are removed entirely. This typically saves 2+ tokens per declaration.

### 3. Remove Private Declarations

Non-public declarations are dropped, retaining only the public API surface. This is often the largest reduction.

### 4. Remove Children

Fields, methods, and other child declarations are removed from structs, classes, enums, etc. Only the top-level declaration names remain.

### 5. Drop Least-Important Files

Files are ranked by importance and dropped from the end until the budget is met.

**File importance scoring:**
- Entry points (`main.rs`, `lib.rs`, `index.ts`, `main.py`, etc.): **+100 points**
- Proximity to root (fewer path components): **-5 per directory level**
- More public declarations: **+3 per public declaration**
- Fewer total lines: slight bonus (tiebreaker)

The directory tree and public API surface sections are always preserved first.

## What's Always Preserved

Even under aggressive truncation:
- The codebase header (stats, language breakdown)
- The directory structure tree
- The public API surface section
- File paths and language metadata
- At least the most important files with their public declarations

## Recommended Budgets

| Context | Suggested Budget |
|---------|-----------------|
| Small focused task | 2,000–4,000 |
| Standard agent context | 8,000–15,000 |
| Large context window | 15,000–30,000 |
| Full index (no budget) | omit `--max-tokens` |

The right budget depends on how much context the agent needs alongside the index — leave room for the conversation, source files the agent might read, and the agent's own reasoning.

## Combining with Filters

Filters apply before the token budget, so they work together:

```bash
# Public API within budget
indxr --public-only --max-tokens 4000

# Scoped to a directory within budget
indxr --filter-path src/api --max-tokens 3000

# Specific language within budget
indxr -l rust --max-tokens 8000
```

Using filters first reduces the data that needs to be truncated, resulting in a more complete output within the same budget.

## Tips

- **Filter first, budget second** — `--public-only` and `--filter-path` are more precise than relying on truncation alone
- **Use `--omit-imports`** to save tokens when import details aren't needed
- **Use `--omit-tree`** for very tight budgets where the directory structure is less important
- **Use `-d summary`** if you only need the file/directory overview
- The budget is approximate — actual output may be slightly over or under
