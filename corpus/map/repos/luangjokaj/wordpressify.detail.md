# luangjokaj/wordpressify -- full detail

[Back to orientation](wordpressify.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/luangjokaj/wordpressify/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/b1048ee00b385110.json](../../../wiki/dossiers/luangjokaj/wordpressify/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/b1048ee00b385110.json)

## specifications (1 claim(s))

- [observation/documented] WordPressify is described as a tool to automate the WordPress development workflow. -- evidence: [README.md#L5-L5](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/README.md#L5-L5) (`clm_fdd54be33397d39f9f5f7e7793179e31f65050127901c8d8b2c177bf84871fc7`)

## components (1 claim(s))

- [observation/documented] The default theme was rewritten as a modern block-based theme using HTML markup instead of PHP templates (v0.5.0). -- evidence: [CHANGELOG.md#L49-L55](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L49-L55) (`clm_86a965440a8e19cc0b591a9ac34c05b6d625821e65174176018259cb68f1c3cd`)

## design-choices (1 claim(s))

- [observation/documented] v0.6.0 replaced chalk and prompts with native ANSI codes and Node's readline, cutting installer dependencies from over 100 to 18 packages. -- evidence: [CHANGELOG.md#L31-L43](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L31-L43) (`clm_bc69155ee6e94bd774b0d13ecdc7d014dfd111f75b6824d4c3ed6f0c05e321d5`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: CLAUDE.md provides guidance to Claude Code when working with code in this repository. -- evidence: [CLAUDE.md#L3-L3](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CLAUDE.md#L3-L3) (`clm_c2e57751cd7dc221d4e5e28d8dd573075ce7816badcfa382e6f0265f6f91efd5`)
- [observation/documented] Repository development practice: contributors fork and clone, install Docker and Node.js v16+, scaffold with npx wordpressify, then run npm start and npm run dev inside the container. -- evidence: [CONTRIBUTING.md#L7-L10](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CONTRIBUTING.md#L7-L10) (`clm_aa69fab023b00fe1fc16699406b6bbda68b49a6236ba3f46e804c793ea1e0e5c`)
- [observation/documented] Repository development practice: the contributor workflow uses five Docker services (MariaDB, WordPress PHP-FPM, nginx, a permissions helper, and a Node.js Gulp/BrowserSync container), with BrowserSync on port 3010 and nginx on 8080. -- evidence: [CONTRIBUTING.md#L27-L27](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CONTRIBUTING.md#L27-L27), [CONTRIBUTING.md#L14-L14](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CONTRIBUTING.md#L14-L14) (`clm_82b9a4ed64cfa801ee88f3d209bc71f59aa7881137edc48bb95caef41e70b570`)
- [observation/documented] Repository development practice: the documented build pipeline compiles CSS via PostCSS, transpiles JS via Babel, copies theme files, and outputs a distributable theme zip under dist/. -- evidence: [CLAUDE.md#L52-L52](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CLAUDE.md#L52-L52), [CLAUDE.md#L45-L50](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CLAUDE.md#L45-L50) (`clm_28d08999a45dc91800411134014c6ecc02cae2ea660ad7769bc5ba726e3cd488`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] v0.4.0 replaced older npm tasks with commands such as npm run start, npm run export, npm run export:backup, npm run lintcss, and docker compose equivalents. -- evidence: [CHANGELOG.md#L61-L69](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L61-L69) (`clm_81d60215c751a5fef171b8b929b7218da4077ffcbbfe379ce31173947c70359a`)
- [observation/documented] The v0.6.3 installer adds an update subcommand that upgrades existing projects without overwriting theme source files. -- evidence: [CHANGELOG.md#L5-L12](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L5-L12) (`clm_9327d227a8f18ce7996c9f88a6b6adda6004d11dfe17a73662a2d3a093a5ffa0`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Export and export:backup scripts auto-stop Docker containers when the stack was not already running, and a healthcheck was added to the WordPress service to fix a chmod race condition. -- evidence: [CHANGELOG.md#L31-L43](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L31-L43) (`clm_54cad9df560a82e52ec55eda90207e0f3230d8b55e174cf543457812dd19a6bd`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project requires Docker and is stated to be compatible with macOS, Windows, and Linux. -- evidence: [README.md#L7-L8](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/README.md#L7-L8) (`clm_c2a5430b4bbede37b88bd8631f501cf12c3f44798c53df5ec78a55c9b78aa4bf`)
- [observation/documented] Since v0.4.0, NodeJS is no longer a global dependency; Docker is the only main dependency, enabling cross-platform runs. -- evidence: [CHANGELOG.md#L59-L59](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L59-L59) (`clm_398dbdeb907696681c5fe42f9a941d2b7e79942a8736bffcba7e59f6936e60b4`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

