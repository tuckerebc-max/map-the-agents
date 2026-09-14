# automazeio/vibeproxy

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 083c13220691 @ 3fe5e881ed22f24d

## Summary (orientation draft, not independently verified)

VibeProxy is a native macOS menu bar app that proxies AI coding tools through users' existing provider subscriptions, built on a bundled CLIProxyAPIPlus server. Evidence covers its architecture, localhost routing, thinking-suffix model interception, token storage, and documented risks.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The app consists of Swift sources (AppDelegate, ServerManager, SettingsView, AuthStatus) plus a bundled cli-proxy-api-plus binary, config.yaml, and icon resources inside the .app. -- evidence: [README.md#L104-L129](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L104-L129)
  - [observation/documented] ServerManager controls the cli-proxy-api server process and OAuth authentication; AuthStatus monitors ~/.cli-proxy-api/ for auth files with real-time updates when files are added or removed. -- evidence: [README.md#L133-L137](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L133-L137)
- design-choices (3 claim(s)):
  - [observation/documented] When a -thinking-* model is used, VibeProxy automatically injects the anthropic-beta interleaved-thinking-2025-05-14 header, merging with existing beta headers without duplicates. -- evidence: [FACTORY_SETUP.md#L538-L538](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L538-L538), [FACTORY_SETUP.md#L559-L562](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L559-L562)
  - [observation/documented] Invalid thinking suffixes (non-integer) are stripped and the vanilla model is used without thinking. -- evidence: [FACTORY_SETUP.md#L522-L523](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L522-L523)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The proxy listens on localhost port 8317; Amp routes /auth/cli-login and /api/* to ampcode.com and /provider/* to CLIProxyAPI on port 8318. -- evidence: [AMPCODE_SETUP.md#L70-L90](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/AMPCODE_SETUP.md#L70-L90), [FACTORY_SETUP.md#L67-L67](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L67-L67)
  - [observation/documented] VibeProxy supports a custom model-name suffix pattern {model}-thinking-{NUMBER} that it intercepts, strips, and converts into a thinking token-budget parameter before forwarding to CLIProxyAPI. -- evidence: [FACTORY_SETUP.md#L502-L502](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L502-L502), [FACTORY_SETUP.md#L515-L520](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L515-L520), [FACTORY_SETUP.md#L497-L498](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L497-L498)
- memory-state (1 claim(s)):
  - [observation/documented] Authentication tokens are stored locally in ~/.cli-proxy-api/ with 0600 permissions and are auto-refreshed before expiration. -- evidence: [FACTORY_SETUP.md#L574-L578](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L574-L578)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The server binds only to localhost (127.0.0.1) and all upstream traffic uses HTTPS, per the security notes. -- evidence: [FACTORY_SETUP.md#L574-L578](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L574-L578)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] VibeProxy is built on CLIProxyAPIPlus (CLIProxyAPI), which provides the core OAuth handling, token management, and API routing; the binary is bundled in the app. -- evidence: [README.md#L104-L129](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L104-L129), [README.md#L141-L141](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L141-L141), [FACTORY_SETUP.md#L599-L599](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L599-L599), [README.md#L16-L16](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/README.md#L16-L16)
- limitations (2 claim(s)):
  - [observation/documented] The docs warn the approach may violate AI providers' terms of service, risking account suspension or bans, and that provider API changes could break it; use is at the user's own risk. -- evidence: [FACTORY_SETUP.md#L582-L593](https://github.com/automazeio/vibeproxy/blob/083c1322069130cbc7955b85bdbc1754a307e9c6/FACTORY_SETUP.md#L582-L593)
More evidence: [full detail](vibeproxy.detail.md)

Metadata and full claim list: [full detail](vibeproxy.detail.md)
Human notes ([notes](vibeproxy.notes.md), never overwritten by build)

[Back to map index](../../index.md)
