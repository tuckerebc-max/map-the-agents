---
access: public
aliases: []
claim_ids:
- clm_0e64851e42b7e152ae742a8caeeb9a96d20b26febc82801004a7795aa2f31c6e
- clm_1fefc086b206a3fd1cd7890e856a1eb1f5fd38dce413d7f5822a4585ca64bb21
- clm_516ae2f346bbba598d3b77550c48365730fa40880d5e142ffa80166c16197f4c
- clm_6d752c104e78ff18d1ee57e82d104bac0e7bc2e109f7fefef4cddb16d30b73ff
- clm_a4b48ffe496d036d367a1448088dbc70aef76308b5b9e29099ee3e946f201ae9
- clm_cf971297c59910ae04981a6640df33ecea79e77260013296795cd0e867fbdfdb
- clm_ec6b6b950f91f55283257136855766529f9cd264873a0e6ac041a2059fb129c9
maturity: draft
page_id: pg_12444557887553b6b7b0b3fd9eb10810
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d6fa616f11f15a6bb98274712eb51371
title: genia-dev/GeniA/README.md @ 39a206b85d84
updated_at: '2026-09-14T02:01:11Z'
---

# genia-dev/GeniA/README.md @ 39a206b85d84

<!-- rcw:begin owner=source:src_d6fa616f11f15a6bb98274712eb51371 block=evidence -->
- Documented use cases target platform-engineering teams: k8s/Argo deployments and troubleshooting, FinOps cloud-cost reporting, SecOps vulnerability checks, SRE outage troubleshooting, and DevOps cluster upgrades. [@claim:clm_0e64851e42b7e152ae742a8caeeb9a96d20b26febc82801004a7795aa2f31c6e]
- GeniA is built on OpenAI's function-calling capability (OpenAI or Azure) and requires an OpenAI API key to run. [@claim:clm_1fefc086b206a3fd1cd7890e856a1eb1f5fd38dce413d7f5822a4585ca64bb21]
- Repository development practice: local setup requires copying .env.template to .env with OPENAI_API_KEY as the minimal secret, and the repo displays a CI workflow badge. [@claim:clm_516ae2f346bbba598d3b77550c48365730fa40880d5e142ffa80166c16197f4c]
- The roadmap lists capabilities not yet present: OKTA SSO integration, RBAC support, and extension with thousands of new tools are future plans. [@claim:clm_6d752c104e78ff18d1ee57e82d104bac0e7bc2e109f7fefef4cddb16d30b73ff]
- The product can run in three modes: a local terminal mode, a Slack app bot mode, and a Streamlit web app mode, per the developer guide and README. [@claim:clm_a4b48ffe496d036d367a1448088dbc70aef76308b5b9e29099ee3e946f201ae9]
- Repository development practice: contributors fork the repo and submit pull requests, run tests with 'poetry run pytest tests', and can build/run the project via Docker or Poetry commands documented in the developer guide. [@claim:clm_cf971297c59910ae04981a6640df33ecea79e77260013296795cd0e867fbdfdb]
- The project positions the agent as a production-grade team member operating inside a team's Slack channel and executing tasks in the production environment on users' behalf. [@claim:clm_ec6b6b950f91f55283257136855766529f9cd264873a0e6ac041a2059fb129c9]
<!-- rcw:end owner=source:src_d6fa616f11f15a6bb98274712eb51371 block=evidence -->

## Researcher notes

