# matthewzmd/aidermacs -- full detail

[Back to orientation](aidermacs.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/matthewzmd/aidermacs/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/850313fb19af3739.json](../../../wiki/dossiers/matthewzmd/aidermacs/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/850313fb19af3739.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Aidermacs wraps the external Aider tool (or its community fork aider-ce), requiring Emacs >= 26.1 and the Transient package. -- evidence: [README.md#L15-L15](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L15-L15), [README.md#L42-L62](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L42-L62) (`clm_2677a720bb1448bf61bbed694956bd5c54bd6def8b63f9af5d74a49016d67c54`)
- [observation/documented] Two terminal backends are supported: comint (default, Emacs built-in) and vterm (better terminal compatibility), selected via aidermacs-backend. -- evidence: [README.md#L322-L324](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L322-L324), [README.md#L315-L315](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L315-L315), [README.md#L313-L313](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L313-L313) (`clm_0ea846dfafc022efcadfdaf9a68e6e6763d098849cd68043d04d8af306ebcd35`)

## design-choices (6 claim(s))

- [observation/documented] Architect mode uses two models: an Architect model for reasoning and an Editor model for code generation; each can be configured independently via aidermacs-architect-model and aidermacs-editor-model. -- evidence: [README.md#L275-L280](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L275-L280), [README.md#L254-L254](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L254-L254), [README.md#L246-L246](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L246-L246), [README.md#L252-L252](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L252-L252) (`clm_4c19f6b27b7169c64643452cac603a1810d5798e267930bed6cf3b9eba4fe6eb`)
- [observation/documented] By default Aidermacs requires explicit confirmation before applying Architect-mode changes; setting aidermacs-auto-accept-architect to t enables automatic acceptance. -- evidence: [README.md#L303-L303](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L303-L303), [README.md#L301-L301](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L301-L301), [README.md#L305-L307](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L305-L307) (`clm_c9d3f0afb2628ad5b3832e54778bcfd671394d9231bedbb9bfa5eb049650cf5c`)
- [observation/documented] Auto-commits of AI-generated changes are disabled by default (unlike Aider's default), and can be re-enabled via aidermacs-auto-commits. -- evidence: [README.md#L436-L439](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L436-L439), [README.md#L434-L434](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L434-L434) (`clm_367f3727173dababa023e618f5a83300600866e7b2b258ab2542615b977b281e`)
- [observation/documented] Configuration precedence: if an .aider.conf.yml is found it takes highest priority and Emacs variables are ignored; otherwise Emacs variables override environment variables, which override built-in defaults. -- evidence: [README.md#L488-L488](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L488-L488), [README.md#L490-L493](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L490-L493) (`clm_67311ea0cf73b7f842afb894c9c41678f5f22508fd31abc6570fadb65f163f22`)
- [observation/documented] When enabled, diff review captures pre-edit file state and shows changes through Emacs' built-in ediff interface for accept/reject review; controlled by aidermacs-show-diff-after-change (default t). -- evidence: [README.md#L422-L425](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L422-L425), [README.md#L427-L430](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L427-L430), [README.md#L420-L420](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L420-L420) (`clm_89ca7663f2395484efface4863a1bc2041df5f0b35472b076dc2c88546a3f66a`)
- [observation/documented] The aidermacs-before-run-backend-hook runs custom setup before the backend starts, using a copy of process-environment so secrets set there affect only the Aider backend. -- evidence: [README.md#L188-L188](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L188-L188), [README.md#L202-L202](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L202-L202) (`clm_242089bd9f1a8c425d4de35c076a89913d5f526e1a22f55b70a748b6373fd1f9`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The main interface is a Magit-like transient menu, invoked via M-x aidermacs-transient-menu or a user-bound key such as C-c a. -- evidence: [README.md#L99-L101](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L99-L101), [README.md#L91-L91](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L91-L91), [README.md#L93-L95](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L93-L95) (`clm_436eed0809f3078fda5c1f8df4ed1fe8f5f0188c63581f0151b78cfe215f07d5`)
- [observation/documented] The transient menu includes session commands (start/open, clear history, reset, exit), persistent mode toggles (Code, Chat/Ask, Architect, Help), utilities, file actions, and code actions, with 'All File Actions' and 'All Code Actions' submenus. -- evidence: [README.md#L119-L126](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L119-L126), [README.md#L113-L116](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L113-L116), [README.md#L129-L140](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L129-L140), [README.md#L154-L154](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L154-L154), [README.md#L143-L152](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L143-L152), [README.md#L106-L110](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L106-L110) (`clm_cbfff34147ce070c4e830ea72ab64ae08f6538b8aa0a58e4a9fe087936c0eac8`)

## memory-state (1 claim(s))

- [observation/documented] Prompt history and a curated common-prompts list (aidermacs-common-prompts) are saved and available across all sessions via completion. -- evidence: [README.md#L366-L366](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L366-L366), [README.md#L375-L375](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L375-L375), [README.md#L368-L369](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L368-L369), [README.md#L371-L373](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L371-L373) (`clm_be8740f7601d5d8ed98ef775a7a028f957053c003f3b76687a40f776bd2d9a5a`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Files added as editable grant the AI read and modify permission; any add-file command prefixed with C-u adds the file as read-only instead. -- evidence: [README.md#L160-L163](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L160-L163) (`clm_a4433adc474f29a8b723ba3f2ba02d16ce504903142e31dc762a83a209ca6318`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Dynamic model selection fetches available models from OpenAI, Anthropic, DeepSeek, Google Gemini, and OpenRouter, caching lists and filtering by Aider version and configured API keys; this applies only to solo (non-Architect) mode. -- evidence: [README.md#L225-L229](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L225-L229), [README.md#L231-L231](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L231-L231), [README.md#L223-L223](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L223-L223), [README.md#L239-L242](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L239-L242) (`clm_1034378ab56cd3e5f51ab4c07e8a18581c3f9cd74a9d4dbd472a4a5da5ec72b0`)

## limitations (2 claim(s))

- [observation/documented] The AI-comment file-watching feature (AI!/AI? triggers) currently only works in vterm mode, per the README note. -- evidence: [README.md#L379-L379](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L379-L379), [README.md#L400-L400](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L400-L400), [README.md#L386-L386](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L386-L386) (`clm_7ebb360c50dcfda4bd910cbe82c94a8c47be2624fbd81c7cb861cc80061a121a`)
- [observation/documented] Code added to a session is sent to the AI provider, so users should be mindful of sensitive code; Aider itself currently supports only Python 3.12. -- evidence: [README.md#L544-L544](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L544-L544), [README.md#L541-L541](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L541-L541) (`clm_308533db8848fcad6254185c0eec8bbda3f1668fdabbfe76d3911e848437f916`)

## relevance (1 claim(s))

- [observation/documented] Aidermacs began as a fork of aider.el and diverged to prioritize Emacs-native workflows, positioning itself as an Emacs-centric alternative to Cursor-style AI editors. -- evidence: [README.md#L589-L589](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L589-L589), [README.md#L15-L15](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L15-L15), [README.md#L587-L587](https://github.com/MatthewZMD/aidermacs/blob/b9a2512e54d8366a0b0472c418d1d2610c98c3ae/README.md#L587-L587) (`clm_2471b364d19ac56aaab526c979b55921072e6deed10a60f9ad1a7bcfa881fca8`)

