# Environment Variables

This document is the source of truth for runtime environment variables in Formax.

It only owns env-variable names and classification. Runtime config merge precedence, `/config` persistence,
and setting side effects are defined in `docs/contracts/config-settings-contract.md`.

## Public (user-facing)

These are intended for normal user configuration.

### LLM and auth

- `FORMAX_API_KEY`: API key (overrides `auth.json`)
- `FORMAX_BASE_URL`: base URL (normalized to include `/v1` for Anthropic-compatible providers)
- `FORMAX_TIMEOUT_MS`: request timeout in milliseconds

### Model tier mapping

- `ANTHROPIC_DEFAULT_HAIKU_MODEL`: override model id for `haiku`
- `ANTHROPIC_DEFAULT_SONNET_MODEL`: override model id for `sonnet`
- `ANTHROPIC_DEFAULT_OPUS_MODEL`: override model id for `opus`

### Config and path overrides

- `FORMAX_CONFIG_DIR`: global config directory override
- `FORMAX_LOGS_DIR`: logs directory override
- `FORMAX_SUBAGENTS_DIR`: sub-agents directory override
- `FORMAX_PLAN_DIR`: plan directory override

### Setup and session controls

- `FORMAX_SESSION_SAVE`: enable/disable session save (default enabled; `0|false|no` disables)
- `FORMAX_TUI_SHOW_INTERNAL_TOOLS`: show internal tool rows in TUI (`ToolSearch` etc.); default hidden
- `FORMAX_ALLOWED_TOOLS`: optional comma-separated allowlist for tools exposed to LLM requests (for example `Read,Edit,Bash`)
- `FORMAX_DISABLED_TOOLS`: optional comma-separated denylist for tools removed from LLM request exposure (applied after allowlist)

### Config-by-env patch keys (advanced)

These map to config fields in `packages/core/src/config/settings/resolve.ts`.

- `FORMAX_ASSISTANT_TEXT_MODE`
- `FORMAX_SHOW_CONTEXT_METER`
- `FORMAX_SHOW_AUTO_COMPACT_NOTICE`
- `FORMAX_CONTEXT_WINDOW_TOKENS`
- `FORMAX_EFFECTIVE_CONTEXT_WINDOW_PERCENT`
- `FORMAX_AUTO_COMPACT_TOKEN_LIMIT_PERCENT`
- `FORMAX_BASELINE_TOKENS`
- `FORMAX_COMPACT_KEEP_LAST_TURNS`
- `FORMAX_AUTO_COMPACT_MIN_TURNS_BETWEEN_RUNS`

## Internal / debug / compatibility

These are used by development, diagnostics, or legacy paths and are not a stable public API.

- `FORMAX_HOOKS_DEBUG`
- `FORMAX_DISABLE_HOOKS`
- `FORMAX_FORCE_INK_STATIC`
- `FORMAX_TODOS_PATH`
- `FORMAX_TODOS_SESSION_ID`
- `FORMAX_VITEST_SESSION_CONFIG_DIR` (test-only session storage root override; used by Vitest setup to keep session writes out of `~/.formax`)
- `FORMAX_SKILL_BODY_CHAR_BUDGET`
- `FORMAX_SKILL_TOOL_CHAR_BUDGET`
- `FORMAX_SKILL_STORE_CACHE_TTL_MS`
- `FORMAX_DEFERRED_TOOL_EXPOSURE` (enable REPL deferred tool exposure mode; default disabled)
- `FORMAX_DEFERRED_TOOL_SOFT_FALLBACK` (when deferred exposure is active, auto-load direct deferred tool calls via internal `select:<tool>` fallback; default enabled)
- `FORMAX_TOOLSEARCH_ENGINE` (optional deferred ToolSearch engine for plain queries: `bm25` [default], `regex`, `keyword`, `hybrid`; per-query prefixes like `regex:` and `bm25:` still override)
- `FORMAX_REQUEST_DRY_RUN` (construct request payload only, dump to file, skip real network request)
- `FORMAX_REQUEST_DRY_RUN_DIR` (optional output directory for dry-run request payload dumps; defaults to `<cwd>/proxy/request-dry-run`)
- `CACHE_EDITING_BETA_HEADER` (Anthropic first-party cache editing beta header, mirroring Claude Code's `CACHE_EDITING_BETA_HEADER`; enables request-only `cache_reference` / `cache_edits` projection when `llm.provider=anthropic` and `llm.baseUrl` points at `api.anthropic.com`; also enables the main-thread Claude Code-style cold-cache time-based microcompact gate. When this capability is unavailable, Formax keeps microcompact no-op instead of applying legacy content-stub fallback.)
- `FORMAX_WEBFETCH_MODEL`
- `FORMAX_WEBFETCH_MAX_TOKENS`
- `FORMAX_WEBFETCH_MAX_INPUT_CHARS`
- `FORMAX_PROJECT_DIR` (injected by hooks runtime)
