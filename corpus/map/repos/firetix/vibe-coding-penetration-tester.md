# firetix/vibe-coding-penetration-tester

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2625ff0bc570 @ 6c023b9835b4eea6

## Summary (orientation draft, not independently verified)

VibePenTester is an AI-assisted web security scanner with a multi-agent CLI and Flask web UI, supporting OpenAI/Anthropic/Ollama providers, Playwright automation, scope-aware scanning, and Markdown/JSON report generation. Evidence is mostly README documentation; no agent source code is included in the slices.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The tool coordinates specialized security agents to discover and validate common web vulnerabilities and generates reproducible Markdown and JSON reports. -- evidence: [README.md#L9-L9](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L9-L9)
- components (1 claim(s)):
  - [observation/documented] The repository includes a CLI entrypoint (main.py), modular Flask web API (run_web.py, web_api/), a legacy web_ui.py, agents/, tools/, and sample reports directories. -- evidence: [README.md#L23-L31](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L23-L31)
- design-choices (1 claim(s)):
  - [observation/documented] Scanning is scope-aware with three scope modes: url, domain, and subdomain. -- evidence: [README.md#L13-L19](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L13-L19), [README.md#L134-L142](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L134-L142)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: tests are run via ./run_tests.sh or focused pytest suites (unit, integration, API E2E, frontend E2E, Vercel preview) with markers defined in pytest.ini. -- evidence: [README.md#L203-L209](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L203-L209), [README.md#L195-L195](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L195-L195), [README.md#L211-L211](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L211-L211), [README.md#L197-L199](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L197-L199)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI accepts --url (required), --model (default gpt-5.2), --provider (openai/anthropic/ollama), --scope, --output, --verbose, and --ollama-url options. -- evidence: [README.md#L134-L142](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L134-L142)
  - [observation/documented] The modular web app exposes session, scan, activity, logs, and report endpoints such as POST /api/scan/start, POST /api/scan/cancel, and GET /api/report/<report_id>. -- evidence: [README.md#L169-L181](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L169-L181)
- memory-state (1 claim(s)):
  - [observation/documented] A session fix added Flask session cookies, cookie-prioritized session tracking, and file-based session persistence so sessions survive server restarts. -- evidence: [README_SESSION_FIX.md#L50-L56](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README_SESSION_FIX.md#L50-L56), [README_SESSION_FIX.md#L14-L18](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README_SESSION_FIX.md#L14-L18)
- orchestration (1 claim(s)):
  - [observation/documented] A multi-agent scan workflow covers discovery, planning, and vulnerability testing, with browser automation via Playwright for realistic interaction testing. -- evidence: [README.md#L13-L19](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L13-L19)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] requirements.txt pins openai, anthropic, playwright, flask, fastapi, uvicorn, pydantic, PyJWT, psycopg, and pytest-based test dependencies, among others. -- evidence: [requirements.txt#L1-L17](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/requirements.txt#L1-L17), [requirements.txt#L20-L23](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/requirements.txt#L20-L23)
  - [observation/documented] The tool requires at least one LLM provider: an OpenAI API key, an Anthropic API key, or an Ollama server (default localhost:11434). -- evidence: [README.md#L35-L40](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L35-L40), [README.md#L61-L65](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L61-L65)
- limitations (1 claim(s)):
  - [observation/documented] The tool is restricted by its own notice to targets the user owns or has explicit authorization to test; unauthorized scanning may violate law and policy. -- evidence: [README.md#L228-L228](https://github.com/firetix/vibe-coding-penetration-tester/blob/2625ff0bc570633fa4bd0c6bc812b3d08bb757fa/README.md#L228-L228)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](vibe-coding-penetration-tester.detail.md) for every claim.)

Metadata and full claim list: [full detail](vibe-coding-penetration-tester.detail.md)
Human notes ([notes](vibe-coding-penetration-tester.notes.md), never overwritten by build)

[Back to map index](../../index.md)
