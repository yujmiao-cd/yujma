1. Sql 学习(参考资料：http://c.biancheng.net/view/2440.html)：

   SQL 包含以下 4 部分：

   1. 数据定义语言（DDL）：DROP、CREATE、ALTER 等语句。
   2. 数据操作语言（DML）：INSERT（插入）、UPDATE（修改）、DELETE（删除）语句。
   3. 数据查询语言（DQL）：SELECT 语句。
   4. 数据控制语言（DCL）: GRANT、REVOKE、COMMIT、ROLLBACK 等语句。

   ### DML:

   ```sql
   #### Insert:
   
   mysql> insert into tb_emp1 values (1, 'yiyi', 001, '3500.0');
   
   mysql> insert into tb_emp1 values (2, 'erer', 002, '5500.0');
   
   mysql> insert into tb_emp1 values (3, 'saner', 003, '2500.0');
   
   #### update:
   
   mysql> update tb_emp1 set name = 'xyn' where name='yiyi';
   
   #### select:
   
   mysql> select * from tb_emp1;
   
   +------+-------+--------+--------+
   
   | id  | name | deptId | salary |
   
   +------+-------+--------+--------+
   
   |  1 | xyn  |   1 |  3500 |
   
   |  2 | erer |   2 |  5500 |
   
   |  3 | saner |   3 |  2500 |
   
   +------+-------+--------+--------+
   
   3 rows in set (0.00 sec)
   
   #### delete:
   
   mysql> delete from tb_emp1 where id = 3;
   
   Query OK, 1 row affected (0.01 sec)
   ```

   ### DDL:

   #### Create table(创建测试表):

   ```sql
   mysql> create table tb_emp1(id int(11), name varchar(25), deptId int(11), salary float);
   mysql> desc tb_emp1;
   mysql> create table student(student_id int unsigned, name varchar(30), sex char(1), bird DATE, primary key(student_id));
   ```

   ```sql
   mysql> show create table tb_emp1;
   
   | Table  | Create Table                                                                                         
   
   | tb_emp1 | CREATE TABLE `tb_emp1` (
   
    `id` int(11) DEFAULT NULL,
   
    `name` varchar(25) DEFAULT NULL,
   
    `deptId` int(11) DEFAULT NULL,
   
    `salary` float DEFAULT NULL
   
   ) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
   
   1 row in set (0.00 sec)
   
     mysql> create database test_del;
   
     Query OK, 1 row affected (0.01 sec)
   
     mysql> drop database test_del;
   
     Query OK, 0 rows affected (0.05 sec). 
   
     mysql> drop database if exists test_del;
   
     Query OK, 0 rows affected, 1 warning (0.00 sec)
   ```

   #### 修改数据库：

   **增加字段，位于所有字段之前（First）或之后（默认after）**

   【实例1 】使用 ALTER TABLE 修改表 tb_emp1 的结构，在表的第一列添加一个 int 类型的字段 col1，输入的 SQL 语句和运行结果如下所示。

   ```sql
   ALTER TABLE <表名> ADD <新字段名> <数据类型> [约束条件] [FIRST|AFTER 已存在的字段名]；
   mysql> alter table tb_emp1 add column col1 int first;
   
   Query OK, 0 rows affected (0.29 sec)
   
   Records: 0 Duplicates: 0 Warnings: 0
   
   
   mysql> desc tb_emp1;
   
   +--------+-------------+------+-----+---------+-------+
   
   | Field | Type    | Null | Key | Default | Extra |
   
   +--------+-------------+------+-----+---------+-------+
   
   | col1  | int(11)   | YES |   | NULL  |    |
   
   | id   | int(11)   | YES |   | NULL  |    |
   
   | name  | varchar(25) | YES |   | NULL  |    |
   
   | deptId | int(11)   | YES |   | NULL  |    |
   
   | salary | float    | YES |   | NULL  |    |
   
   +--------+-------------+------+-----+---------+-------+
   
   5 rows in set (0.00 sec)
   
   mysql> alter table tb_emp1 add column col2 int;
   
   Query OK, 0 rows affected (0.05 sec)
   
   Records: 0 Duplicates: 0 Warnings: 0
   
   mysql> desc tb_emp1;
   
   +--------+-------------+------+-----+---------+-------+
   
   | Field | Type    | Null | Key | Default | Extra |
   
   +--------+-------------+------+-----+---------+-------+
   
   | col1  | int(11)   | YES |   | NULL  |    |
   
   | id   | int(11)   | YES |   | NULL  |    |
   
   | name  | varchar(25) | YES |   | NULL  |    |
   
   | deptId | int(11)   | YES |   | NULL  |    |
   
   | salary | float    | YES |   | NULL  |    |
   
   | col2  | int(11)   | YES |   | NULL  |    |
   
   +--------+-------------+------+-----+---------+-------+
   
   6 rows in set (0.01 sec)
   ```

   【实例 2】使用 ALTER TABLE 修改表 tb_emp1 的结构，在一列 name 后添加一个 int 类型的字段 col2，输入的 SQL 语句和运行结果如下所示。

   ```sql
   mysql> alter table tb_emp1 add column col3 int after name;
   
   Query OK, 0 rows affected (0.04 sec)
   
   Records: 0 Duplicates: 0 Warnings: 0
   
   mysql> desc tb_emp1;
   
   +--------+-------------+------+-----+---------+-------+
   
   | Field | Type    | Null | Key | Default | Extra |
   
   +--------+-------------+------+-----+---------+-------+
   
   | col1  | int(11)   | YES |   | NULL  |    |
   
   | id   | int(11)   | YES |   | NULL  |    |
   
   | name  | varchar(25) | YES |   | NULL  |    |
   
   | col3  | int(11)   | YES |   | NULL  |    |
   
   | deptId | int(11)   | YES |   | NULL  |    |
   
   | salary | float    | YES |   | NULL  |    |
   
   | col2  | int(11)   | YES |   | NULL  |    |
   
   +--------+-------------+------+-----+---------+-------+
   
   7 rows in set (0.01 sec)
   ```

    **修改字段数据类型**

   ```sql
   ALTER TABLE <表名> MODIFY <字段名> <数据类型>
   mysql> alter table tb_emp1 modify name varchar(30);
   ```

   **删除字段**

   ```mysql
   ALTER TABLE <表名> DROP <字段名>；
   
   mysql> alter table tb_emp1 drop col2;
   
   mysql> alter table tb_emp1 drop col3;
   ```

   **修改字段名**

   ```mysql
   ALTER TABLE <表名> CHANGE <旧字段名> <新字段名> <新数据类型>；
   
   mysql> alter table tb_emp1 change col1 col3 char(10);
   ```

   **修改表名**

   ```mysql
   ALTER TABLE <旧表名> RENAME [TO] <新表名>；
   
   mysql> alter table tb_emp1 rename tb_emp;
   ```

   **主键**

   ```mysql
   <字段名> <数据类型> PRIMARY KEY [默认值]
   
   在定义完所有列之后，指定主键的语法格式为：
   
   [CONSTRAINT <约束名>] PRIMARY KEY [字段名]
   
   mysql> create table tb_emp3(id int(11) primary key,
   
     -> name varchar(20),
   
     -> deptId int(11),
   
     -> salary float );
   
   Query OK, 0 rows affected (0.01 sec)
   
   mysql> create table tb_emp4(id int(11),
   
     -> name varchar(20),
   
     -> primary key(id) );
   
   Query OK, 0 rows affected (0.03 sec)
   
   复合主键：
   
    PRIMARY KEY [字段1，字段2，…,字段n]
   
   create table tb_emp5(id int(11), name varchar(20), salary float, 
   
   primary key(id,name));
   
    修改表时添加主键约束
   
   mysql> alter table tb_emp1 add primary key(id);
   
   
   ```

   

   **外键：**

   ```mysql
   mysql> create table tb_dept1(
   
     -> id int(11) primary key,
   
     -> name varchar(20) not null,
   
     -> locate varchar(50)
   
     -> );
   
   Query OK, 0 rows affected (0.02 sec)
   
   
   
   mysql> create table tb_emp6(
   
     -> id int(11) primary key,
   
     -> name varchar(20),
   
     -> deptId int(11),
   
     -> salary float,
   
     -> constraint fk_emp_dept1 
   
     -> foreign key(deptId) references tb_dept1(id)
   
     -> );
   
   deptid   and  id. 类型必须一致
   
   ALTER TABLE <数据表名> ADD CONSTRAINT <索引名>
   FOREIGN KEY(<列名>) REFERENCES <主表名> (<列名>);
   mysql> ALTER TABLE tb_emp2
       -> ADD CONSTRAINT fk_tb_dept1
       -> FOREIGN KEY(deptId)
       -> REFERENCES tb_dept1(id);
   删除外键约束：
   mysql> alter table tb_emp6 drop foreign key fk_emp_dept1;
   ```

   **唯一约束：**

   ```mysql
   <字段名> <数据类型> UNIQUE
   
   mysql> create table tb_dept2( id int(11) primary key, name varchar(20) unique, locate varchar(50) );
   
   Query OK, 0 rows affected (0.01 sec)
   
   mysql> desc tb_dept2;
   
   +--------+-------------+------+-----+---------+-------+
   
   | Field | Type    | Null | Key | Default | Extra |
   
   +--------+-------------+------+-----+---------+-------+
   
   | id   | int(11)   | NO  | PRI | NULL  |    |
   
   | name  | varchar(20) | YES | UNI | NULL  |    |
   
   | locate | varchar(50) | YES |   | NULL  |    |
   
   +--------+-------------+------+-----+---------+-------+
   
   3 rows in set (0.00 sec)
   
   提示：UNIQUE 和 PRIMARY KEY 的区别：一个表可以有多个字段声明为 UNIQUE，但只能有一个 PRIMARY KEY 声明；声明为 PRIMAY KEY 的列不允许有空值，但是声明为 UNIQUE 的字段允许空值的存在。
   
   
   
   修改表时添加唯一约束：
   
   mysql> alter table tb_dept2 add constraint unique_name unique(locate);
   
   Query OK, 0 rows affected (0.00 sec)
   
   Records: 0 Duplicates: 0 Warnings: 0
   
   mysql> desc tb_dept2;
   
   +--------+-------------+------+-----+---------+-------+
   
   | Field | Type    | Null | Key | Default | Extra |
   
   +--------+-------------+------+-----+---------+-------+
   
   | id   | int(11)   | NO  | PRI | NULL  |    |
   
   | name  | varchar(20) | YES | UNI | NULL  |    |
   
   | locate | varchar(50) | YES | UNI | NULL  |    |
   
   +--------+-------------+------+-----+---------+-------+
   
   3 rows in set (0.00 sec)
   
   删除唯一约束：
   
   ALTER TABLE <表名> DROP INDEX <唯一约束名>;
   
   mysql> alter table tb_dept2 drop index unique_name;
   
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> alter table tb_dept2 drop index name;
   
   Query OK, 0 rows affected (0.00 sec)
   
   Records: 0 Duplicates: 0 Warnings: 0
   
   mysql> desc tb_dept2;
   
   +--------+-------------+------+-----+---------+-------+
   
   | Field | Type    | Null | Key | Default | Extra |
   
   +--------+-------------+------+-----+---------+-------+
   
   | id   | int(11)   | NO  | PRI | NULL  |    |
   
   | name  | varchar(20) | YES |   | NULL  |    |
   
   | locate | varchar(50) | YES |   | NULL  |    |
   
   +--------+-------------+-
   ```

    检查约束：

   ```mysql
    mysql> create table tb_emp7(
   
     -> id int(11) primary key,
   
     -> name varchar(25),
   
     -> deptId int(11),
   
     -> salary float,
   
     -> check(salary >0 and salary <10000));
   
   mysql> insert into tb_emp7 values (1,'zs',001,100);
   
   Query OK, 1 row affected (0.01 sec)
   
   mysql> insert into tb_emp7 values (1,'zs',001,100000);
   
   ERROR 1062 (23000): Duplicate entry '1' for key 'PRIMARY'
   
   修改表结构添加约束：
   
   mysql> alter table tb_emp7 
   
     -> add constraint check_id
   
     -> check(id>0);
   
   Query OK, 0 rows affected (0.00 sec)
   
   Records: 0 Duplicates: 0 Warnings: 0
   
   删除检查约束:
   
   ALTER TABLE <数据表名> DROP CONSTRAINT <检查约束名>;
   ```

   **默认值：**

   ```mysql
   创建表时设置默认值：
   <字段名> <数据类型> DEFAULT <默认值>;
   mysql> CREATE TABLE tb_dept3
       -> (
       -> id INT(11) PRIMARY KEY,
       -> name VARCHAR(22),
       -> location VARCHAR(50) DEFAULT 'Beijing'
       -> );
   
   修改表时添加默认值：
   ALTER TABLE <数据表名>
   CHANGE COLUMN <字段名> <数据类型> DEFAULT <默认值>;
   mysql> ALTER TABLE tb_dept3
       -> CHANGE COLUMN location
       -> location VARCHAR(50) DEFAULT 'Shanghai';
       
   删除默认值：
   ALTER TABLE <数据表名>
   CHANGE COLUMN <字段名> <字段名> <数据类型> DEFAULT NULL;
   ```

   **Mysql 中查看约束：**

   ```mysql
   SHOW CREATE TABLE <数据表名>;
   ```

   ==============================================Day3-4

   

   **Mysql 去重：**

   ```sql
   SELECT DISTINCT <字段名> FROM <表名>;
   
   mysql> select distinct name from student;
   ```

   **Mysql  正则表达式:**

   ```mysql
   Regex:
   
   mysql> select * from student where name regexp '^e';
   
   mysql> select * from student where name regexp 'er$';
   
   mysql> select * from student where name regexp 'o.n';
   
   +------------+---------+------+------------+
   
   | student_id | name  | sex | bird    |
   
   +------------+---------+------+------------+
   
   |     7 | Econoyn | 1  | 2020-03-04 |
   
   +------------+---------+------+------------+
   
   
   
   使用 '*'  匹配任意多次，‘+’至少一次：
   
   mysql> select * from student where name regexp '^Ch*';
   
   +------------+----------+------+------------+
   
   | student_id | name   | sex | bird    |
   
   +------------+----------+------+------------+
   
   |     8 | Computer | 1  | 2020-03-03 |
   
   |     9 | Chinese | 1  | 2020-03-03 |
   
   |     10 | Conne  | 2  | 2020-03-06 |
   
   +------------+----------+------+------------+
   
   匹配指定字符串：
   
   mysql> select * from student where name regexp 'in';
   
   +------------+---------+------+------------+
   
   | student_id | name  | sex | bird    |
   
   +------------+---------+------+------------+
   
   |     9 | Chinese | 1  | 2020-03-03 |
   
   +------------+---------+------+------------+
   
   1 row in set (0.00 sec)
   
   mysql> select * from student where name regexp 'in|on';
   
   +------------+---------+------+------------+
   
   | student_id | name  | sex | bird    |
   
   +------------+---------+------+------------+
   
   |     7 | Econoyn | 1  | 2020-03-04 |
   
   |     9 | Chinese | 1  | 2020-03-03 |
   
   |     10 | Conne  | 2  | 2020-03-06 |
   
   +------------+---------+------+------------+
   
   3 rows in set (0.00 sec)
   
   匹配指定字符串中的任意一个：
   
   mysql> select * from student where name regexp '[io]';
   
   +------------+----------+------+------------+
   
   | student_id | name   | sex | bird    |
   
   +------------+----------+------+------------+
   
   |     1 | yiyi   | 1  | 2000-01-01 |
   
   |     7 | Econoyn | 1  | 2020-03-04 |
   
   |     8 | Computer | 1  | 2020-03-03 |
   
   |     9 | Chinese | 1  | 2020-03-03 |
   
   |     10 | Conne  | 2  | 2020-03-06 |
   
   +------------+----------+------+------------+
   
   5 rows in set (0.00 sec)
   
   mysql> select * from student where sex regexp '[12]';
   
   匹配指定字符以外的字符：
   
   mysql> select * from student where name regexp '[^a-t]';
   
   +------------+----------+------+------------+
   
   | student_id | name   | sex | bird    |
   
   +------------+----------+------+------------+
   
   |     1 | yiyi   | 1  | 2000-01-01 |
   
   |     7 | Econoyn | 1  | 2020-03-04 |
   
   |     8 | Computer | 1  | 2020-03-03 |
   
   +------------+----------+------+------------+
   
   3 rows in set (0.00 sec)
   
   ```

   ```mysql
   mysql 插入数据：
   
   mysql> insert into tb_course_new (select * from tb_course);
   
   mysql  修改数据：
   
   mysql> update tb_course_new set grade='99';
   
   Query OK, 2 rows affected (0.00 sec)
   
   Rows matched: 2 Changed: 2 Warnings: 0
   
   mysql 删除数据：
   
   mysql> delete from tb_course_new;
   
   Query OK, 2 rows affected (0.00 sec)
   ```

   **mysql.     视图：52**

   视图并不同于数据表，它们的区别在于以下几点：

   视图不是数据库中真实的表，而是一张虚拟表，其结构和数据是建立在对数据中真实表的查询基础上的。

   存储在数据库中的查询操作 SQL 语句定义了视图的内容，列数据和行数据来自于视图查询所引用的实际表，引用视图时动态生成这些数据。

   视图没有实际的物理记录，不是以数据集的形式存储在数据库中的，它所对应的数据实际上是存储在视图所引用的真实表中的。
   
   视图是数据的窗口，而表是内容。表是实际数据的存放单位，而视图只是以不同的显示方式展示数据，其数据来源还是实际表。
   
   视图是查看数据表的一种方法，可以查询数据表中某些字段构成的数据，只是一些 SQL 语句的集合。从安全的角度来看，视图的数据安全性更高，使用视图的用户不接触数据表，不知道表结构。
   
视图的建立和删除只影响视图本身，不影响对应的基本表。
   
   
   
   CREATE VIEW <视图名> AS <SELECT语句>
   
   mysql> create view student_view as select * from student;
   
   视图用于查询主要应用在以下几个方面：
   
   - 使用视图重新格式化检索出的数据。
   - 使用视图简化复杂的表连接。
   - 使用视图过滤数据。
   
   ```mysql
   DESCRIBE 可以用来查看视图，语法如下：
   
   DESCRIBE 视图名；
   
   mysql> desc student_view;
   
   修改视图：
   
   ALTER VIEW <视图名> AS <SELECT语句>
   
   修改视图的定义，除了可以通过 ALTER VIEW 外，也可以使用 DROP VIEW 语句先删除视图，再使用 CREATE     VIEW 语句来实现。
   
   mysql> alter view student_view as select student_id,name from student;
   
   删除视图：
   
   mysql> drop view if exists student_view;
   ```
   
   **mysql 自定义函数（create function）**
   
   在使用 [MySQL](http://c.biancheng.net/mysql/) 的过程中，MySQL 自带的函数可能完成不了我们的业务需求，这时候就需要自定义函数。
   
   自定义函数是一种与存储过程十分相似的过程式数据库对象。它与存储过程一样，都是由 SQL 语句和过程式语句组成的代码片段，并且可以被应用程序和其他 SQL 语句调用。
   
   自定义函数与存储过程之间存在几点区别：
   
   自定义函数不能拥有输出参数，这是因为自定义函数自身就是输出参数；而存储过程可以拥有输出参数。
   
   自定义函数中必须包含一条 RETURN 语句，而这条特殊的 SQL 语句不允许包含于存储过程中。
   
   可以直接对自定义函数进行调用而不需要使用 CALL 语句，而对存储过程的调用需要使用 CALL 语句。
   
   ```mysql
   【实例 1】创建存储函数，名称为 StuNameById，该函数返回 SELECT 语句的查询结果，数值类型为字符串类型，输入的 SQL 语句和执行结果如下所示。
   
   mysql> create function StudentById()
   
     -> returns varchar(30)
   
     -> return
   
     -> (select name from student
   
     -> where student_id = 1);
   
   Query OK, 0 rows affected (0.02 sec)
   
   成功创建自定义函数后，就可以如同调用系统内置函数一样，使用关键字 SELECT 调用用户自定义的函数，语法格式为：
   
   SELECT <自定义函数名> ([<参数> [,...]])
   
   mysql> select StudentById();
   
   +---------------+
   
   | StudentById() |
   
   +---------------+
   
   | test     |
   
   +---------------+
   
   1 row in set (0.00 sec)
   
    修改： alter function；
   
    删除： drop function function_name；
   ```
   
   **存储过程：**
   
   ```mysql
   可以使用 CREATE PROCEDURE 语句创建存储过程。
   
   语法格式如下：
   
   CREATE PROCEDURE <过程名> ( [过程参数[,…] ] ) <过程体>
   [过程参数[,…] ] 格式
   [ IN | OUT | INOUT ] <参数名> <类型>
   
   mysql> DELIMITER //
   
   mysql> create procedure ShowStuScore()
   
     -> begin
   
     -> select * from student;
   
     -> end //
   
   mysql> delimiter ;
   
   mysql> call ShowStuScore();
   
   +------------+----------+------+------------+
   
   | student_id | name   | sex | bird    |
   
   +------------+----------+------+------------+
   
   |     1 | test   | 1  | 2000-01-01 |
   
   |     2 | erer   | 1  | 2020-03-01 |
   
   |     3 | erer   | 1  | 2020-03-01 |
   
   |     4 | erer   | 1  | 2020-03-01 |
   
   |     5 | erer   | 2  | 2020-03-01 |
   
   |     6 | erer   | 2  | 2020-03-01 |
   
   |     7 | Econoyn | 1  | 2020-03-04 |
   
   |     8 | Computer | 1  | 2020-03-03 |
   
   |     9 | Chinese | 1  | 2020-03-03 |
   
   |     10 | Conne  | 2  | 2020-03-06 |
   
   +------------+----------+------+------------+
   
   10 rows in set (0.00 sec)
   
   
   
   Query OK, 0 rows affected (0.00 sec)
   
    创建带参数的存储过程：
   
   mysql> CREATE PROCEDURE GetNameByStud
   
     -> (IN name varchar(30))
   
     -> begin
   
     -> select student_id,sex from student
   
     -> where name = name;
   
     -> end //
   
   Query OK, 0 rows affected (0.00 sec)
   
   
   
   mysql> call GetNameByStud('erer')
   
     -> //
   
   +------------+------+
   
   | student_id | sex |
   
   +------------+------+
   
   |     1 | 1  |
   
   |     2 | 1  |
   
   |     3 | 1  |
   
   |     4 | 1  |
   
   |     5 | 2  |
   
   |     6 | 2  |
   
   |     7 | 1  |
   
   |     8 | 1  |
   
   |     9 | 1  |
   
   |     10 | 2  |
   
   +------------+------+
   
   10 rows in set (0.00 sec)
   
   mysql> show create procedure GetNameByStud; \G
   
   下面修改存储过程 showstuscore 的定义，将读写权限改为 MODIFIES SQL DATA，并指明调用者可以执行，代码如下：
   
   mysql> ALTER PROCEDURE GetNameByStud MODIFIES SQL DATA SQL SECURITY INVOKER;
   
     -> //
   
   Query OK, 0 rows affected (0.00 sec)
   
   
   
   mysql> show create procedure GetNameByStud; \G
   
   *************************** 1. row ***************************
   
   ​      Procedure: GetNameByStud
   
   ​      sql_mode: ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
   
     Create Procedure: CREATE DEFINER=`root`@`%` PROCEDURE `GetNameByStud`(IN name varchar(30))
   
     MODIFIES SQL DATA
   
     SQL SECURITY INVOKER
   
   提示：ALTER PROCEDURE 语句用于修改存储过程的某些特征。如果要修改存储过程的内容，可以先删除原存储过程，再以相同的命名创建新的存储过程；如果要修改存储过程的名称，可以先删除原存储过程，再以不同的命名创建新的存储过程。
   
   删除存储过程：
   
   mysql> drop procedure ShowStuName;
       -> //
   
    查询存储过程：
   
   mysql> SELECT * FROM information_schema.routines WHERE routine_name='ShowStuName'；
   
     -> //
   ```
   
   
   
   **触发器：**
   
   ```mysql
   mysql> create table tb_emp8(
   
     -> id int(11),
   
     -> name varchar(20),
   
     -> deptId int(11),
   
     -> salary float);
   
     -> //
   
   Query OK, 0 rows affected (0.06 sec)
   
   【实例 1】创建一个名为 SumOfSalary 的触发器，触发的条件是向数据表 tb_emp8 中插入数据之前，对新插入的 salary 字段值进行求和计算。输入的 SQL 语句和执行过程如下所示。
   
   mysql> 
   
   mysql> desc tb_emp8;
   
     -> //
   
   +--------+-------------+------+-----+---------+-------+
   
   | Field | Type    | Null | Key | Default | Extra |
   
   +--------+-------------+------+-----+---------+-------+
   
   | id   | int(11)   | YES |   | NULL  |    |
   
   | name  | varchar(20) | YES |   | NULL  |    |
   
   | deptId | int(11)   | YES |   | NULL  |    |
   
   | salary | float    | YES |   | NULL  |    |
   
   +--------+-------------+------+-----+---------+-------+
   
   4 rows in set (0.01 sec)
   
   mysql> create trigger sum_salary
   
     -> before insert on tb_emp8
   
     -> for each row 
   
     -> set @sum=@sum+NEW.salary;
   
     -> //
   
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> set @sum=0;
   
   触发器 SumOfSalary 创建完成之后，向表 tb_emp8 中插入记录时，定义的 sum 值由 0 变成了 1500，即插入值 1000 和 500 的和，如下所示。
   
   mysql> insert into tb_emp8 values (1,'A',1,1000),(2,'B',1,500);
   
     -> //
   
   Query OK, 2 rows affected (0.01 sec)
   
   Records: 2 Duplicates: 0 Warnings: 0
   
   mysql> select @sum;//
   
   +------+
   
   | @sum |
   
   +------+
   
   | 1500 |
   
   +------+
   
   1 row in set (0.01 sec)
   
   
   
   创建 alter 类型的触发器：
   
   在 test_db 数据库中，数据表 tb_emp6 和 tb_emp7 都为员工信息表，包含 id、name、deptId 和 salary 字段，数据表 tb_emp6 和 tb_emp7 的表结构如下所示。
   
   
   
   设置默认的delimiter语句：
   
   mysql> delimiter ;
   
   mysql> delimiter //
   
   
   
   【实例 2】创建一个名为 double_salary 的触发器，触发的条件是向数据表 tb_emp6 中插入数据之后，再向数据表 tb_emp7 中插入相同的数据，并且 salary 为 tb_emp6 中新插入的 salary 字段值的 2 倍。输入的 SQL 语句和执行过程如下所示。
   
   mysql> create trigger double_salary 
   
     -> after insert on tb_emp7
   
     -> for each row
   
     -> insert into tb_emp8
   
     -> values (NEW.id, NEW.name, NEW.deptId, 2*NEW.salary);
   
   mysql> insert into tb_emp7 values (2,'A',1,1000),(3,'B',1,500);
   
   mysql> select * from tb_emp7 where id in (2,3);
   
   +----+------+--------+--------+
   
   | id | name | deptId | salary |
   
   +----+------+--------+--------+
   
   | 2 | A  |   1 |  1000 |
   
   | 3 | B  |   1 |  500 |
   
   +----+------+--------+--------+
   
   2 rows in set (0.00 sec)
   
   
   
   mysql> select * from tb_emp8 where id in (2,3);
   
   +------+------+--------+--------+
   
   | id  | name | deptId | salary |
   
   +------+------+--------+--------+
   
   |  2 | A  |   1 |  2000 |
   
   |  3 | B  |   1 |  1000 |
   
   +------+------+--------+--------+
   
   2 rows in set (0.00 sec)
   
   
   
   删除触发器：
   
   mysql> DROP TRIGGER double_salary;
   ```
   
   
   
   索引（64）
   
   1. ```mysql
      1. 一般索引
      
         CREATE <索引名> ON <表名> (<列名> [<长度>] [ ASC | DESC])
      
         ADD INDEX [<索引名>] [<索引类型>] (<列名>,…)
      
         ADD PRIMARY KEY [<索引类型>] (<列名>,…)
      
         ADD UNIQUE [ INDEX | KEY] [<索引名>] [<索引类型>] (<列名>,…)
      
         ADD FOREIGN KEY [<索引名>] (<列名>,…)
      
         【实例 1】创建一个表 tb_stu_info，在该表的 height 字段创建一般索引。输入的 SQL 语句和执行过程如下所示。
      
         mysql> create table tb_stu_info(
      
           -> id int not null,
      
           -> name varchar(45) default null,
      
           -> dept_id int default null,
      
           -> age int default null,
      
           -> height int default null,
      
           -> index(height));
      
         Query OK, 0 rows affected (0.04 sec)
      
      2. 唯一索引
      
         【实例 2】创建一个表 tb_stu_info2，在该表的 id 字段上使用 UNIQUE 关键字创建唯一索引。输入的 SQL 语句和执行过程如下所示。
      
         mysql> create table tb_stu_info2
      
           -> ( id int(11) not null,
      
           -> `name` varchar(45) DEFAULT NULL,
      
           -> `dept_id` int(11) DEFAULT NULL,
      
           -> `age` int(11) DEFAULT NULL,
      
           -> `height` int(11) DEFAULT NULL,
      
           -> unique index(height));
      
      3. 查看索引
      
         SHOW INDEX FROM <表名> [ FROM <数据库名>]
      
         mysql> show index from tb_stu_info2 from test;
      
         +--------------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
      
         | Table    | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
      
         +--------------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
      
         | tb_stu_info2 |     0 | height  |      1 | height   | A     |      0 |   NULL | NULL  | YES | BTREE   |     |        |
      
         +--------------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
      
         1 row in set (0.00 sec)
      
         该语句会返回一张结果表，该表有如下几个字段，每个字段所显示的内容说明如下。
      
         - Table：表的名称。
      
         - Non_unique：用于显示该索引是否是唯一索引。若不是唯一索引，则该列的值显示为 1；若是唯一索引，则该列的值显示为 0。
      
         - Key_name：索引的名称。
      
         - Seq_in_index：索引中的列序列号，从 1 开始计数。
      
         - Column_name：列名称。
      
         - Collation：显示列以何种顺序存储在索引中。在 MySQL 中，升序显示值“A”（升序），若显示为 NULL，则表示无分类。
      
         - Cardinality：显示索引中唯一值数目的估计值。基数根据被存储为整数的统计数据计数，所以即使对于小型表，该值也没有必要是精确的。基数越大，当进行联合时，MySQL 使用该索引的机会就越大。
      
         - Sub_part：若列只是被部分编入索引，则为被编入索引的字符的数目。若整列被编入索引，则为 NULL。
      
         - Packed：指示关键字如何被压缩。若没有被压缩，则为 NULL。
      
         - Null：用于显示索引列中是否包含 NULL。若列含有 NULL，则显示为 YES。若没有，则该列显示为 NO。
      
         - Index_type：显示索引使用的类型和方法（BTREE、FULLTEXT、HASH、RTREE）。
      
         - Comment：显示评注。
      
           【实例 3】使用 SHOW INDEX 语句查看表 tb_stu_info2 的索引信息，输入的 SQL 语句和执行结果如下所示
      
           mysql> show index from tb_stu_info2\G
      
           *************************** 1. row ***************************
      
            Table: tb_stu_info2
      
             Non_unique: 0
      
              Key_name: height
      
            Seq_in_index: 1
      
            Column_name: height
      
             Collation: A
      
            Cardinality: 0
      
              Sub_part: NULL
      
              Packed: NULL
      
               Null: YES
      
             Index_type: BTREE
      
              Comment: 
      
           Index_comment: 
      
           1 row in set (0.00 sec)
      
      4. 修改和删除索引：
      
         drop：
      
         DROP INDEX <索引名> ON <表名>
      
         语法说明如下：
      
         - `<索引名>`：要删除的索引名。
         - `<表名>`：指定该索引所在的表名。
      
         alter：
      
         根据 ALTER TABLE 语句的语法可知，该语句也可以用于删除索引。具体使用方法是将 ALTER TABLE 语句的语法中部分指定为以下子句中的某一项。
      
         - DROP PRIMARY KEY：表示删除表中的主键。一个表只有一个主键，主键也是一个索引。
         - DROP INDEX index_name：表示删除名称为 index_name 的索引。
         - DROP FOREIGN KEY fk_symbol：表示删除外键。
      
         注意：如果删除的列是索引的组成部分，那么在删除该列时，也会将该列从索引中删除；如果组成索引的所有列都被删除，那么整个索引将被删除。
      
      5. 删除索引： 
      
      【实例 1】删除表 tb_stu_info 中的索引，输入的 SQL 语句和执行结果如下所示。
      
         mysql> drop index height on tb_stu_info2;
      
      【实例 2】删除表 tb_stu_info2 中名称为 id 的索引，输入的 SQL 语句和执行结果如下所示。
      
        mysql> alter table tb_stu_info drop index height;
      ```
   
      https://www.cnblogs.com/wangchunli-blogs/p/10416046.html。 普通索引和唯一索引。
   
   
   
   #### Mysql 用户
   
   ```mysql
   **Mysql 创建用户：**
   
   CREATE USER <用户名> [ IDENTIFIED ] BY [ PASSWORD ] <口令>
   
   【实例 1】使用 CREATE USER 创建一个用户，用户名是 james，密码是 tiger，主机是 localhost。输入的 SQL 语句和执行过程如下所示。
   
   mysql> create user 'james'@'localhost' identified by 'tiger';
   
   [root@localhost yujma]# mysql -u james -p
   
   Enter password: 
   
   mysql> 
   
   
   
   **mysql 修改用户：**
   
   RENAME USER <旧用户> TO <新用户>
   
   mysql> rename user james@'localhost' to jack@'localhost';
   
   Query OK, 0 rows affected (0.02 sec)
   
   [root@localhost yujma]# mysql -h localhost -u jack -p
   
   
   
   mysql 修改用户口令：
   
   可以使用 SET PASSWORD 语句修改一个用户的登录口令。
   
   SET PASSWORD [ FOR <用户名> ] =
   {
       PASSWORD('新明文口令')
       | OLD_PASSWORD('旧明文口令')
       | '加密口令值'
   }
   
   注意：PASSWORD() 函数为单向加密函数，一旦加密后不能解密出原明文
   
   
   
   使用 SET PASSWORD 语句应注意以下几点：
   
   - 在 SET PASSWORD 语句中，若不加上 FOR 子句，表示修改当前用户的口令。若加上 FOR 子句，表示修改账户为 user 的用户口令。
   - user 必须以 'user_name'@'host_name' 的格式给定，user_name 为账户的用户名，host_name 为账户的主机名。
   - 该账户必须在系统中存在，否则语句执行时会出现错误。
   - 在 SET PASSWORD 语句中，只能使用选项 PASSWORD('新明文口令') 和加密口令值中的一项，且必须使用其中的一项。
   
   【实例 2】使用 SET 语句将用户名为 jack 的密码修改为 lion，主机是 localhost。输入的 SQL 语句和执行过程如下所示。
   
   mysql> set password for 'jack'@'localhost' = password('lion');
   
   Query OK, 0 rows affected, 1 warning (0.00 sec)
   
   mysql> exit
   
   Bye
   
   [root@localhost yujma]# mysql -u jack -p
   
   Enter password:        # lion
   
   mysql> 
   
   
   
   **mysql 删除用户：**
   
   DROP USER <用户名1> [ , <用户名2> ]…
   
   mysql> drop user 'jack'@'localhost';
   
   Query OK, 0 rows affected (0.00 sec)
   
   
   
   **mysql 查询用户：**
   
   mysql> select host, user from mysql.user;
   
   +-----------+---------------+
   
   | host   | user     |
   
   +-----------+---------------+
   
   | %     | root     |
   
   | localhost | mysql.session |
   
   | localhost | mysql.sys   |
   
   +-----------+---------------+
   
   3 rows in set (0.00 sec)
   ```
   
   
   
   ### mysql 用户授权：
   
   ```
   GRANT
   <权限类型> [ ( <列名> ) ] [ , <权限类型> [ ( <列名> ) ] ]
   ON <对象> <权限级别> TO <用户>
   其中<用户>的格式：
   <用户名> [ IDENTIFIED ] BY [ PASSWORD ] <口令>
   [ WITH GRANT OPTION]
   | MAX_QUERIES_PER_HOUR <次数>
   | MAX_UPDATES_PER_HOUR <次数>
   | MAX_CONNECTIONS_PER_HOUR <次数>
   | MAX_USER_CONNECTIONS <次数>
   ```
   
   #### <权限级别>
   
   用于指定权限的级别。可以授予的权限有如下几组：
   
   - 列权限，和表中的一个具体列相关。例如，可以使用 UPDATE 语句更新表 students 中 student_name 列的值的权限。
   - 表权限，和一个具体表中的所有数据相关。例如，可以使用 SELECT 语句查询表 students 的所有数据的权限。
   - 数据库权限，和一个具体的数据库中的所有表相关。例如，可以在已有的数据库 mytest 中创建新表的权限。
   - 用户权限，和 MySQL 中所有的数据库相关。例如，可以删除已有的数据库或者创建一个新的数据库的权限。
   
   
   对应地，在 GRANT 语句中可用于指定权限级别的值有以下几类格式：
   
   - *：表示当前数据库中的所有表。
   - *.*：表示所有数据库中的所有表。
   - db_name.*：表示某个数据库中的所有表，db_name 指定数据库名。
   - db_name.tbl_name：表示某个数据库中的某个表或视图，db_name 指定数据库名，tbl_name 指定表名或视图名。
   - tbl_name：表示某个表或视图，tbl_name 指定表名或视图名。
   - db_name.routine_name：表示某个数据库中的某个存储过程或函数，routine_name 指定存储过程名或函数名。
   - TO 子句：用来设定用户口令，以及指定被赋予权限的用户 user。若在 TO 子句中给系统中存在的用户指定口令，则新密码会将原密码覆盖；如果权限被授予给一个不存在的用户，MySQL 会自动执行一条 CREATE USER 语句来创建这个用户，但同时必须为该用户指定口令。
   
   GRANT语句中的`<权限类型>`的使用说明如下：
   
   #### 1) 授予数据库权限时，<权限类型>可以指定为以下值：
   
   - SELECT：表示授予用户可以使用 SELECT 语句访问特定数据库中所有表和视图的权限。
   - INSERT：表示授予用户可以使用 INSERT 语句向特定数据库中所有表添加数据行的权限。
   - DELETE：表示授予用户可以使用 DELETE 语句删除特定数据库中所有表的数据行的权限。
   - UPDATE：表示授予用户可以使用 UPDATE 语句更新特定数据库中所有数据表的值的权限。
   - REFERENCES：表示授予用户可以创建指向特定的数据库中的表外键的权限。
   - CREATE：表示授权用户可以使用 CREATE TABLE 语句在特定数据库中创建新表的权限。
   - ALTER：表示授予用户可以使用 ALTER TABLE 语句修改特定数据库中所有数据表的权限。
   - SHOW VIEW：表示授予用户可以查看特定数据库中已有视图的视图定义的权限。
   - CREATE ROUTINE：表示授予用户可以为特定的数据库创建存储过程和存储函数的权限。
   - ALTER ROUTINE：表示授予用户可以更新和删除数据库中已有的存储过程和存储函数的权限。
   - INDEX：表示授予用户可以在特定数据库中的所有数据表上定义和删除索引的权限。
   - DROP：表示授予用户可以删除特定数据库中所有表和视图的权限。
   - CREATE TEMPORARY TABLES：表示授予用户可以在特定数据库中创建临时表的权限。
   - CREATE VIEW：表示授予用户可以在特定数据库中创建新的视图的权限。
   - EXECUTE ROUTINE：表示授予用户可以调用特定数据库的存储过程和存储函数的权限。
   - LOCK TABLES：表示授予用户可以锁定特定数据库的已有数据表的权限。
   - ALL 或 ALL PRIVILEGES：表示以上所有权限。
   
   #### 2) 授予表权限时，<权限类型>可以指定为以下值：
   
   - SELECT：授予用户可以使用 SELECT 语句进行访问特定表的权限。
   - INSERT：授予用户可以使用 INSERT 语句向一个特定表中添加数据行的权限。
   - DELETE：授予用户可以使用 DELETE 语句从一个特定表中删除数据行的权限。
   - DROP：授予用户可以删除数据表的权限。
   - UPDATE：授予用户可以使用 UPDATE 语句更新特定数据表的权限。
   - ALTER：授予用户可以使用 ALTER TABLE 语句修改数据表的权限。
   - REFERENCES：授予用户可以创建一个外键来参照特定数据表的权限。
   - CREATE：授予用户可以使用特定的名字创建一个数据表的权限。
   - INDEX：授予用户可以在表上定义索引的权限。
   - ALL 或 ALL PRIVILEGES：所有的权限名。
   
   #### 3) 授予列权限时，<权限类型>的值只能指定为 SELECT、INSERT 和 UPDATE，同时权限的后面需要加上列名列表 column-list。
   
   #### 4) 最有效率的权限是用户权限。
   
   授予用户权限时，<权限类型>除了可以指定为授予数据库权限时的所有值之外，还可以是下面这些值：
   
   - CREATE USER：表示授予用户可以创建和删除新用户的权限。
   - SHOW DATABASES：表示授予用户可以使用 SHOW DATABASES 语句查看所有已有的数据库的定义的权限。
   
   【实例】使用 GRANT 语句创建一个新的用户 james，密码为 tiger。用户 james 对所有的数据有查询、插入权限，并授予 GRANT 权限。输入的 SQL 语句和执行过程如下所示。
   
   ```mysql
   mysql> grant select, insert on  * . *
   
     -> to 'james'@'localhost'
   
     -> identified by 'tiger'
   
     -> with grant option;
   
   Query OK, 0 rows affected, 1 warning (0.01 sec)
   
   mysql> SELECT Host,User,Select_priv,Grant_priv
   
     -> from mysql.user
   
     -> where user='james';
   
   +-----------+-------+-------------+------------+
   
   | Host   | User | Select_priv | Grant_priv |
   
   +-----------+-------+-------------+------------+
   
   | localhost | james | Y      | Y     |
   
   +-----------+-------+-------------+------------+
   
   1 row in set (0.01 sec)
   ```
   
   **mysql 删除用户权限（revoke）**
   
   1. REVOKE <权限类型> [ ( <列名> ) ] [ , <权限类型> [ ( <列名> ) ] ]…
      ON <对象类型> <权限名> FROM <用户1> [ , <用户2> ]…
   2. REVOKE ALL PRIVILEGES, GRANT OPTION
      FROM user <用户1> [ , <用户2> ]…
   
   语法说明如下：
   
   - REVOKE 语法和 GRANT 语句的语法格式相似，但具有相反的效果。
   - 第一种语法格式用于回收某些特定的权限。
   - 第二种语法格式用于回收特定用户的所有权限。
   - 要使用 REVOKE 语句，必须拥有 MySQL 数据库的全局 CREATE USER 权限或 UPDATE 权限。
   
   【实例】使用 REVOKE 语句取消用户 james 的插入权限，输入的 SQL 语句和执行过程如下所示。
   
   ```mysql
   mysql> SELECT Host,User,Select_priv,Insert_priv,Grant_priv
   
     -> from mysql.user
   
     -> where user='james';
   
   +-----------+-------+-------------+-------------+------------+
   
   | Host   | User | Select_priv | Insert_priv | Grant_priv |
   
   +-----------+-------+-------------+-------------+------------+
   
   | localhost | james | Y      | N      | Y     |
   
   +-----------+-------+-------------+-------------+------------+
   
   1 row in set (0.00 sec)
   ```
   
   
   
   ### mysql 数据库备份
   
   ```mysql
   可以使用 SELECT INTO OUTFILE 语句把表数据导出到一个文本文件中进行备份。
   
   注意：这种方法只能导出或导入数据的内容，而不包括表的结构。若表的结构文件损坏，则必须先设法恢复原来表的结构。
   
   【实例】将数据库 test 的表 students 的全部数据备份到 （/kittod/yujma/）的数据备份目录下文件名为 file.txt 的文件中，要求每个字段用逗号分开，并且字符用双引号标注，每行以问号结束。
   
   mysql> select * from test.student
   
     -> into outfile '/kittod/yujma/file.txt'
   
     -> FIELDS TERMINATED BY '"'
   
     -> LINES TERMINATED BY '?';
   
   ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
   
   查看 secure_file_priv 的值，默认为NULL，表示限制不能导入导出。
   
   查看官方文档，secure_file_priv参数用于限制LOAD DATA, SELECT …OUTFILE, LOAD_FILE()传到哪个指定目录。
   
   secure_file_priv 为 NULL 时，表示限制mysqld不允许导入或导出。
   secure_file_priv 为 /tmp 时，表示限制mysqld只能在/tmp目录中执行导入导出，其他目录不能执行。
   secure_file_priv 没有值时，表示不限制mysqld在任意目录的导入导出。
   
   又因为 secure_file_priv 参数是只读参数，不能使用set global命令修改。
   
   修改   my.cnf 文件：
   
    secure_file_priv=' '
   
   mysql> show global variables like '%secure_file_priv%';
   
   +------------------+-------+
   
   | Variable_name  | Value |
   
   +------------------+-------+
   
   | secure_file_priv |    |
   
   +------------------+-------+
   
   1 row in set (0.01 sec)
   
   mysql> select * from test.student 
          into outfile '/kittod/yujma/file.txt' 
          FIELDS TERMINATED BY '"' 
          LINES TERMINATED BY '?';  
   Query OK, 11 rows affected (0.01 sec)
   ```
   
   
   
   ### 数据库恢复：
   
   ```mysql
   数据库恢复是指以备份为基础，与备份相对应的系统维护和管理操作。
   
   系统进行恢复操作时，先执行一些系统安全性的检查，包括检查所要恢复的数据库是否存在、数据库是否变化及数据库文件是否兼容等，然后根据所采用的数据库备份类型采取相应的恢复措施。
   
   数据库恢复机制设计的两个关键问题是：第一，如何建立冗余数据；第二，如何利用这些冗余数据实施数据库恢复。
   
   建立冗余数据最常用的技术是数据转储和登录日志文件。通常在一个数据库系统中，这两种方法是一起使用的。
   
   数据转储是 DBA 定期地将整个数据库复制到磁带或另一个磁盘上保存起来的过程。这些备用的版本成为后备副本或后援副本。
   
   可使用 LOAD DATA…INFILE 语句来恢复先前备份的数据。
   
   【实例】将之前导出的数据备份文件 file.txt 导入数据库 test_db 的表 tb_students_copy 中，其中 tb_students_copy 的表结构和 tb_students_info 相同。
   
   首先创建表 tb_students_copy，输入的 SQL 语句和执行结果如下所示。
   
   mysql> create table test_student 
   
     -> like student;
   
   mysql> LOAD DATA INFILE '/kittod/yujma/file.txt'
   
     -> into table test.test_student
   
     -> FIELDS TERMINATED BY '"'
   
     -> LINES TERMINATED BY '?';
   
   Query OK, 11 rows affected (0.01 sec)
   
   Records: 11 Deleted: 0 Skipped: 0 Warnings: 0
   ```
   
   
   
   
   
   ```mysql
   1. 查看 mysql 支持的搜索引擎：
   
      mysql> show engines;
   
   ```
   
   





