# mikotokawaii25/local-ai-code-assistant

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1ca5630df925 @ 0b528688abe8a25c

## Summary (orientation draft, not independently verified)

The snapshot contains only README documentation for CodeLoom, a desktop offline multi-model AI coding assistant; all claims below are documentation-based, with no code inspected.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Stated system requirements: 16 GB RAM minimum (32 GB recommended), 6 GB VRAM minimum (12 GB+ recommended), 10 GB storage, on Windows 10, macOS 12+, or Linux kernel 5.x. -- evidence: [README.md#L80-L85](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L80-L85)
- components (1 claim(s)):
  - [observation/documented] A local-network collaboration feature shares loom sessions over WebSocket so team members can sync edits and model outputs without internet. -- evidence: [README.md#L44-L44](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L44-L44)
- design-choices (1 claim(s)):
  - [observation/documented] CodeLoom is designed as an offline-only desktop tool that runs multiple open-source models locally with no cloud dependencies or data leaving the machine. -- evidence: [README.md#L5-L5](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L5-L5), [README.md#L7-L7](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L7-L7)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Configuration is exposed through a loom_config.yaml file covering per-task model assignments, token budgets, sampling parameters, context-sharing rules, theme, and LAN-only remote access. -- evidence: [README.md#L99-L99](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L99-L99), [README.md#L101-L106](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L101-L106)
  - [observation/documented] Advanced users can write custom 'loom scripts' in Lua that define model interactions, thread switching, and output merging. -- evidence: [README.md#L108-L108](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L108-L108)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (3 claim(s)):
  - [observation/documented] The product supports up to five concurrent model sessions, each with its own context window, history, and parameters, and lets the user pick which thread's answer wins. -- evidence: [README.md#L26-L26](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L26-L26)
  - [observation/documented] Context can be merged between model threads manually or automatically, e.g. passing a small model's draft to a larger model without copy/paste. -- evidence: [README.md#L29-L29](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L29-L29)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Inference runs via local backends including llama.cpp, ExLlama, and MLX, and models can be imported from Hugging Face, Ollama, or local GGUF/GPTQ files. -- evidence: [README.md#L17-L19](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L17-L19), [README.md#L35-L35](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L35-L35)
  - [observation/documented] The project is MIT-licensed, and a disclaimer notes that orchestrated models carry their own licenses and usage terms for which users are responsible. -- evidence: [README.md#L164-L164](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L164-L164), [README.md#L143-L143](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L143-L143)
- limitations (1 claim(s)):
  - [observation/documented] Per the FAQ, there is no cloud version by design, updates are manual downloads that only check a URL for version strings, and 7B models at 4-bit need at least 6 GB VRAM. -- evidence: [README.md#L135-L136](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L135-L136), [README.md#L138-L139](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L138-L139), [README.md#L129-L130](https://github.com/MIKOTOKAWAII25/local-ai-code-assistant/blob/1ca5630df92515569ceae1f137f2453088c022b3/README.md#L129-L130)
More evidence: [full detail](local-ai-code-assistant.detail.md)

Metadata and full claim list: [full detail](local-ai-code-assistant.detail.md)
Human notes ([notes](local-ai-code-assistant.notes.md), never overwritten by build)

[Back to map index](../../index.md)
