# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A self-evolving coding agent CLI built on [yoagent](https://github.com/yologdev/yoagent). Forked from [yologdev/yoyo-evolve](https://github.com/yologdev/yoyo-evolve) and adapted to run against a local LLM or cloud providers via OpenRouter. A GitHub Actions cron job (`scripts/evolve.sh`) runs the agent every 8 hours, which reads its own source, picks improvements, implements them, and commits — if tests pass.

## Build & Test Commands

```bash
cargo build              # Build
cargo test               # Run tests
cargo clippy --all-targets -- -D warnings   # Lint (CI treats warnings as errors)
cargo fmt -- --check     # Format check
cargo fmt                # Auto-format
```

CI runs all four checks (build, test, clippy with -D warnings, fmt check) on push/PR to main.

To run the agent interactively:
```bash
cargo run                                          # Local LLM (default)
cargo run -- --base-url http://localhost:8080       # Different local endpoint
cargo run -- --provider anthropic                   # Anthropic (needs ANTHROPIC_API_KEY)
cargo run -- --model qwen3.5-27b --skills ./skills  # With skills
cargo run -- --base-url https://openrouter.ai/api/v1 --api-key sk-or-... --model google/gemini-2.5-flash  # OpenRouter
```

To trigger a full evolution cycle:
```bash
./scripts/evolve.sh                                           # Local LLM (default)
PROVIDER=anthropic ANTHROPIC_API_KEY=sk-... ./scripts/evolve.sh  # Anthropic
OPENROUTER_API_KEY=sk-or-... MODEL=google/gemini-2.5-flash ./scripts/evolve.sh  # OpenRouter
```

## Architecture

**Single-file agent** — all source is in:
- `src/main.rs` — REPL loop, command handling, piped stdin mode
- `src/provider.rs` — `LocalProvider` wrapper for OpenAI-compatible endpoints

**Provider support** — defaults to local OpenAI-compatible endpoint (llama.cpp at `http://192.168.1.128:8080`). Anthropic available via `--provider anthropic`. OpenRouter via `--base-url https://openrouter.ai/api/v1 --api-key sk-or-...`. The `LocalProvider` wraps yoagent's `OpenAiCompatProvider`, injecting a `ModelConfig` with the configured base URL.

**Evolution loop** (`scripts/evolve.sh`): Verifies build → fetches GitHub issues (via `gh` CLI + `scripts/format_issues.py`) → pipes a structured prompt into the agent → verifies build after changes → commits or reverts → posts issue responses → pushes. Controlled by env vars: `PROVIDER`, `BASE_URL`, `MODEL`, `TIMEOUT`, `OPENROUTER_API_KEY`.

**Skills** (`skills/`): Markdown files with YAML frontmatter loaded via `--skills ./skills`. Four skills define the agent's workflow:
- `self-assess` — read own code, try tasks, find bugs/gaps
- `evolve` — safely modify source, test, revert on failure
- `communicate` — write journal entries and issue responses
- `research` — search the web, read docs, study other projects

**State files** (read/written by the agent during evolution):
- `IDENTITY.md` — the agent's constitution and rules (DO NOT MODIFY)
- `JOURNAL.md` — chronological log of evolution sessions (append at top, never delete)
- `LEARNINGS.md` — cached knowledge from internet lookups
- `DAY_COUNT` — integer tracking current evolution day
- `ISSUES_TODAY.md` — ephemeral, generated during evolution from GitHub issues (gitignored)
- `ISSUE_RESPONSE.md` — ephemeral, agent writes this to respond to issues (gitignored)

## CLI Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--provider` | `local` | `local` or `anthropic` |
| `--base-url` | `http://192.168.1.128:8080` | OpenAI-compatible endpoint URL (use `https://openrouter.ai/api/v1` for OpenRouter) |
| `--api-key` | from env | API key (overrides env vars) |
| `--context-window` | `65536` | Context window size in tokens |
| `--model` | `qwen3.5-27b` (local) / `claude-opus-4-6` (anthropic) | Model name |
| `--max-tokens` | `4096` | Max output tokens per response |
| `--skills` | none | Skills directory |
| `--help, -h` | — | Show help |
| `--version, -V` | — | Show version |

## Safety Rules

These are enforced by the `evolve` skill and `evolve.sh`:
- Never modify `IDENTITY.md`, `scripts/evolve.sh`, `scripts/format_issues.py`, `scripts/build_site.py`, or `.github/workflows/`
- Every code change must pass `cargo build && cargo test`
- If build fails after changes, revert with `git checkout -- src/`
- Never delete existing tests
- Write tests before adding features

## Security

Issue content is treated as untrusted user input:
- Content boundaries use per-session nonces (not spoofable)
- HTML comments are stripped from issue bodies
- Embedded boundary markers are neutralized
- The evolve skill includes behavioral rules against social engineering
