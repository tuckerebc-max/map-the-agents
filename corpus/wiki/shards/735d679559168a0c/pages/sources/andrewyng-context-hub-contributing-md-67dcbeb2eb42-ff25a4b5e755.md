---
access: public
aliases: []
claim_ids:
- clm_4495b0f0d6f599d45e2e0d2e66b278c7eee21af0e6c4c0d5c8b735ff6d35fd7d
- clm_75bada682e3c02b1d3c1799549b4228f0a4cee047384e838d16f3b98b2c01da5
- clm_7f8944ac89337ced4a0e703faf602ddc92fe82a7ababae91e71d35ca126df6b7
- clm_daa641780112880aa40395ed10bd7f94a67f5004ed2764a36028560de3a3a853
maturity: draft
page_id: pg_b70a474aeecf501885d9ff25a4b5e755
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_45045710554b52eea01c302b89fe2bde
title: andrewyng/context-hub/CONTRIBUTING.md @ 67dcbeb2eb42
updated_at: '2026-09-14T03:33:52Z'
---

# andrewyng/context-hub/CONTRIBUTING.md @ 67dcbeb2eb42

<!-- rcw:begin owner=source:src_45045710554b52eea01c302b89fe2bde block=evidence -->
- Repository development practice: code style mandates ES modules, no build step, minimal dependencies preferring Node built-ins, and every command supporting --json output. [@claim:clm_4495b0f0d6f599d45e2e0d2e66b278c7eee21af0e6c4c0d5c8b735ff6d35fd7d]
- Repository development practice: contributors fork from main, add/update tests, run 'cd cli && npm test', validate with 'chub build content/ --validate-only', then submit a pull request. [@claim:clm_75bada682e3c02b1d3c1799549b4228f0a4cee047384e838d16f3b98b2c01da5]
- Repository development practice: docs are contributed as <author>/docs/<name>/DOC.md with YAML frontmatter (name, description, languages, versions, tags, updated-on) and optional references/ files; skills follow a similar SKILL.md pattern. [@claim:clm_7f8944ac89337ced4a0e703faf602ddc92fe82a7ababae91e71d35ca126df6b7]
- Repository development practice: tests run via npm test, test:watch, and test:coverage inside the cli directory, using Vitest unit tests plus e2e/integration tests. [@claim:clm_daa641780112880aa40395ed10bd7f94a67f5004ed2764a36028560de3a3a853]
<!-- rcw:end owner=source:src_45045710554b52eea01c302b89fe2bde block=evidence -->

## Researcher notes

