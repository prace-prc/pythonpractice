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
#
# class ParentClass:
#     def __init__(self):
#         self.name = 'parent'
#         self.number = 10
#
#     def __str__(self):
#         return f'ParentClass Name : {self.name}, number : {self.number}'
#
#     def add_num(self, new_number):
#         print('부모 : ', new_number, '만큼 더해야지')
#         self.number = self.number + new_number
#
#
# class ChildClass(ParentClass):
#     def __init__(self):
#         super().__init__()
#         self.name = 'child'
#
#     def __str__(self):
#         return f'ChildClass Name : {self.name}, number : {self.number}'
#
#     def add_num(self, new_number):
#         print('자식 : ', '고정적으로 5 더할거야')
#         self.number = self.number + 5
#
#
# parent = ParentClass()
# child = ChildClass()
# print(parent)
# print(child)
# print('--------')
#
# print('7을 더하세요')
# parent.add_num(7)
# child.add_num(7)
# print(parent)
# print(child)
#
# from datetime import timedelta, datetime
# from datetime import date
#
# td = timedelta(days=10)
# print(td)
#
# d1 = date(year=2023, month=5, day=5)
# d2 = date(year=2023, month=6, day=9)
#
# # 날짜의 연산자 오버로딩으로 비교 가능
# print(d1 == d2)
# print(d1 < d2)
# print(d1 > d2)
#
# dt = datetime.today()
#
# formatted_datetime = dt. strftime('%B, %d, %Y')
# print(formatted_datetime)
#
# # 파일 읽기
# file_object = open('example.txt', 'r')
#
# content = file_object.read()
#
# print(content)
#
# file_object.close()
#
# # 파일 쓰기
# file_object = open('new_example.txt', 'w')
#
# content = "This is a new file.\nPython is fun!"
#
# file_object.write(content)
#
# file_object.close()
#
# # 파일 관리
# print("파일 열기")
# file_object = open('example.txt', 'r')
#
# print("현재 파일 위치 확인")
# position = file_object.tell()
# print("Current Position:", position)
#
# print("파일 포인터 위치 이동")
# file_object.seek(5)
# position = file_object.tell()
# print("New position:", position)
# file_object.close()
#
# # with문 사용(close 사용하지 않아도 됨)
# with open('example.txt', 'r') as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print('>', line.strip())
#
# import os
#
# filename = 'example.txt'
#
# print("파일이 존재하는지 확인하기")
# if os.path.isfile(filename):
#     print(f"{filename}이 존재합니다.")
# else:
#     print(f"{filename}이 없습니다.")
#
# file_object = open('list_example.txt', 'w')
#
# content_list = ["Python", "Java", "C++", "Javascript"]
#
# for item in content_list:
#     print(file_object.tell())
#     file_object.write(item + '\n')
#
# file_object.close()
# 폴더 생성
import os

# current_directory = os.getcwd()
# print(current_directory)
#
# os.mkdir('new_directory')
#
# os.makedirs('patent_directory/child_directory/grandchild_directory')
#
# os.chdir('old directory')
# current_directory2 = os.getcwd()
# print(current_directory2)
#
# with open('example.txt','w' ) as file_object:
#     file_object.write("Hello, World!")
#
# print('done')
#
# os.rename('new_directory', 'old_directory')
#
# # 폴더 지우기
# import os
#
# # os.rmdir('new_directory')
# os.removedirs('patent_directory/child_directory/grandchild_directory')

for dirpath, dirnames, filenames in os.walk('patent_directory'):
    print(f"디렉터리 경로: {dirpath}")
    print(f"디렉터리 이름: {dirnames}")
    print(f"파일 이름: {filenames}")