# Tab Design

## Goal

- Treat the border as a single 1px medium-gray stroke that travels left to right.
- When the stroke reaches a tab, it follows the tab contour: up, over, and down.
- Active tab: no bottom segment, so the tab is visually open to the pane area.
- Inactive tab: include a bottom segment while the top segment exists, so the stroke forks around the tab and rejoins.
- Keep the 3px white/black strip above pane titles unchanged.

## Reference Diagram

```text
          ┌──────────┐   ┌────────────┐
          │  ACTIVE  │   │  INACTIVE  │
──────────┘          └───┴────────────┴──────────
```
