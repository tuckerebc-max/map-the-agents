# matthewzmd/aidermacs

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b9a2512e54d8 @ 850313fb19af3739

## Summary (orientation draft, not independently verified)

Selected evidence records: The main interface is a Magit-like transient menu, invoked via M-x aidermacs-transient-menu or a user-bound key such as C-c a. The transient menu includes session commands (start/open, clear history, reset, exit), persistent mode toggles (Code, Chat/Ask, Architect, Help), utilities, file actions, and code actions, with 'All File Actions' and 'All Code Actions' submenus.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Aidermacs wraps the external Aider tool (or its community fork aider-ce), requiring Emacs >= 26.1 and the Transient package. -- evidence: [README.md#L15-L15](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L15-L15), [README.md#L42-L62](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L42-L62)
  - [observation/documented] Two terminal backends are supported: comint (default, Emacs built-in) and vterm (better terminal compatibility), selected via aidermacs-backend. -- evidence: [README.md#L322-L324](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L322-L324), [README.md#L315-L315](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L315-L315), [README.md#L313-L313](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L313-L313)
- design-choices (6 claim(s)):
  - [observation/documented] Architect mode uses two models: an Architect model for reasoning and an Editor model for code generation; each can be configured independently via aidermacs-architect-model and aidermacs-editor-model. -- evidence: [README.md#L275-L280](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L275-L280), [README.md#L254-L254](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L254-L254), [README.md#L246-L246](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L246-L246), [README.md#L252-L252](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L252-L252)
  - [observation/documented] By default Aidermacs requires explicit confirmation before applying Architect-mode changes; setting aidermacs-auto-accept-architect to t enables automatic acceptance. -- evidence: [README.md#L303-L303](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L303-L303), [README.md#L301-L301](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L301-L301), [README.md#L305-L307](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L305-L307)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The main interface is a Magit-like transient menu, invoked via M-x aidermacs-transient-menu or a user-bound key such as C-c a. -- evidence: [README.md#L99-L101](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L99-L101), [README.md#L91-L91](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L91-L91), [README.md#L93-L95](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L93-L95)
  - [observation/documented] The transient menu includes session commands (start/open, clear history, reset, exit), persistent mode toggles (Code, Chat/Ask, Architect, Help), utilities, file actions, and code actions, with 'All File Actions' and 'All Code Actions' submenus. -- evidence: [README.md#L119-L126](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L119-L126), [README.md#L113-L116](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L113-L116), [README.md#L129-L140](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L129-L140), [README.md#L154-L154](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L154-L154), [README.md#L143-L152](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L143-L152), [README.md#L106-L110](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L106-L110)
- memory-state (1 claim(s)):
  - [observation/documented] Prompt history and a curated common-prompts list (aidermacs-common-prompts) are saved and available across all sessions via completion. -- evidence: [README.md#L366-L366](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L366-L366), [README.md#L375-L375](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L375-L375), [README.md#L368-L369](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L368-L369), [README.md#L371-L373](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L371-L373)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Files added as editable grant the AI read and modify permission; any add-file command prefixed with C-u adds the file as read-only instead. -- evidence: [README.md#L160-L163](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L160-L163)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Dynamic model selection fetches available models from OpenAI, Anthropic, DeepSeek, Google Gemini, and OpenRouter, caching lists and filtering by Aider version and configured API keys; this applies only to solo (non-Architect) mode. -- evidence: [README.md#L225-L229](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L225-L229), [README.md#L231-L231](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L231-L231), [README.md#L223-L223](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L223-L223), [README.md#L239-L242](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L239-L242)
- limitations (2 claim(s)):
More evidence: [full detail](aidermacs.detail.md)

Metadata and full claim list: [full detail](aidermacs.detail.md)
Human notes ([notes](aidermacs.notes.md), never overwritten by build)

[Back to map index](../../index.md)
