---
access: public
aliases: []
claim_ids:
- clm_191a5614ab2402f5d699d7900088eae5657cf07b3f65a867ee3998e4e045380a
- clm_36885c75776835396edd255e54c040c5cbc5b884977ec8d14c17afb9f3ac853f
- clm_60b3ac5775ed024c98b40a56ae98239d58535e737f39c04012ecf9226edc2c6f
- clm_65ebc804fcc6cb3425d37d2aeb92ba373e5919dcbd8e1f139c5379484c53d1d7
- clm_7889ad8225b9dc8a01328b15aa024f432e59bf3feb0a542921defac6ac53f608
- clm_aa563e86ab6aca14362c8cb5e3bc1076e43a953299049eae66c3154e5d4ac9b1
- clm_ded7ff974ce58369fa7759387d6c9730b6e88ff6e8e32a8cce2f061af2e66e66
- clm_fa84d85ecf8d778e6a1a395d20d8cda77656f12ea60ef365279a38c1ab249212
- clm_fe0191540bf2cb3c1e9271d58be76337b8f04db15609c3f685ae25a439977253
maturity: draft
page_id: pg_3b100d00307053a0873b6283b72541b6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d36a932791495f3ca67aa940900a09c0
title: devdanzin/fusil/README.rst @ a7aa4e94bd84
updated_at: '2026-09-14T03:46:53Z'
---

# devdanzin/fusil/README.rst @ a7aa4e94bd84

<!-- rcw:begin owner=source:src_d36a932791495f3ca67aa940900a09c0 block=evidence -->
- Repository development practice: tests use unittest (python -m unittest discover -s tests), with ruff check for linting and ruff format for formatting. [@claim:clm_191a5614ab2402f5d699d7900088eae5657cf07b3f65a867ee3998e4e045380a]
- By default the fuzzer expects a dedicated unprivileged fusil user/group to drop privileges to; the --unsafe flag instead runs fuzzed children as the current user. [@claim:clm_36885c75776835396edd255e54c040c5cbc5b884977ec8d14c17afb9f3ac853f]
- Fusil is a revival of Victor Stinner's fuzzing framework; only the Python fuzzing path is actively developed and tested, targeting crashes in CPython, C extensions, the Tier-2 JIT, and OOM error paths. [@claim:clm_60b3ac5775ed024c98b40a56ae98239d58535e737f39c04012ecf9226edc2c6f]
- Fusil requires Python 3.13+ and python-ptrace; numpy and h5py are optional extras supporting the argument generator, installed via pip install -e '.[numpy,h5py]'. [@claim:clm_65ebc804fcc6cb3425d37d2aeb92ba373e5919dcbd8e1f139c5379484c53d1d7]
- Each session generates a standalone test script, runs it as a sandboxed child process with memory/cpu/process limits, dropped privileges, and redirected output, watching for crash signals and patterns like 'Fatal Python error' or AddressSanitizer output. [@claim:clm_7889ad8225b9dc8a01328b15aa024f432e59bf3feb0a542921defac6ac53f608]
- Historical non-Python fuzzers (firefox, php, mplayer) and subsystems like network, file/process mangling, and X11 are legacy and out of scope, kept under notworking/ directories and may not work as-is. [@claim:clm_aa563e86ab6aca14362c8cb5e3bc1076e43a953299049eae66c3154e5d4ac9b1]
- Fusil is built as a small multi-agent system where agents communicate via asynchronous messages, and a per-session score drives the fuzzer's adaptive aggressivity. [@claim:clm_ded7ff974ce58369fa7759387d6c9730b6e88ff6e8e32a8cce2f061af2e66e66]
- Repository development practice: contributions to any part are welcome, but active development and CI focus on the Python fuzzer. [@claim:clm_fa84d85ecf8d778e6a1a395d20d8cda77656f12ea60ef365279a38c1ab249212]
- Documented Python-fuzzer options include --only-c, --jit-fuzz, --oom-fuzz/--oom-seq, --deep-dive, and --no-memory-limit, with the full list in createFuzzerOptions in fusil/python/__init__.py. [@claim:clm_fe0191540bf2cb3c1e9271d58be76337b8f04db15609c3f685ae25a439977253]
<!-- rcw:end owner=source:src_d36a932791495f3ca67aa940900a09c0 block=evidence -->

## Researcher notes

