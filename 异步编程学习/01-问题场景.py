"""
time 库常用方法：

· time.time()           返回当前时间的时间戳（秒，浮点数），常用于计时
· time.sleep(秒)        让程序暂停指定的秒数（模拟 I/O 等待）
· time.ctime()          时间戳 → 可读字符串，如 'Thu Oct 24 10:30:00 2026'

strftime 常用格式符：
    %Y 四位年份   %m 月份   %d 日   %H 时   %M 分   %S 秒
"""


import time

def task1():
    time.sleep(5)  # 模拟一个耗时 5 秒的 I/O 操作
    return 10


def task2():
    time.sleep(3)  # 模拟一个耗时 3 秒的 I/O 操作
    return 20


def main():
    result = task1()
    print('任务1执行结果:', result)
    result = task2()
    print('任务2执行结果:', result)


if __name__ == '__main__':
    start = time.time()
    main()
    print('总耗时:', time.time() - start)
