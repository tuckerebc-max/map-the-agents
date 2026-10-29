# Making CAAM Not Useless - Prompt Edition

Ok, this application (caam) is still quite useless to my workflows despite all its existing features. For one thing, instead of manually always having to add accounts, it would be nice to have an active "watcher" mode and then as I naturally log into different accounts for Claude Code, Codex, or Gemini in the normal course (which causes the contents of the auth files stored in places like `~/.codex` to change in telltale ways), `caam` (this app) should automatically be able to pick up on that and add the account automatically in all its details with the right name and everything. That's one big thing.

The other big thing is that the PRIMARY thing that takes a lot of time and interrupts my workflows is when I have a ton of in-progress Claude Code sessions and then in the middle of all these active sessions, I run out of usage and I'm confronted with a usage expiry message like this:

```text
● The agent-state.ts changes are from different work. I'll only commit my dashboard fix:

● Bash(git add control_plane/src/dashboards/service.ts control_plane/src/__tests__/dashboards.test.ts)
⎿  (No content)
⎿  You've hit your limit · resets 2pm (America/New_York)
Opening your options…

✻ Worked for 6m 27s
```

That completely interrupts my work and requires interactive changes in the terminals. Now, I know there is no universal way to do this no matter what terminal you're using unless you're already doing everything from within a tmux session or similar. But I want to see if there IS a way we can do this using WezTerm, because I'm currently using WezTerm in a manner similar to tmux, where I'm connecting to a persistent session running on the remote machine (a Linux server) so that if WezTerm crashed on my local machine (a Mac Mini), I wouldn't lose any state and could always reconnect.

I can show you my WezTerm config for all this if you need, it's a lua file on my Mac Mini, or you can read about it here: `https://github.com/Dicklesworthstone/misc_coding_agent_tips_and_scripts/blob/main/WEZTERM_PERSISTENT_REMOTE_SESSIONS.md`.

So anyway, we can also later discuss Ghostty, because I also use that (via the Ghostty workspace feature, shown here):

```bash
❯ which trj-workspace
/Users/username/bin/trj-workspace

❯ cat /Users/username/bin/trj-workspace
─────┬─────────────────────────────────────────────────────────────────────────
│ File: /Users/username/bin/trj-workspace
─────┼─────────────────────────────────────────────────────────────────────────
1 │ #!/bin/bash
2 │ # Open Ghostty workspace for TRJ
3 │ # All tabs will SSH to trj:/data/projects
4 │ # Cyberpunk aurora theme + tabs persist across restarts
5 │
6 │ CONFIG="$HOME/.config/ghostty/trj-workspace.conf"
7 │
8 │ # Create workspace config with cyberpunk aurora theme
9 │ cat > "$CONFIG" << CONF
10 │ # TRJ Workspace - all tabs SSH to trj:/data/projects
11 │ command = $HOME/bin/trj-shell
12 │ font-family = Pragmasevka Nerd Font
13 │ font-size = 18
14 │ window-vsync = false
15 │ custom-shader = $HOME/.config/ghostty/shaders/bettercrt.glsl
16 │ auto-update-channel = tip
17 │ window-save-state = always
18 │
19 │ # Cyberpunk Aurora - deep space with electric neon
20 │ background = #0a0e14
21 │ foreground = #b3f4ff
22 │ cursor-color = #ff00ff
23 │ cursor-text = #0a0e14
24 │ selection-background = #1a1f29
25 │ selection-foreground = #ffffff
26 │
27 │ # Neon palette - electric and alive
28 │ palette = 0=#1a1f29
29 │ palette = 1=#ff3366
30 │ palette = 2=#39ffb4
31 │ palette = 3=#ffe566
32 │ palette = 4=#00aaff
33 │ palette = 5=#ff00ff
34 │ palette = 6=#00ffff
35 │ palette = 7=#c7d5e0
36 │ palette = 8=#3d4f5f
37 │ palette = 9=#ff6b9d
38 │ palette = 10=#6bffcd
39 │ palette = 11=#ffef99
40 │ palette = 12=#66ccff
41 │ palette = 13=#ff66ff
42 │ palette = 14=#66ffff
43 │ palette = 15=#ffffff
44 │
45 │ # Tab switching (Shift+Ctrl+Arrow via BetterMouse thumbwheel)
46 │ keybind = ctrl+shift+left=previous_tab
47 │ keybind = ctrl+shift+right=next_tab
48 │ keybind = ctrl+shift+page_up=move_tab:-1
49 │ keybind = ctrl+shift+page_down=move_tab:1
50 │ CONF
51 │
52 │ # Launch Ghostty with workspace config
53 │ open -na "Ghostty" --args --config-file="$CONFIG"
54 │
55 │ echo "TRJ workspace opened (cyberpunk aurora theme)."
56 │ echo "  Cmd+T = new tab (each SSHs to trj:/data/projects)"
57 │ echo "  Tabs will restore automatically next time."
─────┴─────────────────────────────────────────────────────────────────────────

    ~/projects                                           ✔  at 03:51:57 PM  
```

In any event, the basic thing I want to do is to automate the process of handling the login process in each active console. Now let me clarify something: if a Claude Code session already finished a "turn" and was idle when the usage ran out, it's faster for me to simply close it and reopen it using my `cc` alias (see my zhsrc file); that's because once I've completed the login auth flow ONCE, all new sessions automatically use that new one.

MY problems and all my frustrations and wasted time arise for the sessions where Claude Code was right in the middle of something and I would lose valuable state if I were to simply quit and reopen Claude Code; for instance, it could have just started working on something and marked a new bead as being "in progress" from "open"; if I close that Claude Code instance at that moment in an attempt to avoid the relogin annoyance, I would leave that bead in a "stranded" state where other agents don't know to work on it. That's just one example, there are countless others where I would simply waste a ton of tokens to get the agent to the same point in terms of context where it could do the same work at the same level of competence and understanding.

So anyway, what I ended up needing to do is the following: type `/login` and hit enter; wait a few seconds for it to show a URL; then I copy that url (which is generally coming from a remote machine, so that I need to use the "Challenge code" approach instead of direct auth like you can do when the machine running Claude Code IS your local machine, like my Mac Mini for instance) and paste it into Chrome browser on my local Mac, which takes me to a screen.

For the FIRST session that I need to change to a new Google account for Claude Code, I have to figure out which one I haven't used in a while (we really SHOULD be able to directly look up this usage data so we can really be smart about it), then choose that as my Google account in the login screen (I have ALREADY logged in using Google to all the relevant Google accounts; that is, if I went to google.com and clicked the account button in the upper right, I would be able to directly switch to any of them without entering a password again). Anyway, I choose the relevant Google account on the Claude login page, and then I get a code that I can copy to the clipboard, then switch back to the terminal/console and paste it in; I wait a second or two, then I need to press enter again to confirm and it shows the name of the email address using. Then I can simply type "proceed. Reread AGENTS.md so it's still fresh in your mind. Use ultrathink." and it resumes.

Now, for all the OTHER Claude Code sessions that also stopped in the middle of something, those go a bit faster, because I do the login command and press enter and get a link, but when I go to the link, I'm already logged into the new Google account with Claude that still has available usage, so there I only need to press the button to generate the challenge code and paste it into the console and then press enter and then tell it to proceed (that is, I avoid the process of logging into the different Google account).

So anyway, I really want you to carefully think through all this stuff and how, at least on a Mac, you could optimally automate all this for me. It seems really hard because you need a way to capture what's happening inside WezTerm terminal sessions on the remote machine and then how to trigger actions on the local machine in the browser; however we could use Playwright with Chrome for that part.

Here are some examples of the stuff I see in the terminal with Claude Code when this process comes up; each section is separated with `---`:

```text
● Write(control_plane/src/__tests__/approval-store.test.ts)
⎿  Wrote 394 lines to control_plane/src/__tests__/approval-store.test.ts
1 import { describe, it, expect, beforeEach, afterEach } from 'bun:test';
2 import { ApprovalStore, resetApprovalStore, type CreateApprovalInput } from '../approval-store.js';
3 describe('ApprovalStore', () => {
4   let store: ApprovalStore;
5   beforeEach(() => {
6     resetApprovalStore();
7     store = new ApprovalStore();
8   });
… +384 lines (ctrl+o to expand)
⎿  You've hit your limit · resets 2pm (America/New_York)
Opening your options…

✻ Sautéed for 12m 29s

❯ proceed.
⎿  You've hit your limit · resets 2pm (America/New_York)
Opening your options…

❯ /login

Browser didn't open? Use the url below to sign in:

https://claude.ai/oauth/authorize?code=true&client_id=9d1c250a-e61b-44d9-88ed-5944d1962f5e&response_type=code&redirect_uri=https%3A%2F%2Fconsole.anthropic.com%2Foauth%2Fcode%2Fcallback&scope=org%3Acreate_api_key+user%3Aprofile+user%3Ainference+user%3Asessions%3Aclaude_code&code_challenge=REDACTED_CHALLENGE&code_challenge_method=S256&state=REDACTED_STATE

Paste code here if prompted >

---

● The agent-state.ts changes are from different work. I'll only commit my dashboard fix:

● Bash(git add control_plane/src/dashboards/service.ts control_plane/src/__tests__/dashboards.test.ts)
⎿  (No content)
⎿  You've hit your limit · resets 2pm (America/New_York)
Opening your options…

✻ Worked for 6m 27s

---

✻ Worked for 6m 27s

❯ /login


Claude Code can be used with your Claude subscription or billed based on API usage through your Console account.

Select login method:

❯ 1. Claude account with subscription · Pro, Max, Team, or Enterprise

2. Anthropic Console account · API usage billing

---

❯ /login

Browser didn't open? Use the url below to sign in:

https://claude.ai/oauth/authorize?code=true&client_id=9d1c250a-e61b-44d9-88ed-5944d1962f5e&response_type=code&redirect_uri=https%3A%2F%2Fconsole.anthropic.com%2Foauth%2Fcode%2Fcallback&scope=org%3Acreate_api_key+user%3Aprofile+user%3Ainference+user%3Asessions%3Aclaude_code&code_challenge=REDACTED_CHALLENGE&code_challenge_method=S256&state=REDACTED_STATE


Paste code here if prompted >
```

---

● This is a complex but very valuable problem to solve. Let me think through this systematically.

**Understanding Your Pain Points**

1.  **Manual account discovery:** Currently you must explicitly `caam backup` after each login.
2.  **Rate limit recovery across multiple sessions:** When Claude Code hits limits mid-work, you need to manually `/login` in each affected terminal, copy URLs, handle browser auth, paste codes back.

The second problem is particularly painful because:
*   Sessions with in-progress work can't simply be restarted (would lose context, leave beads stranded).
*   You have multiple sessions hitting limits simultaneously.
*   The auth flow involves coordination between remote Linux server (where Claude Code runs) and local Mac (where browser runs).

Let me fetch your WezTerm setup documentation to understand the architecture better.

● Fetch(https://github.com/Dicklesworthstone/misc_coding_agent_tips_and_scripts/blob/main/WEZTERM_PERSISTENT_REMOTE_SESSIONS.md)
⎿  Received 317.9KB (200 OK)

● Now I have a clearer picture. Let me analyze this comprehensively.

### Architecture Analysis

**Your setup:**
```text
[Mac Mini - Local]                    [Linux Server - Remote]
├── WezTerm client          ←SSH→     ├── wezterm-mux-server (systemd)
├── Chrome (all Google                │   ├── Pane 1: Claude Code session
│   accounts logged in)               │   ├── Pane 2: Claude Code session
└── Ghostty (alternative)             │   └── Pane N: ...
                                      └── Auth files (~/.claude/, etc.)
```

**When rate limit hits:**
1.  Claude Code in remote pane shows "You've hit your limit".
2.  You type `/login` → select option 1 → URL appears.
3.  Cross-machine hop needed: URL must go to local Mac browser.
4.  Browser completes OAuth → challenge code generated.
5.  Cross-machine hop back: Code must return to remote pane.
6.  Code pasted + Enter → session resumes.

### Proposed Solution Architecture

**Two Major Features**

**Feature 1: Auto-Discovery Watcher** (simpler, implement first)
`caam watch [--daemon]`
*   Uses `fsnotify` to watch auth file changes.
*   Parses changed files to extract account identity (email from JWT).
*   Auto-creates vault profile with email as name.
*   Runs as daemon or one-shot.

**Feature 2: Distributed Auth Recovery System** (complex, the main value)

```text
┌─────────────────────────────────────────────────────────────────┐
│                     REMOTE (Linux Server)                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  caam auth-coordinator (daemon)                           │  │
│  │  ├── Polls all WezTerm panes via `wezterm cli get-text`   │  │
│  │  ├── State machine per pane (IDLE→RATE_LIMITED→...)       │  │
│  │  ├── Auto-injects `/login` + selects option 1             │  │
│  │  ├── Extracts OAuth URLs                                  │  │
│  │  ├── Queues auth requests (pane_id, url, timestamp)       │  │
│  │  ├── Exposes HTTP API on localhost:PORT                   │  │
│  │  └── Injects codes back via `wezterm cli send-text`       │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↑
                              │ SSH tunnel (ssh -R remote:PORT:local:PORT)
                              │ or persistent WebSocket
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      LOCAL (Mac Mini)                           │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  caam auth-agent (daemon)                                 │  │
│  │  ├── Polls remote coordinator for pending auth requests   │  │
│  │  ├── Uses Playwright + Chrome to complete OAuth flow      │  │
│  │  │   ├── Opens URL                                        │  │
│  │  │   ├── Selects Google account (LRU or configured)       │  │
│  │  │   └── Extracts challenge code                          │  │
│  │  ├── Sends code back to coordinator                       │  │
│  │  └── Tracks account usage (which was used when)           │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**State Machine Per Pane**

1.  **IDLE**
    *   detect "You've hit your limit"
2.  **RATE_LIMITED**
    *   auto-inject "/login\n"
3.  **AWAITING_METHOD_SELECT**
    *   detect "Select login method:" → inject "1\n"
4.  **AWAITING_URL**
    *   detect OAuth URL (regex extract)
5.  **AUTH_IN_PROGRESS**
    *   send URL to local agent
    *   wait for code response
6.  **CODE_RECEIVED**
    *   inject code + "\n"
7.  **AWAITING_CONFIRM**
    *   detect email confirmation or prompt
    *   inject "proceed. Reread AGENTS.md so it's still fresh in your mind. Use ultrathink.\n"
8.  **IDLE** (resumed)

**Key Technical Pieces**

**WezTerm CLI Integration (remote side):**
```bash
# List all panes with their IDs
wezterm cli list --format json

# Get recent text from a pane (last N lines)
wezterm cli get-text --pane-id 123 --start-line -50

# Send text to a pane
wezterm cli send-text --pane-id 123 --no-paste "/login\n"
```

**Pattern Detection (regex):**
```go
var patterns = map[string]*regexp.Regexp{
    "rate_limit":    regexp.MustCompile(`You've hit your limit.*resets`),
    "select_method": regexp.MustCompile(`Select login method:`),
    "oauth_url":     regexp.MustCompile(`https://claude\.ai/oauth/authorize\?[^\s]+`),
    "paste_prompt":  regexp.MustCompile(`Paste code here if prompted`),
    "login_success": regexp.MustCompile(`Logged in as .+@.+`),
}
```

**Playwright OAuth Flow (local side):**
```javascript
// Pseudocode
async function completeOAuth(url: string, preferredAccount?: string) {
    const page = await browser.newPage();
    await page.goto(url);

    // Handle Google account selection
    if (await page.locator('div[data-email]').count() > 0) {
        // Multiple accounts available
        if (preferredAccount) {
            await page.click(`div[data-email="${preferredAccount}"]`);
        } else {
            // Use LRU strategy
            const lru = await getLeastRecentlyUsedAccount();
            await page.click(`div[data-email="${lru}"]`);
        }
    }

    // Wait for challenge code page
    await page.waitForSelector('.challenge-code, [data-testid="code"]');
    const code = await page.textContent('.challenge-code');

    await page.close();
    return code;
}
```

**Clarifying Questions**

Before I dive into implementation, I need to understand:

● User answered Claude's questions:
⎿  · How many Claude Max accounts do you have that you rotate between? → **7+ accounts**
   · For the auth-agent on your Mac, how should it select which Google account to use? → **Least Recently Used (Recommended)**
   · How do you want to handle the communication channel between remote Linux and local Mac? → **SSH reverse tunnel (Recommended)**
   · Do you want fully automatic recovery (no human intervention) or semi-automatic (notification + one-click approve)? → **Fully automatic (Recommended)**

● Excellent choices. With 7+ accounts and fully automatic mode, this will be a powerful system. Let me create a plan for this.

● Let me create a detailed design document for this system.

● Write(docs/DISTRIBUTED_AUTH_RECOVERY.md)
⎿  Wrote 526 lines to docs/DISTRIBUTED_AUTH_RECOVERY.md
    1 # Distributed Auth Recovery System - Design Document
    2 ## Overview
    3 This document describes two related features for caam:
    4 1. **Auto-Discovery Watcher**: Automatically detect and save auth profiles when users log in naturally
    5 2. **Distributed Auth Recovery**: Automatically handle Claude Code rate limit recovery across multiple remote terminal sessions
    6 ## Problem Statement
   … +516 lines (ctrl+o to expand)

---

● The plan is complete and comprehensive. It includes:

**Summary:**
*   `caam setup distributed` command to auto-configure the entire system
*   Agent polls multiple coordinators (fan-out parallel)
*   Parse WezTerm Lua config with regex (no Lua interpreter needed)
*   Cross-reference with Tailscale for optimal IPs
*   Deploy coordinator to remotes via SSH/SFTP with version checking
*   Systemd user services on remotes
*   ~750 lines of new code across 6 implementation phases

● User approved Claude's plan
⎿  Plan saved to: ~/.claude/plans/rippling-coalescing-crane.md · /plan to edit

### Tailscale + WezTerm Auto-Setup Feature Plan

**Overview**

Add a `caam setup distributed` command that automatically configures the distributed auth recovery system across multiple machines using Tailscale for connectivity and parsing WezTerm's Lua config for domain discovery.

**Architecture:**
*   **Local machine (Mac mini):** Runs auth-agent with browser, polls ALL coordinators.
*   **Remote machines (csd, css, trj):** Each runs coordinator daemon to monitor WezTerm mux-server panes.

**Communication Flow:**
```text
Local (agent)                    Remote machines
    │                            ┌─────────────────┐
    │── Poll /auth/pending ────> │ css coordinator │
    │<─ Pending requests ─────── │ (port 7890)     │
    │                            └─────────────────┘
    │                            ┌─────────────────┐
    │── Poll /auth/pending ────> │ csd coordinator │
    │<─ Pending requests ─────── │ (port 7890)     │
    │                            └─────────────────┘
    │                            ┌─────────────────┐
    │── Poll /auth/pending ────> │ trj coordinator │
    │<─ Pending requests ─────── │ (port 7890)     │
    └─                           └─────────────────┘
```

Agent initiates all connections outbound (no firewall issues). Uses Tailscale IPs when available for faster connectivity.

**New Packages**

**1. internal/tailscale/tailscale.go**

Tailscale detection and peer discovery:
*   `IsAvailable() bool` - Check if tailscaled is running
*   `GetStatus() (*Status, error)` - Parse tailscale status --json
*   `GetSelf() *Peer` - Local machine info
*   `GetPeers() []*Peer` - All machines on tailnet
*   `FindPeerByHostname(name string) *Peer` - Fuzzy match
*   `FindPeerByIP(ip string) *Peer` - Match by any IP

```go
type Status struct {
    Version      string
    BackendState string // "Running", "Stopped", etc.
    Self         *Peer
    Peers        map[string]*Peer
}

type Peer struct {
    ID           string
    HostName     string
    DNSName      string   // e.g., "superserver.tail1f21e.ts.net."
    TailscaleIPs []string // e.g., ["100.x.x.x", "fd7a:..."]
    Online       bool
    OS           string
}
```

**2. internal/wezterm/config.go**

Parse WezTerm Lua configuration:
*   `ParseConfig(path string) (*Config, error)` - Parse wezterm.lua
*   `FindConfigPath() string` - Default paths: `~/.config/wezterm/wezterm.lua`, `~/.wezterm.lua`
*   `ExtractSSHDomains(cfg *Config) []SSHDomain`

```go
type SSHDomain struct {
    Name          string // "csd", "css", "trj"
    RemoteAddress string // IP or hostname
    Username      string // "ubuntu"
    Port          int    // default 22
    Multiplexing  string // "WezTerm", "None"
    IdentityFile  string // SSH key path
}

type Config struct {
    SSHDomains []SSHDomain
    // Other fields as needed
}
```

**Lua Parsing Strategy:**
Pattern-based extraction (no Lua interpreter library needed - avoids ~2MB binary bloat):
```lua
config.ssh_domains = {
  { name = 'csd', remote_address = '...', username = '...', ... },
}
```

Parsing approach:
1.  Find `ssh_domains` assignment with regex: `ssh_domains\s*=\s*\{`
2.  Match balanced braces to extract array content
3.  Parse each `{...}` block for: `name`, `remote_address`, `username`, `port`, `ssh_option.identityfile`
4.  Handle Lua string quoting (single and double quotes)
5.  Skip comments and complex expressions

**3. internal/setup/remote.go**

Remote machine setup orchestration:
*   `Setup(opts *Options) error` - Main entry point
*   `DetectLocalMachine() (*Machine, error)` - Identify where we're running
*   `DiscoverRemoteMachines() ([]*Machine, error)` - Find remotes via wezterm + tailscale
*   `DeployToRemote(m *Machine) error` - SSH and setup coordinator
*   `GenerateConfigs() error` - Generate all config files

```go
type Machine struct {
    Name          string // Display name
    WezTermDomain string // "csd", "css", etc.
    SSHAddress    string // Address for SSH connection
    TailscaleIP   string // If on tailnet
    PublicIP      string // Original address
    Username      string
    IdentityFile  string
    Role          Role   // "coordinator" or "agent"
}

type Role string
const (
    RoleCoordinator Role = "coordinator"
    RoleAgent       Role = "agent"
)
```

**4. internal/agent/multi.go**

Extend agent to poll multiple coordinators:
```go
type MultiCoordinatorAgent struct {
    config        Config
    coordinators  []*CoordinatorEndpoint
    browser       *Browser
    accountUsage  map[string]*AccountUsage
    // ... other fields from Agent
}

type CoordinatorEndpoint struct {
    Name        string    // "csd", "css", "trj"
    URL         string    // http://100.x.x.x:7890
    DisplayName string    // "Sense Demo"
    LastCheck   time.Time
    IsHealthy   bool
    LastError   string
}

// pollLoop fans out to all coordinators in parallel
func (a *MultiCoordinatorAgent) pollLoop(ctx context.Context) {
    ticker := time.NewTicker(a.config.PollInterval)
    for {
        select {
        case <-ticker.C:
            // Fan-out: check all coordinators concurrently
            var wg sync.WaitGroup
            for _, coord := range a.coordinators {
                wg.Add(1)
                go func(c *CoordinatorEndpoint) {
                    defer wg.Done()
                    a.checkCoordinator(ctx, c)
                }(coord)
            }
            wg.Wait()
        }
    }
}
```

**5. internal/deploy/deploy.go**

Binary deployment with version checking:
```go
type Deployer struct {
    sshClient    *sync.SSHClient
    localVersion string
    binaryPath   string
}

func (d *Deployer) EnsureCAAM(m *Machine) error {
    // 1. Check if caam exists
    exists, _ := d.remoteFileExists("/usr/local/bin/caam")

    // 2. Compare versions if exists
    if exists {
        remoteVer, _ := d.runCmd("caam --version")
        if remoteVer == d.localVersion {
            return nil // Already up to date
        }
    }

    // 3. Upload via SFTP (use existing sync.SSHClient.WriteFile)
    return d.uploadBinary()
}
```

**New Command**

`caam setup distributed`

`caam setup distributed [--wezterm-config PATH] [--use-tailscale] [--dry-run]`

**Flags:**
*   `--wezterm-config`  Path to wezterm.lua (default: auto-detect)
*   `--use-tailscale`   Prefer tailscale IPs when available (default: true)
*   `--dry-run`         Show what would be done without making changes
*   `--local-port`      Port for local auth-agent (default: 7891)
*   `--remote-port`     Port for remote coordinator (default: 7890)
*   `--remotes`         Comma-separated list of domains to setup (default: all)

**Flow:**
1.  Detect local machine (via tailscale self or hostname)
2.  Parse wezterm.lua for SSH domains
3.  Query tailscale for peer info
4.  Cross-reference domains with tailscale peers
5.  Display discovered configuration for confirmation
6.  For each remote machine:
    a. SSH and check/install caam binary
    b. Generate coordinator config
    c. Set up systemd user service
    d. Start coordinator
7.  Configure local auth-agent
8.  Display status and connection info

**File Changes**

**Modified Files**

*   `cmd/caam/cmd/root.go`
    *   Add setup command group
*   `cmd/caam/cmd/agent.go`
    *   Add `--config-file` flag to load from generated config
*   `cmd/caam/cmd/coordinator.go`
    *   Add `--config-file` flag to load from generated config

**New Files**

*   `cmd/caam/cmd/setup.go`
    ```go
    var setupCmd = &cobra.Command{Use: "setup"}
    var setupRemoteCmd = &cobra.Command{
        Use:   "remote",
        Short: "Auto-configure coordinator/agent across machines",
        RunE:  runSetupRemote,
    }
    ```
*   `internal/tailscale/tailscale.go` - Tailscale client
*   `internal/wezterm/config.go` - WezTerm config parser
*   `internal/setup/remote.go` - Remote setup orchestration
*   `internal/setup/deploy.go` - SSH deployment logic
*   `internal/setup/service.go` - Systemd service generation

**Generated Configs**

**Local (Mac mini):** `~/.config/caam/distributed-agent.json`
```json
{
  "port": 7891,
  "coordinators": [
    {
      "name": "csd",
      "url": "http://100.x.x.x:7890",
      "display_name": "Sense Demo"
    },
    {
      "name": "css",
      "url": "http://100.x.x.x:7890",
      "display_name": "Super Server"
    },
    {
      "name": "trj",
      "url": "http://100.x.x.x:7890",
      "display_name": "Threadripper"
    }
  ],
  "poll_interval": "2s",
  "accounts": [],
  "strategy": "lru",
  "chrome_profile": ""
}
```

**Remote (e.g., css):** `~/.config/caam/coordinator.json`
```json
{
  "port": 7890,
  "poll_interval": "500ms",
  "auth_timeout": "60s",
  "state_timeout": "30s",
  "resume_prompt": "proceed. Reread AGENTS.md so it's still fresh in your mind. Use ultrathink.\n",
  "output_lines": 100,
  "pane_filter": {
    "domain": "local"
  }
}
```

*Note: Coordinator no longer needs agent_url - the agent polls the coordinator, not vice versa.*

**Systemd user service:** `~/.config/systemd/user/caam-coordinator.service`
```ini
[Unit]
Description=CAAM Auth Recovery Coordinator
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/caam auth-coordinator --config %h/.config/caam/coordinator.json
Restart=on-failure
RestartSec=5
Environment=HOME=%h

[Install]
WantedBy=default.target
```

Enable linger for user services to survive logout:
`loginctl enable-linger ubuntu`

**Implementation Order**

1.  **Phase 1: Tailscale package (~50 lines)**
    *   `internal/tailscale/tailscale.go`
    *   Parse `tailscale status --json`
    *   Get self, peers, find by hostname/IP
    *   Tests with sample JSON
2.  **Phase 2: WezTerm config parser (~100 lines)**
    *   `internal/wezterm/config.go`
    *   Regex-based extraction of `ssh_domains`
    *   Handle user's actual config patterns
    *   Tests with user's `wezterm.lua` as sample
3.  **Phase 3: Multi-coordinator agent (~150 lines)**
    *   `internal/agent/multi.go`
    *   Extend agent to poll multiple coordinators
    *   Fan-out parallel polling
    *   Health tracking per coordinator
4.  **Phase 4: Remote deployment (~200 lines)**
    *   `internal/deploy/deploy.go` - Binary deployment via SFTP
    *   `internal/deploy/systemd.go` - Systemd unit generation
    *   `internal/deploy/config.go` - Config file generation
    *   Reuse existing `internal/sync/ssh.go` patterns
5.  **Phase 5: Setup orchestration (~150 lines)**
    *   `internal/setup/setup.go`
    *   Machine discovery (wezterm + tailscale cross-reference)
    *   Orchestrate full setup flow
    *   Progress reporting
6.  **Phase 6: CLI command (~100 lines)**
    *   `cmd/caam/cmd/setup.go`
    *   `caam setup distributed` command
    *   Flags, dry-run, progress display

**Total: ~750 lines of new code**

**Cross-Platform Notes**

**Remote machines (Linux):** Use systemd user units as shown above.

**Local machine (macOS):** The agent can run in foreground or use launchd:
`~/Library/LaunchAgents/com.caam.agent.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "...">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.caam.agent</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/caam</string>
        <string>auth-agent</string>
        <string>--config</string>
        <string>~/.config/caam/distributed-agent.json</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

For initial implementation, focus on Linux systemd for remotes. Local agent can start manually or via the user's preferred method.

**Verification Plan**

1.  **Unit tests:**
    *   `internal/tailscale/tailscale_test.go` - Parse sample JSON, find peers
    *   `internal/wezterm/config_test.go` - Parse user's actual wezterm.lua
    *   `internal/agent/multi_test.go` - Multi-coordinator polling
    *   `internal/deploy/deploy_test.go` - Version checking logic
2.  **Integration test (dry-run):**
    `caam setup distributed --dry-run`
    *   Should output:
        *   Detected local machine
        *   Found wezterm domains
        *   Tailscale cross-reference results
        *   What would be deployed to each remote
        *   Generated config previews
3.  **Manual end-to-end test:**
    ```bash
    # On Mac mini:
    caam setup distributed --remotes css  # Start with one remote

    # Verify coordinator is running on css:
    ssh css 'systemctl --user status caam-coordinator'

    # Start agent locally:
    caam auth-agent --config ~/.config/caam/distributed-agent.json

    # Trigger a rate limit in a css pane and verify auth recovery works
    ```

**Edge Cases**

*   No tailscale → Fall back to public IPs from wezterm config
*   wezterm.lua not found → Error with helpful message pointing to common paths
*   Remote machine offline → Skip with warning, continue with others
*   caam binary missing on remote → Auto-copy from local via SFTP
*   Existing coordinator running → Check status, offer restart if needed
*   SSH key not found → Clear error message with the expected key path
*   Port already in use → Detect and suggest alternative port
*   No SSH domains in wezterm.lua → Error explaining what to add
*   Tailscale peer hostname doesn't match wezterm domain → Fuzzy match by IP or let user specify mapping

**Future Enhancements (Not in Scope)**
*   Automatic launchd plist generation for macOS local agent
*   Web dashboard showing all coordinator statuses
*   Automatic caam updates across all machines
*   Support for non-WezTerm multiplexers (tmux, screen)

● Let me set up the todo list and start implementing.
