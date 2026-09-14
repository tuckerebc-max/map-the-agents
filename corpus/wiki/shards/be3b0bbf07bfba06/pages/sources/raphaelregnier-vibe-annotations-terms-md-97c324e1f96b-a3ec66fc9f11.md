---
access: public
aliases: []
claim_ids:
- clm_1a7e3221dbabeae39155ee368c97c5da668a60bcd25ada1d11292665a2a3bb10
- clm_2867a2d8e472515af35d8619f411e1801c960384d09056ce962877ddaebe494f
- clm_3e7070b24578ddefc9b7e322d27416b8442d137036ee5646231773ed3999df9f
- clm_7b0868d7f7e0a7c5e3246482ce52df5cab446418cd5ae52487a70dd87b4a571d
- clm_bb1e1db9a3bd33418194b4c317472dd52524699e3ce00536dc724aed251e00ef
maturity: draft
page_id: pg_7223d8c4722958988287a3ec66fc9f11
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d8f8bccecea5582ab52da17b51315756
title: RaphaelRegnier/vibe-annotations/TERMS.md @ 97c324e1f96b
updated_at: '2026-09-14T04:17:17Z'
---

# RaphaelRegnier/vibe-annotations/TERMS.md @ 97c324e1f96b

<!-- rcw:begin owner=source:src_d8f8bccecea5582ab52da17b51315756 block=evidence -->
- The Chrome extension requests three permissions: activeTab (annotate the current page), storage (persist annotations locally), and scripting (inject the annotation interface). [@claim:clm_1a7e3221dbabeae39155ee368c97c5da668a60bcd25ada1d11292665a2a3bb10]
- The terms disclaim responsibility for AI-generated code quality and instruct users to review all AI-implemented changes before committing, placing responsibility for annotation-based code changes on the user. [@claim:clm_2867a2d8e472515af35d8619f411e1801c960384d09056ce962877ddaebe494f]
- Annotation data is stored locally on the user's machine under ~/.vibe-annotations/, with the Chrome extension using the Chrome Storage API for persistence; no data is sent to external servers. [@claim:clm_3e7070b24578ddefc9b7e322d27416b8442d137036ee5646231773ed3999df9f]
- The tool is designed to operate exclusively on local development environments (localhost, 127.0.0.1, 0.0.0.0, *.local, *.test, *.localhost, file://), and its terms prohibit annotating production websites or third-party services. [@claim:clm_7b0868d7f7e0a7c5e3246482ce52df5cab446418cd5ae52487a70dd87b4a571d]
- The extension communicates only with a local server on port 3846, which the terms describe as the sole network endpoint for the product besides an optional NPM registry version check. [@claim:clm_bb1e1db9a3bd33418194b4c317472dd52524699e3ce00536dc724aed251e00ef]
<!-- rcw:end owner=source:src_d8f8bccecea5582ab52da17b51315756 block=evidence -->

## Researcher notes

