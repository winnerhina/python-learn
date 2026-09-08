# # 案例：嵌套循环模拟B战登录（复杂版）
# # 正确的用户名与密码
# ok_acount = "admin"
# ok_password ="666"

# ok_ac = "root"
# ok_pas = "888"

# ok_a = "xxx"
# ok_pa = "000"

# # 判断
# i = 0
# while i < 1:
#     # 用户输入账号与密码
#     acount = input("请输入您的账号：")
#     password = input("请输入您的密码：")
#     if acount != "" or password != "":
#         if acount == ok_acount and password == ok_password:
#             i += 1
#         elif acount == ok_ac and password == ok_pas:
#             i += 1
#         elif acount == ok_a and password == ok_pa:
#              i += 1
#         else:
#             print("你输入的账号或密码有误！")
#     else:
#         print("账号和密码不能为空！")
# else:
#     print(f"尊敬的{acount},欢迎您使用~")


# 优化上述案例----引入关键字break--->只能出现在循环中，结束循环。
#                               出现了break，和while配套的else（正常结束循环才能执行）无法执行
# 案例：嵌套循环模拟B战登录（复杂版）
# 正确的用户名与密码
ok_acount = "admin"
ok_password ="666"

ok_ac = "root"
ok_pas = "888"

ok_a = "xxx"
ok_pa = "000"

# 判断
while True:
    # 用户输入账号与密码
    acount = input("请输入您的账号：")
    password = input("请输入您的密码：")
    if acount != "" or password != "":
        if acount == ok_acount and password == ok_password:
            break #跳出循环
        elif acount == ok_ac and password == ok_pas:
            break #跳出循环
        elif acount == ok_a and password == ok_pa:
            break #跳出循环
        else:
            print("你输入的账号或密码有误！")
    else:
        print("账号和密码不能为空！")
print(f"尊敬的{acount},欢迎您使用~")