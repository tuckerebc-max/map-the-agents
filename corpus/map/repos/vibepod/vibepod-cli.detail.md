# vibepod/vibepod-cli -- full detail

[Back to orientation](vibepod-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vibepod/vibepod-cli/ef6519007b1d8ab6857f99c27299490605c26b75/c5c8a1991d43f49f.json](../../../wiki/dossiers/vibepod/vibepod-cli/ef6519007b1d8ab6857f99c27299490605c26b75/c5c8a1991d43f49f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Each agent runs in its own Docker or Podman container, with default images published under the `vibepod` namespace on Docker Hub (e.g. `vibepod/claude:latest`, `vibepod/codex:latest`). -- evidence: [README.md#L16-L19](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L16-L19), [README.md#L174-L190](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L174-L190), [README.md#L170-L170](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L170-L170) (`clm_3dbcc01d27a7595931ef4e502a5001acfd59a66f9f972c02f0033bfc42a88a7e`)
- [observation/documented] Metrics are collected locally while agents run and served through a built-in dashboard managed via `vp logs start/stop/status`, showing per-agent HTTP traffic, usage over time, and Claude token metrics. -- evidence: [README.md#L158-L162](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L158-L162), [README.md#L153-L154](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L153-L154), [README.md#L164-L166](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L164-L166) (`clm_4159193229c12321477102e459493848f58508a800d2f989df15964f27e1c450`)

## design-choices (2 claim(s))

- [observation/documented] Project overlays let users commit a FROM-less Dockerfile fragment in `.vibepod/overlay/`; VibePod auto-builds a cached, content-addressed image layer on top of the agent's base image. -- evidence: [README.md#L23-L32](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L23-L32) (`clm_8ebe4a6ab137885c1e9b9ff564cfee3a0418039e0220a972aac6dfa2e0d88600`)
- [observation/documented] The project describes itself as privacy-first: all metrics are collected and stored locally and never sent to the cloud. -- evidence: [README.md#L23-L32](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L23-L32) (`clm_5835348860345d9d0d91ce0e68f0d4f6378517660cfe16d6ca8f8bbde6244210`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the test runner is pytest (`python -m pytest`); CI also validates default images with `scripts/check_default_images.py`, and `ruff check`, `ruff format --check`, and `mypy` are pre-commit gated. Tests should run with a throwaway `VP_CONFIG_DIR` when a host global config exists. -- evidence: [AGENTS.md#L35-L40](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/AGENTS.md#L35-L40) (`clm_50c0ee0bbe48c244d12500bef316e64c8af9e08294af86c2221cad6b6bad446c`)

## skills-patterns (1 claim(s))

- [observation/documented] Reusable prompt recipes ('skills') can be installed per-project or per-user with `vp skills add`. -- evidence: [README.md#L23-L32](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L23-L32) (`clm_b6ec1f0db41fcf1a048564c6adca0287e2245852b103ad24e02b9f1a8f76037a`)

## interfaces (5 claim(s))

- [observation/documented] The product is a unified CLI named `vp`; `vp run <agent>` launches an agent with no required configuration, and extra arguments after `--` are forwarded to the agent process. -- evidence: [README.md#L16-L19](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L16-L19), [README.md#L67-L68](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L67-L68), [README.md#L70-L72](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L70-L72) (`clm_e91eaa48f1a08e42e542895ab9a6557da30db892c06592384ef78b9d81740138`)
- [observation/documented] Implemented v1 commands include `vp run`, `vp stop <agent|--all>`, `vp list`, `vp config init/show/path`, and `vp version`. -- evidence: [README.md#L143-L149](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L143-L149) (`clm_e571f591456707e025b6162ad43133b5cb9107c0f1256c63a64c83faadb4b670`)
- [observation/documented] `--ikwid` appends each agent's auto-approval/permission-skip flag when supported; e.g. claude gets `--dangerously-skip-permissions`, gemini and qwen get `--approval-mode=yolo`, and several agents (opencode, auggie, tau, jcode, freebuff, dsh) are listed as not supported. -- evidence: [README.md#L78-L94](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L78-L94), [README.md#L76-L76](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L76-L76) (`clm_65cc574b85b2d8a5f9efa36f1c855bda2b1ab476aa5abfcf379e73838cbb5b5a`)
- [observation/documented] `vp run <agent> --acp` turns the CLI into an Agent Client Protocol adapter so the containerized agent appears in ACP-capable editors like Zed, with isolation, profiles, overlays and proxy metrics intact. -- evidence: [README.md#L98-L98](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L98-L98) (`clm_a5c4ffb79a0645efc9a4f803666364306864eaba630392c31d9710da2edf9363`)
- [observation/documented] Individual images can be overridden per agent via environment variables such as `VP_IMAGE_CLAUDE`, plus `VP_DATASETTE_IMAGE` for the dashboard and `VP_SKILLS_ENGINE_IMAGE` for skills commands. -- evidence: [README.md#L194-L194](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L194-L194), [README.md#L196-L215](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L196-L215) (`clm_f7492468b539c503e317b0cef46179c58eb1bd30e2fa892b8f531ba7e47bded3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The CLI is installable via pip (`pip install vibepod`), Homebrew, and conda-forge (conda, mamba, pixi). -- evidence: [README.md#L48-L49](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L48-L49), [README.md#L44-L46](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L44-L46), [README.md#L51-L55](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L51-L55), [README.md#L42-L42](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L42-L42), [README.md#L36-L36](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L36-L36), [README.md#L38-L40](https://github.com/VibePod/vibepod-cli/blob/ef6519007b1d8ab6857f99c27299490605c26b75/README.md#L38-L40) (`clm_718605621670a3b371a48d654c4c4b2de63b573a603ad07da77607bb1ae4162f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

