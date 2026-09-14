# zhikunqingtao/zhikuncode -- full detail

[Back to orientation](zhikuncode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zhikunqingtao/zhikuncode/931a9beebf21bd404a6332b96fdb5035930637ae/c7992362e1b91e4b.json](../../../wiki/dossiers/zhikunqingtao/zhikuncode/931a9beebf21bd404a6332b96fdb5035930637ae/c7992362e1b91e4b.json)

## specifications (1 claim(s))

- [observation/documented] The README describes ZhikunCode as an open-source AI programming assistant deployed once and controllable entirely from a browser, with multi-agent collaboration, Docker self-hosting, direct connections to domestic Chinese LLM providers, and what it calls a deep security architecture. -- evidence: [README.md#L3-L7](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L3-L7) (`clm_a70e6822e385ce9d3c5eb8b2c4eb30ae29da878f792680000a6bec228c9a9711`)

## components (1 claim(s))

- [observation/documented] Documentation describes a three-tier architecture: a Java 21/Spring Boot backend handling core orchestration, LLM routing, and the authorization gateway; a React/TypeScript frontend for the interactive UI; and an optional Python/FastAPI service for code analysis and MCP bridging. -- evidence: [README.md#L534-L538](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L534-L538), [README.md#L514-L514](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L514-L514) (`clm_7977a466349508f09e7091b0507a2e17bbcdbd95b8a97eddd92fa07842ea42e6`)

## design-choices (1 claim(s))

- [observation/documented] Documentation states that on a 402 quota-exceeded or 404 model-unavailable response, the system automatically cools that key down for 15 minutes and switches to the next configured API key. -- evidence: [README.md#L356-L357](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L356-L357) (`clm_0e69d18a33e2cdd269485b7c25ae19c899962346c4cd50571a19124cf2675735`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (1 claim(s))

- [observation/documented] The README describes a six-level context-compression cascade (Snip, MicroCompact, ContextCollapse, AutoCompact, CollapseDrain, ReactiveCompact) intended to keep sessions within the context window, with a documented two-stage CollapseDrain/ReactiveCompact recovery path for large sessions. -- evidence: [README.md#L453-L456](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L453-L456) (`clm_cf1be386b8c04cdab5abe264204053ccdc0b441eafeab0e42fb591740c28da0c`)

## orchestration (1 claim(s))

- [observation/documented] The README lists three multi-agent collaboration modes: Team for fixed role division, Swarm for dynamic negotiation, and SubAgent for master/subordinate delegation. -- evidence: [README.md#L120-L141](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L120-L141) (`clm_e7e501fd2cdf4edbfe1ee3f688e49ebd796e05d2c59bd3a3b60320143e8732b4`)

## tools-permissions (3 claim(s))

- [observation/documented] Documentation describes a unified authorization pipeline where core tools pass through a Tool Gateway: input normalization, an Operation Analyzer risk/resource check, a system-invariant check, a RUN/SESSION/WORKSPACE grant match or persistent-permission prompt, a pre-execution recheck, and a structured audit of results; high-risk operations are limited to single-use authorization. -- evidence: [README.md#L120-L141](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L120-L141) (`clm_0ae4a2b69195d13ba20965d3d65e1ce101d0141c47f552bec729041418db2cf0`)
- [observation/documented] Documentation states MCP tools must pass three independent checks before use - registry whitelist, a per-service enable toggle, and credential availability - and that of the preset MCP services, thirteen lower-frequency or higher-risk ones default to disabled while a smaller default-enabled set covers web search, maps, and image/video generation. -- evidence: [README.md#L412-L412](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L412-L412), [README.md#L379-L379](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L379-L379) (`clm_0098f537af91e14235dadc780e9896970d1fdc0d3a78534c87711bd95833c5d3`)
- [observation/documented] Documentation states that referencing a local file when connected directly adds only its path to the prompt without uploading content, but doing so over a remote or proxied connection instead uploads the file as a permanent public OSS object and requires OSS to be configured first. -- evidence: [README.md#L120-L141](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L120-L141) (`clm_7a1621f582660cf19c0e826b30472346b732baa66e3e26df82507c75f9bde81c`)

## evaluation (1 claim(s))

- [observation/documented] The README reports ZhikunCode completed the SWE-bench Lite benchmark (300 instances, pass@1) against an official harness, with a resolve rate of 168/300 (56.0%) and a patch-generation rate of 284/300 (94.7%), and states the evaluation artifacts are open-sourced for third-party reproduction. -- evidence: [README.md#L422-L431](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L422-L431), [README.md#L418-L418](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L418-L418) (`clm_f3b98eebe4bd0845a84c2740ed886384d63b8e37cd795aa140037cf7d63174f2`)

## dependencies (2 claim(s))

- [observation/documented] Documentation states Docker deployment ships the Java backend and a built-in static frontend by default in one container, with an optional managed Python service included in the image but not started, and not exposing a port, unless explicitly enabled via environment variables or a compose override. -- evidence: [README.md#L542-L542](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L542-L542), [README.md#L559-L559](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L559-L559) (`clm_4c2cdb1d021845b04961d62fde11c847001644578f7786be91005ea18d076c1b`)
- [observation/documented] A documented provider table lists direct connections to DashScope (Qianwen, the default), DeepSeek, Moonshot (Kimi), Zhipu GLM, and MiniMax as domestic options, plus OpenAI (requiring external network access) and a fully offline local Ollama option. -- evidence: [README.md#L363-L373](https://github.com/zhikunqingtao/zhikuncode/blob/931a9beebf21bd404a6332b96fdb5035930637ae/README.md#L363-L373) (`clm_f84a0ca9b1f834a385ec9ce087d194537dd0511f1fc07ceb23772700fd4c96c6`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

