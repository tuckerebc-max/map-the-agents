# gerome-elassaad/codingit -- full detail

[Back to orientation](codingit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gerome-elassaad/codingit/b21eff408c446369bf4147fd728cfbe1d5c471e8/0a9071aac76f43b8.json](../../../wiki/dossiers/gerome-elassaad/codingit/b21eff408c446369bf4147fd728cfbe1d5c471e8/0a9071aac76f43b8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The app is built on Next.js 14 (App Router, Server Actions) with shadcn/ui, TailwindCSS, and the Vercel AI SDK, and streams output in the UI. -- evidence: [README.md#L21-L43](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L21-L43) (`clm_b6be0f3ba68d5ef85f7684365a62f4500fb18601c41c3b9c6d7865a450c3eae0`)
- [observation/documented] AI-generated code is executed via the E2B SDK (code-interpreter), which the README describes as executing such code securely. -- evidence: [README.md#L21-L43](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L21-L43) (`clm_e3f570167f7d2e358fd3e333103b3ad27503fb55e9eb71ca43c0ab2bd37baad8`)
- [observation/documented] A Stripe payment system provides checkout, billing portal, and webhook handling, with Pro ($9/month) and Enterprise ($25/month) subscription plans. -- evidence: [CHANGELOG.md#L306-L310](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L306-L310) (`clm_386fc9d4e74c5ef4010109d621cb9cb76073f5b88d117fcaa6a1a64633d32f1c`)

## design-choices (2 claim(s))

- [observation/documented] The theme system was simplified to dark mode only; light theme support and the theme toggle were removed. -- evidence: [CHANGELOG.md#L275-L276](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L275-L276), [CHANGELOG.md#L238-L243](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L238-L243) (`clm_a69d6c2ca96df882fcbbb5de97467aee9b54a11a4aaca1d5fb5285b8037ff1a2`)
- [observation/documented] Security hardening includes SSRF prevention with domain allowlisting for PyPI/npm requests, input validation, rate limiting, and a centralized lib/security.ts module. -- evidence: [CHANGELOG.md#L246-L251](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L246-L251), [CHANGELOG.md#L220-L225](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L220-L225) (`clm_0467e5bc19b3a45e43bff1bc05753299b7310b6c12af0095373a3cc222736b7a`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: setup requires cloning the repo, running npm i, creating .env.local with E2B and LLM provider API keys, then npm run dev or npm run build. -- evidence: [README.md#L77-L77](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L77-L77), [README.md#L135-L137](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L135-L137), [README.md#L58-L61](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L58-L61), [README.md#L67-L69](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L67-L69), [README.md#L73-L73](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L73-L73), [README.md#L141-L143](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L141-L143) (`clm_4ca0acbd119c0a76dcc6e61a4d0299dc11f70e8bd2bce1508105e876b65025dc`)
- [observation/documented] Repository development practice: custom personas are added by creating a sandbox-templates folder, building an E2B template via the E2B CLI, and registering it in lib/templates.json. -- evidence: [README.md#L182-L182](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L182-L182), [README.md#L216-L216](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L216-L216), [README.md#L184-L186](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L184-L186), [README.md#L153-L153](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L153-L153), [README.md#L194-L194](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L194-L194), [README.md#L151-L151](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L151-L151) (`clm_d271c94cc50229bfcfe81198c11c22bd1ddcf93db26cbb10c9c73c02196f72c6`)
- [observation/documented] Repository development practice: custom LLM models are added in lib/models.json and providers via providerConfigs in lib/models.ts, with optional structured-output mode adjustments. -- evidence: [README.md#L222-L222](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L222-L222), [README.md#L239-L239](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L239-L239), [README.md#L241-L241](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L241-L241), [README.md#L249-L249](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L249-L249) (`clm_fa47b82fe64ebeccc7e77411ea3e5a0aa71191aad4978a1424cff84597b0c5f7`)
- [observation/documented] Repository development practice: the project welcomes community contributions via issues or pull requests for bugs and improvements. -- evidence: [README.md#L261-L261](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L261-L261) (`clm_e3fcfaf02ec85d132dad9b63e64946e462c119c89fc3ddb2c3117c09be1d7750`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product ships several sandbox personas/stacks, including Python data analyst, Next.js, Vue.js, Streamlit, Gradio, and CodinIT Engineer. -- evidence: [README.md#L21-L43](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L21-L43) (`clm_e849bca338ab918e93e03a8c5f8e13fe0c87fe0de7b9530a451a7ee4f61c3127`)
- [observation/documented] Chat session REST endpoints cover listing/creating sessions, per-session management, messages, cross-history search, analytics, and JSON/CSV export. -- evidence: [CHANGELOG.md#L77-L80](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L77-L80), [CHANGELOG.md#L82-L86](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L82-L86) (`clm_d2c6e93fb7e4dd056658450e268967bf880689f3b9ae8967e599ac55775d985c`)

## memory-state (1 claim(s))

- [observation/documented] Chat persistence stores sessions and messages in AWS S3 under a users/{userId}/sessions/{sessionId} layout with metadata.json and messages.json, plus aggregate analytics folders. -- evidence: [CHANGELOG.md#L62-L66](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L62-L66), [CHANGELOG.md#L118-L127](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L118-L127), [CHANGELOG.md#L68-L73](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L68-L73) (`clm_cdfe672ecf5ab141c77cf8b22a349b9795d7d534e0165fa50c67b85830aada55`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Usage limits are enforced per tier: GitHub imports 5/50/unlimited per month, storage 100MB/5GB/unlimited, and execution time 30s/300s/600s for Free/Pro/Enterprise. -- evidence: [CHANGELOG.md#L312-L317](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L312-L317) (`clm_38a18c6c9de4a306d3a25d9684c82a63c8946b706699db2b706872080f6824aa`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Supported LLM providers include OpenAI, Anthropic, Google Generative AI, Google Vertex AI, Mistral, Groq, Fireworks, Together AI, Ollama, xAI, and DeepSeek. -- evidence: [README.md#L21-L43](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/README.md#L21-L43) (`clm_a378fdb9a094a873bb83d46b5118b2a3f2873d99fa934d8b18aeb0104c1bffab`)

## limitations (1 claim(s))

- [observation/documented] Workflow builder and deployment features were removed as a breaking change; users can no longer access them, with focus on core AI code generation and sandbox execution. -- evidence: [CHANGELOG.md#L210-L213](https://github.com/Gerome-Elassaad/CodingIT/blob/b21eff408c446369bf4147fd728cfbe1d5c471e8/CHANGELOG.md#L210-L213) (`clm_f1eb0e72186048eb8870356c67db3d88b2de21fa84a2d726d25941af04ebb608`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

