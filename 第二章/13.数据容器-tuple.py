"""
----------------------------------------元组----------------------------------------------

为什么要用元组？
    
    列表的特点
         元素可重复，有序，可以修改的
    如果要记录一些信息，而这些信息不能修改，只能查询呢？
         列表就不合适了
         此时可以考虑使用元组，元组与列表最大的不同点在于：
                                                   ### 元组一旦定义完成，就不可修改 ###


    -----------------元组与列表最大的不同点在于：元组一旦定义完成，就不可修改---------------------


    

元组介绍：---元组是不可变的序列，类似于列表，但创建后不可修改。
元组特点：
    1，可以储存不同类型的元素。
    2.元素可以重复，有序，不可修改（支持索引访问，切片）

元组定义：
    元组名称 = (元素1，元素2······)


基本操作：
    count()----统计元素在元组中出现的次数。
    index()----查找某个元素在元组中首次出现的位置，返回索引。


"""


# t1 = (1,2,3,4,5,6,7,8,9,0)

# # 访问索引
# print(t1[0])
# print(t1[-1])

# # 切片
# print(t1[1 : 7 : 2])
# print(t1[ :  : -1])

# # 统计count()
# m = t1.count(5)
# print(m)

# # 查找索引index()
# n = t1.index(6)
# print(n)


# # 注意点：

#     # 1.定义空元组
# t2 = ()
# print(t2)
# print(type(t2))
#     # 2.定义含有一个元素的元组：定义完成之后要加一个逗号，例如：t5 = (1,)
#     #   以下是正确与错误对比
# t3 = (1)
# t5 = (1,)
# print(t3)
# print(type(t3))
# print("----------------------------")
# print(t5)
# print(type(t5))

"""
运行结果对比：

1
<class 'int'>
----------------------------
(1,)
<class 'tuple'>
"""







"""


 -----------------------------------------------元组的解包与组包-----------------------------------------
 
 
 1.组包：将多个值合并到一个容器(列表，元组)中
    # 定义一个元组：即是组包---t1 = (1,2,3)
 2.解包：将容器(列表，元组)解开为独立的元素，分别赋给多个变量。
    # 基础解包：a,b,c = t1------把t1里面有多少个元素，就定义多少个变量，把元素赋值给变量

    # 扩展解包(*)
        t2 = [1,2,3,4]
        a,*b,c = t2  ------->a = 1, b = [2,3], c = 3
        a,*b = t2    ------->a = 1, b = [2,3,4]
        *a,b = t2    ------->a = [1,2,3], b= 4
    注意：在元组解包时，*表示收集所有元素，允许我们处理不确定数量的元素(生成列表，以便下一步处理。)

"""


# # 组包操作
# t1 = (0,1,2,3,4,5,6,7,8,9)
# t2 = 5,7,9,10,2,23,12       # 可以不加括号，但一般建议加上。

# print(t1)
# print(t2)

# # 解包操作
# # 基础解包操作(需要变量数量与容器元素数量一致)
# a,b,c,d,f,e,f,g,h,i = t1
# print(a,b,c,d,f,e,f,g,h,i)


# # 扩展解包(* 可以用来收集剩下的所有元素)
# first,second,*other,last = t1
# print(first,second)
# print(other)
# print(last)
# print()
# print(first,second,other,last)




# # 案例1：a = 10,b = 20,将这两个变量交换数值，然后输出、
# a = 10
# b = 20

# # # 组包
# # t = b,a
# # # 解包
# # a,b = t

# # 合并简化
# a,b = b,a
# print(a,b)
# # 案例2：a = 100,b = 200,c = 300,将这三个变量交换数值，然后输出、

# a = 100
# b = 200
# c = 300

# a,b,c = c,a,b
# print(a,b,c)



# -------------------------练习-----------------------

# 根据提供的学生成绩单，完成以下需求
    # 1.计算每个学生的总分，各科平均分，然后输出
    # 2.统计各科成绩的最低分，最低分，平均分，输出
    # 3.查找成绩优秀(平均分大于90)的学生输出、

students = (
    ("s001","大马猴",85,92,78),
    ("s002","二狗",92,88,95),
    ("s003","张三",78,85,82),
    ("s004","李四",88,79,91),
    ("s005","王五",95,96,89)
)
# 1.计算每个学生的总分，各科平均分，然后输出
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分\t")
for i in students:
    total = i[2] + i[3] + i[4]
    avg = total / 3
    print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t {avg:.1f}")



# 2.统计各科成绩的最低分，最低分，平均分，输出

print("-----------------------------------------------------------------------------------")
print("科目\t最低分\t最高分\t平均分\t")
chineses = []
maths = []
englishs = []
km = ["语文","数学","英语"]

ch_total = 0
ma_total = 0
en_total = 0
# 获取各科成绩的列表---------->可以已使用列表推导式，更简单
for j in students:
    chineses.append(j[2])
    ch_total += j[2]

    maths.append(j[3])
    ma_total += j[3]

    englishs.append(j[4])
    en_total += j[4]

ch_avg = ch_total / 5
ma_avg = ma_total / 5
en_avg = en_total / 5

print(f"{km[0]} \t {min(chineses)} \t {max(chineses)} \t {ch_avg}")
print(f"{km[1]} \t {min(maths)} \t {max(maths)} \t {ma_avg}")
print(f"{km[2]} \t {min(englishs)} \t {max(englishs)} \t {en_avg}")



# 3.查找成绩优秀(平均分大于90)的学生输出、

print("-----------------------------------------------------------------")
print("姓名\t分数\t")
goods = []
for n in students:
    total = n[2] + n[3] + n[4]
    avg = total / 3
    # 列表必须在循环内部创建：append存的是引用，
    # 在循环外创建一个反复复用，goods里所有元素都指向同一个列表
    good = [n[1], avg]
    goods.append(good)

for k in goods:
    if k[1] >= 90:
        print(f"{k[0]} \t {k[1]:.1f} \t")


# ====================== 错误写法对比（原第3部分的写法） ======================
# goods = []
# # 创建每次循环单独的姓名与平均分列表
# good = [1,2]                          # 错误1：在循环外创建，全程序只有一个列表
# for n in students:
#     total = n[2] + n[3] + n[4]
#     avg = total / 3
#     good[0] = n[1]                    # 每轮修改的都是同一个列表的内容
#     good[1] = avg
#     goods.append(good)                # 错误2：append存的是引用！5个位置指向同一个列表
#                                       # 循环结束后，goods = [good,good,good,good,good]
#                                       # 内容全是最后一轮的"王五"，所以打印了5行王五
# for k in goods:
#     if k[1] >= 90:
#         print(f"{k[0]} \t {[k[1]]} \t")  
# =============================================================================










# -------------------------------上述学生成绩案例优化----------------------------------

# 根据提供的学生成绩单，完成以下需求
    # 1.计算每个学生的总分，各科平均分，然后输出
    # 2.统计各科成绩的最低分，最低分，平均分，输出
    # 3.查找成绩优秀(平均分大于90)的学生输出、

students = (
    ("s001","大马猴",85,92,78),
    ("s002","二狗",92,88,95),
    ("s003","张三",78,85,82),
    ("s004","李四",88,79,91),
    ("s005","王五",95,96,89)
)
# 1.计算每个学生的总分，各科平均分，然后输出
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分\t")


# 方式1：
# for i in students:
#     total = i[2] + i[3] + i[4]
#     avg = total / 3
#     print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t {avg:.1f}")

# 方式2：元组解包--可观性更好
for id,name,chinese,mathss,englishss in students:
    total = chinese + mathss + englishss
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {mathss} \t {englishss} \t {total} \t {avg:.1f}")


# 2.统计各科成绩的最低分，最低分，平均分，输出

print("-----------------------------------------------------------------------------------")
print("科目\t最低分\t最高分\t平均分\t")
# 方式1：
# chineses = []
# maths = []
# englishs = []
# km = ["语文","数学","英语"]

# ch_total = 0
# ma_total = 0
# en_total = 0
# # 获取各科成绩的列表---------->可以已使用列表推导式，更简单
# for j in students:
#     chineses.append(j[2])
#     ch_total += j[2]

#     maths.append(j[3])
#     ma_total += j[3]

#     englishs.append(j[4])
#     en_total += j[4]

# ch_avg = ch_total / 5
# ma_avg = ma_total / 5
# en_avg = en_total / 5

# print(f"{km[0]} \t {min(chineses)} \t {max(chineses)} \t {ch_avg}")
# print(f"{km[1]} \t {min(maths)} \t {max(maths)} \t {ma_avg}")
# print(f"{km[2]} \t {min(englishs)} \t {max(englishs)} \t {en_avg}")


# 方式2：---列表推导式
chineses = [i[2] for i in students]
maths = [i[3] for i in students]
englishs = [i[4] for i in students]
km = ["语文","数学","英语"]


print(f"{km[0]} \t {min(chineses)} \t {max(chineses)} \t {sum(chineses) / len(chineses)}")
print(f"{km[1]} \t {min(maths)} \t {max(maths)} \t {sum(maths) / len(maths)}")
print(f"{km[2]} \t {min(englishs)} \t {max(englishs)} \t {sum(englishs) / len(englishs)}")



# 3.查找成绩优秀(平均分大于90)的学生输出、

# 方式1：
# print("-----------------------------------------------------------------")
# print("姓名\t分数\t")
# goods = []
# for n in students:
#     total = n[2] + n[3] + n[4]
#     avg = total / 3
#     # 列表必须在循环内部创建：append存的是引用，
#     # 在循环外创建一个反复复用，goods里所有元素都指向同一个列表
#     good = [n[1], avg]
#     goods.append(good)

# for k in goods:
#     if k[1] >= 90:
#         print(f"{k[0]} \t {k[1]:.1f} \t")


# 方式2：----元组解包(可观性更强)
print("-----------------------------------------------------------------")
print("优秀学生名单(各科平均分大于90)如下")

for id,name,chinese,mathss,englishss in students:
    total =chinese + mathss + englishss
    avg = total / 3
    if avg >= 90:
        print(f"学号：{id}，姓名：{name}")
   