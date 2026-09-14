# anthropics/claude-agent-sdk-python -- full detail

[Back to orientation](claude-agent-sdk-python.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/anthropics/claude-agent-sdk-python/37a52c9fb3f0271de017911914b0d42efea6267e/6691541e24958815.json](../../../wiki/dossiers/anthropics/claude-agent-sdk-python/37a52c9fb3f0271de017911914b0d42efea6267e/6691541e24958815.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Custom tools are implemented as in-process SDK MCP servers running inside the host Python application, avoiding subprocess management and IPC overhead of external MCP servers. -- evidence: [README.md#L96-L96](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L96-L96), [README.md#L138-L142](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L138-L142) (`clm_abd472a33ebb7736903065ed582edfc3647f4885d6236cfc9f315e0fd8fd196d`)
- [observation/documented] Hooks are Python functions invoked by the Claude Code application at points of the agent loop, e.g. a PreToolUse matcher that can deny a Bash command by pattern. -- evidence: [README.md#L189-L189](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L189-L189), [README.md#L216-L223](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L216-L223), [README.md#L198-L214](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L198-L214) (`clm_118091d0972494b5c04814d489939d17f6989c51fad8f37e8f954d8a295e121a`)

## design-choices (2 claim(s))

- [observation/documented] ClaudeAgentOptions supports both in-process SDK MCP servers and external stdio subprocess MCP servers in the same mcp_servers mapping. -- evidence: [README.md#L173-L173](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L173-L173), [README.md#L175-L185](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L175-L185) (`clm_a6518366c72ae5b8cab5e8d77e0455ffc14b1ebc71e5d494217f72123045566e`)
- [observation/documented] The changelog documents security hardening such as validating skill names to prevent --allowedTools injection and passing --resume/--session-id as single =-joined argv tokens. -- evidence: [CHANGELOG.md#L238-L238](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L238-L238), [CHANGELOG.md#L171-L171](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L171-L171) (`clm_8266ae1f684292ad3cce1db4ae92229c94bc77ea7e69ad874828fdb79b1758de`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run ./scripts/initial-setup.sh to install a pre-push hook that runs lint checks matching CI, skippable with git push --no-verify. -- evidence: [README.md#L304-L304](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L304-L304), [README.md#L298-L298](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L298-L298), [README.md#L300-L302](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L300-L302) (`clm_d782b5c6f20e3e4455dd08bad704723fd93a34c5ed75758911a8f4fc4dea5f01`)
- [observation/documented] Repository development practice: releases are published to PyPI via a manually triggered GitHub Actions workflow that builds platform wheels bundling a chosen CLI version and opens a version-update PR. -- evidence: [README.md#L341-L341](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L341-L341), [README.md#L347-L357](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L347-L357), [README.md#L343-L345](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L343-L345) (`clm_958187aab2fe766b5073b185e6ebc858030cc2c6561a3e3a835019bd968ec40f`)

## skills-patterns (1 claim(s))

- [observation/documented] Skill names in ClaudeAgentOptions.skills are validated at connect time; wildcard entries like "plugin:*" or "*" must be replaced with skills="all" or a Skill(...) rule in allowed_tools. -- evidence: [CHANGELOG.md#L167-L167](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L167-L167) (`clm_788eb7b986d8c40f01fa504ef2b120ed6c3b5bb547bfadaf59d6498ebb5b82c3`)

## interfaces (3 claim(s))

- [observation/documented] The SDK exposes an async query() function that returns an AsyncIterator of response messages, with a ClaudeAgentOptions configuration object. -- evidence: [README.md#L48-L51](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L48-L51), [README.md#L35-L35](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L35-L35) (`clm_1c8491ad259e7576f1bf9254da4d52c365c0fca6a0db3280f2afd4da0d790fc8`)
- [observation/documented] ClaudeSDKClient supports bidirectional interactive conversations and, unlike query(), additionally enables custom tools and hooks defined as Python functions. -- evidence: [README.md#L87-L88](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L87-L88), [README.md#L90-L90](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L90-L90) (`clm_3b7d3cacea18debf4844ef00b9854e8ca935727d38ec65de8b177acbe53996b6`)
- [observation/documented] The SDK defines typed message and content-block types (AssistantMessage, UserMessage, SystemMessage, ResultMessage, TextBlock, ToolUseBlock, ToolResultBlock) and an error hierarchy including CLINotFoundError, ProcessError, and ResultError. -- evidence: [README.md#L249-L257](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L249-L257), [README.md#L243-L245](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L243-L245) (`clm_d79ad534167853fc40bbece7c4a8b5d987c082116ff7fda1b47269c280ce9bb3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] By default Claude has the full Claude Code toolset; allowed_tools is an auto-approval allowlist that does not remove tools, while disallowed_tools blocks tools, and permission_mode and can_use_tool handle unlisted tools. -- evidence: [README.md#L61-L65](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L61-L65), [README.md#L59-L59](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L59-L59) (`clm_f0e282972d9c2b11a6434118b7bb67ccb065473210cc15d0fbb046af5df633db`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The package requires Python 3.10+ and bundles the Claude Code CLI by default; a system CLI or custom cli_path can be specified instead. -- evidence: [README.md#L13-L13](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L13-L13), [README.md#L15-L15](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L15-L15), [README.md#L17-L18](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/README.md#L17-L18) (`clm_e6eececddeb3ae7da43a035c66369f2a70de17356585c16bf1a93c9903bf5222`)
- [observation/documented] The mcp dependency was widened to mcp>=1.23.0,<3.0.0, supporting mcp 2.x for in-process servers served over mcp's in-memory transport. -- evidence: [CHANGELOG.md#L79-L82](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L79-L82) (`clm_e56cc68f5d84e3920961f0d755857c8febc6dfa94c61099c7a4d39a45c711e23`)

## limitations (1 claim(s))

- [observation/documented] On Windows, the SDK refuses to spawn .bat/.cmd CLI scripts and rejects cmd.exe metacharacters in resume/session_id values to prevent command injection. -- evidence: [CHANGELOG.md#L214-L216](https://github.com/anthropics/claude-agent-sdk-python/blob/37a52c9fb3f0271de017911914b0d42efea6267e/CHANGELOG.md#L214-L216) (`clm_8188a3ef0ab129c393bbac20970dd3f193c656324f7d7d574215ea880cc7f638`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

