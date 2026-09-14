# ai-genie/chatgpt-vscode

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e6203fb099f3 @ 8480da848e15b2dd

## Summary (orientation draft, not independently verified)

The evidence is README/CHANGELOG documentation for the Genie ChatGPT VS Code extension, describing its OpenAI/Azure model support, editor and conversation features, settings, and known limitations; no code or contributor-workflow evidence is present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [inference/documented] The repository itself appears intended mainly for documentation, bug reports, and feature requests rather than shipping source code, per the README statement. -- evidence: [README.md#L1-L3](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L1-L3)
- components (1 claim(s)):
  - [observation/documented] Documented features include commit-message generation from git changes, quick fixes for compile-time errors via the Problems window, one-click diffs against suggestions, streaming answers, and Markdown export of conversation history. -- evidence: [README.md#L31-L41](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L31-L41), [README.md#L168-L168](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L168-L168), [README.md#L170-L170](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L170-L170)
- design-choices (3 claim(s)):
  - [observation/documented] The API key is stored in VS Code's Secrets Storage and cannot be read back once stored; users can clear or re-enter it via the Genie: Clear API Key command or the home page. -- evidence: [README.md#L241-L249](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L241-L249), [README.md#L255-L263](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L255-L263)
  - [observation/documented] Telemetry is disabled by default and collects metadata only if both the global telemetry.telemetryLevel setting and genieai.telemetry.disable permit it; the disclaimer states no personally identifiable information is used or stored. -- evidence: [README.md#L298-L303](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L298-L303)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product is a VS Code extension (genieai.chatgpt-vscode) that lets users prompt OpenAI models from within Visual Studio Code, published on the VS Code Marketplace. -- evidence: [README.md#L1-L3](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L1-L3), [README.md#L5-L15](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L5-L15)
  - [observation/documented] Context-menu commands include Genie: Add tests, Find bugs, Optimize, Explain, Add comments, and an ad-hoc custom prompt, each with a configurable prompt prefix; context menu items are grouped under a Genie submenu. -- evidence: [README.md#L215-L237](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L215-L237), [README.md#L77-L80](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L77-L80)
- memory-state (1 claim(s)):
  - [observation/documented] Conversation history is an experimental opt-in feature (genieai.enableConversationHistory) storing conversations only on the user's machine via VS Code's global storage API; the extension can only write new threads, so users may need to delete stored files manually. -- evidence: [README.md#L134-L140](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L134-L140), [CHANGELOG.md#L97-L103](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/CHANGELOG.md#L97-L103)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The extension depends on the user's own OpenAI API key, and also supports Azure OpenAI Service deployments via the genieai.azure.url setting with the model setting matching the deployment's base model. -- evidence: [README.md#L31-L41](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L31-L41), [README.md#L102-L104](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L102-L104), [README.md#L159-L159](https://github.com/ai-genie/chatgpt-vscode/blob/e6203fb099f36dec65df4bbd7401d919259d6722/README.md#L159-L159)
More evidence: [full detail](chatgpt-vscode.detail.md)

Metadata and full claim list: [full detail](chatgpt-vscode.detail.md)
Human notes ([notes](chatgpt-vscode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
