# """
# 案例2：猜数字游戏
#     1.系统随机生成一个数字
#     2.用户来猜测，并输入系统
#     3.猜大了，或小了给提示，然后用户重新输入。
#     4.猜对了，结束循环
#     自我附加：用户猜测了几次。
# """

# # 猜数字游戏
# # 系统随机生成数字
# import random
# random_number = random.randint(1,100)
# # 用户输入
# i = 0
# while True:
#     user_number = int(input("系统会生成1-100数字，请您输入猜测结果："))
# # 系统判断，并记录输入次数。
#     if user_number < 1 or user_number > 100:
#         print("猜测的数字是在1-100哦~")
#     elif user_number == None:
#         i += 1
#         print("输入结果不能为空，请重新输入。")
#     elif user_number > random_number:
#         i += 1
#         print(f"您猜大了，您当前已经输入了{i}次哦~")
#     elif user_number < random_number:
#         i += 1
#         print(f"您猜小了，您当前已经输入了{i}次哦~~")
#     elif user_number == random_number:
#         i += 1
#         print(f"恭喜您猜对了，您共猜测了{i}次哦~~")
#         break
# print(f"随机生成的数字是：{random_number}。")


    
