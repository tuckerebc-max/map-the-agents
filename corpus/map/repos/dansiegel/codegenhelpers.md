# dansiegel/codegenhelpers

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 69671cd8bfe8 @ dc1a9016b7bb4a04

## Summary (orientation draft, not independently verified)

The snapshot is a README-only view of CodeGenHelpers, a C# source-generator helper library distributed as the AvantiPoint.CodeGenHelpers NuGet package, offering a fluent builder API over Roslyn types. Evidence covers the library's purpose, distribution, API surface, and source-generator integration; no code, tests, or CI are shown.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] CodeGenHelpers is a library intended to help developers write C# code generators, per its README. -- evidence: [ReadMe.md#L3-L3](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The library provides a fluent builder framework for generating code, working with native Roslyn types such as ITypeSymbol to manage namespace imports. -- evidence: [ReadMe.md#L77-L77](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L77-L77)
- design-choices (3 claim(s)):
  - [observation/documented] Version 2.0 changes distribution from source linked into the project to a pre-compiled library; consumers can opt back into source via the CodeGenHelpersMode property set to 'source'. -- evidence: [ReadMe.md#L9-L9](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L9-L9)
  - [observation/documented] Generated output includes a standard auto-generated header comment warning that changes may cause incorrect behavior and will be lost on regeneration. -- evidence: [ReadMe.md#L101-L109](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L101-L109)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the maintainer states pull requests are welcome, noting the project began as an afternoon hack and improvements are being added while integrating it into their own source generators. -- evidence: [ReadMe.md#L150-L150](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L150-L150)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The API includes CodeBuilder.Create(typeSymbol) with chained methods like AddNamespaceImport, AddConstructor, AddParameter, WithBody, and AddProperty with UseGetOnlyAutoProp/UseAutoProps, and a Build method producing the generated source text. -- evidence: [ReadMe.md#L96-L97](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L96-L97), [ReadMe.md#L79-L94](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L79-L94)
  - [observation/documented] Builders include overloads for Roslyn types like ITypeSymbol and INamespaceSymbol; adding an ITypeSymbol parameter automatically imports its namespace even when it appears higher in the syntax tree. -- evidence: [ReadMe.md#L132-L132](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L132-L132)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The library is distributed as the AvantiPoint.CodeGenHelpers NuGet package. -- evidence: [ReadMe.md#L5-L7](https://github.com/dansiegel/CodeGenHelpers/blob/69671cd8bfe82c3bdb2952d0c08f969c33a0b400/ReadMe.md#L5-L7)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](codegenhelpers.detail.md) for every claim.)

Metadata and full claim list: [full detail](codegenhelpers.detail.md)
Human notes ([notes](codegenhelpers.notes.md), never overwritten by build)

[Back to map index](../../index.md)
