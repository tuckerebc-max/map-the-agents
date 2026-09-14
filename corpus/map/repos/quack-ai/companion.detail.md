# quack-ai/companion -- full detail

[Back to orientation](companion.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/quack-ai/companion/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/30c955454afab93a.json](../../../wiki/dossiers/quack-ai/companion/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/30c955454afab93a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A deployment includes a backend API on port 5050, an APM dashboard on port 3000, and a Gradio chat interface on port 7860. -- evidence: [README.md#L105-L108](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L105-L108) (`clm_d0c2a2898f9f9ef3d08827e52a68b8953193e960ded1b6d40c0186ff94f60961`)

## design-choices (2 claim(s))

- [observation/documented] The community edition lets users choose their own locally-run open-source models; recommended options include Deepseek Coder 6.7B, Gemma 7b, and Dolphin Mistral 7b. -- evidence: [docs/community/faq.mdx#L35-L39](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/community/faq.mdx#L35-L39) (`clm_dd64fc060e3d56266bf5a6177c8de4845c82d069cec515b103c81fceaa50123a`)
- [observation/documented] The database schema defines users with an access-type enum of user/admin, repositories keyed by provider repo id, and guidelines with content, creator, and timestamps. -- evidence: [docs/dbdiagram.txt#L29-L38](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L29-L38), [docs/dbdiagram.txt#L2-L5](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L2-L5), [docs/dbdiagram.txt#L19-L27](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L19-L27), [docs/dbdiagram.txt#L7-L17](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L7-L17) (`clm_0e3a016b1349fb661a4c0363bce2456acc990b786e32e0fdb8b74480f99c0445`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: docs contributors install the Mintlify CLI globally and run 'mintlify dev' in the folder containing mint.json to preview changes locally. -- evidence: [docs/README.md#L44-L44](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L44-L44), [docs/README.md#L38-L38](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L38-L38), [docs/README.md#L46-L48](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L46-L48), [docs/README.md#L58-L59](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L58-L59), [docs/README.md#L40-L42](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L40-L42) (`clm_f192e86daf0e6ef7398a3457fb27e3d7f8d865b4e154e389b01f9c77c126c970`)
- [observation/documented] Repository development practice: docs changes deploy to production automatically on push to the default branch, and pull requests generate preview links. -- evidence: [docs/README.md#L52-L52](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L52-L52), [docs/README.md#L54-L54](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L54-L54) (`clm_1b6dc6061f77c2bf20fd6b580f0959a4b8dc19abef8b668e8e302da4f15f4dda`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a REST API for guideline management and LLM inference, browsable via Swagger docs at localhost:5050/docs or through HTTP requests. -- evidence: [README.md#L65-L65](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L65-L65), [README.md#L67-L67](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L67-L67) (`clm_0a7b2c2a1c47d5470773e1fc2e962cdb5331c1dfa017704324a31ac9c8bb8e4d`)
- [observation/documented] A code chat endpoint is offered as a coding-specific LLM chat, with the backend API acting as gatekeeper for an Ollama-powered inference container. -- evidence: [README.md#L59-L59](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L59-L59) (`clm_4530cec3cddd4e68c27607137f5dd083f721264c868049af5ec0433fce43a2da`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] API requests authenticate with a token header of the form 'Authorization: Token <team_token>', and the docs include a Permissions section (placeholder body). -- evidence: [docs/api-reference/authentication.mdx#L8-L10](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/api-reference/authentication.mdx#L8-L10), [docs/api-reference/authentication.mdx#L20-L20](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/api-reference/authentication.mdx#L20-L20) (`clm_9423a92692f4411fd14f2cb3539111b32f0262ae37858bdfdf133e7733796527`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running the service requires Git, Docker, Docker Compose, and the NVIDIA Container Toolkit with a GPU of at least 6 GB VRAM for good latency. -- evidence: [README.md#L74-L77](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L74-L77) (`clm_7cb942447a13189d9f297255c689e772652df493ae1b9c3acd8a1c542e9094a5`)

## limitations (2 claim(s))

- [observation/documented] IDE support currently covers VSCode only, with other development environments planned gradually; the best-supported languages so far are Python and JavaScript/TypeScript. -- evidence: [docs/community/faq.mdx#L27-L29](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/community/faq.mdx#L27-L29), [docs/community/faq.mdx#L31-L33](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/community/faq.mdx#L31-L33) (`clm_ffeca12d02198a8f54567589c2e7b13e84e4f40f8ee2ef663145bc5a4f04d09a`)
- [observation/documented] The product is described as being in beta; code autocompletion that is guideline-aware is listed as coming soon rather than shipped. -- evidence: [docs/community/roadmap.mdx#L36-L38](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/community/roadmap.mdx#L36-L38), [docs/community/roadmap.mdx#L7-L8](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/community/roadmap.mdx#L7-L8) (`clm_613077cf9c3bcffc14243ff8a6f92bd761975cf23fcf12c8b60ddd222450c239`)

## relevance (1 claim(s))

- [observation/documented] Quack Companion targets software teams, acting like an onboarded team member with knowledge of internal libraries and coding standards, and is positioned against GitHub Copilot with team-guideline context. -- evidence: [docs/community/faq.mdx#L41-L44](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/community/faq.mdx#L41-L44), [README.md#L50-L50](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L50-L50) (`clm_9defe6bf36c82621edfc5fea7eca0ad5ea4085b320ae4fea1315123ad36f3b82`)

