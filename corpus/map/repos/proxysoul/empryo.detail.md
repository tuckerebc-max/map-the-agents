# proxysoul/empryo -- full detail

[Back to orientation](empryo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/proxysoul/empryo/f771fc238e6426706a28773a9aaa01b967c70342/945eb6c6544cb407.json](../../../wiki/dossiers/proxysoul/empryo/f771fc238e6426706a28773a9aaa01b967c70342/945eb6c6544cb407.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product offers 65+ symbol-level AST editing operations with atomic all-or-nothing rollback and structural edits across 30+ languages, with a typecheck as the gate. -- evidence: [README.md#L53-L56](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L53-L56), [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69) (`clm_d782d826851893b948b1e0bdd2a9f31d84714013714695bd66b66957966293a7`)

## design-choices (1 claim(s))

- [observation/documented] Empryo builds codebase understanding before mutating code: on launch, tree-sitter parses the repo into a live graph of symbols, imports, and call sites ranked by PageRank and git co-change. -- evidence: [README.md#L53-L56](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L53-L56), [README.md#L51-L51](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L51-L51) (`clm_21b796a4bf6d31a5ce6e41b8ee98702675533a89284c8c96e62cb6aea1cf082c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: governance is single-maintainer; architecture changes and public API/SDK changes require opening an issue first, and CODEOWNERS prevents self-merging of PRs touching IP-sensitive paths. -- evidence: [GOVERNANCE.md#L17-L26](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L17-L26), [GOVERNANCE.md#L3-L3](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L3-L3), [GOVERNANCE.md#L36-L36](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L36-L36), [GOVERNANCE.md#L40-L43](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GOVERNANCE.md#L40-L43) (`clm_540ba59c06c8b213f82a74893bba6f3b845dc479f45a6dff28e32ea533cb1b8c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Three surfaces share one code graph: a native desktop app, a full terminal UI, and a headless CLI for scripts and CI. -- evidence: [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69) (`clm_11b155fae820130f6b2e57ed1cff76ebe9979c2126b04a30ad99827e1b97982b`)
- [observation/documented] The terminal UI embeds a real Neovim instance (Ctrl+E toggles focus), with config modes selectable via /nvim-config (auto, user, default, none). -- evidence: [GETTING_STARTED.md#L132-L134](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L132-L134), [GETTING_STARTED.md#L25-L25](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L25-L25), [GETTING_STARTED.md#L142-L142](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L142-L142), [GETTING_STARTED.md#L128-L128](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L128-L128), [GETTING_STARTED.md#L144-L149](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L144-L149) (`clm_dc4a6bb564069f27c0d5319a2da08da825a1957874b72f846fab1e3a7dac4c62`)

## memory-state (2 claim(s))

- [observation/documented] A SQLite-backed memory system stores decisions, patterns, and preferences across conversations, with write scope configurable to session, project, or global and memories injected into the system prompt. -- evidence: [GETTING_STARTED.md#L270-L271](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L270-L271), [GETTING_STARTED.md#L268-L268](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L268-L268) (`clm_fcb6c2beae5b10a5987a3aa1cedfc2527b715afdfa144f0b361c969edf116b18`)
- [observation/documented] Every prompt creates a git checkpoint ('time machine'), letting users rewind code and conversation together to any turn. -- evidence: [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69) (`clm_93b032eebe4dc60c8a58ea9bd5727dd46e4cdf57e03e718bcba44e8326b77175`)

## orchestration (1 claim(s))

- [observation/documented] A task router assigns models to ten routable roles (e.g. spark for read-only scouting, ember for code edits, verify for review), configurable per tab, per project, or globally, with custom agents definable. -- evidence: [README.md#L60-L69](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L60-L69), [README.md#L77-L77](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L77-L77), [GETTING_STARTED.md#L159-L168](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L159-L168), [README.md#L81-L85](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L81-L85), [README.md#L73-L73](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L73-L73) (`clm_e8e585d9f5405bcd4ce7afe08b501f314913f8a68cbb7687cd53fa5ef4e4f0f1`)

## tools-permissions (1 claim(s))

- [observation/documented] A privacy feature lets users block file patterns (e.g. .env, secrets/**) via /privacy add; the agent then refuses to read, display, or access matching files even through shell commands. -- evidence: [GETTING_STARTED.md#L292-L292](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L292-L292), [GETTING_STARTED.md#L285-L285](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L285-L285), [GETTING_STARTED.md#L287-L290](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L287-L290) (`clm_bb92a300bee440aec290092a449a3b1a5f28f2f8b55a49f2ec8126820988591e`)

## evaluation (1 claim(s))

- [observation/documented] The README reports head-to-head benchmarks against pi on bug-fixing tasks (e.g. 8/9 vs 7/9 bugs fixed, 28% lower cost, 57% faster), with methodology and a reproduction repo at proxysoul/pi-vs-empryo-bench. -- evidence: [README.md#L98-L98](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L98-L98), [README.md#L89-L89](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L89-L89), [README.md#L91-L96](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L91-L96) (`clm_1ea081c8d8f82949a172903bc4b5b471f3eff431a7c530630f335d28997d2ceb`)

## dependencies (2 claim(s))

- [observation/documented] Source/npm installs require Bun (>= 1.0) rather than Node.js; Neovim >= 0.11 is needed for the embedded editor; a Nerd Font is needed for icons. -- evidence: [GETTING_STARTED.md#L42-L42](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L42-L42), [GETTING_STARTED.md#L21-L21](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L21-L21), [GETTING_STARTED.md#L7-L7](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L7-L7), [GETTING_STARTED.md#L38-L38](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L38-L38), [GETTING_STARTED.md#L11-L11](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/GETTING_STARTED.md#L11-L11) (`clm_65bb86ae4149ee01a598b845f4810bd16c8906b4a3ff354f060fff5d2bfe939b`)
- [observation/documented] The agent supports 22 LLM providers including Anthropic, OpenAI, Google, Groq, DeepSeek, and Bedrock, plus OpenAI-compatible endpoints and fully local Ollama/LM Studio; an llmgateway provider ships built in. -- evidence: [README.md#L102-L102](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L102-L102), [BACKERS.md#L18-L32](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/BACKERS.md#L18-L32), [README.md#L73-L73](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L73-L73), [README.md#L131-L131](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/README.md#L131-L131), [BACKERS.md#L77-L77](https://github.com/proxysoul/Empryo/blob/f771fc238e6426706a28773a9aaa01b967c70342/BACKERS.md#L77-L77) (`clm_61a3f5fdf3ef12024c7679ea81d7e75b70628f52267a52f7c64c0a252618a4fa`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

