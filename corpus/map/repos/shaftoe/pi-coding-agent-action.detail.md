# shaftoe/pi-coding-agent-action -- full detail

[Back to orientation](pi-coding-agent-action.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shaftoe/pi-coding-agent-action/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/0790f41e3e8b35f6.json](../../../wiki/dossiers/shaftoe/pi-coding-agent-action/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/0790f41e3e8b35f6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The action is bundled into a single dist/index.js with esbuild so no node_modules are needed at runtime; non-code Pi SDK assets are copied to dist/pi-sdk/ and resolved via the PI_PACKAGE_DIR environment variable. -- evidence: [README.md#L66-L66](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L66-L66) (`clm_8499d84fac7f5f6871b73b7147173d21c4a67518e295aa231fde6dfcd31d8a7d`)
- [observation/documented] Because CI has no interactive user to approve trust, the action always marks the workspace as trusted (projectTrusted: true), so repository files like AGENTS.md, .pi settings, and project extensions are loaded and followed by the agent. -- evidence: [README.md#L51-L53](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L51-L53) (`clm_7a1b9b56843b0b79057dffdb8c191f497836f96227130f7b93fa9cd2cb7e9d8d`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The action accepts inputs including provider, model, token, github_token, base_url, thinking_level, prompt, pr_number, extensions, loaded_tools, update_comment, share_session, and branch_name_template, per documented examples. -- evidence: [README.md#L377-L388](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L377-L388), [README.md#L128-L137](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L128-L137), [README.md#L284-L292](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L284-L292), [README.md#L758-L766](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L758-L766), [README.md#L467-L479](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L467-L479), [README.md#L234-L242](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L234-L242), [README.md#L590-L602](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L590-L602), [README.md#L143-L152](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L143-L152) (`clm_c3e9a2a6b040c7af5665febd9459b609688a256a2957067babb9ad1e38bf254b`)
- [observation/documented] The action exposes outputs such as success, response, cost, input_tokens, output_tokens, duration_seconds, share_url, gist_url, gist_id, session_html_path, and session_jsonl_path for downstream steps. -- evidence: [README.md#L748-L748](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L748-L748), [README.md#L690-L700](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L690-L700), [README.md#L717-L717](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L717-L717) (`clm_e7ea24fa5edf3cf387896357dd5e56e8bd4f870a8adff6e99c920636eafa6788`)
- [observation/documented] With update_comment enabled, the action overwrites its own prior comment by locating a hidden HTML marker at the comment start, leaving other users' comments untouched; it defaults to false and falls back to creating a new comment. -- evidence: [README.md#L265-L265](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L265-L265), [README.md#L296-L299](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L296-L299) (`clm_093151856b13ad41e18ecc29bd8a5fdef28d700fe3ea79e9b22a3567bf469a6c`)
- [observation/documented] Session sharing uploads exported session HTML to a gist (GitHub Gists by default, or a self-hosted Opengist instance) and surfaces a viewer link in the job log and step summary; enabling it auto-enables HTML export. -- evidence: [README.md#L750-L750](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L750-L750), [README.md#L743-L744](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L743-L744), [README.md#L748-L748](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L748-L748), [README.md#L741-L741](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L741-L741) (`clm_6183ce7d173605aa25791649b52ffff3ba39820b2efe6ae5b240f0e77d97728c`)
- [observation/documented] Custom Pi extensions can be loaded from npm packages (npm:name[@version]), git repositories (git:host/user/repo with optional #branch), or local .ts files via the extensions input. -- evidence: [README.md#L481-L484](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L481-L484), [README.md#L467-L479](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L467-L479) (`clm_ce68d7bcecc4a68256ede98017a8735755323d20a3e55ce3edfcc1b57bac88d1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] By default the action loads all built-in GitHub tools; load_builtin_extensions can disable them, and loaded_tools (default 'all') restricts the session to a named subset, failing early on unrecognized tool names. -- evidence: [README.md#L606-L607](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L606-L607), [README.md#L588-L588](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L588-L588), [README.md#L571-L571](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L571-L571), [README.md#L604-L604](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L604-L604) (`clm_d698035f22bcae36487753bcbcb338160ad8be2cad062dae3bd1588b71c5eb19`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] A README dependency table lists bundled packages including @earendil-works/pi-coding-agent 0.85.1, @actions/core 3.0.1, @actions/github 9.1.1, Octokit packages, simple-git 3.36.0, and typebox 1.3.6; the table is auto-updated by a workflow. -- evidence: [README.md#L74-L86](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L74-L86), [README.md#L90-L90](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L90-L90) (`clm_a72e86ec58a8761448c579e3ce2f3cda22e281c645304589145d3b9f39220ef5`)
- [observation/documented] The AWS Bedrock provider and its @aws-sdk/client-bedrock-runtime dependency are bundled into dist/index.js and statically registered at startup, adding roughly 500 KB to the action bundle. -- evidence: [README.md#L566-L567](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L566-L567) (`clm_fc800a4e3f127501541213d77e3b301629f9165b6a3c42fbad6a8aa0fbbdcb0e`)

## limitations (2 claim(s))

- [observation/documented] GitHub's GITHUB_TOKEN can never create or modify files under .github/workflows/ even with contents: write; PRs touching workflow files require a personal access token with the workflow scope. -- evidence: [README.md#L48-L49](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L48-L49) (`clm_8d2c3d974136cb1e615832831f9942a70a3375da3471d23fad251d57febc4402`)
- [observation/documented] Shared secret gists are URL-obscured rather than access-controlled, so anyone with the link can read the rendered session, which may include code or secrets the agent touched. -- evidence: [README.md#L755-L756](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L755-L756) (`clm_db19fdfad3373e12209584316d20cc5b0beec70db314d14fd25d780f85d04c44`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

