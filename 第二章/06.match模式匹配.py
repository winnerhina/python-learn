"""
match---case---模式匹配
"""

# # 工作日程安排
# # 输入星期几
# day = int(input("请输入星期："))
# # 执行
# match day:
#     case 1:
#         print("周一：工作会议日！")
#     case 2:
#         print("周二：学习培训日！")
#     case 3:
#         print("周三：项目开发日！")
#     case 4:
#         print("周四：代码审查日！")
#     case 5:
#         print("周五：总结规划日！")
#     case 6 | 7:
#         print("周末：今天是休息日哦，好好放松一下吧！")
#     case _:
#         print("输入有误！")






# # 案例：简易计算器--->match---case
# # 用户输入数据
# num1 = float(input("请输入第一个数字:"))
# num2 = float(input("请输入第二个数字:"))
# # 用户输入符号
# symbol = input("请输入要运算的方式：")
# # 判断符号，并执行计算
# match symbol:
#     case "+":
#         s= num1 + num2
#         print(f"{num1}+{num2}={s}")
#     case "-":
#         s= num1 - num2
#         print(f"{num1}-{num2}={s}")
#     case "*":
#         s= num1 * num2
#         print(f"{num1}*{num2}={s}")
#     case "/" if num2 != 0:    #if条件句成立，才会匹配case。
#         s= num1 / num2
#         print(f"{num1}/{num2}={s}") 
#     case _:
#         print("运算符号输入有误，或者被除数为0！")

# print("""
#     注意：match适合用于多个等值匹配
#          if适用于范围匹配
# """)


# 案例：游戏操作读取
# 用户键盘输入
operate = input("请输入游戏操作：")
# 匹配并输出
match operate:
    case "W" | "w":
        print("角色向前移动")
    case "S" | "s":
        print("角色向后移动")
    case "A" | "a":
        print("角色向左移动")
    case "D" | "d":
        print("角色向右移动")
    case "J" | "j":
        print("角色进行攻击！")
    case " ":
            print("角色跳跃！")
    case "ESC":
        print("退出游戏！")
    case _:
          print("操作有误！")
        