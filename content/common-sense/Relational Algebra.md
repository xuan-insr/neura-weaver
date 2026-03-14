---
tags:
  - 领域常识
  - 数据库系统
permalink: relational-algebra
aliases:
---
Relational Algebra 基于 set algebra，定义了在 relation 中获取和操作 tuples 的一些基础运算 (primitives)。

每个 operator 接受一个或多个 relation (table) 作为输入，并输出一个新的 relation。因此我们可以链式使用 operator 来做到复杂的操作。

## Operators

### Selection | 选择

选择操作从关系中选择满足特定条件的元组。

形式化地说，$\sigma_p(r) = \{t | t \in r \land p(t)\}$，即选择出 $r$ 中所有满足命题 $p$ 的元素的集合。

符号助记：$\sigma$ = sigma = s = selection

其中，谓词 $p$ 是由一系列 $\land$、$\lor$、$\neg$ 连接的命题组成的，每个命题满足形式：
- $\langle \text{attribute} \rangle \ op \ \langle \text{attribute} \rangle$ 
- $\langle \text{attribute} \rangle \ op \ \langle \text{constant} \rangle$

其中 $op$ 为 $=, \neq, >, \geq, <, \leq$ 之一。

例如：$\sigma_{\text{dept\_name} = \text{"Physics"} \land \text{salary} > 90000}(\text{instructor})$ 表示关系 $\text{instructor}$ 中 $\text{dept\_name}$ 为 "Physics" 且 $\text{salary}$ 大于 90000 的元素形成的子集。

<img src="common-sense/assets/2025-10-07-22-51-49.png" width="350"/>

### Projection | 投影

投影操作从关系中选择特定的属性列，并可以重新处理属性顺序、去除不想要的属性、根据属性做操作得到新的属性。

例如：$\pi_{\text{name}, \text{salary}*2}(\text{instructor})$ 表示从教师关系中选择姓名属性，并计算工资属性的两倍作为新的属性。

符号助记：$\pi$ = pi = p = projection

<img src="common-sense/assets/2025-10-07-23-01-45.png" width="350"/>

### Union | 并

并操作将两个关系合并，返回包含两个关系中所有元组的新关系。

形式化地说，$r \cup s = \{t | t \in r \lor t \in s\}$，即包含 $r$ 和 $s$ 中所有元组的集合。

**要求**：$r$ 和 $s$ 必须是**并相容**的（union-compatible），即：
- 两个关系具有相同的属性数量
- 对应位置的属性具有相同的域（domain）

例如：$\text{instructor} \cup \text{student}$ 表示所有教师和学生的并集。

### Intersection | 交

交操作返回两个关系中共有的元组。

形式化地说，$r \cap s = \{t | t \in r \land t \in s\}$，即同时属于 $r$ 和 $s$ 的元组集合。

**要求**：$r$ 和 $s$ 必须是并相容的。

例如：$\text{instructor} \cap \text{student}$ 表示既是教师又是学生的元组。

### Difference | 差

差操作返回属于第一个关系但不属于第二个关系的元组。

形式化地说，$r - s = \{t | t \in r \land t \notin s\}$，即属于 $r$ 但不属于 $s$ 的元组集合。

**要求**：$r$ 和 $s$ 必须是并相容的。

例如：$\text{instructor} - \text{student}$ 表示是教师但不是学生的元组。

### Cartesian Product | 笛卡尔积

笛卡尔积操作将两个关系的元组进行组合，生成所有可能的元组对。

形式化地说，$r \times s = \{t \cdot q | t \in r \land q \in s\}$，其中 $t \cdot q$ 表示元组 $t$ 和 $q$ 的连接。

结果关系的模式是 $r$ 和 $s$ 模式的并集，属性名可能冲突时需要重命名。

例如：$\text{instructor} \times \text{department}$ 表示教师和部门的所有可能组合。

### Join | 连接

连接操作是笛卡尔积和选择的组合，用于根据特定条件连接两个关系。

#### Natural Join | 自然连接

自然连接 $\bowtie$ 自动连接具有相同属性名的元组，并消除重复属性。

形式化地说，$r \bowtie s = \pi_{R \cup S}(\sigma_{r.A_1 = s.A_1 \land \cdots \land r.A_n = s.A_n}(r \times s))$，其中 $A_1, \ldots, A_n$ 是 $r$ 和 $s$ 的共同属性。

#### Theta Join | θ连接

θ连接 $\bowtie_\theta$ 根据条件 $\theta$ 连接两个关系。

形式化地说，$r \bowtie_\theta s = \sigma_\theta(r \times s)$，其中 $\theta$ 是连接条件。

#### Equijoin | 等值连接

等值连接是 θ连接的特例，其中连接条件只包含等号比较。

例如：$\text{instructor} \bowtie_{\text{instructor.dept\_name} = \text{department.dept\_name}} \text{department}$ 表示根据部门名称连接教师和部门信息。

