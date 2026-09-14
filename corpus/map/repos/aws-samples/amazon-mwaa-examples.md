# aws-samples/amazon-mwaa-examples

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d81ee28ec4ea @ 9f7c741a27bf9484

## Summary (orientation draft, not independently verified)

This repository is a collection of educational example DAGs, requirements.txt files, plugins, CloudFormation templates, and IAM policies for Amazon MWAA, not a supported product. Evidence covers repository contents and contributor guidelines; no runtime agent behavior is documented.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Example DAG workflows include moving Airflow Connections and Variables to AWS Secrets Manager, EMR jobs, Bash Operator interactive commands, duplicating an RBAC role, and returning the DAG ID during task execution. -- evidence: [README.md#L19-L23](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L19-L23)
  - [observation/documented] A usecases folder contains complete sample use cases with documentation, infrastructure as code, and dependent resources, including an image processing pipeline, CodeArtifact Python dependency setup, and stopping/starting an MWAA environment. -- evidence: [README.md#L28-L30](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L28-L30), [README.md#L26-L26](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L26-L26)
- design-choices (2 claim(s)):
  - [observation/documented] The examples assume a working Amazon MWAA environment as a prerequisite. -- evidence: [README.md#L57-L57](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L57-L57)
  - [observation/documented] The project is licensed under the MIT-0 License, and contributors will be asked to confirm licensing of their contributions. -- evidence: [CONTRIBUTING.md#L59-L59](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/CONTRIBUTING.md#L59-L59), [README.md#L65-L65](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L65-L65)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors are asked to fork the repo, make focused changes, ensure local tests pass, commit with clear messages, submit a pull request, and monitor automated CI failures. -- evidence: [CONTRIBUTING.md#L32-L37](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/CONTRIBUTING.md#L32-L37)
  - [observation/documented] Repository development practice: bug reports should use the GitHub issue tracker and include a reproducible test case, code version, relevant modifications, and unusual environment details. -- evidence: [CONTRIBUTING.md#L17-L20](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/CONTRIBUTING.md#L17-L20), [CONTRIBUTING.md#L12-L12](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/CONTRIBUTING.md#L12-L12)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The repository offers requirements.txt examples to help find the right Python library combinations, including Amazon and GCP backport providers. -- evidence: [README.md#L34-L34](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L34-L34), [README.md#L36-L37](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L36-L37)
- limitations (1 claim(s)):
  - [observation/documented] The examples are educational samples, not supported products; users are told to test, secure, and optimize any integrated application before production use. -- evidence: [README.md#L5-L5](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L5-L5)
- relevance (1 claim(s)):
  - [observation/documented] The repository provides example DAGs, requirements.txt files, plugins, and CloudFormation templates focused on Amazon MWAA, and notes many contributions also apply to self-managed Apache Airflow. -- evidence: [README.md#L9-L9](https://github.com/aws-samples/amazon-mwaa-examples/blob/d81ee28ec4ea606339a2f71368ebad444fef3316/README.md#L9-L9)

(3 additional claim(s) omitted for length; see [full detail](amazon-mwaa-examples.detail.md) for every claim.)

Metadata and full claim list: [full detail](amazon-mwaa-examples.detail.md)
Human notes ([notes](amazon-mwaa-examples.notes.md), never overwritten by build)

[Back to map index](../../index.md)
