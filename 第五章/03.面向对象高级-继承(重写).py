"""
----------------------------------面向对象高级-继承(重写)----------------------------------

1. 重写：子类继承父类之后，如果父类中的方法不满足子类的需求，子类可以重写父类的方法（方法名字相同，参数相同，返回值相同）。
    重写后的方法，会(变相，不是真的覆盖)覆盖父类的方法。子类对象调用方法时，会调用子类的方法。

2. 如果子类在重写父类方法时，需要调用父类的方法，可以使用父类名.方法名(self)调用或者super().方法名()调用。
    注意：父类名.方法名(self)调用或者super().方法名()要调用时，写在子类重写的方法中


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

    def charge(self):    # 充电
        print(f"{self.brand} {self.model}正在补充燃料...")


# 定义油车类
class OilCar(Car):
    def charge(self):
        super().charge()
        print(f"{self.brand} {self.model}正在加油......")

# 定义电车类
class ElectricCar(Car):
    def charge(self):
        Car.charge(self)
        print(f"{self.brand} {self.model}正在充电......")


if __name__ == "__main__":

    oil_car = OilCar("usv","Q7","红色","东哥")
    oil_car.charge()
    electric_car = ElectricCar("usv","Q7","红色","东哥")
    electric_car.charge()