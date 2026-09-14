# agentscope-ai/agentteams

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f65d6e1af268 @ 00898cd68a276fb4

## Summary (orientation draft, not independently verified)

The snapshot documents an AgentTeams Kubernetes controller that creates agent Pods (with a ConfigMap-driven PodTemplateSpec overlay), a WorkerBackend abstraction with Docker/K8s backends, an agt CLI REST client, Helm chart and CRDs, and embedded/incluster deployment modes; an internal progress doc also tracks unimplemented features. Evidence coverage: 141 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 12 of 54 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The controller creates one Kubernetes Pod per Manager and Worker; by default each Pod has a single 'worker' container, a projected agentteams-token volume, and the controller-managed ServiceAccount. -- evidence: [docs/design/agent-pod-template.md#L3-L6](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L3-L6)
  - [observation/documented] A WorkerBackend abstraction layer unifies worker lifecycle management; the progress doc marks the interface, Docker backend, Kubernetes backend, and backend auto-selection as complete, and lists additional SAE, APIG gateway, gateway abstraction, and cloud-credential files as implemented beyond the design. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L47-L52](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L47-L52), [docs/design/internal/agentteams-controller-refactor-progress.md#L38-L43](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L38-L43)
- design-choices (5 claim(s)):
  - [observation/documented] The pod template ConfigMap is read fresh on each Pod creation with no caching: edits affect the next created Pod while existing Pods are untouched; a missing, malformed, or unfetchable ConfigMap falls back to the default Pod shape without blocking creation. -- evidence: [docs/design/agent-pod-template.md#L34-L36](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L34-L36), [docs/design/agent-pod-template.md#L30-L32](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L30-L32)
  - [observation/documented] Merge semantics are field-specific: the template wins for nodeSelector, tolerations, affinity, securityContext, and non-worker sidecar containers; the controller wins for ownerReferences, serviceAccountName, forced automountServiceAccountToken=false, and the agent container's image/env; labels and annotations merge with controller values overwriting on key collision. -- evidence: [docs/design/agent-pod-template.md#L83-L86](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L83-L86), [docs/design/agent-pod-template.md#L69-L79](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L69-L79), [docs/design/agent-pod-template.md#L90-L97](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L90-L97)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Cluster-specific Pod settings (sysctls, nodeSelectors, tolerations, imagePullSecrets, injector annotations) are injected via a corev1.PodTemplateSpec stored in a ConfigMap under the key pod-template.yaml, read on every Create call. -- evidence: [docs/design/agent-pod-template.md#L14-L19](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L14-L19), [docs/design/agent-pod-template.md#L8-L10](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/agent-pod-template.md#L8-L10)
  - [observation/documented] The agt CLI was rewritten as a pure REST API client calling the controller at AGENTTEAMS_CONTROLLER_URL (default http://localhost:8090), supporting CRUD for workers/teams/humans/managers, worker wake/sleep/status, YAML and ZIP apply, with tokens via AGENTTEAMS_AUTH_TOKEN or SA token file discovery. -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L120-L120](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L120-L120), [docs/design/internal/agentteams-controller-refactor-progress.md#L122-L138](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L122-L138)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] An embedded all-in-one image bundles Higress, Tuwunel, MinIO, Element Web, the controller, CLI, and kube-apiserver, started in layers via supervisord; deployment is dual-container (controller container plus an auto-created manager-agent container created via DockerBackend). -- evidence: [docs/design/internal/agentteams-controller-refactor-progress.md#L169-L177](https://github.com/agentscope-ai/AgentTeams/blob/f65d6e1af268039507b413e3c16679bb84d21ac7/docs/design/internal/agentteams-controller-refactor-progress.md#L169-L177)
More evidence: [full detail](agentteams.detail.md)

Metadata and full claim list: [full detail](agentteams.detail.md)
Human notes ([notes](agentteams.notes.md), never overwritten by build)

[Back to map index](../../index.md)
