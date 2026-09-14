# cactus-compute/needle -- full detail

[Back to orientation](needle.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cactus-compute/needle/956840ff176bfe179bb2f230b726f4be44fb11cf/60917bc650675824.json](../../../wiki/dossiers/cactus-compute/needle/956840ff176bfe179bb2f230b726f4be44fb11cf/60917bc650675824.json)

## specifications (2 claim(s))

- [observation/documented] Needle 2 is described as an open 45M-parameter model for tool calling, device use and structured extraction, shipped as a single 14MB binary that runs a session in about 28MB of RAM. -- evidence: [README.md#L5-L5](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L5-L5) (`clm_5ed679f2e3751906f4447a3da39fcd759fca00470c005f58ce48157e09f8fb21`)
- [observation/documented] The model is said to be compressed to CQ2-bit via Cactus Quants and built on the Simple Attention Network findings, baked into its own engine. -- evidence: [README.md#L5-L5](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L5-L5) (`clm_527cef466feb87996281312d8fba7dd5282bf122bbcd45f59b202a367e63e0c3`)

## components (1 claim(s))

- [observation/documented] The repository is the Python package cactus-needle covering inference, LoRA fine-tuning, and export; the inference engine is fetched once from Hugging Face and cached. -- evidence: [README.md#L7-L7](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L7-L7) (`clm_1d420df65fb5faf82007fa72f2259b0162051296301856c51f473b188d73b4ee`)

## design-choices (3 claim(s))

- [observation/documented] Tool calls are constrained by a byte-level grammar compiled from the declared schemas, so output is structured JSON and cannot be malformed; the reasoning field is generated unconstrained. -- evidence: [doc/apis.md#L120-L127](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L120-L127), [README.md#L9-L13](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L9-L13) (`clm_d8073d6887fd543270ac5fc17e391f6154679e4a3bb9390a7be34bc512635444`)
- [observation/documented] Every response carries a calibrated confidence score from a learned head, defined as the minimum of a post-hoc head score and the decoding probability of the call tokens; users set a threshold and escalate below it. -- evidence: [doc/apis.md#L171-L171](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L171-L171), [README.md#L9-L13](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L9-L13) (`clm_270696d65805383ec97ef3c7814e31ec64b6b883df3b13e64def131e237f870e`)
- [observation/documented] For catalogues above five tools, a built-in contrastive retrieval head embeds schemas at init and renders only the top five tools per turn, rebuilding the grammar over that subset. -- evidence: [doc/apis.md#L167-L167](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L167-L167), [README.md#L9-L13](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L9-L13) (`clm_f170c7f8620d525fa3b69b90323ac4653aa4e10ee719e0d73995ee1b1e7814fe`)

## workflows (1 claim(s))

- [observation/documented] The documented fine-tuning workflow is: optionally synthesize data via needle generate-data (needs OPENROUTER_API_KEY), LoRA fine-tune with needle finetune (defaults epochs 3, lora-rank 16, lr 1e-4), then merge and quantize with needle build into a .cact archive. -- evidence: [README.md#L138-L138](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L138-L138), [README.md#L124-L124](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L124-L124), [README.md#L99-L99](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L99-L99), [README.md#L140-L142](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L140-L142), [README.md#L107-L107](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L107-L107), [README.md#L109-L113](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L109-L113), [README.md#L119-L122](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L119-L122) (`clm_348d2201733e5695078f30a40b91ddafa25cf0cd2b2e0e7d87ac019012ff9b96`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The Python API exposes needle.Needle(tools, system, weights, tool_index_path, buffer_size), agent.run/complete/embed/reset, needle.tool, needle.Field, and needle.extract; tools can be decorated functions, Pydantic models, raw JSON schemas, or a JSON string. -- evidence: [llms.txt#L18-L28](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/llms.txt#L18-L28), [doc/apis.md#L3-L12](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L3-L12) (`clm_10ec3ced1b0716cebbcbd2a2c3d7862b2d8fcb258afb359b76c7612a6414e80e`)
- [observation/documented] Each turn returns one JSON object with fields including type, success, error, function_calls, reasoning, confidence, prefill_tps, decode_tps, and peak_ram_mb; empty function_calls is the off-topic refusal. -- evidence: [doc/apis.md#L101-L114](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L101-L114), [llms.txt#L102-L106](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/llms.txt#L102-L106) (`clm_b073d68618295e2f8c1f250d99780f2a392de26d6043f2bd702bafa0c830bf56`)

## memory-state (1 claim(s))

- [observation/documented] The runtime uses a 256-token sliding window with tools pinned as KV sinks, which the README says keeps total memory near 28MB regardless of conversation length. -- evidence: [README.md#L9-L13](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L9-L13) (`clm_df2769309b4444b276236564b419700a85cde2a56aa5b21b4954b96582998b69`)

## orchestration (1 claim(s))

- [observation/documented] agent.run() drives a full agentic loop (max_steps=8 default): the model picks calls, Needle executes the user's Python functions, feeds results back, and returns final results; ungrounded fields are refused unless strict=False. -- evidence: [doc/apis.md#L120-L127](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L120-L127), [doc/apis.md#L3-L12](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/doc/apis.md#L3-L12) (`clm_91ac23d2434e7ee7770189d0be48da5f1878558cfb6ba0ee877e442f96305f56`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The runtime install excludes training; fine-tuning and export need the [train] extra (JAX, imported lazily), with [train,gpu] for CUDA and [train,metal] for Apple Silicon; Pydantic is used for typed extraction. -- evidence: [README.md#L126-L126](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L126-L126), [llms.txt#L76-L82](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/llms.txt#L76-L82), [README.md#L132-L132](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L132-L132), [llms.txt#L14-L14](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/llms.txt#L14-L14), [README.md#L33-L34](https://github.com/cactus-compute/needle/blob/956840ff176bfe179bb2f230b726f4be44fb11cf/README.md#L33-L34) (`clm_6dc5efe24d6c7f87c67060a7435ab98d951335969ae7f7e09b193b4d8c77b5ee`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

