---
access: public
aliases: []
claim_ids:
- clm_07c2fe0eeb7dd3b3e50d6f3e3ee07bae15f6d9cecd85064e41d47a2e6b999c73
- clm_0b9ab5d50e1a1a887dad8db121ddcb8a16735adc9e978b77f6c423fdc524bc73
- clm_1b7f04d36f08057e4252ac736d43103c706ea032ada072818dae44ce2581f1c8
- clm_2df4093a9cebba46c03cda5c437d2f064020739e09051d55a20bef9cc3697daa
- clm_344f4a70c35524f948999c54cdbcb5abe1a655f88a4b5fa9ff74b9db9c8b3301
- clm_484d61549efb9f11c5b3c1bec2129f01055e61a406dbd96c0ee7cb997cab2755
- clm_5f3e087ab877ed1d85c85610a931507edd27ae4fa49c0505cc1f3b7d3171131b
- clm_5f4dd3fb28de0a20c6bc36f2fdfa5f3b9fae36bb8c4e858cd13196f9b371a2de
- clm_6aed6b1346bc2f63ac9b03e51c7a40ed94412758edbe31afd24937aed829b2bf
- clm_82a1cb02c21a0a33e27a3559724a1a9b210edbb45df6e41b20a1aef123df90ed
- clm_8b3ad3c8cf0c9590c8d272909248dace1909b758a39054524c41ca50039c9b87
maturity: draft
page_id: pg_c3b4515bc7e45b549398e4745dc53fc7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1f6ea54678c454df938e5533f879339f
title: google-deepmind/code_contests/README.md @ fa7a4f8139aa
updated_at: '2026-09-14T03:53:47Z'
---

# google-deepmind/code_contests/README.md @ fa7a4f8139aa

<!-- rcw:begin owner=source:src_1f6ea54678c454df938e5533f879339f block=evidence -->
- The repository is supported on Linux compiled with clang; MacOS and Windows users have reported build errors in GitHub issues. [@claim:clm_07c2fe0eeb7dd3b3e50d6f3e3ee07bae15f6d9cecd85064e41d47a2e6b999c73]
- Problems include paired input/output test cases plus both correct and incorrect human solutions in a variety of languages. [@claim:clm_0b9ab5d50e1a1a887dad8db121ddcb8a16735adc9e978b77f6c423fdc524bc73]
- Execution code defaults to Python 3.9 and 2.7 at /usr/bin paths, configurable via flags defined in py_locations.cc such as --python3_path. [@claim:clm_1b7f04d36f08057e4252ac736d43103c706ea032ada072818dae44ce2581f1c8]
- Attached solutions are not guaranteed to compile or execute identically to their original contest environment; some fail compilation or produce sandbox violations, especially incorrect ones. [@claim:clm_2df4093a9cebba46c03cda5c437d2f064020739e09051d55a20bef9cc3697daa]
- Data is stored as ContestProblem protocol buffers in Riegeli format, with the schema and field documentation in contest_problem.proto. [@claim:clm_344f4a70c35524f948999c54cdbcb5abe1a655f88a4b5fa9ff74b9db9c8b3301]
- The full dataset is about 3 GiB and is downloaded from a Google Cloud Storage bucket using gsutil from the Cloud SDK. [@claim:clm_484d61549efb9f11c5b3c1bec2129f01055e61a406dbd96c0ee7cb997cab2755]
- CodeContests is a competitive programming dataset for machine learning, and it was used when training AlphaCode, which was published in Science with an arXiv preprint. [@claim:clm_5f3e087ab877ed1d85c85610a931507edd27ae4fa49c0505cc1f3b7d3171131b]
- Problems come from a variety of sources, including Aizu and AtCoder (via CodeNet), and CodeChef, Codeforces, and HackerEarth (via description2code). [@claim:clm_5f4dd3fb28de0a20c6bc36f2fdfa5f3b9fae36bb8c4e858cd13196f9b371a2de]
- The execution subdirectory contains code for executing a solution and evaluating whether it solves a problem, demonstrated by the solve_example target. [@claim:clm_6aed6b1346bc2f63ac9b03e51c7a40ed94412758edbe31afd24937aed829b2bf]
- The dataset has three splits: Training (sharded as code_contests_train.riegeli-*-of-00128), Validation, and Test, each with its own Riegeli filename. [@claim:clm_82a1cb02c21a0a33e27a3559724a1a9b210edbb45df6e41b20a1aef123df90ed]
- Example code iterates the dataset in C++ (print_names.cc) and Python (print_names_and_sources.py), runnable via bazel to print problem names and sources. [@claim:clm_8b3ad3c8cf0c9590c8d272909248dace1909b758a39054524c41ca50039c9b87]
<!-- rcw:end owner=source:src_1f6ea54678c454df938e5533f879339f block=evidence -->

## Researcher notes

