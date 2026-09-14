# agentsmd/agents.md -- full detail

[Back to orientation](agents.md.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agentsmd/agents.md/d001185d792eb6402a58e4cbef1c228b309ec25d/dc191f78ddacbe4c.json](../../../wiki/dossiers/agentsmd/agents.md/d001185d792eb6402a58e4cbef1c228b309ec25d/dc191f78ddacbe4c.json)

## specifications (1 claim(s))

- [observation/documented] AGENTS.md is described as a simple, open format for guiding coding agents, acting as a dedicated, predictable place to give AI agents context and instructions about a project. -- evidence: [README.md#L7-L8](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L7-L8), [README.md#L5-L5](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L5-L5) (`clm_34caa9bd0b96037098067c0ba8ff6edc5956e3ece8d6eb12c2350d1a52e5a45e`)

## components (1 claim(s))

- [observation/documented] The repository includes a basic Next.js website hosted at agents.md that explains the project's goals and features examples. -- evidence: [README.md#L37-L38](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L37-L38) (`clm_4a9e3bbe1594bff4f40844302bf23ab69e1589a663b32b947bcb9912a4b61fe9`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (7 claim(s))

- [observation/documented] Repository development practice: contributors are told to use the dev server (npm/pnpm/yarn run dev) and never run the production build inside an agent session, since it disables hot reload and can leave the dev server inconsistent. -- evidence: [AGENTS.md#L10-L15](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L10-L15) (`clm_ba16adfc89c4da687f508b447d50949b9d96f4cc2da11559c22e69b4827c2d98`)
- [observation/documented] Repository development practice: when adding or updating dependencies, update the relevant lockfile and restart the dev server so Next.js picks up the changes. -- evidence: [AGENTS.md#L19-L19](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L19-L19), [AGENTS.md#L21-L22](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L21-L22) (`clm_07941e7283cc5537c6664a9cbdb6684e709b6e6aca73079c00798d04cbb1765c`)
- [observation/documented] Repository development practice: new components and utilities should preferably be TypeScript (.ts/.tsx), with component-specific styles co-located in the component's folder. -- evidence: [AGENTS.md#L26-L28](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L26-L28) (`clm_cb56b6111324b0ad739d38686ac925308a7137bf519cc73c8616df03a045bd49`)
- [observation/documented] Repository development practice: a commands recap lists npm run dev, lint, test, and build, marking the production build as not to be run during agent sessions. -- evidence: [AGENTS.md#L32-L37](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/AGENTS.md#L32-L37) (`clm_f2ec269f2e3f2ff7c61c91bd871c5a30fc0efc097aabfd62e96531345f02a6be`)
- [observation/documented] Repository development practice: the README's embedded example AGENTS.md instructs running pnpm turbo run test per package, keeping the suite green before merging, and adding or updating tests for changed code. -- evidence: [README.md#L22-L28](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L22-L28) (`clm_9e621fd0bc4c175efd99f9ea05e719fb9af0fa9352787ffd444ddb15ee8664c8`)
- [observation/documented] Repository development practice: PR titles should follow the format [<project_name>] <Title>, and lint plus test should be run before committing. -- evidence: [README.md#L31-L33](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L31-L33) (`clm_26c6503b856e36742950e08568f9c4577955b2f4e801e564474b24312e854857`)
- [observation/documented] Repository development practice: local development is via pnpm install, pnpm run dev, then opening http://localhost:3000; turbo's 'where' command is suggested for locating packages in the monorepo. -- evidence: [README.md#L41-L49](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L41-L49), [README.md#L16-L19](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L16-L19) (`clm_1a61c6bf3affbd5ee427a29d6cef0746730cbe461d9726d985795a571a870a23`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The format is realized as a markdown file (a minimal example is shown in the README), analogous to a README but aimed at agents. -- evidence: [README.md#L10-L10](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L10-L10), [README.md#L7-L8](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L7-L8), [README.md#L12-L12](https://github.com/agentsmd/agents.md/blob/d001185d792eb6402a58e4cbef1c228b309ec25d/README.md#L12-L12) (`clm_eccb391f3545248fdf24cf2348ab1b8e3e621da9bf27005a39c3fc2c2dc412cb`)

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

