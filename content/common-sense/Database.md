---
aliases:
  - Database
tags:
  - 领域常识
  - 数据库系统
permalink: database
---
> [!abstract]
> 数据库是有组织的数据集合。
> 
> Organized collection of inter-related data that models some aspect of the real-world.

## 何谓「有组织」

按照 [[CMU 15-445]] 的例子，我们考虑维护一个音乐软件的场景。我们可以以 [[CSV]] 格式维护艺人信息 `Artist(name, year, country)` 和专辑信息 `Album(name, artist, year)`:

```csv
"Wu-Tang Clan",1992,"USA"
"Notorious BIG",1992,"USA"
"GZA",1990,"USA"
```

```csv
"Enter the Wu-Tang","Wu-Tang Clan",1993
"St.Ides Mix Tape","Wu-Tang Clan",1994
"Liquid Swords","GZA",1990
```

这样，我们可以通过简单的 Python 脚本查询想要的信息，例如 GZA 的出道年份：

```python showLineNumbers
for line in file.readlines():
  record = parse(line)
  if record[0] == "GZA":
    print(int(record[1]))
```

这其实就实现了一个最基本的 Database，完成了基本的数据「组织」——可以通过可编程的手段对数据做修改和查询。    
很多人（至少我）生活中确实有很多数据是通过简单的表格形式维护的，例如账单和通讯录。

但是，上面这种组织形式会有很多问题：

- [[Integrity]]:
  - 如何保证每个 Album 的 artist 是有效的，而不会有拼写错误或简称之类的问题？
  - 如果某个 Artist 的 year 不是合法数字，那上面 Python 代码的 line 4 会抛异常。
- Implementation:
  - 找到特定记录，需要遍历整个文件。在数据库很大的时候速度会很慢。
  - 每次更改查询都要重新写代码。如果要用同样的数据库开发另一个应用，那就要重新写一遍。换言之，数据没有合理的 [[抽象]]。
  - 如果这个文件在另一个机器上怎么办？
  - 如果有两个线程要同时写入怎么办？
- [[Durability]]:
  - 如果更新一条记录的时候机器挂了怎么办？
  - 如果我们想让文件能在多台机器上冗余，从而在一个挂掉的时候还能用其他的 ([[高可用]]) 或者实现 [[负载均衡]]，怎么做？

上述问题就是一个现代的 [[数据库系统]] 要解决的问题。
