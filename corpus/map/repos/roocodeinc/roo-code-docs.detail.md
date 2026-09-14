# roocodeinc/roo-code-docs -- full detail

[Back to orientation](roo-code-docs.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/roocodeinc/roo-code-docs/a676c4173ae60348095efaebfd1292a9617622c0/4f3c03b6e158e322.json](../../../wiki/dossiers/roocodeinc/roo-code-docs/a676c4173ae60348095efaebfd1292a9617622c0/4f3c03b6e158e322.json)

## specifications (1 claim(s))

- [observation/documented] Roo Code is described as an AI-powered suite of coding products that uses large language models to understand user requests and translate them into actions. -- evidence: [docs/faq.md#L29-L29](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L29-L29), [docs/faq.md#L25-L25](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L25-L25) (`clm_a6ac58067ab16fa74de44a386f8ca07adb977585736be1dd6babf1ff6c85bd14`)

## components (1 claim(s))

- [observation/documented] The product ships in two forms: a VS Code Extension working locally in the IDE, and Roo Code Cloud Agents described as an autonomous AI development team reachable via channels like Slack and GitHub. -- evidence: [docs/index.mdx#L24-L26](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/index.mdx#L24-L26) (`clm_88f02a9c01a30d417685a4af40bc2b966f6dec2ca5fccdfcb5959fde35836da0`)

## design-choices (1 claim(s))

- [observation/documented] Roo Code offers persona-based modes (Code, Architect, Ask, Debug) plus user-created Custom Modes, switchable via a dropdown or the '/' command. -- evidence: [docs/faq.md#L106-L106](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L106-L106), [docs/faq.md#L98-L102](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L98-L102), [docs/faq.md#L96-L96](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L96-L96) (`clm_23f9032d6ebdc270b86603ebc8f35ef7352edf509ca9a8729da43edf4f2c0cea`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the docs site is built with Docusaurus; contributors install dependencies with pnpm install and run a local dev server with pnpm start, which live-reloads changes without restart. -- evidence: [README.md#L17-L17](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L17-L17), [README.md#L3-L3](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L3-L3), [README.md#L7-L9](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L7-L9), [README.md#L13-L15](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L13-L15) (`clm_5a704c7963593c0df310d27269995d10059d8147b271aafb063bc99081063aa6`)
- [observation/documented] Repository development practice: the README displays an Apache 2.0 license badge linking to the LICENSE file. -- evidence: [README.md#L21-L21](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/README.md#L21-L21) (`clm_10f9676283b42eb4c3dbe92d72be0cc83467c21bcbfb6e65964a2e040f77c12e`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are SKILL.md files with required name/description frontmatter that Roo loads on demand via progressive disclosure: metadata is indexed at startup, full instructions load only when a request matches, and bundled resources are discovered on demand. -- evidence: [docs/features/skills.mdx#L60-L60](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L60-L60), [docs/features/skills.mdx#L58-L58](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L58-L58), [docs/features/skills.mdx#L104-L104](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L104-L104), [docs/features/skills.mdx#L14-L14](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L14-L14), [docs/features/skills.mdx#L62-L62](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L62-L62), [docs/features/skills.mdx#L230-L233](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L230-L233) (`clm_0524295c1dd07c641aa0e4d88b3a9d3b5304e7ecd293f6c855df15cfbe92fe3b`)
- [observation/documented] Skills live in .roo/skills/ or .agents/skills/ directories (global or project), support mode-specific variants like skills-code/, and follow an eight-level override priority where project beats global and .roo beats .agents. -- evidence: [docs/features/skills.mdx#L219-L219](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L219-L219), [docs/features/skills.mdx#L208-L208](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L208-L208), [docs/features/skills.mdx#L183-L186](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L183-L186), [docs/features/skills.mdx#L75-L75](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L75-L75), [docs/features/skills.mdx#L210-L217](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L210-L217), [docs/features/skills.mdx#L88-L88](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/features/skills.mdx#L88-L88) (`clm_a9959b9dccbda454e98007046a26f06f21fc3c0547c01735b36acf2481ac410d`)

## interfaces (1 claim(s))

- [observation/documented] The Extension exposes a chat panel (Kangaroo icon) where tasks are typed, supports '@' context mentions for files, folders, and problems, and offers error diagnostics export with basic and detailed options. -- evidence: [docs/reporting-errors.md#L20-L20](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/reporting-errors.md#L20-L20), [docs/reporting-errors.md#L32-L35](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/reporting-errors.md#L32-L35), [docs/faq.md#L112-L112](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L112-L112), [docs/reporting-errors.md#L39-L43](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/reporting-errors.md#L39-L43), [docs/faq.md#L93-L93](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L93-L93) (`clm_da81f65c1a1a6dc7e561d3af81a7b02a1e40ced407a8a35f5766a0f6b9cefaf7`)

## memory-state (1 claim(s))

- [observation/documented] Codebase Indexing builds a semantic search index of the project using AI embeddings, requiring an OpenAI API key for embeddings and a Qdrant vector database for storage; initial indexing is the most expensive step with cheaper incremental updates. -- evidence: [docs/faq.md#L158-L158](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L158-L158), [docs/faq.md#L154-L154](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L154-L154) (`clm_ad76642e27e43a267cfe65564ead533f967bbc69e0ab7207c0e60dee7710baa0`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Roo Code can read/write project files, execute shell commands, browse the web if enabled, and use external tools via MCP; users are prompted to approve or reject each tool use, with optional auto-approval settings. -- evidence: [docs/faq.md#L31-L34](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L31-L34), [docs/faq.md#L136-L136](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L136-L136), [docs/faq.md#L109-L109](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L109-L109), [docs/faq.md#L120-L120](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L120-L120) (`clm_04b6e6bcbce6196afe2db6dc3c60e25934e6154c9f8ee9196c069db90c17b791`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Roo Code relies on external LLM inference providers such as Anthropic, OpenAI, OpenRouter, and Requesty, requiring users to obtain API keys; the Roo Code Router is offered as an alternative that needs no API key. -- evidence: [docs/faq.md#L83-L83](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L83-L83), [docs/faq.md#L56-L57](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L56-L57) (`clm_1d98e3d1b67a3ef5804a63eb48960974cff0d5ebfe18f7c9a8de7f2261b31f85`)
- [observation/documented] Local model use is supported via Ollama and LM Studio, and the FAQ states offline use is possible when a local model is used. -- evidence: [docs/faq.md#L143-L143](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L143-L143), [docs/faq.md#L86-L86](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L86-L86) (`clm_1ba5a56949fe34e5779ab36b91775b653cb9ce44b8bf69815ada8f2ae5013f83`)

## limitations (2 claim(s))

- [observation/documented] The docs carry a prominent notice that all Roo Code products (Extension, Cloud, and Router) will be shut down on May 15, 2026, with refunds of unused balances and recommended alternatives. -- evidence: [docs/index.mdx#L16-L18](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/index.mdx#L16-L18) (`clm_f84053df266c08c912ce3e7f0ba4d101fcd159e9c4c476ae4c54d7d01dc5dcea`)
- [observation/documented] Documented caveats include that Roo Code can make mistakes and changes should be reviewed, and that markdown write failures can occur when VS Code extensions or settings (e.g., format-on-save, markdown preview) interfere with file editing. -- evidence: [docs/faq.md#L63-L65](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L63-L65), [docs/faq.md#L182-L182](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L182-L182), [docs/faq.md#L184-L187](https://github.com/RooCodeInc/Roo-Code-Docs/blob/a676c4173ae60348095efaebfd1292a9617622c0/docs/faq.md#L184-L187) (`clm_13349ec979372deeb9bdfd0a78f945550e3b6a4693b06120a5548c5a179d5569`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

