# Autoresearch: continue-decompose-web-app-shell-toward-500-lines

## Objective
Drive `runtime/web/src/app.ts` toward a thin orchestration entrypoint by extracting coherent behavior domains (not micro line shaves) while preserving UX semantics and payload shapes.

This tranche prioritizes higher-leverage seams still remaining in `app.ts`:
1. **Boot/load orchestration** (initial load and refresh loops)
2. **Branch/pane lifecycle coordination** (chat branch navigation + pane popout lifecycle)
3. **Timeline/status refresh orchestration glue** (view-driven timeline load flow)
4. **Top-level composition helpers** (render-mode routing and grouped shell wiring)
5. **Reusable shell utilities** (shared normalization/dedupe helpers removing repeated inline logic)

## Metrics
- **Primary**: `app_ts_lines` (lines, lower is better)
- **Secondary**:
  - `focused_web_tests_ms` (ms, lower is better)
  - `largest_extracted_module_lines` (lines, lower is better)
  - `number_of_coherent_modules` (count, higher is better)

## How to Run
- `./autoresearch.sh` — runs focused seam tests and emits structured `METRIC` lines.
- `./autoresearch.checks.sh` — runs `build:web`, `lint`, `typecheck`, and `check:stale-dist`.

## Files in Scope
- `runtime/web/src/app.ts`
- `runtime/web/src/ui/app-*.ts` (new or existing typed shell orchestration/util files)
- `runtime/test/web/app-*.test.ts` for new extracted seams

## Off Limits
- Backend/runtime protocol behavior changes
- Login/auth service behavior
- Payload contract changes for existing UI APIs/events

## Constraints
- No new dependencies
- Avoid creating any replacement god module
- Prefer multiple bounded domain modules
- Extracted modules should stay reasonably bounded (target < 600-800 LOC)
- Preserve UX behavior and payload shapes
- Keep focused tests green and pass: `build:web`, `lint`, `typecheck`, `check:stale-dist`

## What's Been Tried
- Previous tranches already extracted many shell seams (`app-branch-actions`, `app-window-actions`, `app-status-refresh-orchestration`, `app-sse-events`, `app-main-shell-render`, etc.), but `app.ts` still carries several orchestration-heavy clusters.
- Current tranche will explicitly target behavior-level decomposition (boot/load + branch/pane + composition + shared shell utilities) instead of helper-only nibbling.
