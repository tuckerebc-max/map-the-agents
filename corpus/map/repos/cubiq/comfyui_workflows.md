# cubiq/comfyui_workflows

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 038cb775f2e8 @ b33986008b4b4dec

## Summary (orientation draft, not independently verified)

A documentation repository of ComfyUI workflow JSON files organized into categories (basic, upscale, text2img, image conditioning, in/out painting, guided composition), aimed at beginners to intermediate users and designed to work mostly without plugins.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Content is organized into macro categories; each directory root holds basic JSON workflow files plus an experiments directory with more advanced examples and tips. -- evidence: [README.md#L11-L11](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L11-L11)
  - [observation/documented] Sections cover basics of ComfyUI and Stable Diffusion, upscaling (hires fix), advanced text-to-image techniques (word weighting, embeddings, timestepping, gligen), image-to-image conditioning, in/out painting, and guided composition with ControlNets and T2I-Adapter. -- evidence: [README.md#L49-L49](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L49-L49), [README.md#L40-L40](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L40-L40), [README.md#L43-L43](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L43-L43), [README.md#L46-L46](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L46-L46), [README.md#L52-L52](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L52-L52), [README.md#L55-L55](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L55-L55)
- design-choices (2 claim(s)):
  - [observation/documented] Workflows are laid out for readability, with execution flowing left to right and top to bottom so node graphs can be followed without rearranging nodes. -- evidence: [README.md#L9-L9](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L9-L9)
  - [inference/documented] The author appears to favor ComfyUI for its modular, granular component mixing and memory/speed efficiency, while acknowledging easier alternatives exist. -- evidence: [README.md#L25-L25](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L25-L25), [README.md#L21-L21](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L21-L21), [README.md#L23-L23](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L23-L23)
- workflows (1 claim(s)):
  - [observation/documented] To follow the exercises, users are instructed to clone or download the repository and place its files into the ComfyUI/input directory on their machine. -- evidence: [README.md#L29-L29](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L29-L29)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Workflows are JSON files that can be loaded by dropping them onto the ComfyUI work area; generated images embed the full workflow and can also be dropped in to load the node structure. -- evidence: [README.md#L31-L31](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L31-L31)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Most workflows are designed to run without any installed plugins, with few exceptions noted in the documentation, to lower the entry barrier and avoid ecosystem conflicts. -- evidence: [README.md#L15-L15](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L15-L15)
- limitations (1 claim(s)):
  - [observation/documented] The repository is described as a work in progress, with a planned future section on detailing (cutting out parts like faces or hands to enhance them). -- evidence: [README.md#L58-L58](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L58-L58)
- relevance (2 claim(s)):
  - [observation/documented] The repository provides documented, easy-to-follow ComfyUI workflows intended as a learning exercise rather than optimized or best-practice pipelines. -- evidence: [README.md#L7-L7](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L7-L7), [README.md#L3-L3](https://github.com/cubiq/ComfyUI_Workflows/blob/038cb775f2e8eb54bdbc99a8b9720177c7f8a336/README.md#L3-L3)
More evidence: [full detail](comfyui_workflows.detail.md)

Metadata and full claim list: [full detail](comfyui_workflows.detail.md)
Human notes ([notes](comfyui_workflows.notes.md), never overwritten by build)

[Back to map index](../../index.md)
