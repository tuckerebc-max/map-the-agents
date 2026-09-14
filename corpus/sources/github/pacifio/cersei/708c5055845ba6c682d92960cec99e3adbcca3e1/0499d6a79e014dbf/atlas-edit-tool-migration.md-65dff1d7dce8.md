# Cersei SDK — `Edit` tool now does tolerant matching (Atlas migration report)

**Audience:** the Claude Code agent developing Atlas.
**TL;DR:** The Cersei SDK's built-in `Edit` tool no longer requires a byte-exact
`old_string`. It now runs the same kind of replacer ladder Atlas ported from
OpenCode, upstream. Atlas can **switch its `tools/atlas_coding` Edit back to the
SDK's `Edit` tool**. Read/Write/Grep/Glob/List/Bash were not touched by this
change — migrate only the Edit abstraction (and only if the custom one exists
purely to work around the exact-match bug).

---

## Why this changed

Exact string matching made edits brittle. Weaker BYOK models (Qwen, DeepSeek,
Gemini Flash) drift on leading whitespace and indentation, so an otherwise
correct `old_string` failed with `old_string not found`, and the model fell back
to slow, error-prone `sed`/`cat` edits. This was the primary source of editing
failures in Atlas/Cersei.

The fix lives in the SDK so every consumer benefits, and so Atlas can drop its
temporary workaround.

## What changed in the SDK

Crate: `cersei-tools` (shipped in workspace **`0.2.3`** — see the `[0.2.3]`
section of `CHANGELOG.md`).

1. **New primitive — `cersei_tools::tool_primitives::replace::replace`**
   ```rust
   pub fn replace(
       content: &str,
       old: &str,
       new: &str,
       replace_all: bool,
   ) -> Result<String, ReplaceError>;

   pub enum ReplaceError { NotFound, Ambiguous { count: usize }, NoChange, EmptyOldString }
   ```
   A "replacer ladder" — tries strategies in order, first **unique** hit wins:
   1. Exact match (tried first)
   2. Line-trimmed (per-line leading/trailing whitespace ignored)
   3. Block-anchor (first + last line anchor a 3+ line block, interior ignored)
   4. Whitespace-normalized (runs of whitespace collapsed)
   5. Indentation-flexible (common leading indent stripped)

2. **`tool_primitives::fs::edit_file` now routes through the ladder.** Same
   signature as before; added a `NoChange` variant to `EditError`.

3. **`Edit` tool (`file_edit::FileEditTool`) hardened at the input/output edges:**
   - **Input coercion** — accepts common near-miss field names (`path`, `old`,
     `new`, `search`, `replace`, camelCase variants), stringified/numeric
     booleans (`"replace_all": "true"`), and a missing `new_string` (treated as
     a deletion).
   - **Corrective error messages** — failures now guide the model to a fix
     (re-read the file and copy verbatim; add surrounding context to
     disambiguate; set `replace_all=true`) instead of a bare error.

### Safety: the destructive-match guard

This is the important property for Atlas to trust the swap:

- **A fuzzy match never invents text.** Every strategy only ever yields a
  candidate that *already exists* in the file; fuzziness relaxes *how* the text
  is located, never *what* is written.
- **Exact match is tried first**, so genuine duplicates still report
  `Ambiguous { count }` (→ `AmbiguousMatch` at the tool layer) rather than being
  silently fuzz-matched.
- **Line-based strategies require every line to match** after normalization.
- **The one anchor-only strategy (block-anchor)** is additionally gated by a
  `0.5` char-level similarity threshold, so a coincidental first/last-line pair
  cannot rewrite an unrelated block.
- **Non-unique fuzzy candidates are skipped**, not guessed.

## Behavioral contract (what the model sees)

- `Edit` input schema is unchanged: `file_path`, `old_string`, `new_string`,
  optional `replace_all` (now coercible from aliases/strings as above).
- Success message format is unchanged (`"The file ... has been updated. N
  replacement(s) made."` followed by a truncated unified diff).
- Errors:
  - not located by any strategy → error mentioning the editor already tolerates
    whitespace/indent and to re-read + copy verbatim.
  - `old_string` appears verbatim more than once and `replace_all` is false →
    "not unique (N occurrences)… add context or set replace_all".
  - `old_string == new_string` → "identical, would do nothing" (new `NoChange`).
- **Edge case to know:** after a `replace_all` that engaged a *fuzzy* candidate,
  `replacements_made` is approximated (exact-occurrence count, min 1). Single
  edits always report exactly 1. Don't build logic that depends on an exact
  fuzzy-replace-all count.

## Migration steps for Atlas

1. In `tools/atlas_coding`, replace the custom Edit tool registration with the
   SDK's `cersei_tools::file_edit::FileEditTool` (it registers under the tool
   name `"Edit"`). Keep your custom Read/Write/Grep/Glob/List/Bash unless you
   have a separate reason to keep them.
2. If you registered the custom Edit by name, remove it so there's no duplicate
   `"Edit"` tool; ensure the SDK one is in the tool set.
3. Delete the now-dead OpenCode-port Edit code (and its tests) from
   `tools/atlas_coding`, or leave it behind a feature flag if you want an A/B.
4. Re-run your editing benchmarks against a weak model (Gemini Flash / Qwen) to
   confirm the SDK tool matches or beats the custom one. The SDK has unit + tool
   tests covering indentation drift, field aliasing, stringified `replace_all`,
   and ambiguous-match messaging.
5. Pin the cersei dependency to **`0.2.3`** (the release that contains this
   change).

## If Atlas wants the primitive instead of the whole tool

If `tools/atlas_coding` needs to keep its own tool wrapper (custom result
formatting, telemetry, permission handling) but wants the matching logic, call
the primitive directly and keep your wrapper thin:

```rust
use cersei_tools::tool_primitives::replace::{replace, ReplaceError};

let new_content = replace(&content, &old_string, &new_string, replace_all)?;
// then write new_content yourself
```

or use `cersei_tools::tool_primitives::fs::edit_file(path, old, new, replace_all)`
which reads/replaces/writes and returns `EditResult { replacements_made }`.

## Files changed in the SDK (for reference / review)

- `crates/cersei-tools/src/tool_primitives/replace.rs` (new)
- `crates/cersei-tools/src/tool_primitives/mod.rs` (module registration)
- `crates/cersei-tools/src/tool_primitives/fs.rs` (`edit_file` → ladder, `NoChange`)
- `crates/cersei-tools/src/file_edit.rs` (coercion, corrective errors, tests)
- `CHANGELOG.md` (`[Unreleased]`)

Tests: `cargo test -p cersei-tools --lib` (131 passing, clippy-clean).
