# benc-uk/workflow-dispatch -- full detail

[Back to orientation](workflow-dispatch.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/benc-uk/workflow-dispatch/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/3eb4093669280522.json](../../../wiki/dossiers/benc-uk/workflow-dispatch/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/3eb4093669280522.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The intended use case is chaining workflows, e.g. a CI build workflow triggering a CD deploy workflow, allowing separate CI/CD workflows that pass data between them. -- evidence: [README.md#L6-L6](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L6-L6) (`clm_5bbd03c504971e64a0da710c8c58a9c6d8e8320a7659ad3a7d5b73d32a855510`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (9 claim(s))

- [observation/documented] The action triggers another GitHub Actions workflow using the workflow_dispatch event, and the target workflow must be configured for that event type. -- evidence: [README.md#L3-L4](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L3-L4) (`clm_77f1a4d8c9666b80d9e4d84fb2a3baf5204b83111a73acbd9289fd8974ad67ca`)
- [observation/documented] The required `workflow` input accepts the target workflow's name, filename, or ID, and all three forms are used when looking up the workflow. -- evidence: [README.md#L24-L24](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L24-L24) (`clm_ab9bbaa57f9fdc21277935e768b48616af8930bf3bad777aedb0f5f6ebaf8775`)
- [observation/documented] An optional `inputs` parameter passes inputs to the target workflow as a JSON-encoded string, for workflows that have inputs configured. -- evidence: [README.md#L38-L38](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L38-L38) (`clm_b55009ba4a706844940229229c032d80b0989f470803fd1c81cefd419a991c84`)
- [observation/documented] An optional `ref` input sets the Git reference (branch, tag, or commit SHA) for the triggered run; if omitted, the triggering workflow's context ref is used. -- evidence: [README.md#L42-L42](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L42-L42) (`clm_62efcea2197d2796fcf407626b6f50ab4c95abb4309c2db4d9e01d809d639b27`)
- [observation/documented] By default workflows are triggered in the same repo; an optional `repo` input (owner/name) enables triggering in another repository. -- evidence: [README.md#L46-L46](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L46-L46) (`clm_48fc76b459966a6b51a16048da35f820d62c5fa90a0a2b2b580f9bc45fa3f609`)
- [observation/documented] Setting `wait-for-completion` to true makes the action poll the triggered run's status every 5 seconds until it finishes, with the interval configurable via `wait-interval-seconds`. -- evidence: [README.md#L61-L61](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L61-L61), [README.md#L69-L69](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L69-L69) (`clm_b58084cd291ef269914f25524263ce4321732e65c35c792fa5f8c82c090e3d85`)
- [observation/documented] The `wait-timeout-seconds` input caps waiting at a default of 900 seconds (15 minutes), applying only when wait-for-completion is enabled. -- evidence: [README.md#L65-L65](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L65-L65) (`clm_773d0a99079f5de9e41aed1cc476e26f8554f2e13e70175d6d2a040195f6cb78`)
- [observation/documented] With `sync-status` set to true, the action fails if the triggered workflow run fails or is cancelled; this requires wait-for-completion to be enabled. -- evidence: [README.md#L73-L73](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L73-L73) (`clm_ea7812eac26aae256d286a7384eef75f0576b16ea50b6b05f4d3a5bc15dab073`)
- [observation/documented] The action exposes outputs runId, runUrl, runUrlHtml, and workflowId describing the triggered workflow run. -- evidence: [README.md#L77-L82](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L77-L82) (`clm_0a7d63090279ac57cd4493643c215917db4a2cc29d1232db5557ffbfab7960b5`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] By default the standard GITHUB_TOKEN is used, so users no longer need to supply their own token; cross-repo dispatch requires a PAT with repo rights passed via a secret. -- evidence: [README.md#L55-L55](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L55-L55), [README.md#L53-L53](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L53-L53) (`clm_e82c34f2e54f92acd6b43e9d545f4a28b3a67c9fd93d8a2f2a18b0d8d5b3a505`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] Workflows triggered by this action appear in the GitHub UI as "manually triggered", since the action simulates the manual workflow_dispatch trigger. -- evidence: [README.md#L14-L14](https://github.com/benc-uk/workflow-dispatch/blob/78e99d70d9acaa4e2c98fe781b3cabda5df0228e/README.md#L14-L14) (`clm_55e60e31c082f76692d9e1716ad43c506b219855fc5f1cc1cf1f5a48c655fdb5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

