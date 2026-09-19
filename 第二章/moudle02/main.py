# 导入模块
import my_fun
# 使用模块功能

print(my_fun.PI)
print(my_fun.NAME)
print(my_fun.log_separator1())
print(my_fun.log_separator2())
print(my_fun.log_separator3())
print(my_fun.log_separator4())

# __all__:是一个模块级别的特殊变量，用于指定 from 模块名 import * 时，会导入那些功能(通配了那些变量)
# 注意：__all__只会影响 from 模块名 import * 这种导入模块与功能的方法