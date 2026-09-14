<div align="center">

```
 ▄▀▀▀ █▀▀▄ ▄▀▀▄ █▀▀█ █▀▀▀ █▀▀▄ ▄▀▀▄ ▄▀▀▄ ▀█▀
 █ ▀▄ █▄▄▀ █▄▄█ █▄▄█ █▀▀  █▄▄▀ █  █ █  █  █
 ▀▀▀▀ ▀ ▀▀ ▀  ▀ █    ▀▀▀▀ ▀ ▀▀ ▀▀▀▀ ▀▀▀▀  ▀
```

### Contexto Acumulativo para Asistentes de Programación con IA

**[graperoot.dev](https://graperoot.dev)** · [Documentación](https://graperoot.dev/docs) · [Benchmarks](https://graperoot.dev/benchmarks) · [Pro](https://graperoot.dev/graperoot-pro) · [Discord](https://discord.com/invite/YwKdQATY2d)

[![PyPI](https://img.shields.io/pypi/v/graperoot?label=version&color=brightgreen)](https://pypi.org/project/graperoot/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](#install)
[![Discord](https://img.shields.io/badge/Discord-community-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/YwKdQATY2d)
[![Stars](https://img.shields.io/github/stars/kunal12203/Codex-CLI-Compact?style=social)](https://github.com/kunal12203/Codex-CLI-Compact/stargazers)

---

🌐 **Leer en tu idioma:**
[English](../README.md) · [中文](./README_zh-CN.md) · [Español](./README_es.md) · [हिंदी](./README_hi.md) · [Français](./README_fr.md) · [Deutsch](./README_de.md) · [日本語](./README_ja.md) · [한국어](./README_ko.md) · [Português](./README_pt-BR.md) · [Русский](./README_ru.md) · [العربية](./README_ar.md) · [Türkçe](./README_tr.md) · [Bahasa Indonesia](./README_id.md)

</div>

---

## ¿Qué es GrapeRoot?

GrapeRoot es un **motor de contexto** de código abierto que actúa como intermediario entre tú y tu asistente de programación con IA. Construye un grafo semántico de tu base de código — archivos, símbolos, importaciones, cadenas de llamadas — y precarga exactamente el código correcto en cada prompt antes de que lo vea tu IA.

El resultado: tu IA dedica los tokens a **razonar**, no a explorar.

```
Ejecutas: dgc /path/to/project
              ↓
1. Proyecto escaneado → grafo semántico construido (archivos, símbolos, importaciones)
2. Haces una pregunta
3. El grafo identifica los archivos relevantes → los empaqueta en el contexto
4. La IA recibe tu pregunta + el código correcto ya cargado
5. Menos turnos, menos tokens, mejores respuestas
```

El ahorro de tokens se **acumula** a lo largo de una sesión. El grafo recuerda qué archivos fueron leídos, editados y consultados — cada turno se vuelve más económico.

---

## Resultados

Evaluado en múltiples bases de código reales (más de 7,700 archivos) y más de 50 prompts de ingeniería:

| Métrica | Sin GrapeRoot | Con GrapeRoot |
|---------|:-------------:|:-------------:|
| Costo por prompt | $0.49 | **$0.27** |
| Turnos promedio por tarea | 11.7 | **3.5** |
| Tiempo de respuesta promedio | 172s | **124s** |
| Calidad (puntuada) | 76.6 / 100 | **86.6 / 100** |
| Tasa de victoria en costo | — | **10 de 10 prompts** |

### Reducción de costo por tipo de tarea

| Tipo de tarea | Reducción de costo |
|---------------|:------------------:|
| Migración y diseño de arquitectura | **hasta 81%** |
| Análisis de rendimiento | **hasta 80%** |
| Pruebas y generación de pruebas | **hasta 76%** |
| Depuración full-stack | **hasta 73%** |
| Desarrollo de funcionalidades | **hasta 71%** |
| Explicación y auditoría de código | **hasta 55%** |
| Base de código grande (7k+ archivos, promedio) | **43% de promedio** |

> Los ahorros se **acumulan** a lo largo de una sesión — un token evitado en el turno 3 también evita la refacturación de caché en cada turno posterior. La calidad se mantiene igual o mejora en cada tipo de tarea anterior.

Metodología completa y resultados del benchmark: [graperoot.dev/benchmarks](https://graperoot.dev/benchmarks)

---

## Herramientas de IA Compatibles

| Herramienta | Comando | Estado |
|-------------|---------|--------|
| Claude Code | `dgc` | ✅ Soporte completo |
| OpenAI Codex CLI | `dg` | ✅ Soporte completo |
| Cursor | `graperoot . --cursor` | ✅ Soporte completo |
| Gemini CLI | `graperoot . --gemini` | ✅ Soporte completo |
| OpenCode | `graperoot . --opencode` / `dgo` | ✅ Soporte completo |
| GitHub Copilot | `graperoot . --copilot` | ✅ Soporte completo |
| OpenClaw | `graperoot . --openclaw` | ✅ Soporte completo |
| Kilocode | `graperoot . --kilocode` | ✅ Soporte completo |
| MiMo Code | `graperoot . --mimocode` | ✅ Soporte completo |
| Antigravity | `graperoot . --antigravity` | ✅ Soporte completo |

---

## Lenguajes Compatibles

TypeScript · JavaScript · Python · Go · Swift · Rust · Java · Kotlin · Scala · C# · Ruby · PHP

---

## Instalación

**macOS / Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/kunal12203/Codex-CLI-Compact/main/install.sh | bash
source ~/.zshrc   # o ~/.bashrc / ~/.profile
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

> **Requisitos previos:** Python 3.10+, Node.js 18+, y una de las herramientas de IA compatibles. El instalador detecta las herramientas faltantes y ofrece instalarlas automáticamente.

---

## Uso

> **Importante:** Usa siempre `dgc` (no `claude` directamente) para garantizar que el servidor MCP esté en ejecución.

### Claude Code

```bash
dgc                                      # escanea el directorio actual, inicia Claude
dgc /path/to/project                     # escanea un proyecto específico
dgc /path/to/project "fix the login bug" # inicia con un prompt
```

### OpenAI Codex CLI

```bash
dg                              # escanea el directorio actual
dg /path/to/project             # escanea un proyecto específico
dg /path/to/project "add tests" # inicia con un prompt
```

### Selector Interactivo (nuevo en v3.9.99)

```bash
graperoot          # muestra confirmación del directorio + selector de herramientas con flechas
graperoot .        # igual, usa el directorio actual
graperoot --version   # muestra la versión instalada
graperoot --update    # fuerza la actualización automática
```

### Todas las Herramientas vía `graperoot`

```bash
graperoot . --cursor          # Cursor
graperoot . --gemini          # Gemini CLI
graperoot . --opencode        # OpenCode
graperoot . --copilot         # GitHub Copilot
graperoot . --openclaw        # OpenClaw
graperoot . --kilocode        # Kilocode
graperoot . --mimocode        # MiMo Code
graperoot /path --gemini "add tests"   # proyecto específico + prompt
```

### Windows

```powershell
dgc .                          # desde dentro del directorio del proyecto
dgc "D:\projects\my-app"       # cualquier unidad, cualquier ruta
dg "C:\work\backend"           # Codex CLI
dgc --gemini "D:\projects\app" # Gemini CLI en Windows
```

---

## Cómo Funciona

1. **Escaneo del grafo** — en la primera ejecución, GrapeRoot extrae archivos, funciones, clases y relaciones de importación en un grafo local almacenado en `.dual-graph/`.
2. **Recuperación de contexto** — cada vez que haces una pregunta, el grafo clasifica los archivos más relevantes y los empaqueta en el prompt antes de que tu IA lo reciba.
3. **Memoria de sesión** — los archivos que has leído, editado o consultado reciben mayor peso en los turnos futuros. El contexto se acumula.
4. **Herramientas MCP** — tu IA puede profundizar más mediante herramientas con conocimiento del grafo (`graph_read`, `graph_retrieve`, `graph_neighbors`) cuando necesita explorar.

Todo el procesamiento es **local**. Ningún código abandona tu máquina.

---

## Datos y Archivos

Todos los datos residen en `<project>/.dual-graph/` (añadido automáticamente a `.gitignore`):

| Archivo | Descripción |
|---------|-------------|
| `info_graph.json` | Grafo semántico: archivos, símbolos, aristas |
| `chat_action_graph.json` | Memoria de sesión: lecturas, ediciones, consultas |
| `context-store.json` | Decisiones, tareas y hechos persistentes entre sesiones |

Instalación global en `~/.dual-graph/`:

| Archivo | Descripción |
|---------|-------------|
| `dgc.ps1` / `dg.ps1` | Scripts de lanzamiento (actualizados automáticamente) |
| `venv/` | Entorno virtual de Python |
| `version.txt` | Versión instalada |

---

## Configuración

Todo es opcional, mediante variables de entorno:

| Variable | Valor por defecto | Descripción |
|----------|:-----------------:|-------------|
| `DG_HARD_MAX_READ_CHARS` | `4000` | Máximo de caracteres por lectura de archivo |
| `DG_TURN_READ_BUDGET_CHARS` | `18000` | Presupuesto total de lectura por turno |
| `DG_FALLBACK_MAX_CALLS_PER_TURN` | `1` | Máximo de llamadas grep de respaldo por turno |
| `DG_RETRIEVE_CACHE_TTL_SEC` | `900` | TTL de caché de recuperación (15 min) |
| `DG_MCP_PORT` | auto (8080–8099) | Fuerza un puerto específico para el servidor MCP |

---

## Actualización Automática

El lanzador verifica actualizaciones en cada ejecución y se actualiza silenciosamente. Para forzar una actualización:
```bash
graperoot --update
```

Para desactivar la actualización automática:
```bash
graperoot --no-auto-update
```

Para reactivarla:
```bash
graperoot --auto-update
```

Versión actual: **3.10.16**

---

## Telemetría

GrapeRoot recopila informes de fallos anónimos para ayudar a corregir errores. Lo que se envía: tipo de error, qué paso falló, versión de OS/Python, versión de GrapeRoot. Nunca se envía: tu código, rutas de archivos, nombres de proyecto ni datos personales.

```bash
graperoot --no-telemetry    # disable
graperoot --telemetry       # re-enable
```

---

## GrapeRoot Pro

[GrapeRoot Pro](https://graperoot.dev/graperoot-pro) añade funcionalidades avanzadas para usuarios expertos:

- **Modo de tarea exhaustivo** — análisis profundo de múltiples archivos para refactorizaciones complejas
- **Detección de exportaciones muertas** — encuentra exportaciones no utilizadas en toda la base de código
- **Detector de ciclos de dependencias** — detecta cadenas de importación circulares
- **Búsqueda entre bases de código** — búsqueda semántica en múltiples repositorios
- **Escudo de deshacer** — hooks previos al uso de herramientas que protegen operaciones destructivas

---

## Solución de Problemas

### "MCP Server Connection Failed"

Usa siempre `dgc` en lugar de `claude` directamente. `dgc` inicia el servidor MCP automáticamente.

```bash
# Solución:
claude mcp remove dual-graph
dgc   # vuelve a registrar todo
```

### Guía completa de solución de problemas

Consulta [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) o [graperoot.dev/docs](https://graperoot.dev/docs).

---

## Contribuir

Los scripts de lanzamiento (`bin/`) son de código abierto bajo Apache 2.0. Se aceptan pull requests — correcciones de errores, soporte para nuevos asistentes de IA, mejoras de instalación, documentación.

**Nota:** El motor de grafos (paquete pip `graperoot`) es propietario. Los lanzadores y herramientas de este repositorio son completamente de código abierto.

---

## Comunidad

¿Tienes una pregunta, encontraste un error o quieres compartir tus comentarios?

**[Únete al Discord →](https://discord.com/invite/YwKdQATY2d)**

---

## Historial de Estrellas

<a href="https://star-history.dera.page/#kunal12203/GrapeRoot&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
 </picture>
</a>

---

## Licencia

Scripts de lanzamiento y herramientas en este repositorio: [Apache License 2.0](../LICENSE)

El motor de grafos `graperoot` (PyPI): propietario. Consulta [graperoot.dev/graperoot-pro](https://graperoot.dev/graperoot-pro).

---

<div align="center">

Hecho con ❤️ · [graperoot.dev](https://graperoot.dev) · [Discord](https://discord.com/invite/YwKdQATY2d)

</div>
