# Research Notes

## Ports And Adapters

Primary source: Alistair Cockburn's original 2005 article,
<https://alistair.cockburn.us/hexagonal-architecture>.

Relevant takeaways for CodeAlmanac:

- The useful distinction is inside versus outside. Code that represents
  CodeAlmanac's product decisions should not leak into code that talks to
  Commander, SQLite, launchd, provider SDKs, or external transcript stores.
- A port is a purposeful conversation, not a generic suffix. Good candidates in
  this repo are provider runtime execution, transcript discovery, run storage,
  wiki graph storage/query, and scheduler installation/status.
- The pattern explicitly allows several adapters for one port. This supports
  one capture discovery contract with Claude and Codex adapters, rather than a
  separate manual Claude scanner and scheduled Claude/Codex scanners.
- The pattern should not become folder-name theater. Cockburn's point is the
  boundary and the contract; for this repo, a simple domain directory plus a
  small interface is often enough.

Applied recommendation:

```ts
// arch: one capture discovery conversation, multiple source adapters
const sessions = await capture.discovery.find({
  apps: ["claude", "codex"],
  repoRoot,
  scope: capture.discovery.scope.fromManualFlags(flags),
});

const selected = capture.selection.manual(sessions, flags);
const result = await operations.absorb.start({ targetKind: "session", targetPaths: selected.paths });
```

This is ports/adapters in a small-tool style: the domain names the conversation,
but there is no need for an enterprise `Ports/Adapters/Application/Infrastructure`
directory stack.

## Functional Core, Imperative Shell

Primary source: Gary Bernhardt's "Boundaries" talk page,
<https://www.destroyallsoftware.com/talks/boundaries>.

Relevant takeaways for CodeAlmanac:

- Keep policy and decisions as value transformations where possible.
- Keep filesystem, child processes, launchd, provider SDKs, and stdout/stderr at
  the edge.
- This repo already does this well in some places: capture sweep computes
  eligibility decisions from candidates, ledger entries, and timestamps, then
  calls a supplied `startCapture` function at the edge.
- The same style should replace `sqlite-free.ts`: command definitions can be
  pure-ish data/action shapes, while imports and native dependency checks happen
  only when a command actually needs them.

Applied recommendation:

```ts
// arch: command shape is cheap; implementation import is the effect
program.command("search [query]")
  .option("--mentions <path>")
  .action(async (query, opts) => {
    const { runSearch } = await import("./commands/search.js");
    emit(await runSearch({ cwd: process.cwd(), query, mentions: opts.mentions }));
  });
```

This keeps Commander as the parser and avoids a second parser for
SQLite-free commands.

## Commander Prior Art

Source: Commander documentation,
<https://github.com/tj/commander.js>.

Relevant takeaways for CodeAlmanac:

- Commander supports subcommands, action handlers, async action handlers, and
  stand-alone executable subcommands.
- CodeAlmanac does not need separate executables for every command; that would
  add packaging surface and make the CLI feel less local.
- The useful piece is that action handlers can be async. A registration module
  can define command syntax without importing implementation modules until the
  selected command runs.

Applied recommendation:

- Keep one binary.
- Keep grouped help.
- Replace `sqlite-free.ts` with lazy action imports.
- Keep the early ABI guard for commands that do need SQLite.
- Make the skip-list a small command metadata table rather than a second parser.

## Anti-Pattern To Avoid

Do not rename the whole repository around a textbook pattern:

```text
src/application/
src/domain/
src/infrastructure/
src/adapters/
```

That would hide the product nouns that already work: `wiki`, `capture`,
`operations`, `process`, `harness`, `agent`, `platform`, `viewer`, `config`.

The target architecture should preserve those nouns and fix the places where a
product conversation has two paths or where one module carries both command
parsing and domain policy.
