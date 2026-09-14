# Fullstack-Nextjs-App-Generator (`fullstack-nextjs-app-generator`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: spark-engine-opensource-projects
- License: MIT
- Language: JavaScript
- Interface: install=git clone, npm install, deploy to Vercel with Vercel CLI, set SPARK_API_KEY and NGROK_DEPLOYER_URL env vars
- Model providers: OpenAI, Groq (via Spark Engine API gateway)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: yes (yes)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [spark-engine-opensource-projects/fullstack-nextjs-app-generator](../../repos/spark-engine-opensource-projects/fullstack-nextjs-app-generator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fullstack Next.js app builder using Spark Engine AI's multi-agent system for interactive generation of pages, APIs, and database schemas, with automated deployment to Vercel + Supabase including database schema generation and serverless API creation through a guided multi-step UI.

(captured site page body (agents/fullstack-nextjs-app-generator.md), not a verified repo-code finding)
The project demonstrates Spark Engine AI's multi-agent generation applied to a concrete stack: Next.js pages, API routes, and Supabase schemas produced through a guided multi-step interface rather than a one-shot prompt. A backend deployer service, reached through an ngrok tunnel, executes the Vercel deployment and runs the generated SQL against Supabase, so the output is a deployed app with its schema rather than a folder of code. Generation goes through a Spark API key with OpenAI and Groq listed as underlying providers. Development stopped at 33 commits in late 2024, leaving it as a working demonstration of the Spark Engine workflow rather than a maintained product.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fullstack-nextjs-app-generator.md)
