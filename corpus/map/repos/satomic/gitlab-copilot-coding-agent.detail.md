# satomic/gitlab-copilot-coding-agent -- full detail

[Back to orientation](gitlab-copilot-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/satomic/gitlab-copilot-coding-agent/c768d1266af5c118f5461ea7d47353d2ef03a3cc/51a0ffd4ad935453.json](../../../wiki/dossiers/satomic/gitlab-copilot-coding-agent/c768d1266af5c118f5461ea7d47353d2ef03a3cc/51a0ffd4ad935453.json)

## specifications (1 claim(s))

- [observation/documented] Described as a fully automated coding agent powered by GitHub Copilot CLI and GitLab CI/CD, enabling autonomous code implementation and code review via issue assignments, MR comments, and reviewer assignments. -- evidence: [README.md#L5-L5](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L5-L5) (`clm_43632538e87cec24e44c80e7b40a36822cd97a9d653fbbd36dea38738c19f99d`)

## components (1 claim(s))

- [observation/documented] Three components are documented: the app repository, a Flask-based webhook relay service that captures GitLab events, and the Copilot Coding Agent repository acting as a CI/CD orchestrator. -- evidence: [README.md#L62-L64](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L62-L64) (`clm_c4345d6750b6d14407d424b5bfe1012c2eff0595532f85e5cc041928504c6144`)

## design-choices (2 claim(s))

- [observation/documented] If a merge request already exists for an issue, the agent detects it and posts a notification asking the user to continue in the existing MR rather than creating a duplicate. -- evidence: [README.md#L302-L302](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L302-L302) (`clm_c4b1d90f39e1985ac74d7012b09b3c9e31020172bca4200bf62f688c3b292dd2`)
- [observation/documented] Intermediate execution files such as patch_raw.txt, todo.md, plan.json, commit_msg.txt, and mr_summary.txt are generated during runs but excluded from commits. -- evidence: [README.md#L377-L382](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L377-L382) (`clm_9f725a17c68aa85dd29a37d6f0b2ef9794fe80fc6a2342b7e45ed786a4cd43f8`)

## workflows (3 claim(s))

- [observation/documented] The issue assignment workflow proceeds: acknowledge issue, generate TODO plan, create MR, implement code, push changes, then update MR and issue. -- evidence: [README.md#L68-L73](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L68-L73) (`clm_9403cd0b695475c6d2b96b8d8a1985f786158ec68fa5299a7a865523839c1627`)
- [observation/documented] The MR note workflow handles quick updates: a comment triggers the pipeline, the agent acknowledges, implements changes, pushes to the source branch, and posts a summary comment. -- evidence: [README.md#L75-L80](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L75-L80) (`clm_440ed5900c4740f3c390a655c43ea9b937adace09b9c422d03665c6526c300a1`)
- [observation/documented] The MR reviewer workflow performs code review: acknowledge, analyze code changes, perform a comprehensive review, and post a detailed review comment. -- evidence: [README.md#L82-L87](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L82-L87) (`clm_1d121a1e6e67f340b74b3c93ceb145b7eeb44207fafa79dbdb17212231740dac`)

## skills-patterns (1 claim(s))

- [observation/documented] Prompt templates are organized per language (en, zh, ja, hi, ko, th) under prompts/ directories, with a scripts/load_prompt.sh loader that selects language via COPILOT_LANGUAGE and falls back to English. -- evidence: [I18N_README.md#L9-L14](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L9-L14), [I18N_README.md#L106-L110](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L106-L110), [I18N_README.md#L104-L104](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L104-L104), [I18N_README.md#L20-L100](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L20-L100) (`clm_1977c01e07b5b1436c7bee93d36b24c13b51256357834247cecf52c9e327f1a8`)

## interfaces (4 claim(s))

- [observation/documented] Three trigger interfaces are supported: assigning an issue to Copilot, commenting @copilot-agent in an MR, and assigning Copilot as an MR reviewer; each maps to a distinct workflow (issue, mr_update, mr_review). -- evidence: [README.md#L26-L32](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L26-L32), [README.md#L40-L49](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L40-L49) (`clm_3e6851815c2ce30f189a35140e5f9a100621090323206c0133ec883dd69f342b`)
- [observation/documented] The webhook service is configured via environment variables including PIPELINE_TRIGGER_TOKEN, PIPELINE_PROJECT_ID, WEBHOOK_SECRET_TOKEN, COPILOT_AGENT_USERNAME, LISTEN_HOST/PORT, ENABLE_INLINE_REVIEW_COMMENTS, and COPILOT_LANGUAGE. -- evidence: [README.md#L182-L197](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L182-L197) (`clm_d589d239ecadb56a6ad6176c4add302ca480e84a80ff6bcac35eddb276f8bb2e`)
- [observation/documented] The review report includes an overall assessment, issues categorized by severity (Critical, Major, Minor, Suggestions), file locations with fix recommendations, and a final recommendation of APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION. -- evidence: [README.md#L347-L351](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L347-L351) (`clm_274d9c5bc685894d98202309a89da6715ab58f2a758c6c6e4c68c93fac071d4b`)
- [observation/documented] The webhook service can run as a Docker container (satomic/gitlab-copilot-coding-agent-hook:latest, port 8080) or from source via python3 main.py, exposing a /webhook endpoint. -- evidence: [README.md#L230-L235](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L230-L235), [README.md#L206-L223](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L206-L223) (`clm_0c51d71c880f0159a7ee75efc8a0340e83e96d317bf2d1cd2ae8fd3e91fae572`)

## memory-state (1 claim(s))

- [observation/documented] The prompt loader supports template variable substitution using {variable_name} syntax, accepting variables from environment or arguments, with Python-based safe substitution for special characters and emojis. -- evidence: [I18N_README.md#L106-L110](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L106-L110), [I18N_README.md#L218-L218](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L218-L218), [I18N_README.md#L318-L318](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L318-L318) (`clm_353a722eed04348ada31e670ce124f7e38c530ecec07f3b641d1b0765dd6112b`)

## orchestration (1 claim(s))

- [observation/documented] GitLab events trigger a webhook to a Flask service, which validates and extracts pipeline variables and triggers a CI/CD pipeline via the GitLab API. -- evidence: [README.md#L34-L38](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L34-L38), [README.md#L26-L32](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L26-L32) (`clm_72536333c7c793ba870a4ba4be0d1bf872fb64e0d504f0033f8873bd1d40dbc4`)

## tools-permissions (1 claim(s))

- [observation/documented] The runtime requires a GitLab personal access token with api, read_repository, and write_repository scopes, plus a GITHUB_TOKEN fine-grained PAT with the Copilot Requests permission. -- evidence: [README.md#L98-L103](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L98-L103), [README.md#L150-L154](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L150-L154) (`clm_b600718a0bf4d4355fd2ef5d8fdacd99ae51e13550758ff37ea3992c8415de7e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Required tools include a GitLab account with API access, a GitLab Runner with Docker/Kubernetes executor, GitHub Copilot CLI access with subscription, and optionally Docker for the webhook service. -- evidence: [README.md#L92-L95](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L92-L95) (`clm_34d98dff602041712f0da0f8860ef2215c02baad62c1f40b10fd63d0eed944aa`)
- [observation/documented] CI/CD execution uses a Docker image satomic/copilot-cli:latest with GitHub Copilot CLI installed and authentication pre-configured to read the GITHUB_TOKEN environment variable; users may alternatively build their own image. -- evidence: [README.md#L165-L167](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L165-L167), [README.md#L174-L176](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L174-L176), [README.md#L178-L178](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/README.md#L178-L178) (`clm_d7304bf37728c311a589239b04da7353396c380af3a88003280fef7bf7130ede`)

## limitations (1 claim(s))

- [observation/documented] The i18n documentation lists future enhancements including dynamic language detection from GitLab user preferences, language-specific formatting rules, and automated template validation; UI message localization is marked optional. -- evidence: [I18N_README.md#L322-L325](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L322-L325), [I18N_README.md#L264-L264](https://github.com/satomic/gitlab-copilot-coding-agent/blob/c768d1266af5c118f5461ea7d47353d2ef03a3cc/I18N_README.md#L264-L264) (`clm_1626cc95090f2e367a7d996c268861164d4a1142daeb9a0247156a54d9141e2e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

