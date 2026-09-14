---
access: public
aliases: []
claim_ids:
- clm_02aecaeb9271b034db13d867fa67d5299431b856111694d93bf48d73dc68a73d
- clm_044d21217cc331a245272705b16a521986f4a86e87935dd140b675a111ce9c85
- clm_98aca8401f700c9c2c2ba1cfabce9005f7a3833bcdb96c46e7e39e42506ae62a
maturity: draft
page_id: pg_75cd08ef50ef5e3fad889c88369c5715
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f16de8cb6dc254f79a590403b0c9f06d
title: ZhangHanDong/harness-engineering-from-cc-to-ai-coding/docs/reverse-engineering-guide.md
  @ e40e0feec02b
updated_at: '2026-09-14T04:34:01Z'
---

# ZhangHanDong/harness-engineering-from-cc-to-ai-coding/docs/reverse-engineering-guide.md @ e40e0feec02b

<!-- rcw:begin owner=source:src_f16de8cb6dc254f79a590403b0c9f06d block=evidence -->
- Per the guide, v2.1.88 shipped a 57MB source map restoring 4,756 source files, while v2.1.89+ removed source-map distribution, forcing minified-bundle analysis. [@claim:clm_02aecaeb9271b034db13d867fa67d5299431b856111694d93bf48d73dc68a73d]
- A comparison table reports v2.1.88 to v2.1.91 changes: cli.js grew ~115KB, tengu events went 827 to 860, environment variables 178 to 183, GrowthBook configs 17 to 18. [@claim:clm_044d21217cc331a245272705b16a521986f4a86e87935dd140b675a111ce9c85]
- The reverse-engineering guide documents helper scripts: scripts/extract-signals.sh for string-constant mining and scripts/cc-version-diff.sh for structured version-to-version diff reports. [@claim:clm_98aca8401f700c9c2c2ba1cfabce9005f7a3833bcdb96c46e7e39e42506ae62a]
<!-- rcw:end owner=source:src_f16de8cb6dc254f79a590403b0c9f06d block=evidence -->

## Researcher notes

