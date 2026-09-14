# CodeGenHelpers (`codegenhelpers`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: dansiegel
- License: MIT
- Language: C#
- Interface: install=NuGet package AvantiPoint.CodeGenHelpers
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [dansiegel/codegenhelpers](../../repos/dansiegel/codegenhelpers.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fluent builder library for writing C# Source Generators (Roslyn) instead of raw IndentedStringBuilder string concatenation; typed builders work with native Roslyn types (e.g., ITypeSymbol); automatically handles namespace imports, class/enum/record construction, and source file naming (.g.cs); version 2.0 ships as pre-compiled library by default (with opt-in source-link mode). Not an AI agent harness.

(captured site page body (agents/codegenhelpers.md), not a verified repo-code finding)
CodeGenHelpers is a developer library for people writing C# Roslyn source generators, included in this census only because its name matches code-generation tooling. Writing source generators typically means concatenating output text through IndentedStringBuilder, which produces brittle, hard-to-maintain generator code; CodeGenHelpers replaces that with a fluent builder API that works directly with Roslyn symbols such as ITypeSymbol and handles namespace imports, class/enum/record construction, and .g.cs source-file naming automatically. Version 2.0 ships as a compiled NuGet library (AvantiPoint.CodeGenHelpers) by default, with an opt-in mode that injects the builder source directly into the generator project for scenarios that require source-only distribution. It is a Dan Siegel (AvantiPoint) project with no AI component.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codegenhelpers.md)
