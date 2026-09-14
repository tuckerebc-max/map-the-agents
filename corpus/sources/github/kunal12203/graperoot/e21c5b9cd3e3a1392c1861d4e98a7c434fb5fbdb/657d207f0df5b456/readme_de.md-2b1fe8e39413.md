<div align="center">

```
 ▄▀▀▀ █▀▀▄ ▄▀▀▄ █▀▀█ █▀▀▀ █▀▀▄ ▄▀▀▄ ▄▀▀▄ ▀█▀
 █ ▀▄ █▄▄▀ █▄▄█ █▄▄█ █▀▀  █▄▄▀ █  █ █  █  █
 ▀▀▀▀ ▀ ▀▀ ▀  ▀ █    ▀▀▀▀ ▀ ▀▀ ▀▀▀▀ ▀▀▀▀  ▀
```

### Kumulativer Kontext für KI-Programmierassistenten

**[graperoot.dev](https://graperoot.dev)** · [Docs](https://graperoot.dev/docs) · [Benchmarks](https://graperoot.dev/benchmarks) · [Pro](https://graperoot.dev/graperoot-pro) · [Discord](https://discord.com/invite/YwKdQATY2d)

[![PyPI](https://img.shields.io/pypi/v/graperoot?label=version&color=brightgreen)](https://pypi.org/project/graperoot/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](#install)
[![Discord](https://img.shields.io/badge/Discord-community-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/YwKdQATY2d)
[![Stars](https://img.shields.io/github/stars/kunal12203/Codex-CLI-Compact?style=social)](https://github.com/kunal12203/Codex-CLI-Compact/stargazers)

---

🌐 **In deiner Sprache lesen:**
[English](../README.md) · [中文](./README_zh-CN.md) · [Español](./README_es.md) · [हिंदी](./README_hi.md) · [Français](./README_fr.md) · [Deutsch](./README_de.md) · [日本語](./README_ja.md) · [한국어](./README_ko.md) · [Português](./README_pt-BR.md) · [Русский](./README_ru.md) · [العربية](./README_ar.md) · [Türkçe](./README_tr.md) · [Bahasa Indonesia](./README_id.md)

</div>

---

## Was ist GrapeRoot?

GrapeRoot ist eine quelloffene **Kontext-Engine**, die zwischen dir und deinem KI-Programmierassistenten arbeitet. Sie baut einen semantischen Graphen deines Codebases auf — Dateien, Symbole, Importe, Aufrufketten — und lädt genau den richtigen Code in jeden Prompt, bevor deine KI ihn zu sehen bekommt.

Das Ergebnis: Deine KI verwendet Tokens fürs **Denken**, nicht fürs Suchen.

```
Du führst aus: dgc /path/to/project
                    ↓
1. Projekt wird gescannt → semantischer Graph wird aufgebaut (Dateien, Symbole, Importe)
2. Du stellst eine Frage
3. Graph ermittelt die relevanten Dateien → packt sie in den Kontext
4. KI erhält deine Frage + den bereits geladenen richtigen Code
5. Weniger Gesprächsrunden, weniger Tokens, bessere Antworten
```

Die Token-Einsparungen **summieren** sich über eine Sitzung hinweg. Der Graph merkt sich, welche Dateien gelesen, bearbeitet und abgefragt wurden — jede Runde wird günstiger.

---

## Ergebnisse

Benchmarks auf mehreren realen Codebasen (über 7.700 Dateien) und mehr als 50 Engineering-Prompts:

| Metrik | Ohne GrapeRoot | Mit GrapeRoot |
|--------|:--------------:|:-------------:|
| Kosten pro Prompt | $0.49 | **$0.27** |
| Durchschn. Runden pro Aufgabe | 11.7 | **3.5** |
| Durchschn. Antwortzeit | 172s | **124s** |
| Qualität (bewertet) | 76.6 / 100 | **86.6 / 100** |
| Kostengewinnrate | — | **10 von 10 Prompts** |

### Kostenreduzierung nach Aufgabentyp

| Aufgabentyp | Kostenreduzierung |
|-------------|:-----------------:|
| Migration & Architekturdesign | **bis zu 81%** |
| Leistungsanalyse | **bis zu 80%** |
| Tests & Testgenerierung | **bis zu 76%** |
| Full-Stack-Debugging | **bis zu 73%** |
| Funktionsentwicklung | **bis zu 71%** |
| Code-Erklärung & Audit | **bis zu 55%** |
| Große Codebasis (7k+ Dateien, Durchschn.) | **43% im Durchschnitt** |

> Die Einsparungen **summieren sich** über eine Sitzung hinweg — ein in Runde 3 eingesparter Token vermeidet auch die Cache-Neuabrechnung in jeder nachfolgenden Runde. Die Qualität bleibt bei jedem der oben genannten Aufgabentypen gleich oder verbessert sich.

Vollständige Benchmark-Methodik und Ergebnisse: [graperoot.dev/benchmarks](https://graperoot.dev/benchmarks)

---

## Unterstützte KI-Tools

| Tool | Befehl | Status |
|------|--------|--------|
| Claude Code | `dgc` | ✅ Vollständige Unterstützung |
| OpenAI Codex CLI | `dg` | ✅ Vollständige Unterstützung |
| Cursor | `graperoot . --cursor` | ✅ Vollständige Unterstützung |
| Gemini CLI | `graperoot . --gemini` | ✅ Vollständige Unterstützung |
| OpenCode | `graperoot . --opencode` / `dgo` | ✅ Vollständige Unterstützung |
| GitHub Copilot | `graperoot . --copilot` | ✅ Vollständige Unterstützung |
| OpenClaw | `graperoot . --openclaw` | ✅ Vollständige Unterstützung |
| Kilocode | `graperoot . --kilocode` | ✅ Vollständige Unterstützung |
| MiMo Code | `graperoot . --mimocode` | ✅ Vollständige Unterstützung |
| Antigravity | `graperoot . --antigravity` | ✅ Vollständige Unterstützung |

---

## Unterstützte Sprachen

TypeScript · JavaScript · Python · Go · Swift · Rust · Java · Kotlin · Scala · C# · Ruby · PHP

---

## Installation

**macOS / Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/kunal12203/Codex-CLI-Compact/main/install.sh | bash
source ~/.zshrc   # or ~/.bashrc / ~/.profile
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/kunal12203/Codex-CLI-Compact/main/install.ps1 | iex
```

**Windows (Scoop):**
```powershell
scoop bucket add dual-graph https://github.com/kunal12203/scoop-dual-graph
scoop install dual-graph
```

> **Voraussetzungen:** Python 3.10+, Node.js 18+ sowie eines der unterstützten KI-Tools. Das Installationsprogramm erkennt fehlende Tools und bietet deren automatische Installation an.

---

## Verwendung

> **Wichtig:** Verwende immer `dgc` (nicht direkt `claude`), um sicherzustellen, dass der MCP-Server läuft.

### Claude Code

```bash
dgc                                      # scan current directory, launch Claude
dgc /path/to/project                     # scan a specific project
dgc /path/to/project "fix the login bug" # start with a prompt
```

### OpenAI Codex CLI

```bash
dg                              # scan current directory
dg /path/to/project             # scan a specific project
dg /path/to/project "add tests" # start with a prompt
```

### Interaktive Auswahl (neu in v3.9.99)

```bash
graperoot          # shows directory confirm + arrow-key tool picker
graperoot .        # same, picks from current directory
graperoot --version   # print current version
graperoot --update    # force self-update
```

### Alle Tools über `graperoot`

```bash
graperoot . --cursor          # Cursor
graperoot . --gemini          # Gemini CLI
graperoot . --opencode        # OpenCode
graperoot . --copilot         # GitHub Copilot
graperoot . --openclaw        # OpenClaw
graperoot . --kilocode        # Kilocode
graperoot . --mimocode        # MiMo Code
graperoot /path --gemini "add tests"   # specific project + prompt
```

### Windows

```powershell
dgc .                          # from inside the project directory
dgc "D:\projects\my-app"       # any drive, any path
dg "C:\work\backend"           # Codex CLI
dgc --gemini "D:\projects\app" # Gemini CLI on Windows
```

---

## Funktionsweise

1. **Graph-Scan** — Beim ersten Aufruf extrahiert GrapeRoot Dateien, Funktionen, Klassen und Importbeziehungen in einen lokalen Graphen, der unter `.dual-graph/` gespeichert wird.
2. **Kontextabruf** — Bei jeder Frage bewertet der Graph die relevantesten Dateien und fügt sie in den Prompt ein, bevor deine KI ihn sieht.
3. **Sitzungsgedächtnis** — Dateien, die du gelesen, bearbeitet oder abgefragt hast, werden in zukünftigen Runden höher gewichtet. Der Kontext wächst mit jeder Interaktion.
4. **MCP-Tools** — Deine KI kann über graphbewusste Tools (`graph_read`, `graph_retrieve`, `graph_neighbors`) bei Bedarf weiter in die Tiefe gehen.

Die gesamte Verarbeitung findet **lokal** statt. Kein Code verlässt deinen Rechner.

---

## Daten & Dateien

Alle Daten liegen in `<project>/.dual-graph/` (wird automatisch zu `.gitignore` hinzugefügt):

| Datei | Beschreibung |
|-------|--------------|
| `info_graph.json` | Semantischer Graph: Dateien, Symbole, Kanten |
| `chat_action_graph.json` | Sitzungsgedächtnis: Lesevorgänge, Bearbeitungen, Abfragen |
| `context-store.json` | Persistente Entscheidungen, Aufgaben und Fakten über Sitzungen hinweg |

Globale Installation unter `~/.dual-graph/`:

| Datei | Beschreibung |
|-------|--------------|
| `dgc.ps1` / `dg.ps1` | Startskripte (werden automatisch aktualisiert) |
| `venv/` | Virtuelle Python-Umgebung |
| `version.txt` | Installierte Version |

---

## Konfiguration

Alle Einstellungen sind optional und werden über Umgebungsvariablen gesetzt:

| Variable | Standard | Beschreibung |
|----------|----------|--------------|
| `DG_HARD_MAX_READ_CHARS` | `4000` | Maximale Zeichen pro Dateilesezugriff |
| `DG_TURN_READ_BUDGET_CHARS` | `18000` | Gesamtes Lesebudget pro Gesprächsrunde |
| `DG_FALLBACK_MAX_CALLS_PER_TURN` | `1` | Maximale Fallback-Grep-Aufrufe pro Runde |
| `DG_RETRIEVE_CACHE_TTL_SEC` | `900` | Cache-Gültigkeit für Abrufvorgänge (15 Min.) |
| `DG_MCP_PORT` | auto (8080–8099) | Bestimmten MCP-Server-Port erzwingen |

---

## Automatische Aktualisierung

Das Startprogramm prüft bei jedem Aufruf auf Updates und aktualisiert sich stillschweigend selbst. Um ein Update manuell anzustoßen:
```bash
graperoot --update
```

Um die automatische Aktualisierung zu deaktivieren:
```bash
graperoot --no-auto-update
```

Um sie wieder zu aktivieren:
```bash
graperoot --auto-update
```

Aktuelle Version: **3.10.16**

---

## Telemetrie

GrapeRoot sammelt anonyme Absturzberichte, um Fehler zu beheben. Was gesendet wird: Fehlertyp, welcher Schritt fehlschlug, OS/Python-Version, GrapeRoot-Version. Niemals gesendet: Ihr Code, Dateipfade, Projektnamen oder persönliche Daten.

```bash
graperoot --no-telemetry    # disable
graperoot --telemetry       # re-enable
```

---

## GrapeRoot Pro

[GrapeRoot Pro](https://graperoot.dev/graperoot-pro) bietet erweiterte Funktionen für anspruchsvolle Nutzer:

- **Exhaustiver Aufgabenmodus** — Tiefgehende Mehrfachdatei-Analyse für komplexe Refaktorierungen
- **Erkennung toter Exporte** — Findet ungenutzte Exporte im gesamten Codebase
- **Abhängigkeitskreis-Finder** — Erkennt zirkuläre Importketten
- **Codebase-übergreifende Suche** — Semantische Suche über mehrere Repositories hinweg
- **Undo-Schutzschild** — Pre-Tool-Use-Hooks, die destruktive Operationen absichern

---

## Fehlerbehebung

### „MCP Server Connection Failed"

Verwende immer `dgc` statt direkt `claude`. `dgc` startet den MCP-Server automatisch.

```bash
# Fix:
claude mcp remove dual-graph
dgc   # re-registers everything
```

### Vollständiger Fehlerbehebungsleitfaden

Siehe [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) oder [graperoot.dev/docs](https://graperoot.dev/docs).

---

## Mitwirken

Die Startskripte (`bin/`) sind quelloffen unter Apache 2.0. Pull Requests sind willkommen — Fehlerbehebungen, Unterstützung neuer KI-Assistenten, Verbesserungen bei der Installation, Dokumentation.

**Hinweis:** Die Graph-Engine (`graperoot` PyPI-Paket) ist proprietär. Die Startskripte und Tools in diesem Repository sind vollständig quelloffen.

---

## Community

Hast du eine Frage, einen Fehler gefunden oder möchtest Feedback teilen?

**[Tritt dem Discord bei →](https://discord.com/invite/YwKdQATY2d)**

---

## Star-Verlauf

<a href="https://star-history.dera.page/#kunal12203/GrapeRoot&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
 </picture>
</a>

---

## Lizenz

Startskripte und Tools in diesem Repository: [Apache License 2.0](./LICENSE)

Die `graperoot` Graph-Engine (PyPI): proprietär. Siehe [graperoot.dev/graperoot-pro](https://graperoot.dev/graperoot-pro).

---

<div align="center">

Made with ❤️ · [graperoot.dev](https://graperoot.dev) · [Discord](https://discord.com/invite/YwKdQATY2d)

</div>
