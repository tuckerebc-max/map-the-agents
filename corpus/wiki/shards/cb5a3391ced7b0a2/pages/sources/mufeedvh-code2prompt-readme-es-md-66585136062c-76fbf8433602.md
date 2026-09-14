---
access: public
aliases: []
claim_ids:
- clm_22d3e8339c0a7c3eb8a1111cf7b5ad3495c48728818bf597fce2a95d3eab0692
- clm_3b102fe8eeff36f54ad5676bb23d1a70c2d64747b8c9e6786e5bbd5a96fa8295
- clm_88f93e79164fa4465e0844b3e24c700547d3db554b8a634db9a3cc58110d81dc
- clm_f45a47bfd2091789a085d9887f7d884344134876c4b4e611feaaf2a25072287f
maturity: draft
page_id: pg_e1c7e3c273515d2d9f5176fbf8433602
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2985f599f9645955a9888b518229e23b
title: mufeedvh/code2prompt/README_ES.md @ 66585136062c
updated_at: '2026-09-14T04:10:23Z'
---

# mufeedvh/code2prompt/README_ES.md @ 66585136062c

<!-- rcw:begin owner=source:src_2985f599f9645955a9888b518229e23b block=evidence -->
- Tokenization is implemented with tiktoken-rs, supporting encodings cl100k_base, p50k_base, p50k_edit, r50k_base, and o200k_base for OpenAI model families. [@claim:clm_22d3e8339c0a7c3eb8a1111cf7b5ad3495c48728818bf597fce2a95d3eab0692]
- Prompt generation respects .gitignore rules, supports glob-based include/exclude filtering, and uses Handlebars templates that users can customize. [@claim:clm_3b102fe8eeff36f54ad5676bb23d1a70c2d64747b8c9e6786e5bbd5a96fa8295]
- With --json, the tool outputs a JSON object containing prompt, directory_name, token_count, model_info, and files fields. [@claim:clm_88f93e79164fa4465e0844b3e24c700547d3db554b8a634db9a3cc58110d81dc]
- Templates can include user-defined variables outside the default context (absolute_code_path, source_tree, files); the tool prompts the user for their values at generation time. [@claim:clm_f45a47bfd2091789a085d9887f7d884344134876c4b4e611feaaf2a25072287f]
<!-- rcw:end owner=source:src_2985f599f9645955a9888b518229e23b block=evidence -->

## Researcher notes

