"""
---------------------------------面向对象高级-继承---------------------------------
1. 继承的定义：继承就是把一个类(父类)的属性和方法继承过来，形成一个新的类(子类)。

2. 继承的特征：
    2.1 子类可以继承父类的属性和方法。
    2.2 子类可以重写父类的方法。
    2.3 子类可以添加自己的属性和方法。
    2.4 子类可以调用父类的方法。
  $ 2.5 子类无法直接访问父类的私有属性和方法
        （私有成员仍会继承并存在于实例中，但子类不能以 self.__xxx 直接使用，只能通过父类内部的方法间接访问）。
        可以继承，但不能直接使用父类的私有方法

3. 继承的语法：class 子类(父类):
    方法体
"""

class Car:
    def __init__(self, brand, model, color,owner):
        self.brand = brand  # 品牌(公有属性)
        self.model = model  # 型号(公有属性)
        self.color = color  # 颜色(公有属性)
        self.__owner = owner  # 主人(私有属性)

    def start(self):    # 启动
        print(f"{self.brand} {self.model}正在启动...")

    def drive(self):    # 驾驶
        print(f"{self.__owner}正在驾驶{self.brand} {self.model}中...")
        self.__control_oyo()

    def stop(self):    # 停止
        print(f"{self.brand} {self.model}正在停止...")

    def __control_oyo(self):    # 控制
        print(f"{self.brand} {self.model}正在控制油门...")

    def get_owner(self):    # 获取主人
        return self.__owner[0:1] + "××是这辆车的主人"


# 定义油车类
class OilCar(Car):
    pass

# 定义电车类
class ElectricCar(Car):
    pass

if __name__ == "__main__":
    car = OilCar("usv","Q7","红色","东哥")
    car.start()
    car.drive()
    car.stop()
    print(car.get_owner())
    print(car.brand)
    print(car.model)
    print(car.color)
    # print(car.__owner)
    # print(car.__control_oyo())  # 报错：子类不能直接访问父类的私有方法