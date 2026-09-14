# duckdb/extension-ci-tools -- full detail

[Back to orientation](extension-ci-tools.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/duckdb/extension-ci-tools/8fd4bb14edb07f8ba82809355e683d3647544994/b0f51f1531bcbd06.json](../../../wiki/dossiers/duckdb/extension-ci-tools/8fd4bb14edb07f8ba82809355e683d3647544994/b0f51f1531bcbd06.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The repository provides reusable components for building, testing and deploying DuckDB extensions, used by the extension template and other extensions to deduplicate build/CI configuration. -- evidence: [README.md#L2-L2](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L2-L2), [README.md#L4-L4](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L4-L4) (`clm_68edf777afcc475e24a9a5d420a7b74072198676eca161d1336f60d4fca16cc3`)
- [observation/documented] It exposes reusable GitHub Actions workflows such as _submodule_version.yml and _extension_distribution.yml that extension repositories invoke with 'uses: duckdb/extension-ci-tools/...'. -- evidence: [README.md#L12-L15](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L12-L15), [README.md#L17-L24](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L17-L24) (`clm_4d4b4671a5e4e639625ad1a8f20b4ee32dbde9c72d130035ae8b4febd5f58ed4`)

## design-choices (3 claim(s))

- [observation/documented] The _submodule_version workflow makes the vendored DuckDB submodule the single source of truth for the version, so bumping the submodule is the only action that moves CI. -- evidence: [README.md#L26-L27](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L26-L27), [README.md#L8-L10](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L8-L10) (`clm_11e1922f20ee797131209d767d7333c239c3f4c95bd42d49ddc9f93844d45b67`)
- [observation/documented] Passing an empty duckdb_version also builds whatever the submodule points at, but loses the version in artifact names and ccache keys, which the submodule-version workflow preserves. -- evidence: [README.md#L29-L32](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L29-L32) (`clm_78ca9928c3e6d330d2e96098ec1c3dfd9b205e961d2c80f2bdd360247afb8ea3`)
- [observation/documented] Each branch of the repository targets a specific DuckDB version (e.g. main targets main, v1.4.4 targets v1.4.4), with a table indicating which branches are actively maintained. -- evidence: [README.md#L35-L48](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L35-L48) (`clm_104052cd48530dba26b10fbc924c2b1b379beaa6e0bd0c9c9ffdf46ea07e2308`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: maintained branches are continually updated so the build environment stays functional for their targeted DuckDB version. -- evidence: [README.md#L50-L51](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L50-L51) (`clm_9350d38132507e1d1b05e60f50176e371cc9a0c9fd30e2ddeb841e4685339e00`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The _extension_distribution workflow accepts inputs including duckdb_version, ci_tools_version and extension_name, with duckdb_version fed from the submodule-version job's output. -- evidence: [README.md#L17-L24](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L17-L24) (`clm_49f704eeb0d9b9a90ad308cd35a3ab921995ef1e8e05be2b18173556b4b9286e`)
- [observation/documented] The submodule-version workflow accepts a submodule_path input that defaults to 'duckdb' and can be set to resolve a different submodule. -- evidence: [README.md#L26-L27](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L26-L27) (`clm_c8301ed2f4185ff103918a501c63bf8eef7fb0148942c1c62ac8bd555a6d3d05`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Extensions vendor DuckDB as a git submodule and normally pass a duckdb_version literal to workflows, keeping the two in sync by hand unless the submodule-resolution workflow is used. -- evidence: [README.md#L8-L10](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L8-L10) (`clm_fa4be3aebef193acf831fc5152163ace14b285fdeaf35156ebe5c6c5480628be`)

## limitations (1 claim(s))

- [observation/documented] Support for older DuckDB versions will eventually be dropped; the maintainers currently aim to support the latest two DuckDB versions to ease extension developers' transitions. -- evidence: [README.md#L50-L51](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L50-L51) (`clm_02c7c85b764f82551e3be1c1f76199e4a895b004381ecf913f5ccd010b6d21cd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

