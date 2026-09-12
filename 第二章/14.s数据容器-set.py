"""
------------------------------------------set集合---------------------------------------------
1.介绍：集合是一种无序的，不可重复的，可修改的数据容器。
2.定义：s = {1,2,3}     
    空集合 s = set()
    不可以 s = {}------这是空字典
3.由于集合是无序的，所以集合不支持索引访问，输出结果也是不会按照你输入的顺序的。
4.由于集合是不可重复的，你输入的数据有重复，输出不会有重复的元素
"""

# # 定义
# s1 = {0,6,5,4,3,2,2,9,7,8,0,6,1}
# print(s1)
# print(type(s1))


"""
--------------------------------------set常见方法-------------------------------------------------
1.add()：添加元素到集合里面
2.remove()：移除集合当中指定元素(指定元素不存在将报错)
3.pop()：随机删除集合中的元素并返回
4.clear()：清空集合内的元素
5.difference() == -：求两个集合的差集(包含第一个集合，但不包含在第二个集合中的元素)
6.union() == |：求两个集合的并集 
7.intersection() == &：求两个集合的交集
"""

# # 操作方法
# s1 = {1,2,3,4,5,6,7,8,9,0}
# print(s1)
# # 1.add()：添加元素到集合里面
# s1.add(11)
# print(s1)
# # 2.remove()：移除集合当中指定元素(指定元素不存在将报错)
# s1.remove(0)
# print(s1)
# # 3.pop()：随机删除集合中的元素并返回
# e = s1.pop()
# print(e)
# print(s1)
# # 4.clear()：清空集合内的元素
# s1.clear()
# print(s1)


# s2 = {"A","B","C","D","F","G"}
# s3 = {"X","C","V","B"}
# # 5.difference() == -：求两个集合的差集(包含第一个集合，但不包含在第二个集合中的元素)
# print(s2.difference(s3))
# print(s3.difference(s2))
# # 6.union() == |：求两个集合的并集
# print(s2.union(s3))
# print(s3.union(s2))
# # 7.intersection() == &：求两个集合的交集
# print(s2.intersection(s3))
# print(s3.intersection(s2))


# -------------------------------------set案例-----------------------------
# 案例：
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1.找出同时选修法语和艺术的学生
# 方式一：
print(f"同时选修法语和艺术的学生：{french_set.intersection(art_set)}")
# 方式二：---> & 交集符号(逻辑与)
print(f"同时选修法语和艺术的学生：{french_set & art_set}")

# 2.找出同时选修了所有4门课的学生
s1 = french_set.intersection(art_set)
s2 = football_set.intersection(basketball_set)
print(f"选修了所有课程的学生：{s1.intersection(s2)}")

# 3，找出选修了足球，但没选选修篮球的学生
# 方式一：
print(f"选修了足球，但没选选修篮球的学生：{football_set.difference(basketball_set)}")
# 方式二：----> - 减号
print(f"选修了足球，但没选选修篮球的学生：{football_set - basketball_set}")
# 方式三：集合推导式(和列表推导式语法一样)
fb_set = {s for s in football_set if s not in basketball_set}
print(f"选修了足球，但没选选修篮球的学生：{fb_set}")

# 4.统计每个学生选修的课程数量
# 4.1获取学生名单--方式一：
# all_set = football_set.union(basketball_set).union(french_set).union(art_set)
# 4.1获取学生名单--方式二：---交集符号 |
all_set = football_set | basketball_set | french_set | art_set
# 4.2获取选课次数，用列表来统计次数
all_list = [*football_set, *basketball_set, *french_set, *art_set]
print(all_set)
# 4.3判断名字出现几次，就是选了几门课
for i in all_set:
    print(f"{i}同学选了{all_list.count(i)}门选修课。")


# 注意：& 求交集     | 求并集     - 求差集

