---
access: public
aliases: []
claim_ids:
- clm_97bb50af6163a9968c5c1b9d984ae6ad1db9d866f035235bdfc8f404ce19b03d
- clm_d06d78d5cd8373f0f6a24f03099e854573e204cacd03f44603974b67687a0e1c
maturity: draft
page_id: pg_6ef80011f33f598390acc8aa33956eac
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e635279e77cc5484b5e07f8f2a622b39
title: cline/cline/docs/customization/skills.mdx @ c1c0b55ca03a
updated_at: '2026-09-14T01:42:03Z'
---

# cline/cline/docs/customization/skills.mdx @ c1c0b55ca03a

<!-- rcw:begin owner=source:src_e635279e77cc5484b5e07f8f2a622b39 block=evidence -->
- Skills are modular instruction sets loaded on demand (unlike always-active rules): metadata loads at startup (~100 tokens), full SKILL.md instructions load when triggered via the use_skill tool or slash commands, and resources load as needed. [@claim:clm_97bb50af6163a9968c5c1b9d984ae6ad1db9d866f035235bdfc8f404ce19b03d]
- A skill is a directory containing a required SKILL.md with YAML frontmatter (name matching the directory, description up to 1024 chars), optionally with docs/ and scripts/ subdirectories; skills are discovered from .cline/skills/ or ~/.cline/skills/. [@claim:clm_d06d78d5cd8373f0f6a24f03099e854573e204cacd03f44603974b67687a0e1c]
<!-- rcw:end owner=source:src_e635279e77cc5484b5e07f8f2a622b39 block=evidence -->

## Researcher notes

