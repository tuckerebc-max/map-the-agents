# Contributing

Thank you for your interest in contributing to Archon!

## Getting Started

1. Fork the repository
2. Clone your fork
3. Install dependencies: `bun install`
4. Copy `.env.example` to `.env` and configure
5. Start development: `bun run dev`

## Development Workflow

### Code Quality

Before submitting a PR, ensure:

```bash
bun run check:bundled  # Bundled defaults are up to date
bun run type-check     # TypeScript types
bun run lint           # ESLint
bun run format         # Prettier
bun run test           # All tests (per-package isolation)

# Or run the full validation suite:
bun run validate
```

**Schema changes**: `bun run validate` does not cover `migrations/000_combined.sql`
upgrades — that check needs a live PostgreSQL, so CI runs it as its own job. If you
touched the schema, run it yourself against any PostgreSQL:

```bash
bun run check:schema-upgrades   # PGHOST/PGUSER/… or DATABASE_URL
```

**SDLC workflows**: We do not accept pull requests that change
`.archon/workflows/sdlc/`. Open an issue instead and describe the problem or
change you want the maintainers to consider.

**Important:** Use `bun run test` (not `bun test` from the repo root) to avoid mock pollution across packages.

### Commit messages

Follow the repository's Conventional Commit style. Write a concise,
human-readable subject that explains the meaningful outcome. Commit subjects
may become changelog entries or pull request titles, so they must make sense
without the diff.

Use plain language and the repository's exact terms. Cut filler and vague verbs.
Do not present a mechanical change as a larger outcome. Treat Git history as
evidence of valid structure, not as the writing-quality standard.

Never add AI attribution, generated-by text, robot emoji, or
`Co-Authored-By: $Agent`.

**Bad:** `refactor(prp-pr): update skill instructions`

**Good:** `refactor(prp-pr): PR creation now uses one focused workflow`

### Pull requests

1. Create a feature branch from `dev`.
2. Keep the pull request focused on one coherent slice or concern. Split broad
   work into reviewable pull requests organized by product slices or concerns.
   Pull requests that combine too many concerns will be closed.
3. Ensure all checks pass.
4. Use the template at
   [`.github/pull_request_template.md`](./.github/pull_request_template.md).
   GitHub fills it in when you open a pull request through the Web UI. If you
   use `gh pr create`, copy the template into the body. Keep **Problem and
   outcome**, **Review guidance**, **Solution**, and **Validation**. Delete
   conditional sections that do not apply instead of filling them with "N/A".
   Bot-authored dependency pull requests (`renovate[bot]`) are exempt because
   Renovate generates the body.
5. Link the issue the pull request addresses with `Closes #<number>`,
   `Fixes #<number>`, or `Resolves #<number>` in the description. Pull requests
   without a linked issue will be closed.

Treat repository rules as syntax constraints, not as the writing-quality
standard. Write in plain, natural language. Use the repository's exact terms
and name concrete behavior and validation evidence. Cut filler, generic praise,
formulaic transitions, and vague claims.

#### Title

Write a concise, human-readable title that describes the meaningful outcome.
Follow the repository's Conventional Commit style, but do not copy vague or
implementation-focused titles from its history.

**Bad:** `feat(core): add child run traversal and parent event aggregation`

**Good:** `feat(core): workflows can now include a child workflow in the parent run`

#### Description

Preserve the pull request template's structure and fill every applicable section
with concrete information from the issue, diff, commits, and validation
evidence. Lead with the problem and outcome, not an implementation inventory.

## Code style

- Follow [`AGENTS.md`](./AGENTS.md) and
  [`.archon/engineering.md`](./.archon/engineering.md).
- TypeScript strict mode is enforced.
- All functions require explicit return types.
- Do not use `any` without justification.
- Follow existing patterns in the codebase.

Before proposing a major feature, read
[`.archon/direction.md`](./.archon/direction.md). Pull requests that conflict
with the documented product direction will be closed.

## Architecture

See [AGENTS.md](./AGENTS.md) for detailed architecture documentation.

## Contributing Workflows to the Marketplace

Share your Archon workflows with the community by adding an entry to the marketplace registry at [`packages/docs-web/src/data/marketplace.ts`](packages/docs-web/src/data/marketplace.ts).

### How to Submit

1. Keep your workflow in a **public GitHub repository** — either as a single YAML file or a directory
2. Pin it to a specific commit SHA (ensures immutability after merge)
3. Fork Archon and add an entry to `packages/docs-web/src/data/marketplace.ts`
4. Open a PR — automated lint validates your entry before review

### Submission Formats

**Single-file workflow** — a standalone `.yaml` file:

```
sourceUrl: "https://github.com/you/repo/blob/main/my-workflow.yaml"
```

**Directory workflow** — a folder containing the workflow YAML plus supporting commands, scripts, or skills:

```
sourceUrl: "https://github.com/you/repo/tree/main/my-workflow/"
```

Directory structure convention:

```
my-workflow/
├── README.md          # Describe what the workflow does and any prereqs a user needs to run it
├── my-workflow.yaml   # Main workflow (must match slug or be the only .yaml)
├── commands/          # → installed to .archon/commands/
│   └── helper.md
├── scripts/           # → installed to .archon/scripts/
│   └── analyze.ts
└── skills/            # → installed to .archon/skills/
    └── my-skill/
```

Use a directory when your workflow references custom commands, scripts, or other resources that users need locally.

### Entry Requirements

| Field | Requirement |
|-------|-------------|
| `slug` | Lowercase, hyphens only (e.g. `my-review-workflow`) — must be unique |
| `name` | Human-readable display name |
| `author` | Your GitHub username |
| `description` | 1–3 sentences: what it does and when to use it |
| `sourceUrl` | GitHub blob URL (single file) or tree URL (directory) |
| `sha` | Full 40-character commit SHA pinning the exact version |
| `tags` | At least one from: `development`, `review`, `automation`, `planning` |
| `archonVersionCompat` | Semver range (e.g. `>=0.3.0`) |

### Self-Attestation

By submitting, you attest that:

- [ ] The workflow does not exfiltrate data, credentials, or secrets
- [ ] The workflow does not execute destructive operations without user confirmation
- [ ] You have the right to share this workflow publicly
- [ ] The pinned SHA points to a reviewed, stable version of your workflow

## Questions?

Open an [issue](https://github.com/coleam00/Archon/issues) or start a [discussion](https://github.com/coleam00/Archon/discussions).
