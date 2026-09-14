---
access: public
aliases: []
claim_ids:
- clm_0ea846dfafc022efcadfdaf9a68e6e6763d098849cd68043d04d8af306ebcd35
- clm_1034378ab56cd3e5f51ab4c07e8a18581c3f9cd74a9d4dbd472a4a5da5ec72b0
- clm_242089bd9f1a8c425d4de35c076a89913d5f526e1a22f55b70a748b6373fd1f9
- clm_2471b364d19ac56aaab526c979b55921072e6deed10a60f9ad1a7bcfa881fca8
- clm_2677a720bb1448bf61bbed694956bd5c54bd6def8b63f9af5d74a49016d67c54
- clm_308533db8848fcad6254185c0eec8bbda3f1668fdabbfe76d3911e848437f916
- clm_367f3727173dababa023e618f5a83300600866e7b2b258ab2542615b977b281e
- clm_436eed0809f3078fda5c1f8df4ed1fe8f5f0188c63581f0151b78cfe215f07d5
- clm_4c19f6b27b7169c64643452cac603a1810d5798e267930bed6cf3b9eba4fe6eb
- clm_67311ea0cf73b7f842afb894c9c41678f5f22508fd31abc6570fadb65f163f22
- clm_7ebb360c50dcfda4bd910cbe82c94a8c47be2624fbd81c7cb861cc80061a121a
- clm_89ca7663f2395484efface4863a1bc2041df5f0b35472b076dc2c88546a3f66a
- clm_a4433adc474f29a8b723ba3f2ba02d16ce504903142e31dc762a83a209ca6318
- clm_be8740f7601d5d8ed98ef775a7a028f957053c003f3b76687a40f776bd2d9a5a
- clm_c9d3f0afb2628ad5b3832e54778bcfd671394d9231bedbb9bfa5eb049650cf5c
- clm_cbfff34147ce070c4e830ea72ab64ae08f6538b8aa0a58e4a9fe087936c0eac8
maturity: draft
page_id: pg_1b5c47838bbf5f80b247222dfd8e6080
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_985634c59b145fe192ae94771d3cf952
title: MatthewZMD/aidermacs/README.md @ b9a2512e54d8
updated_at: '2026-09-14T04:08:37Z'
---

# MatthewZMD/aidermacs/README.md @ b9a2512e54d8

<!-- rcw:begin owner=source:src_985634c59b145fe192ae94771d3cf952 block=evidence -->
- Two terminal backends are supported: comint (default, Emacs built-in) and vterm (better terminal compatibility), selected via aidermacs-backend. [@claim:clm_0ea846dfafc022efcadfdaf9a68e6e6763d098849cd68043d04d8af306ebcd35]
- Dynamic model selection fetches available models from OpenAI, Anthropic, DeepSeek, Google Gemini, and OpenRouter, caching lists and filtering by Aider version and configured API keys; this applies only to solo (non-Architect) mode. [@claim:clm_1034378ab56cd3e5f51ab4c07e8a18581c3f9cd74a9d4dbd472a4a5da5ec72b0]
- The aidermacs-before-run-backend-hook runs custom setup before the backend starts, using a copy of process-environment so secrets set there affect only the Aider backend. [@claim:clm_242089bd9f1a8c425d4de35c076a89913d5f526e1a22f55b70a748b6373fd1f9]
- Aidermacs began as a fork of aider.el and diverged to prioritize Emacs-native workflows, positioning itself as an Emacs-centric alternative to Cursor-style AI editors. [@claim:clm_2471b364d19ac56aaab526c979b55921072e6deed10a60f9ad1a7bcfa881fca8]
- Aidermacs wraps the external Aider tool (or its community fork aider-ce), requiring Emacs >= 26.1 and the Transient package. [@claim:clm_2677a720bb1448bf61bbed694956bd5c54bd6def8b63f9af5d74a49016d67c54]
- Code added to a session is sent to the AI provider, so users should be mindful of sensitive code; Aider itself currently supports only Python 3.12. [@claim:clm_308533db8848fcad6254185c0eec8bbda3f1668fdabbfe76d3911e848437f916]
- Auto-commits of AI-generated changes are disabled by default (unlike Aider's default), and can be re-enabled via aidermacs-auto-commits. [@claim:clm_367f3727173dababa023e618f5a83300600866e7b2b258ab2542615b977b281e]
- The main interface is a Magit-like transient menu, invoked via M-x aidermacs-transient-menu or a user-bound key such as C-c a. [@claim:clm_436eed0809f3078fda5c1f8df4ed1fe8f5f0188c63581f0151b78cfe215f07d5]
- Architect mode uses two models: an Architect model for reasoning and an Editor model for code generation; each can be configured independently via aidermacs-architect-model and aidermacs-editor-model. [@claim:clm_4c19f6b27b7169c64643452cac603a1810d5798e267930bed6cf3b9eba4fe6eb]
- Configuration precedence: if an .aider.conf.yml is found it takes highest priority and Emacs variables are ignored; otherwise Emacs variables override environment variables, which override built-in defaults. [@claim:clm_67311ea0cf73b7f842afb894c9c41678f5f22508fd31abc6570fadb65f163f22]
- The AI-comment file-watching feature (AI!/AI? triggers) currently only works in vterm mode, per the README note. [@claim:clm_7ebb360c50dcfda4bd910cbe82c94a8c47be2624fbd81c7cb861cc80061a121a]
- When enabled, diff review captures pre-edit file state and shows changes through Emacs' built-in ediff interface for accept/reject review; controlled by aidermacs-show-diff-after-change (default t). [@claim:clm_89ca7663f2395484efface4863a1bc2041df5f0b35472b076dc2c88546a3f66a]
- Files added as editable grant the AI read and modify permission; any add-file command prefixed with C-u adds the file as read-only instead. [@claim:clm_a4433adc474f29a8b723ba3f2ba02d16ce504903142e31dc762a83a209ca6318]
- Prompt history and a curated common-prompts list (aidermacs-common-prompts) are saved and available across all sessions via completion. [@claim:clm_be8740f7601d5d8ed98ef775a7a028f957053c003f3b76687a40f776bd2d9a5a]
- By default Aidermacs requires explicit confirmation before applying Architect-mode changes; setting aidermacs-auto-accept-architect to t enables automatic acceptance. [@claim:clm_c9d3f0afb2628ad5b3832e54778bcfd671394d9231bedbb9bfa5eb049650cf5c]
- The transient menu includes session commands (start/open, clear history, reset, exit), persistent mode toggles (Code, Chat/Ask, Architect, Help), utilities, file actions, and code actions, with 'All File Actions' and 'All Code Actions' submenus. [@claim:clm_cbfff34147ce070c4e830ea72ab64ae08f6538b8aa0a58e4a9fe087936c0eac8]
<!-- rcw:end owner=source:src_985634c59b145fe192ae94771d3cf952 block=evidence -->

## Researcher notes

