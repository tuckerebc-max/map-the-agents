# labring/sealos -- full detail

[Back to orientation](sealos.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/labring/sealos/1e97ffc475898cefae9ef1b095344a8c74ef7f87/fc36ab0d011ee508.json](../../../wiki/dossiers/labring/sealos/1e97ffc475898cefae9ef1b095344a8c74ef7f87/fc36ab0d011ee508.json)

## specifications (1 claim(s))

- [observation/documented] Sealos is described as an AI-native cloud operating system built on Kubernetes, covering the application lifecycle from cloud IDE development to production deployment. -- evidence: [README.md#L13-L13](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L13-L13) (`clm_c5b27fe6421668b73c450db68e2604edd3bf9ef9d2d68724b4f7caeffdb01dd6`)

## components (2 claim(s))

- [observation/documented] The README lists core features including DevBox cloud IDEs, managed databases (PostgreSQL, MySQL, MongoDB, Redis), S3-compatible object storage, and a one-click app store. -- evidence: [README.md#L109-L114](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L109-L114) (`clm_18542f01c422aeee63d324f3a801b2f1a28438c6b8091dc24a90c1bbd47190e1`)
- [observation/documented] App Launchpad is a deployment tool for single images, and Terminal provides command-line services like a single-machine OS terminal; apps can call Kubernetes services or CRD controllers. -- evidence: [docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L17-L19](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L17-L19) (`clm_acd70e486d81f3d2b6d1217f8ffc5231724c6904c8f82cbeda1313accf9a5c67`)

## design-choices (3 claim(s))

- [observation/documented] Sealos applications use a front-end/back-end separation architecture, with front-ends able to serve independently via SSR rather than being bound to a monolith. -- evidence: [docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L13-L13](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L13-L13) (`clm_90805b7f9e27885ba75f0f5a0e5fd913c03e2fc9120de0dc2cb1d2d3586e58b5`)
- [observation/documented] The archived 3.0 design states Sealos aimed to be a simple, lightweight, stable Kubernetes installer supporting high-availability installs with a zero-dependency single binary. -- evidence: [docs/archived/3.0/design/design.md#L23-L23](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L23-L23), [docs/archived/3.0/design/design.md#L9-L17](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L9-L17), [docs/archived/3.0/design/design.md#L3-L3](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L3-L3) (`clm_d6dc9733c3568670dff2dd51dbfbea770b7e955f452df037a359324d2a7003f7`)
- [observation/documented] For local load balancing, the 3.0 design chose kernel IPVS managed by an lvscare static pod over envoy/nginx, pre-creating IPVS rules before node join and cleaning them if apiserver becomes unreachable. -- evidence: [docs/archived/3.0/design/design.md#L65-L79](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L65-L79), [docs/archived/3.0/design/design.md#L43-L43](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L43-L43), [docs/archived/3.0/design/design.md#L49-L49](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L49-L49), [docs/archived/3.0/design/design.md#L45-L45](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L45-L45) (`clm_e172f7c0d2d84ea14b107d852c6a21b9bb8a882d2f39c8ad4117551ea417d5ad`)

## workflows (3 claim(s))

- [observation/documented] The 3.0 execution flow generates certs/kubeconfig locally, copies binaries and offline packages to targets, runs kubeadm init on master0, joins other masters forming an etcd cluster, then joins nodes with IPVS rules. -- evidence: [docs/archived/3.0/design/design.md#L54-L58](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/3.0/design/design.md#L54-L58) (`clm_6a298b67c3bab5a84caf1c7adae3583343794eff32536f4b87ffb1f860946cde`)
- [observation/documented] Repository development practice: contributors must sign a Contributor License Agreement granting the company perpetual copyright and patent licenses to contributions, and submitting a contribution constitutes acceptance. -- evidence: [CONTRIBUTOR_LICENSE_AGREEMENT.md#L21-L21](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/CONTRIBUTOR_LICENSE_AGREEMENT.md#L21-L21), [CONTRIBUTOR_LICENSE_AGREEMENT.md#L51-L51](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/CONTRIBUTOR_LICENSE_AGREEMENT.md#L51-L51), [CONTRIBUTOR_LICENSE_AGREEMENT.md#L17-L17](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/CONTRIBUTOR_LICENSE_AGREEMENT.md#L17-L17) (`clm_f204ce090d30d37c599f4b7629bca482f7a557bf6c7faccd818682655f01502c`)
- [observation/documented] Repository development practice: MAINTAINERS.md lists seven maintainers, and names fanux, cuisongliu, and zzjin as both reviewers and approvers. -- evidence: [MAINTAINERS.md#L17-L17](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/MAINTAINERS.md#L17-L17), [MAINTAINERS.md#L13-L15](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/MAINTAINERS.md#L13-L15), [MAINTAINERS.md#L11-L11](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/MAINTAINERS.md#L11-L11), [MAINTAINERS.md#L19-L21](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/MAINTAINERS.md#L19-L21), [MAINTAINERS.md#L3-L9](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/MAINTAINERS.md#L3-L9) (`clm_d74fc67ecb1cdfb33492e909a21f5b1d461d6fcdaaf13b11e191508ce7ab23a2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] All services authenticate using kubeconfig as the application identity, giving a consistent experience across browser, sealos CLI, and third-party clients. -- evidence: [docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L5-L5](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/docs/archived/4.0/docs/advanced-guide/Architecture/Architecture.md#L5-L5) (`clm_3d0712c05a1e7f49d8d5954b704782016e2303fa49e2e250ebc40853505571a6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README notes that Sealos 4.0 extensively uses Buildah functionality to ensure cluster images are OCI-standard compatible. -- evidence: [README.md#L137-L138](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L137-L138) (`clm_87d55af4a1a9bd68bb5af4b4fb076e01a3efd53ee7293509a4e59e5d057b5832`)

## limitations (1 claim(s))

- [observation/documented] Sealos uses a custom 'Sealos Sustainable Use License' permitting internal business and personal non-commercial use but prohibiting providing cloud services to third parties; it is explicitly not a standard open-source license. -- evidence: [README.md#L150-L150](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L150-L150), [README.md#L145-L145](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L145-L145), [README.md#L147-L148](https://github.com/labring/sealos/blob/1e97ffc475898cefae9ef1b095344a8c74ef7f87/README.md#L147-L148) (`clm_f4539cadeb2f0a5724a772f4f27e9030385a3a4c9539d85ea1ed723bf304d082`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

