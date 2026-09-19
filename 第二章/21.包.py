# 导入包中的模块

# import utils.my_fun
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()
# utils.my_fun.log_separator3()
# utils.my_fun.log_separator4()

# from utils import my_fun
# my_fun.log_separator1()
# my_fun.log_separator2()
# my_fun.log_separator3()
# my_fun.log_separator4()

from utils import *
my_fun.log_separator1()
my_fun.log_separator2()
my_fun.log_separator3()
my_fun.log_separator4()

print(my_var.NAME)
# 导入模块中的功能

# 相对路径---从当前文件所在的目录下开始找
from utils.my_fun import log_separator1
from utils.my_fun import log_separator2
from utils.my_fun import log_separator3
from utils.my_fun import log_separator4

# 绝对路径---从项目的根目录下开始找
from 第二章.utils.my_fun import log_separator1
from 第二章.utils.my_fun import log_separator2
from 第二章.utils.my_fun import log_separator3
from 第二章.utils.my_fun import log_separator4
log_separator1()
log_separator2()
log_separator3()
log_separator4()