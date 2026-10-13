# Skill Packs

Skill packs package reusable prompts, checklists, command templates, recommended tools, and compatible modes. Legacy workspace skills under `.sharpclaw/skills` are still supported; skill packs live under `.sharpclaw/skillpacks`.

## Manifest

`skillpack.json`:

```json
{
  "id": "pr-review",
  "name": "PR Review",
  "version": "1.0.0",
  "description": "Reviews diffs for correctness, tests, security, and maintainability.",
  "author": "team",
  "tags": ["review"],
  "commands": [
    {
      "name": "run",
      "description": "Run the review",
      "promptTemplate": "Review this diff: {{arguments}}"
    }
  ],
  "prompts": [],
  "checklists": [],
  "recommendedTools": [],
  "requiredPermissions": ["toolExecution"],
  "compatibleModes": ["plan", "build"],
  "entryPointPrompt": "Review this diff: {{arguments}}"
}
```

## Use

```bash
sharpclaw skills list
sharpclaw skills show --id pr-review
sharpclaw skills install --path ./skillpack.json
sharpclaw skills enable --id pr-review
sharpclaw skills disable --id pr-review
sharpclaw skills run --id pr-review --args "main...feature"
```

Built-in packs include PR Review, Architecture Review, Release Notes, EFH Recovery, and Figma Handoff.
