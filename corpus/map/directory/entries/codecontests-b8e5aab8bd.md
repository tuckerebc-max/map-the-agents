# CodeContests (`codecontests`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: google-deepmind
- License: Apache-2.0
- Language: C++
- Interface: install=binary
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [google-deepmind/code_contests](../../repos/google-deepmind/code_contests.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A competitive programming dataset used to train DeepMind's AlphaCode, containing programming problems from multiple contest sites (Aizu, AtCoder, CodeChef, Codeforces, HackerEarth) with paired test cases and both correct/incorrect human solutions in multiple languages.

(captured site page body (agents/codecontests.md), not a verified repo-code finding)
CodeContests is the dataset DeepMind built to train and evaluate AlphaCode, the competitive-programming system published in Science in 2022. It aggregates problems from five contest platforms — Aizu, AtCoder, CodeChef, Codeforces, and HackerEarth — pairing each problem with test cases and both correct and incorrect human solutions in multiple languages, the negative examples being deliberate: models learn from failed submissions as well as correct ones. The roughly 3 GiB dataset lives on Google Cloud Storage as ContestProblem protocol buffers in Riegeli format with train/validation/test splits, and the repository provides C++ and Python utilities built with Bazel for loading, executing, and evaluating candidate solutions. The repository was archived on December 6, 2024 and is read-only.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codecontests.md)
