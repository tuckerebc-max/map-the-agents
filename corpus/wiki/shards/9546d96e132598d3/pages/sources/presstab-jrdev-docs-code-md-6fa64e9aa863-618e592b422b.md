---
access: public
aliases: []
claim_ids:
- clm_3aeb69d5a95d2257952df8e7216efcc09db6703b4d78f23ac799b587d89a08e9
- clm_54b74496b779163e5a040a56e6932b84535403d1dff4c43b3fd51202f64b8357
- clm_873d656b10fdc5e96fc4ad47e7ec24e948d552a22db668fb4078a2978ca71a17
- clm_8bde0e16789966adb0e710ef3dede923d7116834fe2dba46e41274fed2a22144
- clm_d51c758a2fa42ddb1ac8ca5620779caf3aa72a2986e7391fb9c06e0006937ef9
maturity: draft
page_id: pg_7dfa5e2565f4524b8ad6618e592b422b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d2c7fec36eba5ae48e0d0b0086f942ea
title: presstab/jrdev/docs/code.md @ 6fa64e9aa863
updated_at: '2026-09-14T02:32:45Z'
---

# presstab/jrdev/docs/code.md @ 6fa64e9aa863

<!-- rcw:begin owner=source:src_d2c7fec36eba5ae48e0d0b0086f942ea block=evidence -->
- JrDev runs in the user's current working directory, started by entering 'jrdev' in a project directory, with commands like /init and /code typed into a Command Input field. [@claim:clm_3aeb69d5a95d2257952df8e7216efcc09db6703b4d78f23ac799b587d89a08e9]
- The tool can modify project files and prompts for confirmation unless in 'Accept All' mode; execute-phase diffs offer Accept, Accept All, Edit, No, or Request Change options. [@claim:clm_54b74496b779163e5a040a56e6932b84535403d1dff4c43b3fd51202f64b8357]
- The /code agent runs a six-phase pipeline: Analyze, Fetch Context, Plan, Execute, Review, and Validate, ending with files updated on disk. [@claim:clm_873d656b10fdc5e96fc4ad47e7ec24e948d552a22db668fb4078a2978ca71a17]
- The Plan phase produces an ordered JSON plan of file-modification steps, validates each filename against loaded files, and offers accept, edit, accept-all, reprompt (restarting at Analyze), or cancel. [@claim:clm_8bde0e16789966adb0e710ef3dede923d7116834fe2dba46e41274fed2a22144]
- If the Review phase finds changes insufficient, the pipeline returns to the Analyze phase with the failed review, forming an agentic loop; a passing review proceeds to validation. [@claim:clm_d51c758a2fa42ddb1ac8ca5620779caf3aa72a2986e7391fb9c06e0006937ef9]
<!-- rcw:end owner=source:src_d2c7fec36eba5ae48e0d0b0086f942ea block=evidence -->

## Researcher notes

