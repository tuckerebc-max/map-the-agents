
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

WebCode 是一个在线 AI 全能工作平台，通过 Web 浏览器远程控制各种 AI CLI 助手，支持编程、文档处理、需求分析、报告撰写等全方位工作场景。

- **技术栈**: .NET 10.0 Blazor Server + Tailwind CSS + SqlSugar ORM
- **AI 工具**: Claude Code CLI、Codex CLI、OpenCode CLI
- **架构模式**: 领域驱动设计 (DDD) + 模块化服务注册

## 项目结构

```
WebCode/
├── WebCodeCli/              # 主应用程序（Blazor Server）
│   ├── Pages/               # Blazor 页面
│   │   ├── CodeAssistant.razor/.cs    # 桌面端主界面
│   │   ├── CodeAssistantMobile.razor/.cs # 移动端界面
│   │   └── Setup.razor      # 初始化设置向导
│   ├── Components/          # 可重用 Blazor 组件
│   ├── Controllers/         # API 控制器
│   ├── wwwroot/             # 静态资源
│   └── Program.cs           # 应用入口点
│
├── WebCodeCli.Domain/       # 领域层（DDD）
│   ├── Common/
│   │   ├── Extensions/      # 服务注册扩展
│   │   ├── Options/         # 配置选项类
│   │   └── Map/             # AutoMapper 配置
│   ├── Domain/
│   │   ├── Model/           # 领域模型
│   │   ├── Service/         # 领域服务
│   │   │   ├── Adapters/    # CLI 工具适配器
│   │   │   └── Channels/    # 飞书渠道服务
│   │   └── Exceptions/      # 自定义异常
│   └── Repositories/        # 数据仓储（SqlSugar）
│
├── docs/                     # 技术文档
├── cli/                      # CLI 工具文档
└── docker/                   # Docker 部署配置
```

## 常用命令

### 构建和运行

```bash
# 恢复 NuGet 包
dotnet restore

# 构建解决方案
dotnet build WebCodeCli.sln

# 运行应用（开发模式）
dotnet run --project WebCodeCli

# 发布应用
dotnet publish WebCodeCli.sln -c Release -o publish
```

### Docker 部署

```bash
# 一键启动
docker compose up -d

# 构建镜像
docker build -t webcodecli:latest .

# 查看日志
docker logs webcodecli
```

### Tailwind CSS 构建

```bash
cd WebCodeCli
npm install
npm run build:css
```

## 核心架构模式

### 服务注册模式

使用自定义 `[ServiceDescription]` 属性自动注册服务：

```csharp
[ServiceDescription(Lifetime = ServiceLifetime.Singleton)]
public class MyService : IMyService { ... }

// 在 Program.cs 中自动发现
builder.Services.AddServicesFromAssemblies("WebCodeCli", "WebCodeCli.Domain");
```

### CLI 适配器模式

在 `WebCodeCli.Domain/Domain/Service/Adapters/` 目录下添加新的 AI CLI 工具适配器。

### 后台服务模式

飞书渠道服务等继承自 `BackgroundService`，在应用启动时自动运行。

### 命令自动扫描模式

飞书命令服务会自动扫描全局技能、项目技能和插件目录下的Markdown文档，自动生成可用命令列表：
- 扫描目录：`skills/`（全局）、`.claude/skills/`（项目）、`plugins/`（插件）
- 支持的文档格式：`SKILL.md`、`COMMAND.md`、`*.command.md`、`README.md`
- 自动解析YAML Front Matter和Markdown内容，提取命令名称、描述、用法等信息
- 支持 `/feishuhelp` 命令手动刷新命令列表

## 关键文件

| 文件路径 | 说明 |
|---------|------|
| `WebCodeCli/Program.cs` | 应用入口点，服务配置 |
| `WebCodeCli/appsettings.json` | 应用配置文件 |
| `WebCodeCli/Pages/CodeAssistant.razor.cs` | 桌面端主界面逻辑（2000+ 行）|
| `WebCodeCli.Domain/Domain/Service/CliExecutorService.cs` | CLI 工具执行服务（核心引擎）|
| `WebCodeCli.Domain/Domain/Service/Channels/FeishuChannelService.cs` | 飞书渠道服务 |
| `WebCodeCli.Domain/Domain/Service/Channels/FeishuCommandService.cs` | 飞书命令管理服务（自动扫描技能/插件命令）|
| `WebCodeCli.Domain/Domain/Service/Channels/FeishuHelpCardBuilder.cs` | 飞书帮助卡片构建服务 |

## 开发约定

- 使用中文注释
- 服务通过 `[ServiceDescription]` 属性自动注册
- 配置通过 `IOptions&lt;T&gt;` 模式访问
- 每个会话有独立的临时工作目录

### 飞书命令开发约定

创建新命令只需在对应目录下添加Markdown文档即可，无需修改代码：
1. 全局技能：`skills/{技能名}/SKILL.md`
2. 项目技能：`.claude/skills/{技能名}/SKILL.md`
3. 插件命令：`plugins/{插件名}/COMMAND.md`

文档格式要求：
```markdown
---
name: "/命令名"
description: "命令功能描述"
usage: "/命令名 [参数]"
official: true
---
# 命令名称

命令详细说明...

## 示例
```bash
/命令名 参数
```
```
