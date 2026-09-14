# cuga-project/cuga-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 65bdf2fb376d @ 17a8859526cc0069

## Summary (orientation draft, not independently verified)

Evidence covers CUGA, a generalist enterprise agent, including an A2A two-process example (consumer/provider over JSON-RPC), a Python SDK, skills, policies, multi-provider LLM configuration, and benchmark ranking claims. Most support is documentation rather than inspected code. Evidence: 6 of 23 candidate files stored (README.md, design.md, todos.md, a Langfuse issue note, and the A2A example README); 17 omitted by file/byte budget, including AGENTS.md, CONTRIBUTING.md and most docs/examples; selection incomplete.

## Source coverage

Source coverage (partial): 6 of 23 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The provider side uses a supervisor YAML declaring one internal agent (digital_sales) that pulls tools from the registry; DYNACONF_A2A__ENABLED=true and a supervisor config path env var route inbound A2A requests through it. -- evidence: [docs/examples/a2a_two_cuga/README.md#L80-L84](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L80-L84)
  - [observation/documented] A registry component serves the digital_sales OpenAPI tool catalog on http://localhost:8001, started with 'cuga start registry' in the example. -- evidence: [docs/examples/a2a_two_cuga/README.md#L73-L76](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L73-L76), [docs/examples/a2a_two_cuga/README.md#L32-L36](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L32-L36)
- design-choices (3 claim(s)):
  - [observation/documented] Configuration resolution priority is documented as environment variables highest, TOML configuration medium, and default values lowest. -- evidence: [README.md#L206-L208](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L206-L208)
  - [observation/documented] The optional run receipt (run_receipt, default false) records tool data in timings-only mode: name, app, and duration only, never arguments, results, or errors, unless track_tool_calls=True is set. -- evidence: [README.md#L542-L544](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L542-L544), [README.md#L564-L567](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L564-L567)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are SKILL.md files with YAML frontmatter requiring name and description; CUGA lists short descriptions in the prompt and exposes a load_skill tool that returns the full markdown body on demand. -- evidence: [README.md#L420-L420](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L420-L420), [README.md#L403-L403](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L403-L403)
  - [observation/documented] A single skills root is configured via [skills] root in settings.toml or DYNACONF_SKILLS__ROOT (default 'cuga'); CUGA scans one directory only, with no merge across paths. -- evidence: [README.md#L407-L407](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L407-L407)
- interfaces (2 claim(s)):
  - [observation/documented] The provider exposes an A2A surface: a JSON-RPC endpoint at /a2a and an AgentCard at /.well-known/agent.json, per the example's documented URLs. -- evidence: [docs/examples/a2a_two_cuga/README.md#L47-L53](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L47-L53), [docs/examples/a2a_two_cuga/README.md#L73-L76](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L73-L76), [docs/examples/a2a_two_cuga/README.md#L38-L44](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/docs/examples/a2a_two_cuga/README.md#L38-L44)
  - [observation/documented] The Python SDK exposes CugaAgent(tools=[...]) with await agent.invoke(message), real-time agent.stream(), per-user thread_id session isolation, and access to the underlying LangGraph graph. -- evidence: [README.md#L473-L473](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L473-L473), [README.md#L521-L531](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L521-L531)
- memory-state (1 claim(s)):
  - [observation/documented] A built-in knowledge engine ingests PDFs, Office files, HTML, Markdown, and images via Docling, with documents scoped either agent-level (permanent, shared) or session-level (per-thread, isolated). -- evidence: [README.md#L76-L76](https://github.com/cuga-project/cuga-agent/blob/65bdf2fb376d9edaa8e929334dbc665d24b9a079/README.md#L76-L76)
- orchestration (1 claim(s)):
More evidence: [full detail](cuga-agent.detail.md)

Metadata and full claim list: [full detail](cuga-agent.detail.md)
Human notes ([notes](cuga-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
