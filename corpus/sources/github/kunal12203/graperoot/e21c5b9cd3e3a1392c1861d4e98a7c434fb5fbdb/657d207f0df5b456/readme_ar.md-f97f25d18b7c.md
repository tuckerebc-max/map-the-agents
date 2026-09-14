<div align="center">

```
 ▄▀▀▀ █▀▀▄ ▄▀▀▄ █▀▀█ █▀▀▀ █▀▀▄ ▄▀▀▄ ▄▀▀▄ ▀█▀
 █ ▀▄ █▄▄▀ █▄▄█ █▄▄█ █▀▀  █▄▄▀ █  █ █  █  █
 ▀▀▀▀ ▀ ▀▀ ▀  ▀ █    ▀▀▀▀ ▀ ▀▀ ▀▀▀▀ ▀▀▀▀  ▀
```

### محرك سياق تراكمي لمساعدي البرمجة بالذكاء الاصطناعي

**[graperoot.dev](https://graperoot.dev)** · [Docs](https://graperoot.dev/docs) · [Benchmarks](https://graperoot.dev/benchmarks) · [Pro](https://graperoot.dev/graperoot-pro) · [Discord](https://discord.com/invite/YwKdQATY2d)

[![PyPI](https://img.shields.io/pypi/v/graperoot?label=version&color=brightgreen)](https://pypi.org/project/graperoot/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](#install)
[![Discord](https://img.shields.io/badge/Discord-community-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/YwKdQATY2d)
[![Stars](https://img.shields.io/github/stars/kunal12203/Codex-CLI-Compact?style=social)](https://github.com/kunal12203/Codex-CLI-Compact/stargazers)

---

🌐 **اقرأ بلغتك:**
[English](../README.md) · [中文](./README_zh-CN.md) · [Español](./README_es.md) · [हिंदी](./README_hi.md) · [Français](./README_fr.md) · [Deutsch](./README_de.md) · [日本語](./README_ja.md) · [한국어](./README_ko.md) · [Português](./README_pt-BR.md) · [Русский](./README_ru.md) · [العربية](./README_ar.md) · [Türkçe](./README_tr.md) · [Bahasa Indonesia](./README_id.md)

</div>

---

## ما هو GrapeRoot؟

GrapeRoot هو **محرك سياق** مفتوح المصدر يعمل كحلقة وصل بينك وبين مساعد البرمجة القائم على الذكاء الاصطناعي. يبني GrapeRoot رسمًا بيانيًا دلاليًا لقاعدة الكود الخاصة بك — يشمل الملفات والرموز والاستيرادات وسلاسل الاستدعاء — ثم يحمّل الكود المناسب تمامًا في كل طلب قبل أن يراه نموذج الذكاء الاصطناعي.

النتيجة: يُنفق الذكاء الاصطناعي رصيد الرموز في **التفكير والاستدلال**، لا في الاستكشاف والبحث.

```
You run: dgc /path/to/project
              ↓
1. Project scanned → semantic graph built (files, symbols, imports)
2. You ask a question
3. Graph identifies the relevant files → packs them into context
4. AI gets your question + the right code already loaded
5. Fewer turns, fewer tokens, better answers
```

تتراكم وفورات الرموز وتتضاعف عبر الجلسة. يتذكر الرسم البياني الملفات التي قُرئت وعُدّلت واستُعلم عنها — فيصبح كل طلب أرخص من سابقه.

---

## النتائج

أُجريت المقارنات على قواعد كود حقيقية متعددة (أكثر من 7,700 ملف) وأكثر من 50 طلبًا هندسيًا:

| المقياس | بدون GrapeRoot | مع GrapeRoot |
|---------|:--------------:|:------------:|
| تكلفة الطلب الواحد | $0.49 | **$0.27** |
| متوسط الدورات لكل مهمة | 11.7 | **3.5** |
| متوسط وقت الاستجابة | 172s | **124s** |
| الجودة (بالتقييم) | 76.6 / 100 | **86.6 / 100** |
| معدل الفوز في التكلفة | — | **10 من أصل 10 طلبات** |

### تخفيض التكلفة حسب نوع المهمة

| نوع المهمة | تخفيض التكلفة |
|------------|:-------------:|
| الترحيل وتصميم البنية المعمارية | **حتى 81%** |
| تحليل الأداء | **حتى 80%** |
| الاختبار وتوليد الاختبارات | **حتى 76%** |
| تشخيص الأخطاء full-stack | **حتى 73%** |
| تطوير الميزات | **حتى 71%** |
| شرح الكود والتدقيق | **حتى 55%** |
| قاعدة كود كبيرة (7k+ ملف، المتوسط) | **43% في المتوسط** |

> تتراكم الوفورات **وتتضاعف** طوال الجلسة — فالرمز المُوفَّر في الدورة 3 يُجنّب أيضًا إعادة الفوترة للذاكرة المؤقتة في كل دورة لاحقة. تبقى الجودة مساوية أو تتحسن في كل نوع من أنواع المهام أعلاه.

المنهجية الكاملة للمقارنة والنتائج: [graperoot.dev/benchmarks](https://graperoot.dev/benchmarks)

---

## أدوات الذكاء الاصطناعي المدعومة

| الأداة | الأمر | الحالة |
|--------|-------|--------|
| Claude Code | `dgc` | ✅ دعم كامل |
| OpenAI Codex CLI | `dg` | ✅ دعم كامل |
| Cursor | `graperoot . --cursor` | ✅ دعم كامل |
| Gemini CLI | `graperoot . --gemini` | ✅ دعم كامل |
| OpenCode | `graperoot . --opencode` / `dgo` | ✅ دعم كامل |
| GitHub Copilot | `graperoot . --copilot` | ✅ دعم كامل |
| OpenClaw | `graperoot . --openclaw` | ✅ دعم كامل |
| Kilocode | `graperoot . --kilocode` | ✅ دعم كامل |
| MiMo Code | `graperoot . --mimocode` | ✅ دعم كامل |
| Antigravity | `graperoot . --antigravity` | ✅ دعم كامل |

---

## لغات البرمجة المدعومة

TypeScript · JavaScript · Python · Go · Swift · Rust · Java · Kotlin · Scala · C# · Ruby · PHP

---

## التثبيت

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

> **المتطلبات الأساسية:** Python 3.10+، وNode.js 18+، وإحدى أدوات الذكاء الاصطناعي المدعومة. يكتشف المثبّت الأدوات المفقودة ويعرض تثبيتها تلقائيًا.

---

## الاستخدام

> **مهم:** استخدم دائمًا `dgc` (وليس `claude` مباشرةً) لضمان تشغيل خادم MCP.

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

### منتقي تفاعلي (جديد في v3.9.99)

```bash
graperoot          # shows directory confirm + arrow-key tool picker
graperoot .        # same, picks from current directory
graperoot --version   # print current version
graperoot --update    # force self-update
```

### جميع الأدوات عبر `graperoot`

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

## كيف يعمل

1. **مسح الرسم البياني** — عند التشغيل الأول، يستخرج GrapeRoot الملفات والدوال والفئات وعلاقات الاستيراد إلى رسم بياني محلي مخزّن في `.dual-graph/`.
2. **استرجاع السياق** — في كل مرة تطرح فيها سؤالًا، يرتّب الرسم البياني الملفات الأكثر صلةً ويضعها في سياق الطلب قبل أن يراه الذكاء الاصطناعي.
3. **ذاكرة الجلسة** — تحظى الملفات التي قرأتَها أو عدّلتَها أو استعلمتَ عنها بأوزان أعلى في الجولات اللاحقة. يتراكم السياق ويتضاعف.
4. **أدوات MCP** — يمكن للذكاء الاصطناعي التعمّق أكثر عبر أدوات مدركة للرسم البياني (`graph_read` و`graph_retrieve` و`graph_neighbors`) حين يحتاج إلى استكشاف إضافي.

تتم جميع العمليات **محليًا**. لا يغادر أي كود جهازك.

---

## البيانات والملفات

تُخزَّن جميع البيانات في `<project>/.dual-graph/` (تُضاف تلقائيًا إلى `.gitignore`):

| الملف | الوصف |
|-------|-------|
| `info_graph.json` | الرسم البياني الدلالي: الملفات والرموز والحواف |
| `chat_action_graph.json` | ذاكرة الجلسة: القراءات والتعديلات والاستعلامات |
| `context-store.json` | القرارات والمهام والحقائق المستمرة عبر الجلسات |

التثبيت العام في `~/.dual-graph/`:

| الملف | الوصف |
|-------|-------|
| `dgc.ps1` / `dg.ps1` | نصوص التشغيل (تُحدَّث تلقائيًا) |
| `venv/` | البيئة الافتراضية لـ Python |
| `version.txt` | الإصدار المثبّت |

---

## الإعدادات

جميعها اختيارية، وتُضبط عبر متغيرات البيئة:

| المتغير | القيمة الافتراضية | الوصف |
|---------|:-----------------:|-------|
| `DG_HARD_MAX_READ_CHARS` | `4000` | الحد الأقصى للأحرف لكل قراءة ملف |
| `DG_TURN_READ_BUDGET_CHARS` | `18000` | إجمالي ميزانية القراءة لكل جولة |
| `DG_FALLBACK_MAX_CALLS_PER_TURN` | `1` | الحد الأقصى لاستدعاءات grep الاحتياطية لكل جولة |
| `DG_RETRIEVE_CACHE_TTL_SEC` | `900` | مدة صلاحية ذاكرة التخزين المؤقت للاسترجاع (15 دقيقة) |
| `DG_MCP_PORT` | auto (8080–8099) | تحديد منفذ خادم MCP يدويًا |

---

## التحديث التلقائي

يتحقق المشغّل من التحديثات عند كل تشغيل ويُحدّث نفسه بصمت. لإجبار التحديث:
```bash
graperoot --update
```

لتعطيل التحديث التلقائي:
```bash
graperoot --no-auto-update
```

لإعادة تفعيله:
```bash
graperoot --auto-update
```

الإصدار الحالي: **3.10.16**

---

## القياس عن بعد

يجمع GrapeRoot تقارير أعطال مجهولة الهوية للمساعدة في إصلاح الأخطاء. ما يُرسَل: نوع الخطأ، أي خطوة فشلت، إصدار نظام التشغيل/Python، إصدار GrapeRoot. لا يُرسَل أبدًا: الكود الخاص بك، مسارات الملفات، أسماء المشاريع، أو البيانات الشخصية.

```bash
graperoot --no-telemetry    # disable
graperoot --telemetry       # re-enable
```

---

## GrapeRoot Pro

يضيف [GrapeRoot Pro](https://graperoot.dev/graperoot-pro) ميزات متقدمة للمستخدمين المحترفين:

- **وضع المهام الشامل** — تحليل عميق متعدد الملفات لعمليات إعادة الهيكلة المعقدة
- **كشف الصادرات غير المستخدمة** — رصد الصادرات غير المُستخدَمة في قاعدة الكود بالكامل
- **كاشف دورات التبعيات** — اكتشاف سلاسل الاستيراد الدائرية
- **البحث عبر قواعد الكود** — بحث دلالي عبر مستودعات متعددة
- **درع التراجع** — خطافات ما قبل استخدام الأداة لحماية العمليات التدميرية

---

## استكشاف الأخطاء وإصلاحها

### "MCP Server Connection Failed"

استخدم دائمًا `dgc` بدلًا من `claude` مباشرةً. يشغّل `dgc` خادم MCP تلقائيًا.

```bash
# Fix:
claude mcp remove dual-graph
dgc   # re-registers everything
```

### دليل استكشاف الأخطاء الكامل

راجع [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) أو [graperoot.dev/docs](https://graperoot.dev/docs).

---

## المساهمة

نصوص المشغّل (`bin/`) مفتوحة المصدر بموجب Apache 2.0. طلبات السحب مرحّب بها — إصلاح الأخطاء، ودعم أدوات ذكاء اصطناعي جديدة، وتحسينات التثبيت، والتوثيق.

**ملاحظة:** محرك الرسم البياني (`graperoot` على pip) مملوك للشركة. أدوات التشغيل والبنية التحتية في هذا المستودع مفتوحة المصدر بالكامل.

---

## المجتمع

هل لديك سؤال، أو اكتشفت خطأً، أو تريد مشاركة ملاحظاتك؟

**[انضم إلى Discord ←](https://discord.com/invite/YwKdQATY2d)**

---

## سجل النجوم

<a href="https://star-history.dera.page/#kunal12203/GrapeRoot&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
 </picture>
</a>

---

## الترخيص

نصوص المشغّل والأدوات في هذا المستودع: [Apache License 2.0](./LICENSE)

محرك الرسم البياني `graperoot` (PyPI): مملوك للشركة. راجع [graperoot.dev/graperoot-pro](https://graperoot.dev/graperoot-pro).

---

<div align="center">

Made with ❤️ · [graperoot.dev](https://graperoot.dev) · [Discord](https://discord.com/invite/YwKdQATY2d)

</div>
