---
access: public
aliases: []
claim_ids:
- clm_05f88e9695ea1104cc6cf184caa8d42596279a7312a0f6c9c2c9fee414c853a8
- clm_0a406d425e7a6fe62da442f9f073f5da1b237f44303bc3356ec23c0724ba0bfc
- clm_3d541c5696915408787c67032073d95aca62159e9294680ca926729e00ccee72
- clm_3f8ce228d0217475a58d193906a50bd40f3877d08e30819f8be6552781a483eb
- clm_6127af11ec116475f80159a1ecea5d2cc61433ca662340948090e4f33b40fc72
- clm_685dcd0e6761adc2695ff736a099b1159dbf0133365d284e9f59c81f66137b64
- clm_7e92189695cf943090a321bdeed1ee7a3b2a903b8d27356d0f38aecef453d17f
- clm_8ea789c97da8389fec31068edcb5dfd1aaf73ad84c9aa554013031eab438fdae
- clm_92c757b88d93d287860a17ce7f6c4fcdbc9d89e2b5270716d1541204586e3ff9
- clm_b8add8445547cc34d6dff4da9de06bea0c0b806ef7ce075587b920177a90337d
- clm_e7a254b6832fddba23e3dfc1d5dbdb217634c0dc920b8e0e9a8b247878d2cd4a
maturity: draft
page_id: pg_8b1bb23832685cbfb854043cb1ba8adb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d6c2cfc823355e31966633c22caae621
title: dansiegel/CodeGenHelpers/ReadMe.md @ 69671cd8bfe8
updated_at: '2026-09-14T03:43:56Z'
---

# dansiegel/CodeGenHelpers/ReadMe.md @ 69671cd8bfe8

<!-- rcw:begin owner=source:src_d6c2cfc823355e31966633c22caae621 block=evidence -->
- Version 2.0 changes distribution from source linked into the project to a pre-compiled library; consumers can opt back into source via the CodeGenHelpersMode property set to 'source'. [@claim:clm_05f88e9695ea1104cc6cf184caa8d42596279a7312a0f6c9c2c9fee414c853a8]
- The AddSource extension names each generated file with the fully qualified type name plus .g.cs (e.g. AwesomeApp.SomeClass.g.cs), and iterating a CodeBuilder yields one source text per included Class, Enum, or Record. [@claim:clm_0a406d425e7a6fe62da442f9f073f5da1b237f44303bc3356ec23c0724ba0bfc]
- Builders include overloads for Roslyn types like ITypeSymbol and INamespaceSymbol; adding an ITypeSymbol parameter automatically imports its namespace even when it appears higher in the syntax tree. [@claim:clm_3d541c5696915408787c67032073d95aca62159e9294680ca926729e00ccee72]
- The library provides a fluent builder framework for generating code, working with native Roslyn types such as ITypeSymbol to manage namespace imports. [@claim:clm_3f8ce228d0217475a58d193906a50bd40f3877d08e30819f8be6552781a483eb]
- The API includes CodeBuilder.Create(typeSymbol) with chained methods like AddNamespaceImport, AddConstructor, AddParameter, WithBody, and AddProperty with UseGetOnlyAutoProp/UseAutoProps, and a Build method producing the generated source text. [@claim:clm_6127af11ec116475f80159a1ecea5d2cc61433ca662340948090e4f33b40fc72]
- Generated output includes a standard auto-generated header comment warning that changes may cause incorrect behavior and will be lost on regeneration. [@claim:clm_685dcd0e6761adc2695ff736a099b1159dbf0133365d284e9f59c81f66137b64]
- Repository development practice: the maintainer states pull requests are welcome, noting the project began as an afternoon hack and improvements are being added while integrating it into their own source generators. [@claim:clm_7e92189695cf943090a321bdeed1ee7a3b2a903b8d27356d0f38aecef453d17f]
- The library is distributed as the AvantiPoint.CodeGenHelpers NuGet package. [@claim:clm_8ea789c97da8389fec31068edcb5dfd1aaf73ad84c9aa554013031eab438fdae]
- The library positions itself against raw StringBuilder and IndentedStringBuilder approaches, which the README describes as producing many AppendLine calls without understanding of the code being generated. [@claim:clm_92c757b88d93d287860a17ce7f6c4fcdbc9d89e2b5270716d1541204586e3ff9]
- CodeGenHelpers is a library intended to help developers write C# code generators, per its README. [@claim:clm_b8add8445547cc34d6dff4da9de06bea0c0b806ef7ce075587b920177a90337d]
- A GeneratorExecutionContext AddSource extension adds generated code to the compilation and formats output based on ParseOptions; Build can also be passed ParseOptions to replicate that formatting. [@claim:clm_e7a254b6832fddba23e3dfc1d5dbdb217634c0dc920b8e0e9a8b247878d2cd4a]
<!-- rcw:end owner=source:src_d6c2cfc823355e31966633c22caae621 block=evidence -->

## Researcher notes

