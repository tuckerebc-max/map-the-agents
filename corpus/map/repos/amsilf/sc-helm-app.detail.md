# amsilf/sc-helm-app -- full detail

[Back to orientation](sc-helm-app.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/amsilf/sc-helm-app/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/2404526c351a141d.json](../../../wiki/dossiers/amsilf/sc-helm-app/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/2404526c351a141d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The repo includes a Helm chart under helm/ that deploys a simple Nginx server serving a Hello World page. -- evidence: [README.md#L14-L14](https://github.com/amsilf/sc-helm-app/blob/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/README.md#L14-L14) (`clm_2756b025cc88bdbe5cd1e146e0e404e9085ebb27406fd3cd204ef3aa08241586`)
- [observation/documented] OPA policies in the opa/ directory verify the Helm chart against predefined rules. -- evidence: [README.md#L17-L17](https://github.com/amsilf/sc-helm-app/blob/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/README.md#L17-L17) (`clm_35a234b8ddd65193d2b2748350f2cad2e89ed599f9bb257cf8558509ff2f420b`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [inference/documented] The ChatGPT fix mechanism appears to rely on the OpenAI API, since an OpenAI API key is listed as a prerequisite for that integration. -- evidence: [README.md#L7-L10](https://github.com/amsilf/sc-helm-app/blob/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/README.md#L7-L10), [README.md#L21-L25](https://github.com/amsilf/sc-helm-app/blob/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/README.md#L21-L25) (`clm_4e00b2400117359d2a54423b3f68f9e898d3157a5cc91af96020ade52dcb6327`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A verification script detects OPA policy violations, uses ChatGPT to suggest fixes, applies them, creates a new branch, pushes it, and opens a pull request. -- evidence: [README.md#L21-L25](https://github.com/amsilf/sc-helm-app/blob/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/README.md#L21-L25) (`clm_0538a75c7e28daf97f53c0890e1324cefbffafb99d8cd5b91d4276550e32cb76`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites listed are Helm 3+, OPA, Python 3+, and an OpenAI API key for the ChatGPT integration. -- evidence: [README.md#L7-L10](https://github.com/amsilf/sc-helm-app/blob/3006ac63cae4b46639fdfc3a1d4ec2b59b9d07bd/README.md#L7-L10) (`clm_728e5096fa13320e74535571de90b548d6d629c3c81bd10d3f69593660130aa3`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

