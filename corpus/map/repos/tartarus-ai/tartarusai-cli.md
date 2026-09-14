# tartarus-ai/tartarusai-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e708827a11df @ 36670dd6b96a642c

## Summary (orientation draft, not independently verified)

Evidence consists of README and SECURITY.md for tartarusai-cli, a terminal client for an 'uncensored' AI coding agent. The snapshot documents installation, quickstart, billing features, usage boundaries, and a vulnerability disclosure policy; no source code is present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The product is marketed as an uncensored coding agent with no policy filter, aimed at security research and edge-case automation that mainstream models reportedly refuse. -- evidence: [README.md#L29-L32](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L29-L32), [README.md#L86-L90](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L86-L90), [README.md#L7-L7](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L7-L7)
  - [observation/documented] The README states stated boundaries: no weaponized payloads, spyware, DRM bypass, or license cracking; lab PoCs for patched public CVEs are in scope, attacking systems you don't own is not. -- evidence: [README.md#L103-L109](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L103-L109)
- workflows (6 claim(s)):
  - [observation/documented] Installation on macOS/Linux is via a curl-piped setup script that installs to ~/.local/bin and auto-detects OS and CPU, falling back to a baseline build on CPUs without AVX2. -- evidence: [README.md#L42-L44](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L42-L44), [README.md#L46-L47](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L46-L47), [README.md#L40-L40](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L40-L40)
  - [observation/documented] Windows users download a zip from the latest GitHub release and run tartarus.exe; separate release artifacts exist for linux-x64, linux-x64-baseline, darwin-arm64, and darwin-x64. -- evidence: [README.md#L57-L59](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L57-L59), [README.md#L51-L55](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L51-L55), [README.md#L49-L49](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L49-L49)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] tartarusai-cli is a terminal client for TartarusAI, invoked as the 'tartarus' command, with a --help flag and docs hosted at dash.tartarusai.dev/docs. -- evidence: [README.md#L29-L32](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L29-L32), [README.md#L72-L72](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L72-L72), [README.md#L63-L70](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L63-L70)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The CLI ships as a single self-contained binary requiring no Python, pip, or Node runtime. -- evidence: [README.md#L38-L38](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L38-L38)
  - [observation/documented] The project is MIT-licensed, with LICENSE and NOTICE files referenced for full attribution. -- evidence: [README.md#L120-L120](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L120-L120), [README.md#L9-L11](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L9-L11)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(5 additional claim(s) omitted for length; see [full detail](tartarusai-cli.detail.md) for every claim.)

Metadata and full claim list: [full detail](tartarusai-cli.detail.md)
Human notes ([notes](tartarusai-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
