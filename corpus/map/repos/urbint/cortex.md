# urbint/cortex

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b2897306c6cd @ d05249608d46ce1b

## Summary (orientation draft, not independently verified)

Cortex is an Elixir coding assistant distributed as a Mix dependency that recompiles modified files, auto-runs tests, and offers shell commands and config-based enable/disable. All prior claims were verified against cited slices; one claim was revised to remove an uncited copyright attribution.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Cortex is described as an intelligent coding assistant for Elixir, installed by adding it as a Mix dependency (e.g. {:cortex, "~> 0.1", only: [:dev, :test]}). -- evidence: [README.md#L18-L18](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L18-L18), [README.md#L20-L26](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L20-L26), [README.md#L4-L4](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L4-L4)
- components (1 claim(s)):
  - [observation/documented] The product compiles and reloads modified files, automatically runs the appropriate tests at the appropriate time, and accepts pluggable adapters for custom builds. -- evidence: [README.md#L6-L8](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L6-L8)
- design-choices (3 claim(s)):
  - [observation/documented] Running is controlled via application config: an 'enabled' option that defaults to on, support for {:system, ENV_VAR, default} tuples such as CORTEX_ENABLED, and an inverted 'disabled' option for contexts like build or CI environments. -- evidence: [README.md#L100-L103](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L100-L103), [README.md#L88-L91](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L88-L91), [README.md#L115-L118](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L115-L118), [README.md#L93-L94](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L93-L94), [README.md#L111-L113](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L111-L113), [README.md#L85-L86](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L85-L86)
  - [observation/documented] A clear_before_running_tests config option clears the screen immediately before running tests and defaults to true. -- evidence: [README.md#L127-L127](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L127-L127), [README.md#L122-L125](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L122-L125)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the project uses CircleCI for CI (badge plus changelog entries about adding CircleCI config and installing inotify-tools in CI), and changelog entries mention Credo and Dialyzer checks. -- evidence: [History.md#L13-L22](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/History.md#L13-L22), [README.md#L2-L2](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L2-L2)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Shell-facing commands are provided in the Cortex module: Cortex.all runs all stages (currently reload and test runner) on all project files, and Cortex.unfocus clears the currently configured focus. -- evidence: [README.md#L56-L57](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L56-L57), [README.md#L53-L54](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L53-L54), [README.md#L69-L69](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L69-L69)
  - [observation/documented] Cortex.focus filters test runs by a regular expression, a string compiled as a regex, an integer line number, or a keyword passed through unchanged to the include option of ExUnit.configure/1. -- evidence: [README.md#L59-L67](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L59-L67)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Cortex runs automatically alongside the mix app (e.g. via iex -S mix); under MIX_ENV=test it automatically runs tests for saved test files and for tests paired with saved lib files. -- evidence: [README.md#L74-L76](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L74-L76), [README.md#L45-L47](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L45-L47), [README.md#L43-L43](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L43-L43), [README.md#L78-L80](https://github.com/urbint/cortex/blob/b2897306c6cda6683c80b3d4b24cbcdfd5bedd60/README.md#L78-L80)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](cortex.detail.md)

Metadata and full claim list: [full detail](cortex.detail.md)
Human notes ([notes](cortex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
