---
tags:
  - 领域常识
  - 数据库系统
permalink: data-manipulation-language
aliases:
  - DML
---

> [!abstract]
> Data Manipulation Language (DML) 是 DBMS 暴露给应用程序的、用于从 database 中存储和获取数据的 API。

DML 分为两种：

- 过程式的：The query specifies the (high-level) strategy to find the desired result.
  - 在 [[Relational Model]] 中，对应 [[Relational Algebra]]
- 声明式的：The query specifies only what data is wanted and not how to find it.
  - 这需要强大的 query optimizer 来优化查询计划。
  - 在 [[Relational Model]] 中，对应 [[Relational Calculus]]，这不是 [[CMU 15-445]] 课程讨论的重点。

See Also: [[Data Definition Language]] & [[Data Control Language]]