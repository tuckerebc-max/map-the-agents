# Dynamic rubric evaluation

When you evaluate a session, mindwalk does not only grade the four fixed
process dimensions. It first asks the judge to derive criteria from your own
request — what would count as done for *this* task — and then scores the
session against both. This document explains how that works and why it is
built the way it is; for day-to-day usage see the README's
[Session evaluation](../README.md#session-evaluation) section.

## Why fixed dimensions aren't enough

Exploration, scope, wandering, verification are process lenses tuned for
code-editing work. On research, debugging, or documentation sessions they
are systematically too harsh: a legitimate batch of empirical investigation
reads as "wandering". And they cannot answer the question you actually care
about — did the agent do what I asked?

A task-specific rubric can, but generating one on the fly has two failure
modes the design must close:

- **Blind-spot lottery** — a single rubric generation has selection
  variance; an angle that isn't drawn into the criteria never gets evaluated
  at all. So the four fixed dimensions always remain, enforced by Go — the
  rubric only ever adds, never replaces.
- **Epistemic contamination** — the judge only sees one-line event digests,
  and a scorer that cannot verify something tends to record a "cannot
  verify" warning, turning an observability gap into an execution defect. So
  every criterion carries a coverage grade, and what the log cannot verify
  lowers coverage instead of raising findings.

## How a report is produced

Evaluation makes up to two sealed judge calls:

```
mindwalk analyze / evaluate panel (explicit trigger)
  ├─ rubric generation   user messages → distinct tasks → criteria per task
  │                      (skipped, reused from cache, or degraded on failure)
  └─ unified scoring     rubric (as data) + evidence document
                         → dimension findings + per-criterion coverage/findings
```

**Generation** reads the session's user messages (first + latest, capped at
48), enumerates the distinct tasks — a new task means a new deliverable or
goal; follow-ups and corrections fold into the current one — and writes a
handful of criteria per task, each with a title, a why, and what good and
bad look like. Every task is anchored to the user messages that stated it,
which is how the report panel jumps to a task's starting point. Criteria
must be judgeable from one-line event digests alone; criteria that would
need file contents, diffs, or external ground truth are not allowed.

**Scoring** is one pass over the evidence document with the rubric attached
as a data section: the four dimensions and all criteria share the same read
of the session. The judge returns findings only — every claim citing real
timeline events — plus a coverage grade per criterion.

**Verdicts are never the model's.** Go rolls them up mechanically: coverage
none → "no signal"; otherwise problem > warning > good, taken from the
finding severities. Hallucinated citations are stripped, a finding with no
valid citation left is dropped, and an unknown severity or coverage value
invalidates the whole output (retried once).

## When there is no scorecard

The rubric layer steps aside rather than failing the evaluation:

- **No tool events** — nothing is citable, so scoring would strip every
  finding and coast to unearned good verdicts.
- **No or too little task text** — one-word replies carry nothing to derive
  criteria from.
- **Generation failed twice** — the report degrades to dimensions-only.

None of these block the fixed layer. `--no-rubric` on the CLI (or
`"rubric": false` on the analyze API) skips the layer explicitly, in a
single judge call.

## Stability and cost

Re-evaluating a session whose task wording hasn't changed reuses the cached
report's rubric and only re-runs scoring: the criteria don't drift between
runs — scores can move, the yardstick doesn't — and the cost drops back to
one call. A full two-phase evaluation takes roughly twice a dimensions-only
pass, one to two minutes on typical sessions.

The rubric lives inside the report JSON in `~/.mindwalk/reports`; there is
no separate rubric store, so a report and its criteria stay atomic.

## Trust boundaries

The rubric is derived from trace content, and trace content is untrusted —
so the rubric is untrusted too:

- hard caps on shape and size (at most 6 tasks, 3–12 criteria in total,
  ≤12KB of JSON, strict vocabularies for ids, severities, and coverage)
  bound what a hostile session could inject;
- the scoring prompt declares the rubric section as data — imperative text
  inside it is ignored;
- the four fixed dimensions are required and validated by Go regardless of
  what the rubric contains, and the UI renders rubric text as plain text.

Everything else follows the standing evaluation invariants: the judge runs
only on explicit request, the subprocess is sealed (no tools, no user
config, no session persistence), and nothing new lands on disk.
