# google-gemini/gemini-cli -- full detail

[Back to orientation](gemini-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/google-gemini/gemini-cli/9c1b0a610534d6f8120964cf2672c07807d8fc90/65fb3d86d9eafaa4.json](../../../wiki/dossiers/google-gemini/gemini-cli/9c1b0a610534d6f8120964cf2672c07807d8fc90/65fb3d86d9eafaa4.json)

## specifications (1 claim(s))

- [observation/documented] Gemini CLI is an open-source AI agent that brings Gemini into the terminal, providing lightweight access from the user's prompt to the model. -- evidence: [README.md#L11-L13](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L11-L13) (`clm_9fbdd939d6e6ca9d7e232806e439f93ea683f18e7777064edf11efcf8d985703`)

## components (1 claim(s))

- [observation/documented] Built-in tools include Google Search grounding, file operations, shell commands, and web fetching, with MCP support for custom integrations. -- evidence: [README.md#L19-L28](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L19-L28) (`clm_661b9302c5c469c85a438d1946120dd86cee1fd1fe54d87bcb0922034ae84b4c`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run npm run test for unit tests, test:e2e for integration, and preflight (clean, install, build, lint, type check, tests) before submitting PRs. -- evidence: [GEMINI.md#L44-L65](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/GEMINI.md#L44-L65) (`clm_a92d62d09cdca7dcdda48591d72342e5f5200b848c49ebc12c1fd107742cec60`)
- [observation/documented] Repository development practice: PRs should be small and issue-linked, commits follow Conventional Commits, and new source files need Apache-2.0 license headers enforced by ESLint. -- evidence: [GEMINI.md#L69-L80](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/GEMINI.md#L69-L80) (`clm_24a467f8475aec0c19157464f21de1fe4a271062760bc935db5b687281bd899c`)
- [observation/documented] Repository development practice: tests depending on environment variables should use vi.stubEnv in beforeEach and vi.unstubAllEnvs in afterEach rather than mutating process.env directly. -- evidence: [GEMINI.md#L84-L88](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/GEMINI.md#L84-L88) (`clm_2c93bcd2fda4a0dafab6a5dfa2ae0e423f2567dc9709c01aab7e54135fee4ebb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI supports non-interactive scripting via -p, with --output-format json for structured output and stream-json for newline-delimited event streaming. -- evidence: [README.md#L240-L242](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L240-L242), [README.md#L251-L252](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L251-L252), [README.md#L244-L245](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L244-L245), [README.md#L254-L256](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L254-L256) (`clm_4655d2b691efddd4381944f048c288ba152fba496a59747138c1fdf667605e9f`)
- [observation/documented] CLI flags include --include-directories for multiple directories, -m for model selection, and -s for sandboxing. -- evidence: [README.md#L226-L228](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L226-L228), [docs/cli/sandbox.md#L41-L43](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L41-L43), [README.md#L232-L234](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L232-L234) (`clm_acc13d43e32f438a4368464e6c7b3702c5b9f23e2bf13d94e75772d93b6a135b`)

## memory-state (2 claim(s))

- [observation/documented] The agent persists durable facts by editing Markdown memory files, routing shared project instructions to GEMINI.md and personal preferences to the global ~/.gemini/GEMINI.md. -- evidence: [docs/tools/memory.md#L8-L11](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/tools/memory.md#L8-L11), [docs/tools/memory.md#L3-L4](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/tools/memory.md#L3-L4) (`clm_7e769d39d49000003db4303dffdf61163a996745410b1f7f373707c21917b33e`)
- [observation/documented] Stored memories are edited with write_file or replace and are automatically included in the hierarchical context system for all future sessions. -- evidence: [docs/tools/memory.md#L15-L19](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/tools/memory.md#L15-L19) (`clm_48736525dd1831b9c0a6df0ba34afec671bb315500be61ef6a4fa6619404dcd7`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (3 claim(s))

- [observation/documented] Sandboxing can be enabled via the -s/--sandbox flag, the GEMINI_SANDBOX env var, or settings.json, with providers including docker, podman, sandbox-exec, runsc, and lxc. -- evidence: [docs/cli/sandbox.md#L75-L79](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L75-L79) (`clm_a6fbf314d1e399f0be2495ec00624f3f82338299fa7a679e01bd9ae0c1d83aa5`)
- [observation/documented] A sandbox expansion mechanism detects permission denials or proactively identified needs and shows a modal request; approval grants extended permissions for that specific run. -- evidence: [docs/cli/sandbox.md#L298-L299](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L298-L299), [docs/cli/sandbox.md#L301-L304](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L301-L304), [docs/cli/sandbox.md#L308-L313](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L308-L313) (`clm_baa1e7a57911f79245ef86de0c134645beb291a6dd3b7d096491a7807dbd84c4`)
- [observation/documented] Tool-level sandboxing isolates individual tool executions such as shell_exec and write_file, and can be disabled via security.toolSandboxing=false in settings.json (restart required). -- evidence: [docs/cli/sandbox.md#L269-L271](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L269-L271), [docs/cli/sandbox.md#L279-L281](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L279-L281), [docs/cli/sandbox.md#L291-L294](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L291-L294) (`clm_131d88c79568389693c0823e748ade39c45712cccc5971f6d61ea9a9c2a8e461`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project uses Node.js (>=20), TypeScript, React with Ink for CLI rendering, Vitest, esbuild, ESLint, and Prettier, in an npm-workspaces monorepo. -- evidence: [GEMINI.md#L9-L29](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/GEMINI.md#L9-L29) (`clm_24f52035b123cf9b108c200bbb4cd59727796633d821cccc53de7b149ccad2ad`)

## limitations (2 claim(s))

- [observation/documented] LXC sandboxing is Linux-only and requires the container to already exist and be running, as Gemini does not create it automatically. -- evidence: [docs/cli/sandbox.md#L232-L235](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L232-L235), [docs/cli/sandbox.md#L261-L265](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/docs/cli/sandbox.md#L261-L265) (`clm_4866bb9642529f95ae4cca923fde2a3abbf83f0dd82cbe9761050a175f444f9b`)
- [observation/documented] Weekly preview releases are not fully vetted and may contain regressions; nightly builds should be assumed to carry pending validations and issues. -- evidence: [README.md#L80-L82](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L80-L82), [README.md#L100-L102](https://github.com/google-gemini/gemini-cli/blob/9c1b0a610534d6f8120964cf2672c07807d8fc90/README.md#L100-L102) (`clm_60cd23edbfb59b0c4a35838142e40e404b0be78273a0383ad6d1d66516370509`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

