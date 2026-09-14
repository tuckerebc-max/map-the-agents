# dansiegel/codegenhelpers -- full detail

[Back to orientation](codegenhelpers.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dansiegel/codegenhelpers/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/dc1a9016b7bb4a04.json](../../../wiki/dossiers/dansiegel/codegenhelpers/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/dc1a9016b7bb4a04.json)

## specifications (1 claim(s))

- [observation/documented] CodeGenHelpers is a library intended to help developers write C# code generators, per its README. -- evidence: [ReadMe.md#L3-L3](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L3-L3) (`clm_b8add8445547cc34d6dff4da9de06bea0c0b806ef7ce075587b920177a90337d`)

## components (1 claim(s))

- [observation/documented] The library provides a fluent builder framework for generating code, working with native Roslyn types such as ITypeSymbol to manage namespace imports. -- evidence: [ReadMe.md#L77-L77](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L77-L77) (`clm_3f8ce228d0217475a58d193906a50bd40f3877d08e30819f8be6552781a483eb`)

## design-choices (3 claim(s))

- [observation/documented] Version 2.0 changes distribution from source linked into the project to a pre-compiled library; consumers can opt back into source via the CodeGenHelpersMode property set to 'source'. -- evidence: [ReadMe.md#L9-L9](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L9-L9) (`clm_05f88e9695ea1104cc6cf184caa8d42596279a7312a0f6c9c2c9fee414c853a8`)
- [observation/documented] Generated output includes a standard auto-generated header comment warning that changes may cause incorrect behavior and will be lost on regeneration. -- evidence: [ReadMe.md#L101-L109](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L101-L109) (`clm_685dcd0e6761adc2695ff736a099b1159dbf0133365d284e9f59c81f66137b64`)
- [observation/documented] The library positions itself against raw StringBuilder and IndentedStringBuilder approaches, which the README describes as producing many AppendLine calls without understanding of the code being generated. -- evidence: [ReadMe.md#L13-L13](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L13-L13), [ReadMe.md#L50-L51](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L50-L51), [ReadMe.md#L68-L75](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L68-L75) (`clm_92c757b88d93d287860a17ce7f6c4fcdbc9d89e2b5270716d1541204586e3ff9`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the maintainer states pull requests are welcome, noting the project began as an afternoon hack and improvements are being added while integrating it into their own source generators. -- evidence: [ReadMe.md#L150-L150](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L150-L150) (`clm_7e92189695cf943090a321bdeed1ee7a3b2a903b8d27356d0f38aecef453d17f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The API includes CodeBuilder.Create(typeSymbol) with chained methods like AddNamespaceImport, AddConstructor, AddParameter, WithBody, and AddProperty with UseGetOnlyAutoProp/UseAutoProps, and a Build method producing the generated source text. -- evidence: [ReadMe.md#L96-L97](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L96-L97), [ReadMe.md#L79-L94](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L79-L94) (`clm_6127af11ec116475f80159a1ecea5d2cc61433ca662340948090e4f33b40fc72`)
- [observation/documented] Builders include overloads for Roslyn types like ITypeSymbol and INamespaceSymbol; adding an ITypeSymbol parameter automatically imports its namespace even when it appears higher in the syntax tree. -- evidence: [ReadMe.md#L132-L132](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L132-L132) (`clm_3d541c5696915408787c67032073d95aca62159e9294680ca926729e00ccee72`)
- [observation/documented] A GeneratorExecutionContext AddSource extension adds generated code to the compilation and formats output based on ParseOptions; Build can also be passed ParseOptions to replicate that formatting. -- evidence: [ReadMe.md#L136-L136](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L136-L136), [ReadMe.md#L142-L144](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L142-L144) (`clm_e7a254b6832fddba23e3dfc1d5dbdb217634c0dc920b8e0e9a8b247878d2cd4a`)
- [observation/documented] The AddSource extension names each generated file with the fully qualified type name plus .g.cs (e.g. AwesomeApp.SomeClass.g.cs), and iterating a CodeBuilder yields one source text per included Class, Enum, or Record. -- evidence: [ReadMe.md#L146-L146](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L146-L146) (`clm_0a406d425e7a6fe62da442f9f073f5da1b237f44303bc3356ec23c0724ba0bfc`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The library is distributed as the AvantiPoint.CodeGenHelpers NuGet package. -- evidence: [ReadMe.md#L5-L7](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L5-L7) (`clm_8ea789c97da8389fec31068edcb5dfd1aaf73ad84c9aa554013031eab438fdae`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

