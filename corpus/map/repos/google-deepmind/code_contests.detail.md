# google-deepmind/code_contests -- full detail

[Back to orientation](code_contests.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/google-deepmind/code_contests/fa7a4f8139aab08362503f3344778eb86901709a/31bd29e415268529.json](../../../wiki/dossiers/google-deepmind/code_contests/fa7a4f8139aab08362503f3344778eb86901709a/31bd29e415268529.json)

## specifications (5 claim(s))

- [observation/documented] CodeContests is a competitive programming dataset for machine learning, and it was used when training AlphaCode, which was published in Science with an arXiv preprint. -- evidence: [README.md#L3-L5](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L3-L5) (`clm_5f3e087ab877ed1d85c85610a931507edd27ae4fa49c0505cc1f3b7d3171131b`)
- [observation/documented] Problems come from a variety of sources, including Aizu and AtCoder (via CodeNet), and CodeChef, Codeforces, and HackerEarth (via description2code). -- evidence: [README.md#L9-L15](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L9-L15), [README.md#L7-L7](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L7-L7) (`clm_5f4dd3fb28de0a20c6bc36f2fdfa5f3b9fae36bb8c4e858cd13196f9b371a2de`)
- [observation/documented] Problems include paired input/output test cases plus both correct and incorrect human solutions in a variety of languages. -- evidence: [README.md#L17-L18](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L17-L18) (`clm_0b9ab5d50e1a1a887dad8db121ddcb8a16735adc9e978b77f6c423fdc524bc73`)
- [observation/documented] The dataset has three splits: Training (sharded as code_contests_train.riegeli-*-of-00128), Validation, and Test, each with its own Riegeli filename. -- evidence: [README.md#L44-L44](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L44-L44), [README.md#L46-L50](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L46-L50) (`clm_82a1cb02c21a0a33e27a3559724a1a9b210edbb45df6e41b20a1aef123df90ed`)
- [observation/documented] Data is stored as ContestProblem protocol buffers in Riegeli format, with the schema and field documentation in contest_problem.proto. -- evidence: [README.md#L40-L42](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L40-L42) (`clm_344f4a70c35524f948999c54cdbcb5abe1a655f88a4b5fa9ff74b9db9c8b3301`)

## components (2 claim(s))

- [observation/documented] Example code iterates the dataset in C++ (print_names.cc) and Python (print_names_and_sources.py), runnable via bazel to print problem names and sources. -- evidence: [README.md#L58-L61](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L58-L61), [README.md#L52-L56](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L52-L56) (`clm_8b3ad3c8cf0c9590c8d272909248dace1909b758a39054524c41ca50039c9b87`)
- [observation/documented] The execution subdirectory contains code for executing a solution and evaluating whether it solves a problem, demonstrated by the solve_example target. -- evidence: [README.md#L73-L75](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L73-L75), [README.md#L77-L80](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L77-L80) (`clm_6aed6b1346bc2f63ac9b03e51c7a40ed94412758edbe31afd24937aed829b2bf`)

## design-choices (1 claim(s))

- [observation/documented] Execution code defaults to Python 3.9 and 2.7 at /usr/bin paths, configurable via flags defined in py_locations.cc such as --python3_path. -- evidence: [README.md#L92-L96](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L92-L96), [README.md#L87-L90](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L87-L90) (`clm_1b7f04d36f08057e4252ac736d43103c706ea032ada072818dae44ce2581f1c8`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions go through GitHub pull requests, all submissions require review, and a Contributor License Agreement must accompany contributions. -- evidence: [CONTRIBUTING.md#L21-L24](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/CONTRIBUTING.md#L21-L24), [CONTRIBUTING.md#L5-L5](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/CONTRIBUTING.md#L5-L5), [CONTRIBUTING.md#L9-L13](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/CONTRIBUTING.md#L9-L13) (`clm_26fd0aa196864f80c78d750a6cf81ab7d1158e9aa714f66b80ad88b32b8371d4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The full dataset is about 3 GiB and is downloaded from a Google Cloud Storage bucket using gsutil from the Cloud SDK. -- evidence: [README.md#L36-L38](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L36-L38), [README.md#L32-L34](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L32-L34) (`clm_484d61549efb9f11c5b3c1bec2129f01055e61a406dbd96c0ee7cb997cab2755`)
- [observation/documented] The repository is supported on Linux compiled with clang; MacOS and Windows users have reported build errors in GitHub issues. -- evidence: [README.md#L128-L128](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L128-L128), [README.md#L22-L24](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L22-L24), [README.md#L133-L134](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L133-L134), [README.md#L130-L131](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L130-L131) (`clm_07c2fe0eeb7dd3b3e50d6f3e3ee07bae15f6d9cecd85064e41d47a2e6b999c73`)

## limitations (1 claim(s))

- [observation/documented] Attached solutions are not guaranteed to compile or execute identically to their original contest environment; some fail compilation or produce sandbox violations, especially incorrect ones. -- evidence: [README.md#L114-L114](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L114-L114) (`clm_2df4093a9cebba46c03cda5c437d2f064020739e09051d55a20bef9cc3697daa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

