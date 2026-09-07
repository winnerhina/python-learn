"""
for循环
"""
# # 案例：for循环遍历字符串
# msg = "hello-python"
# for i in msg:
#     print(i)
# else:
#     print("遍历字符串完成！")





# # rang生成指定规则的数字集合
# # 1.用法1---rang(end)----从0生成到end的数字集合（不包含end）
# for i in range(5):
#     print(i)
# # 2.用法2---rang(star,end)----从你指定生成到end的数字集合（不包含end）
# for i in range(6,10):
#     print(i)
# # 3.用法3---rang(star,end,step)----从你指定生成到end的数字集合（不包含end）---step表示步长，每次间隔的个数，默认1
# for i in range(5,100,5):
#     print(i)


# # 计算1-100所有奇数之和
# s = 0
# for i in range(1,101):
#     if i % 2 != 0:
#         s += i
# else:
#     print(f"1-100之间所有奇数之和为：{s}。")

# s = 0
# for j in range(1,101,2):
#     s += j
# else:
#     print(f"1-100之间所有奇数之和为：{s}。")



# # 打印一个长为m，宽为n的长方形
# m = int(input("请输入长方形的长："))
# n = int(input("请输入长方形的宽："))
# for i in range(n):
#     for j in range(m):
#         print("*", end=" ")
#     print()


# # 案例：打印99乘法表------>外侧循环控制行，内侧循环控制列。
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f"{j} * {i} = {i * j}",end="   ")
#     print()
   

