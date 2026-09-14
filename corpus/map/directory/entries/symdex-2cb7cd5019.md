# SymDex (`symdex`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: other
- Provider/maker: husnainpk
- License: MIT
- Language: Python
- Interface: install=pip install symdex (or uv tool install symdex / uvx symdex); optional extras: symdex\[local\], symdex\[voyage\], symdex\[voyage-multimodal\]
- Model providers: Local sentence-transformers, Voyage, OpenAI-compatible /embeddings, Gemini Embedding (embedding backends)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: n/a (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [husnainpk/symdex](../../repos/husnainpk/symdex.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
SymDex exists because agents burn context reading whole files when they need one definition or call site. It indexes a checked-out repository into a local SQLite database: exact symbols with byte offs
Sources: [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json)
