"""
------------------------------------面向对象高级-多态(鸭子类型)------------------------------------

1. 类型注解的作用在忽视参数类型报错的情况下只用于提示，没有其他作用。
2. 不关注对象的具体实现，只关注对象的行为。

3. python中的多态不依赖继承关系，而是依赖对象的行为。(C和java里面的多态是依赖正统的继承)


"""

class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


def swim(duck:Duck):   #类型注解的作用在忽视参数类型报错的情况下只用于提示，没有其他作用。
    duck.swimming()

if __name__ == "__main__":  
    swim(Duck("鸭子",1))
    swim(Dog("狗",2))
    swim(Pig("猪",3))

