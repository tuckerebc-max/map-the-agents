# steamship-core/python-client

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 62b3f9659fd4 @ 57eb83fc998beb32

## Summary (orientation draft, not independently verified)

The snapshot is the Steamship Python SDK repository: a client library for building/deploying Agents, Packages, and Plugins on Steamship and calling Packages from Python. Evidence covers the SDK's purpose, installation, configuration model, internal package layering, runtime dependencies, and contributor setup/testing practices.

## Source coverage

Source coverage (partial): 6 of 144 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Config values are exposed to package/plugin code via self.config and are automatically populated by Steamship at invocation time. -- evidence: [docs/nextra/developing/configuration.rst#L56-L58](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L56-L58)
  - [observation/documented] The codebase is layered: base depends on nothing; data on base; plugin on base and data; client on base, data, plugin; and app on all four. -- evidence: [DEVELOPING.md#L63-L67](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L63-L67)
- design-choices (2 claim(s)):
  - [observation/documented] Packages and plugins define configuration by subclassing Config with typed fields (boolean, string, or number), a description, and an optional default, returned via a config_cls class method. -- evidence: [docs/nextra/developing/configuration.rst#L35-L38](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L35-L38), [docs/nextra/developing/configuration.rst#L10-L13](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L10-L13), [docs/nextra/developing/configuration.rst#L40-L40](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L40-L40), [docs/nextra/developing/configuration.rst#L31-L31](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L31-L31)
  - [observation/documented] Configuration parameters without defaults are mandatory: instance creation fails if the user omits them or supplies a wrong type, so packages receive structurally matching config; there are no optional parameters. -- evidence: [docs/nextra/developing/configuration.rst#L15-L18](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L15-L18), [docs/nextra/developing/configuration.rst#L20-L22](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L20-L22)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors target Python 3.8, format with black and isort, run CI via GitHub Actions, and use pre-commit hooks (flake8, mypy, bandit, etc.) for linting; tests use Pyunit. -- evidence: [DEVELOPING.md#L11-L16](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L11-L16), [DEVELOPING.md#L22-L22](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L22-L22)
  - [observation/documented] Repository development practice: integration tests run against a live Steamship server using a 'test' profile in ~/.steamship.json, and a client fixture cleans up space-scoped resources, though apps, app versions, plugins, and plugin versions must be destroyed manually. -- evidence: [DEVELOPING.md#L111-L112](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L111-L112), [DEVELOPING.md#L108-L109](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L108-L109), [DEVELOPING.md#L128-L131](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L128-L131), [DEVELOPING.md#L79-L79](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L79-L79), [DEVELOPING.md#L133-L134](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L133-L134)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The library supports building and deploying Agents, Packages, and Plugins on Steamship, and making client calls to a Steamship Package from Python. -- evidence: [README.md#L10-L12](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L10-L12)
  - [observation/documented] The package is installable via pip as 'steamship'. -- evidence: [README.md#L26-L26](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L26-L26), [README.md#L28-L30](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L28-L30)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Runtime dependencies include requests, pydantic, aiohttp, inflection, fluent-logger, toml, click, semver, and tiktoken. -- evidence: [requirements.txt#L1-L9](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/requirements.txt#L1-L9)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](python-client.detail.md)

Metadata and full claim list: [full detail](python-client.detail.md)
Human notes ([notes](python-client.notes.md), never overwritten by build)

[Back to map index](../../index.md)
