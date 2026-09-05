# # 常见的数据类型
# # 整数int
# # 浮点数float
# # 布尔型bool
# # 字符型str

# print(100)
# print(type(100))
# print(3.14)
# print(type(3.14))
# print(True)
# print(type(True))
# print("str")
# print(type("str"))

# # 常见的数据类型--isinstance(数据,数据类型)
# print(isinstance(100,int))
# print(isinstance(100,float))
# print(isinstance(100,bool))
# print(isinstance(3.14,float))
# print(isinstance(3.14,int))
# print(isinstance(True,bool))
# print(isinstance(True,int))
# print(isinstance("str",str))
# print(isinstance("str",int))



# # 字符串
# # 定义字符串的三种方式
# # 1.单引号
# print('hello')
# # 2.双引号
# print("hello")
# # 3.三引号
# print("""尊敬客户：
#         感谢您购买我们的产品
#     您的订单号是：123456，如有问题欢迎联系我们
#     联系电话：13800000000。
# """)




# # 转义字符
# s1 = "hello的意思是\"你好\""
# print(s1)



# # 字符串的拼接
# s1 = "hello"
# s2 = "world"
# print(s1 + s2)

# s3 = "我是世界首富"
# s4 = "我要实现把大模型服务器搬到太空"
# print("马斯克："+ s3 +"，"+s4)



# # 字符串的格式化---方式一:占位符---%s
# name = "李白"
# age = 25
# pro = "诗人"
# print("我的名字是：%s我今年%s岁了，我是一名伟大的%s" % (name,age,pro))

# 字符串的格式化---方式二:---f"内容{变量名/表达式}"
name = "李白"
age = 25
pro = "诗人"
print(f"我的名字是：{name}我今年{age}岁了我是一名伟大的{pro}")
