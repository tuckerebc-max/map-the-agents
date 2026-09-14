# pythagora-io/gpt-pilot

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9b763fdaf002 @ e71333c416601489

## Summary (orientation draft, not independently verified)

Evidence covers a README security notice describing a credential-stealing supply-chain worm hidden in core/telemetry/ (Aug 2025–11 Jun 2026) in an unmaintained repo, plus product docs for the agent pipeline, CLI, config/workspace, telemetry, and pinned dependencies.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The app-building pipeline uses named agents including Specification Writer, Architect, Tech Lead, Developer, Code Monkey, Reviewer, Troubleshooter, Debugger, and Technical Writer. -- evidence: [README.md#L207-L217](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L207-L217)
- design-choices (4 claim(s)):
  - [observation/documented] Generated code is stored in a workspace folder named after the app name entered at startup; config.json (copied from example-config.json) holds LLM provider keys/endpoints and optional fs.ignore_paths. -- evidence: [README.md#L148-L148](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L148-L148), [README.md#L135-L146](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L135-L146)
  - [observation/documented] GPT Pilot filters code shown to the LLM so each conversation contains only code relevant to the current task rather than the entire codebase, aiming to work at any scale. -- evidence: [README.md#L223-L225](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L223-L225)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI supports listing projects (--list), resuming a project or a specific step (--project <app_id> [--step <step>]), deleting a project (--delete <app_id>), and --help for all options. -- evidence: [README.md#L182-L184](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L182-L184), [README.md#L198-L198](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L198-L198), [README.md#L176-L178](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L176-L178), [README.md#L200-L202](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L200-L202), [README.md#L168-L170](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L168-L170), [README.md#L190-L192](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L190-L192)
  - [observation/documented] Documented warnings state that resuming from a specific step deletes all progress after that step, and that deleting a project cannot be undone. -- evidence: [README.md#L194-L194](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L194-L194), [README.md#L186-L186](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L186-L186)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The Architect agent checks whether the app's technologies are installed on the machine and installs them if not. -- evidence: [README.md#L207-L217](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L207-L217)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] requirements.txt pins Python dependencies including openai 1.40.6, anthropic 0.39.0, groq 0.6.0, sqlalchemy 2.0.32, pydantic 2.8.2, tiktoken 0.8.0, and sentry-sdk 2.20.0. -- evidence: [requirements.txt#L1-L38](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/requirements.txt#L1-L38)
  - [observation/documented] SQLite is the default database; PostgreSQL support requires additionally installing asyncpg and psycopg2 and setting db.url to a postgresql+asyncpg:// URL in config.json. -- evidence: [README.md#L162-L162](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L162-L162), [README.md#L156-L156](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L156-L156), [README.md#L158-L160](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L158-L160)
- limitations (3 claim(s)):
  - [observation/documented] A credential-stealing supply-chain worm was hidden in core/telemetry/ from August 2025 until 11 June 2026; users who cloned and ran GPT Pilot from source in that window are told to rotate credentials. -- evidence: [README.md#L10-L10](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L10-L10), [README.md#L12-L14](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L12-L14), [README.md#L1-L2](https://github.com/Pythagora-io/gpt-pilot/blob/9b763fdaf0020c7d8abacc7b58b2b09e57494623/README.md#L1-L2)
More evidence: [full detail](gpt-pilot.detail.md)

Metadata and full claim list: [full detail](gpt-pilot.detail.md)
Human notes ([notes](gpt-pilot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
