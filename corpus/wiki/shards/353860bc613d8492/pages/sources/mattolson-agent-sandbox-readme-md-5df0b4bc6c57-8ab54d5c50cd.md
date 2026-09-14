---
access: public
aliases: []
claim_ids:
- clm_03225438823eef5e69f30b3c01f2c2fbb23060492ad77245413b8c472adf3ae1
- clm_0a560b0adf5f64b8fa7f459978276ca7415fcbcca71b30cf2b1be58e81cb6d56
- clm_275afd71d4edbac7a58a0f8db6ee62a59e87e9edaa35886b5a494b8d488be213
- clm_2786ce3ffa1b17d259a3d5dc05d071d03248a1ed93d392db472f0f6be19b08ec
- clm_2e1bc5035a00a1f9ecb70fd210a9289e18c4116b106277b595d3fd07e174b3d1
- clm_36f005c6ded6130d28b53f3f6d0eb21a9e46b6638b7a521185a8bc3e1a4686e7
- clm_3a29f9569888acd3850c28df21479573b2b7ec11368864de98f7a558b6578a6b
- clm_6464aeebe592d2382ed05c095ac5e8ff004b3e95e015fd0b432f6ca70cd27b94
- clm_6890487d638c6d5bb3fa7a2d580b989dad1fc18be1fd852c0bb318b7fbdfac34
- clm_71dfa3a3b7574daff7d7838f6c3dae07e1bc84195fa03c308d286d33c7eac1aa
- clm_8511be75f2532b77aeb4a306747a393e8c96f20eb0149bc7c8a6c5e153269acd
- clm_c60ce4e1fd1cad55f196bac441f567a0c61aeeff3511e228a7d61951bb86d5cd
- clm_d076ad5c93a84003623be28363429be0283c0480673f0f4e5fd908b7e702a17e
- clm_dc6b4d88debb9250845763365579b3136a18589a90db8362c81c0fa6b1abbe78
maturity: draft
page_id: pg_f356863fba4b518dac6b8ab54d5c50cd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_70d31b454b965255840004743f40f7d3
title: mattolson/agent-sandbox/README.md @ 5df0b4bc6c57
updated_at: '2026-09-14T04:08:39Z'
---

# mattolson/agent-sandbox/README.md @ 5df0b4bc6c57

<!-- rcw:begin owner=source:src_70d31b454b965255840004743f40f7d3 block=evidence -->
- Network policy is defined in project files under .agent-sandbox/policy/ with a user layer applied over the base agent policy, per-agent variants like user.agent.<agent>.policy.yaml, and hot-reload of the running proxy on saved changes. [@claim:clm_03225438823eef5e69f30b3c01f2c2fbb23060492ad77245413b8c472adf3ae1]
- Supported agents include Claude Code, Codex, Gemini, OpenCode, Pi, Factory, Copilot, and Hermes, with support tiers ranging from full support to preview to not-supported per CLI/VS Code/JetBrains surface. [@claim:clm_0a560b0adf5f64b8fa7f459978276ca7415fcbcca71b30cf2b1be58e81cb6d56]
- The proxy runs a mitmproxy addon (enforcer.py) that checks HTTPS CONNECT tunnels against the host policy and decrypted requests against scheme, method, path, and query rules, returning 403 for non-matching traffic. [@claim:clm_275afd71d4edbac7a58a0f8db6ee62a59e87e9edaa35886b5a494b8d488be213]
- The image ships an 'operating-in-agent-sandbox' skill baked in at /usr/local/share/agent-sandbox/skills/ and symlinked into agent skill-discovery directories at startup, explaining the proxy/firewall model and the read-only effective allowlist at /run/agentbox/policy.yaml. [@claim:clm_2786ce3ffa1b17d259a3d5dc05d071d03248a1ed93d392db472f0f6be19b08ec]
- Repository development practice: CONTRIBUTING.md is referenced as covering contribution paths, issue labels, planning requirements, and PR expectations; no contributor workflow details appear in the provided slices themselves. [@claim:clm_2e1bc5035a00a1f9ecb70fd210a9289e18c4116b106277b595d3fd07e174b3d1]
- The target platform is Colima plus Docker Engine on Apple Silicon, though the README says it should work with any Docker-compatible runtime; prerequisites can also be Podman, OrbStack, Docker Desktop, or Rancher Desktop. [@claim:clm_36f005c6ded6130d28b53f3f6d0eb21a9e46b6638b7a521185a8bc3e1a4686e7]
- agentbox init prompts interactively for project name, agent, mode, and IDE, then generates docker compose and network policy files under .agent-sandbox/ plus a devcontainer.json for devcontainer mode. [@claim:clm_3a29f9569888acd3850c28df21479573b2b7ec11368864de98f7a558b6578a6b]
- The project states it reduces but does not eliminate risk, describing local dev as inherently best-effort sandboxing; the network policy does not inspect request bodies or response content, so a broad token could reach any repo allowed through a permitted GitHub endpoint. [@claim:clm_6464aeebe592d2382ed05c095ac5e8ff004b3e95e015fd0b432f6ca70cd27b94]
- agentbox switch changes the active agent without reinitializing, preserving user override files and per-agent state volumes, and regenerating devcontainer.json in devcontainer projects. [@claim:clm_6890487d638c6d5bb3fa7a2d580b989dad1fc18be1fd852c0bb318b7fbdfac34]
- The default proxy policy blocks all traffic; public package registries such as PyPI are intentionally not allowed by default and must be added explicitly to user or per-agent policy. [@claim:clm_71dfa3a3b7574daff7d7838f6c3dae07e1bc84195fa03c308d286d33c7eac1aa]
- In devcontainer mode, IDE-managed features such as port forwarding, browser URL opening, and extension RPC form a separate control plane not fully removed by the container firewall; CLI mode is suggested for the tightest boundary. [@claim:clm_8511be75f2532b77aeb4a306747a393e8c96f20eb0149bc7c8a6c5e153269acd]
- The base image includes the GitHub CLI so agents can use gh api for issues and pull requests with a repo-scoped api policy surface while the token stays on the host. [@claim:clm_c60ce4e1fd1cad55f196bac441f567a0c61aeeff3511e228a7d61951bb86d5cd]
- The proxy's CA certificate is shared via a Docker volume and installed into the agent's system trust store at startup so HTTPS inspection works. [@claim:clm_d076ad5c93a84003623be28363429be0283c0480673f0f4e5fd908b7e702a17e]
- The sandbox restricts filesystem access to the repository directory, enforces egress via a sidecar proxy, and uses an iptables firewall so all outbound traffic must pass through the proxy. [@claim:clm_dc6b4d88debb9250845763365579b3136a18589a90db8362c81c0fa6b1abbe78]
<!-- rcw:end owner=source:src_70d31b454b965255840004743f40f7d3 block=evidence -->

## Researcher notes

