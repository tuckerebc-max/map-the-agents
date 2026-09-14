---
access: public
aliases: []
claim_ids:
- clm_1626cc95090f2e367a7d996c268861164d4a1142daeb9a0247156a54d9141e2e
- clm_1977c01e07b5b1436c7bee93d36b24c13b51256357834247cecf52c9e327f1a8
- clm_353a722eed04348ada31e670ce124f7e38c530ecec07f3b641d1b0765dd6112b
maturity: draft
page_id: pg_622a028cf9e95e6aa289763af5edb41c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bfe3843cead35ffaa6244197a9d66247
title: satomic/gitlab-copilot-coding-agent/I18N_README.md @ c768d1266af5
updated_at: '2026-09-14T04:19:53Z'
---

# satomic/gitlab-copilot-coding-agent/I18N_README.md @ c768d1266af5

<!-- rcw:begin owner=source:src_bfe3843cead35ffaa6244197a9d66247 block=evidence -->
- The i18n documentation lists future enhancements including dynamic language detection from GitLab user preferences, language-specific formatting rules, and automated template validation; UI message localization is marked optional. [@claim:clm_1626cc95090f2e367a7d996c268861164d4a1142daeb9a0247156a54d9141e2e]
- Prompt templates are organized per language (en, zh, ja, hi, ko, th) under prompts/ directories, with a scripts/load_prompt.sh loader that selects language via COPILOT_LANGUAGE and falls back to English. [@claim:clm_1977c01e07b5b1436c7bee93d36b24c13b51256357834247cecf52c9e327f1a8]
- The prompt loader supports template variable substitution using {variable_name} syntax, accepting variables from environment or arguments, with Python-based safe substitution for special characters and emojis. [@claim:clm_353a722eed04348ada31e670ce124f7e38c530ecec07f3b641d1b0765dd6112b]
<!-- rcw:end owner=source:src_bfe3843cead35ffaa6244197a9d66247 block=evidence -->

## Researcher notes

