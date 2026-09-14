---
access: public
aliases: []
claim_ids:
- clm_2fcb2767dcd69536896f4d6f3873c56736be3e76f8268cbd7bd87683564d1c4a
- clm_55a9e34017ba14a6aab899ad5923f1ac573f98603c29947b74c2e4f696e04e8a
- clm_56909b6ed46a9a9058cc5b7f33e51de55d3e8af237e135514317470f652005cd
- clm_57a96008aceb4f0cb8e22c19e62fce375b2aed703084d11bcfb9bb54000a437a
- clm_dd206cd13be8d19ec200150eeee0becb82dbc26a45669589d7115c34930483fc
- clm_dffb6accce2b95fc792a6648d4e30ea6d2045e60f6c3e0547226edf7d4222210
- clm_f894b5256aca07f47e53efd559589e098761386a79069f96291c384af67aeaa5
maturity: draft
page_id: pg_8890317dc5185b0f8cb07c7ff9231842
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e52e0003371754c0afa9781e8ac3d2cc
title: agentscope-ai/AgentTeams/docs/design/internal/agentteams-controller-refactor-progress.md
  @ f65d6e1af268
updated_at: '2026-09-14T01:31:19Z'
---

# agentscope-ai/AgentTeams/docs/design/internal/agentteams-controller-refactor-progress.md @ f65d6e1af268

<!-- rcw:begin owner=source:src_e52e0003371754c0afa9781e8ac3d2cc block=evidence -->
- Per the internal progress doc, ConfigVersionManager, versions.json management, skill hot-update (UpgradeSkills), runtime rolling upgrade, agt config push, debug commands, apply --prune, and all Phase 4 debug/upgrade capabilities are unimplemented. [@claim:clm_2fcb2767dcd69536896f4d6f3873c56736be3e76f8268cbd7bd87683564d1c4a]
- The progress doc marks Phase 3 items partially done: Manager state.json-to-OSS migration and quota checks are unimplemented, and fine-grained CallerIdentity isolation beyond SA token authentication remains incomplete. [@claim:clm_55a9e34017ba14a6aab899ad5923f1ac573f98603c29947b74c2e4f696e04e8a]
- Worker, Team, Human, and Manager CRDs each have Helm crds/, api/v1beta1 types, and reconcilers marked complete, while the DebugWorker CRD is not implemented. [@claim:clm_56909b6ed46a9a9058cc5b7f33e51de55d3e8af237e135514317470f652005cd]
- The agt CLI was rewritten as a pure REST API client calling the controller at AGENTTEAMS_CONTROLLER_URL (default http://localhost:8090), supporting CRUD for workers/teams/humans/managers, worker wake/sleep/status, YAML and ZIP apply, with tokens via AGENTTEAMS_AUTH_TOKEN or SA token file discovery. [@claim:clm_57a96008aceb4f0cb8e22c19e62fce375b2aed703084d11bcfb9bb54000a437a]
- A WorkerBackend abstraction layer unifies worker lifecycle management; the progress doc marks the interface, Docker backend, Kubernetes backend, and backend auto-selection as complete, and lists additional SAE, APIG gateway, gateway abstraction, and cloud-credential files as implemented beyond the design. [@claim:clm_dd206cd13be8d19ec200150eeee0becb82dbc26a45669589d7115c34930483fc]
- The Helm chart ships controller Deployment/Service/RBAC/ServiceAccount, Tuwunel and MinIO StatefulSets, Higress as a subchart, Element Web, and a Manager Deployment; an Ingress template is not yet implemented per the progress doc. [@claim:clm_dffb6accce2b95fc792a6648d4e30ea6d2045e60f6c3e0547226edf7d4222210]
- An embedded all-in-one image bundles Higress, Tuwunel, MinIO, Element Web, the controller, CLI, and kube-apiserver, started in layers via supervisord; deployment is dual-container (controller container plus an auto-created manager-agent container created via DockerBackend). [@claim:clm_f894b5256aca07f47e53efd559589e098761386a79069f96291c384af67aeaa5]
<!-- rcw:end owner=source:src_e52e0003371754c0afa9781e8ac3d2cc block=evidence -->

## Researcher notes

