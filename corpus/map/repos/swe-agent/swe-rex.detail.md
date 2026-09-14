# swe-agent/swe-rex -- full detail

[Back to orientation](swe-rex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/swe-agent/swe-rex/5c995c365dfb1fd5bc56fda688be5d8538f9931f/acc27ffd0a3eab30.json](../../../wiki/dossiers/swe-agent/swe-rex/5c995c365dfb1fd5bc56fda688be5d8538f9931f/acc27ffd0a3eab30.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Deployment classes start the target environment (e.g. a Docker container or AWS instance) and hand back a RemoteRuntime instance as the main interface for interacting with the environment. -- evidence: [docs/architecture.md#L3-L6](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L3-L6) (`clm_65b7ca57b7e04f54978d8e21dbd08f485533eae2ea969aa8c1e0e7a438c09007`)
- [observation/documented] A FastAPI server inside the container forwards requests from RemoteRuntime to LocalRuntime, which actually executes commands; the two classes share the same interface, are interchangeable, and exceptions from LocalRuntime are transferred transparently. -- evidence: [docs/architecture.md#L17-L21](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L17-L21) (`clm_fe5a5f4c8a1acaddc566865581f95a952cc0ee40235826056be2a4121408208a`)
- [observation/documented] Deployment configuration objects such as DockerDeploymentConfig configure deployments; e.g. a config is created with an image name and get_deployment() returns the deployment. -- evidence: [docs/api/deployments/config.md#L3-L3](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/api/deployments/config.md#L3-L3), [docs/api/deployments/config.md#L10-L12](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/api/deployments/config.md#L10-L12), [docs/api/deployments/config.md#L7-L8](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/api/deployments/config.md#L7-L8) (`clm_6ceea63df734e3e24a0c1b3ffedd73ccac359a5b4f3a6a546650c7bfbf9115f8`)

## design-choices (2 claim(s))

- [observation/documented] Agent code stays the same regardless of whether commands run locally, in Docker containers, on AWS remote machines, Modal, or other backends. -- evidence: [README.md#L14-L15](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L14-L15), [docs/index.md#L9-L10](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L9-L10) (`clm_97e3728d64d8e71b86e80ee6f665c875bb3f1e469962092042b26f1bef08bdb4`)
- [inference/documented] Because LocalRuntime can be used directly when code runs locally or in a sandboxed environment, the framework appears to support fully local usage without a remote deployment. -- evidence: [docs/architecture.md#L17-L21](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L17-L21) (`clm_d2c20d571421fb60071f751de608eb7a21801a80ff28e944bb806d40a4832008`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] SWE-ReX detects when shell commands finish, extracts output and exit code for the agent, supports interactive tools like ipython and gdb, and allows multiple parallel shell sessions. -- evidence: [docs/index.md#L14-L16](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L14-L16), [README.md#L19-L21](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L19-L21) (`clm_3c125130d14929067f1b29e0a3a8139b8ae2cc7a95f969b3db26c7bde99c7955`)

## interfaces (2 claim(s))

- [observation/documented] SWE-ReX exposes a runtime interface for interacting with sandboxed shell environments, letting an AI agent run arbitrary commands on arbitrary environments. -- evidence: [docs/index.md#L7-L7](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L7-L7), [README.md#L12-L12](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L12-L12) (`clm_13be2bd5dca4ca4b2a53cc04f88b8a5bb2f50c629f9f146f750d1b03d359389c`)
- [observation/documented] The Runtime class provides file read/write methods, an execute method for arbitrary commands, and a run_in_session method to run commands in an existing shell or interactive session. -- evidence: [docs/architecture.md#L23-L25](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L23-L25) (`clm_fca8982ef3065dd80bfa6153eda29e1ffd6dd3c6ddcb626f0e2906a25e96411c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The project advertises fast, massively parallel agent runs, citing large-benchmark evaluation and a demo of SWE-agent running on 30 SWE-bench instances in parallel. -- evidence: [docs/index.md#L27-L30](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L27-L30), [docs/index.md#L23-L25](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L23-L25), [README.md#L28-L30](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L28-L30), [README.md#L32-L32](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L32-L32) (`clm_445b71d725136ff071170149f409608a1e9a8249d2949602824188875d27eea9`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package installs via pip as swe-rex, with optional extras for modal, fargate, and daytona, plus a dev extra for development setup. -- evidence: [README.md#L45-L45](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L45-L45), [README.md#L49-L50](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L49-L50), [README.md#L40-L41](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L40-L41), [README.md#L43-L43](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L43-L43), [README.md#L47-L47](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L47-L47) (`clm_5e6f5b67bc5ad37ea6c55e0261fba661529fcabeae8c2039d558481c1ea6b606`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] SWE-ReX originated from the SWE-agent and SWE-agent enigma projects and aims to disentangle agent logic from infrastructure concerns. -- evidence: [docs/index.md#L23-L25](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L23-L25), [README.md#L25-L26](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L25-L26), [README.md#L28-L30](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L28-L30), [docs/index.md#L20-L21](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L20-L21) (`clm_676de505113dc5cf97e52690cb4429cf449013796825a64325754d909d618429`)

