# Pre-commit Setup Guide

This repository uses pre-commit hooks to automatically format code on every commit.

## Formatters Used

- **Ruff**: Fast Python linter and formatter (replaces Black, isort, and flake8)
- **Prettier**: Code formatter for JavaScript, TypeScript, JSON, YAML, and Markdown

## Initial Setup

1. **Install dependencies** (if not already installed):

   ```bash
   pip install -r requirements-dev.txt
   ```

   Or install individually:

   ```bash
   pip install pre-commit ruff
   ```

2. **Install pre-commit hooks**:

   ```bash
   pre-commit install
   ```

   This will set up the git hooks to run automatically on every commit.

3. **Optional: Run on all files** (to format existing code):
   ```bash
   pre-commit run --all-files
   ```

## How It Works

Once installed, pre-commit will automatically:

- Format Python code with Ruff before each commit
- Format JavaScript/TypeScript/JSON/YAML/Markdown files with Prettier
- Check for trailing whitespace, end-of-file issues, and other common problems
- Prevent committing if there are formatting issues

## Manual Usage

You can also run the formatters manually:

```bash
# Run all hooks on staged files
pre-commit run

# Run all hooks on all files
pre-commit run --all-files

# Run a specific hook
pre-commit run ruff --all-files
pre-commit run prettier --all-files
```

## Configuration Files

- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `pyproject.toml`: Ruff configuration (Python formatting and linting)
- `.prettierrc`: Prettier configuration (JavaScript/TypeScript formatting)
- `.prettierignore`: Files to exclude from Prettier formatting

## Updating Hooks

To update pre-commit hooks to their latest versions:

```bash
pre-commit autoupdate
```

## Troubleshooting

If hooks fail, you can:

1. **Skip hooks for a specific commit** (not recommended):

   ```bash
   git commit --no-verify
   ```

2. **Update hook versions**:

   ```bash
   pre-commit autoupdate
   ```

3. **Clear pre-commit cache**:
   ```bash
   pre-commit clean
   ```
