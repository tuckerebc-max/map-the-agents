# codefuse-ai/codefuse-muagent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ebc8c3fbc886 @ f5bf97e1930924d2

## Summary (orientation draft, not independently verified)

The snapshot contains only README, LEGAL, and LICENSE content for muAgent, an LLM+Eventic-Knowledge-Graph agent framework by Ant Group. Evidence covers the framework's advertised capabilities, deployment/SDK instructions, licensing, and contribution guidance; no source code is present.

## Source coverage

Source coverage (partial): 3 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] muAgent is described as an agent framework driven by LLM and an Eventic Knowledge Graph (EKG), combining MultiAgent, FunctionCall, and CodeInterpreter techniques. -- evidence: [README.md#L39-L45](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L39-L45)
  - [observation/documented] The project is licensed under Apache License 2.0, copyright 2023 Ant Group, with the standard AS-IS warranty disclaimer. -- evidence: [LICENSE.md#L7-L11](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/LICENSE.md#L7-L11), [LICENSE.md#L1-L5](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/LICENSE.md#L1-L5)
- components (2 claim(s)):
  - [observation/documented] The KG schema includes Intention Nodes, Workflow Nodes, Tool Nodes, and Character Nodes; Tool Nodes aim to improve tool selection and parameter filling, and Character Nodes support human-involved processes. -- evidence: [README.md#L91-L96](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L91-L96)
  - [observation/documented] Advertised feature areas include an EKG Builder with intelligent parsing and one-click import of documents, EKG Reasoning under human guidance, and a Diagnose mode with visual debugging and end-to-end monitoring. -- evidence: [README.md#L91-L96](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L91-L96)
- design-choices (1 claim(s)):
  - [observation/documented] The framework advertises four core differentiating capabilities: Complex Reasoning, Online Collaboration, Human Interaction, and Knowledge On-demand. -- evidence: [README.md#L39-L45](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L39-L45)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are invited to give feedback via GitHub Issues and can contribute through code implementation, test development, and documentation, per an external Contribution Guide. -- evidence: [README.md#L104-L104](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L104-L104), [README.md#L102-L102](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L102-L102)
  - [observation/documented] Repository development practice: the quickstart deploys EKG services by cloning the repo, creating a docker network named ekg-net, and running docker compose up -d, then opening localhost:8000. -- evidence: [README.md#L67-L68](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L67-L68), [README.md#L63-L63](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L63-L63), [README.md#L57-L57](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L57-L57)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Users orchestrate agents through canvas-based drag-and-drop and simple text writing, with the LLM executing complex SOPs under human guidance. -- evidence: [README.md#L39-L45](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L39-L45)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] An SDK is published as the pip package codefuse-muagent; muAgent-sdk v0.1.0 shipped with muAgent v2.2 and supports ekg-sdk with parallel EKG execution. -- evidence: [README.md#L18-L21](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L18-L21), [README.md#L83-L85](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L83-L85)
  - [observation/documented] Prebuilt muAgent-related Docker images (beta) are available at the codefuse-ai/packages GitHub org, downloadable via a provided docker_pull_images.sh script. -- evidence: [README.md#L74-L74](https://github.com/codefuse-ai/CodeFuse-muAgent/blob/ebc8c3fbc886969befb6be18d4f85787de29b086/README.md#L74-L74)
- limitations (1 claim(s)):
More evidence: [full detail](codefuse-muagent.detail.md)

Metadata and full claim list: [full detail](codefuse-muagent.detail.md)
Human notes ([notes](codefuse-muagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
