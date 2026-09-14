# Changelog

All notable changes to momo Code are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-06-16

### Added

- **Experience Fast Loop** (`/evolve`) — Knowledge Embedding Protocol (KEP) for second-level learning
  - Tactic model with Beta(α, β) distribution tracking
  - Thompson sampling and UCB1 selection strategies
  - Signal pattern matching from session trajectories
  - Prompt injection with token budget management
  - Solidify step for verdict feedback
  - Promotion gate with A/B benchmark + ratchet check
  - Two-speed bridge: promoted tactics → fine-tune curriculum
  - Safety guardrails (command whitelist, stagnation detection, PII scrubbing)
  - Append-only ledger (JSONL) for auditability
- **Weight Slow Loop** (`/fine-tune`) — Monte Carlo Graph Search (MCGS) training pipeline
  - Signal mining from session trajectories
  - Curriculum synthesis (Gold/Hard-negative/Replay slices)
  - MCGS exploration (EXPAND/SCORE/FUSE/PRUNE)
  - LoRA fine-tuning integration
  - Ratchet gate for monotonic improvement
  - Model registry with promote/rollback
- **CLI Command System** — `momo /evolve`, `momo /fine-tune`, `momo models`, `momo help`
- **53 TypeScript modules** across provider / evolve / experience / cli layers
- **Dual-speed evolution architecture** — experience (seconds) + weights (hours)

### Changed

- Product name: kqq Code → **momo Code**
- `bin/momo`: Rewritten from CJS to ESM command router
- `package.json`: Production-ready configuration (exports, files, engines, keywords)
- README: Complete rewrite with /evolve documentation and architecture diagrams

## [0.1.0] - 2026-06-15

### Added

- Initial momo Code implementation
- 19 LLM provider integrations (Claude, GPT-4, Gemini, OpenRouter, Groq, Mistral, etc.)
- Model tiers (ultra / standard / lite)
- Claude Code interoperability (.claude/ config inheritance, MCP servers, prompts)
- SSE streaming with 8-minute chunk timeout watchdog
- Auth system with provider credential management
- Configuration system (JSONC with schema)
- Prompt routing with multi-model support
- Effect-powered architecture
