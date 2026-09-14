# cactus-compute/needle

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 956840ff176b @ 60917bc650675824

## Summary (orientation draft, not independently verified)

Evidence describes Needle 2, a 45M-parameter tool-calling model shipped as a Python package (cactus-needle) with inference, LoRA fine-tuning, and export, plus documented API, environments, and offline/WASM distribution. Claims below rest on README and doc text only. Evidence coverage: 134 of 160 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Needle 2 is described as an open 45M-parameter model for tool calling, device use and structured extraction, shipped as a single 14MB binary that runs a session in about 28MB of RAM. -- evidence: [README.md#L5-L5](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L5-L5)
  - [observation/documented] The model is said to be compressed to CQ2-bit via Cactus Quants and built on the Simple Attention Network findings, baked into its own engine. -- evidence: [README.md#L5-L5](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The repository is the Python package cactus-needle covering inference, LoRA fine-tuning, and export; the inference engine is fetched once from Hugging Face and cached. -- evidence: [README.md#L7-L7](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L7-L7)
- design-choices (3 claim(s)):
  - [observation/documented] Tool calls are constrained by a byte-level grammar compiled from the declared schemas, so output is structured JSON and cannot be malformed; the reasoning field is generated unconstrained. -- evidence: [doc/apis.md#L120-L127](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L120-L127), [README.md#L9-L13](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L9-L13)
  - [observation/documented] Every response carries a calibrated confidence score from a learned head, defined as the minimum of a post-hoc head score and the decoding probability of the call tokens; users set a threshold and escalate below it. -- evidence: [doc/apis.md#L171-L171](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L171-L171), [README.md#L9-L13](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L9-L13)
- workflows (1 claim(s)):
  - [observation/documented] The documented fine-tuning workflow is: optionally synthesize data via needle generate-data (needs OPENROUTER_API_KEY), LoRA fine-tune with needle finetune (defaults epochs 3, lora-rank 16, lr 1e-4), then merge and quantize with needle build into a .cact archive. -- evidence: [README.md#L138-L138](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L138-L138), [README.md#L124-L124](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L124-L124), [README.md#L99-L99](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L99-L99), [README.md#L140-L142](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L140-L142), [README.md#L107-L107](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L107-L107), [README.md#L109-L113](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L109-L113), [README.md#L119-L122](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L119-L122)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The Python API exposes needle.Needle(tools, system, weights, tool_index_path, buffer_size), agent.run/complete/embed/reset, needle.tool, needle.Field, and needle.extract; tools can be decorated functions, Pydantic models, raw JSON schemas, or a JSON string. -- evidence: [llms.txt#L18-L28](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/llms.txt#L18-L28), [doc/apis.md#L3-L12](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L3-L12)
  - [observation/documented] Each turn returns one JSON object with fields including type, success, error, function_calls, reasoning, confidence, prefill_tps, decode_tps, and peak_ram_mb; empty function_calls is the off-topic refusal. -- evidence: [doc/apis.md#L101-L114](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L101-L114), [llms.txt#L102-L106](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/llms.txt#L102-L106)
- memory-state (1 claim(s)):
More evidence: [full detail](needle.detail.md)

Metadata and full claim list: [full detail](needle.detail.md)
Human notes ([notes](needle.notes.md), never overwritten by build)

[Back to map index](../../index.md)
