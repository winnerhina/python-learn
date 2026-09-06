# # if----模拟B站登录功能
# # 正确的账号与密码
# ok_account = "1888888"
# ok_password = "666888"
# # 提示用户输入账号与密码
# account = input("请输入您的账号：")
# password = input("请输入您的密码：")
# # 如果账号与密码均正确，登录陆成功
# if account == ok_account and password == ok_password:
#     print("欢迎使用，祝您有美好的一天！")
# # 如果账户或密码有一者不对，提示失败
# if account != ok_account or password != ok_password:
#     print("账号或密码输入有误，请重新输入！！")


# # if---else--模拟B站登录功能
# # 正确的账号与密码
# ok_account = "1888888"
# ok_password = "666888"
# # 提示用户输入账号与密码
# account = input("请输入您的账号：")
# password = input("请输入您的密码：")
# # 如果账号与密码均正确，登录陆成功
# if account == ok_account and password == ok_password:
#     print("欢迎使用，祝您有美好的一天！")
# # 否则（如果账户或密码有一者不对，提示失败）
# else:
#     print("账号或密码输入有误，请重新输入！！")


# # 输入年份判断是平年还是闰年--非整百年份且能被4整除，或者整百年份能被400整除
# # 输入年份
# year = int(input("请输入年份："))
# # 执行判断
# if (year % 100 != 0 and year %4 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")


# #if--elif(可出现多次)---else
# # 判断一个输入的数字是正数还是负数
# num = float(input("请输入数字："))
# if num > 0:
#     print(f"{num}是正数！")
# elif num < 0:
#     print(f"{num}是负数！")
# else:
#     print("%s是0！" %(num))

# # 案例--用户登录功能---（admin  666）(root  888)(abc  000)其余全部提示账号或密码错误！
# # 正确的账号有与密码
# ok_acount1,ok_password1 = "admin","666" 
# ok_acount2,ok_password2 = "root","888"
# ok_acount3,ok_password3 = "abc","000"
# # 输入账号与密码
# acount = input("请输入您的账号：")
# password = input("请输入您的密码:")
# # 判断（admin  666）
# if acount == ok_acount1 and password == ok_password1:
#     print("欢迎使用，祝您有美好的一天！")
# # 判断(root  888)
# elif acount == ok_acount2 and password == ok_password2:
#     print("欢迎使用，祝您有美好的一天！")
# # 判断(root  888)
# elif acount == ok_acount3 and password == ok_password3:
#     print("欢迎使用，祝您有美好的一天！")
# # 错误
# else:
#     print("账号或密码错误，请重新输入！")




# # 案例：判断一个三角形的类型  不规则  等边  等腰  构不成
# # 用户输入三边长
# a = int(input("请输入第一个边的边长："))
# b = int(input("请输入第二个边的边长："))
# c = int(input("请输入第三个边的边长："))
# # 判断是否构成
# if a + b > c and a + c > b and b + c > a:
#     # 判断等边
#     if a  == b == c:
#         print("该三角形是等边三角形！")
#     # 判断等腰
#     elif a == b or b == c or a == c:
#         print("该三角形是等腰三角形！")
#     # 判断不规则
#     else:
#         print("改三角形是不规则三角形")
# else:
#     print("构不成三角形！")