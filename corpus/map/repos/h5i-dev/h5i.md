# h5i-dev/h5i

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ec1a18cd4f2d @ 0b836cce6be3abbe

## Summary (orientation draft, not independently verified)

Selected evidence records: The manual's command table lists groups including browser, box, box share, ui, runner, skill, plugin, websec, recon, join, and shell completions. Browser sessions are driven by verbs such as open, snapshot, click, type, extract, markdown, requests, audit, screenshot, reload, and close, with @ref handles identifying page elements.

## Source coverage

Source coverage (partial): 6 of 28 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The engine is the HTTP client: every request is policy-checked and recorded before bytes move, and a fetch that cannot be recorded is refused, so the log is a decision record. -- evidence: [MANUAL.md#L229-L234](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L229-L234), [MANUAL.md#L14-L16](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L14-L16)
  - [observation/documented] A session grants only the origin it was opened on; --allow adds named origins, loopback is reachable by default unless --no-loopback, and off-origin subresources are refused and logged. -- evidence: [MANUAL.md#L252-L254](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L252-L254), [MANUAL.md#L245-L250](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L245-L250)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The manual's command table lists groups including browser, box, box share, ui, runner, skill, plugin, websec, recon, join, and shell completions. -- evidence: [MANUAL.md#L137-L149](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L137-L149)
  - [observation/documented] Browser sessions are driven by verbs such as open, snapshot, click, type, extract, markdown, requests, audit, screenshot, reload, and close, with @ref handles identifying page elements. -- evidence: [README.md#L99-L107](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/README.md#L99-L107), [README.md#L39-L44](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/README.md#L39-L44), [MANUAL.md#L165-L173](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L165-L173)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Boxes are disposable environments holding code, agent, toolchain and optionally the browser session; box export produces a patch, report, receipt and timelines, and the agent has no direct host write path. -- evidence: [MANUAL.md#L35-L50](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L35-L50), [MANUAL.md#L93-L96](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L93-L96)
- tools-permissions (1 claim(s)):
  - [observation/documented] By default a session runs unsandboxed on the host machine; --in places it in a box whose egress allowlist is enforced at a network boundary outside the engine. -- evidence: [MANUAL.md#L225-L227](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L225-L227), [MANUAL.md#L334-L339](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L334-L339), [MANUAL.md#L369-L373](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L369-L373)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] h5i is one Rust binary with no server, daemon, or SaaS; websec and recon are optional plugins shipped as separate archives and registered via h5i plugin install. -- evidence: [MANUAL.md#L29-L29](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L29-L29), [MANUAL.md#L117-L120](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L117-L120)
- limitations (3 claim(s)):
  - [observation/documented] The manual states the browser is incomplete: Canvas, WebSockets, Workers and IndexedDB are absent, and of twenty SPAs measured, eighteen read usefully and one not at all. -- evidence: [MANUAL.md#L58-L70](https://github.com/h5i-dev/h5i/blob/ec1a18cd4f2d2052c19bb56f3811a27ee619eada/MANUAL.md#L58-L70)
More evidence: [full detail](h5i.detail.md)

Metadata and full claim list: [full detail](h5i.detail.md)
Human notes ([notes](h5i.notes.md), never overwritten by build)

[Back to map index](../../index.md)
