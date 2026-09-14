---
access: public
aliases: []
claim_ids:
- clm_857d53436936acd1bba85e66c6715e19a72907a4b60e5e8072d02c79fb020be7
- clm_c09800861b24d85226afdcc851ff75b11e6666b2e9a770c16673083d3d4cd89a
- clm_c36d6b0874ac3b687127139284eb154224f3a739e2d2e09bb467b08b77774e78
- clm_d4ec3b97e2d827b15a60d5ebb8c0728b5319be39278b5e5ff1b5d31af4c381a1
maturity: draft
page_id: pg_afdb9d3c090e5dfca9b617bc13318879
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_235fd772cca85b48a4cce9c4487ae92b
title: The-PR-Agent/pr-agent/docs/docs/index.md @ d24b6f36e787
updated_at: '2026-09-14T04:25:33Z'
---

# The-PR-Agent/pr-agent/docs/docs/index.md @ d24b6f36e787

<!-- rcw:begin owner=source:src_235fd772cca85b48a4cce9c4487ae92b block=evidence -->
- A /help command lets users ask natural-language questions in a PR comment, and the bot responds with an answer including relevant documentation links. [@claim:clm_857d53436936acd1bba85e66c6715e19a72907a4b60e5e8072d02c79fb020be7]
- The feature matrix lists tools including Describe, Review, Improve, Ask, Add Docs, Generate Labels, and Similar Issues, with per-provider support varying (e.g. Ask lacks Gitea support; Similar Issues is GitHub-only). [@claim:clm_c09800861b24d85226afdcc851ff75b11e6666b2e9a770c16673083d3d4cd89a]
- The /help_docs tool is temporarily disabled since v0.36.1 pending a fix for a credential-exposure issue (issue #2445). [@claim:clm_c36d6b0874ac3b687127139284eb154224f3a739e2d2e09bb467b08b77774e78]
- A PR compression strategy converts code diffs into manageable LLM prompts, and the README claims it handles both small and large PRs. [@claim:clm_d4ec3b97e2d827b15a60d5ebb8c0728b5319be39278b5e5ff1b5d31af4c381a1]
<!-- rcw:end owner=source:src_235fd772cca85b48a4cce9c4487ae92b block=evidence -->

## Researcher notes

