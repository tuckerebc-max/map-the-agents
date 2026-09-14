# jalalx/httpclientcodegenerator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 96f70bf67dbf @ ca06fc6ab6a97d6b

## Summary (orientation draft, not independently verified)

HttpClientGenerator is a Roslyn-based C# source generator that emits HttpClient boilerplate for partial service classes at build time, without writing generated code to disk. Evidence is README-only documentation of usage, generated output, HttpClient injection options, and known IDE issues.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The tool uses the Roslyn C# source generator feature to write boilerplate HttpClient code on behalf of the developer. -- evidence: [README.md#L6-L6](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L6-L6)
- components (1 claim(s)):
  - [observation/documented] A shared HttpClientHelper component performs the actual HTTP send, and its DefaultJsonSerializerOptions singleton can be changed; by default PropertyNameCaseInsensitive is true. -- evidence: [README.md#L140-L140](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L140-L140), [README.md#L121-L122](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L121-L122)
- design-choices (5 claim(s)):
  - [observation/documented] The design philosophy is that no boilerplate or auto-generated code should be written, tracked in the repository, or regenerated manually when HTTP contracts change. -- evidence: [README.md#L9-L9](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L9-L9), [README.md#L11-L15](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L11-L15)
  - [observation/documented] Generated code is produced in-memory at build time and never written to disk, so it needs no source-control tracking. -- evidence: [README.md#L127-L128](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L127-L128)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Users declare partial classes with partial methods decorated by attributes such as HttpGet containing route templates like "todos/{id}"; the generator implements those methods. -- evidence: [README.md#L51-L66](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L51-L66), [README.md#L23-L38](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L23-L38)
  - [observation/documented] The generator emits a constructor taking an HttpClient parameter, and the generated method builds route, query, and header dictionaries before delegating to HttpClientHelper.SendAsync. -- evidence: [README.md#L68-L69](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L68-L69), [README.md#L115-L116](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L115-L116), [README.md#L118-L119](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L118-L119), [README.md#L102-L105](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L102-L105), [README.md#L121-L122](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L121-L122), [README.md#L111-L113](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L111-L113)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The package targets .NET 5 console apps and is installed via the HttpClientGenerator NuGet package; generated code relies on HttpClientGenerator.Shared helpers and System.Text.Json serialization attributes. -- evidence: [README.md#L18-L20](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L18-L20), [README.md#L40-L43](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L40-L43), [README.md#L88-L93](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L88-L93), [README.md#L23-L38](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L23-L38), [README.md#L121-L122](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L121-L122)
- limitations (1 claim(s)):
  - [observation/documented] Known issues include needing a Visual Studio 2019 restart for IntelliSense, a referenced Roslyn issue during development, and incomplete OmniSharp support in VS Code, though the dotnet SDK works. -- evidence: [README.md#L189-L192](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L189-L192)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](httpclientcodegenerator.detail.md) for every claim.)

Metadata and full claim list: [full detail](httpclientcodegenerator.detail.md)
Human notes ([notes](httpclientcodegenerator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
