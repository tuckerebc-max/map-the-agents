# prime-radiant-inc/evener

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ea6649c17c5d @ afd5117241fc1a76

## Summary (orientation draft, not independently verified)

Selected evidence records: The product ships three binaries: `evener` (non-interactive CLI engine), `evener hub` (browser-based orchestrator for many concurrent sessions), and `evener tui` (terminal dashboard), plus a one-shot `llmcall` client. The hub listens on 127.0.0.1:9180, prints a one-time auth URL that sets an authorizing browser cookie, and offers a /new session page, /credentials page, fork-from-message, /aside side threads, transparent resume, and Ctrl/⌘K search.

## Source coverage

Source coverage (partial): 6 of 841 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The repo is a multi-module Go monorepo (llm, agent, auth libraries plus the app) where binaries couple only via the appwire and hubapi wire contracts, never by importing each other's code; libraries may never import app code. -- evidence: [docs/architecture.md#L33-L37](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L33-L37), [docs/architecture.md#L15-L20](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L15-L20), [docs/architecture.md#L39-L41](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L39-L41), [docs/architecture.md#L11-L13](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L11-L13), [docs/architecture.md#L30-L31](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L30-L31), [docs/architecture.md#L78-L84](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L78-L84)
  - [observation/documented] A repeated-call breaker keys a per-session ledger on tool name plus a hash of raw argument bytes: the third consecutive same-class failure is refused before dispatch, and a repetition trigger nudges on byte-identical result bodies without refusing, so communicate is never blocked. -- evidence: [docs/architecture.md#L221-L228](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L221-L228), [docs/architecture.md#L202-L219](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L202-L219)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: build and install from source with make build / build-hub / build-llmcall / make install, run `make help` for targets, and note that vet/test-race/lint gates iterate over every module since a root-only `go test ./...` skips the library suites in a workspace. -- evidence: [README.md#L389-L391](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L389-L391), [docs/architecture.md#L66-L74](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L66-L74), [README.md#L40-L42](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L40-L42), [README.md#L154-L156](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L154-L156), [README.md#L121-L122](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L121-L122), [README.md#L13-L23](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L13-L23)
- skills-patterns (1 claim(s)):
  - [observation/documented] Standalone user skills in the config skills directory are discovered automatically, extra skill paths can be added via skills_dirs in launch.toml or CLI flags, and user-global slash commands are read from a commands directory when present. -- evidence: [README.md#L60-L69](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L60-L69), [README.md#L71-L88](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L71-L88)
- interfaces (3 claim(s)):
  - [observation/documented] The product ships three binaries: `evener` (non-interactive CLI engine), `evener hub` (browser-based orchestrator for many concurrent sessions), and `evener tui` (terminal dashboard), plus a one-shot `llmcall` client. -- evidence: [README.md#L150-L150](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L150-L150), [docs/architecture.md#L11-L13](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L11-L13), [README.md#L379-L379](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L379-L379), [README.md#L3-L8](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L3-L8), [README.md#L116-L117](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L116-L117), [README.md#L209-L211](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L209-L211)
  - [observation/documented] The hub listens on 127.0.0.1:9180, prints a one-time auth URL that sets an authorizing browser cookie, and offers a /new session page, /credentials page, fork-from-message, /aside side threads, transparent resume, and Ctrl/⌘K search. -- evidence: [README.md#L98-L99](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L98-L99), [README.md#L101-L103](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L101-L103), [README.md#L126-L136](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L126-L136), [README.md#L105-L112](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L105-L112)
- memory-state (1 claim(s)):
More evidence: [full detail](evener.detail.md)

Metadata and full claim list: [full detail](evener.detail.md)
Human notes ([notes](evener.notes.md), never overwritten by build)

[Back to map index](../../index.md)
