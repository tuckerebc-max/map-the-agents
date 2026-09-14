# Extension-Ci-Tools (`extension-ci-tools`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: duckdb
- License: unknown
- Language: YAML, Shell, Makefile
- Interface: install=N/A - referenced by DuckDB extension repositories, not a standalone installable package
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [duckdb/extension-ci-tools](../../repos/duckdb/extension-ci-tools.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Reusable CI/CD components (GitHub Actions workflows, Docker configs, makefiles, scripts, vcpkg ports) for building, testing, and deploying DuckDB extensions across multiple DuckDB versions and platforms.

(captured site page body (agents/extension-ci-tools.md), not a verified repo-code finding)
Building a DuckDB extension means compiling against multiple DuckDB versions across Linux, macOS, and Windows with matching toolchains — a configuration burden that used to be duplicated in every extension repository and drifted out of sync with DuckDB's own build changes. extension-ci-tools centralizes that into reusable GitHub Actions workflows, Docker configurations, Makefiles, build scripts, and vcpkg ports that the DuckDB Extension Template and downstream extension repos consume by reference. Versioned branches (v1.4.x, v1.5.x) track DuckDB releases, with the latest two versions actively maintained and older branches retired on a schedule. Its users are DuckDB extension authors; the repository contains no AI or agent functionality whatsoever.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/extension-ci-tools.md)
