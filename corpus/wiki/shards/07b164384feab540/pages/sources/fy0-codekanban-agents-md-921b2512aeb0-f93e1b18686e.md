---
access: public
aliases: []
claim_ids:
- clm_0b402342f6cec69795671d5e66648fb4eba73d9ef73a80a974820f30503a9fc0
- clm_1e1a5bc784f709a9ed934f338d4090c82bb872ea5422b5eb70351da3d1452c69
- clm_da32ec4f2d002431a13b0b82b6ce1e135c8be3acb40d80f535b496bc705f8626
maturity: draft
page_id: pg_96e74f9dba8a514cb64ef93e1b18686e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8a8ec24f4bb856b18c09c3435b47f350
title: fy0/CodeKanban/AGENTS.md @ 921b2512aeb0
updated_at: '2026-09-14T02:01:10Z'
---

# fy0/CodeKanban/AGENTS.md @ 921b2512aeb0

<!-- rcw:begin owner=source:src_8a8ec24f4bb856b18c09c3435b47f350 block=evidence -->
- Repository development practice: commits use imperative mood with issue references in the footer; PRs should describe changes, note config.yaml toggles, and include screenshots or cURL snippets when API responses change. [@claim:clm_0b402342f6cec69795671d5e66648fb4eba73d9ef73a80a974820f30503a9fc0]
- Repository development practice: AGENTS.md instructs contributors to run `go test ./...` (optionally with -race), regenerate SQLC before committing schema changes, and run `go vet ./...` during review. [@claim:clm_1e1a5bc784f709a9ed934f338d4090c82bb872ea5422b5eb70351da3d1452c69]
- Repository development practice: contributors must format with gofmt, group imports with goimports, use PascalCase/camelCase naming, and write structured zap log fields instead of printf-style strings. [@claim:clm_da32ec4f2d002431a13b0b82b6ce1e135c8be3acb40d80f535b496bc705f8626]
<!-- rcw:end owner=source:src_8a8ec24f4bb856b18c09c3435b47f350 block=evidence -->

## Researcher notes

