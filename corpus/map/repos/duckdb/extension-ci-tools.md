# duckdb/extension-ci-tools

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8fd4bb14edb0 @ b0f51f1531bcbd06

## Summary (orientation draft, not independently verified)

The snapshot is a README describing duckdb/extension-ci-tools, a set of reusable GitHub Actions workflows for building, testing and deploying DuckDB extensions, including a submodule-based version-pinning workflow and a branch-per-DuckDB-version scheme.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The repository provides reusable components for building, testing and deploying DuckDB extensions, used by the extension template and other extensions to deduplicate build/CI configuration. -- evidence: [README.md#L2-L2](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L2-L2), [README.md#L4-L4](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L4-L4)
  - [observation/documented] It exposes reusable GitHub Actions workflows such as _submodule_version.yml and _extension_distribution.yml that extension repositories invoke with 'uses: duckdb/extension-ci-tools/...'. -- evidence: [README.md#L12-L15](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L12-L15), [README.md#L17-L24](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L17-L24)
- design-choices (3 claim(s)):
  - [observation/documented] The _submodule_version workflow makes the vendored DuckDB submodule the single source of truth for the version, so bumping the submodule is the only action that moves CI. -- evidence: [README.md#L26-L27](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L26-L27), [README.md#L8-L10](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L8-L10)
  - [observation/documented] Passing an empty duckdb_version also builds whatever the submodule points at, but loses the version in artifact names and ccache keys, which the submodule-version workflow preserves. -- evidence: [README.md#L29-L32](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L29-L32)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: maintained branches are continually updated so the build environment stays functional for their targeted DuckDB version. -- evidence: [README.md#L50-L51](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L50-L51)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The _extension_distribution workflow accepts inputs including duckdb_version, ci_tools_version and extension_name, with duckdb_version fed from the submodule-version job's output. -- evidence: [README.md#L17-L24](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L17-L24)
  - [observation/documented] The submodule-version workflow accepts a submodule_path input that defaults to 'duckdb' and can be set to resolve a different submodule. -- evidence: [README.md#L26-L27](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L26-L27)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Extensions vendor DuckDB as a git submodule and normally pass a duckdb_version literal to workflows, keeping the two in sync by hand unless the submodule-resolution workflow is used. -- evidence: [README.md#L8-L10](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L8-L10)
- limitations (1 claim(s)):
  - [observation/documented] Support for older DuckDB versions will eventually be dropped; the maintainers currently aim to support the latest two DuckDB versions to ease extension developers' transitions. -- evidence: [README.md#L50-L51](https://github.com/duckdb/extension-ci-tools/blob/8fd4bb14edb07f8ba82809355e683d3647544994/README.md#L50-L51)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](extension-ci-tools.detail.md) for every claim.)

Metadata and full claim list: [full detail](extension-ci-tools.detail.md)
Human notes ([notes](extension-ci-tools.notes.md), never overwritten by build)

[Back to map index](../../index.md)
