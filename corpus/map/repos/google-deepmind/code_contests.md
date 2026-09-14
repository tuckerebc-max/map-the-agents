# google-deepmind/code_contests

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fa7a4f8139aa @ 31bd29e415268529

## Summary (orientation draft, not independently verified)

CodeContests is a competitive-programming ML dataset (used to train AlphaCode) with problems, tests, and solutions from several judges, distributed as Riegeli protocol buffers with C++/Python tooling for iterating and evaluating solutions. Contributor instructions cover PRs, CLAs, and code review.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (5 claim(s)):
  - [observation/documented] CodeContests is a competitive programming dataset for machine learning, and it was used when training AlphaCode, which was published in Science with an arXiv preprint. -- evidence: [README.md#L3-L5](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L3-L5)
  - [observation/documented] Problems come from a variety of sources, including Aizu and AtCoder (via CodeNet), and CodeChef, Codeforces, and HackerEarth (via description2code). -- evidence: [README.md#L9-L15](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L9-L15), [README.md#L7-L7](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L7-L7)
- components (2 claim(s)):
  - [observation/documented] Example code iterates the dataset in C++ (print_names.cc) and Python (print_names_and_sources.py), runnable via bazel to print problem names and sources. -- evidence: [README.md#L58-L61](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L58-L61), [README.md#L52-L56](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L52-L56)
  - [observation/documented] The execution subdirectory contains code for executing a solution and evaluating whether it solves a problem, demonstrated by the solve_example target. -- evidence: [README.md#L73-L75](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L73-L75), [README.md#L77-L80](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L77-L80)
- design-choices (1 claim(s)):
  - [observation/documented] Execution code defaults to Python 3.9 and 2.7 at /usr/bin paths, configurable via flags defined in py_locations.cc such as --python3_path. -- evidence: [README.md#L92-L96](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L92-L96), [README.md#L87-L90](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L87-L90)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions go through GitHub pull requests, all submissions require review, and a Contributor License Agreement must accompany contributions. -- evidence: [CONTRIBUTING.md#L21-L24](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/CONTRIBUTING.md#L21-L24), [CONTRIBUTING.md#L5-L5](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/CONTRIBUTING.md#L5-L5), [CONTRIBUTING.md#L9-L13](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/CONTRIBUTING.md#L9-L13)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The full dataset is about 3 GiB and is downloaded from a Google Cloud Storage bucket using gsutil from the Cloud SDK. -- evidence: [README.md#L36-L38](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L36-L38), [README.md#L32-L34](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L32-L34)
  - [observation/documented] The repository is supported on Linux compiled with clang; MacOS and Windows users have reported build errors in GitHub issues. -- evidence: [README.md#L128-L128](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L128-L128), [README.md#L22-L24](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L22-L24), [README.md#L133-L134](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L133-L134), [README.md#L130-L131](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L130-L131)
- limitations (1 claim(s)):
  - [observation/documented] Attached solutions are not guaranteed to compile or execute identically to their original contest environment; some fail compilation or produce sandbox violations, especially incorrect ones. -- evidence: [README.md#L114-L114](https://github.com/google-deepmind/code_contests/blob/fa7a4f8139aab08362503f3344778eb86901709a/README.md#L114-L114)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](code_contests.detail.md) for every claim.)

Metadata and full claim list: [full detail](code_contests.detail.md)
Human notes ([notes](code_contests.notes.md), never overwritten by build)

[Back to map index](../../index.md)
