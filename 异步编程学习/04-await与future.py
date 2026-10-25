"""
-------------------------------深入理解await----------------------------

1. 在 Python 中，await 关键字主要用在 async def 定义的协程函数中，用于暂停协程的执行，
   直到异步操作完成，然后继续执行后续代码。
2. await 关键字后面可以跟 coroutine、future task对象
    2.1 await后面跟coroutine：事件循环暂停当前协程执行，然后继续执行 await 后面的协程对象中的代码
    2.2 当 await 后面的对象换成了 future 对象，则事件循环会挂起当前带有 future 对象的任务，并转到
        其他的任务去执行。我们也可以理解为，await future 时，就是事件循环切换任务的一个时机。
    2.3 当 await 后面的对象换成了 task 对象，则事件循环会挂起当前任务，并转到 临时加入到事件循环里的task 
        对象中的任务去执行。
"""


## await后面跟coroutine：事件循环暂停当前协程执行，然后继续执行 await 后面的协程对象中的代码
# import asyncio
# import time

# async def sub_task():
#     print('sub task')
#     return 100

# async def task():
#     # 暂停当前的 task 执行
#     # 等待 sub_task 执行完毕
#     result = await sub_task()
#     print('task')
#     # 再执行后续代码
#     print('result:', result)

# def demo():
#     asyncio.run(task())

# if __name__ == '__main__':
#     demo()


## await后面跟future对象：事件循环会挂起当前带有 future 对象的任务，并转到其他的任务去执行
# import asyncio

# async def task02():
#     print('task02')
#     return 200

# async def sub_task():
#     print('sub_task')
#     return 100

# async def task01():
#     print('task01')
#     # 注意下面的代码：sleep 内部会执行 await future，此时任务会切换到任务2去执行
#     await asyncio.sleep(3)
#     result = await sub_task()
#     return result

# async def start():
#     result = await asyncio.gather(task01(), task02())
#     print(result)


# if __name__ == '__main__':
#    asyncio.run(start())


"""
￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
-----------------------------await 与 Future 的理解总结----------------------------

1. await 本身不创建 Future，它只是"等"：
   · await 裸协程（await task1()）→ 不包 Future，直接驱动协程跑；
     如果协程内部没有任何 await，就一口气同步跑完，和同步没区别。
   · await sleep() / 网络 I/O → 是它们【内部自己】创建 Future，await 只是等这个 Future。

2. Future 从哪来？两种来源，作用完全不同：
   · Task（Task 继承 Future）：gather() / create_task() / asyncio.run() 自动把协程
     包成 Task → 这才是把协程"注册进事件循环调度"，成为可切换的单元。
   · 普通 Future：sleep() / I/O 内部创建 → 是运行中的任务遇到它"暂停让出"的切换点，
     不是注册新协程。

3. 三组对比（最关键的一课）：
   ① 同步 def 调用             → 8s
   ② await task1(); await task2()（裸协程，无 Future）→ 也是 8s！和同步一模一样
   ③ asyncio.gather(task1(), task2()) → 5s
   省 3 秒的原因：③里 gather 把两个协程包成了 Task/Future，事件循环才有
   "两个可调度的单元"可以来回切换；②里只有一个"人"，切无可切。

4. 结论：
   · 没有 Future，异步 = 同步，事件循环就是摆设（切无可切）。
   · 省时间的功劳记在【gather/create_task 注册】和【sleep/I/O 让出】头上，
     不记在 await 头上。
   · 一句话：注册协程 = 包 Task/Future；让出控制权 = 内部等 Future。

￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
"""
import asyncio, time

async def task1():
    await asyncio.sleep(5)
    return 10

async def task2():
    await asyncio.sleep(3)
    return 20

# ① 同步调用：8s（time.sleep 阻塞 5s → 阻塞 3s）
def sync_main():
    start = time.time()
    time.sleep(5)                   # 同步阻塞，期间什么都做不了
    time.sleep(3)
    print(time.time() - start)      # ~8s

# ② 顺序 await（裸协程，无 Future 包装）：还是 8s！
async def seq_main():
    start = time.time()
    await task1()      # await 只是"等"，没包 Future，照样等满 5s
    await task2()      # 再等 3s
    print(time.time() - start)      # ~8s

# ③ gather（gather 把两个协程包成 Task，Task 就是 Future）：5s
async def conc_main():
    start = time.time()
    await asyncio.gather(task1(), task2())   # 变成 2 个可调度的 Future
    print(time.time() - start)      # ~5s

if __name__ == '__main__':
    sync_main()                     # ① ~8s（同步阻塞）
    asyncio.run(seq_main())         # ② ~8s（顺序 await，和同步一样）
    asyncio.run(conc_main())        # ③ ~5s（gather 并发）

