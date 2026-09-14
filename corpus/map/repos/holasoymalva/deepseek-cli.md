# holasoymalva/deepseek-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 18f5c57f0a53 @ 482743830e15d71f

## Summary (orientation draft, not independently verified)

The evidence is README/LOCAL-SETUP documentation for DeepSeek CLI, a command-line AI coding assistant built on DeepSeek Coder models, supporting local Ollama or cloud API modes. No source code is present in the snapshot, so all claims are documentation-based.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The setup command checks for Ollama, starts the service if needed, downloads the specified model, and verifies the installation. -- evidence: [README.md#L254-L258](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L254-L258)
  - [observation/documented] Interactive mode is described as a REPL with syntax highlighting, session history, automatic file-context inclusion, and multi-turn conversations. -- evidence: [README.md#L264-L268](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L264-L268), [README.md#L262-L262](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L262-L262)
- design-choices (1 claim(s)):
  - [observation/documented] Local Ollama mode is the default (DEEPSEEK_USE_LOCAL defaults to true), with cloud API mode available when an API key is configured. -- evidence: [README.md#L210-L212](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L210-L212), [README.md#L189-L194](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L189-L194)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors fork and clone, run npm install, npm test, and npm run dev; building from source uses npm run build and npm run package. -- evidence: [README.md#L314-L320](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L314-L320), [README.md#L334-L337](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L334-L337), [README.md#L341-L344](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L341-L344)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands including interactive mode (deepseek), single-prompt mode (deepseek chat), setup, --local, --model, --help, and --version. -- evidence: [README.md#L236-L244](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L236-L244)
  - [observation/documented] Repository context can be controlled via flags such as --include-all for the whole repo and --include with specific files or directories. -- evidence: [README.md#L282-L284](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L282-L284), [README.md#L278-L279](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L278-L279)
- memory-state (1 claim(s)):
  - [observation/documented] The CLI maintains context across interactions in multi-turn conversations and automatically includes relevant project files as context. -- evidence: [README.md#L274-L274](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L274-L274), [README.md#L264-L268](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L264-L268)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The tool requires Node.js 18 or higher and Ollama for local operation; the npm package is run-deepseek-cli installed globally. -- evidence: [README.md#L23-L25](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L23-L25), [README.md#L38-L41](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L38-L41)
  - [observation/documented] It uses DeepSeek Coder models in 1.3B, 6.7B, and 33B sizes, with documented RAM needs of 2GB, 8GB, and 32GB respectively. -- evidence: [LOCAL-SETUP.md#L15-L20](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/LOCAL-SETUP.md#L15-L20), [README.md#L198-L202](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L198-L202), [README.md#L366-L368](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L366-L368)
- limitations (1 claim(s)):
  - [observation/documented] Documented model context windows are 16K tokens for the 1.3b, 6.7b, and 33b instruct variants, and the 33b model is noted as slower. -- evidence: [README.md#L356-L360](https://github.com/holasoymalva/deepseek-cli/blob/18f5c57f0a534b29c5cf996a7f64158a6b50eb1a/README.md#L356-L360)
- relevance (1 claim(s)):
More evidence: [full detail](deepseek-cli.detail.md)

Metadata and full claim list: [full detail](deepseek-cli.detail.md)
Human notes ([notes](deepseek-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
