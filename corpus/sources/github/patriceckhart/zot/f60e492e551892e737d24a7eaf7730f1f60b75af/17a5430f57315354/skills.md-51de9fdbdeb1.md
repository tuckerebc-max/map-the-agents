# zot skills

A skill is a reusable instruction set written as a single
`SKILL.md` file with a YAML frontmatter header. Skills may be supplied by
an extension as well as by the normal skill directories. Unless a skill disables
model invocation, zot discovers it at startup and surfaces it to the model
in two ways:

1. The system prompt gains a short manifest:
   `Available skills: ... - code-review — Run a self-review pass...`
2. A built-in `skill` tool lets the model load any one skill's full
   body on demand.

The on-demand-load model keeps token usage cheap: only the manifest
goes into every request; the body is fetched as a tool result the
one or two turns the model actually needs it.

## Anatomy

```markdown
---
name: code-review
description: Run a thorough self-review pass on a recent change.
allowed-tools: [read, bash]
permissions:
  bash: ["git diff*", "git log*"]
---

# Code review

When asked to review code, ...
```

### Frontmatter fields

| field | required | purpose |
|---|---|---|
| `name` | optional | skill identifier; defaults to the normalized relative directory path |
| `description` | required | one-line summary shown in the system prompt |
| `disable-model-invocation` | optional | when `true`, hide the skill from the model's startup manifest; invoke it explicitly with `/skill:<name>` |
| `allowed-tools` | optional | list of tool names the skill is meant to use; informational |
| `permissions` | optional | per-tool patterns; informational |

`allowed-tools` and `permissions` are **parsed but not enforced** in
this version. They appear in the rendered skill body so the model can
see them and self-regulate. Future versions may enforce.

The body (everything after the second `---`) is plain markdown.
There's no template engine; the model sees what you write.

## Discovery

zot recursively looks in these directories, in priority order, and registers the
first `SKILL.md` it finds for each unique name:

| location | scope |
|---|---|
| `./.zot/skills/<name>/SKILL.md` | project (native) |
| `$ZOT_HOME/skills/<name>/SKILL.md` | global (native) |
| `./.claude/skills/<name>/SKILL.md` | project (claude-compat) |
| `~/.claude/skills/<name>/SKILL.md` | global (claude-compat) |
| `./.agents/skills/<name>/SKILL.md` | project (agent-compat) |
| `~/.agents/skills/<name>/SKILL.md` | global (agent-compat) |

The compat paths are deliberate: a `SKILL.md` written for an existing
skill ecosystem works in zot unchanged. Drop your existing
`.claude/skills/` or `.agents/skills/` directories into a project and
zot will pick them up. When no frontmatter `name` is present, nested path
components are lowercased and normalized to kebab-case and joined with `-`.
Only files named exactly `SKILL.md` are read.

Extensions namespace their skills, for example `git-tools:writing-git-commits`.
Explicit `--ext` bundles take precedence over environment, project, global, and
compatibility sources. Duplicate names keep the higher-precedence file and
report a diagnostic. `--no-ext` omits implicit extension bundles;
`--no-ext --ext PATH` loads only the explicitly named bundle. `--no-skill`
disables all skills, including extension and built-in skills.

When `XDG_STATE_HOME` is set on any platform, `$ZOT_HOME` defaults to
`$XDG_STATE_HOME/zot`. Otherwise it defaults to `~/Library/Application Support/zot/`
on macOS, `~/.local/state/zot` on Linux, or `%LOCALAPPDATA%\zot` on Windows.

## Inspecting installed skills

In zot, run `/skills`. A picker lists every discovered skill with its
description and source path. Press enter on a row to view the full
body inline. Press esc to go back.

## Invoking skills

For normal skills, the system prompt tells the model the skill names and
short descriptions. When a request matches, the model calls the `skill` tool
to load the full instructions on demand.

To force a specific skill, invoke it as a slash command. Typing `/skill:` opens a filtered list of discovered user skills. Use the arrow keys to select one, `tab` to complete its name, or `enter` to invoke the highlighted skill.

```text
/skill:code-review
/skill:code-review focus on security issues
```

By default, suggestions match case-insensitive name prefixes and are sorted
alphabetically. Enable **fuzzy skill suggestions** in `/settings` to match
characters in order anywhere in a skill name: `/skill:review` and `/skill:crv`
can both find `code-review`. Results are ranked by relevance, with alphabetical
tie-breaking, and matching characters are shown in bold, including in the
selected row. Only names are searched, not descriptions or the `/skill:` prefix.
An empty query still lists skills alphabetically; an exact name shows only that
skill. Other slash-command suggestions and exact skill lookup during invocation
are unchanged. Complete a fuzzy query before adding request text.

The setting takes effect immediately and persists as `fuzzy_skill_suggest` in
`$ZOT_HOME/config.json`. Missing or `false` preserves the default prefix behavior.
You can turn it off at any time. Bold emphasis depends on terminal support.

zot expands the command into a user message containing the complete skill
body, its directory for resolving relative references, and any text following
the command as the request. This bypasses model-side skill selection.

Set `disable-model-invocation: true` in a skill's frontmatter when it should
only run after explicit user invocation. The skill remains visible in
`/skills` and available through `/skill:<name>`, but its name and description
are omitted from the model's startup context.

## Writing good skills

- **Be procedural.** Number steps. Tell the model what to do in what
  order. Skills are habits, not knowledge dumps.
- **Be precise about boundaries.** "Stop after step 4" is more
  effective than "don't go too far".
- **Trim aggressively.** A 200-line skill bloats every turn the
  model uses it. Aim for 20–80 lines.
- **One skill per behaviour.** Don't pack three workflows into one
  SKILL.md; the model picks one path. Two separate skills work better.
- **Lead with the trigger.** First paragraph should make it
  obvious *when* to use the skill so the model self-selects correctly.

## Examples

See `examples/skills/` for starter skills:

- `code-review/` — self-review pass on a recent diff
- `test-fix/` — diagnose + minimally fix a failing test
- `recursive/` — nested path-derived naming and explicit-name discovery

## Comparison to other discovery layouts

| ecosystem | path | zot reads it? |
|---|---|---|
| (native) | `.zot/skills/<name>/SKILL.md` | yes |
| (claude-style) | `.claude/skills/<name>/SKILL.md` | yes |
| (agent-style) | `.agents/skills/<name>/SKILL.md` | yes |

Cross-pollination is intentional: pick whichever convention you're
already using and zot tags along.
