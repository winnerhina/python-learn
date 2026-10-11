"""
------------------------------------图书管理系统------------------------------------

【题目】
某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、
图书归还等功能。系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。
你需要使用面向对象编程的思想，设计并实现这个图书管理系统。

【核心功能】
1. 会员登录：会员通过卡号和密码登录系统
2. 借书：会员可以借阅库存中有余量的图书
3. 还书：会员可以归还借阅的图书
4. 查看我的借阅：展示当前会员已经借阅的图书列表
5. 退出系统

【借阅规则】
1. 普通会员最多可借3本
2. VIP会员最多可借 6+VIP等级 本（VIP等级，默认为1）

【注意】
1. 登录成功（卡号和密码均正确）后，才可以访问该系统
2. 图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书

"""

from abc import ABC, abstractmethod
import json
# 定义图书类
class Book:
    def __init__(self,book_id,book,author,total_num):
        self.book_id = book_id        # 图书编号
        self.book = book              # 图书标题
        self.author = author          # 图书作者
        self.total_num = total_num    # 图书总数量
        self.__kucun_num = total_num  # 图书库存数量
        
    def borrow_book(self):  # 借书
        if self.__kucun_num > 0:
            self.__kucun_num -= 1
            return True
        return False

    def return_book(self):  # 还书
        self.__kucun_num += 1
        
    def get_kucun_num(self):  # 获取图书库存数量
        return self.__kucun_num


"""  
     1. 抽象类是一种智能被子类继承的类，它定义了一组方法，但是没有实现。
     2. 子类必须实现这些方法，才能使用抽象类。
     3. python里面的抽象类，需要继承abc模块中的ABC类--->ABC: Abstract Base Class
     
"""

class Member:  # 会员类
    pass

# 定义会员类
class Member(ABC):
    def __init__(self,member_id,member_name,member_password):
        self.member_id = member_id                # 会员编号
        self.member_name = member_name            # 会员姓名
        self.__member_password = member_password  # 会员密码
        self.__borrowed_books = []                # 会员已借阅的图书列表


    def borrowed_books(self,book:Book):  # 会员借书
        # 先判断是否超出最大借书数量
        if len(self.__borrowed_books) >= self.max_borrowed_books():
            print("您已借阅数量已达最大借书数量")
            return False
        
        # 判断图书是否还有库存
        if book.get_kucun_num() == 0:
            print("该图书库存不足")
            return False
        else:
            book.borrow_book()
            self.__borrowed_books.append(book)
            print(f"{self.member_name} 已成功借阅 {book.book} !")
            return True

    def return_books(self,book:Book):  # 会员还书
        # 先判断是否借阅了该图书
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
            print(f"{self.member_name} 已成功还书 {book.book} !")
            return True
        else:
            print("您未借阅该图书")
            return False

    def get_member_password(self) -> str:  # 获取会员密码
            return self.__member_password
    
    def get_borrowed_books(self) -> list:  # 获取会员已借阅的图书列表
        return self.__borrowed_books
        
    @abstractmethod
    def max_borrowed_books(self) -> int:  # 获取最大借书数量
        pass



# 定义普通会员类
class NormalMember(Member):
    def max_borrowed_books(self) -> int:  # 获取最大借书数量
        return 3

# 定义VIP会员类
class VIPMember(Member):
    def __init__(self,member_id,member_name,member_password,vip_level=1):
        super().__init__(member_id,member_name,member_password)
        self.vip_level = vip_level

    def max_borrowed_books(self) -> int:  # 获取最大借书数量
        return 6 + self.vip_level


# 定义图书管理系统类
class LibrarySystem:
    def __init__(self):
        self.members = {}  # 会员字典，键为会员编号，值为会员对象
        self.books = {}    # 图书字典，键为图书编号，值为图书对象
        self.user:Member = None   # 当前登录用户
        self.load_books()
        self.load_members()

    # 定义加载图书方法
    def load_books(self):
        with open("第五章/date/book.json","r",encoding="utf-8") as f:
            book_data = json.load(f)
            for book in book_data:
                self.books[book["编号"]] = Book(book["编号"],book["标题"],book["作者"],book["数量"])
        print("图书数据加载完成")

    # 定义加载会员方法
    def load_members(self):
        with open("第五章/date/member.json","r",encoding="utf-8") as f:
            member_data = json.load(f)
            for member in member_data:
                if member["卡号"].startswith("N"):
                    self.members[member["卡号"]] = NormalMember(member["卡号"],member["姓名"],member["密码"])
                elif member["卡号"].startswith("S"):
                    self.members[member["卡号"]] = VIPMember(member["卡号"],member["姓名"],member["密码"],int(member["会员等级"]))
        print("会员数据加载完成")


    # 定义登录方法
    def login(self):
        while True:
            print("---登录系统---")
            member_id = input("请输入会员卡号：")
            member_password = input("请输入会员密码：")
            # 先判断会员是否存在
            if member_id not in self.members:
                print("会员不存在")
                continue
            else:
                # 再判断密码是否正确
                if self.members[member_id].get_member_password() == member_password:
                    print("登录成功！")
                    print(f"欢迎，${self.members[member_id].member_name}!")
                    # 判断是否为会员
                    if self.members[member_id].member_id.startswith("S"):
                        print(f"尊贵的VIP会员，会员等级为：{self.members[member_id].vip_level}！")
                    else:
                        print("尊贵的会员")
                    self.user = self.members[member_id]
                    return True
                else:
                    print("密码错误")
                    continue
        

    # 定义借书方法
    def borrow_books(self):
        # 先展示所有图书信息
        print("当前书库图书有：")
        for book in self.books.values():
            print(f"编号：{book.book_id}，书名：{book.book}，作者：{book.author}，可借阅数量：{book.get_kucun_num()}，总数量：{book.total_num}")
            
        book_id = input("请输入要借阅的图书编号：")
        # 先判断图书是否存在
        if book_id not in self.books:
            print("图书不存在,请检查图书编号")
        else:
            self.user.borrowed_books(self.books[book_id])

    # 定义还书方法
    def return_books(self):
        # 先展示所有已借阅图书信息
        print("您当前借阅的图书有：")
        for book in self.user.get_borrowed_books():
            print(f"编号：{book.book_id}，书名：{book.book}，作者：{book.author}")

        book_id = input("请输入要还书的图书编号：")
        # 先判断图书是否存在
        if book_id not in self.books:
            print("图书不存在,请检查图书编号")
        else:
            self.user.return_books(self.books[book_id])
            
            

    # 定义查看已借阅图书方法
    def show_borrowed_books(self):
        if len(self.user.get_borrowed_books()) == 0:
            print("您当前没有借阅任何图书")
        else:
            print("您当前借阅的图书有：")
            for book in self.user.get_borrowed_books():
                print(f"编号：{book.book_id}，书名：{book.book}，作者：{book.author}")
    
    # 定义运行方法
    def run(self):
        if self.login():
            while True:
                print("---图书借阅系统---\n")
                print("1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看已经借阅的图书")
                print("4. 退出系统\n")
                choice = input("请输入您要进行的操作：")
                match choice:
                    case "1":
                        self.borrow_books()
                    case "2":
                        self.return_books()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("谢谢使用！")
                        break
                    case _:
                        print("无效的选择，请重新输入")

 





if __name__ == "__main__":
    library = LibrarySystem()
    library.run()


   
