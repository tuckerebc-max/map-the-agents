# the-pr-agent/pr-agent -- full detail

[Back to orientation](pr-agent.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/the-pr-agent/pr-agent/d24b6f36e7871829ad8f29e884b4577fb3902f16/80d4ad7ef368be71.json](../../../wiki/dossiers/the-pr-agent/pr-agent/d24b6f36e7871829ad8f29e884b4577fb3902f16/80d4ad7ef368be71.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Each core tool (/review, /improve, /ask) is described as using a single LLM call, taking roughly 30 seconds at low cost. -- evidence: [README.md#L114-L114](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L114-L114) (`clm_38688547e6d89331173e2c045c5b354fcf7583b13a8876df055b0b65ea2eed51`)
- [observation/documented] A PR compression strategy converts code diffs into manageable LLM prompts, and the README claims it handles both small and large PRs. -- evidence: [README.md#L116-L116](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L116-L116), [docs/docs/index.md#L85-L85](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/index.md#L85-L85) (`clm_d4ec3b97e2d827b15a60d5ebb8c0728b5319be39278b5e5ff1b5d31af4c381a1`)
- [observation/documented] Review behavior is customizable through JSON-based prompting in configuration files such as pr_agent/settings/configuration.toml. -- evidence: [README.md#L118-L118](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L118-L118) (`clm_3174da958940b56144bf39d271bb895e41d19347e22817c50f622b70d8756acc`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: for local verification, run 'PYTHONPATH=. uv run pytest' from the repo root, which discovers the unit-test suite under tests/unittest; e2e tests under tests/e2e_tests need provider credentials and are invoked explicitly. -- evidence: [README.md#L210-L210](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L210-L210) (`clm_0633550c31d74b3f5608a8a5176dd50d01a5f9153f6da5d17259870a9c51ca6d`)

## skills-patterns (2 claim(s))

- [observation/documented] Agent Skills use a SKILL.md format: a directory with a markdown file whose YAML frontmatter carries name and description, followed by a markdown body of review guidance. -- evidence: [docs/docs/core-abilities/agent_skills.md#L9-L13](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L9-L13), [docs/docs/core-abilities/agent_skills.md#L7-L7](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L7-L7) (`clm_56a80641befb4b89feccbff5575c0bacc1720455b2a25aefdeb61daffc65d8ca`)
- [observation/documented] When enabled, PR-Agent discovers SKILL.md files under configured paths and injects each skill's name, description, and body into the /review, /improve, /describe, and top-level /ask prompts alongside extra_instructions. -- evidence: [docs/docs/core-abilities/agent_skills.md#L22-L22](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L22-L22) (`clm_0c0562a4b7ea69a1b4fb73240a06fe56a04021739851f9883684dc7b67566a64`)

## interfaces (5 claim(s))

- [observation/documented] PR-Agent tools can be invoked by commenting commands like /describe, /review, /improve, and /ask on a pull request, or locally via a CLI such as 'pr-agent --pr_url <PR_URL> review'. -- evidence: [README.md#L176-L176](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L176-L176), [README.md#L180-L183](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L180-L183), [README.md#L186-L187](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L186-L187) (`clm_b75cb5f2ac81680daf71174d139e8913156e4e0bcd44a9b3a7c48fcbce2a1e0e`)
- [observation/documented] The product can run as a GitHub Action triggered on pull_request opened/synchronize events, configured via a workflow file that supplies OPENAI_KEY and GITHUB_TOKEN secrets. -- evidence: [README.md#L72-L86](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L72-L86) (`clm_1813c09faa7dd08f082d74dceb9c06b2709f075e7186a5162c470f0a7d67c70f`)
- [observation/documented] The tool is installable via pip ('pip install pr-agent') and run locally against a repository using an OPENAI_KEY environment variable. -- evidence: [README.md#L92-L97](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L92-L97) (`clm_ccc0fa8621d7ad72179b1753a5fe6ca5b90df03004fe386b49eab1cb7c1fb1e8`)
- [observation/documented] The feature matrix lists tools including Describe, Review, Improve, Ask, Add Docs, Generate Labels, and Similar Issues, with per-provider support varying (e.g. Ask lacks Gitea support; Similar Issues is GitHub-only). -- evidence: [docs/docs/index.md#L23-L50](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/index.md#L23-L50) (`clm_c09800861b24d85226afdcc851ff75b11e6666b2e9a770c16673083d3d4cd89a`)
- [observation/documented] A /help command lets users ask natural-language questions in a PR comment, and the bot responds with an answer including relevant documentation links. -- evidence: [docs/docs/index.md#L15-L15](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/index.md#L15-L15), [docs/docs/index.md#L17-L17](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/index.md#L17-L17) (`clm_857d53436936acd1bba85e66c6715e19a72907a4b60e5e8072d02c79fb020be7`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] skills.paths is host-level only: it cannot be set from a repository's .pr_agent.toml, and repo-supplied values are ignored with a warning, to prevent malicious repos from pointing the scan at sensitive host files. -- evidence: [docs/docs/core-abilities/agent_skills.md#L44-L44](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L44-L44), [docs/docs/core-abilities/agent_skills.md#L41-L42](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L41-L42) (`clm_1f642a8b20b4c16442496d356e6c8b9a98f08ce6e6b1c36742583cec868cf31b`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Supported AI models include OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek, Mistral, and any model reachable through LiteLLM (e.g. Azure OpenAI, AWS Bedrock, Vertex AI, Ollama). -- evidence: [README.md#L120-L123](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L120-L123) (`clm_f85707b057404a08e08b15c62aaf8f1520fe49896268c867dae993e9e226d554`)
- [observation/documented] Docker images for version 0.34.2 and later are published under the pragent/pr-agent Docker Hub namespace; older codiumai/pr-agent tags are a frozen archive with no new pushes. -- evidence: [README.md#L61-L62](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L61-L62), [RELEASE_NOTES.md#L7-L9](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/RELEASE_NOTES.md#L7-L9) (`clm_b009da95f3270b7a6a88b3e347cce921fb4c46bcfe1970fd37c83357acdf06da`)

## limitations (2 claim(s))

- [observation/documented] The /help_docs tool is temporarily disabled since v0.36.1 pending a fix for a credential-exposure issue (issue #2445). -- evidence: [docs/docs/index.md#L52-L52](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/index.md#L52-L52), [README.md#L137-L137](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L137-L137) (`clm_c36d6b0874ac3b687127139284eb154224f3a739e2d2e09bb467b08b77774e78`)
- [observation/documented] Because PR-Agent makes single-shot model calls with no tool-use loop, the agent-skills progressive-disclosure model is not implementable; all enabled skill text is loaded into every prompt (bounded by max_skills_tokens), and skills needing script execution or binary assets will not work. -- evidence: [docs/docs/core-abilities/agent_skills.md#L58-L58](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L58-L58), [docs/docs/core-abilities/agent_skills.md#L50-L52](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/docs/docs/core-abilities/agent_skills.md#L50-L52) (`clm_5d2a7d1e95113ebcbe914a5e8a694f4624d007c914b54c5939dc2ebe42da071c`)

## relevance (1 claim(s))

- [observation/documented] PR-Agent is an open-source, AI-powered code review agent donated by Qodo to the community; it is distinct from Qodo's primary commercial offering and now lives in the PR-Agent GitHub org with an external maintainer. -- evidence: [README.md#L217-L217](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L217-L217), [README.md#L219-L219](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L219-L219), [README.md#L27-L27](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L27-L27), [README.md#L229-L229](https://github.com/The-PR-Agent/pr-agent/blob/d24b6f36e7871829ad8f29e884b4577fb3902f16/README.md#L229-L229) (`clm_176b920dc593caafc5c5652ba98c8618da11994aad799ff3cd7704e813ce7c13`)

