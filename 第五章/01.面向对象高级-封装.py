"""
---------------------------------------面向对象高级-封装-----------------------------------------

1. 封装的定义：封装就是把数据(属性)和方法(函数)捆绑在一起。形成一个独立的单元(类)，并隐藏内部的实现细节，
   只暴露必要的接口(方法)给外部调用。

2.私有属性和私有方法的设置方法
    2.1 私有属性：在类的内部定义的属性，只能在类的内部使用，属性名前加下划线__。
    2.2 私有方法：在类的内部定义的方法，只能在类的内部使用，方法名前加下划线__。
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

if __name__ == "__main__":
    car = Car("usv","Q7","红色","东哥")
    car.start()
    car.drive()
    car.stop()
    print(car.get_owner())
    
