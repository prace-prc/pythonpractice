# class Mobile:
#     fp = 'yes'
#
#
# realme = Mobile()
# redme = Mobile()
# geek = Mobile()
#
# print(Mobile.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
#
# Mobile.fp = 'no'
# print(Mobile.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
# print("----------")
# realme.fp = 'Not Working'
# print(Mobile.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
#
# class Vector:
#     def __init__(self, x, y):  # 나 자신을 재정의
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):  # 덧셈 동작을 재정의
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):  # string으로 반환되는 값 재정의, 정의하지 않아도 다른 방식으로 동작(오버라이딩)
#         return f'Vector({self.x}, {self.y})'
#
#
# a = Vector(1, 2)
# b = Vector(3, 4)
# print(a)
# print(b)
# c = a + b
# print(c)
#
#
# class Add:
#     def result(self, a, b):
#         print("Addition:", a + b)
#
#
# class Multi(Add):
#     def result(self, a, b):
#         print("Multiplication:", a * b)
#
#
# m = Add()
# n = Multi()
# m.result(10, 20)
# n.result(10, 20)
#
# # 날짜와 시간
# import time
#
# print(time.time())
# print(time.ctime())
#
# from datetime import datetime, date
#
# dt = datetime(year=2023, month=5, day=5, hour=10, minute=30)
# print(dt)
# print(type(dt))
#
# current_time = time.ctime()
# current_datetime = datetime.now()
#
# print(current_datetime, current_time)
#
# d = date(year=2023, month=6, day=25)
# print(d)
#
# current_date = date.today()
# print(current_date)

class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.number = 10

    def __str__(self):
        return f'ParentClass Name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('부모 : ', new_number, '만큼 더해야지')
        self.number = self.number + new_number


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.name = 'child'

    def __str__(self):
        return f'ChildClass Name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('자식 : ', '고정적으로 5 더할거야')
        self.number = self.number + 5


parent = ParentClass()
child = ChildClass()
print(parent)
print(child)
print('--------')

print('7을 더하세요')
parent.add_num(7)
child.add_num(7)
print(parent)
print(child)