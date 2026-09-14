# mattolson/agent-sandbox -- full detail

[Back to orientation](agent-sandbox.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mattolson/agent-sandbox/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/4c77988393ee6d90.json](../../../wiki/dossiers/mattolson/agent-sandbox/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/4c77988393ee6d90.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The base image includes the GitHub CLI so agents can use gh api for issues and pull requests with a repo-scoped api policy surface while the token stays on the host. -- evidence: [README.md#L183-L183](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L183-L183) (`clm_c60ce4e1fd1cad55f196bac441f567a0c61aeeff3511e228a7d61951bb86d5cd`)
- [observation/documented] Supported agents include Claude Code, Codex, Gemini, OpenCode, Pi, Factory, Copilot, and Hermes, with support tiers ranging from full support to preview to not-supported per CLI/VS Code/JetBrains surface. -- evidence: [README.md#L38-L45](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L38-L45), [README.md#L27-L36](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L27-L36) (`clm_0a560b0adf5f64b8fa7f459978276ca7415fcbcca71b30cf2b1be58e81cb6d56`)

## design-choices (5 claim(s))

- [observation/documented] The sandbox restricts filesystem access to the repository directory, enforces egress via a sidecar proxy, and uses an iptables firewall so all outbound traffic must pass through the proxy. -- evidence: [README.md#L8-L15](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L8-L15), [README.md#L163-L164](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L163-L164) (`clm_dc6b4d88debb9250845763365579b3136a18589a90db8362c81c0fa6b1abbe78`)
- [observation/documented] The proxy runs a mitmproxy addon (enforcer.py) that checks HTTPS CONNECT tunnels against the host policy and decrypted requests against scheme, method, path, and query rules, returning 403 for non-matching traffic. -- evidence: [README.md#L170-L170](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L170-L170) (`clm_275afd71d4edbac7a58a0f8db6ee62a59e87e9edaa35886b5a494b8d488be213`)
- [observation/documented] The proxy's CA certificate is shared via a Docker volume and installed into the agent's system trust store at startup so HTTPS inspection works. -- evidence: [README.md#L174-L174](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L174-L174) (`clm_d076ad5c93a84003623be28363429be0283c0480673f0f4e5fd908b7e702a17e`)
- [observation/documented] The default proxy policy blocks all traffic; public package registries such as PyPI are intentionally not allowed by default and must be added explicitly to user or per-agent policy. -- evidence: [README.md#L166-L166](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L166-L166), [README.md#L215-L216](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L215-L216) (`clm_71dfa3a3b7574daff7d7838f6c3dae07e1bc84195fa03c308d286d33c7eac1aa`)
- [observation/documented] SSH port 22 is blocked to prevent proxy-bypassing tunnels, and the container's system git config rewrites SSH GitHub URLs to HTTPS; the image ships Git 2.50.1 with worktree.useRelativePaths=true. -- evidence: [docs/git.md#L15-L16](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/git.md#L15-L16), [docs/git.md#L39-L39](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/git.md#L39-L39), [docs/git.md#L35-L37](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/git.md#L35-L37), [docs/git.md#L33-L33](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/git.md#L33-L33) (`clm_627a2a8ef85d6de427eeba0cb35bf6e2164fc753a18c3b43b02b00e481c57cc3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: CONTRIBUTING.md is referenced as covering contribution paths, issue labels, planning requirements, and PR expectations; no contributor workflow details appear in the provided slices themselves. -- evidence: [README.md#L345-L345](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L345-L345) (`clm_2e1bc5035a00a1f9ecb70fd210a9289e18c4116b106277b595d3fd07e174b3d1`)

## skills-patterns (1 claim(s))

- [observation/documented] The image ships an 'operating-in-agent-sandbox' skill baked in at /usr/local/share/agent-sandbox/skills/ and symlinked into agent skill-discovery directories at startup, explaining the proxy/firewall model and the read-only effective allowlist at /run/agentbox/policy.yaml. -- evidence: [README.md#L181-L181](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L181-L181), [README.md#L185-L185](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L185-L185) (`clm_2786ce3ffa1b17d259a3d5dc05d071d03248a1ed93d392db472f0f6be19b08ec`)

## interfaces (3 claim(s))

- [observation/documented] agentbox init prompts interactively for project name, agent, mode, and IDE, then generates docker compose and network policy files under .agent-sandbox/ plus a devcontainer.json for devcontainer mode. -- evidence: [docs/cli.md#L43-L44](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/cli.md#L43-L44), [README.md#L97-L97](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L97-L97) (`clm_3a29f9569888acd3850c28df21479573b2b7ec11368864de98f7a558b6578a6b`)
- [observation/documented] Network policy is defined in project files under .agent-sandbox/policy/ with a user layer applied over the base agent policy, per-agent variants like user.agent.<agent>.policy.yaml, and hot-reload of the running proxy on saved changes. -- evidence: [README.md#L259-L259](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L259-L259), [README.md#L197-L197](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L197-L197), [README.md#L189-L189](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L189-L189) (`clm_03225438823eef5e69f30b3c01f2c2fbb23060492ad77245413b8c472adf3ae1`)
- [observation/documented] agentbox switch changes the active agent without reinitializing, preserving user override files and per-agent state volumes, and regenerating devcontainer.json in devcontainer projects. -- evidence: [README.md#L157-L157](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L157-L157), [docs/cli.md#L70-L75](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/cli.md#L70-L75), [README.md#L151-L151](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L151-L151) (`clm_6890487d638c6d5bb3fa7a2d580b989dad1fc18be1fd852c0bb318b7fbdfac34`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The target platform is Colima plus Docker Engine on Apple Silicon, though the README says it should work with any Docker-compatible runtime; prerequisites can also be Podman, OrbStack, Docker Desktop, or Rancher Desktop. -- evidence: [README.md#L17-L17](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L17-L17), [README.md#L53-L57](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L53-L57) (`clm_36f005c6ded6130d28b53f3f6d0eb21a9e46b6638b7a521185a8bc3e1a4686e7`)
- [inference/documented] The agentbox CLI appears to be written in Go, per the CLI reference's description of the tool. -- evidence: [docs/cli.md#L3-L3](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/docs/cli.md#L3-L3) (`clm_1aaf239871483e32b6de25808c7fb28e166782c6304efe89c385c40b9ac0eb56`)

## limitations (2 claim(s))

- [observation/documented] The project states it reduces but does not eliminate risk, describing local dev as inherently best-effort sandboxing; the network policy does not inspect request bodies or response content, so a broad token could reach any repo allowed through a permitted GitHub endpoint. -- evidence: [README.md#L298-L298](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L298-L298), [README.md#L309-L309](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L309-L309) (`clm_6464aeebe592d2382ed05c095ac5e8ff004b3e95e015fd0b432f6ca70cd27b94`)
- [observation/documented] In devcontainer mode, IDE-managed features such as port forwarding, browser URL opening, and extension RPC form a separate control plane not fully removed by the container firewall; CLI mode is suggested for the tightest boundary. -- evidence: [README.md#L329-L329](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L329-L329), [README.md#L320-L320](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L320-L320), [README.md#L324-L327](https://github.com/mattolson/agent-sandbox/blob/5df0b4bc6c57293284fdd8bdc2cb905ef6152175/README.md#L324-L327) (`clm_8511be75f2532b77aeb4a306747a393e8c96f20eb0149bc7c8a6c5e153269acd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

