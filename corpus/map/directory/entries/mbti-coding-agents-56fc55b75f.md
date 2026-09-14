# mbti-coding-agents (`mbti-coding-agents`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: weiyangzen
- License: unknown
- Language: JavaScript, Node.js
- Interface: install=git clone https://github.com/weiyangzen/mbti-coding-agents.git; cd mbti-coding-agents; npm run install (optionally select Claude TTS during install)
- Model providers: Anthropic (Claude), Google (Gemini); MiniMax and Gemini for optional TTS
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [weiyangzen/mbti-coding-agents](../../repos/weiyangzen/mbti-coding-agents.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Collection of 16 specialized AI coding agent personas mapped to Myers-Briggs (MBTI) personality types (Analysts, Diplomats, Sentinels, Explorers) to provide distinct cognitive styles; /squad for dynamic team selection, /battle arena where agents compete on tasks, /my-coding-mbti for personal coding MBTI detection; optional Text-to-Speech summaries.

(captured site page body (agents/mbti-coding-agents.md), not a verified repo-code finding)
The project's thesis is that a persona encoded in the system prompt changes coding-agent behavior as much as the underlying model, so it packages sixteen agents spanning analysts, diplomats, sentinels, and explorers, each with distinct approaches to planning, risk, and communication. Teams can be composed dynamically with /squad for a given task, or run in a /battle arena where personas compete on the same task and a report compares their results; /my-coding-mbti turns the mapping back on the user. Agents run inside Claude Code and Gemini CLI, with an optional text-to-speech layer (MiniMax and Gemini) for spoken summaries, and documentation is bilingual with an eight-language README. It is a small solo-maintained persona collection (37 stars, no license file).
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mbti-coding-agents.md)
