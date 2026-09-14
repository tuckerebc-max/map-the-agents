# swe-agent/swe-rex

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5c995c365dfb @ acc27ffd0a3eab30

## Summary (orientation draft, not independently verified)

SWE-ReX is a runtime interface for sandboxed shell environments that decouples agent code from execution backends (local, Docker, AWS, Modal), with interchangeable Remote/Local runtimes, parallel shell sessions, and pip-installable optional extras. Evidence is documentation-only; no code-inspected behavior is available in these slices.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Deployment classes start the target environment (e.g. a Docker container or AWS instance) and hand back a RemoteRuntime instance as the main interface for interacting with the environment. -- evidence: [docs/architecture.md#L3-L6](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L3-L6)
  - [observation/documented] A FastAPI server inside the container forwards requests from RemoteRuntime to LocalRuntime, which actually executes commands; the two classes share the same interface, are interchangeable, and exceptions from LocalRuntime are transferred transparently. -- evidence: [docs/architecture.md#L17-L21](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L17-L21)
- design-choices (2 claim(s)):
  - [observation/documented] Agent code stays the same regardless of whether commands run locally, in Docker containers, on AWS remote machines, Modal, or other backends. -- evidence: [README.md#L14-L15](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L14-L15), [docs/index.md#L9-L10](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L9-L10)
  - [inference/documented] Because LocalRuntime can be used directly when code runs locally or in a sandboxed environment, the framework appears to support fully local usage without a remote deployment. -- evidence: [docs/architecture.md#L17-L21](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L17-L21)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] SWE-ReX detects when shell commands finish, extracts output and exit code for the agent, supports interactive tools like ipython and gdb, and allows multiple parallel shell sessions. -- evidence: [docs/index.md#L14-L16](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L14-L16), [README.md#L19-L21](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L19-L21)
- interfaces (2 claim(s)):
  - [observation/documented] SWE-ReX exposes a runtime interface for interacting with sandboxed shell environments, letting an AI agent run arbitrary commands on arbitrary environments. -- evidence: [docs/index.md#L7-L7](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L7-L7), [README.md#L12-L12](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L12-L12)
  - [observation/documented] The Runtime class provides file read/write methods, an execute method for arbitrary commands, and a run_in_session method to run commands in an existing shell or interactive session. -- evidence: [docs/architecture.md#L23-L25](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/architecture.md#L23-L25)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The project advertises fast, massively parallel agent runs, citing large-benchmark evaluation and a demo of SWE-agent running on 30 SWE-bench instances in parallel. -- evidence: [docs/index.md#L27-L30](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L27-L30), [docs/index.md#L23-L25](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/docs/index.md#L23-L25), [README.md#L28-L30](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L28-L30), [README.md#L32-L32](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L32-L32)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The package installs via pip as swe-rex, with optional extras for modal, fargate, and daytona, plus a dev extra for development setup. -- evidence: [README.md#L45-L45](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L45-L45), [README.md#L49-L50](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L49-L50), [README.md#L40-L41](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L40-L41), [README.md#L43-L43](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L43-L43), [README.md#L47-L47](https://github.com/SWE-agent/SWE-ReX/blob/5c995c365dfb1fd5bc56fda688be5d8538f9931f/README.md#L47-L47)
More evidence: [full detail](swe-rex.detail.md)

Metadata and full claim list: [full detail](swe-rex.detail.md)
Human notes ([notes](swe-rex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
