"""
-------------------------------package软件包----------------------------

1.包：本质就是一个文件夹，该文件中包含若干python模块(.py文件)，文件夹下还包含了一个__init__.py的文件

2.作用；模块文件过于多时，用来管理多个模块。(包的本质也是一个模块)

3.注意：一个软件包下一定有一个__init__.py的文件，否则该文件夹就是一个存放.py文件的普通文件夹

4.包的导入方式：

导入形式                            代码样例                                    调用方式

import 包名.模块名                  import utils.my_fun                       包名.模块名.功能名    如：utils.my_fun.log_separator1()

from 包名 import 模块名             from utils import my_fun                  模块名.功能名        如：my_fun.log_separator1()

from 包名 import *                 from utils import *                       模块名.功能名        如：my_fun.log_separator1()

from 包名.模块名 import 功能名       from utils.my_fun import log_separator1   功能名              如：log_separator1()

from 包名.模块名 import *           from utils.my_fun import *                功能名              如：log_separator1()

5.__init__.py一般啥都不写，它所在的文件夹就是一个包了。一般这里面是描述标的信息与初始化环境信息。

5.如果要用from 包名.模块名 import * 这种方式导入包下的所有模块，需要再__init__.py文件下添加__all__ = [模块名(不加后缀)]
  控制允许导入的模块列表
"""

__all__ = ["my_fun","my_var"]