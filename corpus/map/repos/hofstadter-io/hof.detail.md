# hofstadter-io/hof -- full detail

[Back to orientation](hof.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/hofstadter-io/hof/52feda8ce076ec6a3501811c72dde0ca599b798d/671461f5d33a01fd.json](../../../wiki/dossiers/hofstadter-io/hof/52feda8ce076ec6a3501811c72dde0ca599b798d/671461f5d33a01fd.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is organized around a Go CLI entrypoint (cmd/hof), core logic in lib/, a CUE-based task engine in flow/, docs site source, and CI scripts. -- evidence: [README.md#L75-L80](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L75-L80) (`clm_b3675f3d00a4347391610dd9563ff390ec30845ff2261464da3dc18a400df504`)

## design-choices (2 claim(s))

- [observation/documented] hof is built on CUE, which the project treats as the language for schemas, configuration, and declarative sources of truth, powering both developer experience and implementation. -- evidence: [README.md#L26-L29](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L26-L29) (`clm_39f29d021fe53d75d1fbf63f98aefd0da98544a82f616f291dd9b957ea17659a`)
- [observation/documented] Core features include technology-agnostic code generation from data plus templates, evolvable data models with checkpoint and diff support, an extensible DAG task engine based on cue/flow, and LLM-assisted chat combined with code generation. -- evidence: [README.md#L13-L22](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L13-L22), [README.md#L7-L11](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L7-L11) (`clm_a7cdae4ec2134903d7234aee4c6c6b2ed3b05331c292212b4154e1b2c1952088`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors build the binary with 'make build', run tests with 'make test', and serve docs locally with 'make docs-serve'. -- evidence: [README.md#L92-L94](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L92-L94), [README.md#L86-L88](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L86-L88), [README.md#L98-L100](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L98-L100) (`clm_0c80a46056aec90c887962663eb117275288b568e1b63f27f87c879813995a53`)
- [observation/documented] Repository development practice: AGENTS.md instructs contributing agents to run only one build/validate command at a time (go install ./cmd/hof, then hof version) and forbids other hof commands or go test unless the user explicitly instructs it. -- evidence: [AGENTS.md#L65-L65](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L65-L65), [AGENTS.md#L54-L55](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L54-L55), [AGENTS.md#L59-L59](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L59-L59), [AGENTS.md#L62-L63](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/AGENTS.md#L62-L63) (`clm_2bbc74fb0f9d11e4019b0ed32ca9991e5aee39c2434e134dc6382c0a2197a071`)
- [observation/documented] Repository development practice: contributions follow a standard fork, pull request, and review process with labels organizing issues and PRs; the project follows the CNCF Code of Conduct. -- evidence: [CODE_OF_CONDUCT.md#L3-L3](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/CODE_OF_CONDUCT.md#L3-L3), [README.md#L113-L115](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L113-L115) (`clm_db344ba69b818fe8a89da5de9a96c3e7d701b4e42a91a40f706cdd60449a730c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] hof exposes two interfaces: a CLI suited to scripting and automation, and a TUI for exploring and designing, the latter with a built-in help system. -- evidence: [README.md#L120-L120](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L120-L120), [README.md#L122-L123](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L122-L123), [README.md#L178-L180](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L178-L180) (`clm_cf0b98befba12dcf131c8b19b71e45bf94eb40028c21ca31a9eaa4168b12cf4b`)
- [observation/documented] The CLI offers main commands including chat, create, datamodel, def, eval, export, flow, fmt, gen, mod, tui, and vet, plus additional commands like update, version, completion, and feedback. -- evidence: [README.md#L149-L154](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L149-L154), [README.md#L135-L147](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L135-L147) (`clm_d535373a82465b57b854512d9094172028f7d24f96a0abdc3c882f983b4ef1af`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The security policy states that only the latest version of hof is supported at this time. -- evidence: [SECURITY.md#L5-L5](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/SECURITY.md#L5-L5) (`clm_15c4d538d8e3074ef66be9f9abdbeb9e57e8205d4178487d51517dd90050bf73`)

## relevance (1 claim(s))

- [observation/documented] hof is relevant to teams wanting schema-driven, deterministic or agentic code generation, data model management, and CUE-based workflow orchestration from a single CLI tool. -- evidence: [README.md#L3-L3](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L3-L3), [README.md#L13-L22](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L13-L22), [README.md#L7-L11](https://github.com/hofstadter-io/hof/blob/52feda8ce076ec6a3501811c72dde0ca599b798d/README.md#L7-L11) (`clm_f8231f521c334c5e98ee8a021ecb07ab70e823a923b3271ffac70bda32b1bfea`)

