# touchpoint-labs/gadfly -- full detail

[Back to orientation](gadfly.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/touchpoint-labs/gadfly/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/8e44562db5006424.json](../../../wiki/dossiers/touchpoint-labs/gadfly/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/8e44562db5006424.json)

## specifications (1 claim(s))

- [observation/documented] Gadfly is a Socratic supervision layer that sits inside an AI coding agent's live tool-call loop, questioning consequential moves before they happen. -- evidence: [README.md#L5-L5](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L5-L5), [README.md#L20-L24](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L20-L24) (`clm_882b5a009d20356626caeca0fce2ef4dea0809cb8f0957a34a4b5c2818a6f74e`)

## components (1 claim(s))

- [observation/documented] Two isolated, read-only supervisors review each action: an Architect (default Opus) catching spec drift and undiscussed decisions, and a Code Reviewer (default Sonnet) catching real defects. -- evidence: [spec.md#L16-L16](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L16-L16), [README.md#L91-L97](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L91-L97), [README.md#L89-L89](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L89-L89) (`clm_0cbd08a771b8296897647ddfd461fc3e6888d57b48c7d99de9159ad2aadd9598`)

## design-choices (2 claim(s))

- [observation/documented] An autonomy dial (autonomous, balanced, collaborative) controls how often undiscussed decisions surface to the user; irreversible operations always ask regardless of the setting. -- evidence: [spec.md#L50-L50](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L50-L50), [README.md#L149-L151](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L149-L151), [README.md#L153-L153](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L153-L153), [README.md#L147-L147](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L147-L147) (`clm_0376cb9dc1e4e5382f9316a143c5abb01fdd241ae52f39f4aae24c0426d57661`)
- [observation/documented] Architecture is a pure, agent- and LLM-agnostic core wrapped by two swappable adapters (host-agent format and LLM provider); supervisors call a provider-neutral client with models set in config. -- evidence: [README.md#L227-L229](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L227-L229), [spec.md#L76-L80](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L76-L80), [README.md#L231-L244](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L231-L244) (`clm_d2b7cb21345ad8a16acaf4d91a6e01487d384ea065d42a579f3337e120f6fb30`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Reviews produce four verdicts: silent allow, a question sent back to the agent, a surface that pauses and asks the user, and a block on spec-violating or buggy actions. -- evidence: [README.md#L62-L66](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L62-L66), [README.md#L28-L33](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L28-L33) (`clm_b4ccc116b835aebcec2404e3f20b46b41253febeaa4e61885b1a909b70420d37`)
- [observation/documented] CLI commands include gadfly init (requires spec.md), status, config, disable/enable, and uninstall; configuration lives in gadfly.toml with optional keys and defaults. -- evidence: [README.md#L178-L184](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L178-L184), [README.md#L188-L190](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L188-L190), [README.md#L167-L169](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L167-L169) (`clm_2b5fca4fbdb8f61b809b951035372c2ae3c4e8d8a38433bd8551ab5727e836ea`)

## memory-state (2 claim(s))

- [observation/documented] Supervision is grounded in five project files: spec.md (human, required), claude.md (human, optional), codemap.md (builder), decisions.md and memory.md (Gadfly-owned), with a defined trust order. -- evidence: [spec.md#L28-L28](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L28-L28), [spec.md#L20-L26](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L20-L26), [README.md#L119-L125](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L119-L125) (`clm_bf256486053b36ff38b0f85aa8e9d829fe29d2a531e09a20927bda49a84ed054`)
- [observation/documented] An append-only edit-ledger records agent edits; out-of-band human edits are diffed against them by a separate idle-time extractor that distills generalizable corrections into durable rules. -- evidence: [spec.md#L68-L68](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L68-L68), [README.md#L18-L18](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L18-L18), [README.md#L104-L107](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L104-L107) (`clm_e571918b9f911e09e41297784035a7abce80eb813e933cfa8f90394559e46b12`)

## orchestration (1 claim(s))

- [observation/documented] A deterministic first pass auto-allows reads and safe commands without any model call, so LLM supervisors only engage for consequential actions. -- evidence: [README.md#L58-L60](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L58-L60), [spec.md#L36-L40](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L36-L40) (`clm_6e22ef057fda910ee0e87b17b2ee20fd68a37cf0429878214ecf9f8f4a44e473`)

## tools-permissions (1 claim(s))

- [observation/documented] The agent can read the memory files but is denied direct writes to spec.md, claude.md, and decisions.md; those files change only via the human or Gadfly. -- evidence: [README.md#L127-L129](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L127-L129), [spec.md#L36-L40](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L36-L40) (`clm_ab7e1510af2897fcc01b0870d5de99ed98701b21ec245f46ff92e20ea52ea3e9`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project advertises zero dependencies, targets Python 3.11+, is MIT licensed, and in v1 supervises only Claude Code, running on the user's existing subscription without an API key. -- evidence: [README.md#L159-L161](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L159-L161), [README.md#L157-L157](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L157-L157), [README.md#L11-L14](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L11-L14), [README.md#L262-L262](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/README.md#L262-L262) (`clm_d62a014318873671a1dfa88b3cdb168357da3e9f8df32c2eb7e4ff12429dbd5e`)

## limitations (1 claim(s))

- [observation/documented] Stated v1 non-goals include no post-hoc QA practitioner, no taskmaster, no full interactive or training mode, no daemon, and no adapters for other agents; supervisors never write code or run commands. -- evidence: [spec.md#L11-L14](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L11-L14), [spec.md#L84-L89](https://github.com/Touchpoint-Labs/Gadfly/blob/2798406b5d27a87de29ca8e6d1b86cc7f25d6408/spec.md#L84-L89) (`clm_9fa9a915c32de59faea3bc7abde5774307efafd0cc54a1f1b389fa2352fc5bb5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

