# ducksss/codex-profiles -- full detail

[Back to orientation](codex-profiles.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ducksss/codex-profiles/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/07c8aeb13ebe19ba.json](../../../wiki/dossiers/ducksss/codex-profiles/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/07c8aeb13ebe19ba.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] launcher create builds a small unsigned macOS app in ~/Applications (overridable via CODEX_PROFILE_LAUNCHER_ROOT) that calls codex-profile app <profile>, with named/color-coded identities and list/path/remove subcommands. -- evidence: [docs/llms.txt#L221-L223](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L221-L223), [docs/llms.txt#L214-L219](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L214-L219), [docs/llms.txt#L208-L212](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L208-L212) (`clm_8280cb2416789a2dcb3962829abfd0f3c4c68e7cdb5a009e79afd8b4fcb28712`)

## design-choices (3 claim(s))

- [observation/documented] Profile selection maps the name 'default' to ~/.codex and any other name <x> to ~/.codex-<x>, so each profile gets its own Codex home. -- evidence: [docs/llms.txt#L8-L118](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L8-L118), [README.md#L170-L174](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L170-L174) (`clm_927d02ad5a8e4edc5170e94819acfe5bc9dcdfaa5923881bd104e9b9c758cde6`)
- [observation/documented] init --share-with links only a fixed allowlist of configuration entries (config.toml, AGENTS.md, instructions.md, rules/, plugins/, etc.) while auth.json, sessions, and Electron data stay per-profile; the tool never reads or copies authentication tokens or cookies. -- evidence: [README.md#L180-L184](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L180-L184), [docs/llms.txt#L249-L253](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L249-L253), [docs/llms.txt#L255-L260](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L255-L260) (`clm_e749ca8a51eaee584b966fb2e9fc4824c812e2702e70ca39e2a2f5fa0a58c146`)
- [observation/documented] A workspace guard defaults to warn mode; strict mode rejects mismatched cli, env/use, and app selections before side effects, and off disables checks. -- evidence: [docs/llms.txt#L178-L182](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L178-L182) (`clm_736af6f8f0fbb86328234119a715ed4f034224e12a0b2bf18630d677d641fee9`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are pointed to a contributor guide and coding-agent instructions; there is no build step, and the README instructs running 'make check' as the complete local gate before submitting changes. -- evidence: [README.md#L273-L275](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L273-L275), [README.md#L277-L279](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L277-L279) (`clm_a3b2f69fb1896faca299c689d3a14010d2cd3521f153ba3a3f5a9284256f90ed`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The tool exposes a CLI with commands including setup, init, login, cli, app, run, list, status, doctor, path, shell-init, workspace bind, launcher create, env, and detach. -- evidence: [README.md#L235-L245](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L235-L245), [docs/llms.txt#L142-L164](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L142-L164) (`clm_d460a1787f8ec9bce381627583d0067c1b41d34802ca86000983d00433f23bc7`)
- [observation/documented] shell-init prints shell code for bash/zsh/fish that enables 'use <profile>' in the current shell, with optional --prompt and --completions; it never edits shell startup files. -- evidence: [USAGE.md#L47-L48](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/USAGE.md#L47-L48), [docs/llms.txt#L227-L245](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L227-L245) (`clm_0f0a755eeb5c2d671f665b20821b2f7e79f5893373d55de6ae4a30ec4efca252`)
- [observation/documented] Interactive no-argument cli/app launches show a numbered picker where Enter prefers the workspace-bound profile, exact names take precedence over menu numbers, and scripts must pass an explicit profile name. -- evidence: [agent.md#L139-L150](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/agent.md#L139-L150), [USAGE.md#L65-L74](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/USAGE.md#L65-L74) (`clm_3401761316b9a45318d1445a3ed4e155a1aaf428ae431b97b4db090a87603af6`)

## memory-state (1 claim(s))

- [observation/documented] Workspace bindings store only a canonical path and profile name under ${XDG_CONFIG_HOME:-~/.config}/codex-profile with private permissions, relocatable via CODEX_PROFILE_CONFIG_HOME; nested bindings override ancestors. -- evidence: [docs/llms.txt#L171-L176](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L171-L176) (`clm_c9215aa4dc531c6a0aac96aae0e6fa696f64252bf080a8f03be13cd9e28e7f89`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool is described as a single Bash script with no runtime dependencies beyond standard system tools; it requires Bash and a working upstream Codex CLI, and does not install Codex itself. -- evidence: [agent.md#L66-L70](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/agent.md#L66-L70), [agent.md#L13-L16](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/agent.md#L13-L16), [README.md#L34-L35](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L34-L35) (`clm_6cc76ea236a81e7f87a9c7b02224983ae390c13acb0fe94cc105f26ff30a41b8`)

## limitations (3 claim(s))

- [observation/documented] The project states local-state separation is not an account, OS, or server-side security boundary; OS credentials, network, keychain, and other tool credentials remain shared or outside its control. -- evidence: [README.md#L180-L184](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L180-L184), [docs/llms.txt#L291-L296](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L291-L296) (`clm_1d3d37944a9a4dad2d2ca9f3a88528ce45f18beff46a40e384be9a2e376b6f28`)
- [observation/documented] CLI commands work on macOS and Linux, but the app and launcher create commands require macOS. -- evidence: [README.md#L254-L256](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L254-L256) (`clm_92a19bdf503e03dbdf0e66439ea4297bbe355af6a01e23c30d4481cfd8da3a77`)
- [observation/documented] The tool does not verify that CLI and Desktop sign-ins use the same account, and does not change or inspect server-side ChatGPT workspaces, policies, histories, or plans. -- evidence: [README.md#L147-L150](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L147-L150), [docs/llms.txt#L203-L204](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L203-L204) (`clm_47b39d0ba69be4f8423713ecdc48992e04c1bd68d5e3534109889f194ca1d7a9`)

## relevance (1 claim(s))

- [observation/documented] The project recommends itself for people using multiple Codex contexts who want separate Codex homes or named ChatGPT windows with separate local state on macOS, without copying authentication files. -- evidence: [docs/llms.txt#L303-L305](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L303-L305) (`clm_5cae3c65513751e7ecb2aac094d699c95a7da37e5cc5227c18ced9c46871fa06`)

