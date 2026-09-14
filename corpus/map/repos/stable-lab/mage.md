# stable-lab/mage

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 90c96366c518 @ 7fa8bb76886bbe31

## Summary (orientation draft, not independently verified)

The snapshot consists of README.md content describing MAGE, an open-source multi-agent LLM RTL code generator, its tool dependencies (Icarus Verilog 12, Verilator, Pyverilog), verilog-eval benchmarks, and run configuration via tests/test_top_agent.py.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] MAGE is described as an open-source multi-agent LLM RTL code generator, with an associated arXiv paper (2412.07822). -- evidence: [README.md#L3-L4](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L3-L4)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Users are told to verify the installed iverilog version is v12 by running 'iverilog -v' and checking the first output line. -- evidence: [README.md#L67-L70](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L67-L70), [README.md#L62-L65](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L62-L65)
  - [observation/documented] API keys for OpenAI, Anthropic, or Vertex can be supplied via environment variables or a key.cfg file with a documented format. -- evidence: [README.md#L30-L32](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L30-L32), [README.md#L34-L39](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L34-L39)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Runs are launched with 'python tests/test_top_agent.py' and configured via an args_dict with provider, model, filter_instance regex, benchmark type/path, run_identifier, n, temperature, top_p, max_token, and key_cfg_path. -- evidence: [README.md#L114-L114](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L114-L114), [README.md#L116-L146](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L116-L146), [README.md#L110-L112](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L110-L112)
  - [observation/documented] The run configuration supports verilog_eval_v1 and verilog_eval_v2 benchmark types, and gpt-4o and Claude models are documented as verified. -- evidence: [README.md#L116-L146](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L116-L146)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The run harness executes the agent against verilog-eval benchmark instances selectable by regex filter, with repeated runs (n) and sampling parameters such as temperature 0.85 and top_p 0.95. -- evidence: [README.md#L116-L146](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L116-L146)
- dependencies (4 claim(s)):
  - [observation/documented] The README instructs installing Icarus Verilog 12.0, with an Ubuntu source build of the v12 branch and a macOS Homebrew option. -- evidence: [README.md#L57-L59](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L57-L59), [README.md#L46-L55](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L46-L55), [README.md#L42-L43](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L42-L43)
  - [observation/documented] The README gives Verilator installation instructions via apt or by compiling from the verilator GitHub repository. -- evidence: [README.md#L74-L74](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L74-L74), [README.md#L76-L76](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L76-L76), [README.md#L79-L85](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L79-L85)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](mage.detail.md) for every claim.)

Metadata and full claim list: [full detail](mage.detail.md)
Human notes ([notes](mage.notes.md), never overwritten by build)

[Back to map index](../../index.md)
