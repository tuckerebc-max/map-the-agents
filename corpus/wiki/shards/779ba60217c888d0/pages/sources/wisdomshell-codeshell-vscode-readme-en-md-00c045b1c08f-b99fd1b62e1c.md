---
access: public
aliases: []
claim_ids:
- clm_24410c82dc843821bd1e76dae5869b4fdbf5daeec40ddd8ecb62b2b4434852b0
- clm_34ccf59363a1b4f3bc50b4b2a9df76d20ed13a5addc1b8aaa02162c180f8c43c
- clm_4bccbe6514a113f079c1b4bfe6dd39af865de323420b8f1b41c0f44a3b5f3d68
- clm_520ecd83c164ad5bebed8ff37ed418b61ebcfa32eb138688be37285a177b21eb
- clm_6c0c04fc39a22653581944da9b00b3db5670f19ebeea6e527c0046a36d2297d5
- clm_82fcba81abae5e3da28e29b39637698f0f0ffa7165ddda8afc1793c02b175485
- clm_87c8d9dd5cd5ed29f9849ff4d837368a7bdd58e9314d2af0a88b49c8ffc71c98
- clm_acf55c869e29503235659df4e0a20ff47a44b4f44e840b6a450f2a328f4cc63f
- clm_aed48b3302654df337823d9b8efacec921cb84cffad88af50ba7f1a5a2248c11
- clm_e3e73bd9eb83980e5603d5eca22931fcbc3b53be6971a46737489af26071925d
- clm_faf190f4b394eec2d1705471f9299da89b24f7da0da93183b3471d0f83d05d13
maturity: draft
page_id: pg_e80c5ea6995d59eda960b99fd1b62e1c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ac6657004e7b571299e3a31adce906e0
title: WisdomShell/codeshell-vscode/README_EN.md @ 00c045b1c08f
updated_at: '2026-09-14T04:31:28Z'
---

# WisdomShell/codeshell-vscode/README_EN.md @ 00c045b1c08f

<!-- rcw:begin owner=source:src_ac6657004e7b571299e3a31adce906e0 block=evidence -->
- The companion llama_cpp_for_codeshell project provides a 4-bit quantized model file named codeshell-chat-q4_0.gguf and a server command that serves it as an API on a configurable host and port. [@claim:clm_24410c82dc843821bd1e76dae5869b4fdbf5daeec40ddd8ecb62b2b4434852b0]
- Code completion suggestions can auto-trigger after a configurable 1-3 second input pause, or be triggered manually via Alt+\ on Windows or Option+\ on Mac; suggestions appear in gray and are accepted with Tab. [@claim:clm_34ccf59363a1b4f3bc50b4b2a9df76d20ed13a5addc1b8aaa02162c180f8c43c]
- Repository development practice: to package the plugin from source, contributors clone the repo, run npm install, then npm exec vsce package to produce a .vsix file, which is installed in VSCode via 'Install from VSIX...'. [@claim:clm_4bccbe6514a113f079c1b4bfe6dd39af865de323420b8f1b41c0f44a3b5f3d68]
- For NVIDIA GPU inference, the documented deployment runs text-generation-inference 1.0.3 in Docker with GPU access, mapping $HOME/models into the container and setting limits such as max-total-tokens 5000 and max-input-length 4096. [@claim:clm_520ecd83c164ad5bebed8ff37ed418b61ebcfa32eb138688be37285a177b21eb]
- The product is a VSCode extension acting as an AI coding assistant, supporting languages including Python, Java, C/C++, JavaScript, and Go. [@claim:clm_6c0c04fc39a22653581944da9b00b3db5670f19ebeea6e527c0046a36d2297d5]
- The extension depends on an external CodeShell model service, which can be served via llama_cpp_for_codeshell for the int4 quantized model or via text-generation-inference (TGI) for CodeShell-7B and CodeShell-7B-Chat. [@claim:clm_82fcba81abae5e3da28e29b39637698f0f0ffa7165ddda8afc1793c02b175485]
- Running the extension requires Node v18 or above, VSCode 1.68.1 or above, and a running CodeShell model service. [@claim:clm_87c8d9dd5cd5ed29f9849ff4d837368a7bdd58e9314d2af0a88b49c8ffc71c98]
- On macOS builds with Metal enabled, runtime exceptions can occur; the documented workaround is adding the -ngl 0 parameter to disable Metal GPU inference, and non-Apple-Silicon Macs should build with Metal disabled. [@claim:clm_acf55c869e29503235659df4e0a20ff47a44b4f44e840b6a450f2a328f4cc63f]
- The Q&A interface supports multi-turn conversation, conversation history, editing and re-asking questions, regenerating answers, interrupting responses, and copying or inserting code blocks from answers. [@claim:clm_aed48b3302654df337823d9b8efacec921cb84cffad88af50ba7f1a5a2248c11]
- Code assistance features include explaining, optimizing, and cleaning code, generating comments or unit tests, and checking code for performance or security issues, invoked by selecting code and using the right-click CodeShell menu. [@claim:clm_e3e73bd9eb83980e5603d5eca22931fcbc3b53be6971a46737489af26071925d]
- The plugin exposes settings for the model service address, auto-completion toggle and delay, max tokens for completion and Q&A, and a runtime environment option ('CPU with llama.cpp' for the int4 model, 'GPU with TGI toolkit' for the 7B models). [@claim:clm_faf190f4b394eec2d1705471f9299da89b24f7da0da93183b3471d0f83d05d13]
<!-- rcw:end owner=source:src_ac6657004e7b571299e3a31adce906e0 block=evidence -->

## Researcher notes

