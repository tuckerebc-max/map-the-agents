---
access: public
aliases: []
claim_ids:
- clm_133b57361aeb4d574e8faf8a26510625dd582a37874c3847b5e4707ccd8f0824
- clm_14b6695957fe224cf83773e8f570b8b9baa2b96370afad9bd9bfdbe66f84d4f2
- clm_1f96a30e9a9691e65e6cfcdeee5b3cd7d9b1965d56dfa80b0cafbeef55db7330
- clm_3a4893a4a8c3314de4be26e298bcfbbf9aa2b8b50328c53ab5d63acd6f0c1c26
- clm_617352d91521eb027205187aa439629e6079bdf39d63941a1dae858285ad2af3
- clm_8625a882bd1e1d8518cbcce9d8503f569ef2ae7927bb74b0967f57848fd134c2
- clm_994e3a8c1ab4d37d71ea2bb46b8ed17e9ca0912b020bea59bb11da58574108b6
- clm_e295077c8e49dd9263dd6cff874443f82acf94bbca43bed135a4a0813b21a57d
- clm_ef2b047440486ff18ab2935861ab8b8cfe9e070a4813c00ce485e8628cc9cefe
- clm_ff7b1f525bb97dce2c0dd599aa65b37830ef47560e46fb273afd31e15533b551
maturity: draft
page_id: pg_879a123b0f845a978edea4d723b8e643
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bc54d5d7a0d853e38ba3309d64d7036e
title: ntegrals/10x/README.md @ 6ea128c31173
updated_at: '2026-09-14T04:57:31Z'
---

# ntegrals/10x/README.md @ 6ea128c31173

<!-- rcw:begin owner=source:src_bc54d5d7a0d853e38ba3309d64d7036e block=evidence -->
- Custom skills are markdown prompts stored in .10x/skills/ or ~/.config/10x/skills/ and invoked via /<skill-name>. [@claim:clm_133b57361aeb4d574e8faf8a26510625dd582a37874c3847b5e4707ccd8f0824]
- The tool is distributed as the npm package 10x-cli and installed globally with npm install -g 10x-cli. [@claim:clm_14b6695957fe224cf83773e8f570b8b9baa2b96370afad9bd9bfdbe66f84d4f2]
- The 10x CLI supports an interactive session mode, --byok for a user-supplied OpenRouter key, --model <tier>, --resume <name>, and -x to run a prompt and exit. [@claim:clm_1f96a30e9a9691e65e6cfcdeee5b3cd7d9b1965d56dfa80b0cafbeef55db7330]
- Superpowers are multi-step AI workflows that chain different models, with each step routed to the fastest model tier able to handle it. [@claim:clm_3a4893a4a8c3314de4be26e298bcfbbf9aa2b8b50328c53ab5d63acd6f0c1c26]
- Users can define custom superpowers in .10x/superpowers/ or ~/.config/10x/superpowers/ using markdown files with name and trigger frontmatter. [@claim:clm_617352d91521eb027205187aa439629e6079bdf39d63941a1dae858285ad2af3]
- The project is MIT licensed and advertises BYOK (bring your own key) for cost control, in contrast to subscription-only competitors. [@claim:clm_8625a882bd1e1d8518cbcce9d8503f569ef2ae7927bb74b0967f57848fd134c2]
- Built-in slash commands include /review, /pr, /refactor, /debug, /explain, and /test, each described as a multi-step workflow such as reproduce-analyze-fix debugging. [@claim:clm_994e3a8c1ab4d37d71ea2bb46b8ed17e9ca0912b020bea59bb11da58574108b6]
- Project context is provided via a 10X.md file in the project root, e.g. listing tech stack and conventions. [@claim:clm_e295077c8e49dd9263dd6cff874443f82acf94bbca43bed135a4a0813b21a57d]
- Three model tiers are documented: Superfast (GPT OSS 20B), Fast (Kimi K2 1T), and Smart (Claude Opus 4), mapped to simple queries, code generation, and complex reasoning respectively. [@claim:clm_ef2b047440486ff18ab2935861ab8b8cfe9e070a4813c00ce485e8628cc9cefe]
- The 'up to 20x faster' speed figures appear to be marketing claims tied to the tier table rather than results of a documented benchmark methodology. [@claim:clm_ff7b1f525bb97dce2c0dd599aa65b37830ef47560e46fb273afd31e15533b551]
<!-- rcw:end owner=source:src_bc54d5d7a0d853e38ba3309d64d7036e block=evidence -->

## Researcher notes

