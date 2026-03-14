---
tags:
  - 领域常识
  - 数据库系统
permalink: data-model
aliases:
  - Data Model
---
>[!abstract]
> 在数据库系统的语境下，Data Model 是描述数据、数据之间关系及其操作语义的抽象框架，是 [[数据库系统|DBMS]] 组织与访问数据的设计蓝图。
> 
> 例如我们熟悉的 [[MySQL]] 采用关系模型 (Relational Model)，所以它是一种 [[Relational DBMS|关系型数据库]]；而 [[Redis]] 使用 Key-Value Model，是一种 Key-Value Database。

常见类型：
- 在 [[Database]] 一文的例子中，我们使用 [[CSV]] 存储数据，属于 Flat Model。
- 大多数 DBMS 使用 Relational Model，这也是 [[数据库系统]] 课程讨论的重点。
- Key-Value Model 用于一些简单的应用或者用于缓存。它们类似于编程语言中的 map / dict，但 Key-Value DBMS 通常能够发挥 DBMS 提供的其他能力，例如并发、性能、远程访问等。
- Graph Model, Document Model, Wide Column Model 等和 K-V Model 一样，都属于 NoSQL 阵营。它们通常认为 Relational Model 的一些设计理念（例如严格的一致性）在特定应用场景下是可以放宽或有局限的，因此有了一些定制化的权衡和设计。
- 在科学计算领域，还有 Array Model，用于存放向量、矩阵、张量之类的东西。
- 另外还有更多数据模型，作为历史或未来的 DBMS 探索。