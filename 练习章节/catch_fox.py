# tup = (2,"python",3.14,True,[1,2],"hello",100,(1,2,3),"666",-9,{"a":1})
# lst = list(tup)
# new_tup = tuple([i for i in lst if not (isinstance(i,str) and type(i) is str)])
# print(new_tup)


import random

def get_fox(n: int) -> int:
    """
    随机生成狐狸初始所在洞口编号
    :param n: 洞口总数量
    :return: 狐狸初始洞口编号，范围 [0, n-1]
    """
    return random.randint(0, n - 1)


def get_vary(fox: int, n: int) -> int:
    """
    获取狐狸移动方向的偏移量
    :param fox: 狐狸当前洞口编号
    :param n: 洞口总数量
    :return: 移动偏移量；在0号洞只能+1，最后一号洞只能-1，中间随机±1
    """
    if fox == 0:
        return 1
    elif fox == (n - 1):
        return -1
    else:
        return random.choice([-1, 1])


def play(n: int, m_times: int, guess: int) -> None:
    """
    抓狐狸游戏主逻辑
    :param n: 洞口总数
    :param m_times: 最多猜测天数/机会次数
    :param guess: 玩家一次性输入的猜测洞口编号（全程固定不变）
    :return: 无返回值，抓到狐狸后结束游戏
    """
    print("---------------抓狐狸小游戏-------------------")
    print()
    print(f"有{n}个洞口，洞口编号0-{n-1}，共有{m_times}次机会")

    fox = get_fox(n)
    for day in range(1, m_times + 1):
        print()
        print(f"第{day}天")

        if guess == fox:
            print(f"你在第{day}天抓到狐狸了,狐狸在{fox}号洞口！")
            return
        else:
            print("猜错了，明天再来！")
            fox += get_vary(fox, n)
    print(f"机会用完了，狐狸最后一次在{fox}号洞！")


if __name__ == "__main__":
    while True:
        try:
            n = int(input("请输入有多少个洞口："))
            m_times = int(input("请输入游戏机会："))
            guess = int(input("请输入洞口编号："))
            if 0 <= guess <= (n - 1):
                break
            else:
                print("请输入正确的洞口范围！")
        except ValueError:
            print("洞的个数,游戏机会和洞口编号是整数！")
    play(n, m_times, guess)


# 郝海东