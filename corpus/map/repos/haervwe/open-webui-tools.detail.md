# haervwe/open-webui-tools -- full detail

[Back to orientation](open-webui-tools.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/haervwe/open-webui-tools/a94660737737f9a455f9697778ed128735f5e884/9c74da54a029af00.json](../../../wiki/dossiers/haervwe/open-webui-tools/a94660737737f9a455f9697778ed128735f5e884/9c74da54a029af00.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The repository advertises 20+ specialized tools and functions organized as tools, function pipes, and filters for Open WebUI. -- evidence: [README.md#L14-L14](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L14-L14), [README.md#L8-L8](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L8-L8) (`clm_9a26dc7dd1b8c2d9929b49f9b9065634d76c3016fd8c1e58a179fc250e7c60de`)
- [observation/documented] Tools include arXiv Search, Perplexica Search, Pexels Media Search, YouTube Search & Embed, multiple ComfyUI-based image/audio/video generators, and an OpenWeatherMap forecast tool. -- evidence: [README.md#L18-L33](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L18-L33) (`clm_b14067a7dd581fe01c673614a1d6128609800277b5d17bf7cfa90c130118b8fd`)
- [observation/documented] Function pipes include Planner Agent v3, arXiv Research MCTS, Multi Model Conversations v2, Resume Analyzer, Mopidy Music Controller, Letta Agent, Perplexica Pipe, Google Veo, and MiniMax LLM Pipe. -- evidence: [README.md#L38-L46](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L38-L46) (`clm_8606e56d0e05323801b4a184e682ecd063f887535e553568aa1198d204ca2973`)
- [observation/documented] Filters include Doodle Paint, Prompt Enhancer, Semantic Router, Full Document, Clean Thinking Tags, and OpenRouter WebSearch Citations. -- evidence: [README.md#L50-L55](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L50-L55) (`clm_998ef8f72884f9c30861e81eeb3425441896c1fc524897ac81942661e25019d5`)

## design-choices (3 claim(s))

- [observation/documented] The Native Image Generator is backend-agnostic, using whatever image backend is configured in Open WebUI admin settings, with optional Ollama model unloading to free VRAM. -- evidence: [README.md#L336-L336](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L336-L336), [README.md#L344-L344](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L344-L344), [README.md#L362-L367](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L362-L367) (`clm_ee43eebb3276d7db0556fd829db4dd39eabd727ab20f79d9b868d28c15697514`)
- [observation/documented] The ComfyUI image-editing tool supports three workflow types (Qwen Edit 2509 default, Flux Kontext, or custom JSON), with Qwen accepting 1-3 input images and Flux Kontext currently single-image. -- evidence: [README.md#L587-L590](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L587-L590), [README.md#L545-L551](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L545-L551), [README.md#L582-L585](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L582-L585), [README.md#L619-L622](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L619-L622) (`clm_332b55692b608edfef1bf021b3e04f32a6a132357a31565facf30ab37f392cf2`)
- [observation/documented] The ACE Step 1.5 audio tool exposes admin valves for workflow node IDs and per-user valves for steps, seed, and audio-code generation, supporting batch generation and an embedded player. -- evidence: [README.md#L666-L668](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L666-L668), [README.md#L689-L692](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L689-L692), [README.md#L637-L654](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L637-L654) (`clm_18a6cd4de6fa879994156b1c5cf0f3bcdadf0b05d43839939447cebffb9cabfb`)

## workflows (1 claim(s))

- [observation/documented] Installation is either via the Open WebUI Hub page or manually by copying .py files from tools/, functions/, or filters/ into the Open WebUI Workspace. -- evidence: [README.md#L61-L63](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L61-L63), [README.md#L67-L69](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L67-L69) (`clm_8a64ecd9afe1fdfb3a45699cc247ee3e87534f24bf07a490858505f38e28b53d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Tools are configured through Open WebUI Valves settings; for example the YouTube tool exposes YOUTUBE_API_KEY, MAX_RESULTS, REGION_CODE, and SAFE_SEARCH valves. -- evidence: [README.md#L318-L321](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L318-L321), [README.md#L271-L275](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L271-L275) (`clm_d4da6b2fd9ac3976edd9887cd0a23f8710335098605fea808424eb88eff35dca`)
- [observation/documented] The Pexels tool exposes three search functions (search_photos, search_videos, get_curated_photos) and caps results per page to avoid overwhelming LLMs. -- evidence: [README.md#L223-L227](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L223-L227), [README.md#L253-L259](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L253-L259) (`clm_a6e547b7ce803a875438302ea1b5c7c67404bdbc29a01599e46c92a149a99959`)
- [observation/documented] The Perplexica Pipe streams responses, emits citations with source metadata, supports multiple focus modes, and routes between search and non-search task models. -- evidence: [README.md#L477-L487](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L477-L487), [README.md#L499-L502](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L499-L502), [README.md#L506-L513](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L506-L513) (`clm_d1aec58e9d240fb773763bf063e6b3f10fcd5d527dcf08fe4140ab7c285937da`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Several tools require external services or keys: a self-hosted Perplexica instance with Ollama models, a Pexels API key, a YouTube Data API v3 key, and a running ComfyUI for media generation. -- evidence: [README.md#L223-L227](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L223-L227), [README.md#L277-L277](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L277-L277), [README.md#L189-L189](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L189-L189), [README.md#L553-L556](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L553-L556) (`clm_9105553d505be45d3c217b908b94f131a74fb8059212773434a65df69b3ce7cf`)
- [observation/documented] The arXiv Search tool requires no API key and no configuration, returning up to five recent papers per query. -- evidence: [README.md#L158-L158](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L158-L158), [README.md#L154-L154](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L154-L154), [README.md#L168-L168](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L168-L168) (`clm_5b9db23ee25da91a003f6c302ecc6df557d8c7e0ff26ccb4876e5898c4a8296e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

