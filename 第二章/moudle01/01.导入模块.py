"""
----------------------------导入模块---------------------

1.使用模块中的功能时，必须先导入，再使用。

2.导入模块的具体方法：



------------------------------------模块导入完整列表（含代码样例）---------------------------

导入形式                              代码样例                            调用方式

import 模块名                         import random, os                    模块名.功能名    如：random.randint(10, 100)

import 模块名 as 别名                 import random as rd                  别名.功能名      如：rd.randint(10, 100)

from 模块名 import 功能名             from random import randint,choice    功能名           如：randint(10, 100)

from 模块名 import 功能名 as 别名     from random import randint as rint   别名             如：rint(10, 100)

from 模块名 import *                  from random import *                 功能名           如：randint(10, 100)

注意：别名是自己起的，目的为了简化模块名。
"""


# 导入模块--->调用方式：模块名.功能名/别名.功能名
# import random
# for i in range(100):
#     print(random.randint(1,100))


# 导入模块功能---->调用方式：功能名/别名
from random import randint
for i in range(100):
    print(randint(1,100))