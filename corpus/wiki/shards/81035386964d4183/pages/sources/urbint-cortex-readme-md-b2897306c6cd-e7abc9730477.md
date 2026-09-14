---
access: public
aliases: []
claim_ids:
- clm_145cdd6bdd81babc49572d1697fada88d86ac499e4a5f6c1e4dce78cb79e0ff4
- clm_28e5831c26a3faad4404ca685e307a498a611e4dc7d81f36f812f54aebc7998a
- clm_51ec24c5ef775928953e202fc8f5888eb7330505f4c178bed895397ed55663ca
- clm_5df61da6779547f1d88a68b57395b32ef6b71134b456367bd929281c952bbf06
- clm_830b26a1d96350b70ab92900339657b5813048fa85078cb237ecb28eaeee3ca6
- clm_85b90e6cdf183311f5fda813b65cebb76771208b11a6b87e743591a3adfe95e8
- clm_8cc2b0cdad820a33aabc669f4f4e7f240ecb370056eb6a0e54abdfb4e96fd8f6
- clm_9493cec6a2530b4f140d50d9a2a50d2e9a640a157d0874cd1a90b3f86ebc419a
- clm_bc8f161de8869e59aa59a9a9e9c063a023eb381bac3b49911bd73a8e4727a671
- clm_de140b026f067271a1bd6f289483b8df06eeb143283bd457a434d70ef9d8cd3f
- clm_de609f1a30e7f2593f7da3fb89e3f7f785f820c819d7017c83843bc35dbe5d60
maturity: draft
page_id: pg_4555bb0c688c5cf2858de7abc9730477
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_83a955983f725e37954ff96cefb2d20c
title: urbint/cortex/README.md @ b2897306c6cd
updated_at: '2026-09-14T04:29:07Z'
---

# urbint/cortex/README.md @ b2897306c6cd

<!-- rcw:begin owner=source:src_83a955983f725e37954ff96cefb2d20c block=evidence -->
- Running is controlled via application config: an 'enabled' option that defaults to on, support for {:system, ENV_VAR, default} tuples such as CORTEX_ENABLED, and an inverted 'disabled' option for contexts like build or CI environments. [@claim:clm_145cdd6bdd81babc49572d1697fada88d86ac499e4a5f6c1e4dce78cb79e0ff4]
- The product compiles and reloads modified files, automatically runs the appropriate tests at the appropriate time, and accepts pluggable adapters for custom builds. [@claim:clm_28e5831c26a3faad4404ca685e307a498a611e4dc7d81f36f812f54aebc7998a]
- Cortex is described as an intelligent coding assistant for Elixir, installed by adding it as a Mix dependency (e.g. {:cortex, "~> 0.1", only: [:dev, :test]}). [@claim:clm_51ec24c5ef775928953e202fc8f5888eb7330505f4c178bed895397ed55663ca]
- For umbrella applications, users are instructed to add Cortex to each monitored sub-app's dependencies rather than the root mix.exs, because root umbrella dependencies are not automatically started, a process Cortex depends on. [@claim:clm_5df61da6779547f1d88a68b57395b32ef6b71134b456367bd929281c952bbf06]
- Cortex runs automatically alongside the mix app (e.g. via iex -S mix); under MIX_ENV=test it automatically runs tests for saved test files and for tests paired with saved lib files. [@claim:clm_830b26a1d96350b70ab92900339657b5813048fa85078cb237ecb28eaeee3ca6]
- The software is licensed under the MIT license, and Phoenix users are instructed to run the app in interactive mode (iex -S mix phoenix.server). [@claim:clm_85b90e6cdf183311f5fda813b65cebb76771208b11a6b87e743591a3adfe95e8]
- Cortex.focus filters test runs by a regular expression, a string compiled as a regex, an integer line number, or a keyword passed through unchanged to the include option of ExUnit.configure/1. [@claim:clm_8cc2b0cdad820a33aabc669f4f4e7f240ecb370056eb6a0e54abdfb4e96fd8f6]
- The roadmap lists unfinished items including Credo, Dialyzer, ExDash and custom mix task runners, per-module reload/test from IEx, broader OTP reload support, and auto-fetching dependencies when mix.exs changes deps. [@claim:clm_9493cec6a2530b4f140d50d9a2a50d2e9a640a157d0874cd1a90b3f86ebc419a]
- Shell-facing commands are provided in the Cortex module: Cortex.all runs all stages (currently reload and test runner) on all project files, and Cortex.unfocus clears the currently configured focus. [@claim:clm_bc8f161de8869e59aa59a9a9e9c063a023eb381bac3b49911bd73a8e4727a671]
- Repository development practice: the project uses CircleCI for CI (badge plus changelog entries about adding CircleCI config and installing inotify-tools in CI), and changelog entries mention Credo and Dialyzer checks. [@claim:clm_de140b026f067271a1bd6f289483b8df06eeb143283bd457a434d70ef9d8cd3f]
- A clear_before_running_tests config option clears the screen immediately before running tests and defaults to true. [@claim:clm_de609f1a30e7f2593f7da3fb89e3f7f785f820c819d7017c83843bc35dbe5d60]
<!-- rcw:end owner=source:src_83a955983f725e37954ff96cefb2d20c block=evidence -->

## Researcher notes

