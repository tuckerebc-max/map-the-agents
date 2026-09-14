# julien-c/synthtraces -- full detail

[Back to orientation](synthtraces.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/julien-c/synthtraces/e5f8ec99d8140bcf650b61d9401af996c0c70789/255a7f2e31a09665.json](../../../wiki/dossiers/julien-c/synthtraces/e5f8ec99d8140bcf650b61d9401af996c0c70789/255a7f2e31a09665.json)

## specifications (2 claim(s))

- [observation/documented] The project is described as a minimal codebase that generates synthetic coding agent session traces using the Pi coding-agent package. -- evidence: [README.md#L14-L14](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L14-L14) (`clm_03829bc430697e0d5f36a18217880cc4563cfef75e50068e789653eaa3e1d8ed`)
- [observation/documented] The generation matrix comprises 20 agent models, 3 local user models, 20 codebases, and 20 starting questions, totaling 24,000 sessions. -- evidence: [README.md#L25-L31](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L25-L31) (`clm_28e4ed529cdc705f5922d8ebb729937d071527ad9ab6c344d64692b7fbaecd1d`)

## components (1 claim(s))

- [observation/documented] The full exchange is recorded as a trace, and the dataset is the cartesian product of agent model, user model, codebase, and starting question. -- evidence: [README.md#L21-L21](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L21-L21) (`clm_85544aa3b9a575fa8c1e6060fdb73ac5af9e8c68ea8057afb51f8af5c28ee06e`)

## design-choices (1 claim(s))

- [observation/documented] Each generated session pairs two models: a remotely hosted open model acting as the coding agent and a local llama.cpp model playing the user, within one of the project codebases. -- evidence: [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19), [README.md#L16-L16](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L16-L16) (`clm_215efc569222f7db7773e6680b47fd2344eb32c11153f927502c9b9f4a5e521f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The user model opens with one of the starting questions and drives the conversation with the agent over up to N turns, while the agent reads, edits, and runs against a locally cloned codebase. -- evidence: [README.md#L35-L54](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L35-L54), [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19) (`clm_7b8245e480822bc4ae9d4fc652bc2b841086b273f3d90b7e1fa5f30f647941fa`)

## tools-permissions (1 claim(s))

- [observation/documented] The coding agent is equipped with the default Pi tools: read, write, edit, and bash. -- evidence: [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19) (`clm_4bbde4198df54eeecaa506b36eb12fe55067cf54dd1d2ec341ff6a0719d6a4c6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The 20 remote agent models are served by providers including novita, featherless-ai, together, groq, and nscale, per the listed model table. -- evidence: [remote-models.md#L1-L22](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/remote-models.md#L1-L22) (`clm_65844314ddddda643db529fb36a561736a813c922ef26fc168d8654ac95d904a`)
- [observation/documented] Local user models are GGUF quantizations (Q8_0) such as Qwen3.6-27B, Qwen3.6-35B-A3B-MTP, and gemma-4-26B-A4B-it, run via llama.cpp. -- evidence: [README.md#L25-L31](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L25-L31), [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19) (`clm_1b65dde6f0c2c6e84dca08d7db333007d5e55cbd7922643f8d0004341ed4e84d`)

## limitations (1 claim(s))

- [observation/documented] The README's final statistics section is a TODO, to be populated after generation with success rate, turn counts, and token counts. -- evidence: [README.md#L58-L58](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L58-L58) (`clm_1b59d6e4bd9603dba68e8bbbb6dc79b31a21f21a7358b5af34374351160ef510`)

## relevance (1 claim(s))

- [observation/documented] The project is MIT-licensed, English-language, and links to a GitHub code repository and a Hugging Face dataset, both named julien-c/synthtraces. -- evidence: [README.md#L1-L8](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L1-L8), [README.md#L62-L64](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L62-L64), [README.md#L68-L69](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L68-L69) (`clm_7cdd5a4850da1a3efc4f8bf070c33f1e887112232f85e0b308bdc4dd8bea61b0`)

