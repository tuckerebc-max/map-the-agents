# steamship-core/python-client -- full detail

[Back to orientation](python-client.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/steamship-core/python-client/62b3f9659fd43ce4fe62103b6488514259d1956f/57eb83fc998beb32.json](../../../wiki/dossiers/steamship-core/python-client/62b3f9659fd43ce4fe62103b6488514259d1956f/57eb83fc998beb32.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Config values are exposed to package/plugin code via self.config and are automatically populated by Steamship at invocation time. -- evidence: [docs/nextra/developing/configuration.rst#L56-L58](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L56-L58) (`clm_e88ca0424a4007d1da77308888dbc86d1eb06a25c035bfc265b5ad8a6e6dfb71`)
- [observation/documented] The codebase is layered: base depends on nothing; data on base; plugin on base and data; client on base, data, plugin; and app on all four. -- evidence: [DEVELOPING.md#L63-L67](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L63-L67) (`clm_6d00e8456e6b45c4866c383289e08be539c8cccc30bd69cad22523ab10c4798a`)

## design-choices (2 claim(s))

- [observation/documented] Packages and plugins define configuration by subclassing Config with typed fields (boolean, string, or number), a description, and an optional default, returned via a config_cls class method. -- evidence: [docs/nextra/developing/configuration.rst#L35-L38](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L35-L38), [docs/nextra/developing/configuration.rst#L10-L13](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L10-L13), [docs/nextra/developing/configuration.rst#L40-L40](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L40-L40), [docs/nextra/developing/configuration.rst#L31-L31](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L31-L31) (`clm_918d29d190d877c5d04f0ef359ac5f7c0d931809ba166d9854f8186125c01137`)
- [observation/documented] Configuration parameters without defaults are mandatory: instance creation fails if the user omits them or supplies a wrong type, so packages receive structurally matching config; there are no optional parameters. -- evidence: [docs/nextra/developing/configuration.rst#L15-L18](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L15-L18), [docs/nextra/developing/configuration.rst#L20-L22](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/docs/nextra/developing/configuration.rst#L20-L22) (`clm_6102697f93661c6927175ba582af73ed1f6e77450acadcdc40df59cbc1f5fc80`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors target Python 3.8, format with black and isort, run CI via GitHub Actions, and use pre-commit hooks (flake8, mypy, bandit, etc.) for linting; tests use Pyunit. -- evidence: [DEVELOPING.md#L11-L16](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L11-L16), [DEVELOPING.md#L22-L22](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L22-L22) (`clm_5b289535eb1d0e1431886570e6488df463c22eb5f8fdb4377d3a650226a140e4`)
- [observation/documented] Repository development practice: integration tests run against a live Steamship server using a 'test' profile in ~/.steamship.json, and a client fixture cleans up space-scoped resources, though apps, app versions, plugins, and plugin versions must be destroyed manually. -- evidence: [DEVELOPING.md#L111-L112](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L111-L112), [DEVELOPING.md#L108-L109](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L108-L109), [DEVELOPING.md#L128-L131](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L128-L131), [DEVELOPING.md#L79-L79](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L79-L79), [DEVELOPING.md#L133-L134](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L133-L134) (`clm_a584d98cea3b80ed3e33d1e59389b401df7328610cf2fc378f293467babd64ae`)
- [observation/documented] Repository development practice: releases are deployed by creating a semver tag (without 'v') targeting main via the GitHub Release feature. -- evidence: [DEVELOPING.md#L140-L143](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L140-L143), [DEVELOPING.md#L138-L138](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/DEVELOPING.md#L138-L138) (`clm_20f595ad8df8899839f8d2da22e3629317b37cfd294fa3a4db9bf856c3e8fc32`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The library supports building and deploying Agents, Packages, and Plugins on Steamship, and making client calls to a Steamship Package from Python. -- evidence: [README.md#L10-L12](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L10-L12) (`clm_dcb60a61f6d6066125c3716b67710ea1441c26471b9cbebb4010a2ebe3a5cede`)
- [observation/documented] The package is installable via pip as 'steamship'. -- evidence: [README.md#L26-L26](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L26-L26), [README.md#L28-L30](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L28-L30) (`clm_21d437d194f5624aae880abc9ff6d8100bf46e08ce2c53e436615dd23000b314`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies include requests, pydantic, aiohttp, inflection, fluent-logger, toml, click, semver, and tiktoken. -- evidence: [requirements.txt#L1-L9](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/requirements.txt#L1-L9) (`clm_1cfd03bf28362670b6ffadcc26c93fb838998c2dfddf9d8e4357239bc074534d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The README points agent builders to a multimodal agent starter project, an agent guidebook, and a separate Steamship-Langchain compatibility library for hosting LangChain agents. -- evidence: [README.md#L16-L16](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L16-L16), [README.md#L22-L22](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L22-L22), [README.md#L20-L20](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L20-L20), [README.md#L18-L18](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L18-L18), [README.md#L14-L14](https://github.com/steamship-core/python-client/blob/62b3f9659fd43ce4fe62103b6488514259d1956f/README.md#L14-L14) (`clm_acb36fdd14ccde9079d51375169d81bf26e3cc706ecc4de93165597f907a194c`)

