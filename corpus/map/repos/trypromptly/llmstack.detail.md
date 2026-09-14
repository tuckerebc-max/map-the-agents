# trypromptly/llmstack -- full detail

[Back to orientation](llmstack.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/trypromptly/llmstack/701348426fadd0536de8b72536216a9c0365f25b/99e229211c89b3bc.json](../../../wiki/dossiers/trypromptly/llmstack/701348426fadd0536de8b72536216a9c0365f25b/99e229211c89b3bc.json)

## specifications (1 claim(s))

- [observation/documented] LLMStack is described as a no-code platform for building generative AI agents, workflows, and chatbots that connect to data and business processes. -- evidence: [README.md#L1-L9](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L1-L9) (`clm_d3d6484d92e2e7a1cf870c0cc559980e188bbf86c0a5fa167538929ed9dcf09a`)

## components (3 claim(s))

- [observation/documented] The platform imports data types such as CSV, TXT, PDF, DOCX, and PPTX from sources like Google Drive, Notion, websites, and uploads, then preprocesses and vectorizes it into an out-of-the-box vector database. -- evidence: [README.md#L66-L66](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L66-L66) (`clm_529ae893abf637d42048e603b9c207f5a9539308ae2a8d90d45978902fa8b581`)
- [observation/documented] On first run, LLMStack creates a .llmstack directory in the user's home containing the database and config files, and opens a browser to localhost:3000. -- evidence: [README.md#L47-L47](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L47-L47) (`clm_2dbc34207ae0368104e2bfaa4082f44e4af937ff016853c7d24822901db97bb7`)
- [observation/documented] A default admin account ships with credentials 'admin' and 'promptly', and the documentation instructs changing the password from the admin panel after login. -- evidence: [README.md#L25-L25](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L25-L25) (`clm_ff254f7fedafae0dca9ad21c52aee8e0c90cc659ec6760320653e55279297a32`)

## design-choices (2 claim(s))

- [observation/documented] The platform lets users chain multiple LLMs together to build generative AI applications without coding, via a no-code builder. -- evidence: [README.md#L64-L64](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L64-L64), [README.md#L13-L13](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L13-L13), [README.md#L68-L68](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L68-L68) (`clm_c8b27b667a39b21f951c65d2b597d7138e39d239e276f981aeadcd774a76c82a`)
- [observation/documented] LLMStack is multi-tenant: users can create multiple organizations, and users can only access data and AI chains belonging to their organization. -- evidence: [README.md#L74-L74](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L74-L74) (`clm_cacd7bafe2215e6c96412e95c28f83a6222ef60e1a6448fedf23ed21d62c4ddf`)

## workflows (2 claim(s))

- [observation/documented] LLMStack is installed with 'pip install llmstack' and started with the 'llmstack' command; Windows users are directed to use WSL2. -- evidence: [README.md#L39-L39](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L39-L39), [README.md#L43-L45](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L43-L45), [README.md#L35-L37](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L35-L37) (`clm_8e1aa3539afa8ba79a52e218b04d1782046a15f40025fa56e8b28499655edd8c`)
- [observation/documented] Repository development practice: the README points contributors to an external development guide and a contributing guide at docs.trypromptly.com for how to run, develop, and contribute to LLMStack. -- evidence: [README.md#L116-L116](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L116-L116), [README.md#L112-L112](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L112-L112) (`clm_2e7e378454908a2f9c21b3f602996858fe362f51ac4a76ef9acd031cca1a8203`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Apps and chatbots built with LLMStack are accessible via an HTTP API, and AI chains can be triggered from Slack or Discord. -- evidence: [README.md#L72-L72](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L72-L72), [README.md#L96-L96](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L96-L96) (`clm_82a5924e8a6fa220f2a908c991e5dd8c431f13a529bbedf7d6c64da678a2a9f8`)
- [observation/documented] An admin panel at localhost:3000/admin lets administrators add users and assign them to organizations. -- evidence: [README.md#L100-L100](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L100-L100) (`clm_095ad55b96737dda8ff00ba26ee48fb458e395c9c1c46fad3b962c61f8f6eb0a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Users can add provider API keys (e.g., OpenAI, Cohere, Stability) from the Settings page, and instance-wide default keys can be placed in ~/.llmstack/config. -- evidence: [README.md#L49-L49](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L49-L49) (`clm_0a07b35a56a0f57322a1746e31a04a4f7e830143b96e43f6fd478f995cae9dc2`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running jobs requires a background Docker container, so Docker must be installed on the machine to use the jobs feature. -- evidence: [README.md#L31-L31](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L31-L31) (`clm_19de94b7df26fb78e2f72291a875c2106afb07b7107ef650185350e90d97b751`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

