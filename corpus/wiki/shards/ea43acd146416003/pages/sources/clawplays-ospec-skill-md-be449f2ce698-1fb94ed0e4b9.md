---
access: public
aliases: []
claim_ids:
- clm_187a580e443fed83d8ec8d04543aa3c66af299e604742089d6cab1ecbfe60924
- clm_690d78b56edd195ea23e6842d51eb6a79d71ee900b654e926d7d9ef97ec8efca
- clm_d48f189365599463aed619dfbad38049d7431897bc643ff0d2a2b073cbdfa4c3
maturity: draft
page_id: pg_8152288e1b8f5bed90041fb94ed0e4b9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e5592987911358dc9bba8c9bd2073837
title: clawplays/ospec/SKILL.md @ be449f2ce698
updated_at: '2026-09-14T03:40:58Z'
---

# clawplays/ospec/SKILL.md @ be449f2ce698

<!-- rcw:begin owner=source:src_e5592987911358dc9bba8c9bd2073837 block=evidence -->
- For Claude Code, `ospec session hook --target claude --apply` installs a hook bundle under .ospec/hooks/claude merged into .claude/settings.json that announces dispatches, hard-blocks subagent dispatch while a required decision is pending, and is Claude-only and opt-in. [@claim:clm_187a580e443fed83d8ec8d04543aa3c66af299e604742089d6cab1ecbfe60924]
- Archiving writes an SKILL.index.json.archived_changes entry, refreshes docs/project/feature-catalog.md rows, and idempotently replaces ospec:last-change traceability comments — described as the engine's only write into human-owned documents, with comment failures warning rather than blocking. [@claim:clm_690d78b56edd195ea23e6842d51eb6a79d71ee900b654e926d7d9ef97ec8efca]
- The official npm package is @clawplays/ospec-cli and the command is `ospec`; documented subcommands include init, change, goal, verify, finalize, session, execute, loop, docs, update, and layout migrate. [@claim:clm_d48f189365599463aed619dfbad38049d7431897bc643ff0d2a2b073cbdfa4c3]
<!-- rcw:end owner=source:src_e5592987911358dc9bba8c9bd2073837 block=evidence -->

## Researcher notes

