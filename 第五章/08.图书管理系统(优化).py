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

from datetime import datetime
from abc import ABC, abstractmethod
import json
# 定义图书类
class Book:
    def __init__(self,book_id,book,author,kucun_num,total_num):
        self.book_id = book_id        # 图书编号
        self.book = book              # 图书标题
        self.author = author          # 图书作者
        self.total_num = total_num    # 图书总数量
        self.__kucun_num = kucun_num  # 图书库存数量
        
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

# 定义管理员类
class Admin(Member):
    def __init__(self,member_id,member_name,member_password):
        super().__init__(member_id,member_name,member_password)
        self.vip_level = 999

    def max_borrowed_books(self) -> int:  # 获取最大借书数量（管理员不限量，给一个很大的数）
        return 9999

# 定义借阅记录类
class BorrowedRecord(Book,Member):
    def __init__(self,member_id = None,book_id = None,book = None,borrow_time=None,return_time=None):
        self.member_id = member_id
        self.book_id = book_id
        self.book = book
        self.borrow_time = borrow_time
        self.return_time = return_time

    def max_borrowed_books(self) -> int:  # 借阅记录不参与借书，实现抽象方法使类可实例化
        return 0

# 定义图书管理系统类
class LibrarySystem:
    def __init__(self):
        self.members = {}  # 会员字典，键为会员编号，值为会员对象
        self.books = {}    # 图书字典，键为图书编号，值为图书对象
        self.user:Member = None   # 当前登录用户
        self.borrowed_records = {}  # 借阅记录字典，键为会员编号，值为借阅记录列表对象
        self.load_books()
        self.load_members()
        self.load_borrowed_records()

    # 定义加载图书方法
    def load_books(self):
        with open("第五章/date/book.json","r",encoding="utf-8") as f:
            book_data = json.load(f)
            for book in book_data:
                self.books[book["编号"]] = Book(book["编号"],book["标题"],book["作者"],int(book["库存"]),int(book["总数量"]))
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
                elif member["卡号"].startswith("G"):
                    self.members[member["卡号"]] = Admin(member["卡号"],member["姓名"],member["密码"])
        print("会员数据加载完成")

    # 定义加载借阅记录方法
    def load_borrowed_records(self):
        with open("第五章/date/borrowed_records.json","r",encoding="utf-8") as f:
            record_data = json.load(f)
            for record in record_data:
                self.borrowed_records[record["会员编号"]] = BorrowedRecord(record["会员编号"],record["图书编号"],record["图书标题"],record["借阅时间"],record["还书时间"])
        print("借阅记录数据加载完成")

    # 定义更新book.json文件方法
    def update_book_json(self):
        book_data = []  # 收集所有图书，构造成列表
        for book in self.books.values():
            book_data.append({
                "编号": book.book_id,
                "标题": book.book,
                "作者": book.author,
                "库存": book.get_kucun_num(),
                "总数量": book.total_num
            })
        # 循环外统一写一次文件（"w"覆盖）
        with open("第五章/date/book.json", "w", encoding="utf-8") as f:
            json.dump(book_data, f, ensure_ascii=False, indent=2)
        print("图书数据更新完成")

    # 定义更新borrowed_records.json文件方法
    def update_borrowed_records_json(self):
        record_data = []  # 收集所有借阅记录
        for record in self.borrowed_records.values():
            record_data.append({
                "会员编号": record.member_id,
                "图书编号": record.book_id,
                "图书标题": record.book,
                "借阅时间": record.borrow_time,
                "还书时间": record.return_time
            })
        # 循环外统一写一次文件（"w"覆盖）
        with open("第五章/date/borrowed_records.json", "w", encoding="utf-8") as f:
            json.dump(record_data, f, ensure_ascii=False, indent=2)
        print("借阅记录数据更新完成")
    # 定义添加图书方法
    def add_book(self):
        book_id = input("请输入图书编号：")
        # 先判断图书编号是否存在
        if book_id in self.books:
            print("图书编号已存在")
            return
        book = input("请输入图书标题：")
        author = input("请输入图书作者：")
        kucun_num = int(input("请输入图书库存："))
        total_num = int(input("请输入图书总数量："))
        book = Book(book_id,book,author,kucun_num,total_num)
        self.books[book_id] = book  # 新书加入书库字典
        print(f"图书 {book.book} 已成功添加！")
        # 更新本地文件
        self.update_book_json()
        

    # 定义删除图书方法
    def delete_book(self):
        # 先展示所有图书信息
        print("当前书库图书有：")
        self.show_all_books()

        book_id = input("请输入要删除的图书编号：")
        # 先判断图书是否存在
        if book_id not in self.books:
            print("图书不存在")
            return
        print(f"图书 {self.books[book_id].book} 已成功删除！")
        del self.books[book_id]
        # 更新本地文件
        self.update_book_json()

    # 定义修改图书信息方法
    def modify_book(self):
        book_id = input("请输入要修改的图书编号：")
        # 先判断图书是否存在
        if book_id not in self.books:
            print("图书不存在")
            return
        book = self.books[book_id]
        # 先展示当前图书信息
        print(f"当前图书信息：编号：{book.book_id}，书名：{book.book}，作者：{book.author}，可借阅数量：{book.get_kucun_num()}，总数量：{book.total_num}")

        book.book_id = input("请输入新的图书编号(不填写不修改)：") or book.book_id
        if book.book_id != book_id and book.book_id in self.books:
            print("图书编号已存在")
            return
        book.book = input("请输入新的图书标题(不填写不修改)：") or book.book
        book.author = input("请输入新的图书作者(不填写不修改)：") or book.author
        book.total_num = int(input("请输入新的图书数量(不填写不修改)：") or book.total_num)
        # 编号若被修改，同步更新字典的键
        if book.book_id != book_id:
            del self.books[book_id]
            self.books[book.book_id] = book
        print(f"图书 {book.book} 已成功修改！")
        # 再将图书信息写入文件
        self.update_book_json()
        

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
                    print(f"欢迎，{self.members[member_id].member_name}!")
                    # 判断是否为会员
                    if self.members[member_id].member_id.startswith("S"):
                        print(f"尊贵的VIP会员，会员等级为：{self.members[member_id].vip_level}！")
                    elif self.members[member_id].member_id.startswith("N"):
                        print("尊贵的会员")
                    else:
                        print("尊敬的管理员")
                    self.user = self.members[member_id]
                    return True
                else:
                    print("密码错误")
                    continue
        

    # 定义借书方法
    def borrow_books(self):
        # 先展示所有图书信息
        self.show_all_books()
            
        book_id = input("请输入要借阅的图书编号：")
        # 先判断图书是否存在
        if book_id not in self.books:
            print("图书不存在,请检查图书编号")
        else:
            if self.user.borrowed_books(self.books[book_id]):
                self.borrowed_records[self.user.member_id] = BorrowedRecord(self.user.member_id,book_id,self.books[book_id].book,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),None)
                # 更新本地文件
                self.update_borrowed_records_json()

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
            if self.user.return_books(self.books[book_id]):
                # 找到该会员的借阅记录，更新还书时间
                self.borrowed_records[self.user.member_id].return_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # 更新本地文件
                self.update_borrowed_records_json()

            
            

    # 定义查看已借阅图书方法
    def show_borrowed_books(self):
        if len(self.user.get_borrowed_books()) == 0:
            print("您当前没有借阅任何图书")
        else:
            print("您当前借阅的图书有：")
            for book in self.user.get_borrowed_books():
                print(f"编号：{book.book_id}，书名：{book.book}，作者：{book.author}")

    # 定义查看所有图书方法
    def show_all_books(self):
        if len(self.books) == 0:
            print("当前书库没有图书")
        else:
            print("当前书库图书有：")
            for book in self.books.values():
                print(f"编号：{book.book_id}，书名：{book.book}，作者：{book.author}，可借阅数量：{book.get_kucun_num()}，总数量：{book.total_num}")

    # 定义查看所有会员方法
    def show_all_members(self):
        if len(self.members) == 0:
            print("当前书库没有会员")
        else:
            print("当前书库会员有：")
            for member in self.members.values():
                print(f"卡号：{member.member_id}，姓名：{member.member_name}，密码：{member.get_member_password()}，会员等级：{getattr(member, 'vip_level', 1)}")

    # 定义查看借阅记录方法
    def show_borrowed_records(self):
        if len(self.borrowed_records) == 0:
            print("当前没有任何借阅记录")
        else:
            print("当前借阅记录有：")
            for record in self.borrowed_records.values():
                print(f"会员编号：{record.member_id}，图书编号：{record.book_id}，书名：{record.book}，借阅时间：{record.borrow_time}，还书时间：{record.return_time}")
    
    # 定义运行方法
    def run(self):
        if self.login():
            if self.user.member_id.startswith("G"):
                while True:
                    print("---图书管理系统(管理员)---\n")
                    print("1. 借阅图书")
                    print("2. 归还图书")
                    print("3. 查看已经借阅的图书")
                    print("4. 添加图书")
                    print("5. 修改图书")
                    print("6. 删除图书")
                    print("7. 查看所有图书")
                    print("8. 查看所有会员")
                    print("9. 查看借阅记录")
                    print("10. 退出系统\n")
                
                    choice = input("请输入您要进行的操作：")
                    match choice:
                        case "1":
                            self.borrow_books()
                        case "2":
                            self.return_books()
                        case "3":
                            self.show_borrowed_books()
                        case "4":
                            self.add_book()
                        case "5":
                            self.modify_book()
                        case "6":
                            self.delete_book()
                        case "7":
                            self.show_all_books()
                        case "8":
                            self.show_all_members()
                        case "9":
                            self.show_borrowed_records()
                        case "10":
                            print("谢谢使用！")
                            break
                        case _:
                            print("无效的选择，请重新输入")
            else:
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


   
