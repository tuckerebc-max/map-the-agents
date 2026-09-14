# Host Runtime Validation

> Maintainer-only reference. End users should start from `docs/HOST_USAGE_GUIDE.md` and the generated `host-onboard-smoke-*.md` report instead of learning runtime validation commands first.

这份文档定义的是 host runtime validation 的最小验收面。

目标不是只确认配置生成了，而是确认宿主真的会按协议执行：

- 先进入 `research`
- 先读本地知识和缓存产物
- 先产出三份核心文档
- 必须在文档确认之后再继续后续阶段

## 最小检查项

1. 触发词是否与当前宿主一致
2. 首次响应是否明确声明当前阶段是 `research`
3. 是否明确承诺三文档后暂停等待确认
4. 是否在文档确认后才进入 Spec / coding
5. 是否在质量返工后要求重新执行 review 与 release 验证

## 维护者入口

普通用户不需要先学会一组 runtime validation CLI。默认路径是：

1. 先运行 `super-dev` 完成宿主接入
2. 回到宿主里触发 `/super-dev ...`
3. 让宿主真实进入 `research -> 三文档 -> 等待确认`

只有维护者在排障或补正式验收证据时，才需要进入 `doctor / integrate / review` 这条维护链。

## 产物

建议保留以下运行时证据：

- `output/*-host-surface-audit.md`
- `output/*-host-surface-audit.json`
- `.super-dev/review-state/host-runtime-validation.json`

如果没有这些证据，说明 host runtime validation 仍然不完整。
