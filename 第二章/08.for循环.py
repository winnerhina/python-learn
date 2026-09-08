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
   

# 案例：嵌套循环模拟B战登录（复杂版）
# 正确的用户名与密码
ok_acount = "admin"
ok_password = "666"

ok_ac = "root"
ok_pas =" 888"

ok_a = "xxx"
ok_pa = "000"

# 判断
i = 0
while i < 1:
    # 用户输入账号与密码
    acount = input("请输入您的账号：")
    password = input("请输入您的密码：")
    if acount != "" or password != "":
        if acount == ok_acount and password == ok_password:
            i += 1
        elif acount == ok_ac and password == ok_pas:
            i += 1
        elif acount == ok_a and password == ok_pa:
            i += 1
        else:
            print("你输入的账号或密码有误！")
    else:
        print("账号和密码不能为空！")
else:
    print(f"尊敬的{acount},欢迎您使用~")