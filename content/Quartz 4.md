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

#### Graph View 显示所有文件，而非只显示存在的文件

这涉及源码修改。具体来说，可以参看 [这里 (private repo)](https://github.com/xuan-insr/neura-weaver-private/commit/faa2a1bef5111aee0f69deb94ccc4355c8f65a15) 或 [这里 (public repo)](https://github.com/xuan-insr/neura-weaver/commit/cbe2802f67251d4d0a69240e3779b097d376bb97#diff-3f470d834cc1eecd85858c4b6c2833fbc5874d8ea531bccfe9d10fcd5a0ae4a6)。

更优雅的做法是把它弄成一个配置。但我懒。
