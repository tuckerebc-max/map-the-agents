# structuredllm/syncode

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: uiuc-focal-lab/syncode (github id 687211074).
Latest snapshot: commit 4d6c110a028d @ 4cf25e2790b4916d

## Summary (orientation draft, not independently verified)

SynCode is a grammar-guided constrained-decoding framework for LLMs, usable as a HuggingFace logit processor or via a SynCode class/CLI, with built-in EBNF grammars and a DFA mask store for token masking. All claims below are supported by the cited README and requirements slices.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] SynCode is a framework for grammar-guided LLM generation, claimed to ensure output is syntactically valid with respect to a context-free grammar, with stated soundness and completeness guarantees. -- evidence: [README.md#L24-L26](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L24-L26)
- components (1 claim(s)):
  - [observation/documented] Built-in CFGs are provided for Python, Go, Java, SQL, Math, JSON, and more, stored in the syncode/parsers/grammars directory. -- evidence: [README.md#L33-L33](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L33-L33), [README.md#L42-L48](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L42-L48)
- design-choices (2 claim(s)):
  - [observation/documented] SynCode's core is an offline-constructed DFA mask store built from regular expressions of grammar terminals, used with an incremental parser's accept sequences and remainder to mask invalid tokens during decoding. -- evidence: [README.md#L418-L418](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L418-L418)
  - [observation/documented] Custom grammars can be supplied in an EBNF syntax adapted from Lark, either as a string of rules or a path to a .lark file. -- evidence: [README.md#L345-L345](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L345-L345), [README.md#L246-L246](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L246-L246)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] SynCode can be used as a HuggingFace logit processor: SyncodeLogitsProcessor is imported and passed to model.generate via the logits_processor argument. -- evidence: [README.md#L77-L77](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L77-L77), [README.md#L79-L91](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L79-L91)
  - [observation/documented] A SynCode class offers an infer() method taking prompt and task_id; if neither is given, it reads user input via stdin. -- evidence: [README.md#L105-L105](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L105-L105), [README.md#L95-L101](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L95-L101), [README.md#L103-L103](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L103-L103)
- memory-state (1 claim(s)):
  - [observation/documented] Cache directories can be configured via HF_CACHE and SYNCODE_CACHE environment variables, with defaults used otherwise; HF_ACCESS_TOKEN enables gated HuggingFace models. -- evidence: [README.md#L169-L178](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L169-L178)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports SynCode achieving 99% JSON generation accuracy with Gemma-2b and being 10-20% faster than unconstrained generation, referencing an evaluation notebook. -- evidence: [README.md#L24-L26](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L24-L26)
- dependencies (2 claim(s)):
  - [observation/documented] SynCode v0.4.16 requires transformers v4.53.2 and Python 3.6-3.12; Python 3.13 is not supported due to dependency constraints. -- evidence: [README.md#L74-L74](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L74-L74), [README.md#L70-L72](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L70-L72)
  - [observation/documented] requirements.txt lists dependencies including transformers==4.53.2 (for Python < 3.13), torch, accelerate, interegular, regex, datasets, jsonschema, fire, and tqdm. -- evidence: [requirements.txt#L1-L9](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/requirements.txt#L1-L9)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](syncode.detail.md)

Metadata and full claim list: [full detail](syncode.detail.md)
Human notes ([notes](syncode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
