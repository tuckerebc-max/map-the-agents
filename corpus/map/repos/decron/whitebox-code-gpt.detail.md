# decron/whitebox-code-gpt -- full detail

[Back to orientation](whitebox-code-gpt.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/decron/whitebox-code-gpt/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/c6051f3e9be846f1.json](../../../wiki/dossiers/decron/whitebox-code-gpt/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/c6051f3e9be846f1.json)

## specifications (2 claim(s))

- [observation/documented] The project produces programming assistants hosted on ChatGPT, built by open-sourcing instructions and knowledge files that experts and users collaboratively create and maintain. -- evidence: [README.md#L52-L55](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L52-L55), [README.md#L6-L6](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L6-L6) (`clm_6db968de92748601a5ae4c77d3b11a296833730cd42702f922c038f159876810`)
- [observation/documented] Assistants are listed for Python, Flutter, Git, Regex, Firebase, Node.js, C++, and a DeltaV controls-engineering assistant, with C# and bioinformatics marked as coming soon. -- evidence: [README.md#L29-L33](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L29-L33), [README.md#L18-L27](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L18-L27) (`clm_a3eb740572f94dc831027ec8159bdf179ceca56f00a17ba858a8128ec893d0a3`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Knowledge files are dedicated per topic and organized hierarchically or relationally to augment the LLM's knowledge base; per-flavor regex rule sets are cited as improving valid pattern generation. -- evidence: [README.md#L62-L66](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L62-L66) (`clm_ace0f4fd79a351e54b799981f3b385276f046b9fd94720ad1a47f37225401675`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors fork the repository, clone it locally, and add assistant files via pull requests while updating the README index; solo maintainers may instead add their link to a partnered index. -- evidence: [CONTRIBUTING.md#L9-L9](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/CONTRIBUTING.md#L9-L9), [README.md#L8-L9](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L8-L9), [CONTRIBUTING.md#L7-L7](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/CONTRIBUTING.md#L7-L7), [CONTRIBUTING.md#L11-L12](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/CONTRIBUTING.md#L11-L12) (`clm_5fa0627cd8fe28b6a51f4e31da8868938e8d91f7378d4d1f819ed8b12f54a65d`)
- [observation/documented] Repository development practice: each assistant has a custodian (sole decider of its content) assigned by an admin, who verifies the README directory is updated before merging; forfeiting custodians help find a replacement. -- evidence: [README.md#L83-L83](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L83-L83), [README.md#L79-L79](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L79-L79), [README.md#L85-L85](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L85-L85), [README.md#L87-L87](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L87-L87) (`clm_c09bb6b9ef0f86a66d6db2f7697e3f32ef871b2721862ca7707f4dc5e9703b52`)
- [observation/documented] Repository development practice: custodians are asked to use descriptive names/descriptions with a repo link, disable conversation training, split over-broad assistants, and use backup assistants for experimentation. -- evidence: [README.md#L96-L96](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L96-L96), [README.md#L92-L92](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L92-L92), [README.md#L98-L98](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L98-L98), [README.md#L94-L94](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L94-L94) (`clm_44e685ab4f7e21660f1dae8259af9f7252e73a862f4ceaff6ddebd61231752bb`)
- [observation/documented] Repository development practice: issue reports for assistants or security vulnerabilities should include the assistant title and links to relevant conversation history, or generalized plaintext if sensitive. -- evidence: [README.md#L11-L11](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L11-L11), [SECURITY.md#L9-L11](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/SECURITY.md#L9-L11) (`clm_bc74a5c6d08ea9f60e456c46b49ec25fbc74afcee822189e453b4bc47918b5db`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Assistants are accessed via ChatGPT-hosted custom GPT links and require no installation; users without ChatGPT premium may copy the knowledge files to a different LLM. -- evidence: [README.md#L52-L55](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L52-L55), [README.md#L18-L27](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L18-L27) (`clm_adf449cf0e09ec7e10171c087ed0b043ba4d7abb778d08b6589de7454bfa704a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README claims assistants are quality-tested and rigorously checked, and states that developing automated testing to guarantee functionality is a secondary goal, implying it does not yet exist. -- evidence: [README.md#L68-L71](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L68-L71), [README.md#L18-L27](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L18-L27) (`clm_60f1a6f7ed6f0fe61f48a90667570cde57e9711dea791ba5c1d5267c362c9dff`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] The project warns that conversation-training settings cannot be truly verified and that knowledge-file/document training cannot be disabled in GPT builder, so users should avoid including sensitive material. -- evidence: [README.md#L101-L107](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L101-L107) (`clm_a1357d8913c2cb92bc43b21ddaf73db147f720fbb9910e3d710f012221a6337d`)
- [observation/documented] The README identifies a key flaw of AI assistants: they cannot stay continuously up to date on best practices for every domain, which the project addresses through curated knowledge files. -- evidence: [README.md#L57-L60](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L57-L60) (`clm_f7cf6005db4a205f5f2e8988187bc8f96f2815562cd41e932ad2b749c1bdcfb3`)

## relevance (1 claim(s))

- [observation/documented] The project targets the OpenAI custom GPT marketplace and invites reports on whether its knowledge files transfer effectively to other models; it is volunteer-maintained and seeks sponsors. -- evidence: [README.md#L125-L126](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L125-L126), [README.md#L128-L134](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L128-L134), [README.md#L117-L119](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L117-L119) (`clm_70f500d3a7288c99cf497d14f98e9b2fad8a72cb9663b5e71a6d5dcdee49831e`)

