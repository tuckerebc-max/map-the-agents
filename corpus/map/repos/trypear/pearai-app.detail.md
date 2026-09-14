# trypear/pearai-app -- full detail

[Back to orientation](pearai-app.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/trypear/pearai-app/d930f0233c14668df9f85c6a78a81828f4251194/145d5fa987766159.json](../../../wiki/dossiers/trypear/pearai-app/d930f0233c14668df9f85c6a78a81828f4251194/145d5fa987766159.json)

## specifications (1 claim(s))

- [observation/documented] PearAI is described as a fork of VSCode, with its main functionality in a separate submodule (pearai-submodule) that is itself a fork of Continue. -- evidence: [README.md#L5-L5](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L5-L5), [CONTRIBUTING.md#L84-L86](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L84-L86), [CONTRIBUTING.md#L15-L15](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L15-L15) (`clm_f8e5a885886312803a492bbfab56a252e0f09dd95c12a5abeb2fa80adebd5417`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The README states Pear has context on the user's codebase so questions can be asked directly, with code stored locally on the user's computer. -- evidence: [README.md#L12-L14](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L12-L14) (`clm_a70c1e2c74e33f0f932c0ae0f4e78fc455c549572bc3c787ceb54af9821353ea`)

## workflows (7 claim(s))

- [observation/documented] Repository development practice: contributors need Rust/Cargo, Git, Node 20.18.0, npm 10.8.2, Yarn 1, Python 3.11, and a platform C/C++ toolchain, per the prerequisites list. -- evidence: [CONTRIBUTING.md#L28-L40](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L28-L40) (`clm_927d7ebbffbcd371ec8b066226e604517d360783d28588ffaf026704cac34dbc`)
- [observation/documented] Repository development practice: first-time setup runs scripts/pearai/setup-environment.sh (or .ps1 on Windows), and rebuilds use install-dependencies.sh or yarn. -- evidence: [CONTRIBUTING.md#L69-L76](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L69-L76), [CONTRIBUTING.md#L58-L65](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L58-L65) (`clm_41bae77e4a9aecf51d7d999c3c388a43b2739ee5463109b6d6f9ccc3a8a8697a`)
- [observation/documented] Repository development practice: unit tests run via ./scripts/test.sh from the pearai-app folder, and automated UI smoke tests are documented in test/smoke. -- evidence: [CONTRIBUTING.md#L197-L197](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L197-L197), [CONTRIBUTING.md#L199-L199](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L199-L199) (`clm_79b20f11d8101daa02ad924778231b81ad6a70906cff3f9da4911529f1498d07`)
- [observation/documented] Repository development practice: ESLint is used for linting, runnable via yarn eslint or as a VS Code task. -- evidence: [CONTRIBUTING.md#L203-L203](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L203-L203) (`clm_bb2ff11b25e7588a24a8f875895ee1b4728d6076352bfad0f4e72a4ab114ab00`)
- [observation/documented] Repository development practice: pull requests require signing a Contributor License Agreement once, one PR per issue with the issue linked, and small, focused changes. -- evidence: [CONTRIBUTING.md#L213-L213](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L213-L213), [CONTRIBUTING.md#L215-L215](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L215-L215) (`clm_498b297f86e78bff0600bef8649752ffc4d1fde8098282c7397ac1455ec367c0`)
- [observation/documented] Repository development practice: contributors should fork and use personal feature branches named yourname/branch-name even if they have push rights to the main repo. -- evidence: [CONTRIBUTING.md#L209-L209](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L209-L209) (`clm_327e6e20b42e33a4ce0a7438bc9c374d2cb7ef7b1ecce5769fbe35e23c29fa26`)
- [observation/documented] Repository development practice: packaging is manual, using gulp tasks like vscode-[platform] for win32, darwin, and linux targets, followed by extension packaging and manual integration steps. -- evidence: [CONTRIBUTING.md#L245-L245](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L245-L245), [CONTRIBUTING.md#L256-L262](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L256-L262), [CONTRIBUTING.md#L226-L226](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L226-L226), [CONTRIBUTING.md#L234-L235](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L234-L235), [CONTRIBUTING.md#L230-L230](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L230-L230) (`clm_e94ff437cbf5557738c4d09308e67d77eec09fb2c6527d96f627261885367fdc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Because PearAI is a VSCode fork, the README claims users get a familiar editor experience and can pick up where they left off. -- evidence: [README.md#L12-L14](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L12-L14) (`clm_de27e3248cf88433671c69a714bfb843a13285e705cab6fae735f71217e6a0c3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The README describes the stack as TypeScript/Electron.js, a Next.js/React landing page with Supabase auth, a Python Flask backend with Supabase, and Axiom for logging/telemetry. -- evidence: [README.md#L27-L31](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L27-L31) (`clm_8e50267e5249f49e19f04ff7030ef271f0bd1badb1717d56602da340ffb6e5bd`)
- [inference/documented] The README states Pear OSS is Apache 2.0 licensed, but the included LICENSE.txt is Microsoft's MIT license, suggesting inherited VSCode code remains under MIT alongside the project license claim. -- evidence: [LICENSE.txt#L3-L3](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/LICENSE.txt#L3-L3), [LICENSE.txt#L1-L1](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/LICENSE.txt#L1-L1), [README.md#L34-L34](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L34-L34) (`clm_f2cdd0c1f4886c125399e31b1a26c14f76e4c235b42da66b4f9276adecb1ee77`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

