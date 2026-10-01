"""
------------------------------------------json模块入门--------------------------------------

1.介绍：json是软件开发中最常用的数据交换格式，它是一种轻量级的数据交换格式，易于阅读和编写，同时也易于机器解析和生成。
        为了简化json的解析和生成过程，python提供了json模块，用于处理json数据的解析和生成。

2.导入json模块：
        import json

3.存入json数据：----------序列化
        # 定义一个字典(或者已存在的，要存储的json数据)
        data = {"name":"张三","age":18,"gender":"男"}
        # 打开文件
        with open("json_data.json","w",encoding="utf-8") as f:
            # 写入json数据
            json.dump(data, f, ensure_ascii=False, indent=4)

            ensure_ascii=False：=False表示不使用转义字符，直接使用中文字符
            indent=4：=4表示缩进4个空格，使json数据更易读

4.读取json数据：----------反序列化
        # 打开文件
        with open("json_data.json","r",encoding="utf-8") as f:
            # 读取json数据
            data = json.load(f)
            # 打印json数据
            print(data)
"""

# 案例：
import json


# # 要储存为json文件的数据
# user = {"name":"张三",
#         "age":18,
#         "gender":"男",
#         "address":"北京市海淀区",
#         "email":"zhangsan@example.com",
#         "phone":"13800000000",
#         }

# # 存储为json文件
# # ensure_ascii=False：=False表示不使用转义字符，直接使用中文字符
# # indent=4：=4表示缩进4个空格，使json数据更易读
# with open("第三章/resources/user.json","w",encoding="utf-8") as f:
#     json.dump(user, f, ensure_ascii=False, indent=4)

# 读取json文件
with open("第三章/resources/user.json","r",encoding="utf-8") as f:
    # 读取json数据
    data = json.load(f)
    # 打印json数据
    print(data)