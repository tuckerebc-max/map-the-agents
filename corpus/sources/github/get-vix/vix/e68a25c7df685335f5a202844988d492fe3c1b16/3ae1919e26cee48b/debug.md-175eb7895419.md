# Debug & Profiling

Both `vixd` and `vix` expose a pprof HTTP server when launched with `--pprof-port`.
`make run-d` and `make run-x` enable it automatically.

| Process | Default pprof port | Flag              | Env var          |
|---------|--------------------|-------------------|------------------|
| vixd    | 6060               | `--pprof-port`    | `VIX_PPROF_PORT` |
| vix     | 6061               | `--pprof-port`    | `VIX_PPROF_PORT` |

---

## Capture a Snapshot

Run all commands **while the target process is live**.

### Goroutine Dump (Blocking / Backpressure Issues)

```bash
# vixd
curl -s "http://localhost:6060/debug/pprof/goroutine?debug=2" > /tmp/vixd-goroutines.txt

# vix TUI
curl -s "http://localhost:6061/debug/pprof/goroutine?debug=2" > /tmp/vix-goroutines.txt
```

### Heap Snapshot

```bash
curl -s "http://localhost:6060/debug/pprof/heap" > /tmp/vixd-heap.pprof
curl -s "http://localhost:6061/debug/pprof/heap" > /tmp/vix-heap.pprof

go tool pprof -http=:8080 /tmp/vixd-heap.pprof
```

### CPU Profile (30-Second Sample)

```bash
curl -s "http://localhost:6060/debug/pprof/profile?seconds=30" > /tmp/vixd-cpu.pprof
curl -s "http://localhost:6061/debug/pprof/profile?seconds=30" > /tmp/vix-cpu.pprof

go tool pprof -http=:8080 /tmp/vixd-cpu.pprof
```

### All-In-One Snapshot Script

```bash
TS=$(date +%Y%m%d_%H%M%S)
OUT="/tmp/vix-debug-$TS"
mkdir -p "$OUT"

for PORT in 6060 6061; do
  NAME=$([ "$PORT" = "6060" ] && echo vixd || echo vix)
  curl -s "http://localhost:$PORT/debug/pprof/goroutine?debug=2" > "$OUT/$NAME-goroutines.txt"
  curl -s "http://localhost:$PORT/debug/pprof/heap"               > "$OUT/$NAME-heap.pprof"
  curl -s "http://localhost:$PORT/debug/pprof/allocs"             > "$OUT/$NAME-allocs.pprof"
  echo "[$NAME] snapshots saved to $OUT/"
done
```

---

## Debug Environment Variables

Set by `make run-d` / `make run-x` automatically.

| Variable              | Value            | Effect                                         |
|-----------------------|------------------|------------------------------------------------|
| `GOTRACEBACK=crash`   | crash            | Full goroutine stacks + core dump on panic     |
| `GODEBUG=schedtrace=5000` | 5000 ms      | Scheduler trace every 5 s to stderr            |
| `GORACE=halt_on_error=1`  | 1            | Halt immediately on first data race detected   |

To capture stderr logs to a file while running manually:

```bash
GOTRACEBACK=crash GODEBUG=schedtrace=5000 \
./bin/vixd --pprof-port 6060 2>/tmp/vixd-debug.log &

GOTRACEBACK=crash \
./bin/vix --pprof-port 6061 2>/tmp/vix-debug.log
```
