---
access: public
aliases: []
claim_ids:
- clm_1a9caae5c6a814b2ddf1003b0741221df7c49f37936b0d1bef9b30ae94556021
- clm_30298d82f98ebae25a8a13a4740d32a4b877bb2ef03e651f55bac1adeaca8005
- clm_30db35620469a1b2153e76249e09c65a4e4081e83c651af3fe46796bf1c92f97
- clm_36b34bb3978f7b4ca98b7d5d86b83a8f00301b5c132feaf753613f9ec431294d
- clm_726c396279c7108e8fe733963f2dfd93807afe634aad74501443b352d5e8d02e
- clm_78dbc26a8b0f0fbda28f2dc69b3c807cf69f8092254fff86c1c45463758a3c25
- clm_a371e45e86c7ab740d6c9e2103aa026a480e05b6c95fac133ce82df6d1b81b1b
- clm_b0bcd6e08240884581039f57c28a44bffac53308425deac55f0d83ac28df2bf3
- clm_b610db0cc560b83c7711ff8d56320834666d5b40946e53589cfcfbf8bc4b8865
- clm_cfc8d2ffb7b8a827046c85f618bb19433e0e726cacbfca58896e9b28b4b60371
- clm_f266fbf407a1e954f97e1043b4288a7617ef651021341bf16fb41d4fae4ee83b
maturity: draft
page_id: pg_bc9b421edc51565d82dece27d4c6dc6f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ab22b94920ed55d099016db90c7bd50b
title: a115/iCODES/README.md @ 8961152cb0a9
updated_at: '2026-09-14T03:29:37Z'
---

# a115/iCODES/README.md @ 8961152cb0a9

<!-- rcw:begin owner=source:src_ab22b94920ed55d099016db90c7bd50b block=evidence -->
- Repository development practice: when installing from a cloned repo, Poetry is recommended for dependency management via 'poetry install', and commands are prefixed with 'poetry run python icodes.py'. [@claim:clm_1a9caae5c6a814b2ddf1003b0741221df7c49f37936b0d1bef9b30ae94556021]
- The tool requires Python 3.11 or higher and is installable via pip as the 'icodes' package. [@claim:clm_30298d82f98ebae25a8a13a4740d32a4b877bb2ef03e651f55bac1adeaca8005]
- The 'build-index' command generates an indexed database of commit insights for a given Git repository. [@claim:clm_30db35620469a1b2153e76249e09c65a4e4081e83c651af3fe46796bf1c92f97]
- iCODES analyzes and indexes Git commit histories using LLM techniques, summarizing commit intents and enabling semantic search over codebases. [@claim:clm_36b34bb3978f7b4ca98b7d5d86b83a8f00301b5c132feaf753613f9ec431294d]
- The CLI provides an 'inspect-repo' command taking a repository path and an optional --branch-name flag; without a branch it uses the current branch and analyzes the latest commit. [@claim:clm_726c396279c7108e8fe733963f2dfd93807afe634aad74501443b352d5e8d02e]
- The default model choice of gpt-3.5-turbo appears to reflect a deliberate price/quality tradeoff stated in the documentation. [@claim:clm_78dbc26a8b0f0fbda28f2dc69b3c807cf69f8092254fff86c1c45463758a3c25]
- The only supported LLM backend is OpenAI; the OPENAI_API_KEY environment variable must be exported, and DEFAULT_MODEL selects the GPT model (default gpt-3.5-turbo). [@claim:clm_a371e45e86c7ab740d6c9e2103aa026a480e05b6c95fac133ce82df6d1b81b1b]
- Semantic search and a web-based UI are listed as 'coming soon' features, indicating they are not yet available in the current tool. [@claim:clm_b0bcd6e08240884581039f57c28a44bffac53308425deac55f0d83ac28df2bf3]
- The tool targets developers seeking to understand and navigate codebases by analyzing commit history, trends, and code evolution patterns. [@claim:clm_b610db0cc560b83c7711ff8d56320834666d5b40946e53589cfcfbf8bc4b8865]
- A 'suggest_commit_message' command retrieves currently staged changes, formats them commit-like, and uses the LLM to suggest a commit message shown in console output. [@claim:clm_cfc8d2ffb7b8a827046c85f618bb19433e0e726cacbfca58896e9b28b4b60371]
- The 'search' command accepts a query plus optional --author, --file, --start-date, and --end-date filters (dates in YYYY-MM-DD format) to find relevant commits. [@claim:clm_f266fbf407a1e954f97e1043b4288a7617ef651021341bf16fb41d4fae4ee83b]
<!-- rcw:end owner=source:src_ab22b94920ed55d099016db90c7bd50b block=evidence -->

## Researcher notes

