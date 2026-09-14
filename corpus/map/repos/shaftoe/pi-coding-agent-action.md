# shaftoe/pi-coding-agent-action

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d90187d4bc85 @ 0790f41e3e8b35f6

## Summary (orientation draft, not independently verified)

README evidence documents a GitHub Actions action integrating the Pi coding agent into CI/CD, with documented inputs/outputs, tool-loading controls, session sharing/exports, bundled dependencies, and security caveats. All prior claims are retained with claim 1 revised to include branch_name_template and base_url. Evidence coverage: 130 of 296 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The action is bundled into a single dist/index.js with esbuild so no node_modules are needed at runtime; non-code Pi SDK assets are copied to dist/pi-sdk/ and resolved via the PI_PACKAGE_DIR environment variable. -- evidence: [README.md#L66-L66](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L66-L66)
  - [observation/documented] Because CI has no interactive user to approve trust, the action always marks the workspace as trusted (projectTrusted: true), so repository files like AGENTS.md, .pi settings, and project extensions are loaded and followed by the agent. -- evidence: [README.md#L51-L53](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L51-L53)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The action accepts inputs including provider, model, token, github_token, base_url, thinking_level, prompt, pr_number, extensions, loaded_tools, update_comment, share_session, and branch_name_template, per documented examples. -- evidence: [README.md#L377-L388](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L377-L388), [README.md#L128-L137](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L128-L137), [README.md#L284-L292](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L284-L292), [README.md#L758-L766](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L758-L766), [README.md#L467-L479](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L467-L479), [README.md#L234-L242](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L234-L242), [README.md#L590-L602](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L590-L602), [README.md#L143-L152](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L143-L152)
  - [observation/documented] The action exposes outputs such as success, response, cost, input_tokens, output_tokens, duration_seconds, share_url, gist_url, gist_id, session_html_path, and session_jsonl_path for downstream steps. -- evidence: [README.md#L748-L748](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L748-L748), [README.md#L690-L700](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L690-L700), [README.md#L717-L717](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L717-L717)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] By default the action loads all built-in GitHub tools; load_builtin_extensions can disable them, and loaded_tools (default 'all') restricts the session to a named subset, failing early on unrecognized tool names. -- evidence: [README.md#L606-L607](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L606-L607), [README.md#L588-L588](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L588-L588), [README.md#L571-L571](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L571-L571), [README.md#L604-L604](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L604-L604)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] A README dependency table lists bundled packages including @earendil-works/pi-coding-agent 0.85.1, @actions/core 3.0.1, @actions/github 9.1.1, Octokit packages, simple-git 3.36.0, and typebox 1.3.6; the table is auto-updated by a workflow. -- evidence: [README.md#L74-L86](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L74-L86), [README.md#L90-L90](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L90-L90)
  - [observation/documented] The AWS Bedrock provider and its @aws-sdk/client-bedrock-runtime dependency are bundled into dist/index.js and statically registered at startup, adding roughly 500 KB to the action bundle. -- evidence: [README.md#L566-L567](https://github.com/shaftoe/pi-coding-agent-action/blob/d90187d4bc85ea7c5f8e693575fc817d7447d7c8/README.md#L566-L567)
- limitations (2 claim(s)):
More evidence: [full detail](pi-coding-agent-action.detail.md)

Metadata and full claim list: [full detail](pi-coding-agent-action.detail.md)
Human notes ([notes](pi-coding-agent-action.notes.md), never overwritten by build)

[Back to map index](../../index.md)
