# usagi-org/ai-code-review-helper

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d5fe002184e9 @ af94f1b37c8fe238

## Summary (orientation draft, not independently verified)

README evidence describes an LLM-based automated code review service that listens to GitHub/GitLab webhooks, posts AI review comments, uses Redis for config/result storage, and is deployed via Docker or Python. Evidence is documentation-only; no source code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is described as an LLM-based automated code review assistant that listens to PR/MR changes via GitHub/GitLab webhooks, analyzes code with AI, and posts review comments automatically. -- evidence: [README.md#L14-L14](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L14-L14)
- components (1 claim(s)):
  - [observation/documented] The service posts review comments asynchronously, publishes a summary comment after all files are reviewed, and uses Redis to prevent duplicate reviews of the same commit. -- evidence: [README.md#L21-L42](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L21-L42)
- design-choices (1 claim(s)):
  - [observation/documented] Global configuration is loaded from environment variables; runtime changes made via the admin panel take effect immediately but are reloaded from environment variables on restart, so env vars are recommended for persistent global config. -- evidence: [README.md#L89-L91](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L89-L91)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: local development involves cloning the repo, creating a virtualenv, installing requirements.txt, starting via python -m api.ai_code_review_helper, and optionally running tests with python -m unittest discover tests. -- evidence: [README.md#L130-L130](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L130-L130), [README.md#L133-L134](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L133-L134), [README.md#L117-L118](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L117-L118), [README.md#L121-L122](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L121-L122), [README.md#L125-L125](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L125-L125)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Detailed review mode exposes endpoints /github_webhook and /gitlab_webhook, where the AI analyzes each changed file and the system converts JSON model output into multiple structured comments. -- evidence: [README.md#L21-L42](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L21-L42), [README.md#L105-L112](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L105-L112)
  - [observation/documented] General review mode uses /github_webhook_general and /gitlab_webhook_general endpoints, producing one Markdown summary comment per changed file. -- evidence: [README.md#L21-L42](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L21-L42), [README.md#L105-L112](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L105-L112)
- memory-state (1 claim(s)):
  - [observation/documented] Redis stores repository/project configuration, processed commit SHAs, and AI review results with a default 7-day expiry; records for closed/merged PRs/MRs are cleaned up, and the service strongly depends on Redis. -- evidence: [README.md#L89-L91](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L89-L91), [README.md#L137-L140](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L137-L140)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] All admin operations are authenticated with a key set via the ADMIN_API_KEY environment variable, whose default value is documented and flagged as must-change. -- evidence: [README.md#L81-L87](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L81-L87), [README.md#L68-L78](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L68-L78)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The requirements file lists Flask, openai, requests, redis, and pyyaml as dependencies. -- evidence: [requirements.txt#L1-L5](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/requirements.txt#L1-L5)
  - [observation/documented] Configuration uses OpenAI-compatible LLM settings (OPENAI_API_KEY, OPENAI_MODEL defaulting to gpt-4o, and an optional OPENAI_API_BASE_URL). -- evidence: [README.md#L49-L58](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L49-L58), [README.md#L68-L78](https://github.com/Usagi-org/ai-code-review-helper/blob/d5fe002184e934d39c5032a584f23015cbc33919/README.md#L68-L78)
More evidence: [full detail](ai-code-review-helper.detail.md)

Metadata and full claim list: [full detail](ai-code-review-helper.detail.md)
Human notes ([notes](ai-code-review-helper.notes.md), never overwritten by build)

[Back to map index](../../index.md)
