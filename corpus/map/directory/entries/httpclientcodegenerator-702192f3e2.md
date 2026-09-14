# HttpClientCodeGenerator (`httpclientcodegenerator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Jalalx
- License: MIT
- Language: C# / .NET
- Interface: platforms=CLI; install=dotnet add package HttpClientGenerator (NuGet)
- Model providers: none
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [jalalx/httpclientcodegenerator](../../repos/jalalx/httpclientcodegenerator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Uses Roslyn source generators to produce HttpClient code on the fly at compile time without writing files to disk. No runtime dependency on third-party libraries. Supports flexible HttpClient injection via fields, properties, or resolver methods. NOTE: This is a .NET code generator, NOT an AI coding agent harness.

(captured site page body (agents/httpclientcodegenerator.md), not a verified repo-code finding)
HttpClientCodeGenerator is a C# Roslyn source generator that removes hand-written HttpClient plumbing from service clients. Developers declare partial classes with attributed methods such as \[HttpGet("todos/{id}")\], and the generator emits the full implementation — URL construction, query strings, headers, serialization — at compile time in memory, leaving no generated files in the repository or any runtime dependency on external libraries. Generated code composes with IHttpClientFactory for the usual injection patterns, and the approach keeps repositories free of checked-in generated code. The project dates from the early Roslyn source-generator era, with known IDE tooling friction, and has seen no commits since late 2024.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/httpclientcodegenerator.md)
