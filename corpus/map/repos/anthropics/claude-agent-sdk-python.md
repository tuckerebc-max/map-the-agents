# anthropics/claude-agent-sdk-python

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 37a52c9fb3f0 @ 6691541e24958815

## Summary (orientation draft, not independently verified)

The evidence describes the Claude Agent SDK for Python: an async SDK wrapping the Claude Code CLI with query()/ClaudeSDKClient APIs, in-process MCP custom tools, hooks, permission options, and a release workflow bundling the CLI. Most support is README documentation plus a CHANGELOG; no source code slices are present. Evidence coverage: 167 of 339 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Custom tools are implemented as in-process SDK MCP servers running inside the host Python application, avoiding subprocess management and IPC overhead of external MCP servers. -- evidence: [README.md#L96-L96](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L96-L96), [README.md#L138-L142](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L138-L142)
  - [observation/documented] Hooks are Python functions invoked by the Claude Code application at points of the agent loop, e.g. a PreToolUse matcher that can deny a Bash command by pattern. -- evidence: [README.md#L189-L189](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L189-L189), [README.md#L216-L223](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L216-L223), [README.md#L198-L214](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L198-L214)
- design-choices (2 claim(s)):
  - [observation/documented] ClaudeAgentOptions supports both in-process SDK MCP servers and external stdio subprocess MCP servers in the same mcp_servers mapping. -- evidence: [README.md#L173-L173](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L173-L173), [README.md#L175-L185](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L175-L185)
  - [observation/documented] The changelog documents security hardening such as validating skill names to prevent --allowedTools injection and passing --resume/--session-id as single =-joined argv tokens. -- evidence: [CHANGELOG.md#L238-L238](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L238-L238), [CHANGELOG.md#L171-L171](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L171-L171)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run ./scripts/initial-setup.sh to install a pre-push hook that runs lint checks matching CI, skippable with git push --no-verify. -- evidence: [README.md#L304-L304](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L304-L304), [README.md#L298-L298](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L298-L298), [README.md#L300-L302](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L300-L302)
  - [observation/documented] Repository development practice: releases are published to PyPI via a manually triggered GitHub Actions workflow that builds platform wheels bundling a chosen CLI version and opens a version-update PR. -- evidence: [README.md#L341-L341](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L341-L341), [README.md#L347-L357](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L347-L357), [README.md#L343-L345](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L343-L345)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skill names in ClaudeAgentOptions.skills are validated at connect time; wildcard entries like "plugin:*" or "*" must be replaced with skills="all" or a Skill(...) rule in allowed_tools. -- evidence: [CHANGELOG.md#L167-L167](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L167-L167)
- interfaces (3 claim(s)):
  - [observation/documented] The SDK exposes an async query() function that returns an AsyncIterator of response messages, with a ClaudeAgentOptions configuration object. -- evidence: [README.md#L48-L51](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L48-L51), [README.md#L35-L35](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L35-L35)
  - [observation/documented] ClaudeSDKClient supports bidirectional interactive conversations and, unlike query(), additionally enables custom tools and hooks defined as Python functions. -- evidence: [README.md#L87-L88](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L87-L88), [README.md#L90-L90](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L90-L90)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](claude-agent-sdk-python.detail.md)

Metadata and full claim list: [full detail](claude-agent-sdk-python.detail.md)
Human notes ([notes](claude-agent-sdk-python.notes.md), never overwritten by build)

[Back to map index](../../index.md)
