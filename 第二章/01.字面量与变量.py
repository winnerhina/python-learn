# #字面量的写法
# print(100)  #整形int
# print(3.14) #浮点型float
# print(True) #布尔型bool
# print("str")#字符型str
#
# #bool类型本身属于int
# print(True + 1)

# #变量     python是动态类型语言，一个变量可以出存不同数据类型（在项目开发中，只推荐一个变量名储存一种类型的数据）
# num1 = 666
# print(num1)


# # 案例
# base = 11.6  #基础播放量
# incr = 50    #每个月增长的播放量
# print("第一个月总的播放量：", base + incr)
# print("第二个月总的播放量：", base + incr * 2)

# #案例--一次性定义多个变量
# base,incr = 11.6,50
# print("第一个月总的播放量：", base + incr)
# print("第二个月总的播放量：", base + incr * 2)


# 案例 a = 100 b = 200 c =300,将啊a b c的值分别赋予c a b 
a,b,c = 100,200,300
print("原始数据：",a,b,c)
d = a
a = c
c = b
b = d
print("交换数据后：",a,b,c)
