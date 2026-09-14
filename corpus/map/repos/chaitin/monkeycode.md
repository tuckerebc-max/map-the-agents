# chaitin/monkeycode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a67aef068778 @ 2727223fcc195893

## Summary (orientation draft, not independently verified)

MonkeyCode is documented as an open-source (AGPL-3.0) enterprise AI development platform with cloud dev environments, multi-model support, and mobile access; CONTEXT.md defines a single-instance admin console with credit billing, and a plan document proposes a design-workflow feature set largely not yet shipped. Evidence coverage: 211 of 369 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 47 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] MonkeyCode is described as an open-source enterprise-grade AI development platform combining development environment management, AI model/task management, and project requirement management. -- evidence: [README.md#L23-L23](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L23-L23)
  - [observation/documented] The MonkeyAI admin console manages user identity, AI resources, session usage, credit billing, and admin audit within a single instance, explicitly without multi-tenancy. -- evidence: [CONTEXT.md#L3-L3](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] Tasks run in server-side cloud development environments; build, test, and preview workflows are executed in the cloud rather than on local machines. -- evidence: [README.md#L61-L66](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L61-L66)
  - [observation/documented] AI resources include models, skills, rules, MCP services, individually toggleable MCP tools, and Experts (system-level agent presets combining role prompts, MCP tools, rules, and skills). -- evidence: [CONTEXT.md#L71-L73](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L71-L73), [CONTEXT.md#L75-L77](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L75-L77), [CONTEXT.md#L79-L81](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L79-L81), [CONTEXT.md#L87-L89](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L87-L89), [CONTEXT.md#L83-L85](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L83-L85), [CONTEXT.md#L67-L69](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L67-L69)
- design-choices (2 claim(s)):
  - [observation/documented] The product targets deployment inside enterprise networks shared with an R&D team, with an online hosted environment (managed dev environments, built-in LLMs, mobile support) as an alternative. -- evidence: [README.md#L25-L26](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L25-L26)
  - [observation/documented] Users are organized in a tree expanding from a unique root group; group authorization covers descendant groups, and quotas inherit from the nearest parent group when unset. -- evidence: [CONTEXT.md#L105-L107](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L105-L107), [CONTEXT.md#L15-L17](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/CONTEXT.md#L15-L17)
- workflows (1 claim(s)):
  - [observation/documented] Self-hosted install is via a curl-fetched bash script, with recommended minimums of 2C/4GB/40GB for the console and 8C/16GB/100GB for development-environment hosts. -- evidence: [README.md#L80-L81](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L80-L81), [README.md#L85-L87](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L85-L87)
- skills-patterns (1 claim(s)):
  - [observation/documented] A design-workflow plan proposes extracting design patterns via Skills/Atoms (code-import, design-extract, token-map, rewrite-plan), saved as Design System Packages with revisions so re-extraction creates a new revision rather than overwriting. -- evidence: [docs/plans/monkeydesign-design-workflow.md#L334-L334](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L334-L334), [docs/plans/monkeydesign-design-workflow.md#L325-L325](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L325-L325), [docs/plans/monkeydesign-design-workflow.md#L327-L332](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L327-L332), [docs/plans/monkeydesign-design-workflow.md#L396-L396](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L396-L396)
- interfaces (2 claim(s)):
  - [observation/documented] Native iOS and Android support is claimed, keeping PC and mobile data in sync so agents can continue running tasks while the user is away. -- evidence: [README.md#L61-L66](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/README.md#L61-L66)
  - [inference/documented] The plan proposes new agent-client protocol messages (design/start-choice, template/reference/pattern selection, redesign-level) because plain AskUserQuestion cannot carry images; these appear to be proposals, not shipped behavior. -- evidence: [docs/plans/monkeydesign-design-workflow.md#L571-L571](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L571-L571), [docs/plans/monkeydesign-design-workflow.md#L575-L583](https://github.com/chaitin/MonkeyCode/blob/a67aef068778d4be596ca1cf793f7be25c408a26/docs/plans/monkeydesign-design-workflow.md#L575-L583)
- memory-state (2 claim(s)):
More evidence: [full detail](monkeycode.detail.md)

Metadata and full claim list: [full detail](monkeycode.detail.md)
Human notes ([notes](monkeycode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
