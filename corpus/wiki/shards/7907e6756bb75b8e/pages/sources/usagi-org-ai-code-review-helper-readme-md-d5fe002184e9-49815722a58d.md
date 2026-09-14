---
access: public
aliases: []
claim_ids:
- clm_3044d8e0829b9033c758033e1648098b154eea21e3fee1a48508f3c9f3592065
- clm_396e42fa69bc837f1a30d9234051ea7a4a9f83ba4a702fdb5ac1fc5a20972ac4
- clm_6138bea51456dccdd3e0db49e591a3621735e944f7a9ca3fa801c056b6caace6
- clm_68018abaa9014456143de0f2fff6cad64915eb4d9f678bd3697f56be506d768d
- clm_77a60106b50a8efcf8930d54d6c1044dbc5ed8dae3ac1fe253d9c87f22823919
- clm_8cbd85d3da138c27986b2cee0f3b2b16d04f20e37eb37b63e29c21ec6d76dbf6
- clm_90d14d723cedaa225fa03f89f1a71b2ea300a22381b6ca7a81e49949f3837a5b
- clm_a033501be3f935dcac4603724d8dd5cad1bcb8df43119dac84db8cdc79cf62d7
- clm_cbff012f3a7b26bf9641db0e59fabdfc3190c788db2c395a756ce8bbee7960a4
- clm_ce1fa3b20b7cc33e0e8c5d38e4d76cd84a5d5e9dd570e746367f5eaa2041c6fe
- clm_d2f8e3791403402fcbcaba41b263f0cd625cf38438b5dd1c956aad14f498420e
maturity: draft
page_id: pg_0cf712b6da58582f9b5f49815722a58d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b2718afb11f55f5ebf6a124f1e05e591
title: Usagi-org/ai-code-review-helper/README.md @ d5fe002184e9
updated_at: '2026-09-14T04:28:52Z'
---

# Usagi-org/ai-code-review-helper/README.md @ d5fe002184e9

<!-- rcw:begin owner=source:src_b2718afb11f55f5ebf6a124f1e05e591 block=evidence -->
- General review mode uses /github_webhook_general and /gitlab_webhook_general endpoints, producing one Markdown summary comment per changed file. [@claim:clm_3044d8e0829b9033c758033e1648098b154eea21e3fee1a48508f3c9f3592065]
- Global configuration is loaded from environment variables; runtime changes made via the admin panel take effect immediately but are reloaded from environment variables on restart, so env vars are recommended for persistent global config. [@claim:clm_396e42fa69bc837f1a30d9234051ea7a4a9f83ba4a702fdb5ac1fc5a20972ac4]
- Repository development practice: local development involves cloning the repo, creating a virtualenv, installing requirements.txt, starting via python -m api.ai_code_review_helper, and optionally running tests with python -m unittest discover tests. [@claim:clm_6138bea51456dccdd3e0db49e591a3621735e944f7a9ca3fa801c056b6caace6]
- A web admin panel at /admin and a RESTful config API under /config/* manage webhook secrets, tokens, LLM parameters, and notification URLs; API calls require an X-Admin-API-Key header. [@claim:clm_68018abaa9014456143de0f2fff6cad64915eb4d9f678bd3697f56be506d768d]
- Detailed review mode exposes endpoints /github_webhook and /gitlab_webhook, where the AI analyzes each changed file and the system converts JSON model output into multiple structured comments. [@claim:clm_77a60106b50a8efcf8930d54d6c1044dbc5ed8dae3ac1fe253d9c87f22823919]
- The product is described as an LLM-based automated code review assistant that listens to PR/MR changes via GitHub/GitLab webhooks, analyzes code with AI, and posts review comments automatically. [@claim:clm_8cbd85d3da138c27986b2cee0f3b2b16d04f20e37eb37b63e29c21ec6d76dbf6]
- Review summaries including PR/MR links, branch info, and result overviews can be sent to WeCom (enterprise WeChat) bots and custom webhook URLs. [@claim:clm_90d14d723cedaa225fa03f89f1a71b2ea300a22381b6ca7a81e49949f3837a5b]
- Redis stores repository/project configuration, processed commit SHAs, and AI review results with a default 7-day expiry; records for closed/merged PRs/MRs are cleaned up, and the service strongly depends on Redis. [@claim:clm_a033501be3f935dcac4603724d8dd5cad1bcb8df43119dac84db8cdc79cf62d7]
- The service posts review comments asynchronously, publishes a summary comment after all files are reviewed, and uses Redis to prevent duplicate reviews of the same commit. [@claim:clm_cbff012f3a7b26bf9641db0e59fabdfc3190c788db2c395a756ce8bbee7960a4]
- Configuration uses OpenAI-compatible LLM settings (OPENAI_API_KEY, OPENAI_MODEL defaulting to gpt-4o, and an optional OPENAI_API_BASE_URL). [@claim:clm_ce1fa3b20b7cc33e0e8c5d38e4d76cd84a5d5e9dd570e746367f5eaa2041c6fe]
- All admin operations are authenticated with a key set via the ADMIN_API_KEY environment variable, whose default value is documented and flagged as must-change. [@claim:clm_d2f8e3791403402fcbcaba41b263f0cd625cf38438b5dd1c956aad14f498420e]
<!-- rcw:end owner=source:src_b2718afb11f55f5ebf6a124f1e05e591 block=evidence -->

## Researcher notes

