# tractorjuice/arc-kit -- full detail

[Back to orientation](arc-kit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tractorjuice/arc-kit/bc6bf533811df40e363f91a169fac5f1470abeaf/4dba9575cce4f2e6.json](../../../wiki/dossiers/tractorjuice/arc-kit/bc6bf533811df40e363f91a169fac5f1470abeaf/4dba9575cce4f2e6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The `au-federal` recipe defines 35 targets including 9 optional ones, 2 post-build hooks (arckit:health, arckit:pages), schema_version 1, and an explicit top-level `flagship: AU_DISP`. -- evidence: [docs/au-federal-validation-scorecard.md#L157-L164](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L157-L164), [docs/au-federal-validation-scorecard.md#L233-L240](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L233-L240) (`clm_735f8b4431dd41abf3868175ade2230ff550082a0b768cf34718ee4c7a72bbf9`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: regression tests live in `tests/plugin/test_au_federal_recipe.py` (run via pytest with `-k round2` or `-k ai6` filters), and the suite grew from 61 baseline tests to 191 across review rounds. -- evidence: [docs/au-federal-validation-scorecard.md#L349-L349](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L349-L349), [docs/au-federal-validation-scorecard.md#L377-L377](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L377-L377), [docs/au-federal-validation-scorecard.md#L270-L270](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L270-L270) (`clm_58854593a4f7b90e4e8d135ec4f12f8c91ee5d1430d03f0cd2458dde00e77858`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The `/arckit:adm-preliminary` command takes a project ID or transformation scope and produces an Architecture Vision artefact at `projects/<id>/ARC-<id>-ADMP-v1.0.md`. -- evidence: [docs/guides/adm-preliminary.md#L5-L5](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L5-L5), [docs/guides/adm-preliminary.md#L22-L24](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L22-L24), [docs/guides/adm-preliminary.md#L26-L26](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L26-L26) (`clm_841a98a4ee0753a13618047f0fce3b5ce88789934e5eba747c1f48d8e984e63b`)
- [observation/documented] The adm-preliminary deliverable includes scope, drivers, constraints, success criteria, a Mermaid context diagram, stakeholder map, ADM phase coverage, and traceability sections. -- evidence: [docs/guides/adm-preliminary.md#L32-L42](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/guides/adm-preliminary.md#L32-L42) (`clm_1f84c5d7b724043e33a4dd54ba532282a1aed6f7cbdbb3d8879abfd6b7d214c0`)
- [observation/documented] ArcKit commands follow a documented dependency matrix with MANDATORY, RECOMMENDED, and OPTIONAL dependency levels; the strategy command uniquely requires both principles and stakeholders as mandatory inputs. -- evidence: [docs/DEPENDENCY-MATRIX.md#L7-L10](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/DEPENDENCY-MATRIX.md#L7-L10), [docs/DEPENDENCY-MATRIX.md#L111-L128](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/DEPENDENCY-MATRIX.md#L111-L128) (`clm_c5e652784b83f814f02a35332d26c154343003f876425e4ed7a181199ee86fe1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The build harness schedules recipe targets via topological sort over `targets[].deps` with glob expansion; the au-federal plan computes 9 build waves with maximum parallelism of 11 in wave W2. -- evidence: [docs/au-federal-validation-scorecard.md#L196-L196](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L196-L196), [docs/au-federal-validation-scorecard.md#L183-L194](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L183-L194), [docs/au-federal-validation-scorecard.md#L181-L181](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L181-L181) (`clm_49b4294830a88a7e799db03b1cfca10fb8125e8b39b7d16e4ca0cc197593ea1f`)
- [observation/documented] Per the arckit-build skill's recipe-loading rules, the harness reads recipes from `.arckit/recipes/` first, so a project-level override takes precedence over plugin defaults. -- evidence: [docs/au-federal-validation-scorecard.md#L209-L209](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L209-L209) (`clm_a6144611811556b93584874be0eeaab48dd22ab66a85be0f2c3ced79caebf852`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (3 claim(s))

- [observation/documented] A validation scorecard reports 9 evaluation runs of the 8 AU commands with a 25/25 scorecard pass rate at Run 3, zero UK framework leakage, and 220 AU framework references in the artefacts. -- evidence: [docs/au-federal-validation-scorecard.md#L88-L88](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L88-L88), [docs/au-federal-validation-scorecard.md#L30-L41](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L30-L41) (`clm_971f8ebe187e0f299ac9493069ba3952e3fefdfe66be60dabea2adca6d09f214`)
- [observation/documented] Layer A validation tested the 8 community commands against a real Australian SMB engagement (DISP-track, OFFICIAL:Sensitive, pure-SaaS estate), with underlying artefacts available under NDA. -- evidence: [docs/au-federal-validation-scorecard.md#L17-L20](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L17-L20), [docs/au-federal-validation-scorecard.md#L399-L399](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L399-L399) (`clm_d4512348254cacf7dd13b4be2ae289228b0149c57a3e9345deb3ed1e8ce61a85`)
- [observation/documented] Per-command validation assessed au-e8-posture against the ASD Essential Eight (8 strategies x 4 maturity levels), au-pia against all 13 Australian Privacy Principles, au-dss against all 13 Digital Service Standard criteria, and au-ism-controls against 17 ISM control domains. -- evidence: [docs/au-federal-validation-scorecard.md#L45-L54](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/au-federal-validation-scorecard.md#L45-L54) (`clm_cf33e53f213e9887267011bdd2ba5390592790b706c44b7bf456cf9bed283230`)

## dependencies (2 claim(s))

- [observation/documented] The azure-research, aws-research, and gcp-research commands require external MCP servers (Microsoft Learn, AWS Knowledge, and Google Developer Knowledge with an API key) for authoritative cloud documentation. -- evidence: [docs/DEPENDENCY-MATRIX.md#L134-L172](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/DEPENDENCY-MATRIX.md#L134-L172) (`clm_5b395fa597961f27b06eadc6e031e6477045deede9db7a963cd3117060a1fa10`)
- [observation/documented] The trello backlog-export command requires `TRELLO_API_KEY` and `TRELLO_TOKEN` environment variables, and the tenders command relies on a bundled keyless UK Tenders MCP server with best-effort availability. -- evidence: [docs/DEPENDENCY-MATRIX.md#L209-L211](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/DEPENDENCY-MATRIX.md#L209-L211), [docs/DEPENDENCY-MATRIX.md#L178-L196](https://github.com/tractorjuice/arc-kit/blob/bc6bf533811df40e363f91a169fac5f1470abeaf/docs/DEPENDENCY-MATRIX.md#L178-L196) (`clm_c53309a951e85d864899bd535058b520c30b7b6aa1491c6403d71cc886b683f0`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

