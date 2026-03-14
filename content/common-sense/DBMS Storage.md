---
tags:
  - 领域常识
  - 数据库系统
permalink:
aliases:
---
- disk based architecture：我们假设数据库存储在非易失性存储上，DBMS 需要有组件管理磁盘和内存之间的数据交换。
	- Volatile: CPU Registers, CPU Caches, DRAM. Random Access (Byte-Addressable)
	- Non-Volatile: SSD, HDD, Network Storage (S3, etc.). Sequencial Access (Block-Addressable)
	- 本课程中，我们称 DRAM 为 memory，其上层统称为 CPU，下层统称为 Disk。

![[Pasted image 20251014221851.png]]

易失性存储上，Random Access 几乎总是比 Sequential Access 慢。所以 DBMS 要最大化 Sequential Access。