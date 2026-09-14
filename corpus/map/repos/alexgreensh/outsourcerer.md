# alexgreensh/outsourcerer

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0ad71828e118 @ bb346553aa25c2f8

## Summary (orientation draft, not independently verified)

Evidence consists of README.md and SECURITY.md for Outsourcerer, a bash-based delegation tool that routes coding tasks across multiple AI engines/lanes with cost tracking, advisor consensus, loops, and security gating. No source code slices are present, so claims are documentation-based.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The tool is described as a self-contained bash script with no server, proxy, or resident process, shelling out to existing CLIs such as claude, codex, devin, and agy. -- evidence: [README.md#L189-L189](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L189-L189)
- design-choices (2 claim(s)):
  - [observation/documented] Routing precedence is explicitly ordered: global -m wins, then --route name mapping, then per-agent frontmatter, then the default lane. -- evidence: [README.md#L224-L224](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L224-L224)
  - [observation/documented] The Tab ledger separates real cash cost (read back exactly from OpenRouter per generation) from subscription plan-limit usage, never labeling subscription spend as free. -- evidence: [README.md#L183-L183](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L183-L183), [README.md#L169-L169](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L169-L169)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the project is audited with repo-forensics (27 scanners, 500+ patterns) on every release, with every finding triaged by name and no suppressions, per README and SECURITY.md. -- evidence: [README.md#L264-L264](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L264-L264), [SECURITY.md#L3-L4](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L3-L4), [SECURITY.md#L8-L11](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L8-L11)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes verbs including run/research/edit/yolo, bg/status/watch/result/logs/cancel, second-opinion, image, tab/estimate, suggest/deals, doctor/models, and parity variants. -- evidence: [README.md#L302-L312](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L302-L312)
  - [observation/documented] Named lanes map to providers: OpenRouter lanes (hy3, glm-5.2, deepseek-*), Codex native (sol/terra/luna), Claude native (fable/opus/sonnet/haiku), keyless Gemini via Antigravity, Hermes, and local ollama:<model>/local lanes. -- evidence: [README.md#L314-L316](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L314-L316)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Delegates are watchdog-supervised to a classified end state (done / blocked / timed-out), with exit codes distinguishing done, done-but-unverified, and blocked, and stalled delegates killed rather than silently retried. -- evidence: [README.md#L191-L191](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L191-L191), [README.md#L216-L216](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L216-L216)
  - [observation/documented] Advisor panels convene several strong models in parallel to review a plan or diff, and work is greenlit only on consensus; a split decision is returned to the user. -- evidence: [README.md#L89-L91](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L89-L91)
- tools-permissions (2 claim(s)):
  - [observation/documented] Before any cloud delegation, a hard-block refuses the route if credential files (.env, id_rsa, credentials, etc.) exist anywhere in the working tree; the scan runs on every call and fails closed. -- evidence: [SECURITY.md#L48-L61](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L48-L61), [README.md#L266-L270](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/README.md#L266-L270)
  - [observation/documented] Keys are read one variable at a time from ~/.env via targeted grep, never sourcing the whole file, and keys are never written into command-line arguments, logs, or config. -- evidence: [SECURITY.md#L34-L41](https://github.com/alexgreensh/outsourcerer/blob/0ad71828e1188dc5c90e1bbde57d28a748d76d0b/SECURITY.md#L34-L41)
More evidence: [full detail](outsourcerer.detail.md)

Metadata and full claim list: [full detail](outsourcerer.detail.md)
Human notes ([notes](outsourcerer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
