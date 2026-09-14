# iwangjian/coding-tutor -- full detail

[Back to orientation](coding-tutor.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/iwangjian/coding-tutor/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/d3dc65a20551d0d7.json](../../../wiki/dossiers/iwangjian/coding-tutor/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/d3dc65a20551d0d7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The project proposes Traver (Trace-and-Verify), an agent workflow that incorporates knowledge tracing and turn-by-turn verification for coding tutoring. -- evidence: [README.md#L11-L11](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L11-L11) (`clm_7883b608de9ae388fabb8bca6aaaa8f0ef0ed30cf7baa5a35b8f5fe38d42f0d8`)
- [observation/documented] A trained verifier checkpoint (Verifier-7B) is released for download on Hugging Face. -- evidence: [README.md#L98-L98](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L98-L98) (`clm_236a6b104b0c2ef259fc43c18298775faab59781d56b9d245b18c7f806c0381b`)
- [observation/documented] Released simulated dialogues are stored as JSON records containing a namespace field and a conversation list with alternating tutor and student entries. -- evidence: [README.md#L100-L120](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L100-L120) (`clm_5102e68f914185e003c7566a3af62d517a4211714ce5c1045ccf2964494bde09`)

## design-choices (1 claim(s))

- [observation/documented] Although coding tutoring is the example scenario, the authors state the method extends to other task-tutoring settings where content must adapt to users' varying background knowledge. -- evidence: [README.md#L11-L11](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L11-L11) (`clm_4231913bce16f44d08ad5cc9381a99f89a95b89b1301861908eaf115025b112d`)

## workflows (3 claim(s))

- [observation/documented] Setup requires downloading EvoCodeBench-2403 and building its execution environment per that project's instructions, which the README notes can take a few hours. -- evidence: [README.md#L26-L26](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L26-L26) (`clm_862fd44c5f96d4486ac3fe20a6d718bb7990aa8ea2fe48d1beeae3b861d3e86d`)
- [observation/documented] The project is installed via a Python 3.10 conda environment followed by pip install -r requirements.txt. -- evidence: [README.md#L28-L33](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L28-L33) (`clm_74863043154dcb90579b31103e2bdf12b9bef30309758e415a85a9b7f0b8033d`)
- [observation/documented] Coding tests for simulated students run in three steps via dedicated scripts: pre-test, student code generation, and coding-test metrics. -- evidence: [README.md#L78-L79](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L78-L79), [README.md#L72-L72](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L72-L72), [README.md#L75-L75](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L75-L75) (`clm_061443f6fbf1666e09cfda538d1a84a9cb2c5d20e278ae97e2d59bd1f3f927b0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Users must configure their own Azure API key, data path, and model path based on files under scripts/run/ before use. -- evidence: [README.md#L37-L37](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L37-L37) (`clm_55ec0cb49ccb596a6e6c9cf7fa93193b7b66f15ae139deafa884b724b3e4f767`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (4 claim(s))

- [observation/documented] The work introduces DICT, an evaluation protocol combining student simulation with coding tests to assess tutoring performance. -- evidence: [README.md#L11-L11](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L11-L11) (`clm_5054a540a2958f92b04001626ddc40a1fc57bb37f1289c6648a91effc7d96024`)
- [observation/documented] The README reports that simulated students at different levels show distinct task-completion abilities, and presents DICT as a scalable, cost-effective proxy for human evaluation. -- evidence: [README.md#L133-L133](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L133-L133) (`clm_5c83a36032a87160a57ebe51c5a24faf497ed9c07bf55b8e85838d2b6f5e9287`)
- [observation/documented] Evaluation scripts cover pre-test performance, tutoring outcome (TOR) computed from pre- and post-test directories, and tutoring outcome curves (TOC). -- evidence: [README.md#L84-L84](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L84-L84), [README.md#L87-L87](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L87-L87), [README.md#L90-L91](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L90-L91) (`clm_b5d95599ba410e83664262048d3b919616e7a76222e8d7f37e4472ec8ccb4072`)
- [observation/documented] The README reports that the Traver workflow with the trained verifier exhibits inference-time scaling for coding tutoring. -- evidence: [README.md#L141-L144](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L141-L144) (`clm_663a54f10b3b7e9a4e34c4a89a38bb19dab78ea3cfe61b0ff66ee623d748a05d`)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt pins libraries including torch 2.4.0, transformers 4.44.2, vllm 0.5.4, deepspeed 0.15.0, flash-attn 2.7.2.post1, peft 0.13.2, and openai 1.35.12. -- evidence: [requirements.txt#L1-L25](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/requirements.txt#L1-L25) (`clm_de6e58f593021a29c88e8d2351fc5cd0a489f3400284290bce917421d7a5692c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The work was accepted to ACL Findings 2025 and released on arXiv (2502.13311) in February 2025. -- evidence: [README.md#L19-L21](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L19-L21) (`clm_88b02c1fc04f4f981b1da4b087de3f0d2a836d541e55d4e3b48d2e9e04f13ca8`)

