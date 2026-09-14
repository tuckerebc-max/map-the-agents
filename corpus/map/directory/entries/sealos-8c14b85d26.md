# sealos (`sealos`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: labring
- License: Sealos Sustainable Use License (custom, not OSI-approved)
- Language: Go
- Interface: install=docker
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [labring/sealos](../../repos/labring/sealos.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-native Cloud Operating System built on Kubernetes that unifies the entire application lifecycle — from cloud IDE development (DevBox) to production deployment, managed databases, and app store-style one-click deployments — without requiring Kubernetes expertise.

(captured site page body (agents/sealos.md), not a verified repo-code finding)
Sealos compresses the platform-engineering stack into one Kubernetes-based system: developers get DevBox cloud IDEs (with Cursor and VS Code connectivity), push Docker images through an App Launchpad, attach managed databases, and distribute software through a built-in app store, all without hand-writing Kubernetes YAML. The makers (labring, the FastGPT team) market it as AI-native infrastructure — deploy from GitHub or an AI coding agent, then operate with AI-assisted operations — which is how it intersects this census: it is where agent-built applications land, not the agent. Internally it is Go controllers over kubeadm-based clusters with Buildah-based cluster images, fronted by a React console. The custom Sustainable Use License permits internal and non-commercial use but forbids reselling it as a cloud service. It is widely deployed (18k+ stars) for self-hosted PaaS and AI application hosting.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sealos.md)
