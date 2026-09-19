# 常量(不会发生改变的数据；常量的名称为全部大写)
PI = 3.1415926
NAME = "黑马☆东哥"

# 函数
def log_separator1():
    print("- " * 30)  # 把前面的字符串输出30次

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)


# 测试函数
"""
__name__:是python里面的内置变量，便是当前模块的名字。(直接运行当前模块，__name__的值为："__main__";
         当模块被导入时，__name__的值就是自己模块的名字。)
"""
print(__name__)
if __name__ == "__main__":
    log_separator1()

