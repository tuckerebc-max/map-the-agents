---
access: public
aliases: []
claim_ids:
- clm_47f8d5dc4a26b0bc697855485e3dd50c04619010ebd406468ad6ae60c7bf7d9e
- clm_98191c94cc274ecb59c6d9d3b0426d1a9751f98b178632b73c95cf89949f52f2
- clm_ec7bfa6d10ccfc0777ea5288a5fb7d67aba567e34238be6e0a0b7a1f5a9aaa70
- clm_f8407bf282fbc1a3f86b8258b660a49d97c26d84a140880cd3a37d32b7617b67
- clm_f8fe6b7d3954a008b3c2bdac834c7f5586d428c1333cb306a49d690b50ccc816
maturity: draft
page_id: pg_1eb9402173a65f4585f3d1403d0383f0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7c5bc53ab480521087a616b0697a7f27
title: kuafuai/DevOpsGPT/docs/DOCUMENT.md @ 614a565f9caf
updated_at: '2026-09-14T02:09:26Z'
---

# kuafuai/DevOpsGPT/docs/DOCUMENT.md @ 614a565f9caf

<!-- rcw:begin owner=source:src_7c5bc53ab480521087a616b0697a7f27 block=evidence -->
- Automated deployment to cloud services is configured with CD_ACCESS_KEY, CD_SECRET_KEY, CD_REGION, CD_EIP, CD_SECURITY, and CD_SWITCH, exemplified with Alibaba Cloud. [@claim:clm_47f8d5dc4a26b0bc697855485e3dd50c04619010ebd406468ad6ae60c7bf7d9e]
- APPS configuration holds per-application and per-service metadata (name, base_prompt, intro, api_doc, struct, lib, specification) that guides how tasks are designed; in the open-source version it is maintained manually. [@claim:clm_98191c94cc274ecb59c6d9d3b0426d1a9751f98b178632b73c95cf89949f52f2]
- When Git integration is enabled via GIT_ENABLED and related settings (GIT_URL, GIT_TOKEN, GIT_USERNAME, GIT_EMAIL), development tasks can pull and push code from Git. [@claim:clm_ec7bfa6d10ccfc0777ea5288a5fb7d67aba567e34238be6e0a0b7a1f5a9aaa70]
- Configuration uses an env.yaml file (copied from env.yaml.tpl) holding settings such as GPT_KEYS for OpenAI/Azure, LLM_MODEL, ports, and USERS login configuration. [@claim:clm_f8407bf282fbc1a3f86b8258b660a49d97c26d84a140880cd3a37d32b7617b67]
- The product supports CI tool integration with GitlabCI and GitHub Actions, triggering pipelines on code submission via a configured GIT_API address. [@claim:clm_f8fe6b7d3954a008b3c2bdac834c7f5586d428c1333cb306a49d690b50ccc816]
<!-- rcw:end owner=source:src_7c5bc53ab480521087a616b0697a7f27 block=evidence -->

## Researcher notes

