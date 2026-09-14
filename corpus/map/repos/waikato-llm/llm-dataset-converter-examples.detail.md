# waikato-llm/llm-dataset-converter-examples -- full detail

[Back to orientation](llm-dataset-converter-examples.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/0977f3a6/cf449c25/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/bf4d50672e26a456.json](../../../wiki/dossiers/0977f3a6/cf449c25/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/bf4d50672e26a456.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Output files are automatically compressed when the format supports it, based on the extension used for the output, e.g. producing a .csv.gz via Gzip. -- evidence: [docs/compression.md#L1-L2](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L1-L2), [docs/compression.md#L4-L6](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L4-L6) (`clm_591643db491590ae58d341a9aa42cd880e6c1752d25c5eb3b454303d9cf98370`)
- [observation/documented] Input files are automatically decompressed based on their extension, provided the format supports that. -- evidence: [docs/compression.md#L16-L17](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L16-L17) (`clm_1198a1110524e0bf1e0a7511e904ba0afce34b793bb7c1f01cfe09741826d494`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: The docs site is built with pinned MkDocs and plugin versions in a virtualenv and served locally with mkdocs serve. -- evidence: [README.md#L11-L14](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L11-L14), [README.md#L18-L20](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L18-L20) (`clm_16e93f258071ecc636d2a319e983184a2537d9aabeacb8c7dad95a4f6aa3f9ca`)
- [observation/documented] Repository development practice: Any push triggers a site rebuild on GitHub via a GitHub Actions workflow defined in .github/workflows/main.yml. -- evidence: [README.md#L24-L24](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L24-L24), [README.md#L26-L26](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L26-L26) (`clm_bf5779f445e5965b4e8018d4f6d0c0943babe3663c8c431685a20ff0889bbf04`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The examples show a CLI command llm-convert that takes a source reader (e.g. from-alpaca) with --input and a writer (e.g. to-csv-pr) with --output. -- evidence: [docs/docker.md#L21-L33](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L21-L33), [docs/compression.md#L8-L14](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/compression.md#L8-L14) (`clm_9233bfa8b5195ddecb6fff0061f7d23b5ef99d909c018229bff6c6860d061a32`)
- [observation/documented] A separate ldc-convert command is documented for document conversion, using readers like from-doc-pt and from-docx-pt with per-stage -l INFO logging flags. -- evidence: [docs/docx.md#L9-L18](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docx.md#L9-L18), [docs/doc.md#L14-L23](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/doc.md#L14-L23) (`clm_fffad4307570dd39b382f53e156b40df4a03a6cb9808005891fa51aff2368abd`)
- [observation/documented] An llm-download command fetches files from Hugging Face, taking an identifier (-i), optional type (-t dataset), filename (-f), and output location (-o). -- evidence: [docs/downloaders.md#L17-L25](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/downloaders.md#L17-L25), [docs/downloaders.md#L4-L11](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/downloaders.md#L4-L11) (`clm_987aa7004a1e5ea22c5dfecb8e336fc7c6ceed806f58a7b9552e352b36e76f0e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Docker usage examples run waikatodatamining/llm-dataset-converter:latest with the current directory mounted at /workspace, either interactively or to run a conversion pipeline. -- evidence: [docs/docker.md#L10-L14](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L10-L14), [docs/docker.md#L21-L33](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L21-L33), [docs/docker.md#L7-L8](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L7-L8) (`clm_8e965d19b0f85043971d6255526e4eee0e6b5be84a236df3fd396979beee5c29`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The .doc text-extraction examples require the ldc-doc library and the antiword binary on PATH, installable via apt on Debian/Ubuntu. -- evidence: [docs/doc.md#L6-L7](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/doc.md#L6-L7), [docs/doc.md#L3-L4](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/doc.md#L3-L4) (`clm_57fc99efadac887254e653e29d7c409e763da6c2a723b91cd971e21d963317b7`)
- [observation/documented] The .docx extraction examples require the ldc-docx library. -- evidence: [docs/docx.md#L3-L3](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docx.md#L3-L3) (`clm_88882e513619f1495cc3b195742af9928ba49c25c87a67d09437a5c47469f71f`)

## limitations (1 claim(s))

- [observation/documented] When downloading via Hugging Face, files are cached locally in the user's home directory before being copied to the specified output location. -- evidence: [docs/downloaders.md#L27-L28](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/downloaders.md#L27-L28) (`clm_4edcdbb961ce4f026e610766841cf6a675f59a9ba257c904a86ad0351c4db006`)

## relevance (1 claim(s))

- [inference/documented] The repository appears to be documentation-only example content for the llm-dataset-converter libraries rather than containing the converter implementation itself. -- evidence: [docs/docker.md#L1-L2](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/docs/docker.md#L1-L2), [README.md#L2-L2](https://github.com/waikato-llm/llm-dataset-converter-examples/blob/eb7dc2c462fa61cd3f87a3ad2f4863b75b609e23/README.md#L2-L2) (`clm_6c5f3aa53e91da283c3f0a8b7542b34dd648a86f1e2109d0f11f5963466d169a`)

