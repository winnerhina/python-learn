"""
------------------------------------初识异步编程---------------------------

【核心规则】需要注意的是，为了让事件循环正确地识别和调度任务，我们需要遵循以下两个规则：
1. 首先，创建一个事件循环
   然后，将需要执行的任务注册到事件循环中
   最后，启动事件循环，开始调度和执行各个任务

2. 任务函数定义时，需要使用 `async def` 定义，表示这是一个异步函数，是需要交给事件循环管理的。
   简单理解：普通函数用 `def` 定义，调用即执行；异步函数用 `async def` 定义，调用后不会立刻执行，
   而是交给事件循环去调度。官方文档原话：通过 async/await 语法声明的协程，是编写 asyncio 应用的推荐方式。

3. 在任务函数内部，当遇到需要等待其他异步操作的地方，需要使用 `await`。这就告诉事件循环：
   此处可以挂起当前任务，等异步操作完成后再恢复执行。这样可以避免程序在等待期间白白占用资源，从而提升整体效率。
   简单理解：`await` 就是"挂起信号"，对事件循环说"我现在要等某个操作完成，你先去调度别的任务"。
   等结果返回后，事件循环再回来从挂起点继续往下执行。

   注意：直接调用 async 函数不会执行函数体，必须用 `await` 或包装成任务才会真正运行。
        await 后面的对象必须是 async def 定义的对象，而 sleep 则不是，所以会报错
        例如：
            await time.sleep(5)
            需要切换为 async def 版本的 sleep 函数

【补充：什么是事件循环（Event Loop）】
官方文档把 asyncio 的事件循环比喻成"管弦乐队的指挥"：它不亲自演奏（不做具体工作），
而是协调各个乐手（任务）谁该等、谁该上，从而让整支乐队高效配合地运转。

4.语法（最常用的 4 个）
   · 定义异步函数：`async def 函数名():`（如 async def task1():）
   · 等待异步操作：`await 异步操作`（挂起当前任务，等结果回来再继续）
   · 启动事件循环：`asyncio.run(协程)`（程序入口，负责跑整个异步流程）
   · 异步等待（替代 time.sleep）：`await asyncio.sleep(秒)`（不阻塞事件循环）

   最小可用示例：
   import asyncio

   async def task1():
       await asyncio.sleep(5)   # 模拟耗时 5 秒的 I/O
       return 10

   async def task2():
       await asyncio.sleep(3)   # 模拟耗时 3 秒的 I/O
       return 20

   async def main():
       r1, r2 = await async.gather(task1(),task2())
       print(r1, r2)

   asyncio.run(main())          # 入口：启动事件循环执行 main
"""

import time
import asyncio

async def task1():
    print("task1开始执行！")
    # await 后面的对象必须是 async def 定义的对象，而 sleep 则不是，所以会报错
    # await time.sleep(5)
    # 需要切换为 async def 版本的 sleep 函数
    await asyncio.sleep(5)  # 模拟一个耗时 5 秒的 I/O 操作
    print("task1执行完毕！")
    return 10


async def task2():
    print("task2开始执行！")
    await asyncio.sleep(3)  # 模拟一个耗时 3 秒的 I/O 操作
    print("task2执行完毕！")
    return 20


async def main():
    # 将task1与task2注册到时间循环中
    result = await asyncio.gather(task1(), task2())
    print('任务1与任务2执行结果分别为:', result)


if __name__ == '__main__':
    start = time.time()
    # 创建时间循环，并运行
    asyncio.run(main())
    print('总耗时:', time.time() - start) 