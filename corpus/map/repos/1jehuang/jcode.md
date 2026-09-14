# 1jehuang/jcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 37159430c3d0 @ b7be00436905e014

## Summary (orientation draft, not independently verified)

Selected evidence records: Each conversation turn is embedded as a semantic vector and queried against a memory graph via cosine similarity; hits are injected into the conversation, optionally after verification by a memory sideagent. Memories are extracted by a memory sideagent at triggers such as semantic drift, a K-turn interval, or session end, and added to the memory graph.

## Source coverage

Source coverage (partial): 6 of 90 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] User input is interleaved with the working agent as soon as it can be sent without breaking the KV cache; shift-enter instead queues the message until the agent finishes its turn. -- evidence: [README.md#L672-L672](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L672-L672)
  - [observation/documented] An 'agent grep' tool augments grep output with file structure information (function lists, offsets) and adaptively truncates results based on what the agent has already seen to save context. -- evidence: [README.md#L670-L670](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L670-L670)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are not all loaded at startup; embedding hits on the conversation inject relevant skills automatically, and skills can also be activated manually via a skill tool or slash commands. -- evidence: [README.md#L680-L680](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L680-L680)
- interfaces (5 claim(s)):
  - [observation/documented] jcode offers built-in login flows via `jcode login --provider <id>` for providers including claude, openai, gemini, copilot, azure, fireworks, novita, minimax, lmstudio, ollama, and custom OpenAI-compatible endpoints. -- evidence: [README.md#L352-L364](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L352-L364)
  - [observation/documented] MCP servers are configured in ~/.jcode/mcp.json (global) and .jcode/mcp.json (project-local); Claude Code config files (~/.claude.json, .mcp.json, .claude/mcp.json) are read live, and a one-time import from ~/.codex/config.toml is performed. -- evidence: [README.md#L573-L575](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L573-L575), [README.md#L568-L569](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L568-L569), [README.md#L577-L584](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L577-L584)
- memory-state (4 claim(s)):
  - [observation/documented] Each conversation turn is embedded as a semantic vector and queried against a memory graph via cosine similarity; hits are injected into the conversation, optionally after verification by a memory sideagent. -- evidence: [README.md#L287-L289](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L287-L289)
  - [observation/documented] Memories are extracted by a memory sideagent at triggers such as semantic drift, a K-turn interval, or session end, and added to the memory graph. -- evidence: [README.md#L287-L289](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L287-L289)
- orchestration (2 claim(s)):
  - [observation/documented] Multiple agents spawned in the same repo are managed by a server: when one agent edits a file another has read, the server notifies the reader, which can ignore it or check the diff; agents can DM, broadcast, or message repo-scoped peers. -- evidence: [README.md#L330-L330](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L330-L330)
More evidence: [full detail](jcode.detail.md)

Metadata and full claim list: [full detail](jcode.detail.md)
Human notes ([notes](jcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
