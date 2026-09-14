---
access: public
aliases: []
claim_ids:
- clm_093151856b13ad41e18ecc29bd8a5fdef28d700fe3ea79e9b22a3567bf469a6c
- clm_6183ce7d173605aa25791649b52ffff3ba39820b2efe6ae5b240f0e77d97728c
- clm_7a1b9b56843b0b79057dffdb8c191f497836f96227130f7b93fa9cd2cb7e9d8d
- clm_8499d84fac7f5f6871b73b7147173d21c4a67518e295aa231fde6dfcd31d8a7d
- clm_8d2c3d974136cb1e615832831f9942a70a3375da3471d23fad251d57febc4402
- clm_a72e86ec58a8761448c579e3ce2f3cda22e281c645304589145d3b9f39220ef5
- clm_c3e9a2a6b040c7af5665febd9459b609688a256a2957067babb9ad1e38bf254b
- clm_ce68d7bcecc4a68256ede98017a8735755323d20a3e55ce3edfcc1b57bac88d1
- clm_d698035f22bcae36487753bcbcb338160ad8be2cad062dae3bd1588b71c5eb19
- clm_db19fdfad3373e12209584316d20cc5b0beec70db314d14fd25d780f85d04c44
- clm_e7ea24fa5edf3cf387896357dd5e56e8bd4f870a8adff6e99c920636eafa6788
- clm_fc800a4e3f127501541213d77e3b301629f9165b6a3c42fbad6a8aa0fbbdcb0e
maturity: draft
page_id: pg_3b77a413c8c653568dbe020f4d815016
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_39e51b78f3af578681592735ca2de8fe
title: shaftoe/pi-coding-agent-action/README.md @ d90187d4bc85
updated_at: '2026-09-14T04:20:52Z'
---

# shaftoe/pi-coding-agent-action/README.md @ d90187d4bc85

<!-- rcw:begin owner=source:src_39e51b78f3af578681592735ca2de8fe block=evidence -->
- With update_comment enabled, the action overwrites its own prior comment by locating a hidden HTML marker at the comment start, leaving other users' comments untouched; it defaults to false and falls back to creating a new comment. [@claim:clm_093151856b13ad41e18ecc29bd8a5fdef28d700fe3ea79e9b22a3567bf469a6c]
- Session sharing uploads exported session HTML to a gist (GitHub Gists by default, or a self-hosted Opengist instance) and surfaces a viewer link in the job log and step summary; enabling it auto-enables HTML export. [@claim:clm_6183ce7d173605aa25791649b52ffff3ba39820b2efe6ae5b240f0e77d97728c]
- Because CI has no interactive user to approve trust, the action always marks the workspace as trusted (projectTrusted: true), so repository files like AGENTS.md, .pi settings, and project extensions are loaded and followed by the agent. [@claim:clm_7a1b9b56843b0b79057dffdb8c191f497836f96227130f7b93fa9cd2cb7e9d8d]
- The action is bundled into a single dist/index.js with esbuild so no node_modules are needed at runtime; non-code Pi SDK assets are copied to dist/pi-sdk/ and resolved via the PI_PACKAGE_DIR environment variable. [@claim:clm_8499d84fac7f5f6871b73b7147173d21c4a67518e295aa231fde6dfcd31d8a7d]
- GitHub's GITHUB_TOKEN can never create or modify files under .github/workflows/ even with contents: write; PRs touching workflow files require a personal access token with the workflow scope. [@claim:clm_8d2c3d974136cb1e615832831f9942a70a3375da3471d23fad251d57febc4402]
- A README dependency table lists bundled packages including @earendil-works/pi-coding-agent 0.85.1, @actions/core 3.0.1, @actions/github 9.1.1, Octokit packages, simple-git 3.36.0, and typebox 1.3.6; the table is auto-updated by a workflow. [@claim:clm_a72e86ec58a8761448c579e3ce2f3cda22e281c645304589145d3b9f39220ef5]
- The action accepts inputs including provider, model, token, github_token, base_url, thinking_level, prompt, pr_number, extensions, loaded_tools, update_comment, share_session, and branch_name_template, per documented examples. [@claim:clm_c3e9a2a6b040c7af5665febd9459b609688a256a2957067babb9ad1e38bf254b]
- Custom Pi extensions can be loaded from npm packages (npm:name[@version]), git repositories (git:host/user/repo with optional #branch), or local .ts files via the extensions input. [@claim:clm_ce68d7bcecc4a68256ede98017a8735755323d20a3e55ce3edfcc1b57bac88d1]
- By default the action loads all built-in GitHub tools; load_builtin_extensions can disable them, and loaded_tools (default 'all') restricts the session to a named subset, failing early on unrecognized tool names. [@claim:clm_d698035f22bcae36487753bcbcb338160ad8be2cad062dae3bd1588b71c5eb19]
- Shared secret gists are URL-obscured rather than access-controlled, so anyone with the link can read the rendered session, which may include code or secrets the agent touched. [@claim:clm_db19fdfad3373e12209584316d20cc5b0beec70db314d14fd25d780f85d04c44]
- The action exposes outputs such as success, response, cost, input_tokens, output_tokens, duration_seconds, share_url, gist_url, gist_id, session_html_path, and session_jsonl_path for downstream steps. [@claim:clm_e7ea24fa5edf3cf387896357dd5e56e8bd4f870a8adff6e99c920636eafa6788]
- The AWS Bedrock provider and its @aws-sdk/client-bedrock-runtime dependency are bundled into dist/index.js and statically registered at startup, adding roughly 500 KB to the action bundle. [@claim:clm_fc800a4e3f127501541213d77e3b301629f9165b6a3c42fbad6a8aa0fbbdcb0e]
<!-- rcw:end owner=source:src_39e51b78f3af578681592735ca2de8fe block=evidence -->

## Researcher notes

