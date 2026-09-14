# labring/sealos

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1e97ffc47589 @ fc36ab0d011ee508

## Summary (orientation draft, not independently verified)

Evidence covers README positioning, archived 4.0 architecture and 3.0 design docs, the CLA, and MAINTAINERS.md; no runtime code is included. Claims rest on documentation only, with the maintainers claim corrected to cite the header slices.

## Source coverage

Source coverage (partial): 6 of 498 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Sealos is described as an AI-native cloud operating system built on Kubernetes, covering the application lifecycle from cloud IDE development to production deployment. -- evidence: [README.md#L13-L13](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L13-L13)
- components (2 claim(s)):
  - [observation/documented] The README lists core features including DevBox cloud IDEs, managed databases (PostgreSQL, MySQL, MongoDB, Redis), S3-compatible object storage, and a one-click app store. -- evidence: [README.md#L109-L114](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L109-L114)
  - [observation/documented] App Launchpad is a deployment tool for single images, and Terminal provides command-line services like a single-machine OS terminal; apps can call Kubernetes services or CRD controllers. -- evidence: [docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L17-L19](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L17-L19)
- design-choices (3 claim(s)):
  - [observation/documented] Sealos applications use a front-end/back-end separation architecture, with front-ends able to serve independently via SSR rather than being bound to a monolith. -- evidence: [docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L13-L13](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L13-L13)
  - [observation/documented] The archived 3.0 design states Sealos aimed to be a simple, lightweight, stable Kubernetes installer supporting high-availability installs with a zero-dependency single binary. -- evidence: [docs/archived/3.0/design/design.md#L23-L23](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L23-L23), [docs/archived/3.0/design/design.md#L9-L17](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L9-L17), [docs/archived/3.0/design/design.md#L3-L3](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L3-L3)
- workflows (3 claim(s)):
  - [observation/documented] The 3.0 execution flow generates certs/kubeconfig locally, copies binaries and offline packages to targets, runs kubeadm init on master0, joins other masters forming an etcd cluster, then joins nodes with IPVS rules. -- evidence: [docs/archived/3.0/design/design.md#L54-L58](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L54-L58)
  - [observation/documented] Repository development practice: contributors must sign a Contributor License Agreement granting the company perpetual copyright and patent licenses to contributions, and submitting a contribution constitutes acceptance. -- evidence: [CONTRIBUTOR_LICENSE_AGREEMENT.md#L21-L21](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/CONTRIBUTOR_LICENSE_AGREEMENT.md#L21-L21), [CONTRIBUTOR_LICENSE_AGREEMENT.md#L51-L51](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/CONTRIBUTOR_LICENSE_AGREEMENT.md#L51-L51), [CONTRIBUTOR_LICENSE_AGREEMENT.md#L17-L17](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/CONTRIBUTOR_LICENSE_AGREEMENT.md#L17-L17)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] All services authenticate using kubeconfig as the application identity, giving a consistent experience across browser, sealos CLI, and third-party clients. -- evidence: [docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L5-L5](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L5-L5)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The README notes that Sealos 4.0 extensively uses Buildah functionality to ensure cluster images are OCI-standard compatible. -- evidence: [README.md#L137-L138](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L137-L138)
- limitations (1 claim(s)):
More evidence: [full detail](sealos.detail.md)

Metadata and full claim list: [full detail](sealos.detail.md)
Human notes ([notes](sealos.notes.md), never overwritten by build)

[Back to map index](../../index.md)
