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
# class Car:
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


# # 案例：
# class Car:
#     def __init__(self,brand,name,color,price):
#         self.brand = brand
#         self.name = name
#         self.color = color
#         self.price = price
#         print(f"对象初始化完成！")

#     # 定义实例方法
#     def running(self):
#         print(f"{self.brand}-{self.name}正在高速行驶～")

#     # 定义魔法方法
#     def __str__(self):
#         return f"{self.brand} {self.name} {self.color} {self.price}"

#     def __eq__(self, other):
#         return self.price == other.price and self.brand == other.brand and self.name == other.name
#     def __lt__(self, other):
#         return self.price < other.price

# # 创建对象
# c1 = Car("USV","y7","red",666666)
# c2 = Car("USV","y7","red",666666)
# c3 = Car("BYD","微光","write",100000)

# print(c1)
# print(c2)
# print(c3)

# print(c1 == c2)
# print(c1 == c3)

# print(c1 < c2)
# print(c1 < c3)



"""
-----------------------------实例属性与类属性------------------------

1.属性
属性分为：
    实例属性：实例属性属于每个具体对象的属性，每个对象都是独立的。(各个对象特有的数据)
    类属性：类属性属于类本身的属性，所有实例共享的。(所有对象的共享数据局或配置)

2.实例属性通过  实例对象名.属性的方法操作
  类属性通过  实例类名.属性的方法操作

3.通过实例对象,去查找属性时,会先查找实例属性,若实例属性不存在,再去找类属性.
"""


# # 案例

# class Car:
#     # 定义类属性
#     wheel = 4      #车轮数
#     tax_rate = 0.1      #购置税

#     # 定义实例属性
#     def __init__(self,brand,name,color,price):
#         self.brand = brand
#         self.name = name
#         self.color = color
#         self.price = price
#         self.wheel = 2
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
    
# # 创建对象
# c1 = Car("USV","y7","red",666666)
# print(c1.brand)
# print(c1.wheel)  #通过实例对象,去查找属性时,会先查找实例属性,若实例属性不存在,再去找类属性.



"""
-------------------------------面向对象综合练习---------------------------------

采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过
控制台菜单与用户交互，具体的功能如下：

1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中

2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩

3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩

4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出

5. 展示全部学生成绩：展示出系统中所有学生的成绩

"""


# ================================== 题目细化要求（实现时对照） ==================================
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，
# 通过控制台菜单与用户交互，具体的功能如下：
#
# 1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
#     1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
#     1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
#     1.3 验证成绩范围（0-100分）
#     1.4 创建学生对象并添加到系统
#
# 2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
#     2.1 输入要修改的学生姓名
#     2.2 根据姓名查找该学生，显示该生当前成绩信息
#     2.3 输入新的语文、数学、英语成绩
#     2.4 更新学生成绩数据
#
# 3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
#
# 4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
#     4.1 输出格式为："姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
#
# 5. 展示全部学生成绩：展示出系统中所有学生的成绩


class Student:
    # 定义学生类实例属性
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    # 定义查找学生信息实例方法
    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"

    # 定义修改学生分数实例方法
    def update_score(self,chinese = None,math = None,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:   
            self.english = english


# 定义教学管理系统类
class EduMangement:
    System_version = "1.0"
    System_name = "教务管理系统"


    def __init__(self):
        self.student_list = []
    
    # 实例方法--添加学生信息
    def add_student(self):
        # 输入要添加的学生姓名
        name = input("请输入要添加的学生姓名：")
        # 判断学生是否已存在
        for s in self.student_list:
            if s.name == name:
                print(f"{name}的成绩信息已存在！")
                return
            
        chinese = int(input(f"请输入{name}的语文成绩："))
        math = int(input(f"请输入{name}的数学成绩："))
        english = int(input(f"请输入{name}的英语成绩："))

        # 判断成绩区间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print(f"添加成功：{stu}")
        else:
            print("输入的各科成绩应在0-100之间！")

    # 实例方法--修改指定学生信息
    def update_student(self):
        # 请输入要修改成绩学生的姓名
        name = input("请输入要添加的学生姓名：")
        # 检查学生姓名是否不存在
        for s in self.student_list:
            if s.name == name:
                print(f"当前：{s}")

                chinese = int(input(f"请输入{name}的语文成绩："))
                math = int(input(f"请输入{name}的数学成绩："))
                english = int(input(f"请输入{name}的英语成绩："))
                # 判断成绩区间
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功！")
                    print(f"修改之后：{s}")
                    return
                else:
                    print("输入的各科成绩应在0-100之间！")
                    return
        print(f"未找到{name}学生成绩信息，请先添加！")
                
        #  print(f"{name}的信息与成绩不存在，请先添加！")
            
    # 实例方法--删除指定学生信息
    def del_student(self):
        # 请输入要修改成绩学生的姓名
        name = input("请输入要添加的学生姓名：")
        # 检查学生姓名是否不存在
        for s in self.student_list:
            if s.name == name:
                print(f"即将要删除：{s}")
                self.student_list.remove(s)
                print("删除成功！")
                return
        print(f"未找到{name}学生成绩信息，请先添加！")
                
    # 实例方法--查看指定学生信息
    def find_student(self):
         # 请输入要修改成绩学生的姓名
        name = input("请输入要添加的学生姓名：")
        # 检查学生姓名是否不存在
        for s in self.student_list:
            if s.name == name:
                print(f"{name}学生成绩：{s}")
                return
        print(f"未找到{name}学生成绩信息，请先添加！")

    # 实例方法--查看所有学生信息
    def find_all_student(self):
        if self.student_list:
            print("所有的学生成绩如下：")
            for s in self.student_list:
                print(f"{s}")
        else:
            print(f"未找到任何学生成绩信息，请先添加！")

    # 实例方法--运行教务管理系统
    def run(self):
        print(f"欢迎使用教务管理系统V{EduMangement.System_version}")
        while True:
            print("########################################################################################")
            print(" 1.添加学生成绩  2.修改学生成绩  3.删除学生成绩  4.查看指定学生成绩  5.查看所有学生成绩  6.退出系统 #")
            print("########################################################################################")
            print()

            # 用户输入选择功能
            chioce = input("请根据系统菜单选择要使用的功能(1-6)：")
            # 增加基本的异常处理，使得程序不会崩溃
            try:
                # 选择分支
                match chioce:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.del_student()
                    case "4":
                        self.find_student()
                    case "5":
                        self.find_all_student()
                    case "6":
                        print("已退出系统！")
                        break
                    case _:
                        print("你选择的功能不存在，请按照系统菜单提示输入要使用的功能！")
            except Exception as e:
                print("系统故障，请联系工作人员！",e)







# 测试
if __name__ == "__main__":
    # Student类测试
    # s1 = Student("李白",100,88,66)
    # print(s1)

    # s1.update_score(english = 90)
    # print(s1)


    # EduMangement测试
    # 实例方法必须先创建对象，再用 对象.方法() 调用；直接 类名.方法() 就缺self了
    # edu = EduMangement()
    # edu.add_student()

    # 测试整体运行
    admin = EduMangement()
    admin.run()