# Shai – Quick Guide

## How to compile
```bash
# Debug build (default)
cargo build

# Optimized release build
cargo build --release
```
- Binaries are placed in `target/debug/` or `target/release/`.


## Project layout
- **`shai-cli/`** – Command‑line interface entry point.
- **`shai-core/`** – Core library (agent, state machine, protocol).
- **`shai-llm/`** – LLM provider wrappers.
- **`docs/`** – Additional documentation and diagrams.
- **`assets/`** – Images/GIFs used in the README.
- **`examples/`** – Small example programs.
- **`tests/`** – Integration and unit tests.
- **`install.sh`** – Helper script to install the CLI (`cargo install --path .`).
- Root `README.md`, `CONTRIBUTING.md`, `LICENSE`, etc. – Project meta‑information.

## About Shai
*Shai is a coding agent, your pair‑programming buddy that lives in the terminal. Written in Rust with love <3.*
