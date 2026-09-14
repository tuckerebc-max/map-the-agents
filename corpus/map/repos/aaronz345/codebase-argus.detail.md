# aaronz345/codebase-argus -- full detail

[Back to orientation](codebase-argus.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aaronz345/codebase-argus/71922e7555f36c9d62a0525824924f38f4ec73e7/3d55409f5967b792.json](../../../wiki/dossiers/aaronz345/codebase-argus/71922e7555f36c9d62a0525824924f38f4ec73e7/3d55409f5967b792.json)

## specifications (1 claim(s))

- [observation/documented] The README describes the tool as a review desk for maintainers that inspects pull requests, failing CI logs, and long-lived fork syncs using one shared set of signals: patches, checks, files, branch state, policy gates, provider consensus, and local git simulations. -- evidence: [README.md#L36-L39](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L36-L39) (`clm_5c485a14b23d2dbf192107ce1eb2a28d83862ccd53d84dab190da0762a5a8abd`)

## components (1 claim(s))

- [observation/documented] An at-a-glance table documents five distinct workflows - PR review, CI review, autofix planning, downstream fork sync, and agent handoff - each with its own input shape and output type. -- evidence: [README.md#L79-L85](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L79-L85) (`clm_86a718931ea50333c5e020fd9ab2571215d14f38c4aff7760ee476f5155e7292`)

## design-choices (1 claim(s))

- [observation/documented] A planning document describes an intended architecture where pr-review.ts keeps responsibility for normalized review results, while new, separately focused helpers would own policy parsing, evidence extraction, tribunal aggregation, and workflow generation. -- evidence: [docs/superpowers/plans/2026-05-06-maintainer-firewall-mvp.md#L7-L7](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/docs/superpowers/plans/2026-05-06-maintainer-firewall-mvp.md#L7-L7) (`clm_548998f926307520e3f4bc82ab447d44491b8c11c4587c59e7e0bd39ab3bf477`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] A README permission table lists pull requests and issues with read/write access; contents, checks, actions and metadata have read access. -- evidence: [README.md#L295-L302](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L295-L302) (`clm_517d94e14589086c60f2ce90add1156d1dc387cc9f931e3474190eed7a296b61`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] A write-model table documents narrow write behavior: the hosted demo is read-only, GitHub App reviews post comment-level PR reviews, and the sync command runs dry-run unless --execute, --push, or --create-pr is explicitly passed. -- evidence: [README.md#L451-L458](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L451-L458) (`clm_d4eff823ec7e80f52ec8973fffbc4edf532ffd723263acc87a4053b18620cc99`)
- [observation/documented] Documented webhook behavior includes verifying the X-Hub-Signature-256 header before handling a payload, and skipping draft pull requests as well as PRs labeled argus:paused. -- evidence: [README.md#L337-L343](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/README.md#L337-L343) (`clm_87fa7e9c7c1f6b35ff6f5a908ff1fae5cf80902fe8ba7bd5f4d211b6ca3215ee`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The case study frames its own output as a review aid rather than an approval, noting that pull-request state and code can change after the reviewed snapshot was taken. -- evidence: [docs/case-studies/cowagent-2965.md#L34-L34](https://github.com/AaronZ345/codebase-argus/blob/71922e7555f36c9d62a0525824924f38f4ec73e7/docs/case-studies/cowagent-2965.md#L34-L34) (`clm_2434a176385d1381aa0f16dd9230f9a881b0bc9c0461548218e9658040a6e8a3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

