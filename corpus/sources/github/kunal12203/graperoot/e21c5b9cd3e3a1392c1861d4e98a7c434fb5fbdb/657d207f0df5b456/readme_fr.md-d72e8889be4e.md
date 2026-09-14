<div align="center">

```
 ▄▀▀▀ █▀▀▄ ▄▀▀▄ █▀▀█ █▀▀▀ █▀▀▄ ▄▀▀▄ ▄▀▀▄ ▀█▀
 █ ▀▄ █▄▄▀ █▄▄█ █▄▄█ █▀▀  █▄▄▀ █  █ █  █  █
 ▀▀▀▀ ▀ ▀▀ ▀  ▀ █    ▀▀▀▀ ▀ ▀▀ ▀▀▀▀ ▀▀▀▀  ▀
```

### Contexte cumulatif pour les assistants de programmation IA

**[graperoot.dev](https://graperoot.dev)** · [Docs](https://graperoot.dev/docs) · [Benchmarks](https://graperoot.dev/benchmarks) · [Pro](https://graperoot.dev/graperoot-pro) · [Discord](https://discord.com/invite/YwKdQATY2d)

[![PyPI](https://img.shields.io/pypi/v/graperoot?label=version&color=brightgreen)](https://pypi.org/project/graperoot/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](#install)
[![Discord](https://img.shields.io/badge/Discord-community-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/YwKdQATY2d)
[![Stars](https://img.shields.io/github/stars/kunal12203/Codex-CLI-Compact?style=social)](https://github.com/kunal12203/Codex-CLI-Compact/stargazers)

---

🌐 **Lire dans votre langue :**
[English](../README.md) · [中文](./README_zh-CN.md) · [Español](./README_es.md) · [हिंदी](./README_hi.md) · [Français](./README_fr.md) · [Deutsch](./README_de.md) · [日本語](./README_ja.md) · [한국어](./README_ko.md) · [Português](./README_pt-BR.md) · [Русский](./README_ru.md) · [العربية](./README_ar.md) · [Türkçe](./README_tr.md) · [Bahasa Indonesia](./README_id.md)

</div>

---

## Qu'est-ce que GrapeRoot ?

GrapeRoot est un **moteur de contexte** open-source qui s'intercale entre vous et votre assistant de programmation IA. Il construit un graphe sémantique de votre base de code — fichiers, symboles, imports, chaînes d'appels — et précharge exactement le bon code dans chaque prompt avant que votre IA ne le voie.

Résultat : votre IA dépense ses tokens à **raisonner**, pas à explorer.

```
Vous exécutez : dgc /chemin/vers/projet
                    ↓
1. Projet analysé → graphe sémantique construit (fichiers, symboles, imports)
2. Vous posez une question
3. Le graphe identifie les fichiers pertinents → les intègre dans le contexte
4. L'IA reçoit votre question + le bon code déjà chargé
5. Moins de tours, moins de tokens, de meilleures réponses
```

Les économies de tokens se **cumulent** tout au long d'une session. Le graphe se souvient des fichiers lus, modifiés et interrogés — chaque tour devient moins coûteux.

---

## Résultats

Évalué sur plusieurs bases de code réelles (plus de 7 700 fichiers) et plus de 50 prompts d'ingénierie :

| Métrique | Sans GrapeRoot | Avec GrapeRoot |
|----------|:--------------:|:--------------:|
| Coût par prompt | $0.49 | **$0.27** |
| Tours moyens par tâche | 11.7 | **3.5** |
| Temps de réponse moyen | 172s | **124s** |
| Qualité (évaluée) | 76.6 / 100 | **86.6 / 100** |
| Taux de victoire sur les coûts | — | **10 prompts sur 10** |

### Réduction des coûts par type de tâche

| Type de tâche | Réduction du coût |
|---------------|:-----------------:|
| Migration et conception d'architecture | **jusqu'à 81%** |
| Analyse des performances | **jusqu'à 80%** |
| Tests et génération de tests | **jusqu'à 76%** |
| Débogage full-stack | **jusqu'à 73%** |
| Développement de fonctionnalités | **jusqu'à 71%** |
| Explication et audit de code | **jusqu'à 55%** |
| Grande base de code (7k+ fichiers, moy.) | **43% en moyenne** |

> Les économies se **cumulent** tout au long d'une session — un token évité au tour 3 évite également la refacturation du cache à chaque tour suivant. La qualité reste égale ou s'améliore pour chaque type de tâche ci-dessus.

Méthodologie complète et résultats des benchmarks : [graperoot.dev/benchmarks](https://graperoot.dev/benchmarks)

---

## Outils IA pris en charge

| Outil | Commande | Statut |
|-------|----------|--------|
| Claude Code | `dgc` | ✅ Support complet |
| OpenAI Codex CLI | `dg` | ✅ Support complet |
| Cursor | `graperoot . --cursor` | ✅ Support complet |
| Gemini CLI | `graperoot . --gemini` | ✅ Support complet |
| OpenCode | `graperoot . --opencode` / `dgo` | ✅ Support complet |
| GitHub Copilot | `graperoot . --copilot` | ✅ Support complet |
| OpenClaw | `graperoot . --openclaw` | ✅ Support complet |
| Kilocode | `graperoot . --kilocode` | ✅ Support complet |
| MiMo Code | `graperoot . --mimocode` | ✅ Support complet |
| Antigravity | `graperoot . --antigravity` | ✅ Support complet |

---

## Langages pris en charge

TypeScript · JavaScript · Python · Go · Swift · Rust · Java · Kotlin · Scala · C# · Ruby · PHP

---

## Installation

**macOS / Linux :**
```bash
curl -sSL https://raw.githubusercontent.com/kunal12203/Codex-CLI-Compact/main/install.sh | bash
source ~/.zshrc   # ou ~/.bashrc / ~/.profile
```

**Windows (PowerShell) :**
```powershell
irm https://raw.githubusercontent.com/kunal12203/Codex-CLI-Compact/main/install.ps1 | iex
```

**Windows (Scoop) :**
```powershell
scoop bucket add dual-graph https://github.com/kunal12203/scoop-dual-graph
scoop install dual-graph
```

> **Prérequis :** Python 3.10+, Node.js 18+, et l'un des outils IA pris en charge. L'installateur détecte les outils manquants et propose de les installer automatiquement.

---

## Utilisation

> **Important :** Utilisez toujours `dgc` (et non `claude` directement) pour vous assurer que le serveur MCP est en cours d'exécution.

### Claude Code

```bash
dgc                                      # analyser le répertoire courant, lancer Claude
dgc /path/to/project                     # analyser un projet spécifique
dgc /path/to/project "fix the login bug" # démarrer avec un prompt
```

### OpenAI Codex CLI

```bash
dg                              # analyser le répertoire courant
dg /path/to/project             # analyser un projet spécifique
dg /path/to/project "add tests" # démarrer avec un prompt
```

### Sélecteur interactif (nouveau dans v3.9.99)

```bash
graperoot          # affiche la confirmation du répertoire + sélecteur d'outils avec flèches
graperoot .        # idem, à partir du répertoire courant
graperoot --version   # afficher la version actuelle
graperoot --update    # forcer la mise à jour automatique
```

### Tous les outils via `graperoot`

```bash
graperoot . --cursor          # Cursor
graperoot . --gemini          # Gemini CLI
graperoot . --opencode        # OpenCode
graperoot . --copilot         # GitHub Copilot
graperoot . --openclaw        # OpenClaw
graperoot . --kilocode        # Kilocode
graperoot . --mimocode        # MiMo Code
graperoot /path --gemini "add tests"   # projet spécifique + prompt
```

### Windows

```powershell
dgc .                          # depuis l'intérieur du répertoire du projet
dgc "D:\projects\my-app"       # n'importe quel lecteur, n'importe quel chemin
dg "C:\work\backend"           # Codex CLI
dgc --gemini "D:\projects\app" # Gemini CLI sur Windows
```

---

## Comment ça fonctionne

1. **Analyse du graphe** — au premier lancement, GrapeRoot extrait les fichiers, fonctions, classes et relations d'import dans un graphe local stocké dans `.dual-graph/`.
2. **Récupération du contexte** — à chaque question, le graphe classe les fichiers les plus pertinents et les intègre dans le prompt avant que votre IA ne le voie.
3. **Mémoire de session** — les fichiers que vous avez lus, modifiés ou interrogés sont pondérés plus fortement dans les tours suivants. Le contexte se cumule.
4. **Outils MCP** — votre IA peut encore approfondir l'analyse via des outils tenant compte du graphe (`graph_read`, `graph_retrieve`, `graph_neighbors`) lorsqu'elle a besoin d'explorer davantage.

Tout le traitement est **local**. Aucun code ne quitte votre machine.

---

## Données et fichiers

Toutes les données se trouvent dans `<projet>/.dual-graph/` (ajouté automatiquement à `.gitignore`) :

| Fichier | Description |
|---------|-------------|
| `info_graph.json` | Graphe sémantique : fichiers, symboles, arêtes |
| `chat_action_graph.json` | Mémoire de session : lectures, modifications, requêtes |
| `context-store.json` | Décisions, tâches et faits persistants entre les sessions |

Installation globale dans `~/.dual-graph/` :

| Fichier | Description |
|---------|-------------|
| `dgc.ps1` / `dg.ps1` | Scripts de lancement (mis à jour automatiquement) |
| `venv/` | Environnement virtuel Python |
| `version.txt` | Version installée |

---

## Configuration

Tout est optionnel, via des variables d'environnement :

| Variable | Défaut | Description |
|----------|--------|-------------|
| `DG_HARD_MAX_READ_CHARS` | `4000` | Nombre maximum de caractères par lecture de fichier |
| `DG_TURN_READ_BUDGET_CHARS` | `18000` | Budget total de lecture par tour |
| `DG_FALLBACK_MAX_CALLS_PER_TURN` | `1` | Nombre maximum d'appels grep de secours par tour |
| `DG_RETRIEVE_CACHE_TTL_SEC` | `900` | Durée de vie du cache de récupération (15 min) |
| `DG_MCP_PORT` | auto (8080–8099) | Forcer un port spécifique pour le serveur MCP |

---

## Mise à jour automatique

Le lanceur vérifie les mises à jour à chaque exécution et se met à jour silencieusement. Pour forcer une mise à jour :
```bash
graperoot --update
```

Pour désactiver la mise à jour automatique :
```bash
graperoot --no-auto-update
```

Pour la réactiver :
```bash
graperoot --auto-update
```

Version actuelle : **3.10.16**

---

## Télémétrie

GrapeRoot collecte des rapports de plantage anonymes pour aider à corriger les bugs. Ce qui est envoyé : type d'erreur, quelle étape a échoué, version OS/Python, version de GrapeRoot. Jamais envoyé : votre code, chemins de fichiers, noms de projet, ni données personnelles.

```bash
graperoot --no-telemetry    # disable
graperoot --telemetry       # re-enable
```

---

## GrapeRoot Pro

[GrapeRoot Pro](https://graperoot.dev/graperoot-pro) ajoute des fonctionnalités avancées pour les utilisateurs expérimentés :

- **Mode tâche exhaustif** — analyse approfondie multi-fichiers pour les refactorisations complexes
- **Détection des exports morts** — repérer les exports inutilisés dans toute la base de code
- **Détecteur de cycles de dépendances** — détecter les chaînes d'imports circulaires
- **Recherche inter-bases de code** — recherche sémantique sur plusieurs dépôts
- **Bouclier d'annulation** — hooks pré-utilisation d'outils qui protègent les opérations destructives

---

## Dépannage

### « MCP Server Connection Failed »

Utilisez toujours `dgc` à la place de `claude` directement. `dgc` démarre le serveur MCP automatiquement.

```bash
# Correction :
claude mcp remove dual-graph
dgc   # réenregistre tout
```

### Guide de dépannage complet

Consultez [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) ou [graperoot.dev/docs](https://graperoot.dev/docs).

---

## Contribuer

Les scripts de lancement (`bin/`) sont open source sous licence Apache 2.0. Les pull requests sont les bienvenues — corrections de bugs, support de nouveaux assistants IA, améliorations de l'installation, documentation.

**Remarque :** Le moteur de graphe (`graperoot` pip package) est propriétaire. Les lanceurs et les outils de ce dépôt sont entièrement open source.

---

## Communauté

Vous avez une question, trouvé un bug, ou souhaitez partager des retours ?

**[Rejoignez le Discord →](https://discord.com/invite/YwKdQATY2d)**

---

## Historique des étoiles

<a href="https://star-history.dera.page/#kunal12203/GrapeRoot&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
 </picture>
</a>

---

## Licence

Scripts de lancement et outils de ce dépôt : [Apache License 2.0](./LICENSE)

Le moteur de graphe `graperoot` (PyPI) : propriétaire. Voir [graperoot.dev/graperoot-pro](https://graperoot.dev/graperoot-pro).

---

<div align="center">

Made with ❤️ · [graperoot.dev](https://graperoot.dev) · [Discord](https://discord.com/invite/YwKdQATY2d)

</div>
