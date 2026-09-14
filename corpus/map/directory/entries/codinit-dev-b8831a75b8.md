# codinit-dev (`codinit-dev`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: codinit-dev
- License: MIT
- Language: TypeScript
- Interface: platforms=Desktop, Web; install=Download prebuilt desktop release (macOS/Windows/Linux); or clone repo + npm install + pnpm run dev; or Docker (npm run dockerbuild + docker compose --profile development up)
- Model providers: OpenAI, Anthropic, Google, Groq, xAI, DeepSeek, Cohere, Mistral, Together, Perplexity, HuggingFace, OpenRouter, Ollama, LM Studio, OpenAI-compatible local endpoints (19+ providers)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [codinit-dev/codinit-dev](../../repos/codinit-dev/codinit-dev.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source, local-first AI full-stack app builder with hybrid web + desktop (Electron) support. Vendor-neutral architecture with dynamic switching between 19+ cloud and local AI providers. Production-ready Dockerization with presets for Vercel/Netlify/GitHub Pages. Integrated dev suite with semantic search, diff visualization, and file-locking. Native Supabase integration.

(captured site page body (agents/codinit-dev.md), not a verified repo-code finding)
Hosted app generators keep both the project and the model access inside a vendor's cloud, which conflicts with local development workflows and data-control requirements. CodinIT.dev is the open-source counterexample: a Bolt-style builder that runs as an Electron desktop app, a web app, or a Docker container, generating Node.js web and mobile applications with the edit loop happening on local files. Model access is vendor-neutral - nineteen-plus providers including OpenAI, Anthropic, Google, Groq, and OpenRouter, plus local runtimes via Ollama and LM Studio - switchable per task. Around the generation loop it adds project-management scaffolding: semantic code search, diff visualization, file locking for concurrent edits, voice commands, and deploy presets that push finished projects to Vercel, Netlify, or GitHub Pages. Supabase integration covers backend services. Developers and small teams wanting an open, local-first alternative to hosted app builders are its users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codinit-dev.md)
