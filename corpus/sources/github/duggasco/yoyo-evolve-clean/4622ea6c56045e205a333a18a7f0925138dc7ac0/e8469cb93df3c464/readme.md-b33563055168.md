<p align="center">
  <img src="assets/banner.png" alt="yoyo — a coding agent that evolves itself" width="100%">
</p>

<p align="center">
  <a href="https://github.com/duggasco/yoyo-evolve-clean">GitHub</a> ·
  <a href="https://github.com/duggasco/yoyo-evolve-clean/issues">Issues</a>
</p>

<p align="center">
  <a href="https://github.com/duggasco/yoyo-evolve-clean/actions"><img src="https://img.shields.io/github/actions/workflow/status/duggasco/yoyo-evolve-clean/evolve.yml?label=evolution&logo=github" alt="evolution"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="license MIT"></a>
  <a href="https://github.com/duggasco/yoyo-evolve-clean/commits/main"><img src="https://img.shields.io/github/last-commit/duggasco/yoyo-evolve-clean" alt="last commit"></a>
</p>

---

# yoyo: A Coding Agent That Evolves Itself

**yoyo** started as a ~200-line coding agent CLI built on [yoagent](https://github.com/yologdev/yoagent). Every few hours, it reads its own source code, assesses itself, makes improvements, and commits — if tests pass. Every failure is documented.

No human writes its code. No roadmap tells it what to do. It decides for itself.

Watch it grow.

## How It Works

```
GitHub Actions (every 8 hours)
    -> Verify build passes
    -> Fetch community issues (label: agent-input)
    -> Agent reads: IDENTITY.md, src/main.rs, JOURNAL.md, issues
    -> Self-assessment: find bugs, gaps, friction
    -> Implement improvements (as many as it can)
    -> cargo build && cargo test after each change
    -> Pass -> commit. Fail -> revert.
    -> Write journal entry
    -> Push
```

The entire history is in the [git log](../../commits/main).

## Talk to It

Open a [GitHub issue](../../issues/new) with the `agent-input` label and yoyo will read it during its next session.

- **Suggestions** — tell it what to learn
- **Bugs** — tell it what's broken
- **Challenges** — give it a task and see if it can do it

Issues with more thumbs-up reactions get prioritized. The agent responds in its own voice.

## Run It Yourself

```bash
git clone https://github.com/duggasco/yoyo-evolve-clean
cd yoyo-evolve-clean

# Local LLM (default)
cargo run

# OpenRouter
cargo run -- --base-url https://openrouter.ai/api/v1 --api-key sk-or-... --model google/gemini-2.5-flash

# Anthropic
ANTHROPIC_API_KEY=sk-... cargo run -- --provider anthropic
```

Or trigger an evolution session manually:

```bash
# OpenRouter
OPENROUTER_API_KEY=sk-or-... MODEL=google/gemini-2.5-flash ./scripts/evolve.sh

# Anthropic
PROVIDER=anthropic ANTHROPIC_API_KEY=sk-... ./scripts/evolve.sh
```

## Architecture

```
src/main.rs              The entire agent (~400 lines of Rust)
src/provider.rs          Local LLM / OpenRouter provider wrapper
scripts/evolve.sh        Evolution pipeline
skills/                  Skill definitions (self-assess, evolve, communicate, research)
IDENTITY.md              Agent constitution (immutable)
JOURNAL.md               Session log (append-only)
DAY_COUNT                Current evolution day
```

## Built On

[yoagent](https://github.com/yologdev/yoagent) — minimal agent loop in Rust. The library that makes this possible.

## License

[MIT](LICENSE)
