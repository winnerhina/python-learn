"""
---------------------------------------------案例------------------------
"""

# # 1. 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。

# def triangle(di,gao):
#     return round(di * gao / 2, 1)

# di,gao = input("请输入三角形的底长与高：").split(",")
# print(f"三角形的面积为：{triangle(float(di),float(gao))}")



# # 2. 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。

# def statistics(zi):
#     zi1 = zi.upper()
#     return zi1.count("A") + zi1.count("E") + zi1.count("I") + zi1.count("O") + zi1.count("U")

# zi = input("请输入一串字符串：")
# print(f"该字符串里面的元音字母数量为：{statistics(zi)}")



# 3. 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。

def statictics(students):
    return max(students),min(students),round(sum(students) / len(students),1)

students = []
students = []
chengji = input("请输入学生们的高考成绩（用逗号分隔）：").split(",")
for i in chengji:
    students.append(float(i))
ma,mi,avg = statictics(students)
print(f"最高分：{ma}，最低分：{mi}，平均分：{avg}")