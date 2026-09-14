# codefox-lab/codefox-cli -- full detail

[Back to orientation](codefox-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codefox-lab/codefox-cli/7b5f855fb6b5fb6d842327a40702d785aa379fb4/33c5a99fd2de433d.json](../../../wiki/dossiers/codefox-lab/codefox-cli/7b5f855fb6b5fb6d842327a40702d785aa379fb4/33c5a99fd2de433d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] RAG-based context retrieval is configurable: chunk size, overlap, max RAG characters, embedding batch size, and lazy loading, with fastembed embedding defaulting to BAAI/bge-small-en-v1.5. -- evidence: [WIKI.md#L194-L209](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L194-L209), [WIKI.md#L177-L177](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L177-L177), [WIKI.md#L175-L175](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L175-L175) (`clm_f94f33ccd8cd547116554f21493e51889dbddd8d125e76d37f2cf78aba797c3c`)

## design-choices (4 claim(s))

- [observation/documented] The tool is positioned as a CLI-first diff review tool, explicitly not an IDE coding assistant like Cursor or Claude Code. -- evidence: [README.md#L63-L63](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L63-L63), [README.md#L65-L66](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L65-L66) (`clm_4b41872cc74b3cdd194e465d7060119be7b71b40fb127436a0d7f3491c499b46`)
- [observation/documented] Supported providers are Gemini (default), Ollama for local/remote servers, and OpenRouter; Ollama allows fully local reviews. -- evidence: [README.md#L83-L85](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L83-L85), [README.md#L33-L35](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L33-L35), [WIKI.md#L47-L49](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L47-L49), [WIKI.md#L53-L57](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L53-L57) (`clm_bddcabe4e1e06c7aa3522a1051b41015d54d265af12f37239c4b6539661b75a0`)
- [observation/documented] Analysis rule categories cover security (vulnerabilities, secret leaks), performance, and style, toggleable in the ruler config section. -- evidence: [WIKI.md#L351-L353](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L351-L353), [WIKI.md#L361-L363](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L361-L363), [WIKI.md#L371-L373](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L371-L373), [WIKI.md#L343-L343](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L343-L343), [WIKI.md#L336-L341](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L336-L341) (`clm_85429c59af7c20ec475ff145d3a4b3d1507942d7120fa382cf5d5aeca9af38b7`)
- [observation/documented] The system prompt can be fully overridden via prompt.system, and prompt options include hard_mode, short_mode, and strict_facts. -- evidence: [WIKI.md#L396-L396](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L396-L396), [WIKI.md#L381-L388](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L381-L388) (`clm_e31ee75fc39008345d739c17892878e761989d34c69e1a7fcea72c8c6e33cbdf`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: dev setup installs pytest, mypy, ruff, and types-PyYAML; tests run with 'pytest tests -v', linting via ruff, and type checking via mypy codefox. -- evidence: [README.md#L240-L243](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L240-L243), [README.md#L247-L249](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L247-L249), [README.md#L219-L219](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L219-L219), [requirements-dev.txt#L3-L8](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/requirements-dev.txt#L3-L8), [README.md#L234-L236](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L234-L236) (`clm_3dcb2265348d48aaf20cbf42c0fb80205c81b2a3ee22178192f6e88bb2d40b76`)
- [observation/documented] Repository development practice: bug reports, pull requests, and documentation improvements are welcome, and a Contributor Covenant-based code of conduct governs the community. -- evidence: [CODE_OF_CONDUCT.md#L117-L119](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/CODE_OF_CONDUCT.md#L117-L119), [README.md#L255-L255](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L255-L255) (`clm_283f95b00a318f8a9f87b30765e6882540ca3a7282fad85c164f2ffd5918e9c0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands: init, list, scan, version, clean, and --help, per the commands table. -- evidence: [README.md#L190-L197](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L190-L197) (`clm_b8c3c78c82174558adf84c5c709c2d993c95dd72a7d2405468359489cbdb016b`)
- [observation/documented] The scan command collects the current git diff, loads project context, sends a review request to the configured model, and returns review comments with optional fix suggestions. -- evidence: [README.md#L131-L131](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L131-L131), [README.md#L127-L127](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L127-L127), [README.md#L135-L135](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L135-L135), [README.md#L133-L133](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L133-L133), [README.md#L129-L129](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L129-L129), [README.md#L122-L125](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L122-L125) (`clm_aa3bd5cdb417dd33d5c20697b78fc9637600c52a86016c2acfcd80a9fc7b80fb`)
- [observation/documented] Configuration uses ./.codefox.yml for model and analysis settings, ./.codefoxignore for excluded paths, and ./codefoxenv for the API token. -- evidence: [README.md#L146-L147](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L146-L147), [README.md#L149-L151](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L149-L151), [README.md#L177-L178](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L177-L178) (`clm_790326232abb5c5523f567e39d219b0ffedeaff9b2676a35e131d2769129637a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Runtime dependencies include GitPython, google-genai, ollama, openai, qdrant-client, fastembed, typer, rich, PyGithub, and python-gitlab, per requirements.txt. -- evidence: [requirements.txt#L1-L19](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/requirements.txt#L1-L19) (`clm_8fb3619a89769159757b0e1ad3989462247e39e1cc54adb3ebc40c40d5aa95cd`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

