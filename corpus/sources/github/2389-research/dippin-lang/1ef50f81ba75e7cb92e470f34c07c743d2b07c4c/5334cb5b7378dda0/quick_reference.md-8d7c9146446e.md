# Complexity Policy

## Thresholds (enforced by pre-commit hook)

| Metric | Max | Tool |
|--------|-----|------|
| Cyclomatic complexity | 5 per function | `gocyclo -over 5 .` |
| Cognitive complexity | 7 per function | `gocognit -over 7 .` |

Test functions (`_test.go`) are excluded from enforcement.

## Quick Commands

```bash
just complexity                       # run complexity checks
gocyclo -over 5 . | grep -v _test.go # cyclomatic violations
gocognit -over 7 . | grep -v _test.go # cognitive violations
gocyclo -top 10 .                     # top 10 most complex
```

## Refactoring Patterns

When a function exceeds the threshold, use **Extract Method**:

1. **Map lookup** for flat switches (e.g., `switch kind { case A: ... }` → `var kindMap = map[Kind]Value{...}`)
2. **Extract helper** for nested loops or conditionals
3. **Named predicate** for compound boolean expressions (e.g., `ch == '=' || ch == '!'` → `isOperatorChar(ch)`)
4. **Split by responsibility** for functions doing multiple things

## Tools Setup

```bash
go install github.com/fzipp/gocyclo/cmd/gocyclo@latest
go install github.com/uudashr/gocognit/cmd/gocognit@latest
just setup-hooks  # install pre-commit hook
```
