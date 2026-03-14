---
tags:
  - 领域常识
  - 数据库系统
permalink:
aliases:
---
我们希望能将 schema 设计成没有非必要的冗余、同时获取数据也相对简单的样子。历史上的好事之人总结了不少范式 (normal form)。

### 问题

假如我们有一个大学的数据库，形如：`instructor_dept(ID, name, salary, dept_name, building, budget)`，其中存储导师的 ID、姓名、工资、学院名、学院办公楼、学院预算。

容易看到，学院的地点和预算在每个教师记录中重复，这容易引发一致性问题或者提高更新的复杂度。当一个系没有老师时，无法创建这个系。当一个系的最后一个老师被删除时，这个系的信息丢失。

符合直觉的是，将这个关系分解 (decompose) 成更小的关系，可以解决上面的问题：
`instructor(ID, name, salary, dept_name)` + `department(dept_name, building, budget)`。

但是，分解并不总是好的。举个例子，TODO

#### 函数依赖 (Functional Dependencies)

如果关系 r 中，对于任意两个元组 t₁ 和 t₂，只要它们在属性集 α 上的值相同，则它们在属性集 β 上的值也必然相同，我们就说 α → β（α 函数决定 β，或者说 β 函数依赖 α）。

这表示一种语义。例如，给定 instructor ID，我们能唯一确定他的 name, salary 和 dept_name。但是给定 name 或者 salary，不一定能唯一确定一个 ID。

α 是一个属性集，意味着其中可能有多个属性。举例而言，对于 `选课(学生ID, 课程ID, 成绩)` 来说，我们有 `(学生ID, 课程ID) -> 成绩`。`(学生ID, 课程ID)` 的任意一个真子集都不能唯一确定成绩，此时我们称 成绩 **完全函数依赖**于 `(学生ID, 课程ID)`。否则，例如 `(ID, name) -> (salary, dept_name)`，但 `ID -> (salary, dept_name)`，则我们称 `(salary, dept_name)` **部分函数依赖**于 `(ID, name)`。

结合 [[Relational Model#Keys]]，容易理解，对于一个关系，所有属性完全函数依赖于关系的候选码，函数依赖于关系的超码。



### 范式

#### 第一范式 | 1NF

第一范式要求很简单，即所有属性的域都是 atomic 的。

也就是说，不应该有这样的 `phone_numbers` 是集合的情况: `instructor(ID, name, {phone_numbers})`。这样的情况应该被分解为 `instructor(ID, name)` + `instructor_phone(ID, phone_number)`。

#### 第二范式 | 2NF：消除部分依赖

给定一个关系 r，在其所有候选键中出现的所有属性 定义为 主属性。
举例而言，`选课(学生ID, 课程ID, 成绩)` 中 `(学生ID, 课程ID)` 是唯一候选码，这两个属性是主属性。
再举个例子，`学生(学号, 身份证号, 姓名)` 中 `学号` 和 `身份证号` 都是候选码，这两个属性也都是主属性。
再举个例子，`教室(编号, 楼号, 房间号, 人数)` 中 `编号` 和 `(楼号, 房间号)` 都是候选码，这三个属性都是主属性。

2NF 要求，任何一个**非**主属性，都不能部分函数依赖于候选码。

举例而言，`student_course(student_id, course_id, student_name, course_name, grade)` 中，一个候选码是 `(student_id, course_id)`，但 `student_id -> student_name`，因此不符合 2NF。

#### 第三范式 | 3NF：消除传递依赖

3NF 要求，所有非主属性直接依赖于主属性。

举例而言，`学生(学生ID, 姓名, 系ID, 系名)` 中 `学生ID` 是主属性，但 `学生ID -> 系ID -> 系名`，因此不符合 3NF。应被拆分成 `学生(学生ID, 姓名, 系ID)` + `系(系ID, 系名)`

#### BCNF

BCNF 要求，

举例而言，`学生(学号, 身份证号, 姓名, 班级)` 满足 1~3NF

#### 第四范式 | 4NF：消除多值依赖