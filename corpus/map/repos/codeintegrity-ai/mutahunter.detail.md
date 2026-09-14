# codeintegrity-ai/mutahunter -- full detail

[Back to orientation](mutahunter.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codeintegrity-ai/mutahunter/97221a1aedca8a8e92bf67843903af26cacab5b7/71c01af5105f3c94.json](../../../wiki/dossiers/codeintegrity-ai/mutahunter/97221a1aedca8a8e92bf67843903af26cacab5b7/71c01af5105f3c94.json)

## specifications (2 claim(s))

- [observation/documented] Mutahunter is described as open-source, language-agnostic, LLM-based mutation testing software. -- evidence: [README.md#L5-L5](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L5-L5) (`clm_dd7fc1d493f5b148d97f817ce815850bdab25bdfb3aa5d8795ce95a80d4592cd`)
- [observation/documented] The project is licensed under AGPL 3.0. -- evidence: [README.md#L7-L12](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L7-L12) (`clm_e0d3f8ed590c5921ba2a09da2a8e9c25742049d251a447fd5b252f448b4e723c`)

## components (1 claim(s))

- [observation/documented] Generated mutants are written under a logs/_latest/mutants directory, and each mutant run is logged as survived or killed. -- evidence: [README.md#L27-L28](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L27-L28), [README.md#L30-L31](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L30-L31) (`clm_518b47bf4bb6c2ee3898c60718ab2ba89f1d27d4677bc5659c5fe42c2ee66b9c`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A CLI command 'mutahunter run' accepts a test command, model name, source file path, and test file path as arguments. -- evidence: [README.md#L24-L24](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L24-L24) (`clm_b14b68b0b21e32f93bc7ef1e6d164d4a1471cb3cf6fb8906b947589b2dad4d66`)
- [inference/documented] The tool appears to run the user-specified test command (e.g. 'mvn clean test') against each generated mutant to determine survival. -- evidence: [README.md#L27-L28](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L27-L28), [README.md#L30-L31](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L30-L31), [README.md#L24-L24](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L24-L24) (`clm_bbefd04e833af164d80dde40596276f5873cdac92af0729e96ba99107af5ad01`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The tool reports mutation coverage metrics including total, survived, killed, timeout, and compile-error mutant counts plus total cost. -- evidence: [README.md#L40-L47](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L40-L47) (`clm_1888111f264132ad7bcc6dafb1ad910ca25a1bfffdda356e6390a47809be0a5e`)

## dependencies (1 claim(s))

- [observation/documented] Usage involves setting an OPENAI_API_KEY environment variable, and the example run uses the gpt-4o-mini model. -- evidence: [README.md#L21-L21](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L21-L21), [README.md#L24-L24](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L24-L24) (`clm_cb6f5f71518ac5b508fbf0e1cc02c9858ed092bb6745b1c52aa9fc78df4ac206`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The repository includes an examples directory with a Java Maven example demonstrating LLM-based mutation testing. -- evidence: [README.md#L57-L57](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L57-L57), [README.md#L55-L55](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L55-L55), [README.md#L59-L59](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L59-L59) (`clm_4d679a7721a0a7466801d7faa3a683154189365456d803d6bfc8b02a45bda05b`)

