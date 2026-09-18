"""
-----------------------------类型注解--------------------------

1.介绍：类型注解是python的一种语法特性，用于明确标识变量，参数，返回值的数据类型，从而使代码更清晰，更安全，
        更容易维护。
2.形式：
    常规定义变量： a = 1
    类型注释定义变量：  a: float = 1
                     s: str = "666"

                     names: list[int | str] = [1,2,3]      | 表示或
                     phones: set[str] = {"13458398736"}
                     goods: dict[str,float] = {"电脑":9999}

3.类型注解只是起到语法提示作用，并不会影响程序运行结果
"""

"""
------------------------------函数的类型注解---------------------

1.为函数添加类型注解，其实就是为函数的参数和返回值参加类型注解，形式与变量添加类型注解一样

2.为函数返回值添加类型注解与之前所学不一样。

def calc(scores: list[int]) -> float:
在上面的定义函数中，分别是对参数与返回值添加的类型注解

def calc(scores: list[int]) -> tuple[int,int,float]:
        函数体
        return 返回值1,返回值2，返回值3
在上面的定义的函数中，注解了它的三个返回值类型，并封装到元组里


"""

# 演示
# 函数添加注释方式
import math
def circle_area_len(r: float) -> tuple[float,float]:
    return round(math.pi * pow(r,2),2),round(math.pi * r * 2,2)

al = circle_area_len(10)
print(al)



# 以上一节19.   为例，添加函数注解
""" 
练习2：定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息
计算订单的总金额。
 具体规则如下：
     ·优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
     ·积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""

def calc_order_cost(*args: tuple[str,float,int],coupon=0,score=0,express=0.0) -> float:
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

total = calc_order_cost(("鼠标",100,2),("键盘",388,1),("iphone",10999,2),coupon=500,score=35892)

print(total)