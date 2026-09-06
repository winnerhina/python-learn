# # 算数运算符--->  +=  -=  /=  //=  %=  **=  *=
# num = 3
# num += 5
# print(f"num += 5的结果为：{num}")

# num = 3
# num -= 5
# print(f"num -= 5的结果为：{num}")

# num = 3
# num /= 5
# print(f"num /= 5的结果为：{num}")

# num = 3
# num //= 5
# print(f"num //= 5的结果为：{num}")

# num = 3
# num %= 5
# print(f"num %= 5的结果为：{num}")

# num = 3
# num **= 5
# print(f"num **= 5的结果为：{num}")

# num = 3
# num *= 5
# print(f"num *= 5的结果为：{num}")



# 比较运算符----> ==  !=  >  <  >=  <=  



# # 逻辑运算符--->  and  or  not
# #案例1--在键盘上输入一个数，判断是否在10-20之间
# num = float(input("请输入数字："))
# print(f"{num}在10-20之间：",num >= 10 and num <= 20)
#案例2--在键盘上输入一个数，判断是否在不在10-20之间
num = float(input("请输入数字："))
print(f"{num}不在10-20之间：",num <= 10 or num >= 20)