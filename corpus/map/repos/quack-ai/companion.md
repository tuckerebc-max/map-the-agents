# quack-ai/companion

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ce9a10ac7924 @ 30c955454afab93a

## Summary (orientation draft, not independently verified)

Evidence covers Quack Companion's documentation and README: a self-hostable REST API for guideline management and LLM inference backed by Ollama, with a VSCode extension, Gradio chat UI, and Docker-based deployment. Much of the docs content is placeholder text, so several facets remain unsupported.

## Source coverage

Source coverage (partial): 6 of 28 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A deployment includes a backend API on port 5050, an APM dashboard on port 3000, and a Gradio chat interface on port 7860. -- evidence: [README.md#L105-L108](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L105-L108)
- design-choices (2 claim(s)):
  - [observation/documented] The community edition lets users choose their own locally-run open-source models; recommended options include Deepseek Coder 6.7B, Gemma 7b, and Dolphin Mistral 7b. -- evidence: [docs/community/faq.mdx#L35-L39](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/community/faq.mdx#L35-L39)
  - [observation/documented] The database schema defines users with an access-type enum of user/admin, repositories keyed by provider repo id, and guidelines with content, creator, and timestamps. -- evidence: [docs/dbdiagram.txt#L29-L38](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L29-L38), [docs/dbdiagram.txt#L2-L5](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L2-L5), [docs/dbdiagram.txt#L19-L27](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L19-L27), [docs/dbdiagram.txt#L7-L17](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/dbdiagram.txt#L7-L17)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: docs contributors install the Mintlify CLI globally and run 'mintlify dev' in the folder containing mint.json to preview changes locally. -- evidence: [docs/README.md#L44-L44](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L44-L44), [docs/README.md#L38-L38](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L38-L38), [docs/README.md#L46-L48](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L46-L48), [docs/README.md#L58-L59](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L58-L59), [docs/README.md#L40-L42](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L40-L42)
  - [observation/documented] Repository development practice: docs changes deploy to production automatically on push to the default branch, and pull requests generate preview links. -- evidence: [docs/README.md#L52-L52](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L52-L52), [docs/README.md#L54-L54](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/README.md#L54-L54)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a REST API for guideline management and LLM inference, browsable via Swagger docs at localhost:5050/docs or through HTTP requests. -- evidence: [README.md#L65-L65](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L65-L65), [README.md#L67-L67](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L67-L67)
  - [observation/documented] A code chat endpoint is offered as a coding-specific LLM chat, with the backend API acting as gatekeeper for an Ollama-powered inference container. -- evidence: [README.md#L59-L59](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L59-L59)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] API requests authenticate with a token header of the form 'Authorization: Token <team_token>', and the docs include a Permissions section (placeholder body). -- evidence: [docs/api-reference/authentication.mdx#L8-L10](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/api-reference/authentication.mdx#L8-L10), [docs/api-reference/authentication.mdx#L20-L20](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/docs/api-reference/authentication.mdx#L20-L20)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Running the service requires Git, Docker, Docker Compose, and the NVIDIA Container Toolkit with a GPU of at least 6 GB VRAM for good latency. -- evidence: [README.md#L74-L77](https://github.com/quack-ai/companion/blob/ce9a10ac7924aea41c9e2f23a6d92b9bd6ef8131/README.md#L74-L77)
- limitations (2 claim(s)):
More evidence: [full detail](companion.detail.md)

Metadata and full claim list: [full detail](companion.detail.md)
Human notes ([notes](companion.notes.md), never overwritten by build)

[Back to map index](../../index.md)
