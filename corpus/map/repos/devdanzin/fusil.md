# devdanzin/fusil

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a7aa4e94bd84 @ fe73214caf262697

## Summary (orientation draft, not independently verified)

Fusil is a revived Python-focused fuzzing framework built as a multi-agent system that generates and runs sandboxed test scripts against CPython targets. Evidence covers its architecture, CLI configuration, sandbox/permission model, dependencies, and documented development workflow.

## Source coverage

Source coverage (partial): 6 of 35 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Fusil is a revival of Victor Stinner's fuzzing framework; only the Python fuzzing path is actively developed and tested, targeting crashes in CPython, C extensions, the Tier-2 JIT, and OOM error paths. -- evidence: [README.rst#L4-L8](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L4-L8)
- components (3 claim(s)):
  - [observation/documented] The architecture defines action agents (CreateProcess, StdoutFile, MangleFile, AutoMangle), network agents (TcpClient, UnixSocketClient, HttpServer), and probes such as FileWatch, CpuProbe, ProcessTimeWatch, WatchStdout, and Syslog. -- evidence: [doc/architecture.rst#L33-L36](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/architecture.rst#L33-L36), [doc/architecture.rst#L41-L50](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/architecture.rst#L41-L50), [doc/architecture.rst#L25-L29](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/architecture.rst#L25-L29)
  - [observation/documented] Agents are objects that send and receive messages, are inactive by default until activate() is called, expose a live() method invoked each session step, and register event handlers via on_EVENT-style method names. -- evidence: [doc/agent.rst#L12-L15](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L12-L15), [doc/agent.rst#L4-L7](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L4-L7), [doc/agent.rst#L44-L44](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L44-L44), [doc/agent.rst#L28-L30](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L28-L30)
- design-choices (2 claim(s)):
  - [observation/documented] Fusil is built as a small multi-agent system where agents communicate via asynchronous messages, and a per-session score drives the fuzzer's adaptive aggressivity. -- evidence: [README.rst#L16-L21](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L16-L21)
  - [observation/documented] A few settings lack CLI flags — session scoring thresholds, the memory limit, and the dedicated fusil-user sandbox user/group — and live as constants in fusil/config.py's FusilConfig class. -- evidence: [doc/configuration.rst#L23-L26](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L23-L26)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: tests use unittest (python -m unittest discover -s tests), with ruff check for linting and ruff format for formatting. -- evidence: [README.rst#L59-L59](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L59-L59), [README.rst#L61-L63](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L61-L63)
  - [observation/documented] Repository development practice: a tech-debt plan records that CI (GitHub Actions running unittest and ruff check) was added after phases 0-7, with the suite green on Python 3.13 and 3.14 and grown to 308 tests. -- evidence: [TECH_DEBT_PLAN.md#L184-L196](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/TECH_DEBT_PLAN.md#L184-L196), [TECH_DEBT_PLAN.md#L180-L182](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/TECH_DEBT_PLAN.md#L180-L182)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Fusil is configured entirely through command-line options, grouped into categories like Input, Running, Fuzzing, OOM Fuzzing, and Logging; a former fusil.conf file mechanism was removed, making CLI options the single source of truth. -- evidence: [doc/configuration.rst#L10-L11](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L10-L11), [doc/configuration.rst#L5-L6](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L5-L6), [doc/configuration.rst#L15-L18](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L15-L18)
  - [observation/documented] Documented Python-fuzzer options include --only-c, --jit-fuzz, --oom-fuzz/--oom-seq, --deep-dive, and --no-memory-limit, with the full list in createFuzzerOptions in fusil/python/__init__.py. -- evidence: [README.rst#L40-L42](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L40-L42)
- memory-state (1 claim(s)):
More evidence: [full detail](fusil.detail.md)

Metadata and full claim list: [full detail](fusil.detail.md)
Human notes ([notes](fusil.notes.md), never overwritten by build)

[Back to map index](../../index.md)
