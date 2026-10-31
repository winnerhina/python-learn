use hhh;
-- DDL
alter table empolyee rename to emp;
alter table emp rename to empolyee;




show tables;
-- DML
insert into empolyee(id, g_id, name, gender, age, idcard, hire_date) values (1,'001','xx','男',20,'123456789012345678','2020-5-5');

insert into empolyee values (2,'002','李麻花','男',44,'198204041234567890','2000-04-04');

insert into  empolyee values (3,'003','大马猴','男',25,'200104041234567890','2014-04-04'),(4,'004','二狗','男',25,'200104041234567890','2014-04-04');

select * from empolyee;

update empolyee set name='强哥',age = 23 where id = 1;

insert into empolyee(id, g_id, name, gender, age) values (5,'005','老赵','男','60');

delete from empolyee where id = 5;

insert into empolyee values (5,'005','王小明','男',28,'110101199003074512','2018-06-15'),(6,'006','赵静','女',24,'320102198506121234','2019-09-01'),(7,'007','陈志强','男',35,'440103199207083456','2015-03-22'),(8,'008','刘洋','男',31,'510104198811245678','2016-11-08'),(9,'009','孙悦','女',26,'370102199501157890','2019-01-30'),(10,'010','周杰','男',42,'420106198709032345','2014-07-19'),(11,'011','吴梦','女',23,'610113199303284567','2020-05-12'),(12,'012','郑凯','男',38,'330106198605196789','2015-10-25'),(13,'013','冯丽','女',29,'230103199108278901','2017-08-03'),(14,'014','韩磊','男',33,'500101198912302345','2016-02-17');

-- DQL

select * from empolyee;

select distinct name as '姓名',age as '年龄',idcard as '身份证号码' from empolyee where age > 10;




-- 分组查询
# 第 1 题 按性别分组，统计每种性别的人数。
select gender as '性别' , count(gender)  from empolyee group by gender;
# 第 2 题 按性别分组，统计每组的平均年龄、最大年龄、最小年龄。
select gender as '性别',max(age),min(age),avg(age) from empolyee group by gender;
# 第 3 题 只统计年龄 ≥ 28 的人，再按性别分组统计人数。
select gender as '性别',count(*) as '人数' from empolyee where age >= 28 group by gender;
# 第 4 题 按性别分组，只保留平均年龄大于 30 的组。
select gender as '性别', avg(age) as '平均年龄' from empolyee group by gender having avg(age) > 30;
# 第 5 题 统计每种性别中，不同年龄的个数（去重计数）。
select gender as '性别', count(distinct age) from empolyee group by gender;
# 附加题 只统计年龄 ≥ 25 的人，按性别分组，只保留人数不少于 5 的组，查询性别和人数。
select gender as '性别', count(age) as '人数' from empolyee where age >= 25 group by gender having count(age) >= 5;





