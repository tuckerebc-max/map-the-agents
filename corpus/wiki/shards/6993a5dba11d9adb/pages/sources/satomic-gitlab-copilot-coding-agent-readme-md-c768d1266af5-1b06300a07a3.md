---
access: public
aliases: []
claim_ids:
- clm_0c51d71c880f0159a7ee75efc8a0340e83e96d317bf2d1cd2ae8fd3e91fae572
- clm_1d121a1e6e67f340b74b3c93ceb145b7eeb44207fafa79dbdb17212231740dac
- clm_274d9c5bc685894d98202309a89da6715ab58f2a758c6c6e4c68c93fac071d4b
- clm_34d98dff602041712f0da0f8860ef2215c02baad62c1f40b10fd63d0eed944aa
- clm_3e6851815c2ce30f189a35140e5f9a100621090323206c0133ec883dd69f342b
- clm_43632538e87cec24e44c80e7b40a36822cd97a9d653fbbd36dea38738c19f99d
- clm_440ed5900c4740f3c390a655c43ea9b937adace09b9c422d03665c6526c300a1
- clm_72536333c7c793ba870a4ba4be0d1bf872fb64e0d504f0033f8873bd1d40dbc4
- clm_9403cd0b695475c6d2b96b8d8a1985f786158ec68fa5299a7a865523839c1627
- clm_9f725a17c68aa85dd29a37d6f0b2ef9794fe80fc6a2342b7e45ed786a4cd43f8
- clm_b600718a0bf4d4355fd2ef5d8fdacd99ae51e13550758ff37ea3992c8415de7e
- clm_c4345d6750b6d14407d424b5bfe1012c2eff0595532f85e5cc041928504c6144
- clm_c4b1d90f39e1985ac74d7012b09b3c9e31020172bca4200bf62f688c3b292dd2
- clm_d589d239ecadb56a6ad6176c4add302ca480e84a80ff6bcac35eddb276f8bb2e
- clm_d7304bf37728c311a589239b04da7353396c380af3a88003280fef7bf7130ede
maturity: draft
page_id: pg_1a03c416da2d5e39a6b91b06300a07a3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a3728f42523853ac8dd20bd602915066
title: satomic/gitlab-copilot-coding-agent/README.md @ c768d1266af5
updated_at: '2026-09-14T04:19:53Z'
---

# satomic/gitlab-copilot-coding-agent/README.md @ c768d1266af5

<!-- rcw:begin owner=source:src_a3728f42523853ac8dd20bd602915066 block=evidence -->
- The webhook service can run as a Docker container (satomic/gitlab-copilot-coding-agent-hook:latest, port 8080) or from source via python3 main.py, exposing a /webhook endpoint. [@claim:clm_0c51d71c880f0159a7ee75efc8a0340e83e96d317bf2d1cd2ae8fd3e91fae572]
- The MR reviewer workflow performs code review: acknowledge, analyze code changes, perform a comprehensive review, and post a detailed review comment. [@claim:clm_1d121a1e6e67f340b74b3c93ceb145b7eeb44207fafa79dbdb17212231740dac]
- The review report includes an overall assessment, issues categorized by severity (Critical, Major, Minor, Suggestions), file locations with fix recommendations, and a final recommendation of APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION. [@claim:clm_274d9c5bc685894d98202309a89da6715ab58f2a758c6c6e4c68c93fac071d4b]
- Required tools include a GitLab account with API access, a GitLab Runner with Docker/Kubernetes executor, GitHub Copilot CLI access with subscription, and optionally Docker for the webhook service. [@claim:clm_34d98dff602041712f0da0f8860ef2215c02baad62c1f40b10fd63d0eed944aa]
- Three trigger interfaces are supported: assigning an issue to Copilot, commenting @copilot-agent in an MR, and assigning Copilot as an MR reviewer; each maps to a distinct workflow (issue, mr_update, mr_review). [@claim:clm_3e6851815c2ce30f189a35140e5f9a100621090323206c0133ec883dd69f342b]
- Described as a fully automated coding agent powered by GitHub Copilot CLI and GitLab CI/CD, enabling autonomous code implementation and code review via issue assignments, MR comments, and reviewer assignments. [@claim:clm_43632538e87cec24e44c80e7b40a36822cd97a9d653fbbd36dea38738c19f99d]
- The MR note workflow handles quick updates: a comment triggers the pipeline, the agent acknowledges, implements changes, pushes to the source branch, and posts a summary comment. [@claim:clm_440ed5900c4740f3c390a655c43ea9b937adace09b9c422d03665c6526c300a1]
- GitLab events trigger a webhook to a Flask service, which validates and extracts pipeline variables and triggers a CI/CD pipeline via the GitLab API. [@claim:clm_72536333c7c793ba870a4ba4be0d1bf872fb64e0d504f0033f8873bd1d40dbc4]
- The issue assignment workflow proceeds: acknowledge issue, generate TODO plan, create MR, implement code, push changes, then update MR and issue. [@claim:clm_9403cd0b695475c6d2b96b8d8a1985f786158ec68fa5299a7a865523839c1627]
- Intermediate execution files such as patch_raw.txt, todo.md, plan.json, commit_msg.txt, and mr_summary.txt are generated during runs but excluded from commits. [@claim:clm_9f725a17c68aa85dd29a37d6f0b2ef9794fe80fc6a2342b7e45ed786a4cd43f8]
- The runtime requires a GitLab personal access token with api, read_repository, and write_repository scopes, plus a GITHUB_TOKEN fine-grained PAT with the Copilot Requests permission. [@claim:clm_b600718a0bf4d4355fd2ef5d8fdacd99ae51e13550758ff37ea3992c8415de7e]
- Three components are documented: the app repository, a Flask-based webhook relay service that captures GitLab events, and the Copilot Coding Agent repository acting as a CI/CD orchestrator. [@claim:clm_c4345d6750b6d14407d424b5bfe1012c2eff0595532f85e5cc041928504c6144]
- If a merge request already exists for an issue, the agent detects it and posts a notification asking the user to continue in the existing MR rather than creating a duplicate. [@claim:clm_c4b1d90f39e1985ac74d7012b09b3c9e31020172bca4200bf62f688c3b292dd2]
- The webhook service is configured via environment variables including PIPELINE_TRIGGER_TOKEN, PIPELINE_PROJECT_ID, WEBHOOK_SECRET_TOKEN, COPILOT_AGENT_USERNAME, LISTEN_HOST/PORT, ENABLE_INLINE_REVIEW_COMMENTS, and COPILOT_LANGUAGE. [@claim:clm_d589d239ecadb56a6ad6176c4add302ca480e84a80ff6bcac35eddb276f8bb2e]
- CI/CD execution uses a Docker image satomic/copilot-cli:latest with GitHub Copilot CLI installed and authentication pre-configured to read the GITHUB_TOKEN environment variable; users may alternatively build their own image. [@claim:clm_d7304bf37728c311a589239b04da7353396c380af3a88003280fef7bf7130ede]
<!-- rcw:end owner=source:src_a3728f42523853ac8dd20bd602915066 block=evidence -->

## Researcher notes

