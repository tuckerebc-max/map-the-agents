# roocodeinc/roo-code -- full detail

[Back to orientation](roo-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/roocodeinc/roo-code/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/8d53777eefb26eae.json](../../../wiki/dossiers/roocodeinc/roo-code/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/8d53777eefb26eae.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (4 claim(s))

- [observation/documented] The product offers multiple modes: Code, Architect, Ask, Debug, plus user-defined Custom Modes for team workflows. -- evidence: [README.md#L37-L43](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L37-L43), [README.md#L49-L53](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L49-L53) (`clm_4d9900b517eced7cd9a99a6d62e2fc6cf51d6d57d345d5b8c11431990fc1c60e`)
- [observation/documented] API keys entered by the user are stored locally on the device and are not sent to Roo Code or third parties other than the chosen provider. -- evidence: [PRIVACY.md#L9-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L9-L13) (`clm_c95d13fc6d6aed343908e6b7dfbb03aac1e38fc9cca715d901b52224fb422671`)
- [observation/documented] Anonymous telemetry via PostHog (VS Code machine ID, usage patterns, exception reports) is enabled by default but can be opted out in settings. -- evidence: [PRIVACY.md#L9-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L9-L13), [PRIVACY.md#L23-L25](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L23-L25) (`clm_0e391553f12f7176a2f6c321968ae6160fc933429054b446e80fab6305a02c46`)
- [observation/documented] Commands executed through Roo Code run in the user's local environment, and users can run models locally to avoid third-party data transmission. -- evidence: [PRIVACY.md#L9-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L9-L13), [PRIVACY.md#L23-L25](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L23-L25) (`clm_03de8174369f630fed76fa9f136d65601e355b7d5fe269b64bce50bd2c556c53`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs agents that SettingsView inputs must bind to local cachedState rather than live useExtensionState(), to avoid race conditions until Save is clicked. -- evidence: [AGENTS.md#L5-L5](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/AGENTS.md#L5-L5), [AGENTS.md#L3-L3](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/AGENTS.md#L3-L3) (`clm_d646089ae99f130bd0ba322d94d8c9f33631f139b715ad689032738fc85fda55`)
- [observation/documented] Repository development practice: the security policy asks vulnerability reports be emailed to security@roocode.com with summary, reproduction steps, and logs; reports are acknowledged within 48 hours with fixes targeted within 30 days. -- evidence: [SECURITY.md#L9-L9](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/SECURITY.md#L9-L9), [SECURITY.md#L11-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/SECURITY.md#L11-L13), [SECURITY.md#L15-L15](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/SECURITY.md#L15-L15) (`clm_09469cabc0cfcbd4fe0a29f641cec7be66ee1c2a6f5948a1d63c9031d608c306`)
- [observation/documented] Repository development practice: a progress file records cherry-pick batches onto a pre-AI-SDK codebase, with some PRs deferred as AI-SDK-entangled and a pre-push hook failure worked around using --no-verify after independent verification. -- evidence: [progress.txt#L27-L29](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/progress.txt#L27-L29), [progress.txt#L15-L19](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/progress.txt#L15-L19), [progress.txt#L55-L59](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/progress.txt#L55-L59) (`clm_89c20c41c6e6773ad700a67d2ef1f31ea48f31c63b8a340f970e4ef52611b376`)
- [observation/documented] Repository development practice: the maintenance log reports backend tests (5224), UI tests (1267), and type checks (14/14 packages) all passing after the cherry-pick work. -- evidence: [progress.txt#L49-L52](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/progress.txt#L49-L52) (`clm_31e341d69a27101a418e719302234bd4acbcdb956c21986a7776c0d2d5ae0d98`)

## skills-patterns (1 claim(s))

- [observation/documented] The README advertises support for MCP servers as part of the extension's capabilities. -- evidence: [README.md#L37-L43](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L37-L43) (`clm_56b5440a3b430f3abdc4e06adc821d3f5675ea8135941e3f983bece0e046ec7c`)

## interfaces (1 claim(s))

- [observation/documented] Roo Code is distributed as a VS Code extension via the Visual Studio Code Marketplace. -- evidence: [README.md#L1-L3](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L1-L3) (`clm_e2bf96dcbfab5155dc4ecfdf45f484d840dcb2cfbe922880792dd81e12d12320`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The extension sends prompts and relevant project context to a user-chosen AI model provider such as OpenAI, Anthropic, or OpenRouter. -- evidence: [PRIVACY.md#L9-L13](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/PRIVACY.md#L9-L13) (`clm_1512bb45e905b5c6c31a1bc4e354d5e95205b6b764a4a6e18d924be545942bdb`)

## limitations (1 claim(s))

- [observation/documented] The README states the Roo Code Extension was shut down on May 15th, pointing users to forks such as ZooCode and to Cline as alternatives. -- evidence: [README.md#L68-L69](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L68-L69), [README.md#L66-L66](https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/README.md#L66-L66) (`clm_2b58837bea37df45412541db602373e0007169f60f32641676856318aeef7ea8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

