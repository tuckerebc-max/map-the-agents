# gensyn-ai/codeassist -- full detail

[Back to orientation](codeassist.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gensyn-ai/codeassist/3bf99c623173c07d86e7a9ac74a5aabee5abc103/0a81e310c0a13d4f.json](../../../wiki/dossiers/gensyn-ai/codeassist/3bf99c623173c07d86e7a9ac74a5aabee5abc103/0a81e310c0a13d4f.json)

## specifications (1 claim(s))

- [observation/documented] CodeAssist is described as a fully private, local AI coding assistant by Gensyn that helps users practice programming problems and train a personal assistant. -- evidence: [README.md#L6-L6](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L6-L6) (`clm_d91e5f2c9eb57bb50c57523f22435f0eb06cc58abd0f1f84d7e05704c0c2726f`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The assistant writes directly in the user's editor; every keystroke, edit, or deletion acts as a learning signal so it adapts to the user's habits over time. -- evidence: [README.md#L69-L69](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L69-L69), [README.md#L8-L8](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L8-L8) (`clm_3fd9ea0667807a7a4caec04b9f927c74d0b4f5e968c65b2b7f394bec7eca78d6`)

## workflows (3 claim(s))

- [observation/documented] Training is triggered by pressing Ctrl+C in the terminal; the system compares user edits to assistant actions, computes rewards and penalties, updates a local checkpoint, and stores weights under persistent-data/trainer/models. -- evidence: [README.md#L83-L88](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L83-L88), [README.md#L79-L79](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L79-L79) (`clm_273fa2ca809abaddb82e1688ee6d8ee3ec8003a89d602393f3b792a0014d3d4f`)
- [observation/documented] Episodes need not solve the problem successfully; users can stop recording by leaving the web UI and starting training with ctrl+c, and the trained model uploads to Hugging Face if a valid token exists. -- evidence: [README.md#L81-L81](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L81-L81), [README.md#L83-L88](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L83-L88) (`clm_efce536500807093090219eec8da40d6d864f1f2d597928ece7d8384c411ffc2`)
- [observation/documented] Repository development practice: contributors use a pre-commit hook for linting and ruff format; commits failing Ruff checks fail GitHub actions and must be fixed before merging. -- evidence: [README.md#L153-L153](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L153-L153), [README.md#L133-L133](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L133-L133) (`clm_81ffc565586c212c42fc7864a258e6e1dfc3de7417eb0bb16a0023d327195468`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product runs a web UI on localhost:3000 with email one-time-passcode or Google login, and credentials are stored in persistent-data/auth/userKeyMap.json. -- evidence: [README.md#L63-L63](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L63-L63), [README.md#L65-L65](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L65-L65) (`clm_05d034de3719a5ba616f909e520606defa633fb7690abce437bb3a873234c485`)
- [observation/documented] Users select Easy, Medium, or Hard problems from a sidebar, and the assistant can be paused via Shift+Space or a Pause button, with a 'No-Op' signaling the user's turn. -- evidence: [README.md#L73-L75](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L73-L75), [README.md#L67-L67](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L67-L67) (`clm_79b5722ed17d48039954d33dd9f7e389bc810d96b0357c17e687e49fff4a814e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The main script is run with 'uv run run.py', which handles the environment and launches the assistant; a --port argument can override the default port 3000. -- evidence: [README.md#L51-L51](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L51-L51), [README.md#L53-L55](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L53-L55), [README.md#L122-L125](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L122-L125), [README.md#L117-L120](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L117-L120) (`clm_de31052833cec99e4894c5ad6ae2d289970bda0682b056894965b14a684afd9b`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] The product's improvement loop is user-driven: README guidance suggests improvement becomes clearer after roughly 4-5 training episodes, implying no automated benchmark harness is documented. -- evidence: [README.md#L94-L98](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L94-L98) (`clm_88ad0ac9efb7579a7902a85a0172153b67651f0e5e24851b7840edfc58e826f9`)

## dependencies (1 claim(s))

- [observation/documented] Running CodeAssist requires Docker, Python no older than 3.10, and UV for dependency management, plus a HuggingFace token with Write access. -- evidence: [README.md#L26-L26](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L26-L26), [README.md#L59-L59](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L59-L59), [README.md#L18-L18](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L18-L18), [README.md#L22-L22](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L22-L22) (`clm_f1e6093d9ee077f5404a15d4319cdde8e2fd55c2d17b3b259cc383ba89a1f9c4`)

## limitations (2 claim(s))

- [observation/documented] The README notes that new CodeAssist participation on Testnet is no longer tracked as the team shifts focus to Mainnet, though historical data remains on-chain. -- evidence: [README.md#L4-L4](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L4-L4) (`clm_656c77976c11e92acad28941ae64ce09c72564c6c6a12f7f3de60cd5292f5b60`)
- [observation/documented] Documented troubleshooting covers unhealthy containers (viewable via docker logs), Docker daemon connection errors, and port 3000 conflicts, with ports 8000, 8080, 8001, 8008, 3003, and 11434 reserved for other services. -- evidence: [README.md#L113-L113](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L113-L113), [README.md#L104-L104](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L104-L104), [README.md#L122-L125](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L122-L125), [README.md#L117-L120](https://github.com/gensyn-ai/codeassist/blob/3bf99c623173c07d86e7a9ac74a5aabee5abc103/README.md#L117-L120) (`clm_a99fd65a56809281d9b4c2e26c4f312cc8de45cfdec263be91aba42342ef7472`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

