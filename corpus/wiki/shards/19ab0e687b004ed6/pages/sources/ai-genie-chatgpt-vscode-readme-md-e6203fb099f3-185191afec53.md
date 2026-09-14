---
access: public
aliases: []
claim_ids:
- clm_27eba0f75ea9af279b998f1eefb6a2297c3cdcbc61d2a188e859b5d9f8f51ae6
- clm_2a6edf47f7fb97cc9dbba4dc19c36b24b272edbf4d248ed1e5790e66d2c824ae
- clm_300cdad67a39eef5b24c39357399e3eb385b5c00e9bebf84937e139889eb0b80
- clm_3241ab0cad504d7a6ac2e27ecb190f424a3f55a0e765c67aa38e868dd320eb19
- clm_5eaa80aee3b46cfe2230e23adeb13e334c396a088967faa7dfe7e0c0b03d9204
- clm_67d2b6597c7180e01f35ec39d28c260d3e4f98e83ca114331691fe2a460f942a
- clm_95a317eabf208e1c90462384b79194a43fe30bfb2760141a35e1430e2e5be22d
- clm_9c338f52bcb44562450bce529df577f429ab7f1b5f03beef9497cf66e827050e
- clm_a2888f2a2f27148c26ee87e23f89803e01517159cb2f0f0f4d2fc9a48a378387
- clm_c28b828f73da38c2a1f2ada7da680294299fa5af8ca9560a9f0a48dcf18f2a3b
- clm_c7c52eb299ce27af6f96c66234aa6148075316f593cd23f0cb69c9f7e1d7c8d8
- clm_fb45a5f9bc1f938638bdc83d64c0967c4ae7b6189cecd6192ad517e1c5eb9038
maturity: draft
page_id: pg_d9846f9ac917577dac3f185191afec53
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_749e95854f075248802873e9e1307563
title: ai-genie/chatgpt-vscode/README.md @ e6203fb099f3
updated_at: '2026-09-14T03:31:51Z'
---

# ai-genie/chatgpt-vscode/README.md @ e6203fb099f3

<!-- rcw:begin owner=source:src_749e95854f075248802873e9e1307563 block=evidence -->
- The repository itself appears intended mainly for documentation, bug reports, and feature requests rather than shipping source code, per the README statement. [@claim:clm_27eba0f75ea9af279b998f1eefb6a2297c3cdcbc61d2a188e859b5d9f8f51ae6]
- Other commands include Clear API Key, Show conversations, Start a new chat, Ask anything, Reset session, Clear conversation, Export conversation, and Focus on Genie View; keyboard shortcuts can be assigned via VS Code's keybindings menu. [@claim:clm_2a6edf47f7fb97cc9dbba4dc19c36b24b272edbf4d248ed1e5790e66d2c824ae]
- The API key is stored in VS Code's Secrets Storage and cannot be read back once stored; users can clear or re-enter it via the Genie: Clear API Key command or the home page. [@claim:clm_300cdad67a39eef5b24c39357399e3eb385b5c00e9bebf84937e139889eb0b80]
- The editor view historically used text-davinci-003 by design because it was said to be the only model guaranteeing a code response without conversational context, though a later release states the editor view now uses the user's selected model. [@claim:clm_3241ab0cad504d7a6ac2e27ecb190f424a3f55a0e765c67aa38e868dd320eb19]
- Conversation history is an experimental opt-in feature (genieai.enableConversationHistory) storing conversations only on the user's machine via VS Code's global storage API; the extension can only write new threads, so users may need to delete stored files manually. [@claim:clm_5eaa80aee3b46cfe2230e23adeb13e334c396a088967faa7dfe7e0c0b03d9204]
- Supported models documented include gpt-4o and other 2024 models, o1-mini and o1-preview, GPT-4 Turbo and GPT-3.5 Turbo variants, with some older models deprecated; o1 models reportedly have usage-tier limitations. [@claim:clm_67d2b6597c7180e01f35ec39d28c260d3e4f98e83ca114331691fe2a460f942a]
- Documented features include commit-message generation from git changes, quick fixes for compile-time errors via the Problems window, one-click diffs against suggestions, streaming answers, and Markdown export of conversation history. [@claim:clm_95a317eabf208e1c90462384b79194a43fe30bfb2760141a35e1430e2e5be22d]
- The product is a VS Code extension (genieai.chatgpt-vscode) that lets users prompt OpenAI models from within Visual Studio Code, published on the VS Code Marketplace. [@claim:clm_9c338f52bcb44562450bce529df577f429ab7f1b5f03beef9497cf66e827050e]
- The extension depends on the user's own OpenAI API key, and also supports Azure OpenAI Service deployments via the genieai.azure.url setting with the model setting matching the deployment's base model. [@claim:clm_a2888f2a2f27148c26ee87e23f89803e01517159cb2f0f0f4d2fc9a48a378387]
- Telemetry is disabled by default and collects metadata only if both the global telemetry.telemetryLevel setting and genieai.telemetry.disable permit it; the disclaimer states no personally identifiable information is used or stored. [@claim:clm_c28b828f73da38c2a1f2ada7da680294299fa5af8ca9560a9f0a48dcf18f2a3b]
- Context-menu commands include Genie: Add tests, Find bugs, Optimize, Explain, Add comments, and an ad-hoc custom prompt, each with a configurable prompt prefix; context menu items are grouped under a Genie submenu. [@claim:clm_c7c52eb299ce27af6f96c66234aa6148075316f593cd23f0cb69c9f7e1d7c8d8]
- Documented limitations include HTTP 429 errors from rate limits or insufficient quota, HTTP 400 when conversations exceed model context or settings are invalid, GPT-4 requiring separate API access, and no guarantee the extension works without issues. [@claim:clm_fb45a5f9bc1f938638bdc83d64c0967c4ae7b6189cecd6192ad517e1c5eb9038]
<!-- rcw:end owner=source:src_749e95854f075248802873e9e1307563 block=evidence -->

## Researcher notes

