# Repository Guidelines

## AGENTS Scope

- Keep high-frequency operational guidance here (review workflow/profile, commonly used commands/scripts, commit workflow, and day-to-day guardrails).
- Keep canonical product/runtime semantics in `docs/contracts/*` and related canonical docs.
- Keep code navigation in `CODEMAP.md` ("where to change what"), with AGENTS linking to it instead of duplicating path-level maps.

## Project Structure & Module Organization

- `packages/core/src/` contains TypeScript source.
  - `entrypoints/` CLI/runtime entrypoints (for example `cli.tsx`).
  - `runtime/cli/` argument parsing + command dispatch for the CLI wrapper.
  - `runtime/bootstrap/` REPL bootstrap + runtime assembly wiring.
  - `core/` productized app core (config resolution, setup flows, boundaries checks).
  - `tui/` Ink “wizard” UIs (first-run setup, selectors, forms).
  - `adapters/` filesystem + setup adapters (config files, setup persistence).
  - `screens/` Ink screens; `components/` reusable UI.
  - `tools/` tool registry, modules, handlers, presenters, runtime managers.
  - `streaming/` Anthropic streaming client and parsers.
  - `features/subagents/` registry/runner for sub-agent tools.
  - `prompts/`, `config/`, `services/`, `shared/utils/` supporting code.
- `packages/` contains companion workspaces. Package-local implementation details belong to each package `AGENTS.md`.
- Tests live next to source as `*.test.ts`/`*.test.tsx`.
- `docs/` holds architecture notes and guides; `plans/` captures refactor plans.
- `proxy/` contains proxy/logger scripts plus traffic/log artifacts used for parity/reference during development.
- `CODEMAP.md` is the “where to change what” index (entrypoints, main loop, tools, plan mode, sub-tasks).

## Build, Test, and Development Commands

- `bun install` installs dependencies.
- `bun run dev` runs the CLI via `tsx` (entry: `packages/core/src/entrypoints/cli.tsx`).
- `bun run app-server:bridge -- --host 127.0.0.1 --port 3777` runs the app-server WebSocket bridge for web client development.
- `bun run build` bundles the CLI to `dist/cli.js` (requires Bun).
- `bun run type-check` runs TypeScript checks + boundary checks (`core` + `ui`).
- `bun run check:root-script-governance` enforces root `package.json` script governance (orchestration-only, no feature alias uplift).
- `bun run ui:boundaries` runs UI boundary checks (guards `packages/core/src/tui/`, `packages/core/src/screens/`, `packages/core/src/components/` from importing forbidden layers).
- `bun run test` runs `vitest run`; `bun run test:watch` runs Vitest watch.
- Single test: `bun run test -- packages/core/src/tools/registry.test.ts`.
- Package-specific commands (web/desktop/shared/semantics) live in each package `AGENTS.md`.

## Coding Style & Naming Conventions

- TypeScript ESM (`"type": "module"`, bundler module resolution).
- Tool modules follow `packages/core/src/tools/modules/<name>/{index,handler,presenter}.ts(x)` and `createXToolModule` factory naming.
- Root script governance: keep feature/package workflows in owning package scripts; root scripts are orchestration-level only (see `docs/contracts/root-script-governance-contract.md`).
- **GLOBAL CLARIFICATION RULE (MANDATORY)**: In ANY task, if user intent is ambiguous (UI, behavior, scope, risk, tradeoff, or acceptance criteria), you MUST ask the user BEFORE making directional choices. DO NOT infer beyond explicit requirements.
- **QUESTION TOOL RULE (MANDATORY)**: When clarification is needed, you MUST use the user-input question tool first (e.g. `request_user_input`) when available. If that tool is unavailable in the current mode, you MUST ask the user directly in chat instead of guessing.

## Testing Guidelines

- Framework: Vitest; Ink UI tests use `ink-testing-library`.
- Property-based tests use `fast-check` where appropriate.
- Keep tests colocated with source and use `*.test.ts`/`*.test.tsx`.
- **Coverage mindset**: Prioritize adding/strengthening tests when behavior is user-visible or stability-critical (tools, permissions, hooks, REPL input, UI flows). Avoid “happy-path only” tests—cover edge cases and regressions you’ve already seen.
- **Refactor safety**: Before refactoring, add/extend tests to lock current behavior. Do not rely on “tests pass” if manual behavior regresses.
- **Code review (mandatory in loops)**: After tests pass, run review using the **Review Profile (Single Source of Truth)** below before committing; fix all high/medium findings (and any low-risk issues that are clearly correct and low-churn).
- **REPL semantics pre-review gate**: For `packages/core/src/features/repl/**` semantic-flow changes, run `bun run test:repl-semantic-gate` before `codex review`.

### Review Profile (Single Source of Truth)

- Review command: `codex review --uncommitted -c model="gpt-5.4" -c model_reasoning_effort="medium" -c service_tier="fast"`
- Tool-call timeout for review: `timeout_ms >= 1200000`
- Review output artifact path (preferred): `.tmp/codex-review-result/`
- Preferred local wrapper when running review manually or from agents:
  - `mkdir -p .tmp/codex-review-result`
  - `codex review --uncommitted -c model="gpt-5.4" -c model_reasoning_effort="medium" -c service_tier="fast" > .tmp/codex-review-result/review-latest.txt 2>&1`
  - Then inspect the saved output with a full-file finding/no-finding search instead of relying on the last lines:
    - `rg -n "Review comment:|Finding|findings|P0|P1|P2|P3|actionable|bug|regression|issue|I did not find|I did not identify" .tmp/codex-review-result/review-latest.txt`
  - If extra surrounding context is needed after the `rg` scan, use a local `sed`/`tail` view around the relevant line numbers; do not treat a fixed tail length as sufficient.
- Goal: keep mandatory review behavior unchanged while reducing noisy stdout/stderr in the active agent context.
- Apply this profile everywhere (skills/plans/docs). Do not redefine model/reasoning/timeout in other files.

## Refactor Guardrails (Important)

- **Refactor != rewrite**: refactors must preserve existing functionality and user-visible behavior; do not add/remove features as a side-effect.
- **Tests are not the spec**: before refactoring, first check whether missing/weak tests can be added to lock current behavior; use those tests to validate the refactor.
- **UI parity**: UI refactors must keep layout/spacing/keys/interaction the same unless the user explicitly requests a UI change; do not “improve” UI by default.
- **When uncertain**: if expectations are unclear (not limited to UI), ask the user before changing behavior.
- **Root-cause first (mandatory)**: do not default to patch/stopgap fixes for systemic bugs (state ownership, ordering, lifecycle, data flow). First identify and fix the root cause in the canonical layer.
- **Shared-utility and schema-safety rule (mandatory)**: prefer shared utilities over hand-rolled helpers to keep invariants centralized; do not probe data YOLO-style. Validate boundaries or rely on typed SDK/contracts before coding against a shape.
- **Stopgap policy (strict)**: if a temporary mitigation is unavoidable, explicitly mark it as temporary in code comments and PR/commit notes, define removal conditions, and create a follow-up task in the same iteration. Do not leave silent long-term stopgaps.
- **UI refactor workflow (mandatory)**:
  - Before refactor: write/extend `ink-testing-library` tests that lock the current UI text + key paths (Enter/Esc/Tab/↑↓/←→/Backspace).
  - During refactor: do not change copy/spacing/colors unless explicitly requested; treat “simplifying UI” as a behavior change.
  - After refactor: run the targeted UI test file(s) + do a quick manual spot-check in `bun run dev` for the overlay(s) you touched.
- **No “test-only” refactors**: a passing test suite is not sufficient if manual UI behavior regresses; prioritize user-visible parity over internal cleanup.

## Tool Contract Checks

If you modify tool specs/contracts or tool module coverage, consider running:

- `bun run tools:parity`
- `bun run tools:coverage`

## Commit & Pull Request Guidelines

- Commits follow Conventional Commit style in history: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:` with optional scope (`refactor(chat): ...`).
- Avoid placeholder messages like `tmp`; keep summaries imperative and specific.
- PRs should include a concise description, link relevant issues/plans, list tests run, and add terminal screenshots for Ink UI changes.
- **Commit workflow (when user says “commit”)**: assume the user already ran `git add`. Do:
  - `git status --short` and `git diff --cached` (or `git diff --cached --stat`)
  - Generate a Conventional Commit message: `type(scope): summary` (≤72 chars, imperative)
  - Run `git commit -m "<message>"`

## Documentation Hygiene

- Treat `CODEMAP.md` as the "where to change what" index; update it when key entrypoints or ownership move.
- Canonical docs map: `docs/index.md`
- Semantics source of truth: `docs/contracts/semantics-contract.md`
- Interactive input source of truth: `docs/contracts/interactive-input-contract.md`
- Permissions/policy source of truth: `docs/contracts/permissions-policy-contract.md`
- Transcript surface source of truth: `docs/contracts/transcript-surface-contract.md`
- Prompt/tool exposure source of truth: `docs/contracts/prompt-tool-exposure-contract.md`
- Context strategy stack source of truth: `docs/contracts/context-strategy-stack-contract.md`
- Tool runtime / ToolSearch source of truth: `docs/contracts/tool-runtime-contract.md`
- Hooks source of truth: `docs/contracts/hooks-contract.md`
- Session persistence / resume source of truth: `docs/contracts/session-persistence-contract.md`
- Web parity adapter / reducer source of truth: `docs/contracts/web-parity-adapter-contract.md`
- Slash command source of truth: `docs/contracts/slash-command-contract.md`
- Config settings source of truth: `docs/contracts/config-settings-contract.md`
- Root script governance source of truth: `docs/contracts/root-script-governance-contract.md`
- Runtime env-variable reference: `docs/environment-variables.md`
- Verification and failure-recovery path: `docs/runbooks/runbook.md`
- **CODEMAP update triggers**: If you (a) add a new entrypoint/wiring point, (b) extract a cross-cutting helper used by multiple subsystems (e.g. audit/logging), or (c) move/rename user-facing UI/tool files, update `CODEMAP.md` in the same commit.
- When semantics or interactive input behavior changes, update the canonical contract first, then update linked summaries/references.
- When permissions, remember side effects, or workspace approval behavior changes, update the permissions/policy contract first.
- When `/clear` `/resume` transcript remount, Ctrl+O/Ctrl+E view reset, or legacy terminal clear behavior changes, update the transcript surface contract first.
- When deferred tool exposure, skills reminder, or request dry-run behavior changes, update the prompt/tool exposure contract first.
- When query-time middle-layer stage order, stage roles, request-only projection scope, or terminal prune fallback behavior changes, update the context strategy stack contract first.
- When tool protocol shape, executor gate order, ToolSearch runtime, or ToolResult vs CommandResult boundaries change, update the tool runtime contract first.
- When hook events, matcher semantics, or `additionalContext` injection behavior changes, update the hooks contract first.
- When session persistence roots, `query(...).resume/continue`, `unstable_v2_resumeSession`, `thread/start` provisional-file behavior, or `thread/resume` stale-input recovery changes, update the session persistence contract first.
- When Web history adapters, reducer/projection baselines, active-thread canonical gating, or `turnEventCursor` ordering behavior changes, update the web parity adapter contract first.
- When slash command discovery, overlay-dismiss sublines, command dispatch precedence, or next-turn injection behavior changes, update the slash command contract first.
- When config merge precedence, `/config` persistence targets, or output-style / thinking-mode / verbose-output behavior changes, update the config settings contract first.
- When root `package.json` script admission policy, exception registration, or script-governance gate behavior changes, update the root script governance contract first.
- When only env-variable names or user-facing classification changes, update `docs/environment-variables.md`.
- When you ship a behavior-alignment change, add/update a short learning note under `docs/learnings/` so mapping decisions remain traceable.
- For complex subsystems with repo-local deep dives, keep the local README aligned when you move boundaries, control flow, invariants, or extension points:
  - `packages/core/src/tools/README.md`
  - `packages/core/src/core/README.md`
  - `packages/core/src/streaming/README.md`
  - `packages/core/src/features/subagents/README.md`
- Keep repo-local deep-dive READMEs aligned with their canonical docs; do not let them become a second source of truth.
- Prefer linking to source files over duplicating code; keep diagrams high-level to reduce churn.

## Configuration & Runtime Notes

- Runtime config entrypoint: `packages/core/src/config/config.ts`
- Runtime config still merges env vars, global config under `FORMAX_CONFIG_DIR` (default `~/.formax/`), and per-project overrides under `<repo>/.formax/`.
- Key env families to remember:
  - LLM/auth: `FORMAX_API_KEY`, `FORMAX_BASE_URL`, `FORMAX_TIMEOUT_MS`
  - Model mapping: `ANTHROPIC_DEFAULT_HAIKU_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`
  - Paths: `FORMAX_CONFIG_DIR`, `FORMAX_LOGS_DIR`, `FORMAX_SUBAGENTS_DIR`, `FORMAX_PLAN_DIR`
- Full environment-variable and config classification reference: `docs/environment-variables.md`

## Security & Config Tips

- Do not commit secrets. Local config uses `.env` (e.g., `FORMAX_API_KEY`); keep `.env` and traffic logs out of git.
- When sharing context with other AIs/tools, double-check exports for accidental secrets (API keys, tokens, cookies) before pasting.

## Pitfalls & Gotchas (Keep Updated)

- Record reproducible pitfalls under `docs/pitfalls/` and keep `docs/pitfalls/index.md` in sync when a deep-dive doc exists.
- If a pitfall changes day-to-day agent behavior, update `docs/pitfalls/` (and linked docs/skills) as the canonical location.
- Prefer linking to the existing pitfall doc or skill instead of duplicating the full troubleshooting narrative here.
- High-signal recurring pitfalls worth keeping in view:
  - Static-heavy surface fixes need real smoke validation; Vitest alone can miss duplicate-row / stale-surface regressions.
  - `/clear`, `/resume`, compact, and Ctrl+O/Ctrl+E paths must stay on the shared surface-reset transaction.
  - Keep Vitest session writes under `FORMAX_VITEST_SESSION_CONFIG_DIR`, not `~/.formax`.
  - For Anthropic fake-overload triage, separate main turns from auto-title traffic before debugging prompt headers or thinking signatures.

## Local Paths

- Avoid hardcoding machine-specific absolute paths in repo docs.
