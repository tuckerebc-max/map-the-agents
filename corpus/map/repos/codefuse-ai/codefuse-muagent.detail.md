# codefuse-ai/codefuse-muagent -- full detail

[Back to orientation](codefuse-muagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codefuse-ai/codefuse-muagent/ebc8c3fbc886969befb6be18d4f85787de29b086/f5bf97e1930924d2.json](../../../wiki/dossiers/codefuse-ai/codefuse-muagent/ebc8c3fbc886969befb6be18d4f85787de29b086/f5bf97e1930924d2.json)

## specifications (2 claim(s))

- [observation/documented] muAgent is described as an agent framework driven by LLM and an Eventic Knowledge Graph (EKG), combining MultiAgent, FunctionCall, and CodeInterpreter techniques. -- evidence: [README.md#L39-L45](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L39-L45) (`clm_5f4a08398c60c983cdfe1f5ef7ecb5d483caf7002c45cafebbd255fd38e7c70a`)
- [observation/documented] The project is licensed under Apache License 2.0, copyright 2023 Ant Group, with the standard AS-IS warranty disclaimer. -- evidence: [LICENSE.md#L7-L11](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/LICENSE.md#L7-L11), [LICENSE.md#L1-L5](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/LICENSE.md#L1-L5) (`clm_503306901b35a8598a94df709e1e6288825301dbdaea52abc3fb6e6b58447d39`)

## components (2 claim(s))

- [observation/documented] The KG schema includes Intention Nodes, Workflow Nodes, Tool Nodes, and Character Nodes; Tool Nodes aim to improve tool selection and parameter filling, and Character Nodes support human-involved processes. -- evidence: [README.md#L91-L96](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L91-L96) (`clm_0957292716fbfa0ed79f9df4a5384a34861addb1603ce3c3d9353ac9adf2ff83`)
- [observation/documented] Advertised feature areas include an EKG Builder with intelligent parsing and one-click import of documents, EKG Reasoning under human guidance, and a Diagnose mode with visual debugging and end-to-end monitoring. -- evidence: [README.md#L91-L96](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L91-L96) (`clm_86380261be28427864dcfead536753d3f9681a021ce37bfb6223d73418c92a26`)

## design-choices (1 claim(s))

- [observation/documented] The framework advertises four core differentiating capabilities: Complex Reasoning, Online Collaboration, Human Interaction, and Knowledge On-demand. -- evidence: [README.md#L39-L45](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L39-L45) (`clm_8c8ab0c9e300d9e9bee06e9c3231f2fd7e26459c10d13e39c4807fab79279994`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are invited to give feedback via GitHub Issues and can contribute through code implementation, test development, and documentation, per an external Contribution Guide. -- evidence: [README.md#L104-L104](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L104-L104), [README.md#L102-L102](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L102-L102) (`clm_e69eb5138cbcd5ed9570d3ef0e7d885a9f89f5273f2e780e65338f03bcba56db`)
- [observation/documented] Repository development practice: the quickstart deploys EKG services by cloning the repo, creating a docker network named ekg-net, and running docker compose up -d, then opening localhost:8000. -- evidence: [README.md#L67-L68](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L67-L68), [README.md#L63-L63](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L63-L63), [README.md#L57-L57](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L57-L57) (`clm_e07466a51a794676dddf1105fcc23c890c309e9fff8b42b86495d68c9490eb3d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Users orchestrate agents through canvas-based drag-and-drop and simple text writing, with the LLM executing complex SOPs under human guidance. -- evidence: [README.md#L39-L45](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L39-L45) (`clm_0c88f05352da0628a8535e95eb6b0ff4a79e2a7ef7ecfb951825ef8b1d555a59`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] An SDK is published as the pip package codefuse-muagent; muAgent-sdk v0.1.0 shipped with muAgent v2.2 and supports ekg-sdk with parallel EKG execution. -- evidence: [README.md#L18-L21](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L18-L21), [README.md#L83-L85](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L83-L85) (`clm_4ed11632c1dc349169eff0848063d0b639e469a4f5c2f7ba29f606cf53f58311`)
- [observation/documented] Prebuilt muAgent-related Docker images (beta) are available at the codefuse-ai/packages GitHub org, downloadable via a provided docker_pull_images.sh script. -- evidence: [README.md#L74-L74](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L74-L74) (`clm_14620e2545345a189f364c4f3533eccb205e8397bda40d9ed5588dd97d8ed7e7`)

## limitations (1 claim(s))

- [observation/documented] LEGAL.md states that Chinese code comments are the governing version and comments in other languages are reference only, with Chinese prevailing in conflicts. -- evidence: [LEGAL.md#L3-L3](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/LEGAL.md#L3-L3) (`clm_99a531958c566ad767853f787373570ca715a55ecc098e1040d07b12c594d02b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

