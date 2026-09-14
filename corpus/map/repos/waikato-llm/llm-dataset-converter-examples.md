# waikato-llm/llm-dataset-converter-examples

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit eb7dc2c462fa @ bf4d50672e26a456

## Summary (orientation draft, not independently verified)

This repository hosts documentation examples for the llm-dataset-converter libraries, published as an MkDocs site deployed via GitHub Actions. The examples document CLI conversion, downloading, and Docker usage of the underlying tools.

## Source coverage

Source coverage (partial): 6 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Output files are automatically compressed when the format supports it, based on the extension used for the output, e.g. producing a .csv.gz via Gzip. -- evidence: [docs/compression.md#L1-L2](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L1-L2), [docs/compression.md#L4-L6](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L4-L6)
  - [observation/documented] Input files are automatically decompressed based on their extension, provided the format supports that. -- evidence: [docs/compression.md#L16-L17](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L16-L17)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: The docs site is built with pinned MkDocs and plugin versions in a virtualenv and served locally with mkdocs serve. -- evidence: [README.md#L11-L14](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L11-L14), [README.md#L18-L20](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L18-L20)
  - [observation/documented] Repository development practice: Any push triggers a site rebuild on GitHub via a GitHub Actions workflow defined in .github/workflows/main.yml. -- evidence: [README.md#L24-L24](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L24-L24), [README.md#L26-L26](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L26-L26)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The examples show a CLI command llm-convert that takes a source reader (e.g. from-alpaca) with --input and a writer (e.g. to-csv-pr) with --output. -- evidence: [docs/docker.md#L21-L33](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L21-L33), [docs/compression.md#L8-L14](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L8-L14)
  - [observation/documented] A separate ldc-convert command is documented for document conversion, using readers like from-doc-pt and from-docx-pt with per-stage -l INFO logging flags. -- evidence: [docs/docx.md#L9-L18](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docx.md#L9-L18), [docs/doc.md#L14-L23](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/doc.md#L14-L23)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Docker usage examples run waikatodatamining/llm-dataset-converter:latest with the current directory mounted at /workspace, either interactively or to run a conversion pipeline. -- evidence: [docs/docker.md#L10-L14](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L10-L14), [docs/docker.md#L21-L33](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L21-L33), [docs/docker.md#L7-L8](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L7-L8)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The .doc text-extraction examples require the ldc-doc library and the antiword binary on PATH, installable via apt on Debian/Ubuntu. -- evidence: [docs/doc.md#L6-L7](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/doc.md#L6-L7), [docs/doc.md#L3-L4](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/doc.md#L3-L4)
  - [observation/documented] The .docx extraction examples require the ldc-docx library. -- evidence: [docs/docx.md#L3-L3](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docx.md#L3-L3)
- limitations (1 claim(s)):
  - [observation/documented] When downloading via Hugging Face, files are cached locally in the user's home directory before being copied to the specified output location. -- evidence: [docs/downloaders.md#L27-L28](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/downloaders.md#L27-L28)
- relevance (1 claim(s)):
  - [inference/documented] The repository appears to be documentation-only example content for the llm-dataset-converter libraries rather than containing the converter implementation itself. -- evidence: [docs/docker.md#L1-L2](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L1-L2), [README.md#L2-L2](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L2-L2)

(1 additional claim(s) omitted for length; see [full detail](llm-dataset-converter-examples.detail.md) for every claim.)

Metadata and full claim list: [full detail](llm-dataset-converter-examples.detail.md)
Human notes ([notes](llm-dataset-converter-examples.notes.md), never overwritten by build)

[Back to map index](../../index.md)
