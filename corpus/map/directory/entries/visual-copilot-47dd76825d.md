# Visual Copilot (`visual-copilot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Figma
- License: Proprietary
- Language: unknown
- Interface: platforms=IDE; install=Figma Community plugin
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Figma's Visual Copilot (Figma-to-Code plugin) converts Figma designs into code. Figma page returned HTTP 403; details could not be directly verified from the listing page.

(captured site page body (agents/visual-copilot.md), not a verified repo-code finding)
Visual Copilot addresses the gap between finalized Figma designs and production front-end code, where manual conversion is slow and generic exporters produce unmaintainable markup. Mechanically, a Figma plugin converts a selected layer into an intermediate code hierarchy using Builder.io's open-source Mitosis compiler, and an LLM then refines that output to match the requested framework and styling system, including a team's own mapped components. Output targets React, Vue, Svelte, Angular, Qwik, Solid, React Native, and HTML, with styling in plain CSS, Tailwind, or Emotion. The Figma plugin itself is free on all Builder.io plans, while code generation runs against agent credits that are metered across Builder's Free, Pro, Team, and Enterprise tiers. It is used by front-end teams that want design exports to follow their existing component and styling conventions.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/visual-copilot.md)
