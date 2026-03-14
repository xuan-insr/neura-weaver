---
tags:
  - 领域常识
permalink:
aliases:
---
- Aggregates: `AVG`, `SUM`, `MIN`, `COUNT`, etc.
	- `SELECT AVG(gpa), COUNT(1) AS cnt FROM student WHERE login LIKE '%@cs'`
	- `%` matches 0~n any chars, `_` matches exactly 1
- `GROUP BY` & `HAVING`
- String Operations `SUBSTRING`, `UPPER`, concat
- Date & Time
- `INTO`
- Window Functions: 滑动平均、rank……
- Nested Queries
- EXPLAIN
- LATERAL joins
- WITH