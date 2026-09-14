# Contributing to mole

Thank you for looking. This document covers the licence question first, because
it is the one thing you cannot undo after clicking "Create pull request", and
then how the project expects code to be written — which is more demanding than
most, and deliberately so.

## Licensing, and why there is a CLA

**mole is Apache-2.0, and every released version stays Apache-2.0 forever.**

Contributions are accepted under a Contributor License Agreement. The CLA asks
you to grant the maintainer a licence to your contribution that is broader than
Apache-2.0 alone — specifically, the right to release it under other terms in
future versions.

It exists for one reason, and it is worth stating plainly rather than leaving
you to infer it: mole is intended to become a business, and if a well-funded
company packages it as a hosted service, the project needs to be able to
respond. Without a CLA that response would require the written consent of every
contributor, which is impossible in practice and therefore not a real option.

What that does **not** mean:

- **No released version can be taken away.** This is not a promise in prose — it
  is §7 of the [CLA](CLA.md), which binds the maintainer: releases already made
  stay Apache-2.0 permanently, a licence change applies only to versions released
  after it and must be announced first, and your contribution ships under
  Apache-2.0 in the release it first appears in.
- **You keep your copyright.** The CLA is a licence grant, not an assignment.
  Your contribution remains yours to use however you like, including in other
  projects under any licence you choose.
- **No plan is in motion.** As of this writing the intended business model is
  hosted convenience and bundled inference, neither of which requires
  restricting the source. The CLA is insurance against a scenario that may never
  arrive.

If that trade is not one you want to make, that is a legitimate position and no
argument is needed — open an issue describing the bug or the design instead. A
precise issue is often worth more than a patch.

Sign-off is also required on every commit (`git commit -s`). The two coexist and
answer different questions: the
[DCO](https://developercertificate.org/) asks whether you have the right to submit
the code, the CLA asks what the project may do with it.

If you are contributing work your employer owns — most work written on company
time or equipment — your employer signs the corporate agreement in the same
document.

### Copyright headers

There are none, and please do not add them. Copyright is recorded once in
`NOTICE`. Per-file headers are permitted by Apache-2.0 and add a maintenance
burden — a stale year in three hundred files — for no legal benefit that `NOTICE`
does not already provide.

## How this project expects code to be written

mole is a research tool whose entire value is that its answers can be trusted.
That makes the standard for changes higher than "the tests pass".

### Falsify your own fix

**This is the one non-negotiable practice.** After a change, revert the mechanism
— not the test — and confirm the test fails. A test that passes with the fix
removed proves nothing, and this project has caught several of its own tests
doing exactly that.

Say so in the pull request:

> Falsified: reverted the offset check in `merge.go:214`, `TestOffsetsSurvive`
> fails with `offset = 0, want 4096`. Restored, passes.

If you cannot make the test fail, the test is wrong. Fix it before the code.

### The test must describe a failure, not a feature

Test names are sentences about what must not happen —
`TestARowWithNoKeyIsDropped`, `TestAPageCannotCloseItsOwnFence`. The comment
above a test says what breaks in the real world if it regresses, and where the
bug came from if it is a regression test. "Tests the merge function" is not a
comment.

### Comments carry the argument, not the mechanics

The code says what it does. A comment exists to record **why this and not the
obvious alternative**, and especially what was measured. `// increment counter`
adds nothing; `// p75 rather than the mean because the reservation should
usually cover the call` is the reason someone will need in a year.

If you changed an approach because you measured something, put the number in the
comment. Most of the useful comments in this codebase are numbers.

### Dependencies

mole builds `CGO_ENABLED=0` into a single static binary, and every dependency is
permissive-licensed. Both properties are load-bearing: the first is a stated
product promise, the second keeps future commercial editions possible.

A new dependency needs an argument in the pull request. A new **copyleft**
dependency (GPL, LGPL, MPL, AGPL) will not be merged. A dependency requiring cgo
will not be merged.

### Scope

One change per pull request. A bug fix that also renames three things and
reformats a file is three pull requests, and the review will ask for them
separately.

## Before you open a pull request

```bash
gofmt -l .          # must print nothing
go build ./...
go test ./...       # must be clean, and no new skips
go vet ./...
```

A test that **skips** is not a test that passes. If your change makes tests skip
in an environment where they used to run, that is a defect — this project has
shipped that bug too.

## Commit messages

Conventional Commits for the subject (`fix(dataset): …`, `feat(compute): …`),
then a body that explains *why*, including what was measured and what was ruled
out. Look at `git log` for the house style. Long bodies are welcome; the history
is documentation.

## Reporting a bug

The most useful report contains the command you ran, what you expected, what
happened, and the session id if there is one (`mole sessions`). If the problem
involves a model's output, `mole trace <session>` shows the per-call breakdown,
and recording a cassette (`MOLE_RECORD=record`) makes the failure reproducible
for someone who does not have your API keys.

## Security

Do not open a public issue for a vulnerability. See `SECURITY.md` if present, or
contact the maintainer directly. The parts of this codebase where a security
report is most valuable are the prompt-injection fences (§3.2), the aggregation
gate (§12.1), the sandbox flags (§3.6), and the credential handling (§3.5).
