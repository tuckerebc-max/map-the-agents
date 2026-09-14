---
access: public
aliases: []
claim_ids:
- clm_1888111f264132ad7bcc6dafb1ad910ca25a1bfffdda356e6390a47809be0a5e
- clm_4d679a7721a0a7466801d7faa3a683154189365456d803d6bfc8b02a45bda05b
- clm_518b47bf4bb6c2ee3898c60718ab2ba89f1d27d4677bc5659c5fe42c2ee66b9c
- clm_b14b68b0b21e32f93bc7ef1e6d164d4a1471cb3cf6fb8906b947589b2dad4d66
- clm_bbefd04e833af164d80dde40596276f5873cdac92af0729e96ba99107af5ad01
- clm_cb6f5f71518ac5b508fbf0e1cc02c9858ed092bb6745b1c52aa9fc78df4ac206
- clm_dd7fc1d493f5b148d97f817ce815850bdab25bdfb3aa5d8795ce95a80d4592cd
- clm_e0d3f8ed590c5921ba2a09da2a8e9c25742049d251a447fd5b252f448b4e723c
maturity: draft
page_id: pg_42e297c1bd545cd2bae59381c321e960
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2ed4c8ce3ca75862ae801c92a74bbfb1
title: codeintegrity-ai/mutahunter/README.md @ 97221a1aedca
updated_at: '2026-09-14T02:00:23Z'
---

# codeintegrity-ai/mutahunter/README.md @ 97221a1aedca

<!-- rcw:begin owner=source:src_2ed4c8ce3ca75862ae801c92a74bbfb1 block=evidence -->
- The tool reports mutation coverage metrics including total, survived, killed, timeout, and compile-error mutant counts plus total cost. [@claim:clm_1888111f264132ad7bcc6dafb1ad910ca25a1bfffdda356e6390a47809be0a5e]
- The repository includes an examples directory with a Java Maven example demonstrating LLM-based mutation testing. [@claim:clm_4d679a7721a0a7466801d7faa3a683154189365456d803d6bfc8b02a45bda05b]
- Generated mutants are written under a logs/_latest/mutants directory, and each mutant run is logged as survived or killed. [@claim:clm_518b47bf4bb6c2ee3898c60718ab2ba89f1d27d4677bc5659c5fe42c2ee66b9c]
- A CLI command 'mutahunter run' accepts a test command, model name, source file path, and test file path as arguments. [@claim:clm_b14b68b0b21e32f93bc7ef1e6d164d4a1471cb3cf6fb8906b947589b2dad4d66]
- The tool appears to run the user-specified test command (e.g. 'mvn clean test') against each generated mutant to determine survival. [@claim:clm_bbefd04e833af164d80dde40596276f5873cdac92af0729e96ba99107af5ad01]
- Usage involves setting an OPENAI_API_KEY environment variable, and the example run uses the gpt-4o-mini model. [@claim:clm_cb6f5f71518ac5b508fbf0e1cc02c9858ed092bb6745b1c52aa9fc78df4ac206]
- Mutahunter is described as open-source, language-agnostic, LLM-based mutation testing software. [@claim:clm_dd7fc1d493f5b148d97f817ce815850bdab25bdfb3aa5d8795ce95a80d4592cd]
- The project is licensed under AGPL 3.0. [@claim:clm_e0d3f8ed590c5921ba2a09da2a8e9c25742049d251a447fd5b252f448b4e723c]
<!-- rcw:end owner=source:src_2ed4c8ce3ca75862ae801c92a74bbfb1 block=evidence -->

## Researcher notes

