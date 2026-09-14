# Extension CI Tools for DuckDB
This repository contains reusable components for building, testing and deploying DuckDB extensions.

DuckDB's [Extension Template](https://github.com/duckdb/extension-template/actions) and various DuckDB Extensions based on the template use this repository to deduplicate code for build configuration and easily update the extension repositories when changes occur to DuckDB's build system and/or CI.

## Pinning DuckDB to the submodule

Extensions vendor DuckDB as a submodule, but pass `duckdb_version` to the build workflows as a
literal, so the two are kept in sync by hand. `_submodule_version.yml` resolves the submodule's pin
instead, making the submodule the single source of truth:

```yaml
jobs:
  duckdb-submodule-version:
    uses: duckdb/extension-ci-tools/.github/workflows/_submodule_version.yml@main

  duckdb-stable-build:
    needs: duckdb-submodule-version
    uses: duckdb/extension-ci-tools/.github/workflows/_extension_distribution.yml@main
    with:
      duckdb_version: ${{ needs.duckdb-submodule-version.outputs.version }}
      ci_tools_version: main
      extension_name: <name>
```

Bumping the submodule is then the only action that moves CI. `submodule_path` defaults to `duckdb`
and can be set to resolve a different submodule.

Note that passing `duckdb_version: ''` also builds whatever the submodule points at, since the
calling repository is checked out with `submodules: recursive` and the ref is only overridden when
non-empty. That path loses the version in artifact names and ccache keys, which the workflow above
preserves.

## Versioning
| Extension-ci-tools Branch | DuckDB target version | Actively maintained? |
|---------------------------|-----------------------|----------------------|
| main                      | main                  | yes                  |
| v1.5.1                    | v1.5.1                | yes                  |
| v1.5.0                    | v1.5.0                | no                   |
| v1.4.4                    | v1.4.4                | yes                  |
| v1.4.3                    | v1.4.3                | no                   |
| v1.4.2                    | v1.4.2                | no                   |
| v1.4.1                    | v1.4.1                | no                   |
| v1.4.0                    | v1.4.0                | no                   |
| v1.3.2                    | v1.3.2                | no                   |
| v1.3.1                    | v1.3.1                | no                   |
| v1.3.0                    | v1.3.0                | no                   |
| <= v1.2.2                 |                       | no                   |

Each branch in this repository targets a specific version of DuckDB. Note that these branches will be continually updated to ensure the build environment is functional for that version of DuckDB.
Also note that at some point, support for versions will be dropped. Currently, we aim to support the latest 2 DuckDB versions, to allow extensions devs to transition to a new DuckDB version.
