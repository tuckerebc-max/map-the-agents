# haervwe/open-webui-tools

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a94660737737 @ 9c74da54a029af00

## Summary (orientation draft, not independently verified)

The snapshot is a README-only view of a collection of 20+ Open WebUI tools, function pipes, and filters for search, media generation, and agent workflows, with per-tool configuration via Valves and external service prerequisites. Evidence coverage: 139 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The repository advertises 20+ specialized tools and functions organized as tools, function pipes, and filters for Open WebUI. -- evidence: [README.md#L14-L14](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L14-L14), [README.md#L8-L8](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L8-L8)
  - [observation/documented] Tools include arXiv Search, Perplexica Search, Pexels Media Search, YouTube Search & Embed, multiple ComfyUI-based image/audio/video generators, and an OpenWeatherMap forecast tool. -- evidence: [README.md#L18-L33](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L18-L33)
- design-choices (3 claim(s)):
  - [observation/documented] The Native Image Generator is backend-agnostic, using whatever image backend is configured in Open WebUI admin settings, with optional Ollama model unloading to free VRAM. -- evidence: [README.md#L336-L336](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L336-L336), [README.md#L344-L344](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L344-L344), [README.md#L362-L367](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L362-L367)
  - [observation/documented] The ComfyUI image-editing tool supports three workflow types (Qwen Edit 2509 default, Flux Kontext, or custom JSON), with Qwen accepting 1-3 input images and Flux Kontext currently single-image. -- evidence: [README.md#L587-L590](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L587-L590), [README.md#L545-L551](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L545-L551), [README.md#L582-L585](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L582-L585), [README.md#L619-L622](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L619-L622)
- workflows (1 claim(s)):
  - [observation/documented] Installation is either via the Open WebUI Hub page or manually by copying .py files from tools/, functions/, or filters/ into the Open WebUI Workspace. -- evidence: [README.md#L61-L63](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L61-L63), [README.md#L67-L69](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L67-L69)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Tools are configured through Open WebUI Valves settings; for example the YouTube tool exposes YOUTUBE_API_KEY, MAX_RESULTS, REGION_CODE, and SAFE_SEARCH valves. -- evidence: [README.md#L318-L321](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L318-L321), [README.md#L271-L275](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L271-L275)
  - [observation/documented] The Pexels tool exposes three search functions (search_photos, search_videos, get_curated_photos) and caps results per page to avoid overwhelming LLMs. -- evidence: [README.md#L223-L227](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L223-L227), [README.md#L253-L259](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L253-L259)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Several tools require external services or keys: a self-hosted Perplexica instance with Ollama models, a Pexels API key, a YouTube Data API v3 key, and a running ComfyUI for media generation. -- evidence: [README.md#L223-L227](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L223-L227), [README.md#L277-L277](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L277-L277), [README.md#L189-L189](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L189-L189), [README.md#L553-L556](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L553-L556)
  - [observation/documented] The arXiv Search tool requires no API key and no configuration, returning up to five recent papers per query. -- evidence: [README.md#L158-L158](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L158-L158), [README.md#L154-L154](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L154-L154), [README.md#L168-L168](https://github.com/Haervwe/open-webui-tools/blob/a94660737737f9a455f9697778ed128735f5e884/README.md#L168-L168)
More evidence: [full detail](open-webui-tools.detail.md)

Metadata and full claim list: [full detail](open-webui-tools.detail.md)
Human notes ([notes](open-webui-tools.notes.md), never overwritten by build)

[Back to map index](../../index.md)
