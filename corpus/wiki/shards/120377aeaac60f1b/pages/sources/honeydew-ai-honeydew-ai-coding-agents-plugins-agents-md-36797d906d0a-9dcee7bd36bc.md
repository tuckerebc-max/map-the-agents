---
access: public
aliases: []
claim_ids:
- clm_92be926ba41044dd0a9a93026967b48c013cf07ab3be04e0a2f0c79b544c4ead
- clm_b8df81b2a76109e7eb7063c0052b95ca8c0fb7d932dc8c233d6044270f7f2365
- clm_dd1c51eed1e72df619f1676282df2f108f775b635f5a311ab01f9e4af6ecae64
maturity: draft
page_id: pg_7268eb06e49855b7beb19dcee7bd36bc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_14c9b28b473257c7878684bc5f7cf50a
title: honeydew-ai/honeydew-ai-coding-agents-plugins/AGENTS.md @ 36797d906d0a
updated_at: '2026-09-14T03:57:08Z'
---

# honeydew-ai/honeydew-ai-coding-agents-plugins/AGENTS.md @ 36797d906d0a

<!-- rcw:begin owner=source:src_14c9b28b473257c7878684bc5f7cf50a block=evidence -->
- Repository development practice: adding a new skill requires creating SKILL.md with YAML frontmatter, updating .cursor/skills symlinks, the GitHub Copilot plugin.json skills array, the README table, and AGENTS.md, then bumping the version. [@claim:clm_92be926ba41044dd0a9a93026967b48c013cf07ab3be04e0a2f0c79b544c4ead]
- Repository development practice: version bumps treat .claude-plugin/plugin.json as the source of truth, require updating ten version-bearing files, and contributors run ./scripts/validate-versions.sh locally before pushing. [@claim:clm_b8df81b2a76109e7eb7063c0052b95ca8c0fb7d932dc8c233d6044270f7f2365]
- Repository development practice: GitHub Actions CI on PRs validates YAML frontmatter, plugin structure and version consistency, and skill registration (Copilot skills array, .cursor/skills symlinks, README table and count). [@claim:clm_dd1c51eed1e72df619f1676282df2f108f775b635f5a311ab01f9e4af6ecae64]
<!-- rcw:end owner=source:src_14c9b28b473257c7878684bc5f7cf50a block=evidence -->

## Researcher notes

