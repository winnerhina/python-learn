"""
while循环
"""

# # 案例---打印10遍我要看番！
# i = 0
# while i <= 9:
#     print("重要的事情说10遍！我要看番！")
#     i += 1
# else:
#     print("我说完了，你听见了没？")


# # 案例---计算1-100内所有偶数的和
# i = 2
# sum = 0
# while i <= 100:
#     sum += i
#     i += 2
# else:
#     print(f"1-100内所有偶数的和为：{sum}。")

# i = 1
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#         i += 1
#     else:
#         i += 1
# else:
#     print(f"1-100内所有偶数的和为：{sum}。")
#     print("1-100内所有偶数的和为：%s。---%s"% (sum,i))





# # 作业：一月1日是星期一，问2月15日是星期几？星期日用0表示
# day = 1
# i = 1
# while i < 46:
#     day += 1
#     if day >= 7:
#         day = 0
#     i += 1
# else:
#     print(f"除夕是星期{day}")


# # 重力加速度计算
# t = float(input("请输入小球运行了几秒："))
# h = 5 * t
# l = 0.5 * 9.8 * t ** 2
# s = h ** 2 + l ** 2
# import math
# ss = math.sqrt(s)
# print(f"小球距离远点{ss}米。")