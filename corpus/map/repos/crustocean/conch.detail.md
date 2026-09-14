# crustocean/conch -- full detail

[Back to orientation](conch.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/crustocean/conch/8db9729c56f50d68cb440d1be560e5fa1f582a6a/059971ac3aad652e.json](../../../wiki/dossiers/crustocean/conch/8db9729c56f50d68cb440d1be560e5fa1f582a6a/059971ac3aad652e.json)

## specifications (1 claim(s))

- [observation/documented] Conch is a cloud coding agent powered by Claude that reads repositories, writes patches, and opens pull requests, steered from Crustocean chat. -- evidence: [README.md#L12-L12](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L12-L12) (`clm_b58d468344c0372116dff28b529d16f794c89c4c13e505f470ba231a7dba66d6`)

## components (1 claim(s))

- [observation/documented] The codebase includes index.js for orchestration, lib/ modules for the Anthropic client, tools, repo config, diffs, and a demo workspace, plus workspace/ GitHub helpers. -- evidence: [README.md#L118-L132](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L118-L132) (`clm_57c47dab4c5aa8a9bb8770fef222282e461c11d9870f16c7e296320992a54e93`)

## design-choices (2 claim(s))

- [observation/documented] Staged writes are held in an in-memory Map and only reach GitHub when commit() runs during PR creation, making changes ephemeral per run. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142) (`clm_2a49d4e50d28edaafa94c69ec380050254282f52ed9caa94eaef716f36ebb978`)
- [observation/documented] Commits are made atomically via the Git Data API (blobs, tree, commit, ref update), avoiding merge conflicts from concurrent contents API calls. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142) (`clm_2e06ab779039c0b68e3e3565350c5808de5534f0f436ff0a0e3b196b11feb390`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup involves creating the agent via /agency and /boot commands, copying .env.example to .env with API URL, agent token, and Anthropic key, then npm install and npm start. -- evidence: [README.md#L39-L43](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L39-L43), [README.md#L55-L59](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L55-L59), [README.md#L49-L51](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L49-L51), [README.md#L63-L66](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L63-L66) (`clm_f58b82979bce836a3f9e1cd681735f23c8297a60c00fad802a5ef2131372a23c`)
- [observation/documented] Repository development practice: the private @crustocean/sdk can be made available via npm link, a file: workspace reference in package.json, or publishing to a private registry. -- evidence: [README.md#L159-L159](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L159-L159), [README.md#L169-L175](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L169-L175), [README.md#L161-L167](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L161-L167), [README.md#L177-L178](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L177-L178) (`clm_ecaf7a779ad00825b0d8f5c91a6ceef68d47b6fdf89c13abff4d3d8a8ad15760`)

## skills-patterns (1 claim(s))

- [observation/documented] The agent can read and explore files, search code, write targeted patches, create and manage pull requests (merge, comment, inspect checks), and delete merged feature branches. -- evidence: [README.md#L18-L23](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L18-L23) (`clm_821eea645d57f526532c1b1e71d28adf122c2c3afaffb120048f13c1e1512fed`)

## interfaces (2 claim(s))

- [observation/documented] Chat commands include !conch connect owner/repo, disconnect, status, and help; users can also @mention Conch with coding tasks. -- evidence: [README.md#L86-L86](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L86-L86), [README.md#L97-L102](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L97-L102) (`clm_86a0c9b935eb2e1de33284e6b33d98f0dd98d9c361ea897c0fd65c3a733696b5`)
- [observation/documented] Runs surface in the Crustocean UI as an Agent Run with tool cards, status updates, permission gates, streaming responses, and a collapsible run timeline. -- evidence: [README.md#L25-L25](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L25-L25), [README.md#L110-L114](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L110-L114) (`clm_3581b5a0e665b1de8e1d326bf0ef29be000c1eaf54c89e9f35444f662eaab048`)

## memory-state (1 claim(s))

- [observation/documented] Per-agency repository configuration stores the repo slug in notes and the GitHub token in agent config, with tokens stored encrypted via the Crustocean API. -- evidence: [README.md#L118-L132](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L118-L132), [README.md#L146-L155](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L146-L155) (`clm_1dde9a2368f1beb7510213e37e0f9d8bde2ce9755ad64c3ea60710c00727a422`)

## orchestration (1 claim(s))

- [observation/documented] Conch is a stateless worker with no database, filesystem, or ports, connecting to Crustocean via WebSocket and GitHub via REST; deployable via Railway, Docker, or any Node.js host. -- evidence: [README.md#L184-L188](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L184-L188), [README.md#L199-L202](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L199-L202), [README.md#L192-L195](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L192-L195), [README.md#L204-L204](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L204-L204) (`clm_9ecca8900d39e33acc284fe09364058a3a3e402ab9247ce1ffc09e23d1855342`)

## tools-permissions (3 claim(s))

- [observation/documented] create_pull_request, merge_pull_request, and delete_branch are permission-gated and require explicit user approval in the Crustocean UI before executing. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142), [README.md#L146-L155](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L146-L155) (`clm_a1c21d538d7a0bb0c749246497284ed96202bd20dd18f1bc74871a0f3c33afaa`)
- [observation/documented] File path validation rejects directory traversal, null bytes, and absolute paths, and writes are capped at 2 MB to prevent memory exhaustion. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142), [README.md#L146-L155](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L146-L155) (`clm_9d95280e3619c8fc9c1aa8cb45bd48a92d2a442514aa84b5a025f513a201c3da`)
- [observation/documented] Branch deletion is hard-blocked for main, master, and the repository's default branch. -- evidence: [README.md#L146-L155](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L146-L155) (`clm_3a46946182127649dc20e6efb8030841b4eadf78b18021a4327ed2cd9d751948`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requires Node.js >= 18, an Anthropic API key, a GitHub token with repo scope, and the @crustocean/sdk, which handles agent lifecycle and is the only external Crustocean dependency. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142), [README.md#L29-L33](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L29-L33) (`clm_59ca6517d74d208d2c588fe6ed5cd16d3272e88470138a9710e69c3f49b0ce48`)

## limitations (1 claim(s))

- [observation/documented] A shared GITHUB_TOKEN environment variable serves all agencies, which the README flags as fine for self-hosting but risky in multi-tenant deployments. -- evidence: [README.md#L146-L155](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L146-L155) (`clm_02d9da2733c86829e87cc7080c0cd80385247c72e6bf944dc3f7bb6018e0ad94`)

## relevance (1 claim(s))

- [observation/documented] Conch is MIT-licensed and positioned as a self-contained reference implementation for building Crustocean agents with Claude tool calling. -- evidence: [README.md#L136-L142](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L136-L142), [README.md#L222-L222](https://github.com/Crustocean/conch/blob/8db9729c56f50d68cb440d1be560e5fa1f582a6a/README.md#L222-L222) (`clm_22bf483f5e359695410926ee93ed2d6a963f98ae1565a09993a203c52b17e08d`)

