"""
----------------------------------面向对象高级-多态--------------------------------------

1.多态：多态是指同一个方法，具有不同的行为，现象，表现。

2.多态的实现：
    class  Car:
        def __init__(self, brand, model, color,owner):
            self.brand = brand  # 品牌(公有属性)
            self.model = model  # 型号(公有属性)
            self.color = color  # 颜色(公有属性)
            self.__owner = owner  # 主人(私有属性)
        def charge(self):
            print("正在补充燃料...")

    class OilCar(Car):
        def charge(self):
            super().charge()
            print(f"{self.brand} {self.model}正在加油......")
    
    class ElectricCar(Car):
        def charge(self):
            super().charge()
            print(f"{self.brand} {self.model}正在充电......")
    
            
    def charge_car(car:Car):   #参数类型为父类，支持传入任意子类
        car.charge()

    
    # 调用多态方法
    charge_car(oil_car("usv","Q7","红色","东哥"))
    charge_car(electric_car("usv","Q7","红色","东哥"))

    注意：调用多态方法时，同一调用语句，传入对象不同，触发不同行为。

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

# 定义多态方法
def charge_car(car:Car):   #参数类型为父类，支持传入任意子类
    car.charge()
    car.drive()

if __name__ == "__main__":
    # 调用多态方法
    charge_car(OilCar("usv","Q7","红色","东哥"))
    charge_car(ElectricCar("bwm","x5","红色","东哥"))
