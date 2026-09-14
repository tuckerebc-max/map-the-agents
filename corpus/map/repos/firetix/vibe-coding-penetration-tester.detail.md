# firetix/vibe-coding-penetration-tester -- full detail

[Back to orientation](vibe-coding-penetration-tester.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/firetix/vibe-coding-penetration-tester/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/6c023b9835b4eea6.json](../../../wiki/dossiers/firetix/vibe-coding-penetration-tester/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/6c023b9835b4eea6.json)

## specifications (1 claim(s))

- [observation/documented] The tool coordinates specialized security agents to discover and validate common web vulnerabilities and generates reproducible Markdown and JSON reports. -- evidence: [README.md#L9-L9](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L9-L9) (`clm_6f460a68f770910367b48ae7e4e9f815391d8b7a7b9b45bd3e2fa149886465d2`)

## components (1 claim(s))

- [observation/documented] The repository includes a CLI entrypoint (main.py), modular Flask web API (run_web.py, web_api/), a legacy web_ui.py, agents/, tools/, and sample reports directories. -- evidence: [README.md#L23-L31](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L23-L31) (`clm_626a316d06dbb7623bb1e571087a3af8450e71dc2cc21e998b84bd7b3801d1a2`)

## design-choices (1 claim(s))

- [observation/documented] Scanning is scope-aware with three scope modes: url, domain, and subdomain. -- evidence: [README.md#L13-L19](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L13-L19), [README.md#L134-L142](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L134-L142) (`clm_679ef622b467298283b7c8bb9e00843c131bb668c3c01447ac8d229363a45304`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: tests are run via ./run_tests.sh or focused pytest suites (unit, integration, API E2E, frontend E2E, Vercel preview) with markers defined in pytest.ini. -- evidence: [README.md#L203-L209](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L203-L209), [README.md#L195-L195](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L195-L195), [README.md#L211-L211](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L211-L211), [README.md#L197-L199](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L197-L199) (`clm_709d309b198df576f606e6af6f740b58aead3524c8d51bfaa114081ac1011434`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI accepts --url (required), --model (default gpt-5.2), --provider (openai/anthropic/ollama), --scope, --output, --verbose, and --ollama-url options. -- evidence: [README.md#L134-L142](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L134-L142) (`clm_8f51319fe06d48e12e29f488bae3973f72bbab7ae627bbfd60afe833ce4cb0c3`)
- [observation/documented] The modular web app exposes session, scan, activity, logs, and report endpoints such as POST /api/scan/start, POST /api/scan/cancel, and GET /api/report/<report_id>. -- evidence: [README.md#L169-L181](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L169-L181) (`clm_0e5c65a5f83a2f8f61e998d1dc8051d28918a78f9111e0b7711ba0aae5150e8c`)
- [observation/documented] Optional hosted/billing endpoints include GET /api/entitlements, POST /api/billing/checkout, and POST /api/billing/webhook, plus a mock checkout route for local/test setups. -- evidence: [README.md#L185-L189](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L185-L189) (`clm_0707f126ddaecea3908de8cce39a5b9d9b743e28a547e1e5dde62cf52a7aa2fe`)

## memory-state (1 claim(s))

- [observation/documented] A session fix added Flask session cookies, cookie-prioritized session tracking, and file-based session persistence so sessions survive server restarts. -- evidence: [README_SESSION_FIX.md#L50-L56](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README_SESSION_FIX.md#L50-L56), [README_SESSION_FIX.md#L14-L18](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README_SESSION_FIX.md#L14-L18) (`clm_ef92a2c52270253cf575972246765e73d36efe62c92582a23b59fa0a5963c1b4`)

## orchestration (1 claim(s))

- [observation/documented] A multi-agent scan workflow covers discovery, planning, and vulnerability testing, with browser automation via Playwright for realistic interaction testing. -- evidence: [README.md#L13-L19](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L13-L19) (`clm_a96814219c2c3881607dc4a6d540fffa933bdb3c6484f45011dbcc4af020bc12`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt pins openai, anthropic, playwright, flask, fastapi, uvicorn, pydantic, PyJWT, psycopg, and pytest-based test dependencies, among others. -- evidence: [requirements.txt#L1-L17](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/requirements.txt#L1-L17), [requirements.txt#L20-L23](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/requirements.txt#L20-L23) (`clm_87ca730efa1d9fe6ab0bcd3f89805a1b759f4929b8fdd78256393e0629272474`)
- [observation/documented] The tool requires at least one LLM provider: an OpenAI API key, an Anthropic API key, or an Ollama server (default localhost:11434). -- evidence: [README.md#L35-L40](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L35-L40), [README.md#L61-L65](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L61-L65) (`clm_139af722d641765e06102a34b79f07fcbd173fd9e1f336b8fe2cf4e055c645e9`)

## limitations (1 claim(s))

- [observation/documented] The tool is restricted by its own notice to targets the user owns or has explicit authorization to test; unauthorized scanning may violate law and policy. -- evidence: [README.md#L228-L228](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L228-L228) (`clm_4354df2c66fca2a8a051be85864e2fc8b18947e1e5550c73beedabeb8b226ee0`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

