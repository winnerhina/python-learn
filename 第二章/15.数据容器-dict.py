"""
--------------------------------------dict字典-----------------------------------------------

1.字典：python中的字典(dict)，里面储存的是键值对(key:value)类型的数据，可以通过对应的键(key)找到对应的值(value)
2.特点：键值对(key:value)储存，键(key)不可重复，值(value)可修改。
    key不能重复(如果重复，后面的值会覆盖前面的值),key必须得是不可变类型(int str float tuple)


3.定义：
3.1定义字典：
    字典名称 = {key:value,key:value········}
3.2定义空字典：
    字典名称 = {}
    字典名称 = dict()
3.3根据key获取value:
    变量 = 字典名称[key]

注意：字典中value可以使任何类型的数据，而key不能为可变类型(如：不能为list,set,dict)

"""

# # 定义字典---key不能重复(如果重复，后面的值会覆盖前面的值),key必须得是不可变类型(int str float tuple)
# dict1 = {"王林":666,"李慕婉":608,"徐立国":444,"李白":735,"王林":700}
# print(dict1)
# print(type(dict1))

# # 访问字典---通过 键 来访问 值 
# print(dict1["李白"])
# # 修改值
# dict1["李白"] = 750
# print(dict1)



"""
--------------------------------dict常用操作-------------------------------
1.添加  字典名称[key] = value       往指定字典中添加对应的key:value对    和修改方法一样，如果key不存在，则添加，如果存在则是修改。

2.删除  字典名称.pop(key)           删除字典中指定的key，并返回key对应的value
        del 字典名称[key]           删除字典中指定的key:value对

3.修改  字典名称[key] = value       修改字典中key对应的value   和添加方法一样，如果key存在，则修改，如果不存在则是添加。

4.查询   字典名称[key]               根据key获取对应的value
        字典名称.get(key)           根据key获取value值
        字典名称.keys()             获取所有的key
        字典名称.values()           获取所有的value
        字典名称.items()            获取所有的键值对
"""

#--------------------------------dict字典常规操作--------------------------------

dict1 = {"王林":666,"李慕婉":608,"徐立国":444,"李白":735}
print(dict1)

# 1.添加  字典名称[key] = value       往指定字典中添加对应的key:value对
#         和修改方法一样，如果key不存在，则添加，如果存在则是修改。
dict1["赵云"] = 666
print(dict1)

# 2.删除  字典名称.pop(key)           删除字典中指定的key，并返回key对应的value
e = dict1.pop("徐立国")
print(e)
print(dict1)
#         del 字典名称[key]           删除字典中指定的key:value对
del dict1["李慕婉"]
print(dict1)

# 3.修改  字典名称[key] = value       修改字典中key对应的value
#          和添加方法一样，如果key存在，则修改，如果不存在则是添加。
dict1["李白"] = 750

# 4.查询   字典名称[key]               根据key获取对应的value
print(dict1["李白"])
#         字典名称.get(key)           根据key获取value值
print(dict1.get("李白"))
#         字典名称.keys()             获取所有的key
print(dict1.keys())
#         字典名称.values()           获取所有的value
print(dict1.values())
#         字典名称.items()            获取所有的键值对
print(dict1.items())

# 遍历

for k in dict1.keys():               #先获取key，然后通过key查找对应的value，逐个遍历value
    print(f"{k} : {dict1[k]}")

for m in dict1.items():             #先获取所有的key和value，这是一个类似元组的形式，然后逐个按照元组的索引遍历
    print(f"{m[0]} : {m[1]}")

for x,y in dict1.items():           #先获取所有的key和value，这是一个类似元组的形式，然后通过解包来遍历
    print(f"{x} : {y}")   
































#-----------------------------------dict案例------------------------------------

# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 0. 框架：

# ======================= 原版代码（注释保留，供对比） =======================
"""
print("#########################################################")
print("#                                                       #")
print("#                                                       #")
print("#              -----欢迎使用购物车系统-----             #")
print("#                                                       #")
print("#                                                       #")
print("#                     1.添加购物车                      #")
print("#                     2.修改购物车                      #")
print("#                     3.删除购物车                      #")
print("#                     4.查询购物车                      #")
print("#                     5.退出购物车                      #")
print("#                                                       #")
print("#                                                       #")
print("#                                                       #")
print("#########################################################")


shoppings = {}

while True:

    # 0.1 用户输入操作
    user_fa = int(input("请输入您要使用的功能序号(1-5)："))

    # 0.2 判断要进入的功能
    match user_fa:

        # 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        case 1:
            while True:

                # 1.1 输入要填假的商品名称
                key = input("请输入要添加的商品名称：")

                # 1.2 判断要添加的商品是否存在
                if key not in shoppings.keys():
                    prices = float(input(f"请输入{key}价格："))
                    nums = int(input(f"请输入{key}数量"))
                    shoppings[key] = {"price":prices,"num":nums}
                    print(f"{key}信息添加完成，{key}的价格与新数量：{shoppings[key]}")
                    break

                else:
                    print(f"{key}已存在与购物车，如要修改，请按2。")
                    break
                    
        # 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        case 2:
            while True:

                # 2.1 用户输入要修改的商品名称
                key = input("请输入要修改的商品名称：")

                # 2.2 判断商品是否存在购物车
                if key not in shoppings.keys():
                    print("该商品不存在，请重新输入！")
                    break

                else:
                    prices = float(input(f"请输入{key}新价格："))
                    nums = int(input(f"请输入{key}新数量："))
                    shoppings[key] = {"price":prices,"num":nums}
                    print(f"{key}信息修改完成，新价格与新数量：{shoppings[key]}")
                    break

        # 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        case 3:
            while True:
                # 3.1 用户输入要修改的商品名称
                key = input("请输入要删除的商品名称：")

                # 3.2 判断商品是否存在购物车
                if key not in shoppings.keys():
                    print("该商品不存在，无法删除，请重新输入！")
                    break
                else:
                    del shoppings[key]
                    print(f"{key}删除完成！")
                    break

        # 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
        case 4:
            for k in shoppings.keys():
                print(f"{k}的价格与数量：{shoppings[k]}")
                
        # 5. 退出购物车
        case 5:
            print("已成功退出购物车。")
            break

        # 6. 输入有误，重新跳转用户输入操作
        case _:
            print("输入有误，清重新输入！")
"""

# ======================= 原版代码的不足之处 =======================
# 1. 冗余：case 1/2/3 内层的 while True 每条分支都以 break 结尾，循环体只执行一轮，
#    内层循环完全形同虚设，白白增加一层缩进。
# 2. 逻辑缺陷：菜单打印在 while True 之外，一轮操作结束后回到循环开头只提示
#    "请输入功能序号"，用户看不到完整菜单，与"返回1-5操作页面"的预期不符。
# 3. 稳定性缺陷：user_fa = int(input(...)) 直接转换，用户输入非数字（如 abc）时
#    程序直接 ValueError 崩溃，case _ 根本接不住，也谈不上"重新输入"。
# 4. 不符合题目要求：查询功能输出 "{k}的价格与数量：{'price':..,'num':..}"，
#    打印的是原始字典结构；题目要求格式为"商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 错别字两处："已存在与购物车"应为"已存在于购物车"；
#    case _ 提示"输入有误，清重新输入"应为"请重新输入"。
# 6. 代码规范：菜单 15 行 print 重复堆砌，应提成变量统一维护；
#    "请输入{key}数量"提示末尾缺冒号；添加成功的提示语"价格与新数量"用词不当（添加的不是"新"信息）。
# 7. 小冗余：if key not in shoppings.keys() 中的 .keys() 多余，直接写 key not in shoppings 即可。
# =================================================================





# # ======================= 优化后的代码 =======================
# shoppings = {}

# # 菜单提成变量：只维护一处，循环内每轮重新显示
# MENU = """
# #########################################################
# #                                                       #
# #                                                       #
# #              -----欢迎使用购物车系统-----             #
# #                                                       #
# #                                                       #
# #                     1.添加购物车                      #
# #                     2.修改购物车                      #
# #                     3.删除购物车                      #
# #                     4.查询购物车                      #
# #                     5.退出购物车                      #
# #                                                       #
# #                                                       #
# #                                                       #
# #########################################################
# """

# while True:
#     print(MENU)
#     # 先按字符串接收，校验合法再转int，防止输入非数字导致程序崩溃
#     choice = input("请输入您要使用的功能序号(1-5)：")
#     if not choice.isdigit():
#         print("输入有误，请重新输入！")
#         continue
#     user_fa = int(choice)

#     match user_fa:
#         # 1. 添加购物车
#         case 1:
#             key = input("请输入要添加的商品名称：")
#             if key in shoppings:
#                 print(f"{key}已存在于购物车，如要修改，请按2。")
#             else:
#                 price = float(input(f"请输入{key}价格："))
#                 num = int(input(f"请输入{key}数量："))
#                 shoppings[key] = {"price": price, "num": num}
#                 print(f"{key}信息添加完成，价格：{price}，数量：{num}。")
#         # 2. 修改购物车
#         case 2:
#             key = input("请输入要修改的商品名称：")
#             if key not in shoppings:
#                 print("该商品不存在，请重新输入！")
#             else:
#                 price = float(input(f"请输入{key}新价格："))
#                 num = int(input(f"请输入{key}新数量："))
#                 shoppings[key] = {"price": price, "num": num}
#                 print(f"{key}信息修改完成，价格：{price}，数量：{num}。")
#         # 3. 删除购物车
#         case 3:
#             key = input("请输入要删除的商品名称：")
#             if key not in shoppings:
#                 print("该商品不存在，无法删除，请重新输入！")
#             else:
#                 del shoppings[key]
#                 print(f"{key}删除完成！")
#         # 4. 查询购物车：按题目要求格式输出
#         case 4:
#             if not shoppings:
#                 print("购物车为空，快去添加商品吧！")
#             else:
#                 for name, info in shoppings.items():
#                     print(f"商品名称：{name}，商品价格：{info['price']}，商品数量：{info['num']}")
#         # 5. 退出购物车
#         case 5:
#             print("已成功退出购物车。")
#             break
        
#         # 6. 输入有误（含超出1-5的数字），回到菜单重新输入
#         case _:
#             print("输入有误，请重新输入！")



# 注意：break立即结束离他最近的循环
#      continue跳过当前循环的一个轮次
# # =================================================================





















# -------------------------------练习----------------------------


# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
shcool = {}

MENU = """
#####################################################

       -----------欢迎使用教务管理系统-----------

                   1.添加学生信息   
                   2.修改学生信息   
                   3.删除学生信息   
                   4.查询学生信息   
                   5.查询所有学生信息  
                   6.统计班级成绩
                   7.退出系统

#####################################################

"""

   
while True:
    # 0. 用户输入功能
    print(MENU)
    choice = input("请输入要使用的功能(1-5)：")
    # 0.1 判断功能是否存在
    if not choice.isdigit():
        print("输入有误，请重新输入！")
        choice = input("请输入要使用的功能(1-5)：")
        continue
    else:
        user_fa = int(choice)   

    # 0.2 选择要执行的功能
    match user_fa:

        # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        case 1:
            students = input("请输入要添加的学生姓名：")
            if students not in shcool.keys():

                chinese = float(input(f"请输入{students}的语文成绩："))
                math = float(input(f"请输入{students}的数学成绩："))
                english = float(input(f"请输入{students}的英语成绩："))

                shcool[students] = [chinese,math,english]

                print(f"{students}信息录入完成！")
                print(f"{students}的各科成绩为---语文：{chinese},数学：{math},英语：{english}")
            else:
                print(f"{students}的信息已存在，若要修改，请稍后按菜单提示操作！")

        # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        case 2:
            students = input("请输入要修改的学生姓名：")

            if students not in shcool.keys():
                 print(f"{students}的信息不存在，若要添加，请稍后按菜单提示操作！")
            else:
                chinese = float(input(f"请输入{students}的语文成绩："))
                math = float(input(f"请输入{students}的数学成绩："))
                english = float(input(f"请输入{students}的英语成绩："))

                shcool[students] = [chinese,math,english]

                print(f"{students}信息修改完成！")
                print(f"{students}的各科成绩为---语文：{chinese},数学：{math},英语：{english}")
               
            
        # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        case 3:
            students = input("请输入要修改的学生姓名：")
            
            if students not in shcool.keys():
                    print(f"{students}的信息不存在，无法删除！")
            else:
               del shcool[students]
               print(f"{students}信息删除完成！")

        # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        case 4:
            students = input("请输入要查询的学生姓名：")

            if students not in shcool.keys():
                print(f"{students}的信息不存在，无法查询！")
            else:
                y,s,e = shcool[students]
                print(f"{students}的各科成绩为---语文：{y},数学：{s},英语：{e}")

        # 5. 列出所有学生：遍历所有学生信息并输出。
        case 5:
            if not shcool:
                print(f"教务系统里面没有任何学生信息，请先添加吧！")
            else:
                for i in shcool.keys():
                    y,s,e = shcool[i]
                    print(f"{i}的各科成绩为---语文：{y},数学：{s},英语：{e}")

        # 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        # 6里面所有功能为爱实现，我只想想到的是不完整版
        case 6:
            if not shcool:
                print(f"教务系统里面没有任何学生信息，请先添加吧！")
            else:
                # 6.1 收集：三科成绩列表（shcool[i] = [语文,数学,英语]）
                y_list = [sc[0] for i,sc in shcool.items()]      # 语文
                s_list = [sc[1] for i,sc in shcool.items()]      # 数学
                e_list = [sc[2] for i,sc in shcool.items()]      # 英语
                # 458-460为自己学习书写

                # 6.2 找并列极值的学生：遍历筛选（index()只返回第一个，同分会漏人）
                #     scores[0]=语文 scores[1]=数学 scores[2]=英语，'、'.join(列表)把名字用顿号连起来
                y_max, y_min = max(y_list), min(y_list)

                y_best = [n for n, sc in shcool.items() if sc[0] == y_max]
                # 解包  n = 字典中的key，  sc = 字典中的value(单人各科成绩列表)
                y_worst = [n for n, sc in shcool.items() if sc[0] == y_min]
                print(f"语文---最高分：{y_max}（{y_best}），最低分：{y_min}（{y_worst}），平均分：{sum(y_list) / len(y_list):.1f}")

                s_max, s_min = max(s_list), min(s_list)
                s_best = [n for n, sc in shcool.items() if sc[1] == s_max]
                s_worst = [n for n, sc in shcool.items() if sc[1] == s_min]
                print(f"数学---最高分：{s_max}（{s_best}），最低分：{s_min}（{s_worst}），平均分：{sum(s_list) / len(s_list):.1f}")

                e_max, e_min = max(e_list), min(e_list)
                e_best = [n for n, sc in shcool.items() if sc[2] == e_max]
                e_worst = [n for n, sc in shcool.items() if sc[2] == e_min]
                print(f"英语---最高分：{e_max}（{e_best}），最低分：{e_min}（{e_worst}），平均分：{sum(e_list) / len(e_list):.1f}")
                    

        # 7. 退出系统。
        case 7:
            print("bye~")
            break

        # 8. 输入错误
        case _:
            print("功能选择输入有误，请重新输入！")

            











