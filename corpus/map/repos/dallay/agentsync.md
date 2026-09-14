# dallay/agentsync

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7102a4d56da0 @ 5a41a0627fdde6f2

## Summary (orientation draft, not independently verified)

AgentSync is a Rust CLI (with an npm wrapper) that synchronizes AI agent configurations and MCP servers across multiple coding assistants using symlinks from a single .agents/ source of truth. Evidence covers its CLI, TOML configuration, target types, MCP generation, skills catalog, distribution channels, and a catalog E2E validation workflow. Evidence coverage: 188 of 391 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] AgentSync can generate MCP configuration files for Claude Code, GitHub Copilot, OpenAI Codex CLI, Gemini CLI, Cursor, VS Code, and OpenCode; under merge strategy, TOML-defined servers win conflicts while other existing servers are preserved. -- evidence: [README.md#L435-L444](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L435-L444), [README.md#L456-L459](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L456-L459), [README.md#L405-L406](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L405-L406)
  - [observation/documented] The repository is a monorepo containing a Rust core and CLI in src/, a TypeScript npm wrapper in npm/agentsync/, a Starlight documentation site, and integration tests in tests/. -- evidence: [README.md#L628-L628](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L628-L628), [README.md#L632-L635](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L632-L635)
- design-choices (3 claim(s)):
  - [observation/documented] AgentSync uses symlinks rather than copies so changes propagate instantly, and it automatically backs up existing files before replacing them. -- evidence: [README.md#L98-L105](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L98-L105)
  - [observation/documented] Configuration lives in a TOML file at .agents/agentsync.toml (the default lookup location), which defines the source of truth, gitignore handling, and per-assistant targets. -- evidence: [website/docs/src/content/docs/reference/configuration.mdx#L8-L8](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/website/docs/src/content/docs/reference/configuration.mdx#L8-L8), [website/docs/src/content/docs/reference/configuration.mdx#L10-L10](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/website/docs/src/content/docs/reference/configuration.mdx#L10-L10), [README.md#L366-L366](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L366-L366)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: a Catalog E2E GitHub Actions workflow validates that every skill entry can be resolved, installed, and registered; it runs manually and weekly (Mondays 08:00 UTC), and locally via RUN_E2E=1 cargo test with an agents-skills sibling checkout, kept out of normal CI because it depends on external networks. -- evidence: [README.md#L109-L110](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L109-L110), [README.md#L117-L121](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L117-L121), [README.md#L126-L127](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L126-L127), [README.md#L123-L124](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L123-L124), [README.md#L112-L115](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L112-L115)
- skills-patterns (1 claim(s)):
  - [observation/documented] AgentSync ships a curated skill catalog of 200+ skills across 110+ technologies, sourced from the dallay/agents-skills repository plus external providers such as Angular, Vercel, Cloudflare, Expo, and Stripe. -- evidence: [README.md#L608-L608](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L608-L608), [README.md#L610-L611](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L610-L611)
- interfaces (3 claim(s)):
  - [observation/documented] The apply command supports flags including --clean, --config, --dry-run, --no-gitignore, --agents (filtering), and --verbose, per documented usage examples. -- evidence: [README.md#L331-L331](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L331-L331), [README.md#L325-L325](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L325-L325), [README.md#L328-L328](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L328-L328), [README.md#L313-L313](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L313-L313), [README.md#L322-L322](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L322-L322), [README.md#L319-L319](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L319-L319)
  - [observation/documented] The status command accepts optional --project-root and --json flags, is sync-type aware (symlink vs symlink-contents), and exits 0 when no problems are found and 1 otherwise, described as CI-friendly. -- evidence: [README.md#L362-L362](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L362-L362), [README.md#L356-L356](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L356-L356), [README.md#L358-L360](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L358-L360), [README.md#L353-L354](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L353-L354), [README.md#L349-L351](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L349-L351)
- memory-state: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agentsync.detail.md)

Metadata and full claim list: [full detail](agentsync.detail.md)
Human notes ([notes](agentsync.notes.md), never overwritten by build)

[Back to map index](../../index.md)
