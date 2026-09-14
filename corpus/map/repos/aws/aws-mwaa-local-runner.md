# aws/aws-mwaa-local-runner

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ff4f882f10cd @ a022cda1bd8255b3

## Summary (orientation draft, not independently verified)

aws-mwaa-local-runner is a CLI utility that builds a Docker image replicating an MWAA environment locally for DAG/plugin/dependency testing, with commands for building, running, testing requirements, and resetting the DB. Evidence is mostly README usage documentation plus contributor guidelines.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The CLI builds a Docker container image locally similar to a MWAA production image, letting users develop and test DAGs, custom plugins, and dependencies before deploying to MWAA. -- evidence: [README.md#L17-L17](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L17-L17)
  - [observation/documented] The repo contains dags/, docker/ (config, scripts, compose files, Dockerfile), plugins/, requirements/, and a mwaa-local-env script, per its file listing. -- evidence: [README.md#L21-L53](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L21-L53)
- design-choices (1 claim(s)):
  - [observation/documented] Dynamic configurations that depend on environment class are aligned with the Large MWAA environment class in this repository. -- evidence: [README.md#L12-L13](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L12-L13)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors should file issues with reproducible steps and version info, fork and PR against main with focused changes, ensure local tests pass, and report security issues privately rather than via public GitHub issues. -- evidence: [CONTRIBUTING.md#L54-L54](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L54-L54), [CONTRIBUTING.md#L17-L20](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L17-L20), [CONTRIBUTING.md#L32-L37](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L32-L37), [CONTRIBUTING.md#L14-L15](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L14-L15)
  - [observation/documented] Repository development practice: the project uses the Amazon Open Source Code of Conduct and the MIT-0 license, with contributors asked to confirm licensing of their contributions. -- evidence: [README.md#L213-L213](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L213-L213), [CONTRIBUTING.md#L59-L59](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L59-L59), [CODE_OF_CONDUCT.md#L2-L4](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CODE_OF_CONDUCT.md#L2-L4), [CONTRIBUTING.md#L48-L50](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/CONTRIBUTING.md#L48-L50)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The repository provides a CLI utility that replicates an Amazon MWAA environment locally. -- evidence: [README.md#L8-L8](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L8-L8)
  - [observation/documented] The mwaa-local-env script supports subcommands including build-image, start, test-requirements, package-requirements, test-startup-script, and reset-db. -- evidence: [README.md#L138-L140](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L138-L140), [README.md#L158-L160](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L158-L160), [README.md#L84-L86](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L84-L86), [README.md#L194-L196](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L194-L196), [README.md#L72-L74](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L72-L74), [README.md#L115-L117](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L115-L117)
- memory-state (1 claim(s)):
  - [observation/documented] A Fernet key generated during image build encrypts connection passwords in the Airflow DB; rebuilding the image can produce a new key requiring a DB reset. -- evidence: [README.md#L202-L205](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L202-L205)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Python dependencies are managed via requirements/requirements.txt, which can be tested or packaged into WHL files without running Airflow using dedicated CLI commands. -- evidence: [README.md#L136-L136](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L136-L136), [README.md#L138-L140](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L138-L140), [README.md#L112-L113](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L112-L113), [README.md#L115-L117](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L115-L117)
- limitations (1 claim(s)):
  - [observation/documented] Airflow 3.x versions are to be supported via the separate amazon-mwaa-docker-images repository, not this local-runner repo. -- evidence: [README.md#L4-L4](https://github.com/aws/aws-mwaa-local-runner/blob/ff4f882f10cdf51ef876ba77aabcda22c680bbe7/README.md#L4-L4)
- relevance (1 claim(s)):
More evidence: [full detail](aws-mwaa-local-runner.detail.md)

Metadata and full claim list: [full detail](aws-mwaa-local-runner.detail.md)
Human notes ([notes](aws-mwaa-local-runner.notes.md), never overwritten by build)

[Back to map index](../../index.md)
