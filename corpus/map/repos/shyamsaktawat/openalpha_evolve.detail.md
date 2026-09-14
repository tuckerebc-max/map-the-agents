# shyamsaktawat/openalpha_evolve -- full detail

[Back to orientation](openalpha_evolve.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shyamsaktawat/openalpha_evolve/0389aea0e0a745b61babdc0fdd18ac61098dfa84/d4155f4b317d4239.json](../../../wiki/dossiers/shyamsaktawat/openalpha_evolve/0389aea0e0a745b61babdc0fdd18ac61098dfa84/d4155f4b317d4239.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The system uses a modular agent architecture with named agents: PromptDesignerAgent, CodeGeneratorAgent, EvaluatorAgent, DatabaseAgent, SelectionControllerAgent, and a task_manager agent that orchestrates the evolutionary loop and coordinates the others. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63), [README.md#L82-L99](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L82-L99) (`clm_4dcb233eec2d76efe1d0c6d69be71ef878aa36f552b92a7b53e3b7a4b4076e5c`)

## design-choices (1 claim(s))

- [observation/documented] Mutation and bug-fix prompts often request changes in diff format, and the code generator attempts to apply received diffs to the parent code; the features list describes diff-based mutations for targeted modifications. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63), [README.md#L69-L76](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L69-L76) (`clm_6bf311b4dca724d03b43287b96a02a33c550507a14b64c2b6ee2cdb0e439e31c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are asked to report bugs or suggest features via GitHub issues, and to fork the repo, create a feature branch, write clean documented code, add tests if applicable, avoid breaking existing functionality, and submit pull requests with clear descriptions. -- evidence: [README.md#L257-L265](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L257-L265), [README.md#L255-L255](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L255-L255) (`clm_710932ecc951899eeb3f531edcef1c32a113e5a202758f0c3d54086eb987e9bf`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A Gradio web interface is started with 'python app.py'; it displays a local URL (e.g., http://127.0.0.1:7860) and optionally a public share link, where users can define custom tasks and run evolution interactively. -- evidence: [README.md#L167-L172](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L167-L172) (`clm_ecaa41cd141de451dc72c16f4ca94312bbdb29e0e16e2a60f65b482eddce663b`)
- [observation/documented] The CLI entry point runs an evolutionary run via 'python -m main <task.yaml>' (e.g., examples/shortest_path.yaml), with logs also saved to alpha_evolve.log by default. -- evidence: [README.md#L160-L165](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L160-L165) (`clm_656ee61ec88e72d115cd2a81cab3dedc00b97cbb46480cc385bd7143abc55fff`)

## memory-state (1 claim(s))

- [observation/documented] The DatabaseAgent stores programs with code, fitness scores, generation, and lineage as a record of evolutionary history; the README notes this storage is currently in-memory. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63) (`clm_0470886912073b1ea830fb09cd8cfedfda1ccf6f349ad9204baa7357ea6a5c2c`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Per the README feature list, generated code is executed in Docker containers for sandboxed evaluation, with configurable timeout mechanisms. -- evidence: [README.md#L69-L76](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L69-L76) (`clm_48c202c3ce22f3b37976a2cd5e94b20d6485fcba6b40620d8ae663c32e614a9a`)

## evaluation (1 claim(s))

- [observation/documented] The EvaluatorAgent syntax-checks generated code, executes it in an isolated environment against task input/output examples, and scores fitness based on correctness (test cases passed), runtime efficiency, and other potential metrics. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63) (`clm_b79a1dc768c450e1c2cad875a871deee50bb57fb581b1e65bff04c336a67a628`)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt lists litellm, python-dotenv, PyYAML, tiktoken, openai, anthropic, google-generativeai, gradio, docker, Jinja2, pydantic, watchdog, termcolor, requests, and typing-extensions as core libraries, plus pytest. -- evidence: [requirements.txt#L2-L16](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/requirements.txt#L2-L16), [requirements.txt#L32-L32](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/requirements.txt#L32-L32) (`clm_ebfe29bcebd828f3a40cffeac82c3aef913bc4ad8ffbfdb9a2551fe967b598f1`)
- [observation/documented] The README prerequisites require Python 3.10+, pip, git, and a running Docker installation (Docker Desktop on Windows/Mac or Docker Engine on Linux) for sandboxed code evaluation. -- evidence: [README.md#L105-L109](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L105-L109) (`clm_f39c37f4e2d1eb652be0cdf29566f1a8b473f6d390ad233480d9fccf288da4b2`)

## limitations (1 claim(s))

- [observation/documented] The README's disclaimer states this is an experimental project whose generated code may not always be optimal, correct, or secure, and should be reviewed and tested thoroughly before production use. -- evidence: [README.md#L283-L283](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L283-L283) (`clm_2d17cbaacef4034af336c7036a360980cdfa1ba58a500159940345894d9b8286`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

