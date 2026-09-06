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


# 案例---计算1-100内所有偶数的和
i = 2
sum = 0
while i <= 100:
    sum += i
    i += 2
else:
    print(f"1-100内所有偶数的和为：{sum}。")

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
        i += 1
    else:
        i += 1
else:
    print(f"1-100内所有偶数的和为：{sum}。")
    print("1-100内所有偶数的和为：%s。---%s"% (sum,i))