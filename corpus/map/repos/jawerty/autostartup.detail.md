# jawerty/autostartup -- full detail

[Back to orientation](autostartup.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jawerty/autostartup/60ec3affede5062345657a11b3bd020975b488d9/b2515a478e1e3939.json](../../../wiki/dossiers/jawerty/autostartup/60ec3affede5062345657a11b3bd020975b488d9/b2515a478e1e3939.json)

## specifications (1 claim(s))

- [observation/documented] The project is described as a Llama 2 autonomous agent that devises a startup idea, business plans, and React codebases from a simple user 'intuition'. -- evidence: [README.md#L5-L5](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L5-L5) (`clm_1f99275eda3b8e236020dc3c1e82cd1b5226701781b1edbe829d5f0a48b057b7`)

## components (1 claim(s))

- [observation/documented] After plan approval, the agent generates a React codebase using the author's separate 10x-React-Engineer project. -- evidence: [README.md#L8-L8](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L8-L8), [README.md#L10-L22](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L10-L22) (`clm_e533d32d7e4c6dbf8d6c4aae136d494851c553afa76707031aa53b93c9a0cbba`)

## design-choices (1 claim(s))

- [observation/documented] The project advertises 100% Llama 2 inference with no OpenAI keys necessary, and applies lean startup concepts such as pivots and a tight MVP build loop. -- evidence: [README.md#L27-L34](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L27-L34) (`clm_54e77c15b00d3c43644506d1fb6c9a1dc4fccf81154e07fe5415cfebc2a399a4`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: to run from source, install dependencies with pip3 install -r requirements.txt (after Llama 2 access and huggingface-cli login) and run the main loop with python3 main.py; a Google Colab notebook is offered for quick testing. -- evidence: [README.md#L49-L52](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L49-L52), [README.md#L44-L47](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L44-L47), [README.md#L42-L42](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L42-L42), [README.md#L55-L55](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L55-L55) (`clm_0ab916c3efe008be414fa2ccfd5278d9020c8eb71e177e005c353323f46a595c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The user-facing input is a free-text 'intuition' (e.g. 'I think a website for dogsitters would be cool'), and an optional final step applies pivots based on user feedback. -- evidence: [README.md#L8-L8](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L8-L8), [README.md#L10-L22](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L10-L22) (`clm_03f981cf2c902ccc1daffcf76bae77443a3f523f337e86d69440a7abc517f042`)

## memory-state (1 claim(s))

- [observation/documented] The README claims memory via vector search over historically successful ideas paired with intuitions, and that previous criticisms are used for investor approvals. -- evidence: [README.md#L27-L34](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L27-L34) (`clm_da475bc54ded7368025a0f32fe5554efa950d538fad8b614274cf1a1f0e57725`)

## orchestration (1 claim(s))

- [observation/documented] The agent runs an idea loop: it develops a business idea and plan, iterates via a criticism loop that regenerates the plan, and asks an 'investor' prompt for approval, restarting on disapproval. -- evidence: [README.md#L8-L8](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L8-L8), [README.md#L10-L22](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L10-L22) (`clm_38b485dc506ba15a8ba029d71bfdf5df6e1e021a484369752ec567cc79a63503`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt pins torch 2.0.1, transformers 4.31.0, sentence-transformers 2.2.2, scikit-learn 1.3.0, nltk, and huggingface-hub 0.16.4, among others. -- evidence: [requirements.txt#L1-L35](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/requirements.txt#L1-L35) (`clm_e52b562b3ee999a63d911e9ca4f90d2b97d5e8d9c702f48cb735721875a5e819`)

## limitations (1 claim(s))

- [observation/documented] The author notes the model needs a quality GPU to load the Llama 2 13b chat model, and a TODO says the React coding output needs bug fixing more often than not. -- evidence: [README.md#L58-L58](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L58-L58), [README.md#L37-L37](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L37-L37) (`clm_ba076d4464309fb6940ee9230e3fcd833970ecbee8d926fed397bcaf94a73e9c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

