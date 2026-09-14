# demo2apk (`demo2apk`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: DeadWaveWave
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=docker
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [deadwavewave/demo2apk](../../repos/deadwavewave/demo2apk.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): One-click tool that converts AI-generated code (Vibe Coding) into installable Android APKs with no Android dev environment setup required; supports HTML, React, ZIP projects with smart detection and offline support

(captured site page body (agents/demo2apk.md), not a verified repo-code finding)
Vibe-coding tools produce HTML and React demos that die in the browser; demo2apk exists to turn them into things users can actually install on a phone. Uploads are classified into single-file, pasted-code, or ZIP project types, then routed through an appropriate build strategy — raw HTML wraps directly, React/Vite projects run an npm build — with automatic handling of CDN resources and JSX compilation so apps keep working offline in Android WebView. The service queues concurrent builds, generates shareable download links, and purges artifacts after two hours. It serves hobbyists and hackathon participants who want an APK from an LLM chat without installing Android Studio.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/demo2apk.md)
