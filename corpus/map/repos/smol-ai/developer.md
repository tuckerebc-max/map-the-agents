# smol-ai/developer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a6747d1a6ccd @ 7aee3279a6f05064

## Summary (orientation draft, not independently verified)

The evidence is the README and prompt.md of smol-ai/developer at one commit, describing a 'junior developer' agent that scaffolds codebases from a prompt, usable in git-repo, library, and Agent Protocol API modes. No source code files are included, so claims are documentation-based.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The tool is described as a 'junior developer' agent that scaffolds an entire codebase from a product spec, or provides building blocks to embed a similar agent in other apps. -- evidence: [readme.md#L20-L21](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L20-L21), [readme.md#L18-L18](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L18-L18)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] For whole-program coherence, the tool adds an intermediate step generating shared_dependencies.md and insists on using it when generating each file, since hallucinated cross-file dependencies break programs. -- evidence: [readme.md#L206-L224](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L206-L224)
  - [observation/documented] The workflow is human-in-the-loop: the human writes/extends a markdown prompt, runs generated code, and pastes errors back into the prompt; debugger.py reads the whole codebase to suggest specific fixes. -- evidence: [readme.md#L60-L67](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L60-L67), [readme.md#L58-L58](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L58-L58)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The bundled prompt.md is a detailed spec for a Chrome Manifest V3 extension that summarizes page content via the Anthropic Claude API, choosing claude-instant-v1 or the 100k model based on content length. -- evidence: [prompt.md#L1-L1](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/prompt.md#L1-L1), [prompt.md#L49-L69](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/prompt.md#L49-L69)
- interfaces (4 claim(s)):
  - [observation/documented] In git repo mode the CLI is run as 'python main.py' with a prompt string argument, defaulting to gpt-4-0613, and supports --prompt and --debug flags. -- evidence: [readme.md#L42-L44](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L42-L44), [readme.md#L38-L38](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L38-L38)
  - [observation/documented] Library mode exposes functions plan(), specify_file_paths(), and generate_code_sync() from smol_dev.prompts, plus an async generate_code() variant, installable via pip as smol_dev. -- evidence: [readme.md#L99-L100](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L99-L100), [readme.md#L79-L81](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L79-L81), [readme.md#L102-L104](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L102-L104), [readme.md#L85-L86](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L85-L86), [readme.md#L90-L90](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L90-L90)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The repo is installed with poetry ('poetry install') in git repo mode, and the library is published as the pip package smol_dev. -- evidence: [readme.md#L79-L81](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L79-L81), [readme.md#L33-L35](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L33-L35)
- limitations (3 claim(s)):
  - [observation/documented] Generation is slow: the README reports roughly 2-4 minutes to generate a program with GPT4 even with parallelization via Modal, occasionally spiking higher. -- evidence: [readme.md#L234-L234](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L234-L234)
More evidence: [full detail](developer.detail.md)

Metadata and full claim list: [full detail](developer.detail.md)
Human notes ([notes](developer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
