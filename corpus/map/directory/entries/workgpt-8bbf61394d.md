# WorkGPT (`workgpt`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: team-openpm
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=npm
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: partial (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [team-openpm/workgpt](../../repos/team-openpm/workgpt.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Agent framework (AutoGPT/LangChain-style) that takes a directive and an array of APIs, then converses with AI until the directive is complete. Universal API support via OpenAPI files and OpenPM packages. Smart authentication (pass an authKey, library figures out authorization). Includes Puppeteer-based web crawling and Zod-schema-based structured data extraction. Maintained status unclear from README.

(captured site page body (agents/workgpt.md), not a verified repo-code finding)
WorkGPT is an AutoGPT/LangChain-era agent framework (2023, TypeScript/Node) that takes a directive and a set of APIs and converses with the model until the directive is complete. Its differentiator is universal API support: any API describable by an OpenAPI file can be invoked, packaged through OpenPM (a package manager for OpenAPI files), with smart authentication where passing an authKey lets the library figure out authorization. Execution runs through a WorkGptRunner loop with invokable API classes carrying Zod schemas, including a Puppeteer-based text browser. It is MIT-licensed, npm-published, and effectively dormant: 34 commits, no releases, and no ongoing development. It was aimed at developers prototyping agent flows against REST APIs in the AutoGPT era.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/workgpt.md)
