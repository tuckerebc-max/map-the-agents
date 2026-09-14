---
access: public
aliases: []
claim_ids:
- clm_6a298b67c3bab5a84caf1c7adae3583343794eff32536f4b87ffb1f860946cde
- clm_d6dc9733c3568670dff2dd51dbfbea770b7e955f452df037a359324d2a7003f7
- clm_e172f7c0d2d84ea14b107d852c6a21b9bb8a882d2f39c8ad4117551ea417d5ad
maturity: draft
page_id: pg_720b1af527c454f39397cad35a88e2a1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f6e5ed47b16f50969163d926b14045d5
title: labring/sealos/docs/archived/3.0/design/design.md @ 1e97ffc47589
updated_at: '2026-09-14T04:04:55Z'
---

# labring/sealos/docs/archived/3.0/design/design.md @ 1e97ffc47589

<!-- rcw:begin owner=source:src_f6e5ed47b16f50969163d926b14045d5 block=evidence -->
- The 3.0 execution flow generates certs/kubeconfig locally, copies binaries and offline packages to targets, runs kubeadm init on master0, joins other masters forming an etcd cluster, then joins nodes with IPVS rules. [@claim:clm_6a298b67c3bab5a84caf1c7adae3583343794eff32536f4b87ffb1f860946cde]
- The archived 3.0 design states Sealos aimed to be a simple, lightweight, stable Kubernetes installer supporting high-availability installs with a zero-dependency single binary. [@claim:clm_d6dc9733c3568670dff2dd51dbfbea770b7e955f452df037a359324d2a7003f7]
- For local load balancing, the 3.0 design chose kernel IPVS managed by an lvscare static pod over envoy/nginx, pre-creating IPVS rules before node join and cleaning them if apiserver becomes unreachable. [@claim:clm_e172f7c0d2d84ea14b107d852c6a21b9bb8a882d2f39c8ad4117551ea417d5ad]
<!-- rcw:end owner=source:src_f6e5ed47b16f50969163d926b14045d5 block=evidence -->

## Researcher notes

