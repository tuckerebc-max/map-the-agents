# agentscope-ai/agentteams -- full detail

[Back to orientation](agentteams.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agentscope-ai/agentteams/f65d6e1af268039507b413e3c16679bb84d21ac7/00898cd68a276fb4.json](../../../wiki/dossiers/agentscope-ai/agentteams/f65d6e1af268039507b413e3c16679bb84d21ac7/00898cd68a276fb4.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The controller creates one Kubernetes Pod per Manager and Worker; by default each Pod has a single 'worker' container, a projected agentteams-token volume, and the controller-managed ServiceAccount. -- evidence: [docs/design/agent-pod-template.md#L3-L6](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L3-L6) (`clm_2ff6055117851266b4f13e022f2b0b932dcdd3548955b1681111fe93b54047d0`)
- [observation/documented] A WorkerBackend abstraction layer unifies worker lifecycle management; the progress doc marks the interface, Docker backend, Kubernetes backend, and backend auto-selection as complete, and lists additional SAE, APIG gateway, gateway abstraction, and cloud-credential files as implemented beyond the design. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L47-L52](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L47-L52), [docs/design/internal/agentteams-controller-refactor-progress.md#L38-L43](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L38-L43) (`clm_dd206cd13be8d19ec200150eeee0becb82dbc26a45669589d7115c34930483fc`)
- [observation/documented] The Helm chart ships controller Deployment/Service/RBAC/ServiceAccount, Tuwunel and MinIO StatefulSets, Higress as a subchart, Element Web, and a Manager Deployment; an Ingress template is not yet implemented per the progress doc. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L142-L155](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L142-L155) (`clm_dffb6accce2b95fc792a6648d4e30ea6d2045e60f6c3e0547226edf7d4222210`)
- [observation/documented] Worker, Team, Human, and Manager CRDs each have Helm crds/, api/v1beta1 types, and reconcilers marked complete, while the DebugWorker CRD is not implemented. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L159-L165](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L159-L165) (`clm_56909b6ed46a9a9058cc5b7f33e51de55d3e8af237e135514317470f652005cd`)

## design-choices (5 claim(s))

- [observation/documented] The pod template ConfigMap is read fresh on each Pod creation with no caching: edits affect the next created Pod while existing Pods are untouched; a missing, malformed, or unfetchable ConfigMap falls back to the default Pod shape without blocking creation. -- evidence: [docs/design/agent-pod-template.md#L34-L36](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L34-L36), [docs/design/agent-pod-template.md#L30-L32](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L30-L32) (`clm_a415dcb4911d3dd6aa014005e8ad0fa4787e6c6fd4b1a6fa220578ae78f76b54`)
- [observation/documented] Merge semantics are field-specific: the template wins for nodeSelector, tolerations, affinity, securityContext, and non-worker sidecar containers; the controller wins for ownerReferences, serviceAccountName, forced automountServiceAccountToken=false, and the agent container's image/env; labels and annotations merge with controller values overwriting on key collision. -- evidence: [docs/design/agent-pod-template.md#L83-L86](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L83-L86), [docs/design/agent-pod-template.md#L69-L79](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L69-L79), [docs/design/agent-pod-template.md#L90-L97](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L90-L97) (`clm_7fe0e4579ffa2c346dc39525b89526470f17a21429249aaeff5387821a2a9ad9`)
- [observation/documented] AGENTTEAMS_CONTROLLER_NAME doubles as the leader-election lease name and the agentteams.io/controller label stamped on created CRs; informer caches filter by this label so multiple releases in one namespace do not reconcile each other's resources, and incluster startup without it fails fast. -- evidence: [docs/design/agent-pod-template.md#L21-L28](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L21-L28) (`clm_d7d96f67ea5eb51e39aeefcb5b0fd7aa8740698b6e84646bce3bdc0a1752f8e8`)
- [observation/documented] The refactor design gives Team Leaders heartbeat-based worker lifecycle management (wake/sleep, idle timeout) with controller-enforced permission isolation: leaders may only manage workers of their own team, and workers cannot manage other workers. -- evidence: [docs/design/internal/agentteams-controller-refactor.md#L534-L534](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L534-L534), [docs/design/internal/agentteams-controller-refactor.md#L570-L578](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L570-L578), [docs/design/internal/agentteams-controller-refactor.md#L481-L508](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L481-L508), [docs/design/internal/agentteams-controller-refactor.md#L563-L568](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L563-L568), [docs/design/internal/agentteams-controller-refactor.md#L556-L561](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L556-L561), [docs/design/internal/agentteams-controller-refactor.md#L520-L525](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L520-L525), [docs/design/internal/agentteams-controller-refactor.md#L580-L583](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L580-L583) (`clm_4897f815bb90c844c68b4e1e38184a56a3c1109b24a4677708c5d674c6d8e6c6`)
- [observation/documented] The design targets two deployment modes: K8s incluster via Helm, and backward-compatible embedded mode where the controller manages worker containers through the Docker socket and runs an embedded kube-apiserver plus kine (SQLite) as a K8s API compatibility layer. -- evidence: [docs/design/internal/agentteams-controller-refactor.md#L102-L102](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L102-L102), [docs/design/internal/agentteams-controller-refactor.md#L82-L92](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor.md#L82-L92) (`clm_b8704347047e463dd3187992c90c92b5d3cdbc3f7b393bab11d5c84481f5a1a3`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Cluster-specific Pod settings (sysctls, nodeSelectors, tolerations, imagePullSecrets, injector annotations) are injected via a corev1.PodTemplateSpec stored in a ConfigMap under the key pod-template.yaml, read on every Create call. -- evidence: [docs/design/agent-pod-template.md#L14-L19](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L14-L19), [docs/design/agent-pod-template.md#L8-L10](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L8-L10) (`clm_29c55ca8eb0bd52a891fc4369c17d5368182cc5a0310939b79220770a7be41ea`)
- [observation/documented] The agt CLI was rewritten as a pure REST API client calling the controller at AGENTTEAMS_CONTROLLER_URL (default http://localhost:8090), supporting CRUD for workers/teams/humans/managers, worker wake/sleep/status, YAML and ZIP apply, with tokens via AGENTTEAMS_AUTH_TOKEN or SA token file discovery. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L120-L120](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L120-L120), [docs/design/internal/agentteams-controller-refactor-progress.md#L122-L138](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L122-L138) (`clm_57a96008aceb4f0cb8e22c19e62fce375b2aed703084d11bcfb9bb54000a437a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] An embedded all-in-one image bundles Higress, Tuwunel, MinIO, Element Web, the controller, CLI, and kube-apiserver, started in layers via supervisord; deployment is dual-container (controller container plus an auto-created manager-agent container created via DockerBackend). -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L169-L177](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L169-L177) (`clm_f894b5256aca07f47e53efd559589e098761386a79069f96291c384af67aeaa5`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] Per the internal progress doc, ConfigVersionManager, versions.json management, skill hot-update (UpgradeSkills), runtime rolling upgrade, agt config push, debug commands, apply --prune, and all Phase 4 debug/upgrade capabilities are unimplemented. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L198-L198](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L198-L198), [docs/design/internal/agentteams-controller-refactor-progress.md#L70-L76](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L70-L76), [docs/design/internal/agentteams-controller-refactor-progress.md#L200-L211](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L200-L211), [docs/design/internal/agentteams-controller-refactor-progress.md#L122-L138](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L122-L138) (`clm_2fcb2767dcd69536896f4d6f3873c56736be3e76f8268cbd7bd87683564d1c4a`)
- [observation/documented] The progress doc marks Phase 3 items partially done: Manager state.json-to-OSS migration and quota checks are unimplemented, and fine-grained CallerIdentity isolation beyond SA token authentication remains incomplete. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L183-L192](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L183-L192) (`clm_55a9e34017ba14a6aab899ad5923f1ac573f98603c29947b74c2e4f696e04e8a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

