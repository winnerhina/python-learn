"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：

1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。

2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。

3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。

4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。

5. 退出购物车
"""

# 定义购物车类
class Shopping:
    def __init__(self,goods,price,num):
        self.goods = goods
        self.price = price
        self.num = num
        print("该商品添加到购物车完成！")

    # 定义实例方法--查询
    def __str__(self):
        return f"商品名称：{self.goods}，商品价格：{self.price}，商品数量：{self.num}。"

    # 定义实例方法--修改
    def update_goods(self,goods,price,num):
        # print(f"当前购物车内商品信息：{self}")
        self.goods = goods
        self.price = price
        self.num = num
        print("商品修改完成！")

# 定义购物车管理系统类
class ShoppingMangement:
    System_version = 1.0
    def __init__(self):
        self.shopping_list = []

    # 定义实例方法--添加购物车
    def add_shopping(self):
        # 输入要添加的商品信息
        goods = input("请输入要添加的商品名称：")
        price = float(input("请输入购商品价格："))
        nums = int(input("请输入商品数量："))
        # 获取所有购物车商品名称
        goods_list = []
        for s in self.shopping_list:
            goods_list.append(s.goods)
        # 判断商品是否存在，存在则增加相应的数量，不存在则添加
        if goods in goods_list:
            print(f"{goods}已存在，故改为{goods}的数量增加{nums}")
            for s in self.shopping_list:
                if goods == s.goods:
                    # 只加数量：直接改属性。nums和s.num都是int，相加仍是int
                    # (不走update_goods：它三个参数都是必填，只传num会TypeError缺参数)
                    s.num = s.num + nums
            print("商品数量增加完成！")
        else:
            goo = Shopping(goods,price,nums)
            self.shopping_list.append(goo)

    # 定义实例方法--修改购物车
    def update_shopping(self):
        # 输入要修改的商品名称
        goods = input("请输入要修改的商品名称：")
        # 判断要修改的商品是否存在
        for s in self.shopping_list:
            if s.goods == goods:
                # 输入要修改的商品其他信息
                price = float(input("请输入购商品价格："))
                num = int(input("请输入商品数量："))
                s.update_goods(goods,price,num)
                return

        print(f"{goods}尚不存在购物车，请先添加！")
    # 定义实例方法--删除购物车内指定商品
    def del_shopping(self):
        # 输入要删除的商品名称
        goods = input("请输入要删除的商品名称：")
        # 判断要删除的商品是否存在
        for s in self.shopping_list:
            if s.goods == goods:
                self.shopping_list.remove(s)
                print(f"{goods}的信息已删除完毕！")
                return
        print(f"{goods}尚不存在购物车，删除失败！请先添加！")

    # 定义实例方法--查询指定购物车
    def find_shopping(self):
        # 输入要查找的商品名称
        goods = input("请输入要查找的商品名称：")
        # 判断要查找的商品是否存在
        for s in self.shopping_list:
            if s.goods == goods:
                print(f"{s}")
                return

        print(f"{goods}尚不存在购物车，请先添加！")

    # 定义实例方法--查询全部购物车
    def find_all_shopping(self):
        print("购物车内所有商品信息如下：")
        for s in self.shopping_list:
            print(s)

    # 定义实例方法--运行购物车管理系统
    def run(self):
        print(f"欢迎使用购物车管理系统，当前系统版本:V:{ShoppingMangement.System_version}")
        MENU = """
                ############################################################################################################
                # 1.添加商品到购物车  2.修改购物车内商品  3.删除购物车内商品  4.查看购物车内指定商品  5.查看购物车内所有商品  6.退出系统  #
                ############################################################################################################
               """
        while True:
            print()
            print(MENU)
            print()
            # 用户输入
            choice = input("请根据系统菜单选择你要使用的功能(1-6):")
            # 增加基本的异常处理，使得程序不会崩溃
            try:
            # 功能分支
                match choice:
                    case "1":
                        # 添加商品到购物车
                        self.add_shopping()
                    case "2":
                        # 修改购物车内的商品
                        self.update_shopping()
                    case "3":
                        # 删除购物车内商品
                        self.del_shopping()
                    case "4":
                        # 查看购物车内指定商品
                        self.find_shopping()
                    case "5":
                        # 查看购物车内所有商品
                        self.find_all_shopping()
                    case "6":
                        print("欢迎下次使用～")
                        break
                    case _:
                        print("选择功能有误，请根据系统菜单选择你要使用的功能！")
            except Exception as e:
                print("系统故障，请联系工作人员！",e)

# 测试运行
if __name__ == "__main__":
    vip = ShoppingMangement()
    vip.run()