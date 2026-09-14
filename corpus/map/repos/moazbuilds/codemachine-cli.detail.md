# moazbuilds/codemachine-cli -- full detail

[Back to orientation](codemachine-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/moazbuilds/codemachine-cli/572def63eb808e95b18ccf6c69a13d7a13fe06fd/3c737dd66b55d243.json](../../../wiki/dossiers/moazbuilds/codemachine-cli/572def63eb808e95b18ccf6c69a13d7a13fe06fd/3c737dd66b55d243.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A default workflow called the Ali Workflow Builder is included for creating workflows interactively. -- evidence: [README.md#L38-L38](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L38-L38) (`clm_02ed3a587d54deb76323996be0048336771ceffddf99746b3ba0a1542308a736`)

## design-choices (1 claim(s))

- [observation/documented] Workflows can range from fully interactive to fully autonomous, with documentation on orchestration patterns available. -- evidence: [README.md#L34-L34](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L34-L34) (`clm_249eeeac9eba1d03a62369358977607d6b66adc9d67b3b092d046224a49559f4`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors need Bun 1.3+, install with 'bun install', start with 'bun dev', and run 'bun run lint' and 'bun run typecheck' before submitting PRs. -- evidence: [CONTRIBUTING.md#L41-L44](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L41-L44), [CONTRIBUTING.md#L19-L22](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L19-L22), [CONTRIBUTING.md#L15-L15](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L15-L15) (`clm_e6614bf551062484e817a6be782feafb94bbd4578253763937a66b90da4f4464`)
- [observation/documented] Repository development practice: UI and feature PRs require prior team review or will likely be refused; PRs should be focused on one feature or fix. -- evidence: [CONTRIBUTING.md#L11-L11](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L11-L11), [CONTRIBUTING.md#L46-L46](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L46-L46) (`clm_f830f30b89df1d9b085acf318be0ef8df60bda435f63d197ed64bb58ac36394a`)
- [observation/documented] Repository development practice: the codebase is organized into src/infra, src/cli/tui, src/workflows, src/agents, src/shared, plus config, prompts, and templates directories. -- evidence: [CONTRIBUTING.md#L26-L35](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTING.md#L26-L35) (`clm_ad702bf091eecd71724945e3d755d1f97e767b02ac117e5b25ec2f14b75675d5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The tool is distributed as an npm package installable globally via 'npm i -g codemachine'. -- evidence: [README.md#L5-L7](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L5-L7) (`clm_a1ff254684f08d396d4166cc00df2d7580bb4573e42888f99faed78e113632e7`)

## memory-state (1 claim(s))

- [observation/documented] The tool centralizes prompts and manages dynamic context, controlling what each agent sees at each workflow step. -- evidence: [README.md#L40-L44](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L40-L44) (`clm_d363d1e3747867cce2de1339127965e59e4386db5360da41b31df456fb67b7a2`)

## orchestration (4 claim(s))

- [observation/documented] CodeMachine is an orchestration layer that runs AI coding CLIs through structured workflows, handling execution, context passing, and agent coordination. -- evidence: [README.md#L29-L29](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L29-L29) (`clm_d04e624bfc9c167cf84eb4aaa4795766ead5a29202f006be6e751c1f5b618704`)
- [observation/documented] It spawns AI coding engines via CLI using their headless scripting mode, passing appropriate arguments and flags to control agents. -- evidence: [README.md#L32-L32](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L32-L32) (`clm_3b26b58b9f3b782600432c029439547e23c707564aa8938fc07907f140c99dd5`)
- [observation/documented] The product supports multi-agent orchestration where different agents are assigned to different tasks, can communicate with each other, and collaborate on decisions. -- evidence: [README.md#L40-L44](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L40-L44) (`clm_c02fb2a5b3c6ef147e2942a46f3df2a10a0682f70f762da2d3a8c531368808d7`)
- [observation/documented] Multiple agents can run in parallel on different parts of a workflow, and workflows can run for hours or days with persistence handled by the tool. -- evidence: [README.md#L40-L44](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L40-L44) (`clm_a43a6ec694dac0a968e6b1d5048359f0210f49d8e232b1587396637aa69123ce`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool integrates multiple AI engines, including Claude Code, Codex, Cursor, CCR (Claude Code Router), OpenCode CLI, Auggie CLI, and Mistral Vibe, per contributor notes. -- evidence: [CONTRIBUTORS.md#L17-L17](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L17-L17), [README.md#L32-L32](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md#L32-L32), [CONTRIBUTORS.md#L29-L29](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L29-L29), [CONTRIBUTORS.md#L20-L20](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L20-L20), [CONTRIBUTORS.md#L11-L11](https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/CONTRIBUTORS.md#L11-L11) (`clm_555140827587fff4cf2f2fbd1f97e8097be6721ac071d87a66c5ce75a27fd81f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

