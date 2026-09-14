When compiling zerostack:
- Never run `cargo build`
- Don't use `--release` during development
- Never run `cargo check` (instead use `cargo test`)
- Always run `cargo fmt`
- Always run `cargo install --path . --debug`
- Run `cargo test` if you want to check all unit tests

Important notes:
- Always write tests when writing new non-TUI code.
- Always update docs/ files when needed.
- If adding or editing slash commands, edit the slash commands `/` picker in the TUI.
