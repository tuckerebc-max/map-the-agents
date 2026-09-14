# wisdomshell/codeshell-vscode

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 00c045b1c08f @ 815a2fd4950a2b23

## Summary (orientation draft, not independently verified)

The evidence consists of bilingual READMEs for codeshell-vscode, a VSCode extension built on the CodeShell LLM that provides code completion, code assistance actions, and multi-turn Q&A, plus instructions for building the plugin and deploying the backing model service.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The companion llama_cpp_for_codeshell project provides a 4-bit quantized model file named codeshell-chat-q4_0.gguf and a server command that serves it as an API on a configurable host and port. -- evidence: [README_EN.md#L73-L75](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L73-L75), [README.md#L75-L75](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L75-L75), [README.md#L77-L79](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L77-L79), [README_EN.md#L28-L28](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L28-L28), [README_EN.md#L71-L71](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L71-L71), [README.md#L28-L28](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L28-L28)
- design-choices (2 claim(s)):
  - [observation/documented] The plugin exposes settings for the model service address, auto-completion toggle and delay, max tokens for completion and Q&A, and a runtime environment option ('CPU with llama.cpp' for the int4 model, 'GPU with TGI toolkit' for the 7B models). -- evidence: [README_EN.md#L111-L116](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L111-L116), [README.md#L117-L122](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L117-L122), [README.md#L124-L124](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L124-L124), [README_EN.md#L118-L118](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L118-L118)
  - [observation/documented] For NVIDIA GPU inference, the documented deployment runs text-generation-inference 1.0.3 in Docker with GPU access, mapping $HOME/models into the container and setting limits such as max-total-tokens 5000 and max-input-length 4096. -- evidence: [README.md#L87-L87](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L87-L87), [README.md#L101-L108](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L101-L108), [README_EN.md#L97-L104](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L97-L104), [README_EN.md#L83-L83](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L83-L83)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: to package the plugin from source, contributors clone the repo, run npm install, then npm exec vsce package to produce a .vsix file, which is installed in VSCode via 'Install from VSIX...'. -- evidence: [README_EN.md#L17-L22](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L17-L22), [README.md#L17-L22](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L17-L22), [README.md#L15-L15](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L15-L15), [README.md#L24-L24](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L24-L24), [README_EN.md#L24-L24](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L24-L24), [README.md#L115-L115](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L115-L115), [README_EN.md#L15-L15](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L15-L15)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product is a VSCode extension acting as an AI coding assistant, supporting languages including Python, Java, C/C++, JavaScript, and Go. -- evidence: [README_EN.md#L5-L5](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L5-L5), [README.md#L5-L5](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L5-L5)
  - [observation/documented] Code completion suggestions can auto-trigger after a configurable 1-3 second input pause, or be triggered manually via Alt+\ on Windows or Option+\ on Mac; suggestions appear in gray and are accepted with Tab. -- evidence: [README_EN.md#L131-L131](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L131-L131), [README.md#L137-L137](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L137-L137), [README.md#L135-L135](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L135-L135), [README_EN.md#L129-L129](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L129-L129)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Running the extension requires Node v18 or above, VSCode 1.68.1 or above, and a running CodeShell model service. -- evidence: [README_EN.md#L9-L11](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L9-L11), [README.md#L9-L11](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L9-L11)
More evidence: [full detail](codeshell-vscode.detail.md)

Metadata and full claim list: [full detail](codeshell-vscode.detail.md)
Human notes ([notes](codeshell-vscode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
