"""
--------------------------------匿名函数--------------------------------

1.介绍：匿名函数是指没有名字的函数，需要通过lambda表达式来声明函数，可以简化简单的函数编写（单行表达式）

2.定义匿名函数：
    lambda 参数列表（可无参数）:函数体

3,调用（使用）
    add = lambda x,y : x + y
    print(add(10,20))

    out_line = lambda : print("----------------------------------------")
    out_line()

4.注意：函数逻辑比较简单（通常一个表达式）且只在一个地方使用时，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）

5.列表操作方法补充：
列表名字.sort(key = 要排序的方法,reverse = False或者True)
                                    是否反转顺序
"""


# # 案例1：打印分割线

# # def out_line():
# #     print("------------------------")

# out_line = lambda : print("---------------------")
# out_line()


# # 案例2：写个加法函数

# # def sum(x,y):
# #     return x + y

# sum = lambda x,y : x + y
# print(sum(10,66))


# # 案例3：把下面列表里面的每个字符串按照字符数冲少到多，从多到时候排序
# str_list = ["c","c++","java","python","Go","666666"]
# print(f"原始顺序：{str_list}")

# str_list.sort(key=lambda item : len(item))  #直接可修改字符串的排序，无返回值
# print(f"字符数量从少到多顺序：{str_list}")

# str_list.sort(key=lambda item : len(item),reverse=True)   #直接可修改字符串的排序，无返回值
# print(f"字符数量从多到少顺序：{str_list}")




# -----------------------------------练习-----------------------------

# 练习1：定义一个函数，根据传入的数字，计算概述紫的阶乘结果

# 方法一：for循环
# def factorial(num):
#     s = 1
#     for i in range(1,num + 1):
#         s *= i
#     return s

# num = int(input("请输入一个数字，系统会计算阶乘："))
# print(f"{num}的阶乘为：{factorial(num)}")


# # 方法二：函数的递归
# # 函数递归（先层层递进，再层层回归）：值得是在函数中，自己调用自己的情况--->一动要有终点，否则会死循环。
# def jc(num):
#     if num == 1:
#         return 1
#     else:
#         return num * jc(num - 1)

# num = int(input("请输入一个数字，系统会计算阶乘："))
# print(f"{num}的阶乘为：{jc(num)}")



""" 
练习2：定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息
计算订单的总金额。
 具体规则如下：
     ·优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
     ·积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""

def calc_order_cost(*args,coupon=0,score=0,express=0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args：商品信息（商品名、价格、数量）---->如:（"鼠标"，188，2）（"键盘"，388，1)
    :param coupon：优惠券
    :param score：积分
    :param express：运费
    :return： 订单的总金额
    """
    # 总金额 = 商品总价 - 优惠券 - 积分优惠 + 邮费


    # 商品总价
    goods_price = [goods[1] * goods[2] for goods in args]
    goods_cost = sum(goods_price)

    # 减去优惠券
    if goods_cost >= 5000 and coupon <= goods_cost:
        goods_cost -= coupon

    # 减去积分优惠
    if goods_cost >= 5000 and score // 100 <= goods_cost:
        goods_cost -= (score // 100)

    # 加上邮费
    total = goods_cost + express

    return total

total = calc_order_cost(("鼠标",188,2),("键盘",388,1),("iphone",10999,2),coupon=500,score=35892)

print(total)

