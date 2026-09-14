---
access: public
aliases: []
claim_ids:
- clm_18a6cd4de6fa879994156b1c5cf0f3bcdadf0b05d43839939447cebffb9cabfb
- clm_332b55692b608edfef1bf021b3e04f32a6a132357a31565facf30ab37f392cf2
- clm_5b9db23ee25da91a003f6c302ecc6df557d8c7e0ff26ccb4876e5898c4a8296e
- clm_8606e56d0e05323801b4a184e682ecd063f887535e553568aa1198d204ca2973
- clm_8a64ecd9afe1fdfb3a45699cc247ee3e87534f24bf07a490858505f38e28b53d
- clm_9105553d505be45d3c217b908b94f131a74fb8059212773434a65df69b3ce7cf
- clm_998ef8f72884f9c30861e81eeb3425441896c1fc524897ac81942661e25019d5
- clm_9a26dc7dd1b8c2d9929b49f9b9065634d76c3016fd8c1e58a179fc250e7c60de
- clm_a6e547b7ce803a875438302ea1b5c7c67404bdbc29a01599e46c92a149a99959
- clm_b14067a7dd581fe01c673614a1d6128609800277b5d17bf7cfa90c130118b8fd
- clm_d1aec58e9d240fb773763bf063e6b3f10fcd5d527dcf08fe4140ab7c285937da
- clm_d4da6b2fd9ac3976edd9887cd0a23f8710335098605fea808424eb88eff35dca
- clm_ee43eebb3276d7db0556fd829db4dd39eabd727ab20f79d9b868d28c15697514
maturity: draft
page_id: pg_30262b4086af5d96b4a1826ac22194cf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5c996d0f01a956f7972f60f522237849
title: Haervwe/open-webui-tools/README.md @ a94660737737
updated_at: '2026-09-14T03:56:01Z'
---

# Haervwe/open-webui-tools/README.md @ a94660737737

<!-- rcw:begin owner=source:src_5c996d0f01a956f7972f60f522237849 block=evidence -->
- The ACE Step 1.5 audio tool exposes admin valves for workflow node IDs and per-user valves for steps, seed, and audio-code generation, supporting batch generation and an embedded player. [@claim:clm_18a6cd4de6fa879994156b1c5cf0f3bcdadf0b05d43839939447cebffb9cabfb]
- The ComfyUI image-editing tool supports three workflow types (Qwen Edit 2509 default, Flux Kontext, or custom JSON), with Qwen accepting 1-3 input images and Flux Kontext currently single-image. [@claim:clm_332b55692b608edfef1bf021b3e04f32a6a132357a31565facf30ab37f392cf2]
- The arXiv Search tool requires no API key and no configuration, returning up to five recent papers per query. [@claim:clm_5b9db23ee25da91a003f6c302ecc6df557d8c7e0ff26ccb4876e5898c4a8296e]
- Function pipes include Planner Agent v3, arXiv Research MCTS, Multi Model Conversations v2, Resume Analyzer, Mopidy Music Controller, Letta Agent, Perplexica Pipe, Google Veo, and MiniMax LLM Pipe. [@claim:clm_8606e56d0e05323801b4a184e682ecd063f887535e553568aa1198d204ca2973]
- Installation is either via the Open WebUI Hub page or manually by copying .py files from tools/, functions/, or filters/ into the Open WebUI Workspace. [@claim:clm_8a64ecd9afe1fdfb3a45699cc247ee3e87534f24bf07a490858505f38e28b53d]
- Several tools require external services or keys: a self-hosted Perplexica instance with Ollama models, a Pexels API key, a YouTube Data API v3 key, and a running ComfyUI for media generation. [@claim:clm_9105553d505be45d3c217b908b94f131a74fb8059212773434a65df69b3ce7cf]
- Filters include Doodle Paint, Prompt Enhancer, Semantic Router, Full Document, Clean Thinking Tags, and OpenRouter WebSearch Citations. [@claim:clm_998ef8f72884f9c30861e81eeb3425441896c1fc524897ac81942661e25019d5]
- The repository advertises 20+ specialized tools and functions organized as tools, function pipes, and filters for Open WebUI. [@claim:clm_9a26dc7dd1b8c2d9929b49f9b9065634d76c3016fd8c1e58a179fc250e7c60de]
- The Pexels tool exposes three search functions (search_photos, search_videos, get_curated_photos) and caps results per page to avoid overwhelming LLMs. [@claim:clm_a6e547b7ce803a875438302ea1b5c7c67404bdbc29a01599e46c92a149a99959]
- Tools include arXiv Search, Perplexica Search, Pexels Media Search, YouTube Search & Embed, multiple ComfyUI-based image/audio/video generators, and an OpenWeatherMap forecast tool. [@claim:clm_b14067a7dd581fe01c673614a1d6128609800277b5d17bf7cfa90c130118b8fd]
- The Perplexica Pipe streams responses, emits citations with source metadata, supports multiple focus modes, and routes between search and non-search task models. [@claim:clm_d1aec58e9d240fb773763bf063e6b3f10fcd5d527dcf08fe4140ab7c285937da]
- Tools are configured through Open WebUI Valves settings; for example the YouTube tool exposes YOUTUBE_API_KEY, MAX_RESULTS, REGION_CODE, and SAFE_SEARCH valves. [@claim:clm_d4da6b2fd9ac3976edd9887cd0a23f8710335098605fea808424eb88eff35dca]
- The Native Image Generator is backend-agnostic, using whatever image backend is configured in Open WebUI admin settings, with optional Ollama model unloading to free VRAM. [@claim:clm_ee43eebb3276d7db0556fd829db4dd39eabd727ab20f79d9b868d28c15697514]
<!-- rcw:end owner=source:src_5c996d0f01a956f7972f60f522237849 block=evidence -->

## Researcher notes

