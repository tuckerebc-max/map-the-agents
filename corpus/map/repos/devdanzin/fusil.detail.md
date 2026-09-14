# devdanzin/fusil -- full detail

[Back to orientation](fusil.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/devdanzin/fusil/a7aa4e94bd8468f074d96fc6da6a76426b15b341/fe73214caf262697.json](../../../wiki/dossiers/devdanzin/fusil/a7aa4e94bd8468f074d96fc6da6a76426b15b341/fe73214caf262697.json)

## specifications (1 claim(s))

- [observation/documented] Fusil is a revival of Victor Stinner's fuzzing framework; only the Python fuzzing path is actively developed and tested, targeting crashes in CPython, C extensions, the Tier-2 JIT, and OOM error paths. -- evidence: [README.rst#L4-L8](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L4-L8) (`clm_60b3ac5775ed024c98b40a56ae98239d58535e737f39c04012ecf9226edc2c6f`)

## components (3 claim(s))

- [observation/documented] The architecture defines action agents (CreateProcess, StdoutFile, MangleFile, AutoMangle), network agents (TcpClient, UnixSocketClient, HttpServer), and probes such as FileWatch, CpuProbe, ProcessTimeWatch, WatchStdout, and Syslog. -- evidence: [doc/architecture.rst#L33-L36](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/architecture.rst#L33-L36), [doc/architecture.rst#L41-L50](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/architecture.rst#L41-L50), [doc/architecture.rst#L25-L29](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/architecture.rst#L25-L29) (`clm_b8013caa4297865fd780c1b22657b0b19dd6e42b0f4fbdb0cc2aee391cdeec05`)
- [observation/documented] Agents are objects that send and receive messages, are inactive by default until activate() is called, expose a live() method invoked each session step, and register event handlers via on_EVENT-style method names. -- evidence: [doc/agent.rst#L12-L15](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L12-L15), [doc/agent.rst#L4-L7](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L4-L7), [doc/agent.rst#L44-L44](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L44-L44), [doc/agent.rst#L28-L30](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/agent.rst#L28-L30) (`clm_80d223c57a2389a5c1e8eb4ee4960b0d1df8c97045dcf8c69fb4f890922b05ee`)
- [observation/documented] The fusil.c_tools module provides C code generation utilities: CodeC with addMain()/addFunction() for building functions, a compile() method, and FuzzyFunctionC with value generators like createInt32, createString, and createRandomBytes. -- evidence: [doc/c_tools.rst#L129-L132](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/c_tools.rst#L129-L132), [doc/c_tools.rst#L48-L62](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/c_tools.rst#L48-L62), [doc/c_tools.rst#L93-L93](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/c_tools.rst#L93-L93), [doc/c_tools.rst#L23-L40](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/c_tools.rst#L23-L40), [doc/c_tools.rst#L45-L46](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/c_tools.rst#L45-L46) (`clm_2f65d5ac2fd1e36d6113b6e549adcd9301c26808a6727e646ad7b866084866a3`)

## design-choices (2 claim(s))

- [observation/documented] Fusil is built as a small multi-agent system where agents communicate via asynchronous messages, and a per-session score drives the fuzzer's adaptive aggressivity. -- evidence: [README.rst#L16-L21](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L16-L21) (`clm_ded7ff974ce58369fa7759387d6c9730b6e88ff6e8e32a8cce2f061af2e66e66`)
- [observation/documented] A few settings lack CLI flags — session scoring thresholds, the memory limit, and the dedicated fusil-user sandbox user/group — and live as constants in fusil/config.py's FusilConfig class. -- evidence: [doc/configuration.rst#L23-L26](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L23-L26) (`clm_4592bb549b23f83420a8400a6ca4ce32f0fd9ec8acde3da26ae2be218a1d6006`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: tests use unittest (python -m unittest discover -s tests), with ruff check for linting and ruff format for formatting. -- evidence: [README.rst#L59-L59](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L59-L59), [README.rst#L61-L63](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L61-L63) (`clm_191a5614ab2402f5d699d7900088eae5657cf07b3f65a867ee3998e4e045380a`)
- [observation/documented] Repository development practice: a tech-debt plan records that CI (GitHub Actions running unittest and ruff check) was added after phases 0-7, with the suite green on Python 3.13 and 3.14 and grown to 308 tests. -- evidence: [TECH_DEBT_PLAN.md#L184-L196](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/TECH_DEBT_PLAN.md#L184-L196), [TECH_DEBT_PLAN.md#L180-L182](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/TECH_DEBT_PLAN.md#L180-L182) (`clm_dec7f2c48fba5db8049b41a98bc03c6b1bafcf7f72c2fc80a199cf92358425b0`)
- [observation/documented] Repository development practice: contributions to any part are welcome, but active development and CI focus on the Python fuzzer. -- evidence: [README.rst#L65-L66](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L65-L66) (`clm_fa84d85ecf8d778e6a1a395d20d8cda77656f12ea60ef365279a38c1ab249212`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Fusil is configured entirely through command-line options, grouped into categories like Input, Running, Fuzzing, OOM Fuzzing, and Logging; a former fusil.conf file mechanism was removed, making CLI options the single source of truth. -- evidence: [doc/configuration.rst#L10-L11](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L10-L11), [doc/configuration.rst#L5-L6](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L5-L6), [doc/configuration.rst#L15-L18](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/doc/configuration.rst#L15-L18) (`clm_23e5e36be1bea4a5d315788e05af8ba3eb6e80a3dea2483e106ebe7081911aca`)
- [observation/documented] Documented Python-fuzzer options include --only-c, --jit-fuzz, --oom-fuzz/--oom-seq, --deep-dive, and --no-memory-limit, with the full list in createFuzzerOptions in fusil/python/__init__.py. -- evidence: [README.rst#L40-L42](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L40-L42) (`clm_fe0191540bf2cb3c1e9271d58be76337b8f04db15609c3f685ae25a439977253`)

## memory-state (1 claim(s))

- [observation/documented] The memory cap was made ASan-safe: RLIMIT_AS is skipped when an ASan target is auto-detected or --no-memory-limit is set (since ASan reserves ~20 TB of virtual address space), relying on an external cgroup cap, while core-dump/nproc/nice limits are kept in all cases. -- evidence: [TECH_DEBT_PLAN.md#L9-L33](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/TECH_DEBT_PLAN.md#L9-L33), [TECH_DEBT_PLAN.md#L62-L74](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/TECH_DEBT_PLAN.md#L62-L74) (`clm_587c3096b2ca3b931c2af98fc7ee5650290eadd2b82b1fd0f197eb8ea7092126`)

## orchestration (1 claim(s))

- [observation/documented] Each session generates a standalone test script, runs it as a sandboxed child process with memory/cpu/process limits, dropped privileges, and redirected output, watching for crash signals and patterns like 'Fatal Python error' or AddressSanitizer output. -- evidence: [README.rst#L16-L21](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L16-L21) (`clm_7889ad8225b9dc8a01328b15aa024f432e59bf3feb0a542921defac6ac53f608`)

## tools-permissions (1 claim(s))

- [observation/documented] By default the fuzzer expects a dedicated unprivileged fusil user/group to drop privileges to; the --unsafe flag instead runs fuzzed children as the current user. -- evidence: [README.rst#L36-L38](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L36-L38) (`clm_36885c75776835396edd255e54c040c5cbc5b884977ec8d14c17afb9f3ac853f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Fusil requires Python 3.13+ and python-ptrace; numpy and h5py are optional extras supporting the argument generator, installed via pip install -e '.[numpy,h5py]'. -- evidence: [README.rst#L29-L30](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L29-L30), [README.rst#L32-L34](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L32-L34) (`clm_65ebc804fcc6cb3425d37d2aeb92ba373e5919dcbd8e1f139c5379484c53d1d7`)

## limitations (1 claim(s))

- [observation/documented] Historical non-Python fuzzers (firefox, php, mplayer) and subsystems like network, file/process mangling, and X11 are legacy and out of scope, kept under notworking/ directories and may not work as-is. -- evidence: [README.rst#L10-L14](https://github.com/devdanzin/fusil/blob/a7aa4e94bd8468f074d96fc6da6a76426b15b341/README.rst#L10-L14) (`clm_aa563e86ab6aca14362c8cb5e3bc1076e43a953299049eae66c3154e5d4ac9b1`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

