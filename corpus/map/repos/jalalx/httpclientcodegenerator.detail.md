# jalalx/httpclientcodegenerator -- full detail

[Back to orientation](httpclientcodegenerator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jalalx/httpclientcodegenerator/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/ca06fc6ab6a97d6b.json](../../../wiki/dossiers/jalalx/httpclientcodegenerator/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/ca06fc6ab6a97d6b.json)

## specifications (1 claim(s))

- [observation/documented] The tool uses the Roslyn C# source generator feature to write boilerplate HttpClient code on behalf of the developer. -- evidence: [README.md#L6-L6](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L6-L6) (`clm_4a4491cd845c62b1d2f98860ea5f7b28ae3eda59e758a161ee5c17258813e5ab`)

## components (1 claim(s))

- [observation/documented] A shared HttpClientHelper component performs the actual HTTP send, and its DefaultJsonSerializerOptions singleton can be changed; by default PropertyNameCaseInsensitive is true. -- evidence: [README.md#L140-L140](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L140-L140), [README.md#L121-L122](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L121-L122) (`clm_1f2462dd33c2d7b3568bf098048a28a547535e0edbf742c37435caba85605166`)

## design-choices (5 claim(s))

- [observation/documented] The design philosophy is that no boilerplate or auto-generated code should be written, tracked in the repository, or regenerated manually when HTTP contracts change. -- evidence: [README.md#L9-L9](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L9-L9), [README.md#L11-L15](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L11-L15) (`clm_99c1f787e911def18f47be0cab3b3f742ace2fa8b6102071d58649eb559d2c0d`)
- [observation/documented] Generated code is produced in-memory at build time and never written to disk, so it needs no source-control tracking. -- evidence: [README.md#L127-L128](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L127-L128) (`clm_57d947abd23d4c31c5edd3633f9650edf8dde944dc0c2045380a69990c3e3bda`)
- [observation/documented] The library claims no runtime dependency on third-party code, since generation happens at compile time within the consumer's project. -- evidence: [README.md#L11-L15](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L11-L15) (`clm_cbeeeb77440fe920478a2afb85a2f0b101b880a0f5a7cf81db577e1bd216e14a`)
- [inference/documented] The tool appears to support route parameters by substituting method arguments into the attribute's path template, as shown by the id route and dictionary usage. -- evidence: [README.md#L23-L38](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L23-L38), [README.md#L111-L113](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L111-L113) (`clm_5c5fbd0bc953a26b6aec7f2bd6e3ddcb7645257fe3bae051739cab4edfec1230`)
- [observation/documented] The README strongly recommends using IHttpClientFactory to resolve HttpClient instances rather than manual instantiation. -- evidence: [README.md#L186-L186](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L186-L186) (`clm_80149ea18ecfd4bc42896614332984f8b60681b9ff13dc5f9c33ee67657b6d0e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Users declare partial classes with partial methods decorated by attributes such as HttpGet containing route templates like "todos/{id}"; the generator implements those methods. -- evidence: [README.md#L51-L66](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L51-L66), [README.md#L23-L38](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L23-L38) (`clm_b1337f2071efa93a672eebdb588d140bab7f081f9e6148fc8d84e56da3ff0e8b`)
- [observation/documented] The generator emits a constructor taking an HttpClient parameter, and the generated method builds route, query, and header dictionaries before delegating to HttpClientHelper.SendAsync. -- evidence: [README.md#L68-L69](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L68-L69), [README.md#L115-L116](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L115-L116), [README.md#L118-L119](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L118-L119), [README.md#L102-L105](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L102-L105), [README.md#L121-L122](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L121-L122), [README.md#L111-L113](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L111-L113) (`clm_2082704fcac7ad0b1684e0868dd3273b36da797da4d0880a7caded6e1ced4fe2`)
- [observation/documented] If the user defines their own HttpClient field/property or a parameterless method returning HttpClient, the generator will use that instead of injecting via constructor. -- evidence: [README.md#L149-L149](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L149-L149), [README.md#L169-L169](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L169-L169), [README.md#L144-L145](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L144-L145) (`clm_304fb050a1c5157ae6855b48ca14c512fb94e64a3a0222f1ab46cb05f33d901a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package targets .NET 5 console apps and is installed via the HttpClientGenerator NuGet package; generated code relies on HttpClientGenerator.Shared helpers and System.Text.Json serialization attributes. -- evidence: [README.md#L18-L20](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L18-L20), [README.md#L40-L43](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L40-L43), [README.md#L88-L93](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L88-L93), [README.md#L23-L38](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L23-L38), [README.md#L121-L122](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L121-L122) (`clm_47d345402434dc7e9afa6b4eeefbc05dc2b9af148658a56d189f1d3bfd7f60dc`)

## limitations (1 claim(s))

- [observation/documented] Known issues include needing a Visual Studio 2019 restart for IntelliSense, a referenced Roslyn issue during development, and incomplete OmniSharp support in VS Code, though the dotnet SDK works. -- evidence: [README.md#L189-L192](https://github.com/Jalalx/HttpClientCodeGenerator/blob/96f70bf67dbfe32d509538c1e5d5a045c8cf302e/README.md#L189-L192) (`clm_a6f2e9847f5bc33b0f313163c547309f7bacd19d38372841446349cfa64022be`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

