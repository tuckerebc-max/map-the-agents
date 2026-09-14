# Terminal compatibility contract

UmaDev treats terminal behavior as a release contract, not a best-effort UI
detail. No emulator is a perfect xterm implementation, and CI cannot reproduce
IME composition or a graphical compositor, so a release needs both automated
protocol tests and the real-terminal matrix below.

## Runtime invariants

- The TUI starts only when both stdin and its stdout render sink are terminals;
  redirected or piped output never enables raw or alternate-screen mode.
- One stdout writer owns every frame and out-of-band control sequence.
- Alternate-screen entry happens once. Focus and resume only reassert
  level-triggered modes.
- Teardown restores raw input, mouse, focus, paste, wrapping, cursor, and the
  main screen on normal exit, panic, and termination signals.
- Autowrap stays off and non-ASCII cell runs are cursor-reanchored, containing
  East Asian ambiguous-width disagreements to one cell.
- Resize, focus return, sleep/resume, IME commit, and terminal-side
  contamination force an appropriate full repaint.
- Terminal query replies travel through the owned input tokenizer and never
  surface as keystrokes. Queries are issued only after alternate-screen entry.
- Windows uses the native crossterm console reader and does not enable the Kitty
  keyboard protocol, preserving CJK IME behavior.
- `UMADEV_THEME=dark|light` is the deterministic fallback when a terminal cannot
  report its background.

## Release matrix

Run every interaction row on every applicable terminal family. Record the OS,
terminal/version, shell, locale, UmaDev version, and pass/fail evidence in the
release issue.

| Platform | Required terminal families |
|---|---|
| Windows | Windows Terminal with PowerShell and cmd; VS Code integrated PowerShell; classic conhost; Git Bash/MSYS2; WSL inside Windows Terminal |
| macOS | Terminal.app; iTerm2; Ghostty or WezTerm; VS Code integrated terminal; tmux |
| Linux | VTE/GNOME Terminal; Konsole; kitty or WezTerm; VS Code integrated terminal; tmux; an SSH session |

| Interaction | Acceptance condition |
|---|---|
| Startup and normal exit | No visible raw escape text; shell echo, cursor, wrapping, mouse, and screen are restored |
| Forced termination | The next shell prompt remains usable; no alternate-screen or mouse mode is left active |
| Chinese/Japanese/Korean IME | Preedit and committed text do not duplicate, reorder, disappear, or leave stale cells |
| ASCII and modified keys | Enter, Shift/Ctrl+Enter, Esc, arrows, Home/End, Backspace, and held-key repeat behave once per action |
| Paste | ASCII, CJK, multiline, large, and bracketed paste remain atomic and never submit an embedded newline unexpectedly |
| Resize | Narrow/wide drag, maximize, fullscreen, and right-edge shrink leave no overlap or stale final column |
| Focus and resume | Alt-tab, sleep/wake, tmux detach/attach, and Unix suspend/`fg` restore input modes and repaint cleanly |
| Streaming | A long mixed CJK/ASCII response has no row drift, wrap cascade, cursor sweep, or input lag |
| Mouse and clipboard | Wheel, drag selection, copy, `/mouse`, local/SSH/tmux clipboard paths do not leak SGR bytes into input |
| Theme | Dark and light backgrounds remain readable; use `UMADEV_THEME` where OSC 11 is unavailable |
| Redirection | Piped stdin, redirected stdout, and non-interactive CI print ordinary help; no raw mode or terminal control frame reaches a file/pipe |

## Automated release gates

- `cargo fmt --all -- --check`
- `cargo clippy --workspace --all-targets -- -D warnings`
- `cargo test --workspace --all-targets --no-fail-fast` on Linux, macOS, and
  Windows
- Windows cross-check from the development host
- recording-backend byte tests for mode ordering, repaint, cursor placement,
  and teardown symmetry
- tokenizer/decoder split-boundary tests for keys, mouse, paste, focus, and
  terminal responses
- native real-process pseudo-terminal smoke on all three CI operating systems:
  Unix PTY on Linux/macOS and ConPTY on Windows; the complete binary must render,
  repaint after narrow/wide resize, preserve an atomic multiline CJK/emoji
  bracketed paste whose first line is `/quit`, accept an intentional `/quit`,
  exit successfully, and show no panic
- npm distribution smoke test, including main-package/platform-package/binary
  version-split repair; on Windows the gate keeps a real copied `.exe` running,
  lets a stand-in package manager return success, and requires the updater to
  reject the still-split install with EPERM recovery guidance rather than print
  a false success

Automated gates are necessary but do not replace the graphical release matrix.
A release with an untested required cell is unverified, not "probably fixed."

## Reference failures studied

- [OpenTUI #1187: incremental diff desynchronization and ambiguous width](https://github.com/anomalyco/opentui/issues/1187)
- [OpenTUI #933: Windows resize stalls after pre-alt-screen queries](https://github.com/anomalyco/opentui/issues/933)
- [OpenTUI #1110: stale right edge after macOS Terminal resize](https://github.com/anomalyco/opentui/issues/1110)
- [OpenCode #34021: Windows CJK corruption after partial rendering](https://github.com/anomalyco/opencode/issues/34021)
- [OpenCode #34198: Windows paste corrupts the TUI](https://github.com/anomalyco/opencode/issues/34198)
- [OpenCode #29697: macOS Terminal IME stale cells](https://github.com/anomalyco/opencode/issues/29697)
- [OpenCode #32336: incomplete terminal teardown](https://github.com/anomalyco/opencode/issues/32336)
- [OpenCode PR #33871: disable Kitty keyboard protocol on Windows for IME compatibility](https://github.com/anomalyco/opencode/pull/33871)
- [Microsoft console virtual-terminal sequence reference](https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences)
