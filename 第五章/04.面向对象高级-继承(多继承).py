"""
---------------------------------------面向对象高级-多继承-----------------------------------------

1. 多继承的定义：多继承就是一个子类可以继承多个父类(会将对各父类的非私有属性和方法都继承到子类中)。
    多继承的语法：class 子类名(父类名1,父类名2,父类名3...):
        方法体

2.注意：当子类继承多个父类时，会默认优先使用第一个父类的同名属性或方法，可以使用 类名.__mro__属性 或
        类名.mro()方法查看继承顺序。
"""


class Car:
    def __init__(self, brand, model, color,owner):
        self.brand = brand  # 品牌(公有属性)
        self.model = model  # 型号(公有属性)
        self.color = color  # 颜色(公有属性)
        self.__owner = owner  # 主人(私有属性)

    def start(self):    # 启动
        print(f"{self.brand} {self.model}正在启动...")

    def run(self):    # 驾驶
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

# 华为智能驾驶类
class HuaweiAIdriving:
    def __init__(self, verson = "V.1.0"):
        self.verson = verson  # 版本号(公有属性)

    def run(self):    # 运行
        print(f"欢迎使用华为智能驾驶系统{self.verson}，当前系统正在运行...")





"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  核心   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
# bwm类继承自Car类和HuaweiAIdriving类
class BWM(Car,HuaweiAIdriving):
    def __init__(self, brand, model, color, owner,verson = "V.1.0"):   #重写构造方法
        Car.__init__(self,brand, model, color, owner)      # 重写完后，调用Car类的构造方法
        HuaweiAIdriving.__init__(self,verson)      # 重写完后，调用HuaweiAIdriving类的构造方法

    def run(self):    # 重写run方法
        Car.run(self)      # 重写完后，调用Car类的run方法
        HuaweiAIdriving.run(self)      # 重写完后，调用HuaweiAIdriving类的run方法
        
"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  核心   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""


if __name__ == "__main__":
    bwm = BWM("BWM","X5","红色","东哥")
    bwm.run()

    print(BWM.mro())   # 查看继承顺序
        