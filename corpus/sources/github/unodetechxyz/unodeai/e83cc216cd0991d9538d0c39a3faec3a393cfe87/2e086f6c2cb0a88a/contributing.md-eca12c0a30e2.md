# Contributing to UnodeAi

Thanks for your interest! UnodeAi is a VS Code extension that runs an
orchestrated, **verified** team of AI coding agents on top of a cheap
OpenAI-compatible gateway (or Anthropic / any OpenAI-compatible endpoint).

## Prerequisites

- **Node.js 18+** and npm
- **VS Code 1.93+** (the `engines.vscode` floor)
- **git** on PATH (worktree fan-out and the merge orchestrator shell out to it)
- Optional: the `claude` CLI on PATH if you work on the Claude headless backend

## Getting started

```bash
git clone https://github.com/UnodeTechxyz/unodeai
cd unodeai
npm install
npm run build      # tsc -p ./
```

Press **F5** in VS Code to launch the Extension Development Host.

## The gates (run these before opening a PR)

```bash
npm run build      # tsc — must be clean (no errors)
npm run lint       # eslint src --ext ts
npm test           # vitest run — keep it green
npm run package    # vsce package — sanity-check the VSIX builds
```

E2E (optional, slower): `npm run test:e2e`.

All four core gates must pass. New behavior needs tests; bug fixes should add a
regression test that fails before the fix.

## House rules

- **Match the surrounding code.** Naming, comment density, and idiom should read
  like the file you're editing.
- **Don't weaken tests to make them pass.** Fix the code. The verifier-as-gate
  exists precisely to catch "passing by editing the test."
- **Verify audit/review findings against the code before acting.** Automated
  reviews (including from other AI agents) carry false positives — confirm first.
- **Keep the worker-compliance protocol honest:** re-read before claiming
  "already done"; small, verifiable steps.
- **Secrets:** never commit real keys. MCP configs use `${VAR}` placeholders.
  `.roam/` is gitignored — runtime artifacts (worktrees, the Claude MCP bridge
  config) live there.

## Commits & PRs

- Conventional-commit style subjects are appreciated (`feat(chat): …`,
  `fix(tools): …`, `docs: …`, `chore(release): …`).
- Keep PRs focused; describe what changed and how you verified it.
- Update `CHANGELOG.md`, and — for any user-visible change — `USAGE.md` and
  `docs/wiki/index.html` (these ship to users on each release).

### Documentation currency

Any PR that changes a user-visible control, label, default, block rule, or command must update `USAGE.md`
and `docs/wiki/index.html` in the same PR. The documentation gates verify source-backed UI facts and version
stamps; review rejects a UX change whose manual/wiki update is absent.

## Reporting bugs / proposing features

Open a GitHub issue with repro steps, your OS / VS Code version, and the
extension version. For **security** issues, see [SECURITY.md](SECURITY.md) —
do not file a public issue.
