# usagi-org/ai-code-review-helper -- full detail

[Back to orientation](ai-code-review-helper.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/usagi-org/ai-code-review-helper/d5fe002184e934d39c5032a584f23015cbc33919/af94f1b37c8fe238.json](../../../wiki/dossiers/usagi-org/ai-code-review-helper/d5fe002184e934d39c5032a584f23015cbc33919/af94f1b37c8fe238.json)

## specifications (1 claim(s))

- [observation/documented] The product is described as an LLM-based automated code review assistant that listens to PR/MR changes via GitHub/GitLab webhooks, analyzes code with AI, and posts review comments automatically. -- evidence: [README.md#L14-L14](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L14-L14) (`clm_8cbd85d3da138c27986b2cee0f3b2b16d04f20e37eb37b63e29c21ec6d76dbf6`)

## components (1 claim(s))

- [observation/documented] The service posts review comments asynchronously, publishes a summary comment after all files are reviewed, and uses Redis to prevent duplicate reviews of the same commit. -- evidence: [README.md#L21-L42](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L21-L42) (`clm_cbff012f3a7b26bf9641db0e59fabdfc3190c788db2c395a756ce8bbee7960a4`)

## design-choices (1 claim(s))

- [observation/documented] Global configuration is loaded from environment variables; runtime changes made via the admin panel take effect immediately but are reloaded from environment variables on restart, so env vars are recommended for persistent global config. -- evidence: [README.md#L89-L91](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L89-L91) (`clm_396e42fa69bc837f1a30d9234051ea7a4a9f83ba4a702fdb5ac1fc5a20972ac4`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: local development involves cloning the repo, creating a virtualenv, installing requirements.txt, starting via python -m api.ai_code_review_helper, and optionally running tests with python -m unittest discover tests. -- evidence: [README.md#L130-L130](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L130-L130), [README.md#L133-L134](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L133-L134), [README.md#L117-L118](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L117-L118), [README.md#L121-L122](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L121-L122), [README.md#L125-L125](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L125-L125) (`clm_6138bea51456dccdd3e0db49e591a3621735e944f7a9ca3fa801c056b6caace6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Detailed review mode exposes endpoints /github_webhook and /gitlab_webhook, where the AI analyzes each changed file and the system converts JSON model output into multiple structured comments. -- evidence: [README.md#L21-L42](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L21-L42), [README.md#L105-L112](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L105-L112) (`clm_77a60106b50a8efcf8930d54d6c1044dbc5ed8dae3ac1fe253d9c87f22823919`)
- [observation/documented] General review mode uses /github_webhook_general and /gitlab_webhook_general endpoints, producing one Markdown summary comment per changed file. -- evidence: [README.md#L21-L42](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L21-L42), [README.md#L105-L112](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L105-L112) (`clm_3044d8e0829b9033c758033e1648098b154eea21e3fee1a48508f3c9f3592065`)
- [observation/documented] A web admin panel at /admin and a RESTful config API under /config/* manage webhook secrets, tokens, LLM parameters, and notification URLs; API calls require an X-Admin-API-Key header. -- evidence: [README.md#L81-L87](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L81-L87) (`clm_68018abaa9014456143de0f2fff6cad64915eb4d9f678bd3697f56be506d768d`)
- [observation/documented] Review summaries including PR/MR links, branch info, and result overviews can be sent to WeCom (enterprise WeChat) bots and custom webhook URLs. -- evidence: [README.md#L21-L42](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L21-L42) (`clm_90d14d723cedaa225fa03f89f1a71b2ea300a22381b6ca7a81e49949f3837a5b`)

## memory-state (1 claim(s))

- [observation/documented] Redis stores repository/project configuration, processed commit SHAs, and AI review results with a default 7-day expiry; records for closed/merged PRs/MRs are cleaned up, and the service strongly depends on Redis. -- evidence: [README.md#L89-L91](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L89-L91), [README.md#L137-L140](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L137-L140) (`clm_a033501be3f935dcac4603724d8dd5cad1bcb8df43119dac84db8cdc79cf62d7`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] All admin operations are authenticated with a key set via the ADMIN_API_KEY environment variable, whose default value is documented and flagged as must-change. -- evidence: [README.md#L81-L87](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L81-L87), [README.md#L68-L78](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L68-L78) (`clm_d2f8e3791403402fcbcaba41b263f0cd625cf38438b5dd1c956aad14f498420e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The requirements file lists Flask, openai, requests, redis, and pyyaml as dependencies. -- evidence: [requirements.txt#L1-L5](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/requirements.txt#L1-L5) (`clm_7e9d76b9a1962ebf159b63d5bd6a70101ab75927f87d220b7f62a4e4ea606c28`)
- [observation/documented] Configuration uses OpenAI-compatible LLM settings (OPENAI_API_KEY, OPENAI_MODEL defaulting to gpt-4o, and an optional OPENAI_API_BASE_URL). -- evidence: [README.md#L49-L58](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L49-L58), [README.md#L68-L78](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L68-L78) (`clm_ce1fa3b20b7cc33e0e8c5d38e4d76cd84a5d5e9dd570e746367f5eaa2041c6fe`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

