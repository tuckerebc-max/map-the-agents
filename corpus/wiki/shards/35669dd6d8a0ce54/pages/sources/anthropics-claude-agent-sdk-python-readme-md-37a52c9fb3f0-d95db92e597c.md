---
access: public
aliases: []
claim_ids:
- clm_118091d0972494b5c04814d489939d17f6989c51fad8f37e8f954d8a295e121a
- clm_1c8491ad259e7576f1bf9254da4d52c365c0fca6a0db3280f2afd4da0d790fc8
- clm_3b7d3cacea18debf4844ef00b9854e8ca935727d38ec65de8b177acbe53996b6
- clm_958187aab2fe766b5073b185e6ebc858030cc2c6561a3e3a835019bd968ec40f
- clm_a6518366c72ae5b8cab5e8d77e0455ffc14b1ebc71e5d494217f72123045566e
- clm_abd472a33ebb7736903065ed582edfc3647f4885d6236cfc9f315e0fd8fd196d
- clm_d782b5c6f20e3e4455dd08bad704723fd93a34c5ed75758911a8f4fc4dea5f01
- clm_d79ad534167853fc40bbece7c4a8b5d987c082116ff7fda1b47269c280ce9bb3
- clm_e6eececddeb3ae7da43a035c66369f2a70de17356585c16bf1a93c9903bf5222
- clm_f0e282972d9c2b11a6434118b7bb67ccb065473210cc15d0fbb046af5df633db
maturity: draft
page_id: pg_6ddf16125d705bd0a445d95db92e597c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8e8e00b074c655f29697d5039bfd10c9
title: anthropics/claude-agent-sdk-python/README.md @ 37a52c9fb3f0
updated_at: '2026-09-14T01:33:27Z'
---

# anthropics/claude-agent-sdk-python/README.md @ 37a52c9fb3f0

<!-- rcw:begin owner=source:src_8e8e00b074c655f29697d5039bfd10c9 block=evidence -->
- Hooks are Python functions invoked by the Claude Code application at points of the agent loop, e.g. a PreToolUse matcher that can deny a Bash command by pattern. [@claim:clm_118091d0972494b5c04814d489939d17f6989c51fad8f37e8f954d8a295e121a]
- The SDK exposes an async query() function that returns an AsyncIterator of response messages, with a ClaudeAgentOptions configuration object. [@claim:clm_1c8491ad259e7576f1bf9254da4d52c365c0fca6a0db3280f2afd4da0d790fc8]
- ClaudeSDKClient supports bidirectional interactive conversations and, unlike query(), additionally enables custom tools and hooks defined as Python functions. [@claim:clm_3b7d3cacea18debf4844ef00b9854e8ca935727d38ec65de8b177acbe53996b6]
- Repository development practice: releases are published to PyPI via a manually triggered GitHub Actions workflow that builds platform wheels bundling a chosen CLI version and opens a version-update PR. [@claim:clm_958187aab2fe766b5073b185e6ebc858030cc2c6561a3e3a835019bd968ec40f]
- ClaudeAgentOptions supports both in-process SDK MCP servers and external stdio subprocess MCP servers in the same mcp_servers mapping. [@claim:clm_a6518366c72ae5b8cab5e8d77e0455ffc14b1ebc71e5d494217f72123045566e]
- Custom tools are implemented as in-process SDK MCP servers running inside the host Python application, avoiding subprocess management and IPC overhead of external MCP servers. [@claim:clm_abd472a33ebb7736903065ed582edfc3647f4885d6236cfc9f315e0fd8fd196d]
- Repository development practice: contributors run ./scripts/initial-setup.sh to install a pre-push hook that runs lint checks matching CI, skippable with git push --no-verify. [@claim:clm_d782b5c6f20e3e4455dd08bad704723fd93a34c5ed75758911a8f4fc4dea5f01]
- The SDK defines typed message and content-block types (AssistantMessage, UserMessage, SystemMessage, ResultMessage, TextBlock, ToolUseBlock, ToolResultBlock) and an error hierarchy including CLINotFoundError, ProcessError, and ResultError. [@claim:clm_d79ad534167853fc40bbece7c4a8b5d987c082116ff7fda1b47269c280ce9bb3]
- The package requires Python 3.10+ and bundles the Claude Code CLI by default; a system CLI or custom cli_path can be specified instead. [@claim:clm_e6eececddeb3ae7da43a035c66369f2a70de17356585c16bf1a93c9903bf5222]
- By default Claude has the full Claude Code toolset; allowed_tools is an auto-approval allowlist that does not remove tools, while disallowed_tools blocks tools, and permission_mode and can_use_tool handle unlisted tools. [@claim:clm_f0e282972d9c2b11a6434118b7bb67ccb065473210cc15d0fbb046af5df633db]
<!-- rcw:end owner=source:src_8e8e00b074c655f29697d5039bfd10c9 block=evidence -->

## Researcher notes

