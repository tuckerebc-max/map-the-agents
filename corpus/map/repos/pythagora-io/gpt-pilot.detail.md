# pythagora-io/gpt-pilot -- full detail

[Back to orientation](gpt-pilot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pythagora-io/gpt-pilot/9b763fdaf0020c7d8abacc7b58b2b09e57494623/e71333c416601489.json](../../../wiki/dossiers/pythagora-io/gpt-pilot/9b763fdaf0020c7d8abacc7b58b2b09e57494623/e71333c416601489.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The app-building pipeline uses named agents including Specification Writer, Architect, Tech Lead, Developer, Code Monkey, Reviewer, Troubleshooter, Debugger, and Technical Writer. -- evidence: [README.md#L207-L217](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L207-L217) (`clm_c8d038ec93fd1091ae882d8b70dc3c15e88e282dd939741e8dd21543680279ba`)

## design-choices (4 claim(s))

- [observation/documented] Generated code is stored in a workspace folder named after the app name entered at startup; config.json (copied from example-config.json) holds LLM provider keys/endpoints and optional fs.ignore_paths. -- evidence: [README.md#L148-L148](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L148-L148), [README.md#L135-L146](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L135-L146) (`clm_3f36762e7d8348e18228f2171001b9db21066ccd1d541a977a2c644024229496`)
- [observation/documented] GPT Pilot filters code shown to the LLM so each conversation contains only code relevant to the current task rather than the entire codebase, aiming to work at any scale. -- evidence: [README.md#L223-L225](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L223-L225) (`clm_3afe4e2d8e5f35702c43bfb93eb313da7292f0f5e44c24c3472943235e12920e`)
- [observation/documented] GPT Pilot codes the app step by step with the developer in the loop, debugging issues as they arise, in contrast to similar tools that output an entire codebase at once. -- evidence: [README.md#L223-L225](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L223-L225) (`clm_00cbf53e041ad2c71b479f6488fec4ed06893a8265f5fcf04ca144c5f5b21ae9`)
- [observation/documented] Telemetry collects data such as total runtime, command runs, LLM request counts, OS, Python version, model, and task/step info; it can be disabled by setting telemetry.enabled to false in ~/.gpt-pilot/config.json. -- evidence: [docs/TELEMETRY.md#L9-L23](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/docs/TELEMETRY.md#L9-L23), [docs/TELEMETRY.md#L44-L44](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/docs/TELEMETRY.md#L44-L44), [docs/TELEMETRY.md#L42-L42](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/docs/TELEMETRY.md#L42-L42) (`clm_5bec08ed3b86c9d55465a6df96049236744134a6461cb69082809614846c4fa5`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI supports listing projects (--list), resuming a project or a specific step (--project <app_id> [--step <step>]), deleting a project (--delete <app_id>), and --help for all options. -- evidence: [README.md#L182-L184](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L182-L184), [README.md#L198-L198](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L198-L198), [README.md#L176-L178](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L176-L178), [README.md#L200-L202](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L200-L202), [README.md#L168-L170](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L168-L170), [README.md#L190-L192](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L190-L192) (`clm_cf1a8d962204e8374ea03d3b2a881622201ee68dd81a27d8b812d4cdeae5c923`)
- [observation/documented] Documented warnings state that resuming from a specific step deletes all progress after that step, and that deleting a project cannot be undone. -- evidence: [README.md#L194-L194](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L194-L194), [README.md#L186-L186](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L186-L186) (`clm_a5d89c1cde16839702308dc926c5836aadccf59c9976fa17934353a8ad57849f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The Architect agent checks whether the app's technologies are installed on the machine and installs them if not. -- evidence: [README.md#L207-L217](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L207-L217) (`clm_bf1e31097c7f7ac3c7459e853ab82e050333204a269aca69483544a69153f16b`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] requirements.txt pins Python dependencies including openai 1.40.6, anthropic 0.39.0, groq 0.6.0, sqlalchemy 2.0.32, pydantic 2.8.2, tiktoken 0.8.0, and sentry-sdk 2.20.0. -- evidence: [requirements.txt#L1-L38](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/requirements.txt#L1-L38) (`clm_15e63c1136e7283e9f90c9c0d93780040306837bc639f98827d6c3de3c536540`)
- [observation/documented] SQLite is the default database; PostgreSQL support requires additionally installing asyncpg and psycopg2 and setting db.url to a postgresql+asyncpg:// URL in config.json. -- evidence: [README.md#L162-L162](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L162-L162), [README.md#L156-L156](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L156-L156), [README.md#L158-L160](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L158-L160) (`clm_5c4af4511258de7e8f440e7db44946b6f056676b2c3c540d2591b1de525d9a4c`)

## limitations (3 claim(s))

- [observation/documented] A credential-stealing supply-chain worm was hidden in core/telemetry/ from August 2025 until 11 June 2026; users who cloned and ran GPT Pilot from source in that window are told to rotate credentials. -- evidence: [README.md#L10-L10](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L10-L10), [README.md#L12-L14](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L12-L14), [README.md#L1-L2](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L1-L2) (`clm_994851ec715d13bd3c17e01cb8f590fa504145cccfc2362879a238a9127a0f32`)
- [observation/documented] The malicious commit added a hidden loader (core/telemetry/_hooks.py) wired via core/telemetry/__init__.py that downloaded the Bun runtime to execute an obfuscated payload (core/telemetry/_runtime.bin) harvesting cloud/AWS keys, GitHub and npm tokens, and SSH keys. -- evidence: [README.md#L8-L8](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L8-L8) (`clm_add6e19d55c26b3f7c801e06a31a1216fd1970c21d0aee6985264a8504c42436`)
- [observation/documented] The repository is no longer actively maintained, which the notice says is why the malicious commit went unnoticed; the notice and file removals are a security cleanup, not a resumption of development. -- evidence: [README.md#L16-L16](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L16-L16), [README.md#L57-L57](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L57-L57) (`clm_95a6942bf56ea442fda37fc0594b27def9d7ad04396ad166022ac7b97a3a9d18`)

## relevance (1 claim(s))

- [observation/documented] GPT Pilot is the core technology for the Pythagora VS Code extension, positioned as an AI developer that can write full features, debug them, and ask for review. -- evidence: [README.md#L80-L80](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L80-L80) (`clm_545233f2a39450e38275aa1ab70ae63eb6ae5a08a72dfa6c055b1c3dbb503b81`)

