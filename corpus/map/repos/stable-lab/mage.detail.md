# stable-lab/mage -- full detail

[Back to orientation](mage.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stable-lab/mage/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/7fa8bb76886bbe31.json](../../../wiki/dossiers/stable-lab/mage/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/7fa8bb76886bbe31.json)

## specifications (1 claim(s))

- [observation/documented] MAGE is described as an open-source multi-agent LLM RTL code generator, with an associated arXiv paper (2412.07822). -- evidence: [README.md#L3-L4](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L3-L4) (`clm_d28aa5a095152ae0017756a5c42ba441a714a5818f34101a893c853707fc0ff9`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Users are told to verify the installed iverilog version is v12 by running 'iverilog -v' and checking the first output line. -- evidence: [README.md#L67-L70](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L67-L70), [README.md#L62-L65](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L62-L65) (`clm_466d6d1d257d1549b46401599bbc667df42810dd0b30877d7011c4c9052e7f85`)
- [observation/documented] API keys for OpenAI, Anthropic, or Vertex can be supplied via environment variables or a key.cfg file with a documented format. -- evidence: [README.md#L30-L32](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L30-L32), [README.md#L34-L39](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L34-L39) (`clm_ff84c999d2f78db99f83de88505fc7ad74b8f201c0c252c8fbe1ea94a283220e`)
- [observation/documented] Installation uses a conda environment with Python 3.11 followed by 'pip install .', and cloning may use --recursive to fetch submodules. -- evidence: [README.md#L11-L12](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L11-L12), [README.md#L20-L21](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L20-L21), [README.md#L14-L15](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L14-L15), [README.md#L26-L27](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L26-L27) (`clm_ea662ea45d4b929a4db1ea1b756db1f7a3394c6ee1ad66626dc682472b844ebf`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Runs are launched with 'python tests/test_top_agent.py' and configured via an args_dict with provider, model, filter_instance regex, benchmark type/path, run_identifier, n, temperature, top_p, max_token, and key_cfg_path. -- evidence: [README.md#L114-L114](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L114-L114), [README.md#L116-L146](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L116-L146), [README.md#L110-L112](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L110-L112) (`clm_d59281c4b0269d88834a92f679a070b2b6b6c03516c2bf8bda839266f1c89160`)
- [observation/documented] The run configuration supports verilog_eval_v1 and verilog_eval_v2 benchmark types, and gpt-4o and Claude models are documented as verified. -- evidence: [README.md#L116-L146](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L116-L146) (`clm_bf8d3df88448c0192f2623e2a7a5918e5e1050e3fc52f68481328e2c4723ec9b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The run harness executes the agent against verilog-eval benchmark instances selectable by regex filter, with repeated runs (n) and sampling parameters such as temperature 0.85 and top_p 0.95. -- evidence: [README.md#L116-L146](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L116-L146) (`clm_2e583ea3226e8a9c38b0147e885baffd22ff1425c8cc17f9717bc1acad8afb03`)

## dependencies (4 claim(s))

- [observation/documented] The README instructs installing Icarus Verilog 12.0, with an Ubuntu source build of the v12 branch and a macOS Homebrew option. -- evidence: [README.md#L57-L59](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L57-L59), [README.md#L46-L55](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L46-L55), [README.md#L42-L43](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L42-L43) (`clm_583b18d3bff414449d72a328cb17d418fe833a940355daadc43be953b80621f8`)
- [observation/documented] The README gives Verilator installation instructions via apt or by compiling from the verilator GitHub repository. -- evidence: [README.md#L74-L74](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L74-L74), [README.md#L76-L76](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L76-L76), [README.md#L79-L85](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L79-L85) (`clm_7b3373d9b6efbb2094d5530c5d1eb8e01468b09d26a9f9af68b166944a317a9b`)
- [observation/documented] Pyverilog is installed from a cloned PyHDI repository, with jinja2 and ply installed beforehand and a user-directory setup.py install. -- evidence: [README.md#L91-L91](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L91-L91), [README.md#L89-L89](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L89-L89), [README.md#L93-L94](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L93-L94), [README.md#L96-L97](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L96-L97) (`clm_6a2ca8b9242316e2235fe54dcd8a65247e203adbc122028ea6279d06f846fd76`)
- [observation/documented] Benchmarks come from the NVlabs verilog-eval repository, fetched via a recursive git submodule update. -- evidence: [README.md#L101-L103](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L101-L103), [README.md#L105-L107](https://github.com/stable-lab/MAGE/blob/90c96366c518d32bd7b81703bdef3cc46eeaeaf9/README.md#L105-L107) (`clm_a152458e5c30a6c40ab871cad788fcc32fc906662e9f6ea14d9b5d6c8f4529aa`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

