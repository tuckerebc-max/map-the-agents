# mindwalk — impeccable

## Design Context

### Users
Engineers studying agent behavior (the primary user is the author). Scenario: replaying
Claude Code sessions locally, watching the model's view of the repository and its traversal
paths; long stretches of focused analysis, with occasional screenshots/recordings dropped
into blog posts and research reports. Information density and readout efficiency come
first, but every frame must hold up as a screenshot.

### Brand Personality
Quiet, precise, with the poetry of night. Three words: **observatory / patient / luminous**.
Emotional target: reading a star chart in an observatory late at night — focused, calm,
occasionally struck by a single trajectory.

### Aesthetic Direction
**Nocturnal Observatory.** The project brief's candidate names were lantern / firefly,
and the interaction vocabulary is all "glow / light up / highlight" — this is a product
about light, so the ground must be night.

- Deep ink-blue night sky (not pure black); the repository is deterministic structure in
  the dark; wherever the model reaches, a light comes on.
- The main view is the **firefly tree** (a radial deterministic tree: directories as
  branches, files as leaves, fireflies as the protagonists, attention depth = ground-glow
  radius); **attention terrain** (mountain ridges rising from a treemap plain) is the
  alternate view. Both share one light spectrum and one playback semantics.
- Spectrum by touch level: search = phosphorescent moss-green shimmer, read = moonlight
  white, edit = warm sodium-lamp amber; trails are firefly-warm light lines.
  **Glow = data; decoration never glows.**
- The UI is a matte instrument panel (slate texture, hairline rules, small uppercase
  eyebrows), not a glassmorphic floating window.
- Anti-list: neon cyan-purple gradients, cyberpunk, glassmorphism, glowing border
  decoration, pure-black backgrounds.

### Type
- The Latin display layer uses a characterful serif/semi-serif (self-hosted, bundled with
  dist); body text uses a humanist sans.
- CJK fallback is PingFang SC / Noto Sans SC; session titles are often Chinese, and mixed
  CJK/Latin setting must be refined: tabular-nums for figures and units, breathing room
  between CJK and Latin runs.

### Design Principles
1. **Light is data** — brightness and hue encode touch state only; anything that glows
   means the model has been there.
2. **Instrument first, picture always** — readout density is never compromised, yet a
   screenshot at any moment is an image worth publishing.
3. **Night, not cyber** — light sources are warm (sodium lamp, moonlight, phosphorescence),
   not neon; the night sky is ink blue, not pure black.
4. **CJK and Latin as equals** — the font stack and size rhythm are tuned for mixed
   CJK/Latin text; Chinese must never fall into a bad fallback font.
5. **Restrained motion** — motion only at state changes, exponential ease-out; full
   prefers-reduced-motion support, and playback advancement offers an animation-free
   degradation.
