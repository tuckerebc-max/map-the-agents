# wisdomshell/codeshell-vscode -- full detail

[Back to orientation](codeshell-vscode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/wisdomshell/codeshell-vscode/00c045b1c08fea8df7adcfa354b443ecdc1fa429/815a2fd4950a2b23.json](../../../wiki/dossiers/wisdomshell/codeshell-vscode/00c045b1c08fea8df7adcfa354b443ecdc1fa429/815a2fd4950a2b23.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The companion llama_cpp_for_codeshell project provides a 4-bit quantized model file named codeshell-chat-q4_0.gguf and a server command that serves it as an API on a configurable host and port. -- evidence: [README_EN.md#L73-L75](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L73-L75), [README.md#L75-L75](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L75-L75), [README.md#L77-L79](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L77-L79), [README_EN.md#L28-L28](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L28-L28), [README_EN.md#L71-L71](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L71-L71), [README.md#L28-L28](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L28-L28) (`clm_24410c82dc843821bd1e76dae5869b4fdbf5daeec40ddd8ecb62b2b4434852b0`)

## design-choices (2 claim(s))

- [observation/documented] The plugin exposes settings for the model service address, auto-completion toggle and delay, max tokens for completion and Q&A, and a runtime environment option ('CPU with llama.cpp' for the int4 model, 'GPU with TGI toolkit' for the 7B models). -- evidence: [README_EN.md#L111-L116](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L111-L116), [README.md#L117-L122](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L117-L122), [README.md#L124-L124](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L124-L124), [README_EN.md#L118-L118](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L118-L118) (`clm_faf190f4b394eec2d1705471f9299da89b24f7da0da93183b3471d0f83d05d13`)
- [observation/documented] For NVIDIA GPU inference, the documented deployment runs text-generation-inference 1.0.3 in Docker with GPU access, mapping $HOME/models into the container and setting limits such as max-total-tokens 5000 and max-input-length 4096. -- evidence: [README.md#L87-L87](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L87-L87), [README.md#L101-L108](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L101-L108), [README_EN.md#L97-L104](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L97-L104), [README_EN.md#L83-L83](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L83-L83) (`clm_520ecd83c164ad5bebed8ff37ed418b61ebcfa32eb138688be37285a177b21eb`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: to package the plugin from source, contributors clone the repo, run npm install, then npm exec vsce package to produce a .vsix file, which is installed in VSCode via 'Install from VSIX...'. -- evidence: [README_EN.md#L17-L22](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L17-L22), [README.md#L17-L22](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L17-L22), [README.md#L15-L15](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L15-L15), [README.md#L24-L24](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L24-L24), [README_EN.md#L24-L24](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L24-L24), [README.md#L115-L115](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L115-L115), [README_EN.md#L15-L15](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L15-L15) (`clm_4bccbe6514a113f079c1b4bfe6dd39af865de323420b8f1b41c0f44a3b5f3d68`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product is a VSCode extension acting as an AI coding assistant, supporting languages including Python, Java, C/C++, JavaScript, and Go. -- evidence: [README_EN.md#L5-L5](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L5-L5), [README.md#L5-L5](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L5-L5) (`clm_6c0c04fc39a22653581944da9b00b3db5670f19ebeea6e527c0046a36d2297d5`)
- [observation/documented] Code completion suggestions can auto-trigger after a configurable 1-3 second input pause, or be triggered manually via Alt+\ on Windows or Option+\ on Mac; suggestions appear in gray and are accepted with Tab. -- evidence: [README_EN.md#L131-L131](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L131-L131), [README.md#L137-L137](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L137-L137), [README.md#L135-L135](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L135-L135), [README_EN.md#L129-L129](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L129-L129) (`clm_34ccf59363a1b4f3bc50b4b2a9df76d20ed13a5addc1b8aaa02162c180f8c43c`)
- [observation/documented] Code assistance features include explaining, optimizing, and cleaning code, generating comments or unit tests, and checking code for performance or security issues, invoked by selecting code and using the right-click CodeShell menu. -- evidence: [README.md#L147-L147](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L147-L147), [README.md#L143-L145](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L143-L145), [README_EN.md#L141-L141](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L141-L141), [README_EN.md#L137-L139](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L137-L139) (`clm_e3e73bd9eb83980e5603d5eca22931fcbc3b53be6971a46737489af26071925d`)
- [observation/documented] The Q&A interface supports multi-turn conversation, conversation history, editing and re-asking questions, regenerating answers, interrupting responses, and copying or inserting code blocks from answers. -- evidence: [README.md#L162-L162](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L162-L162), [README_EN.md#L156-L156](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L156-L156), [README.md#L153-L158](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L153-L158), [README_EN.md#L147-L152](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L147-L152) (`clm_aed48b3302654df337823d9b8efacec921cb84cffad88af50ba7f1a5a2248c11`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Running the extension requires Node v18 or above, VSCode 1.68.1 or above, and a running CodeShell model service. -- evidence: [README_EN.md#L9-L11](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L9-L11), [README.md#L9-L11](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L9-L11) (`clm_87c8d9dd5cd5ed29f9849ff4d837368a7bdd58e9314d2af0a88b49c8ffc71c98`)
- [observation/documented] The extension depends on an external CodeShell model service, which can be served via llama_cpp_for_codeshell for the int4 quantized model or via text-generation-inference (TGI) for CodeShell-7B and CodeShell-7B-Chat. -- evidence: [README.md#L83-L83](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L83-L83), [README.md#L75-L75](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L75-L75), [README_EN.md#L28-L28](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L28-L28), [README_EN.md#L79-L79](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L79-L79), [README_EN.md#L71-L71](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L71-L71), [README.md#L28-L28](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L28-L28) (`clm_82fcba81abae5e3da28e29b39637698f0f0ffa7165ddda8afc1793c02b175485`)

## limitations (1 claim(s))

- [observation/documented] On macOS builds with Metal enabled, runtime exceptions can occur; the documented workaround is adding the -ngl 0 parameter to disable Metal GPU inference, and non-Apple-Silicon Macs should build with Metal disabled. -- evidence: [README.md#L50-L50](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L50-L50), [README_EN.md#L50-L50](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L50-L50), [README.md#L81-L81](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README.md#L81-L81), [README_EN.md#L77-L77](https://github.com/WisdomShell/codeshell-vscode/blob/00c045b1c08fea8df7adcfa354b443ecdc1fa429/README_EN.md#L77-L77) (`clm_acf55c869e29503235659df4e0a20ff47a44b4f44e840b6a450f2a328f4cc63f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

