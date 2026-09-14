# kreneskyp/ix -- full detail

[Back to orientation](ix.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kreneskyp/ix/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/c9dbd6f0b700a064.json](../../../wiki/dossiers/kreneskyp/ix/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/c9dbd6f0b700a064.json)

## specifications (1 claim(s))

- [observation/documented] IX is described as a platform for designing and deploying autonomous and semi-autonomous LLM agents and workflows that can run in parallel and communicate with each other. -- evidence: [README.md#L31-L36](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L31-L36) (`clm_11771a83fd64612c8462414f77b531d486d54b8c7c1a7ad9a469a84af2d9e948`)

## components (2 claim(s))

- [observation/documented] IX implements a component config layer mapping LangChain components to a configuration graph, which dynamically renders nodes and forms in the no-code editor. -- evidence: [README.md#L84-L86](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L84-L86) (`clm_ed1a5d4ac8f6de2bd175cbc529086c3d4096479c133a803f95cf4269a83966fd`)
- [observation/documented] Custom chains include LLMToolChain, ParseJSON, IxSequence, MapSubchain, ToolChooser, LLMToolChooser, ChatModerator, and Planner v3 for planning and executing task sequences. -- evidence: [CHANGELOG.md#L43-L45](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L43-L45), [CHANGELOG.md#L31-L35](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L31-L35), [CHANGELOG.md#L37-L41](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L37-L41) (`clm_34fd675cc96d4563393632cf2f6ed211228ec021c3bded98a45c1f3f6b53af76`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: agent fixtures can be dumped with the dump_agent Django management command, which gathers the agent, chain, and component graph. -- evidence: [README.md#L304-L311](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L304-L311), [README.md#L301-L302](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L301-L302) (`clm_62d63044e7ae160cd48c5226b94e6b0c112ccd1b515c44593097eac9278cff9d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product includes a no-code agent editor where users drop and connect nodes into a graph representing an agent's cognitive logic, with embedded chat for testing and debugging. -- evidence: [README.md#L55-L56](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L55-L56) (`clm_54b58b6d0a5c1e945e0c146d8b7160eee06595aea930d4752cff47f2517f7bc9`)
- [observation/documented] A multi-agent chat interface lets users interact with teams of agents; a default IX moderator agent delegates tasks, and specific agents can be targeted via @mentions. -- evidence: [README.md#L61-L63](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L61-L63) (`clm_71eef01b6fe735bbaf83a10d016d4575cce8f208b86fd730d209b726ba376965`)
- [observation/documented] The smart input bar auto-completes agent @mentions and file/data artifacts created by tasks. -- evidence: [README.md#L70-L70](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L70-L70) (`clm_fa5e491a027fb1098749bff86127bc7319c898af3ad5b9c4fbc881ab04f29652`)
- [observation/documented] The agent-ix CLI starts a preconfigured docker-compose cluster, downloads required images, supports scaling workers (e.g. 'ix scale 5'), and can launch a dev version image. -- evidence: [README.md#L126-L127](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L126-L127), [README.md#L118-L119](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L118-L119), [README.md#L129-L131](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L129-L131), [README.md#L133-L136](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L133-L136) (`clm_4f93c94b63b119621611663f37aa538a468dca692ee504e0b547ff8c7613123a`)

## memory-state (1 claim(s))

- [observation/documented] The changelog describes an artifact system storing task results in the database, giving agents object permanence; artifacts can be viewed by users or reused in future tasks. -- evidence: [CHANGELOG.md#L76-L78](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L76-L78) (`clm_f83005e40a10be22872bb3c4f96c74e852e26afa90eac3d1da815d555afd4c10`)

## orchestration (1 claim(s))

- [observation/documented] The agent runner backend is dockerized and triggered via a celery message queue, allowing horizontal scaling of agents running in parallel. -- evidence: [README.md#L76-L77](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L76-L77) (`clm_826bdb0c3af275c202de633d42ee08bb9adbe977fd9e56fe71feb72d9537a628`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Supported model providers are listed as OpenAI, with Google PaLM, Anthropic, and Llama marked experimental. -- evidence: [README.md#L49-L52](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/README.md#L49-L52) (`clm_3a406f1e7d53169fdd03a29a6f057fce81f418c3194289a280cb76002b069a1f`)

## limitations (1 claim(s))

- [observation/documented] The 0.1 alpha changelog states the project is in early development, not ready for general use, though usable for developers to experiment with chains and agents. -- evidence: [CHANGELOG.md#L5-L7](https://github.com/kreneskyp/ix/blob/d5868fc1d56d5616306e15b1a10a06256cc6e4d2/CHANGELOG.md#L5-L7) (`clm_6af7031e4a3e942a8f05539cdd4e875b057f85cc2446c5fbbdafe0403bd6faac`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

