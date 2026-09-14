# lidangzzz/ai-coding-style-guides -- full detail

[Back to orientation](ai-coding-style-guides.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lidangzzz/ai-coding-style-guides/16f2f9c646d240929567f76ac07643d4426679aa/64afa9d674f12c13.json](../../../wiki/dossiers/lidangzzz/ai-coding-style-guides/16f2f9c646d240929567f76ac07643d4426679aa/64afa9d674f12c13.json)

## specifications (4 claim(s))

- [observation/documented] The project ships a set of coding style guides, including general guides for common languages and guides tailored to specific languages and scenarios, aimed at maximizing code compression. -- evidence: [README.md#L30-L30](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L30-L30) (`clm_5574ff3cd1afc242572a7ef7741df54c57626850535d0dd47e380e54db9e837f`)
- [observation/documented] Basic rules include minimizing whitespace, keeping full names for top-level entities while shortening local variables, brief comments only at top level, and co-locating related code in single files. -- evidence: [README.md#L54-L54](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L54-L54), [README.md#L58-L58](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L58-L58), [README.md#L52-L52](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L52-L52), [README.md#L56-L56](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L56-L56) (`clm_ba170487da994b9847096abf7f3d96fdac0467f4000a45e8bfe405c24a45dad7`)
- [observation/documented] Further rules advocate advanced language features (lambdas, syntactic sugar, type inference), abstracting reusable units, avoiding duplication via higher-order functions/decorators/mixins, and letting the LLM perform compression. -- evidence: [README.md#L60-L60](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L60-L60), [README.md#L68-L68](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L68-L68), [README.md#L64-L64](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L64-L64), [README.md#L62-L62](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L62-L62) (`clm_99cce8193fdb73de809c6430e9ac31d90598b3378ecd28a3dc13e3adf7697b41`)
- [observation/documented] Compression is organized into eight levels, from basic whitespace removal up to full whitespace removal, identifier shortening, comment removal, and refactoring with any language feature. -- evidence: [README_CN.md#L72-L81](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README_CN.md#L72-L81), [README.md#L74-L83](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L74-L83) (`clm_bb147aabf5f94357cc6d407da5419bb851094e842135fe206b9325aee1c239c2`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The stated goal is to maximize code compression across languages while keeping reasonable human readability, balancing compactness against context-window savings. -- evidence: [README.md#L32-L32](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L32-L32) (`clm_178ee3e8625e9114b18d729816d3d980deef94420ce5e5c643de2a12f197ba47`)
- [observation/documented] The guide's rationale cites three trends: growing LLM capability, perpetually insufficient context windows, and reduced importance of human readability when agents do most programming. -- evidence: [README.md#L42-L42](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L42-L42), [README.md#L40-L40](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L40-L40), [README.md#L38-L38](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L38-L38) (`clm_87bbb9e738ccd99a3ef0fe89f2d28d486b0bc91441792f80d749b893b1f4a63e`)
- [observation/documented] The guide argues compressed code remains workable because LLMs can explain or reconstruct it into readable form, demonstrated by an LLM explanation of the 283-character KMP function. -- evidence: [README.md#L46-L46](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L46-L46), [README.md#L236-L236](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L236-L236), [README.md#L309-L309](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L309-L309) (`clm_800938af73fb3505443ed3982d4a970b0f93517b4136cff92a874e930140b3d9`)

## workflows (2 claim(s))

- [observation/documented] Usage instructions tell readers to open AI_Coding_Style_Guide_prompts.toml, copy its prompts into their own prompt management system, and optionally modify them for their needs. -- evidence: [README.md#L9-L9](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L9-L9), [README.md#L11-L11](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L11-L11) (`clm_2d13cd412461e305c184614d500ab692ae7fa6f671e2ea3740d06c48259ecdd2`)
- [observation/documented] A Python snippet using the toml library is provided to load prompts from the TOML file into a user's prompt management system. -- evidence: [README.md#L15-L22](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L15-L22) (`clm_c83ee13c9543c31464c4f26c611bfeee3d9ec15b59c68167fe98d9fbbc5ebc2f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (3 claim(s))

- [observation/documented] The README demonstrates compression on a 1216-character TypeScript KMP implementation, showing staged reductions to 795, 715, 443, and finally 283 characters (~23.3% of original). -- evidence: [README.md#L198-L198](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L198-L198), [README.md#L89-L89](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L89-L89), [README.md#L209-L209](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L209-L209), [README.md#L218-L218](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L218-L218), [README.md#L147-L147](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L147-L147) (`clm_72c2a828da8f3b91e4c2cd77d3ae89626e398649a6f8cd825cf341ef013e9717`)
- [observation/documented] The guide benchmarks against conventional tools: JSCompress output was 348 characters (~28.6%) for the compiled JavaScript, and jsonminify.com produced 2144 characters (~79.2%) for the C++ example. -- evidence: [README.md#L433-L433](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L433-L433), [README.md#L226-L226](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L226-L226) (`clm_dc0ed1519334e388eb03a899f63d0344f6287618b1f91209b7be438beced5e2a`)
- [observation/documented] A C++ JSON parser example is compressed from 2708 to 1330 characters (~49.1%), and the conclusion claims typical reductions to roughly 20-50% of original size. -- evidence: [README.md#L417-L417](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L417-L417), [README.md#L447-L447](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L447-L447), [README.md#L315-L315](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L315-L315) (`clm_2d2b1f286785b5c6537f5abf197433dbbc4e1f5bd9893b18353fc037f4e16a60`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [inference/documented] The evidence shows only documentation and prompt content; no executable tool or agent runtime appears in the provided slices, so the deliverable appears to be prompts and guidance rather than software. -- evidence: [README.md#L9-L9](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L9-L9), [README.md#L15-L22](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L15-L22) (`clm_38e0adfe38599f9148acdaaf6537a6a32ad30d6b19940da60a2d8ca6ff6f1fdf`)

## relevance (1 claim(s))

- [observation/documented] The guide targets vibe-coding and SWE-agent workflows where context-window limits and per-token costs motivate feeding more code in fewer tokens. -- evidence: [README.md#L28-L28](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L28-L28), [README.md#L30-L30](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L30-L30), [README.md#L26-L26](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L26-L26) (`clm_af43ac5a6ffff7f3ebcbbc9f686dee97fc98fbbd00867e00f263d44acc678b90`)

