-- 数据库定义语言
-- 数据库定义语言（Data Definition Language）是用于创建、修改、删除数据库、表、索引、视图等数据库对象的 SQL 语句。
-- 它是 SQL 语句中的一类，用于定义数据库的结构和行为。


--库操作
    --查询
        -- 看看现在有哪些库
        show databases;
        -- 查看当前数据库
        select database();
    --创建
        -- 新建数据库； 以test为例(if not exists 表示如果数据库不存在才创建，如果存在则不创建，可省略)
        -- 字符集：utf8mb4 支持中文、英文、数字、特殊字符等(默认是utf8mb4，可省略)
        create database if not exists test charset utf8mb4;
    --删除
        -- 删除数据库； 以test为例(if exists 表示如果数据库存在才删除，如果不存在则不删除，可省略)
        drop database if exists test;
    --使用
        -- 使用数据库； 以test为例
        use test;


-- 表操作-查询
    -- 查看当前数据库下的所有表
    show tables;
    --查看表结构； 以hhh为例
    desc hhh;
    --查看指定表的见表语句； 以hhh为例
    show create table hhh;

-- 表操作-创建
    -- 新建表； 以hhh为例
    -- 语法：create table if not exists 表名(
    --     字段名 数据类型 comment '字段注释',
    --     字段名 数据类型 comment '字段注释',
    --     字段名 数据类型 comment '字段注释',
    --     ...
    -- ) comment '表注释';
    create table if not exists hhh(
        id int primary key auto_increment,
        name varchar(20),
        age int
    );

-- 表操作-数据类型
    --数值类型
        --整数类型
          --tinyint    小整数类型，占用1字节，范围-128~127
          --smallint   小整数类型，占用2字节，范围-32768~32767
          --mediumint  中整数类型，占用3字节，范围-68,435,456~68,435,455
          --bigint     大整数类型，占用8字节，范围-2^63~2^63-1
        --浮点数类型
          --float    单精度浮点数类型，占用4字节，范围-3.4028234663852886E+38~3.4028234663852886E+38
          --double   双精度浮点数类型，占用8字节，范围-1.7976931348623157E+308~1.7976931348623157E+308
              double(x,y)
              -- x位总长度（显示位数，不做范围限定），y位小数位  
        --定点数类型
          --decimal(x,y)
          -- x位总长度（范围限定），y位小数位
    --字符类型
        --字符串类型
            --char(x)
            -- x位总长度（固定长度，不足用空格填充）
            --varchar(x)
            -- x位总长度（可变长度，不足不填充）
            --text
            -- 多行字符串类型，占用16字节，范围-0~65,355,535
            --longtext
            -- 多行字符串类型，占用4字节，范围-0~4294967295
    --日期时间类型
        --日期类型
          --date
          -- 日期类型，占用3字节，范围-1000-01-01~9999-12-31
        --时间类型
          --time
          -- 时间类型，占用3字节，范围-00:00:00~23:59:59
        --日期时间类型
          --datetime(主流)
          -- 日期时间类型，占用8字节，范围-1000-01-01 00:00:00~9999-12-31 23:59:59
          --timestamp
          -- 时间戳类型，占用4字节，范围-1970-01-01 00:00:00~2038-01-19 03:14:07

-- 表操作-修改表结构
    -- 添加字段：alter table 表名 add 字段名 数据类型 【comment '字段注释' 约束】;
        alter table hhh add sex char(1) comment '性别';
    -- 修改字段：
        --修改数据类型：alter table 表名 modify 字段名 新数据类型 comment '字段注释';
        alter table hhh modify sex char(1) comment '性别';
        --修改字段名和数据类型：alter table 表名 change 字段名 新字段名 数据类型 【comment '字段注释' 约束】;
        alter table hhh change sex gender int comment '性别';
    --删除字段：alter table 表名 drop 字段名;
    alter table hhh drop sex;
    --修改表名：alter table 旧表名 rename to 新表名;
    alter table hhh rename to hhd;
    --删除表：drop table [if exists] 表名;
    drop table if exists hhd;
    --删除表，并重新该创建：truncate table 表名;
    truncate table hhd;
