---
access: public
aliases: []
claim_ids:
- clm_29c55ca8eb0bd52a891fc4369c17d5368182cc5a0310939b79220770a7be41ea
- clm_2ff6055117851266b4f13e022f2b0b932dcdd3548955b1681111fe93b54047d0
- clm_7fe0e4579ffa2c346dc39525b89526470f17a21429249aaeff5387821a2a9ad9
- clm_a415dcb4911d3dd6aa014005e8ad0fa4787e6c6fd4b1a6fa220578ae78f76b54
- clm_d7d96f67ea5eb51e39aeefcb5b0fd7aa8740698b6e84646bce3bdc0a1752f8e8
maturity: draft
page_id: pg_8e563697a5645116b3d53c7151b4c07c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c7194927ce765c25af06663cc65b0c15
title: agentscope-ai/AgentTeams/docs/design/agent-pod-template.md @ f65d6e1af268
updated_at: '2026-09-14T01:31:19Z'
---

# agentscope-ai/AgentTeams/docs/design/agent-pod-template.md @ f65d6e1af268

<!-- rcw:begin owner=source:src_c7194927ce765c25af06663cc65b0c15 block=evidence -->
- Cluster-specific Pod settings (sysctls, nodeSelectors, tolerations, imagePullSecrets, injector annotations) are injected via a corev1.PodTemplateSpec stored in a ConfigMap under the key pod-template.yaml, read on every Create call. [@claim:clm_29c55ca8eb0bd52a891fc4369c17d5368182cc5a0310939b79220770a7be41ea]
- The controller creates one Kubernetes Pod per Manager and Worker; by default each Pod has a single 'worker' container, a projected agentteams-token volume, and the controller-managed ServiceAccount. [@claim:clm_2ff6055117851266b4f13e022f2b0b932dcdd3548955b1681111fe93b54047d0]
- Merge semantics are field-specific: the template wins for nodeSelector, tolerations, affinity, securityContext, and non-worker sidecar containers; the controller wins for ownerReferences, serviceAccountName, forced automountServiceAccountToken=false, and the agent container's image/env; labels and annotations merge with controller values overwriting on key collision. [@claim:clm_7fe0e4579ffa2c346dc39525b89526470f17a21429249aaeff5387821a2a9ad9]
- The pod template ConfigMap is read fresh on each Pod creation with no caching: edits affect the next created Pod while existing Pods are untouched; a missing, malformed, or unfetchable ConfigMap falls back to the default Pod shape without blocking creation. [@claim:clm_a415dcb4911d3dd6aa014005e8ad0fa4787e6c6fd4b1a6fa220578ae78f76b54]
- AGENTTEAMS_CONTROLLER_NAME doubles as the leader-election lease name and the agentteams.io/controller label stamped on created CRs; informer caches filter by this label so multiple releases in one namespace do not reconcile each other's resources, and incluster startup without it fails fast. [@claim:clm_d7d96f67ea5eb51e39aeefcb5b0fd7aa8740698b6e84646bce3bdc0a1752f8e8]
<!-- rcw:end owner=source:src_c7194927ce765c25af06663cc65b0c15 block=evidence -->

## Researcher notes

