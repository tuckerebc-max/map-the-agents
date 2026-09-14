# aws/aws-mwaa-local-runner -- full detail

[Back to orientation](aws-mwaa-local-runner.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aws/aws-mwaa-local-runner/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/a022cda1bd8255b3.json](../../../wiki/dossiers/aws/aws-mwaa-local-runner/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/a022cda1bd8255b3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The CLI builds a Docker container image locally similar to a MWAA production image, letting users develop and test DAGs, custom plugins, and dependencies before deploying to MWAA. -- evidence: [README.md#L17-L17](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L17-L17) (`clm_ea28c598da03b37109a02eaf8404de8288f7bd1ea684d76cf28062d62a4e1ffd`)
- [observation/documented] The repo contains dags/, docker/ (config, scripts, compose files, Dockerfile), plugins/, requirements/, and a mwaa-local-env script, per its file listing. -- evidence: [README.md#L21-L53](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L21-L53) (`clm_82f695c0e50ca5a8c60c61dc49ea74fda90242bc08ce3e50b7ae1e18e4fd14a9`)

## design-choices (1 claim(s))

- [observation/documented] Dynamic configurations that depend on environment class are aligned with the Large MWAA environment class in this repository. -- evidence: [README.md#L12-L13](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L12-L13) (`clm_af216e731d51b4ee1cb64d23feb6063ef363704e45b96cf2f81d590e3c78bfad`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors should file issues with reproducible steps and version info, fork and PR against main with focused changes, ensure local tests pass, and report security issues privately rather than via public GitHub issues. -- evidence: [CONTRIBUTING.md#L54-L54](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L54-L54), [CONTRIBUTING.md#L17-L20](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L17-L20), [CONTRIBUTING.md#L32-L37](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L32-L37), [CONTRIBUTING.md#L14-L15](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L14-L15) (`clm_dbde6182d21370e6059e92897a0970cd9a4df1a1124887bb26fee47a45013e64`)
- [observation/documented] Repository development practice: the project uses the Amazon Open Source Code of Conduct and the MIT-0 license, with contributors asked to confirm licensing of their contributions. -- evidence: [README.md#L213-L213](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L213-L213), [CONTRIBUTING.md#L59-L59](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L59-L59), [CODE_OF_CONDUCT.md#L2-L4](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CODE_OF_CONDUCT.md#L2-L4), [CONTRIBUTING.md#L48-L50](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L48-L50) (`clm_622b2bb4dc29b616f6938903ba539d8f65b6d17bf906c47d51092b1a2fe7be0b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The repository provides a CLI utility that replicates an Amazon MWAA environment locally. -- evidence: [README.md#L8-L8](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L8-L8) (`clm_0b646d021d00d4712a6a8b0b2a8e77f8f91ea557f0eabdb8b5013ff9cdf7fb7b`)
- [observation/documented] The mwaa-local-env script supports subcommands including build-image, start, test-requirements, package-requirements, test-startup-script, and reset-db. -- evidence: [README.md#L138-L140](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L138-L140), [README.md#L158-L160](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L158-L160), [README.md#L84-L86](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L84-L86), [README.md#L194-L196](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L194-L196), [README.md#L72-L74](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L72-L74), [README.md#L115-L117](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L115-L117) (`clm_4ba7257c79bacb52c2fcef2073304f4ea44aee29f9218e70c19edaf84fffdada`)
- [observation/documented] The local Airflow UI is served at http://localhost:8080, with default credentials admin/test created by bootstrap.sh. -- evidence: [README.md#L94-L95](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L94-L95), [README.md#L99-L99](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L99-L99), [README.md#L92-L92](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L92-L92) (`clm_3de1753ba02f836eb6cfc614dd1a55d647c61824f665f31b19c48713461955d5`)

## memory-state (1 claim(s))

- [observation/documented] A Fernet key generated during image build encrypts connection passwords in the Airflow DB; rebuilding the image can produce a new key requiring a DB reset. -- evidence: [README.md#L202-L205](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L202-L205) (`clm_3e0c4488462571782f6f3de2b3c5ae2a8043083092bb36ea18723ef55c1c02cb`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Python dependencies are managed via requirements/requirements.txt, which can be tested or packaged into WHL files without running Airflow using dedicated CLI commands. -- evidence: [README.md#L136-L136](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L136-L136), [README.md#L138-L140](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L138-L140), [README.md#L112-L113](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L112-L113), [README.md#L115-L117](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L115-L117) (`clm_10997f544553451b8020ca2a0bb1c0c6c0c8a8a98853f550f1446bf957ff5103`)

## limitations (1 claim(s))

- [observation/documented] Airflow 3.x versions are to be supported via the separate amazon-mwaa-docker-images repository, not this local-runner repo. -- evidence: [README.md#L4-L4](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L4-L4) (`clm_e240bbab4f1daa94eda835bbe9639eb485cf8b6006507b7cc8dcb4923b6713a0`)

## relevance (1 claim(s))

- [observation/documented] For Airflow 2.9+, MWAA has open-sourced production images in amazon-mwaa-docker-images that can create a local environment identical to MWAA. -- evidence: [README.md#L2-L2](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L2-L2) (`clm_9b4991308ef132f3a4ca30ce1da727fc6088e316f24b8c9432a397a4046e95d8`)

