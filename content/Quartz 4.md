---
title: Quartz 4
draft: false
permalink: quartz-4
tags:
    - Tools
    - Note-Taking
description: Quartz 4 是一个基于 Hugo 的静态站点生成器，专门为 Obsidian 设计，能够生成 Graph View 和 Backlinks。
---

> [!abstract]
> Quartz 4 是一个基于 [[Hugo]] 的静态站点生成器，专门为 [[Obsidian]] 设计，能够生成 Graph View 和 Backlinks。
> 
> 例子可以在 [主页](https://quartz.jzhao.xyz/) 找到。

---

### 常用 References

- [Callouts | 高亮块](https://quartz.jzhao.xyz/features/callouts)


---

### 一些配置记录

#### 直引号被自动转换为弯引号

这是 [GitHubFlavoredMarkdown](https://quartz.jzhao.xyz/plugins/GitHubFlavoredMarkdown) 插件的默认行为。将 `quartz.config.ts` 中的 `Plugin.GitHubFlavoredMarkdown()` 改为 `Plugin.GitHubFlavoredMarkdown({ enableSmartyPants: false })` 即可关闭。
