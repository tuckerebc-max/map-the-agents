# automazeio/vibeproxy -- full detail

[Back to orientation](vibeproxy.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/automazeio/vibeproxy/083c1322069130cbc7955b85bdbc1754a307e9c6/3fe5e881ed22f24d.json](../../../wiki/dossiers/automazeio/vibeproxy/083c1322069130cbc7955b85bdbc1754a307e9c6/3fe5e881ed22f24d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The app consists of Swift sources (AppDelegate, ServerManager, SettingsView, AuthStatus) plus a bundled cli-proxy-api-plus binary, config.yaml, and icon resources inside the .app. -- evidence: [README.md#L104-L129](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L104-L129) (`clm_6efbb2bee8d58a96595c15b4a097df464bbf24f615f1a118a2331b6d8d9eac0a`)
- [observation/documented] ServerManager controls the cli-proxy-api server process and OAuth authentication; AuthStatus monitors ~/.cli-proxy-api/ for auth files with real-time updates when files are added or removed. -- evidence: [README.md#L133-L137](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L133-L137) (`clm_67cff387cb084f210552ee6a206d247a3144b2988d37b028466c44fe9bc452ea`)

## design-choices (3 claim(s))

- [observation/documented] When a -thinking-* model is used, VibeProxy automatically injects the anthropic-beta interleaved-thinking-2025-05-14 header, merging with existing beta headers without duplicates. -- evidence: [FACTORY_SETUP.md#L538-L538](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L538-L538), [FACTORY_SETUP.md#L559-L562](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L559-L562) (`clm_05ead5e303fe0aa6818c350e3777463310d17849d8da645773f831ec8cc6d9d1`)
- [observation/documented] Invalid thinking suffixes (non-integer) are stripped and the vanilla model is used without thinking. -- evidence: [FACTORY_SETUP.md#L522-L523](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L522-L523) (`clm_1ca2a64908f966c79e9e393fe9ceb99bbd05bab845401b9f80d2b3959f69bde5`)
- [observation/documented] Multiple accounts per provider are supported with automatic round-robin distribution and failover when rate-limited; provider enable/disable toggles hot-reload instantly without restart. -- evidence: [README.md#L37-L46](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L37-L46), [AMPCODE_SETUP.md#L102-L102](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/AMPCODE_SETUP.md#L102-L102) (`clm_7dd0a1f0c84cdae1d84dc655a5af37530b11c8adbd35eccf469d1c48464957f2`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The proxy listens on localhost port 8317; Amp routes /auth/cli-login and /api/* to ampcode.com and /provider/* to CLIProxyAPI on port 8318. -- evidence: [AMPCODE_SETUP.md#L70-L90](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/AMPCODE_SETUP.md#L70-L90), [FACTORY_SETUP.md#L67-L67](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L67-L67) (`clm_4d2469188cca33a84190b73e85f0dfe5f2b3b8be6a8b5419247e1ae0703d6645`)
- [observation/documented] VibeProxy supports a custom model-name suffix pattern {model}-thinking-{NUMBER} that it intercepts, strips, and converts into a thinking token-budget parameter before forwarding to CLIProxyAPI. -- evidence: [FACTORY_SETUP.md#L502-L502](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L502-L502), [FACTORY_SETUP.md#L515-L520](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L515-L520), [FACTORY_SETUP.md#L497-L498](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L497-L498) (`clm_3c8f1fd78531f4f707a264dbc25b58634b776715c51d27b8bbbc92181db2a2d6`)

## memory-state (1 claim(s))

- [observation/documented] Authentication tokens are stored locally in ~/.cli-proxy-api/ with 0600 permissions and are auto-refreshed before expiration. -- evidence: [FACTORY_SETUP.md#L574-L578](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L574-L578) (`clm_fcf34ef3a1f93d2898b179715e61a4817633c5f770ca70e9bef45fb51bb12cb8`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The server binds only to localhost (127.0.0.1) and all upstream traffic uses HTTPS, per the security notes. -- evidence: [FACTORY_SETUP.md#L574-L578](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L574-L578) (`clm_bab7457310437f50bdb1d1acc8d28207356647d461fdbd0d8cf97828d4d5d5c6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] VibeProxy is built on CLIProxyAPIPlus (CLIProxyAPI), which provides the core OAuth handling, token management, and API routing; the binary is bundled in the app. -- evidence: [README.md#L104-L129](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L104-L129), [README.md#L141-L141](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L141-L141), [FACTORY_SETUP.md#L599-L599](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L599-L599), [README.md#L16-L16](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L16-L16) (`clm_982b0196c9f614c2b3ea75b14c96a1f92b4f8e3a43b48c6402cb2a7a90d60933`)

## limitations (2 claim(s))

- [observation/documented] The docs warn the approach may violate AI providers' terms of service, risking account suspension or bans, and that provider API changes could break it; use is at the user's own risk. -- evidence: [FACTORY_SETUP.md#L582-L593](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L582-L593) (`clm_77821df021b828d4c1e714a6d3e20014cfa35c0a6e11819ac828ff95e8e2278b`)
- [observation/documented] The Intel build is marked untested with users asked to report issues; the app requires macOS 13 (Ventura) or later. -- evidence: [README.md#L51-L51](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L51-L51), [README.md#L98-L98](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L98-L98), [README.md#L55-L60](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L55-L60) (`clm_f2ed4425d9833dae9312eb707ad4d498dc777c463e8ce2e4d0154e09d24797ab`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

