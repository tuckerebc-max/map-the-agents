# Contributing to OpenRath

Thank you for helping improve OpenRath. This document matches the current repo layout and tool chain. For day-to-day work, treat contributions as **small, verifiable steps**: clarify scope, implement, then run the checks below before opening a pull request.

## Project goals (keep the core small)

- **Session-first**: chunk tables, loops, and sandbox backends should stay easy to reason about.
- **Composable APIs**: workflows and agent parameters should feel natural to combine (PyTorch-like ergonomics without copying PyTorch).
- **Focused changes**: avoid drive-by refactors and unrelated formatting in the same PR as a feature or fix.
- **Design before large moves**: session graph semantics, tool wiring, and major public surfaces deserve a short design note or issue thread before big diffs.

## Development environment

Requirements: **Python 3.10–3.13** (see `requires-python` in `pyproject.toml`).

We use **[uv](https://github.com/astral-sh/uv)** for environments.

```bash
# Runtime + dev tools (ruff, mypy, pytest)
uv sync --group dev
```

After cloning, initialize the documentation submodule if you did not use `--recurse-submodules`:

```bash
git submodule update --init --recursive
```

Optional groups:

```bash
# Editable install with OpenSandbox extras (for backend work)
uv sync --group dev --extra opensandbox

# Sphinx + extensions (for documentation edits)
uv sync --group dev --group docs
```

Run Python tools through `uv run …` so they use the synced environment.

## Verify before you push

These commands are what maintainers expect to pass on a typical PR (library code, tests, and **examples**):

```bash
uv run ruff check src tests example
uv run ruff format --check src tests example
uv run mypy src
uv run pytest
```

Notes:

- **`mypy`** is run on `src/` only (package API surface). If you change typing at boundaries, keep `src` clean.
- **`ruff check`** includes **`example/`**: scripts under `example/` are part of the reviewed surface.
- **`ruff format --check`** verifies formatting without modifying files; run `uv run ruff format src tests example` to apply fixes.
- **`pytest`** runs the full tree. Many tests run **offline**; some are **conditional** (see below).

### Optional / live test tiers

| Kind | When they run | What you need |
|------|----------------|---------------|
| **Default unit & conformance** | Always (unless skipped internally) | Nothing special |
| **`live_llm` / `integration`** | Skip if `OPENAI_API_KEY` is unset or very short | Valid `OPENAI_API_KEY`; sometimes `OPENAI_DEFAULT_MODEL` / base URL per test docstrings |
| **`opensandbox`** | Skip if no server on `localhost:8080` (configurable via `OPENSANDBOX_TEST_HOST` / `PORT`) | Running OpenSandbox stack; see `tests/conftest.py` and repo scripts under `scripts/` |

Do not commit secrets. Use environment variables or local-only config.

### Documentation build

If you change `docs/`, build HTML locally:

```bash
uv sync --group dev --group docs
uv run sphinx-build -M html docs/source docs/_build
```

Start a local HTTP server for the built docs:

```bash
uv run python -m http.server 8000 --directory docs/_build/html
```

Then preview them at `http://127.0.0.1:8000/`.

## Repository layout

```text
src/rath/          Installable package (wheel maps here via hatch)
tests/             pytest tree (unit, integration, conformance, examples checks)
example/           Runnable demos and CLI entry points (also ruff-clean)
assets/readme/     README and example-facing images (independent of docs submodule)
docs/              Sphinx + MyST sources (git submodule: OpenRath-Docs)
pyproject.toml     Metadata, dependencies, dependency groups
```

## Code and review checklist

1. **Scope**: One PR should solve one problem (or one tightly related cluster).
2. **Tests**: Add or update tests for behavior changes; keep fast tests deterministic without network when possible.
3. **Public behavior**: Update `README.md`, user-facing docstrings, or `docs/` when CLI or semantics change.
4. **Style**: Prefer clear names and short module docstrings over long inline chatter. Keep `pragma: no cover` lines purposeful and explained.
5. **Examples**: If you touch `example/`, run entry points mentally (or briefly) and ensure new env vars are documented in the relevant `README.md` there.

## Pull requests

- Describe **motivation**, **what changed**, and **how you verified** it (commands run).
- Link related issues when applicable.
- Call out **breaking changes**, **follow-ups**, or **known limitations** explicitly.

## License

By contributing, you agree your contributions are licensed under the **BSD 3-Clause License** in this repository (`LICENSE`).
