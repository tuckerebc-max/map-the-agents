# urbint/cortex -- full detail

[Back to orientation](cortex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/urbint/cortex/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/d05249608d46ce1b.json](../../../wiki/dossiers/urbint/cortex/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/d05249608d46ce1b.json)

## specifications (1 claim(s))

- [observation/documented] Cortex is described as an intelligent coding assistant for Elixir, installed by adding it as a Mix dependency (e.g. {:cortex, "~> 0.1", only: [:dev, :test]}). -- evidence: [README.md#L18-L18](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L18-L18), [README.md#L20-L26](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L20-L26), [README.md#L4-L4](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L4-L4) (`clm_51ec24c5ef775928953e202fc8f5888eb7330505f4c178bed895397ed55663ca`)

## components (1 claim(s))

- [observation/documented] The product compiles and reloads modified files, automatically runs the appropriate tests at the appropriate time, and accepts pluggable adapters for custom builds. -- evidence: [README.md#L6-L8](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L6-L8) (`clm_28e5831c26a3faad4404ca685e307a498a611e4dc7d81f36f812f54aebc7998a`)

## design-choices (3 claim(s))

- [observation/documented] Running is controlled via application config: an 'enabled' option that defaults to on, support for {:system, ENV_VAR, default} tuples such as CORTEX_ENABLED, and an inverted 'disabled' option for contexts like build or CI environments. -- evidence: [README.md#L100-L103](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L100-L103), [README.md#L88-L91](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L88-L91), [README.md#L115-L118](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L115-L118), [README.md#L93-L94](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L93-L94), [README.md#L111-L113](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L111-L113), [README.md#L85-L86](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L85-L86) (`clm_145cdd6bdd81babc49572d1697fada88d86ac499e4a5f6c1e4dce78cb79e0ff4`)
- [observation/documented] A clear_before_running_tests config option clears the screen immediately before running tests and defaults to true. -- evidence: [README.md#L127-L127](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L127-L127), [README.md#L122-L125](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L122-L125) (`clm_de609f1a30e7f2593f7da3fb89e3f7f785f820c819d7017c83843bc35dbe5d60`)
- [observation/documented] Version 0.6.0 added file throttling to prevent files being compiled multiple times in quick succession and tests being run multiple times from a single change. -- evidence: [History.md#L7-L8](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/History.md#L7-L8), [History.md#L4-L5](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/History.md#L4-L5) (`clm_fe4c06c7a894921ed836f7a3277d0f9fdf2ed5f085856d9589d34abb63afa4ad`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the project uses CircleCI for CI (badge plus changelog entries about adding CircleCI config and installing inotify-tools in CI), and changelog entries mention Credo and Dialyzer checks. -- evidence: [History.md#L13-L22](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/History.md#L13-L22), [README.md#L2-L2](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L2-L2) (`clm_de140b026f067271a1bd6f289483b8df06eeb143283bd457a434d70ef9d8cd3f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Shell-facing commands are provided in the Cortex module: Cortex.all runs all stages (currently reload and test runner) on all project files, and Cortex.unfocus clears the currently configured focus. -- evidence: [README.md#L56-L57](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L56-L57), [README.md#L53-L54](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L53-L54), [README.md#L69-L69](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L69-L69) (`clm_bc8f161de8869e59aa59a9a9e9c063a023eb381bac3b49911bd73a8e4727a671`)
- [observation/documented] Cortex.focus filters test runs by a regular expression, a string compiled as a regex, an integer line number, or a keyword passed through unchanged to the include option of ExUnit.configure/1. -- evidence: [README.md#L59-L67](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L59-L67) (`clm_8cc2b0cdad820a33aabc669f4f4e7f240ecb370056eb6a0e54abdfb4e96fd8f6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Cortex runs automatically alongside the mix app (e.g. via iex -S mix); under MIX_ENV=test it automatically runs tests for saved test files and for tests paired with saved lib files. -- evidence: [README.md#L74-L76](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L74-L76), [README.md#L45-L47](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L45-L47), [README.md#L43-L43](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L43-L43), [README.md#L78-L80](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L78-L80) (`clm_830b26a1d96350b70ab92900339657b5813048fa85078cb237ecb28eaeee3ca6`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] For umbrella applications, users are instructed to add Cortex to each monitored sub-app's dependencies rather than the root mix.exs, because root umbrella dependencies are not automatically started, a process Cortex depends on. -- evidence: [README.md#L31-L33](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L31-L33), [README.md#L35-L37](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L35-L37) (`clm_5df61da6779547f1d88a68b57395b32ef6b71134b456367bd929281c952bbf06`)
- [inference/documented] File watching appears to rely on the file_system package, based on a changelog entry stating the file watcher was updated to use the new file_system API. -- evidence: [History.md#L45-L48](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/History.md#L45-L48) (`clm_f00e8ae3612d8aa5a1a2b876acebaffb678d3d7555eebab2d1f42f17e721c561`)

## limitations (1 claim(s))

- [observation/documented] The roadmap lists unfinished items including Credo, Dialyzer, ExDash and custom mix task runners, per-module reload/test from IEx, broader OTP reload support, and auto-fetching dependencies when mix.exs changes deps. -- evidence: [README.md#L141-L152](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L141-L152) (`clm_9493cec6a2530b4f140d50d9a2a50d2e9a640a157d0874cd1a90b3f86ebc419a`)

## relevance (1 claim(s))

- [observation/documented] The software is licensed under the MIT license, and Phoenix users are instructed to run the app in interactive mode (iex -S mix phoenix.server). -- evidence: [README.md#L157-L157](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L157-L157), [README.md#L131-L132](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L131-L132), [README.md#L134-L136](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L134-L136) (`clm_85b90e6cdf183311f5fda813b65cebb76771208b11a6b87e743591a3adfe95e8`)

