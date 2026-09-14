---
access: public
aliases: []
claim_ids:
- clm_0633550c31d74b3f5608a8a5176dd50d01a5f9153f6da5d17259870a9c51ca6d
- clm_176b920dc593caafc5c5652ba98c8618da11994aad799ff3cd7704e813ce7c13
- clm_1813c09faa7dd08f082d74dceb9c06b2709f075e7186a5162c470f0a7d67c70f
- clm_3174da958940b56144bf39d271bb895e41d19347e22817c50f622b70d8756acc
- clm_38688547e6d89331173e2c045c5b354fcf7583b13a8876df055b0b65ea2eed51
- clm_b009da95f3270b7a6a88b3e347cce921fb4c46bcfe1970fd37c83357acdf06da
- clm_b75cb5f2ac81680daf71174d139e8913156e4e0bcd44a9b3a7c48fcbce2a1e0e
- clm_c36d6b0874ac3b687127139284eb154224f3a739e2d2e09bb467b08b77774e78
- clm_ccc0fa8621d7ad72179b1753a5fe6ca5b90df03004fe386b49eab1cb7c1fb1e8
- clm_d4ec3b97e2d827b15a60d5ebb8c0728b5319be39278b5e5ff1b5d31af4c381a1
- clm_f85707b057404a08e08b15c62aaf8f1520fe49896268c867dae993e9e226d554
maturity: draft
page_id: pg_e33739dba98855fdac35f4e833c79c8f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eca5c23f34c858c182cb22116e53b9f3
title: The-PR-Agent/pr-agent/README.md @ d24b6f36e787
updated_at: '2026-09-14T04:25:33Z'
---

# The-PR-Agent/pr-agent/README.md @ d24b6f36e787

<!-- rcw:begin owner=source:src_eca5c23f34c858c182cb22116e53b9f3 block=evidence -->
- Repository development practice: for local verification, run 'PYTHONPATH=. uv run pytest' from the repo root, which discovers the unit-test suite under tests/unittest; e2e tests under tests/e2e_tests need provider credentials and are invoked explicitly. [@claim:clm_0633550c31d74b3f5608a8a5176dd50d01a5f9153f6da5d17259870a9c51ca6d]
- PR-Agent is an open-source, AI-powered code review agent donated by Qodo to the community; it is distinct from Qodo's primary commercial offering and now lives in the PR-Agent GitHub org with an external maintainer. [@claim:clm_176b920dc593caafc5c5652ba98c8618da11994aad799ff3cd7704e813ce7c13]
- The product can run as a GitHub Action triggered on pull_request opened/synchronize events, configured via a workflow file that supplies OPENAI_KEY and GITHUB_TOKEN secrets. [@claim:clm_1813c09faa7dd08f082d74dceb9c06b2709f075e7186a5162c470f0a7d67c70f]
- Review behavior is customizable through JSON-based prompting in configuration files such as pr_agent/settings/configuration.toml. [@claim:clm_3174da958940b56144bf39d271bb895e41d19347e22817c50f622b70d8756acc]
- Each core tool (/review, /improve, /ask) is described as using a single LLM call, taking roughly 30 seconds at low cost. [@claim:clm_38688547e6d89331173e2c045c5b354fcf7583b13a8876df055b0b65ea2eed51]
- Docker images for version 0.34.2 and later are published under the pragent/pr-agent Docker Hub namespace; older codiumai/pr-agent tags are a frozen archive with no new pushes. [@claim:clm_b009da95f3270b7a6a88b3e347cce921fb4c46bcfe1970fd37c83357acdf06da]
- PR-Agent tools can be invoked by commenting commands like /describe, /review, /improve, and /ask on a pull request, or locally via a CLI such as 'pr-agent --pr_url <PR_URL> review'. [@claim:clm_b75cb5f2ac81680daf71174d139e8913156e4e0bcd44a9b3a7c48fcbce2a1e0e]
- The /help_docs tool is temporarily disabled since v0.36.1 pending a fix for a credential-exposure issue (issue #2445). [@claim:clm_c36d6b0874ac3b687127139284eb154224f3a739e2d2e09bb467b08b77774e78]
- The tool is installable via pip ('pip install pr-agent') and run locally against a repository using an OPENAI_KEY environment variable. [@claim:clm_ccc0fa8621d7ad72179b1753a5fe6ca5b90df03004fe386b49eab1cb7c1fb1e8]
- A PR compression strategy converts code diffs into manageable LLM prompts, and the README claims it handles both small and large PRs. [@claim:clm_d4ec3b97e2d827b15a60d5ebb8c0728b5319be39278b5e5ff1b5d31af4c381a1]
- Supported AI models include OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek, Mistral, and any model reachable through LiteLLM (e.g. Azure OpenAI, AWS Bedrock, Vertex AI, Ollama). [@claim:clm_f85707b057404a08e08b15c62aaf8f1520fe49896268c867dae993e9e226d554]
<!-- rcw:end owner=source:src_eca5c23f34c858c182cb22116e53b9f3 block=evidence -->

## Researcher notes

