# trypear/pearai-app

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d930f0233c14 @ 145d5fa987766159

## Summary (orientation draft, not independently verified)

PearAI is described as a fork of VSCode, with its main functionality in a separate submodule (pearai-submodule) that is itself a fork of Continue. The README states Pear has context on the user's codebase so questions can be asked directly, with code stored locally on the user's computer.

## Source coverage

Source coverage (partial): 4 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] PearAI is described as a fork of VSCode, with its main functionality in a separate submodule (pearai-submodule) that is itself a fork of Continue. -- evidence: [README.md#L5-L5](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L5-L5), [CONTRIBUTING.md#L84-L86](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L84-L86), [CONTRIBUTING.md#L15-L15](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L15-L15)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The README states Pear has context on the user's codebase so questions can be asked directly, with code stored locally on the user's computer. -- evidence: [README.md#L12-L14](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L12-L14)
- workflows (7 claim(s)):
  - [observation/documented] Repository development practice: contributors need Rust/Cargo, Git, Node 20.18.0, npm 10.8.2, Yarn 1, Python 3.11, and a platform C/C++ toolchain, per the prerequisites list. -- evidence: [CONTRIBUTING.md#L28-L40](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L28-L40)
  - [observation/documented] Repository development practice: first-time setup runs scripts/pearai/setup-environment.sh (or .ps1 on Windows), and rebuilds use install-dependencies.sh or yarn. -- evidence: [CONTRIBUTING.md#L69-L76](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L69-L76), [CONTRIBUTING.md#L58-L65](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/CONTRIBUTING.md#L58-L65)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Because PearAI is a VSCode fork, the README claims users get a familiar editor experience and can pick up where they left off. -- evidence: [README.md#L12-L14](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L12-L14)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The README describes the stack as TypeScript/Electron.js, a Next.js/React landing page with Supabase auth, a Python Flask backend with Supabase, and Axiom for logging/telemetry. -- evidence: [README.md#L27-L31](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L27-L31)
  - [inference/documented] The README states Pear OSS is Apache 2.0 licensed, but the included LICENSE.txt is Microsoft's MIT license, suggesting inherited VSCode code remains under MIT alongside the project license claim. -- evidence: [LICENSE.txt#L3-L3](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/LICENSE.txt#L3-L3), [LICENSE.txt#L1-L1](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/LICENSE.txt#L1-L1), [README.md#L34-L34](https://github.com/trypear/pearai-app/blob/d930f0233c14668df9f85c6a78a81828f4251194/README.md#L34-L34)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(5 additional claim(s) omitted for length; see [full detail](pearai-app.detail.md) for every claim.)

Metadata and full claim list: [full detail](pearai-app.detail.md)
Human notes ([notes](pearai-app.notes.md), never overwritten by build)

[Back to map index](../../index.md)
