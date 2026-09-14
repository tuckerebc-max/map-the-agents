# roocodeinc/roo-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b867ec914575 @ 8d53777eefb26eae

## Summary (orientation draft, not independently verified)

The snapshot is the Roo Code VS Code extension repository at a commit whose README announces the extension was shut down on May 15th, with a privacy policy, security policy, contributor guidance, and a progress file documenting cherry-pick work. Evidence covers product description, privacy/data handling, and repository maintenance activity; no code internals are shown.

## Source coverage

Source coverage (partial): 5 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (4 claim(s)):
  - [observation/documented] The product offers multiple modes: Code, Architect, Ask, Debug, plus user-defined Custom Modes for team workflows. -- evidence: [README.md#L37-L43](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L37-L43), [README.md#L49-L53](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L49-L53)
  - [observation/documented] API keys entered by the user are stored locally on the device and are not sent to Roo Code or third parties other than the chosen provider. -- evidence: [PRIVACY.md#L9-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L9-L13)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs agents that SettingsView inputs must bind to local cachedState rather than live useExtensionState(), to avoid race conditions until Save is clicked. -- evidence: [AGENTS.md#L5-L5](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/AGENTS.md#L5-L5), [AGENTS.md#L3-L3](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/AGENTS.md#L3-L3)
  - [observation/documented] Repository development practice: the security policy asks vulnerability reports be emailed to security@roocode.com with summary, reproduction steps, and logs; reports are acknowledged within 48 hours with fixes targeted within 30 days. -- evidence: [SECURITY.md#L9-L9](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/SECURITY.md#L9-L9), [SECURITY.md#L11-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/SECURITY.md#L11-L13), [SECURITY.md#L15-L15](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/SECURITY.md#L15-L15)
- skills-patterns (1 claim(s)):
  - [observation/documented] The README advertises support for MCP servers as part of the extension's capabilities. -- evidence: [README.md#L37-L43](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L37-L43)
- interfaces (1 claim(s)):
  - [observation/documented] Roo Code is distributed as a VS Code extension via the Visual Studio Code Marketplace. -- evidence: [README.md#L1-L3](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L1-L3)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The extension sends prompts and relevant project context to a user-chosen AI model provider such as OpenAI, Anthropic, or OpenRouter. -- evidence: [PRIVACY.md#L9-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L9-L13)
- limitations (1 claim(s)):
  - [observation/documented] The README states the Roo Code Extension was shut down on May 15th, pointing users to forks such as ZooCode and to Cline as alternatives. -- evidence: [README.md#L68-L69](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L68-L69), [README.md#L66-L66](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L66-L66)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](roo-code.detail.md) for every claim.)

Metadata and full claim list: [full detail](roo-code.detail.md)
Human notes ([notes](roo-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
