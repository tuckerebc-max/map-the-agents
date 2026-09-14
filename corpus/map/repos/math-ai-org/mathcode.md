# math-ai-org/mathcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6774236e088b @ c2426028962b88f5

## Summary (orientation draft, not independently verified)

The snapshot documents MathCode, a terminal AI coding assistant with built-in Lean proof capabilities, distributed as a self-contained release bundle with CLI, browser UI, theorem/axiom libraries, and extension mechanisms. Evidence is README documentation only; no source code or development-practice guides appear in the provided slices. Evidence coverage: 150 of 228 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 23 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

23 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] MathCode is described as a terminal AI coding assistant with built-in Lean capabilities: it can inspect goals, check candidates, search declarations, and verify finished proofs interactively. -- evidence: [README.md#L18-L20](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L18-L20)
- components (1 claim(s)):
  - [observation/documented] For Lean work the agent chooses among four atomic tools: LeanGoal (inspect a source position), LeanCheck (compile a file or candidate with structured feedback), LeanSearch (query one provider), and LeanVerify (strict final check; only data.verified=true certifies completion). -- evidence: [README.md#L439-L442](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L439-L442)
- design-choices (2 claim(s)):
  - [observation/documented] The optional /lean skill gives guidance without imposing a fixed phase, tactic order, retry budget, or planner; former fixed controllers were removed and are not release entrypoints or model-visible tools. -- evidence: [README.md#L444-L455](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L444-L455)
  - [observation/documented] The default backend path uses Codex/OpenAI (GPT-6 Astra at medium effort per .env.example); an Anthropic-compatible backend can be selected with MATHCODE_USE_OPENAI=0 plus Anthropic credentials. -- evidence: [README.md#L505-L507](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L505-L507), [README.md#L516-L516](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L516-L516), [README.md#L518-L519](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L518-L519), [README.md#L509-L514](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L509-L514), [README.md#L521-L523](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L521-L523)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup.sh downloads or repairs the bundled runtime, verifies SHA256SUMS entries, creates .env from .env.example, installs a user-local launcher, and creates tools/, plugins/, and skills/ directories. -- evidence: [README.md#L66-L73](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L66-L73), [README.md#L52-L62](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L52-L62)
  - [observation/documented] Repository development practice: maintenance commands include setup.sh --install-lean, --status (health checks on binaries, bundled rg, and Lean readiness), --clean (preserving LeanFormalizations/ and vault data), and --help. -- evidence: [README.md#L125-L130](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L125-L130), [README.md#L134-L138](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L134-L138), [README.md#L140-L142](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L140-L142)
- skills-patterns (3 claim(s)):
  - [observation/documented] Project-local skills load from .mathcode/skills/<name>/SKILL.md, one directory per skill; standalone skills/*.md files are not loaded. -- evidence: [README.md#L476-L477](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L476-L477)
  - [observation/documented] Python tools with YAML frontmatter dropped in tools/ are auto-discovered at startup; three analysis tools ship bundled (axiom-checker, lib-search, proof-stats), overridable by workspace-local tools of the same name. -- evidence: [README.md#L483-L486](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L483-L486), [README.md#L481-L481](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L481-L481)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI accepts a prompt flag (e.g. mathcode -p "..."), piped stdin, and --help; a bundle-local ./run wrapper provides the same interface before the shell profile is reloaded. -- evidence: [README.md#L158-L162](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L158-L162), [README.md#L170-L174](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L170-L174)
More evidence: [full detail](mathcode.detail.md)

Metadata and full claim list: [full detail](mathcode.detail.md)
Human notes ([notes](mathcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
