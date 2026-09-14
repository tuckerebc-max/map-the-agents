# claude-memory-compiler (`claude-memory-compiler`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: coleam00
- License: unknown
- Language: Python
- Interface: install=pip
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [coleam00/claude-memory-compiler](../../repos/coleam00/claude-memory-compiler.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): No RAG / no vector DB / no embeddings — uses a markdown index.md that the LLM reads directly (inspired by Karpathy's LLM Knowledge Base architecture). Captures Claude Code conversations via hooks (SessionStart, SessionEnd, PreCompact), extracts decisions/lessons using Claude Agent SDK, compiles daily logs into cross-referenced knowledge articles. Runs on existing Claude subscription at no extra API cost.

(captured site page body (agents/claude-memory-compiler.md), not a verified repo-code finding)
The project replaces vector-database memory with the observation that at personal scale (roughly 50-500 articles) an LLM reading a well-structured markdown index outperforms cosine similarity, and only becomes necessary past a few thousand articles. Conversation capture happens through Claude Code hooks that spawn a background extraction pass on the user's existing subscription, writing daily logs; after 18:00 the next flush compiles them into concept, connection, and Q&A articles with cross-references. Subsequent sessions get the index injected, giving the assistant durable project memory. Solo developers maintaining long-running projects use it; the repository consists of only two commits published in April 2026.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-memory-compiler.md)
