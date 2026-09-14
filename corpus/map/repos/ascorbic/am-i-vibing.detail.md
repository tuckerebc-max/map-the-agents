# ascorbic/am-i-vibing -- full detail

[Back to orientation](am-i-vibing.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ascorbic/am-i-vibing/39a2d1383d337a0d79c75bb002c5ac559146e88d/317225db7798894d.json](../../../wiki/dossiers/ascorbic/am-i-vibing/39a2d1383d337a0d79c75bb002c5ac559146e88d/317225db7798894d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: the repo is a pnpm-workspace TypeScript monorepo; contributors build, test, and type-check via root or per-package pnpm run build/test/check commands. -- evidence: [CLAUDE.md#L27-L27](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L27-L27), [CLAUDE.md#L30-L30](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L30-L30), [CLAUDE.md#L33-L33](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L33-L33), [CLAUDE.md#L25-L25](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L25-L25), [CLAUDE.md#L36-L36](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L36-L36), [CLAUDE.md#L13-L19](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L13-L19), [CLAUDE.md#L68-L69](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L68-L69), [CLAUDE.md#L7-L7](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L7-L7) (`clm_36b375801174fe0e7cc8832cfec681a3d496ff4c1c8882b364e3a80e0003e6cc`)
- [observation/documented] Repository development practice: releases use Changesets — contributors run pnpm changeset, and CI opens a release PR whose merge publishes to npm; three GitHub Actions workflows cover test, release, and semantic PR titles. -- evidence: [CLAUDE.md#L213-L215](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L213-L215), [CLAUDE.md#L197-L201](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L197-L201), [CLAUDE.md#L195-L195](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L195-L195), [CLAUDE.md#L211-L211](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L211-L211) (`clm_8442c1c187e40ef5a71c14db1893b90fa7ef4d6733b73a42ba704df5e8d81e6e`)
- [observation/documented] Repository development practice: new providers must use verified environment variables (not guessed ones), follow a detection-method priority order, and pass a checklist including unit tests, real-environment and false-positive testing, and a changeset. -- evidence: [CONTRIBUTING.md#L209-L213](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L209-L213), [CONTRIBUTING.md#L11-L13](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L11-L13), [CONTRIBUTING.md#L17-L17](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L17-L17), [CONTRIBUTING.md#L217-L222](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L217-L222) (`clm_a300f5fd1363645572eea38b580d4b0bd9250988789b7871958eb2084425f620`)
- [observation/documented] Repository development practice: provider unit tests go in test/detector.test.ts using a mock environment passed to detectAgenticEnvironment, and the CLI can be exercised with pnpm run cli (optionally --debug). -- evidence: [CONTRIBUTING.md#L187-L187](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L187-L187), [CONTRIBUTING.md#L200-L203](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L200-L203), [CONTRIBUTING.md#L189-L196](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L189-L196), [CONTRIBUTING.md#L205-L205](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CONTRIBUTING.md#L205-L205) (`clm_e945837735089e88937ef932609953ab14369972fbc0007997233238b0602dc1`)
- [observation/documented] Repository development practice: the package version is documented as v0.0.2 and published to npm; the root README is a symlink to the package README. -- evidence: [CLAUDE.md#L257-L257](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L257-L257), [CLAUDE.md#L219-L219](https://github.com/ascorbic/am-i-vibing/blob/39a2d1383d337a0d79c75bb002c5ac559146e88d/CLAUDE.md#L219-L219) (`clm_5ebfd51fbf6d2f49366c9852d8b1e6c6b47e9a1f6ed5a8a6012ed320d7ce7e52`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

