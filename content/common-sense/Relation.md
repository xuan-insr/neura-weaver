---
tags:
  - 领域常识
  - 集合论
permalink: relation
aliases:
  - 关系
---
> [!abstract]
> 关系是各个对象之间的联系和对应。采用 二元组 或 多元组 的集合来表示关系。
> 
> 例如学生 - 班级 - 学院这三组对象的隶属关系：
> 
> $R = \{<\text{咸鱼暄}, 1915, \text{计算机学院}>, <\text{xx}, 1902, \text{生工食品学院}>, ...\}$

如果 $R$ 是 $A_1 \times A_2 \times ... \times A_n$ 的一个子集，则称其为集合 $A_1 \times A_2 \times ... \times A_{n-1}$ 到 $A_n$ 的 n 元关系。
- 特别地，当 $A_i = A$ (i = 1, 2, ..., n) 时，也称 $R$ 为 $A$ 上的 n 元关系。

## 二元关系

二元关系是 n 元关系的一种特殊情况，即 $n = 2$。

例如，$R$ 是 $A \times B$ 的一个子集，则称其为 $A$ 到 $B$ 的二元关系。

又如，$R$ 是 $A \times A$ 的一个子集，则称其为 $A$ 上的二元关系。
- 举例而言，我们定义 $\mathbb{N}$ 上的整除关系 $D = \{<x, y> | x \text{ 整除 } y\}$，那么 $<2, 4> \in D$，而 $<3, 5>\notin D$。

### 记号

- 用 $xRy$ 表示 $<x, y> \in R$
- 用 $\neg xRy$ 表示 $<x, y> \notin R$

### 域

- $R$ 的定义域（domain）：$\text{Dom}(R) = \{x | x \in A \land \exists y (xRy)\}$
- $R$ 的值域（range）：$\text{Ran}(R) = \{y | y \in B \land \exists x (xRy)\}$

称 $A$ 为 $R$ 的前域，$B$ 为 $R$ 的陪域。

### 关系的归纳法定义

关系也可以通过归纳法定义。例如 $\mathbb{N}$ 上的小于关系 $L$ 可以定义为：
1. 基础条款：$<0, 1> \in L$
2. 归纳条款：如果 $<x, y> \in L$，则 $<x, y+1> \in L$，$<x+1, y+1> \in L$
3. 终极条款：除了上述两个条款包含的元素，其他元素均不属于 $L$。
