# cline/cline

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c1c0b55ca03a @ ebde58e88eff80d7

## Summary (orientation draft, not independently verified)

Cline is a multi-surface coding agent (CLI, VS Code extension, JetBrains plugin, desktop app, SDK) documented in README and docs pages covering configuration layout, skills, command permissions, and API authentication. Evidence is documentation-only; no code-level or evaluation evidence appears in the shown slices. Evidence coverage: 168 of 219 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 120 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository ships several products: an SDK, a CLI, a VS Code extension, a native macOS/Windows desktop app (Tauri shell, Bun sidecar, Next.js UI), and docs; the JetBrains plugin is not open-sourced. -- evidence: [README.md#L125-L132](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L125-L132)
- design-choices (1 claim(s)):
  - [observation/documented] Cline offers Plan and Act modes: Plan mode explores the codebase and proposes a strategy, Act mode executes, and every file edit and terminal command requires user approval unless auto-approve is toggled. -- evidence: [README.md#L144-L144](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L144-L144)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to start with the Contributing Guide (CONTRIBUTING.md) and join the #contributors Discord channel. -- evidence: [README.md#L231-L231](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L231-L231)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are modular instruction sets loaded on demand (unlike always-active rules): metadata loads at startup (~100 tokens), full SKILL.md instructions load when triggered via the use_skill tool or slash commands, and resources load as needed. -- evidence: [docs/customization/skills.mdx#L25-L25](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L25-L25), [docs/customization/skills.mdx#L9-L9](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L9-L9), [docs/customization/skills.mdx#L19-L23](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L19-L23), [docs/customization/skills.mdx#L31-L33](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L31-L33), [docs/customization/skills.mdx#L7-L7](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L7-L7)
  - [observation/documented] A skill is a directory containing a required SKILL.md with YAML frontmatter (name matching the directory, description up to 1024 chars), optionally with docs/ and scripts/ subdirectories; skills are discovered from .cline/skills/ or ~/.cline/skills/. -- evidence: [docs/customization/skills.mdx#L39-L39](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L39-L39), [docs/customization/skills.mdx#L89-L89](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L89-L89), [docs/customization/skills.mdx#L68-L70](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L68-L70), [docs/customization/skills.mdx#L41-L48](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/customization/skills.mdx#L41-L48)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI installs via `npm i -g cline` and supports interactive chat or fully headless mode for CI/CD and scripting, including JSON output and piped input. -- evidence: [README.md#L221-L221](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L221-L221), [README.md#L50-L52](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L50-L52), [README.md#L46-L48](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L46-L48), [README.md#L223-L227](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/README.md#L223-L227)
  - [observation/documented] The Cline API requires a Bearer token in the Authorization header, with two auth methods: API keys created in the web dashboard and account auth tokens generated automatically on sign-in. -- evidence: [docs/api/authentication.mdx#L60-L60](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/api/authentication.mdx#L60-L60), [docs/api/authentication.mdx#L7-L7](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/api/authentication.mdx#L7-L7), [docs/api/authentication.mdx#L13-L16](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/api/authentication.mdx#L13-L16)
- memory-state (2 claim(s)):
  - [observation/documented] Configuration lives in two scopes: global `~/.cline/` (with data/settings, teams, sessions, SQLite databases, workflows, rules, hooks, skills, agents, plugins, cron) and per-workspace `.cline/`; a custom directory can be set via CLINE_DATA_DIR. -- evidence: [docs/getting-started/config.mdx#L9-L10](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L9-L10), [docs/getting-started/config.mdx#L109-L117](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L109-L117), [docs/getting-started/config.mdx#L16-L33](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L16-L33), [docs/getting-started/config.mdx#L96-L99](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L96-L99), [docs/getting-started/config.mdx#L47-L55](https://github.com/cline/cline/blob/c1c0b55ca03a4cd1d1eff2f64449445f778be4c4/docs/getting-started/config.mdx#L47-L55)
More evidence: [full detail](cline.detail.md)

Metadata and full claim list: [full detail](cline.detail.md)
Human notes ([notes](cline.notes.md), never overwritten by build)

[Back to map index](../../index.md)
