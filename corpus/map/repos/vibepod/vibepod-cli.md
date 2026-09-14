# vibepod/vibepod-cli

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ef6519007b1d @ c5c8a1991d43f49f

## Summary (orientation draft, not independently verified)

VibePod is a Python CLI (`vp`) that runs AI coding agents in isolated Docker/Podman containers with local metrics collection and an analytics dashboard. Evidence covers its commands, agent image defaults, ACP editor integration, and contributor test/lint practices.

## Source coverage

Source coverage (partial): 3 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Each agent runs in its own Docker or Podman container, with default images published under the `vibepod` namespace on Docker Hub (e.g. `vibepod/claude:latest`, `vibepod/codex:latest`). -- evidence: [README.md#L16-L19](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L16-L19), [README.md#L174-L190](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L174-L190), [README.md#L170-L170](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L170-L170)
  - [observation/documented] Metrics are collected locally while agents run and served through a built-in dashboard managed via `vp logs start/stop/status`, showing per-agent HTTP traffic, usage over time, and Claude token metrics. -- evidence: [README.md#L158-L162](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L158-L162), [README.md#L153-L154](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L153-L154), [README.md#L164-L166](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L164-L166)
- design-choices (2 claim(s)):
  - [observation/documented] Project overlays let users commit a FROM-less Dockerfile fragment in `.vibepod/overlay/`; VibePod auto-builds a cached, content-addressed image layer on top of the agent's base image. -- evidence: [README.md#L23-L32](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L23-L32)
  - [observation/documented] The project describes itself as privacy-first: all metrics are collected and stored locally and never sent to the cloud. -- evidence: [README.md#L23-L32](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L23-L32)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the test runner is pytest (`python -m pytest`); CI also validates default images with `scripts/check_default_images.py`, and `ruff check`, `ruff format --check`, and `mypy` are pre-commit gated. Tests should run with a throwaway `VP_CONFIG_DIR` when a host global config exists. -- evidence: [AGENTS.md#L35-L40](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/AGENTS.md#L35-L40)
- skills-patterns (1 claim(s)):
  - [observation/documented] Reusable prompt recipes ('skills') can be installed per-project or per-user with `vp skills add`. -- evidence: [README.md#L23-L32](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L23-L32)
- interfaces (5 claim(s)):
  - [observation/documented] The product is a unified CLI named `vp`; `vp run <agent>` launches an agent with no required configuration, and extra arguments after `--` are forwarded to the agent process. -- evidence: [README.md#L16-L19](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L16-L19), [README.md#L67-L68](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L67-L68), [README.md#L70-L72](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L70-L72)
  - [observation/documented] Implemented v1 commands include `vp run`, `vp stop <agent|--all>`, `vp list`, `vp config init/show/path`, and `vp version`. -- evidence: [README.md#L143-L149](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L143-L149)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The CLI is installable via pip (`pip install vibepod`), Homebrew, and conda-forge (conda, mamba, pixi). -- evidence: [README.md#L48-L49](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L48-L49), [README.md#L44-L46](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L44-L46), [README.md#L51-L55](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L51-L55), [README.md#L42-L42](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L42-L42), [README.md#L36-L36](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L36-L36), [README.md#L38-L40](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L38-L40)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](vibepod-cli.detail.md)

Metadata and full claim list: [full detail](vibepod-cli.detail.md)
Human notes ([notes](vibepod-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
