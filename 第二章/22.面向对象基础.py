"""
--------------------------------------01类与对象-------------------------------

1.类的定义：
    需要用到关键字  class

    定义类--（不推荐的方法）
    class 类名：
        pass
    创建对象

    对象名 = 类名()
    对象名.属性名1 = 属性值1
       ·······
2.类型的命名规范---大驼峰命名法，单词首字母大写

3.__dict__是python中用户自定义类实例的一个特殊属性，用于以字典形式储存对象的属性
   print(对象名.__dict__)会将对象当中的所有属性，以字典的形式输出出来。

4，定义类的时候，不推荐动态的来为对象添加属性，类应该是起到模版的作用，在类定义的时候直接添加属性名字

5.定义类时，指定实例对象属性(推荐方法)

    定义类
    class 类名：
        def __init__(self,参数列表)：
            self.属性名 = 参数值
            self.属性名 = 参数值

    创建对象
    对象名(参数列表)

5.1 注意：定义在类的外面的函数叫函数，定义在类里的函数里叫方法
         类的本质还是函数

5.2 __init__:初始化方法，会在对象创建后自动调用，主要用于设置对象的初始状态(设置对象属性)

5.3 self：方法的第一个参数，表示当前创建的实例对象
"""

# # 定义类 ----->不推荐动态的来为对象添加属性，类应该是起到模版的作用。
# class Car:
#     pass

# # 创建对象
# c1 = Car()
# # 动态的来为对象添加属性
# c1.color = "red"
# c1.brand = "USV"
# c1.name = "X5"
# c1.price = 666666
# print(c1)
# print(c1.__dict__)  # 会将对象当中的所有属性，以字典的形式输出出来。




# # 定义类
# #  __init__:初始化方法，会在对象创建后自动调用，主要用于设置对象的初始状态(设置对象属性)
# #  self：方法的第一个参数，表示当前创建的实例对象
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕！对象的属性已成功添加！")

# # 创建对象
# c1 = Car("red","USV","X7",666666)
# print(c1.__dict__)
# c2 = Car("black","宝时捷","E7",88888888)
# print(c2.__dict__)


"""
-------------------------------------实例方法----------------------------------

1.在类中定义实例方法时，与之前学到的函数的函数定义方法一致。

# 定义类
class 类名:
    def __init__(self,形参列表):
        self.属性名 = 属性值
            ······

    # 定义实例方法
    def 方法名(self,形参列表):
        ······
    def 方法名(self,形参列表):
    
# 创建对象
对象名 = 类型(参数列表)
# 调用实例方法
对象名.实例方法名(实参)
"""


# # 案例：
# class Car():
#     def __init__(self,brand,name,color,price):
#         self.brand = brand
#         self.name = name
#         self.color = color
#         self.price = price
#         print(f"对象初始化完成！")

#     # 定义实例方法
#     def running(self):
#         print(f"{self.brand}-{self.name}正在高速行驶～")
#     def total_cost(self,zhekou: float,shuilv: float=0.1) -> float:
#         """
#         该方法用来计算提车最终费用(打折后与税后)
#         :param zhekou: 折扣
#         :param shuilv: 税率
#         :return:提车总费用
#         """
#         total_cost = self.price * zhekou + self.price * shuilv
#         return total_cost

# c1 = Car("BMW","X7","red",666666)   # price必须传数字！传"666666"字符串，total_cost里字符串*float会直接TypeError

# total1 = c1.total_cost(0.9,0.1)
# print(f"提车价格为：{total1}")
# # 默认参数
# total2 = c1.total_cost(0.9)
# print(f"提车价格为：{total2}")

# c1.running()


"""
---------------------------------魔法方法------------------------

1.介绍：魔法方法是指python里面提供以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如：__inin__

2.魔法方法不需要自己主动调用，python会在合适的实际自动调用。

3.常见魔法方法一览：

    魔法方法                             描述

    __init__                           初始化方法

    __str__                            字符串表示的方法(print(对象)时自动调用，返回什么就打印什么)

    __eq__                             比较两个对象是否相等（equal），对应 == 运算符

    __lt__ , __le__ , __gt__ , __ge__  支持比较两个对象的大小(小于(less than)，小于等于(less than or equal)，
                                       大于(greater than)，大于等于(greater than or equal))



"""


# 案例：
class Car():
    def __init__(self,brand,name,color,price):
        self.brand = brand
        self.name = name
        self.color = color
        self.price = price
        print(f"对象初始化完成！")

    # 定义实例方法
    def running(self):
        print(f"{self.brand}-{self.name}正在高速行驶～")

    # 定义魔法方法
    def __str__(self):
        return f"{self.brand} {self.name} {self.color} {self.price}"

    def __eq__(self, other):
        return self.price == other.price and self.brand == other.brand and self.name == other.name
    def __lt__(self, other):
        return self.price < other.price

# 创建对象
c1 = Car("USV","y7","red",666666)
c2 = Car("USV","y7","red",666666)
c3 = Car("BYD","微光","write",100000)

print(c1)
print(c2)
print(c3)

print(c1 == c2)
print(c1 == c3)

print(c1 < c2)
print(c1 < c3)
