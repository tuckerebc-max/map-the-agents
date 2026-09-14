# willynikes2/agent-orchestrator

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f99e1eaf7414 @ d5e8c36bd6e17b77

## Summary (orientation draft, not independently verified)

A README-only snapshot describes a terminal-based multi-agent orchestrator (single Python file) that wraps Claude, Codex, and Gemini CLIs with role-based failover, auto-downtime detection, knowledge-base integration, and configurable permission modes. No source code is included in the evidence, so all claims are documentation-based.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is a terminal-based orchestrator wrapping Claude, Codex, and Gemini CLIs with automatic failover and a shared knowledge base, advertised at roughly $60/month in subscriptions. -- evidence: [README.md#L5-L5](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The implementation is a single ~1100-line Python file, daniel.py, containing config handling, per-agent CLI/API call functions, failover logic, auto-downtime detection, and KB context search. -- evidence: [README.md#L250-L250](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L250-L250), [README.md#L231-L248](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L231-L248)
- design-choices (1 claim(s)):
  - [observation/documented] Default role chains differ by role: orchestrator and review prefer Claude first, implementation prefers Codex first, and uidocs prefers Gemini first. -- evidence: [README.md#L30-L33](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L30-L33)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: setup involves cloning, creating a virtualenv, installing requirements, and running 'python3 daniel.py --setup', whose wizard asks for name, per-agent mode, permission mode, optional API keys, model IDs, and chain preferences. -- evidence: [README.md#L63-L69](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L63-L69), [README.md#L55-L61](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L55-L61)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The REPL exposes slash commands including /setup, /models, /modes, /task, /run, /smoke, /kb, /service status/down/up/recover, /allow-dir, and /quit. -- evidence: [README.md#L97-L119](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L97-L119)
  - [observation/documented] Prefix routing sends 'impl:' messages to the implementation chain and 'ui:' to the UI chain, while @claude/@codex/@gemini address a specific agent directly, bypassing failover. -- evidence: [README.md#L157-L157](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L157-L157), [README.md#L165-L165](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L165-L165), [README.md#L121-L126](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L121-L126)
- memory-state (1 claim(s)):
  - [observation/documented] When a knowledge-base-server is running, the orchestrator searches it for relevant context before each response and injects KB results for the active task; kb_port is configurable for non-default ports. -- evidence: [README.md#L141-L141](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L141-L141), [README.md#L148-L149](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L148-L149), [README.md#L153-L153](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L153-L153)
- orchestration (2 claim(s)):
  - [observation/documented] Messages are routed through ordered role chains; when an agent fails or is down, the next agent in the chain is tried, and if all fail an error with recovery options is shown. -- evidence: [README.md#L28-L28](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L28-L28), [README.md#L9-L26](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L9-L26)
  - [observation/documented] Auto-downtime detection maps error patterns to actions: usage caps disable until reset, rate limits trigger a 5-minute cooldown, auth failures and bad models require manual re-enabling via /service up. -- evidence: [README.md#L219-L225](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L219-L225)
- tools-permissions (2 claim(s)):
  - [observation/documented] Codex and Gemini CLI permission modes are configurable between full-host-unattended (default) and sandboxed-auto; the former runs Codex with --dangerously-bypass-approvals-and-sandbox and Gemini with yolo approval and sandbox disabled. -- evidence: [README.md#L63-L69](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L63-L69), [README.md#L199-L203](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L199-L203), [README.md#L205-L207](https://github.com/willynikes2/agent-orchestrator/blob/f99e1eaf74149066f970d8804509730f680654ff/README.md#L205-L207)
More evidence: [full detail](agent-orchestrator.detail.md)

Metadata and full claim list: [full detail](agent-orchestrator.detail.md)
Human notes ([notes](agent-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
