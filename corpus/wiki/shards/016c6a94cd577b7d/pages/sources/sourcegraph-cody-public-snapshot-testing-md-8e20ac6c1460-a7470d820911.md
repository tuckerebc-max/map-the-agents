---
access: public
aliases: []
claim_ids:
- clm_7acf56d7059983d5ce9970c193c162614488a9fc3e9a5442d7e91ea2dc46ba57
- clm_8b32793d9a4ce4b22050998856df63e307ac1120cd9ec1ff8a1ceed907c87dff
- clm_b623466d176947f8bb5d4c93d9a67928fb4940c6e10b6a93fe50357352e0f8f1
- clm_df35acfc3095456ac75aeb7bedd245f63631101fed14aab6338f5bb5ab97f0e8
maturity: draft
page_id: pg_4bc26971965a5bd09352a7470d820911
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_03d972780cc6508ab94ceea09958e2ba
title: sourcegraph/cody-public-snapshot/TESTING.md @ 8e20ac6c1460
updated_at: '2026-09-14T02:42:09Z'
---

# sourcegraph/cody-public-snapshot/TESTING.md @ 8e20ac6c1460

<!-- rcw:begin owner=source:src_03d972780cc6508ab94ceea09958e2ba block=evidence -->
- The edit workflow applies changes with code lenses for Show diff, Accept All, Retry, Undo, Accept, and Reject, and shows a 'Cody is working...' notification while edits apply. [@claim:clm_7acf56d7059983d5ce9970c193c162614488a9fc3e9a5442d7e91ea2dc46ba57]
- Custom commands can be defined in user or workspace settings JSON with a prompt and context (e.g. currentFile or selection) and run from the Custom Commands menu. [@claim:clm_8b32793d9a4ce4b22050998856df63e307ac1120cd9ec1ff8a1ceed907c87dff]
- Per the QA checklist, Free users' chat defaults to Claude 2 with no LLM switching without upgrading to Pro, while Pro users can switch and enterprise users cannot change the LLM. [@claim:clm_b623466d176947f8bb5d4c93d9a67928fb4940c6e10b6a93fe50357352e0f8f1]
- Repository development practice: TESTING.md is a manual QA checklist covering commands (Explain, Edit, Test, Document, Smell), chat UX, LLM selection, and autocomplete behaviors. [@claim:clm_df35acfc3095456ac75aeb7bedd245f63631101fed14aab6338f5bb5ab97f0e8]
<!-- rcw:end owner=source:src_03d972780cc6508ab94ceea09958e2ba block=evidence -->

## Researcher notes

