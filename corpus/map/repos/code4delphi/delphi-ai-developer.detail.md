# code4delphi/delphi-ai-developer -- full detail

[Back to orientation](delphi-ai-developer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/code4delphi/delphi-ai-developer/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/2d3e54b5de481a65.json](../../../wiki/dossiers/code4delphi/delphi-ai-developer/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/2d3e54b5de481a65.json)

## specifications (2 claim(s))

- [observation/documented] A Delphi IDE plugin, inspired by GitHub Copilot, that adds AI interaction to the Delphi IDE using the OpenAI, Gemini, Mistral and Groq APIs plus offline AI support. -- evidence: [README.md#L2-L2](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L2-L2) (`clm_9dc938ff40ea5e4abf375ca5a25b751edb1e99b046887257495ff436f5b3c5bc`)
- [observation/documented] The plugin aims to assist with generating and refactoring code, and offers suggestions in the IDE plus user-defined predefined questions to speed up searches. -- evidence: [README.md#L4-L4](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L4-L4), [README.md#L6-L6](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L6-L6) (`clm_0eefad283aa7d81b7fe44994c4ed6e7e3b9041f36e0c9721ea8440423d5372cf`)

## components (2 claim(s))

- [observation/documented] A code completion feature can be toggled on/off, configured with a default AI, suggestion highlight color, and a shortcut (default Alt+Enter, requiring IDE restart); Tab accepts the suggestion. -- evidence: [README.md#L76-L78](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L76-L78), [README.md#L66-L66](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L66-L66), [README.md#L70-L74](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L70-L74) (`clm_fa9c900706e0b7024505269586b0a09f8507374388a8ea842ffa0cfac8a19c90`)
- [observation/documented] A database chat lets users register databases, generate a structure reference, ask questions, execute the returned SQL, and view, copy or export results in a grid. -- evidence: [README.md#L119-L136](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L119-L136), [README.md#L104-L105](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L104-L105), [README.md#L107-L109](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L107-L109) (`clm_28646df33be5940fac2ee4d31d371e03f5f8e2601d30254bdbd663e8f0fd5e95`)

## design-choices (2 claim(s))

- [observation/documented] Both chats can optionally include the current unit's source code as prompt context; if code is selected only the selection is used, otherwise the entire unit. -- evidence: [README.md#L119-L136](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L119-L136), [README.md#L87-L99](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L87-L99) (`clm_cfb0d9154ee90631def244b05f9d87c8cb19f30fb2adb98d17b34f4186b23323`)
- [observation/documented] Users can set default prompts sent with every request to improve response quality, and can toggle modes where the AI returns only code or only SQL without comments. -- evidence: [README.md#L119-L136](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L119-L136), [README.md#L44-L47](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L44-L47), [README.md#L70-L74](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L70-L74), [README.md#L87-L99](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L87-L99) (`clm_7465a5ec90899b9967a23e91eb936bd2942bae53120aa913e382611f3be9b78c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are welcomed via pull requests or by opening an issue in the repository. -- evidence: [README.md#L161-L161](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L161-L161) (`clm_74fe267cbc997e95a6d0d45a7be5e70783db5427b95750cceed7e5a76f76c021`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Installation is done by opening Package\DelphiAIDeveloper.dpk in Delphi and installing the package; afterwards an "AI Developer" item appears in the IDE's main menu. -- evidence: [README.md#L24-L24](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L24-L24), [README.md#L29-L29](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L29-L29), [README.md#L34-L34](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L34-L34) (`clm_72a231863161d9de5b6eb6c359d383f0cdca74f27d716e3cee3e844eb368927a`)
- [observation/documented] An AI chat panel is opened via the "AI Developer" menu or Ctrl+Shift+Alt+A, with prompt and response fields, pre-registered questions, and actions to insert selected text at the cursor, create a new unit, or copy text. -- evidence: [README.md#L84-L85](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L84-L85), [README.md#L87-L99](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L87-L99) (`clm_ff99b12755c1ec73e29cf6156a4d21fa90bd7abd49be9254cf62c683ea13d381`)

## memory-state (1 claim(s))

- [observation/documented] Database structure metadata (database name, table names, field names, types, sizes) is stored locally in a JSON file on the user's computer, not exposed to any server. -- evidence: [LGPD.md#L14-L14](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/LGPD.md#L14-L14) (`clm_607423b8774f7344680b64d49f3631a73ae27ddad5ac50bdd98f918cfe51da69`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Offline AI relies on Ollama: users install Ollama, pick a model from its library, run "ollama run <name_model>", then configure the plugin's AI off-Line tab. -- evidence: [README.md#L142-L149](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L142-L149) (`clm_765bca04a51544011d098dd1f8066fcf33271c4ad98fd8bc1f58d6caff593b6b`)
- [observation/documented] Online AI configuration offers a choice among Gemini, ChatGPT (OpenAI) and Groq APIs, with model selection, a key-generation link, and an API key field; Gemini and Groq are noted as free. -- evidence: [README.md#L53-L53](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L53-L53), [README.md#L55-L56](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L55-L56), [README.md#L58-L60](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/README.md#L58-L60) (`clm_19958d98d5b56af9fecc74a02ba18c1f2501edebf7117bcaf3131834eef0fe5c`)

## limitations (1 claim(s))

- [observation/documented] Per its LGPD statement, the plugin sends code snippets and database structure to AI APIs but claims not to store user information on external servers and not to access or send database data itself. -- evidence: [LGPD.md#L9-L11](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/LGPD.md#L9-L11), [LGPD.md#L14-L14](https://github.com/Code4Delphi/Delphi-AI-Developer/blob/3d979ffc33a80551d4515d6d1fb8e28f6eae4ecc/LGPD.md#L14-L14) (`clm_260c0537f9c89b6ae9e57197566c8cd48d49986cc1dd39613bd61cb08cacd56a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

